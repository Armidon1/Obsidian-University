---
tags: [ethl, hacking-exposed-7, hacking-unix, local-access, privilege-escalation, apt, cap5]
capitolo: 5.2
data: 2026-07-04
collegamenti: ["[[ETHL 0x13 - Cap 5.1 Hacking Unix (Remote Access)]]", "[[ETHL 0x12 - Cap 4 Hacking Windows]]", "[[ETHL - SAM (Security Accounts Manager)]]", "[[ETHL - Buffer Overflow e Stack Smashing]]", "[[ETHL - TOCTOU e Race Condition]]", "[[ETHL - SUID e Privilege Escalation]]", "[[ETHL - Rootkit e Persistenza]]"]
---

# Cap 5.2 Hacking Unix (Local Access)

> [!abstract] Scope del capitolo
> Il seguito di [[ETHL 0x13 - Cap 5.1 Hacking Unix (Remote Access)]]: ottenuto un accesso locale (shell da utente qualsiasi), come si sale a **root**. È tutto **privilege escalation** in due famiglie — (1) *attaccare il sistema* (password deboli, symlink, race condition, core file, shared library, kernel flaws) e (2) *sfruttare misconfigurazioni* (permessi, **SUID**, file world-writable) — più il blocco **persistenza / APT** (trojan, sniffer, log cleaning, rootkit del kernel). L'equivalente Unix di gran parte del Cap. 4 Windows: `/etc/shadow` sta a SAM come John the Ripper sta a hashcat.

> [!note] Mappa in tre blocchi
> **Da locale a root: privilege escalation** → (1) *attaccare il sistema* (weak password, symlink, kernel flaws...) e (2) *sfruttare misconfigurazioni* (permessi file/dir, SUID...). **Restare persistenti: APT** → (1) trojan, (2) rootkit, (3) log cleaner. Questa slide si ripete come indice tra i blocchi.

---

## Blocco 1 — Attaccare il sistema

### Password deboli

> [!info] Il problema eterno
> Le password deboli sono un problema senza fine perché gli utenti prendono sempre la via di minor resistenza. I requisiti aiutano solo marginalmente: `P@ssword1` rispetta lunghezza, simboli, maiuscole e numeri ma si cracka probabilmente in <10 secondi. I **dictionary attack** abbattono velocemente le password facili da indovinare.

> [!note] /etc/passwd
> Sette campi separati da `:` — es. `oracle:x:1021:1020:Oracle user:/data/network/oracle:/bin/bash`:
> 1. **username**; 2. **stub della password** (`x` → la vera hash è in `/etc/shadow`); 3–4. **UID** e **GID**; 5. **GECOS** (nome, telefono...); 6. path assoluto della **home**; 7. path assoluto della **shell** di default.

> [!info] passwd vs shadow — a voce
> Perché due file? `/etc/passwd` è **world-readable** (serve a chiunque per mappare UID↔nome), quindi tenerci le hash le esporrebbe a tutti. Le hash sono spostate in `/etc/shadow`, leggibile **solo da root**. La `x` nel campo 2 di passwd è solo il puntatore. Questa separazione è l'analogo Unix del perché su Windows la SAM è protetta da SYSKEY (→ [[ETHL - SAM (Security Accounts Manager)]]).

