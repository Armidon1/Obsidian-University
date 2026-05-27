## tags: [ethical-hacking, he7, ch5, post-exploitation, rootkit, persistence]

# Trojan binaries

> Componente di [[rootkits]] — la variante **userland** dell'occultamento. HE7 Ch.5, sezione "Trojans". Qui c'è anche la parte moderna, perché su questo il libro è davvero datato.

## Concetto

Un binario trojanizzato è un eseguibile di sistema **rimpiazzato** con una versione che:

1. fa **esattamente** il lavoro originale → niente si rompe, niente insospettisce;
2. aggiunge **logica nascosta** → harvesting di credenziali, occultamento dell'attaccante, o backdoor.

La proprietà definente è il punto 1: _stesso comportamento osservabile + payload invisibile_. Un trojan che cambia il comportamento visibile è un trojan fallito. È la stessa logica del cavallo di Troia — l'oggetto è quello che ti aspetti, il contenuto no.

## Quali binari, e perché

HE7 elenca i candidati (`login`, `su`, `telnet`, `ftp`, `passwd`, `netstat`, `ifconfig`, `ls`, `ps`, `ssh`, `find`, `du`, `df`...). Non è una lista casuale: si dividono in **due famiglie**, una per ciascuno scopo dell'attaccante.

|Famiglia|Binari tipici|Scopo|Cosa fa il trojan|
|---|---|---|---|
|**Credential-handling**|`login`, `su`, `sshd`, `passwd`, `ftp`, `telnet`|rubare credenziali|logga username+password in chiaro su file nascosto a ogni autenticazione|
|**System-visibility**|`ps`, `netstat`, `ls`, `ifconfig`, `find`, `du`, `df`|nascondere l'attaccante|filtra dall'output i propri processi, connessioni, file, consumo disco|

Quindi i binari trojanizzati coprono **due dei quattro scopi del rootkit**: furto credenziali + occultamento. È l'occultamento fatto in userland — quello che `[[kernel_rootkits]]` fa intercettando le syscall, qui lo fai riscrivendo il programma che le chiama. Più rozzo, ma allo stesso livello a cui guarda un integrity checker → ed è il suo tallone d'Achille.

## Meccanismo

- **Trojan di `login`/`sshd`**: l'utente si autentica normalmente, ma la coppia username/password viene scritta in un file nascosto (tipo `/tmp/.../...`). Il libro lo dice esplicito: _"a hacked-up version of SSH performs the same function"_.
- **Trojan di `ps`/`netstat`/`ls`**: prima di stampare l'output, scarta le righe che contengono il PID / la porta / il path dell'attaccante. È un filtro applicato a valle.

### Variante: il binario-backdoor _nuovo_

Un trojan non è per forza un _rimpiazzo_: può essere un binario **aggiuntivo** che apre un canale di rientro. Esempio HE7 → **rathole**: server `hole` + client `rat`, listener TCP su porta 1337, password magica `rathole!`, traffico cifrato (blowfish) via due pipe in `/tmp`. Gira sotto **nome di processo falso** (`bash`) → questo è _masquerading_ (ATT&CK T1036): in `ps` sembra una shell legittima.

I canali di persistenza veri e propri (reverse shell, port knocking, covert channel) → [[Backdoors]].

## Evasione della detection

HE7 mette il dito sul punto giusto: i trojan ben fatti **annullano gli indicatori ingenui**.

- **File size matching** — il binario malevolo viene paddato per pesare quanto l'originale.
- **Timestamp matching** — dopo la sostituzione si usa `touch` per riallineare le date. Oggi si chiama **timestomping** (ATT&CK T1070.006). Contromisura: `ctime` (inode change time) è molto più difficile da falsificare di `mtime`/`atime` — la forensics guarda lì.

Conseguenza: la dimensione e la data **non bastano**. Serve un **checksum crittografico**.

## Countermeasures

- **Checksum crittografici** — firma univoca di ogni binario, archiviata **offline / fuori banda**. Su una macchina compromessa un DB locale è falsificabile. Tool: Tripwire, AIDE, OSSEC.
- **Verifica via package manager** — `rpm -V <pkg>` (RPM include MD5 nei metadati), `debsums -c` / `dpkg --verify` su Debian, Solaris Fingerprint Database + `digest`. Da fare con un package manager **known-good**.
    - L'output di `rpm -V` va letto: una riga su `sshd_config` con flag `S.5....T` può essere una modifica _legittima_ dell'admin. Sospetti veri = **binari** modificati senza spiegazione.
- **Rootkit scanner** — `chkrootkit`, `rkhunter`: beccano solo trojan pubblici "in scatola", non quelli personalizzati. Sicurezza da script kiddie.
- **Prevenzione** — impedire la modifica del binario in partenza: filesystem read-only, flag immutable.
- **Recovery** — ricostruire dal supporto originale; **mai** fidarsi dei backup (probabilmente già infetti). Toolkit di binari statically-linked → vedi [[rootkits]].

## Stato moderno (2026)

HE7 descrive l'attaccante che riscrive `/bin/ls` sulla _tua_ macchina. Quel modello è in gran parte morto — ma il concetto non è morto, si è **spostato**. Due direzioni.

> [!tip] Filo conduttore — due fughe dal File Integrity Monitoring Se la difesa è "verifico i checksum dei binari", l'attaccante ha due uscite:
> 
> - **andare sotto** → il trojan si sposta nel kernel/firmware, dove il checker userland non guarda → `[[kernel_rootkits]]`, bootkit.
> - **andare prima** → il trojan si sposta _a monte_, nella build chain, così il binario arriva già trojanizzato **e già firmato** a tutti → supply-chain attack. Il FIM verifica che il binario sia quello del vendor. Non verifica che il vendor non sia compromesso.

### 1. Il trojan è risalito la supply chain

Invece di trojanizzare un binario sulla vittima, lo trojanizzi **alla sorgente**:

- **XZ Utils backdoor — CVE-2024-3094** (marzo 2024). Una backdoor piazzata in `liblzma` da un manutentore infiltrato dopo una lunga campagna di social engineering. `sshd`, sui sistemi systemd, si linka indirettamente a `liblzma` → la backdoor agganciava (via IFUNC resolver) la verifica della chiave RSA in `sshd`, permettendo RCE pre-auth a chi possedeva una specifica chiave privata. **Questo è letteralmente "l'`sshd` trojanizzato" di HE7**, ma consegnato globalmente via build chain invece che box per box. Scoperta quasi per caso da uno sviluppatore PostgreSQL che notò ~500ms di latenza in più sui login SSH.
- **SolarWinds / SUNBURST** (2020) — DLL di Orion trojanizzata, **firmata col certificato legittimo** di SolarWinds e distribuita via update ufficiale a ~18.000 clienti. Dimostra il punto del callout: la firma non ti salva se la pipeline è compromessa.
- **Pacchetti trojanizzati e typosquatting** su npm, PyPI, crates.io; **immagini Docker** malevole su Docker Hub.

### 2. La persistenza si è staccata dal binario

L'attaccante moderno su Linux **non riscrive `ls`**. Ottiene lo stesso risultato senza toccare un binario di sistema:

- **Modulo [[PAM]] malevolo** — il discendente esatto del "trojaned `login`" di HE7. Non rimpiazzi `/bin/login`: lasci cadere un `.so` nello stack PAM, e quello logga ogni password _o_ accetta una password universale. Sopravvive agli aggiornamenti del pacchetto e `rpm -V` su `login` non vede nulla.
- **`/etc/ld.so.preload` + `LD_PRELOAD`** — trojanizzi il _caricamento delle librerie_, non il binario. È un rootkit userland a tutti gli effetti → vedi [[shared_library_hijacking]].
- **systemd unit/timer**, cron, `.bashrc`/profile, regole udev, `~/.ssh/authorized_keys`, git hooks, web shell.

### 3. Perché il modello classico fa fatica oggi

- **Verified boot / rootfs immutabile** — dm-verity verifica crittograficamente il filesystem di sistema a ogni boot (Android Verified Boot, ChromeOS, Fedora Silverblue/CoreOS, immagini `bootc`). Su questi sistemi `/usr/bin/ls` è **read-only e verificato**: non lo riscrivi.
- **Code signing** ovunque (forte su macOS/Windows, in crescita su Linux) → l'attaccante è costretto a rubare certificati (SolarWinds) o, appunto, a risalire la supply chain.
- **Risposta difensiva alla supply chain**: reproducible builds, framework **SLSA**, **SBOM**, firma degli artefatti con sigstore/cosign. La domanda non è più solo "questo binario è integro?" ma "questa _catena di build_ è fidata?".

## Mapping MITRE ATT&CK

|Tecnica|ID|Dove|
|---|---|---|
|Compromise Host Software Binary|T1554|rimpiazzo classico del binario|
|Modify Authentication Process|T1556|trojaned `login` / modulo PAM malevolo|
|Hijack Execution Flow: `LD_PRELOAD`|T1574.006|`/etc/ld.so.preload`|
|Masquerading|T1036|rathole sotto nome di processo `bash`|
|Indicator Removal: Timestomp|T1070.006|riallineamento dei timestamp con `touch`|
|Supply Chain Compromise|T1195|XZ, SolarWinds, npm/PyPI|

## Collegamenti

- Nota-hub: [[rootkits]]
- Variante kernel dell'occultamento: [[Kernel Rootkits]]
- Canali di rientro persistenti: [[Backdoors]]
- Trojan del _caricamento librerie_: [[Shared Library Hijacking]]
- `sshd` come bersaglio (XZ): [[Obsidian-University/University/Magistrale/Ethical Hacking/For Passion/Hacking Linux/SSH|SSH]]