> [!note] /etc/shadow
> Campi di `vivek:$1$fnfffc$pGteyHdicpGOfffXX4ow#5:13064:0:99999:7:::`:
> 1. **username**; 2. **hash in Modular Crypt Format** `$hash_id$salt$hash$`; 3. ultimo cambio password; 4. giorni minimi prima di poterla cambiare; 5. giorni massimi prima che il cambio sia obbligatorio; 6. giorni di preavviso alla scadenza; 7. giorni dopo la scadenza prima di disabilitare l'account; 8. data di scadenza dell'account (giorni dall'epoch).

> [!info] MCF — a voce
> Il **Modular Crypt Format** `$id$salt$hash` codifica *quale algoritmo* nella `id`: `$1$`=MD5, `$5$`=SHA-256, `$6$`=SHA-512, `$2a/2b/2y$`=bcrypt, `$y$`=yescrypt. Il **salt** rende ogni hash unico anche a parità di password → distrugge le rainbow table e forza il cracking a procedere una password alla volta. È la stessa `crypt()` one-way già vista nel Cap. 4: cifrario/hash usato in modo da essere irreversibile.

> [!note] John the Ripper
> Ottimo tool per crackare hash: gestisce automaticamente l'MCF, facile da configurare ed estendere, buon set di **mangling rules** (deriva varianti da ogni parola del dizionario), estendibile con file di input separati. Uso base: `john --wordlist=<dizionario> <file_password>`.

> [!note] Contromisure password
> "Richiedi password più forti" funziona a metà: se imponi lunghezza, l'utente ripete l'ultima lettera; se metti regex contro le ripetizioni, aggiunge caratteri facili (la data di nascita). Imporre password forti è difficile senza collaborazione dell'utente. Le **passphrase** aiutano potenzialmente ma si aggirano anch'esse (studio Ars Technica 2012: solo marginalmente più sicure per via delle scelte prevedibili).

### Symlink

> [!info] Cos'è il rischio
> I link simbolici sono puntatori da un file a un altro, **trasparenti** ad applicazioni e utenti: scrivere su `temp` o su un symlink a `temp` è indistinguibile dal punto di vista dell'utente. Un attaccante li sfrutta per **ingannare un programma** perché durante l'esecuzione referenzi un file diverso. Creare symlink verso file protetti **non richiede permessi**: `ln -s /etc/shadow ./link_to_shadow` è concesso da utente non privilegiato.

> [!info] Perché è pericoloso — a voce
> I permessi del *symlink* non contano: al momento dell'accesso vengono valutati i permessi del **target**, verificati con l'identità di **chi dereferenzia**. Se un programma **root/SUID** apre il tuo symlink, accede a `/etc/shadow` *come root*. Combinato con una race condition è il classico **TOCTOU** (time-of-check-to-time-of-use): il programma privilegiato controlla un file, poi lo apre; nel mezzo l'attaccante scambia un symlink → il programma opera sul file sbagliato coi suoi privilegi (→ [[ETHL - TOCTOU e Race Condition]]).

> [!note] Contromisure symlink
> Il coding sicuro è la difesa migliore: usare `O_EXCL | O_CREAT` con la `open()` → fallisce con `EEXIST` se il file (o symlink) esiste già, chiudendo la finestra TOCTOU. Attenzione a leggere/scrivere in directory pubblicamente accessibili. Anche le opzioni di mount del filesystem aiutano (`cat /proc/mounts`).

### Race condition

> [!info] Vincere la corsa
> I programmi diventano interessanti quando girano con privilegi elevati. Molti li elevano solo **temporaneamente** → finestra breve in cui l'attaccante può colpire: chi sfrutta il programma in quella finestra **vince la corsa**. Esempio comune: le race condition nella **gestione dei segnali**.

> [!info] Segnali e flusso — a voce
> I **segnali** sono il meccanismo Unix per notificare eventi in modo asincrono (es. `ctrl+z` invia `SIGTSTP` ai processi in foreground). Alterano il flusso di esecuzione: l'attaccante può usarli per **fermare un processo mentre è privilegiato**, o più in generale per deviarne il flusso e renderlo più facile da sfruttare. Il nodo è l'*async-signal-safety*: un handler che scatta a metà di un'operazione privilegiata può lasciare il programma in uno stato incoerente ma ancora privilegiato.

> [!note] Contromisure segnali
> Da utente si può fare poco: contano le pratiche di coding sicuro lato sviluppatore. Come sempre, tenere aggiornati i programmi di terze parti.

### Core file

> [!info] Dump che tradisce
> Un **core file** è il dump dello spazio d'indirizzamento di un processo, creato quando termina in modo inatteso. Preziosissimo per il debug, ma se mal gestito **espone informazioni sensibili** — incluse le hash da `/etc/shadow` finite in memoria. Il crash di una web app può generare un core nella root directory: `www.vulnerablesite.com/core` → scaricabile. Un piccolo survey stima ~0.1% dei siti Alexa Top 1M affetti.

> [!info] Meccanica — a voce
> Se un processo privilegiato (o SUID) che aveva letto `/etc/shadow` in RAM va in crash, quelle hash finiscono nel dump. Se il core cade nella webroot, chiunque lo scarica e lo analizza offline. È l'analogo "a freddo" del dumping di LSASS visto su Windows: memoria di un processo privilegiato che cola all'esterno.

> [!note] Contromisure core file
> Gestirli correttamente: disabilitarli se possibile (scomodo per sysadmin/dev), altrimenti configurare i core dump con permessi appropriati e limitare chi può accedervi. Regola pratica: se stai salvando dump dove chiunque può scaricarli, rivedi le tue pratiche di sicurezza.

### Shared library

> [!info] Bersaglio condiviso
> Le shared library (le DLL di Windows) permettono a più programmi di chiamare routine da una libreria comune. Fanno risparmiare memoria e semplificano la manutenzione: aggiornare la libreria aggiorna tutti i programmi che la usano. Ottimo bersaglio: **iniettare una libreria alterata** consente esecuzione arbitraria e compromette **più programmi in un colpo solo**.

> [!note] Ordine di ricerca (ld)
> Dove il sistema cerca le shared library, in ordine: directory da `rpath-link` (solo a link time); directory da `-rpath` (incluse nell'eseguibile, usate a runtime); env `LD_RUN_PATH` (link time); env `LD_LIBRARY_PATH` (runtime); `DT_RUNPATH` o `DT_RPATH` (il secondo ignorato se esiste il primo); `/lib` e `/usr/lib`; directory in `/etc/ld.so.conf`.

> [!info] Library hijacking — a voce
> È l'equivalente Linux del DLL hijacking. Il loader percorre quella lista **in ordine**: se l'attaccante riesce a scrivere una `.so` malevola in una posizione che viene consultata **prima** della libreria vera (o in uno slot di libreria *mancante*, o via `LD_LIBRARY_PATH`), un programma più privilegiato la carica → code execution nel **contesto di quell'utente**. Il vettore più diretto (non nelle slide ma è il classico) è `LD_PRELOAD`, che forza il preload di una libreria prima di ogni altra. Il flowchart ContextIS riassume esattamente questa caccia: `ldd` → RPATH → env vars → RUNPATH → `/lib` → `ld.so.conf` → librerie mancanti; a ogni tappa la domanda è *"ho permesso di scrivere in questa posizione?"*.

> [!note] Contromisure shared library
> Seguire le pratiche di sicurezza: usare `-rpath` al linking quando possibile; assicurarsi che `LD_RUN_PATH`, `LD_LIBRARY_PATH`, `RUNPATH` **non** includano directory con permessi deboli.

### Kernel flaws

> [!info] Falla alla radice
> I sistemi Unix sono complessi e robusti, ma più complessità = più probabilità di bug. Il **kernel** è responsabile dell'intero modello di sicurezza (permessi, escalation, gestione segnali...): un bug di sicurezza nel kernel **compromette il modello alla radice** → l'attaccante ottiene facilmente il controllo completo del sistema. Contromisura: **sempre** tenere il kernel aggiornato con le patch di sicurezza.

---

## Blocco 2 — Sfruttare misconfigurazioni

### Permessi Unix

> [!note] Classi e modi
> Tre **classi di accesso**: *user* (proprietario), *group* (membri di un gruppo), *others* (tutti gli altri). Per ogni classe tre **modi**: **r** (read), **w** (write), **x** (execute). Si leggono con `ls -l`: `-rwxrwxrwx`, con l'ottale 4/2/1 per bit → `7` per classe (`rwx`). Il primo carattere è il tipo (`-` file, `d` directory).

> [!note] Modi speciali
> Oltre ai tre modi, ogni file ha tre **modi speciali** validi per tutte le classi: **SUID** (Set User ID), **SGID** (Set Group ID), **Sticky**.

### SUID

> [!info] Implicazioni di sicurezza
> Quando un file **SUID** viene eseguito, il processo assume l'**effective user ID del proprietario** del file. Serve flessibilità e elevazione temporanea di privilegi: `sudo` e `passwd` richiedono SUID per funzionare. Eseguire un SUID **di proprietà di root** genera un processo con **EUID 0** (root). *What could go wrong?*

> [!info] EUID e il nodo del privesc — a voce
> Distinzione chiave: **real UID** (chi sei) vs **effective UID** (con quali privilegi agisci). Il bit SUID fa sì che all'exec l'EUID diventi quello del proprietario del binario; se il proprietario è root, l'EUID è 0. Il pericolo: se riesci a far eseguire **codice tuo** dentro un binario SUID-root (buffer overflow, race sul temp file, symlink, shell escape), quel codice gira **come root**. È qui che l'overflow del Cap. 5.1 diventa privesc locale — *"buffer overflow are even more fun with SUID"*: overflow di un SUID-root → root shell (→ [[ETHL - SUID e Privilege Escalation]]).

> [!info] SUID mal configurati
> Molti programmi SUID creano file temporanei in `/tmp` (`stat /tmp` → `1777/drwxrwxrwt`). Chi usa `/tmp`? `strings /bin/* | grep tmp`. L'attacco: piazzare **symlink** in `/tmp` con il nome di temp file prevedibile che il SUID scriverà → il programma (da root) scrive sul target del symlink. È il TOCTOU/symlink applicato ai temp file dei SUID.

> [!info] Sticky bit — a voce
> `/tmp` è `1777` = `rwxrwxrwt`: world-writable **ma** con lo **sticky bit** (`t`). Lo sticky significa che chiunque può creare file, ma **solo il proprietario** può cancellare/rinominare i propri — impedisce che gli utenti si cancellino i file a vicenda. Non protegge però dal pre-piazzamento di un symlink col nome che un SUID userà: lì la falla è il nome prevedibile + la mancanza di `O_EXCL`.

> [!note] Contromisure SUID
> La difesa migliore è **rimuovere quanti più file SUID possibile**: inventariarli, togliere il bit SUID dove si può, usare l'opzione `nosuid` di mount (`cat /proc/mounts`).

### File world-writable

> [!info] Scrivibili da tutti
> File modificabili da **qualunque** utente, di solito per comodità/pigrizia; quasi sempre evitabili. Per trovarli nella VM: `find / -not -type l -not -path "/proc/*" -perm -o+w 2>/dev/null` (ignora symlink e `/proc`).

> [!note] Contromisure world-writable
> Non usarli se non strettamente necessario; inventariarli e rivederli tutti; **mai** lasciare gli startup script world-writable (uno script d'avvio scrivibile = root al reboot).

---

## Blocco 3 — Persistenza (APT)

### Trojan

> [!info] Malware nascosto
> I trojan sono malware nascosti in file altrimenti normali. Ottenuto root, l'attaccante può attaccare un trojan a **qualsiasi** file/programma: es. una versione corrotta di `login`/`ssh` che memorizza le credenziali digitate dagli utenti. Aprono facilmente backdoor per connessioni remote o, per aggirare il firewall, **reverse connection** dal target all'attaccante (stesso principio del back channel del Cap. 5.1).

> [!note] Contromisure trojan
> Difficili da rilevare senza setup adeguato: data di creazione/modifica **spoofabile**, dimensione praticamente identica. L'**hash del binario** è il modo migliore per verificarne la legittimità, ma richiede un **database** con l'hash di ogni programma. Attenzione: dopo la compromissione non ci si può fidare dei backup (potrebbero essere compromessi anch'essi). *A voce*: il DB va costruito **prima** della compromissione e tenuto offline — è la logica di Tripwire/AIDE.

### Sniffer

> [!info] Ascolto passivo
> Nel traffico di rete c'è molta informazione confidenziale. Gli sniffer catturano tutto il traffico che passa sullo **stesso segmento locale**, problema aggravato dal wifi. Restando **completamente passivi** gli attaccanti mappano i servizi bersaglio; se il traffico non è protetto, ottengono anche password e documenti riservati.

> [!note] Contromisure sniffer
> Quasi impossibili da rilevare, ma se ne limita l'efficacia: topologie **switched** (ogni host vede meno traffico — ma resta vulnerabile all'**ARP spoofing**); **sniffer detection** (la NIC in promiscuo e i log grandi tradiscono lo sniffer, ma un attaccante root può sabotare il rilevamento); soprattutto **crittografia a livello di rete** (TLS, IPSec proteggono efficacemente — non applicabile in tutti gli scenari).

### Log cleaning

> [!info] Cancellare le tracce
> I log di sistema registrano ogni attività, **inclusa quella dell'attaccante**. I **log cleaner** fanno parte di praticamente ogni rootkit e cancellano le tracce (record di login, cronologia dei comandi shell). Possono anche **intercettare** i programmi che spediscono i log a server remoti. Log della VM: `cat /etc/syslog.conf`.

> [!info] ptrace — a voce
> `ptrace()` è la funzione di debugging che permette di tracciare e controllare l'esecuzione di **altri processi** (è quello che usa `gdb`). Un log cleaner può usarla per **agganciarsi al demone di logging** e intercettare/sopprimere ciò che invia in remoto, prima che parta — persistenza silenziosa senza toccare i file di log su disco.

### Kernel rootkit

> [!info] Il peggiore
> Il tipo peggiore: compromette il **kernel stesso** del sistema. Permette di compromettere tutti i programmi **senza modificarne nessuno**. Molte vie d'attacco: i **Loadable Kernel Module** (LKM) sono storicamente abusati per piazzare rootkit; metodi avanzati basati su modifiche raw della memoria (`/dev/mem`).

> [!note] Intercettare le syscall
> Diversi approcci, sempre più profondi per evadere i controlli: (1) **modificare la syscall table** redirigendo le chiamate a routine custom — facilmente rilevabile con integrity check; (2) **corrompere il syscall handler** perché punti alla tabella dell'attaccante — non tocca la tabella originale, bypassa l'integrity check, ottenibile via `/dev/mem`; (3) **hackerare la IDT** (Interrupt Descriptor Table) o l'interrupt handler — logicamente simile ai precedenti.

> [!info] La corsa alla profondità — a voce
> Il filo dei tre livelli: ogni tecnica sposta il **hook** più in basso di quello che i controlli d'integrità ispezionano. Se il difensore verifica la syscall table, l'attaccante colpisce l'handler; se verifica l'handler, scende alla IDT. È la stessa dinamica vista sui rootkit Windows: chi controlla vede solo il livello sopra a quello dove il rootkit si è annidato.

> [!note] Contromisure rootkit del kernel
> Non ci si può fidare di **nessun** binario del sistema, né del sistema stesso. Certi tool congelano lo stato di ogni processo e ne catturano le info chiave (anche estraendo l'immagine dei processi in esecuzione). Ma la **prevenzione** è di fatto l'unica contromisura reale per i rootkit del kernel — e va ancora peggio coi rootkit **hardware**.

---

> [!summary] In una riga
> Da utente locale a root si sale sfruttando *ciò che il sistema fa fidandosi* (SUID che agisce come root, programmi che dereferenziano symlink, che caricano librerie da path scrivibili, che scrivono temp file prevedibili) o *bug* (kernel, race, overflow); poi si resta con trojan, sniffer, log cleaner e — il peggiore — rootkit del kernel che intercetta le syscall sotto il livello dei controlli.

> [!question] Punti aperti
> Da approfondire: (1) **TOCTOU** come nota trasversale (symlink + race + temp file dei SUID convergono tutti lì); (2) **LD_PRELOAD** e i dettagli pratici del library hijacking; (3) meccanica fine dei rootkit LKM moderni vs kernel hardening (KASLR, lockdown, module signing, SMEP/SMAP) — le slide si fermano a `/dev/mem`; (4) confronto sistematico privesc **Unix vs Windows** (SUID↔token/UAC, `/etc/shadow`↔SAM, LKM rootkit↔driver/BYOVD del Cap. 4). Confermare se dopo 5.2 c'è altro nel capitolo 5.

> [!todo] Prossimi obiettivi
> (1) Scorporare i callout densi in note standalone già linkate nel frontmatter: [[ETHL - TOCTOU e Race Condition]], [[ETHL - SUID e Privilege Escalation]], [[ETHL - Rootkit e Persistenza]] (+ [[ETHL - Buffer Overflow e Stack Smashing]] dalla 5.1). (2) Chiude il **dittico Unix** 5.1+5.2: valutare una nota-ponte "Unix vs Windows: attack surface a confronto" col Cap. 4. (3) Restano in coda dalle sessioni precedenti: **nota Kerberos completa**, **nota Device Driver Exploits**, integrazioni in [[ETHL - LAN Manager (LM) vs NTLM]], **Homework #2** (Cap. 2 & 3).
