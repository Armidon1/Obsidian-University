---

tags:

- unix
- linux
- sistemi-operativi
- storia-informatica
- posix
- hacking-exposed-7 aliases:
- Unix
- sistema Unix
- Unix-like

---

# Unix — Storia, Filosofia, Varianti e Confronto con Linux

## 1. La nascita — Bell Labs, 1969

Unix nasce nei **Bell Labs di AT&T** nel 1969, sviluppato da **Ken Thompson** e **Dennis Ritchie**. Il progetto è una reazione al fallimento di **MULTICS**, un sistema operativo precedente troppo ambizioso e complesso a cui Bell Labs aveva collaborato.

> [!note] Etimologia Il nome "Unix" è un gioco di parole su MULTICS — la versione "uniplexed" (semplificata) di quello che era "multiplexed". Inizialmente scritto "Unics", poi "Unix".

### Tappe fondamentali

|Anno|Evento|
|---|---|
|1969|Prima versione di Unix su PDP-7|
|1971|Prima edizione documentata, Unix 1st Edition|
|1972|Riscrittura in **C** — fondamentale per la portabilità|
|1977|Prima distribuzione BSD da Berkeley|
|1983|AT&T rilascia System V — base commerciale|
|1988|POSIX — primo standard|
|1991|Linus Torvalds inizia Linux|
|1992|AT&T causa Berkeley sul codice BSD — rallenta BSD|
|2010|Oracle acquisisce Sun (Solaris)|

> [!abstract] Il momento decisivo: la riscrittura in C Unix originariamente era scritto in assembly per il PDP-7. Nel 1972 Thompson e Ritchie lo riscrivono in **C** (linguaggio inventato apposta da Ritchie). Conseguenza: Unix diventa portabile su nuove architetture. Questo è il motivo per cui Unix si è diffuso ovunque mentre i suoi concorrenti dell'epoca, legati all'hardware, sono morti.

---

## 2. La filosofia Unix

Più importante del codice stesso è la **filosofia** che Unix ha imposto. Codificata da Doug McIlroy:

> 1. Fai un programma che faccia una sola cosa, ma falla bene
> 2. Fai programmi che lavorino insieme
> 3. Fai programmi che gestiscano flussi di testo, perché il testo è un'interfaccia universale

Concretamente questo si traduce in:

- **Comandi piccoli e componibili** (`grep`, `cut`, `sort`, `uniq`, `awk`, ...)
- **Pipe** (`|`) per concatenarli
- **Testo come formato universale** — file di configurazione, output, log
- **Tutto è un file** — dispositivi, processi, socket, network, esposti come file in `/dev`, `/proc`, `/sys`

> [!tip] Esempio concreto Quando fai `ps aux | grep nginx | awk '{print $2}'` stai applicando la filosofia Unix: tre tool piccoli e specializzati, concatenati con pipe, che si scambiano testo.

---

## 3. Concetti architetturali di Unix

Il modello che Unix ha imposto e che ritrovi ovunque oggi:

### Tutto è un file

|Risorsa|File in Unix|
|---|---|
|Tastiera, mouse|`/dev/input/*`|
|Disco|`/dev/sda`|
|Processi|`/proc/<pid>/`|
|Memoria|`/dev/mem`, `/proc/meminfo`|
|Random|`/dev/random`, `/dev/urandom`|
|Network socket|File descriptor|
|Pipe|File descriptor|

Conseguenza: gli stessi system call (`read`, `write`, `open`, `close`) funzionano su tutto. Non serve un'API diversa per ogni tipo di risorsa.

### File descriptor

Ogni processo ha una tabella di file descriptor (FD). I primi tre sono standard:

|FD|Nome|Default|
|---|---|---|
|0|stdin|tastiera|
|1|stdout|terminale|
|2|stderr|terminale|

Tutto il resto (file aperti, socket, pipe) sono FD aggiuntivi. La redirezione (`>`, `<`, `2>&1`) manipola questa tabella.

### Processi e fork/exec

Unix introduce il modello **fork + exec**:

- `fork()` — duplica il processo corrente in due processi identici
- `exec()` — sostituisce l'immagine del processo corrente con un programma diverso

Sembra strano (perché duplicare per poi sostituire?) ma permette la pipe, la redirezione, e tutta la flessibilità della shell.

### Permessi e utenti

- **UID/GID** — ogni file ha owner e group
- **Permessi rwx** — read/write/execute per owner/group/other
- **root (UID 0)** — superutente con privilegi totali

Questo modello è quasi invariato da 50+ anni. Linux lo eredita identico.

### Signal

Comunicazione asincrona tra processi via "segnali" — `SIGTERM`, `SIGKILL`, `SIGHUP`, ecc. Ancora oggi il modo standard per gestire interruzioni e shutdown su qualsiasi sistema Unix-like.

---

## 4. Lo scisma: AT&T vs BSD

Negli anni '70-'80 Unix si divide in **due rami principali**:

### System V (AT&T)

La versione commerciale, da cui derivano tutti i Unix commerciali:

- **Solaris** (Sun → Oracle)
- **HP-UX** (HP)
- **AIX** (IBM)
- **IRIX** (SGI, morto)

### BSD (Berkeley Software Distribution)

La variante universitaria, sviluppata a UC Berkeley. Più "permissiva" come licenza. Da BSD discendono:

- **FreeBSD, OpenBSD, NetBSD** (liberi, ancora attivi)
- **macOS / iOS / iPadOS** (Apple, via NeXT)
- **PlayStation OS** (Sony, basato su FreeBSD)

> [!warning] La causa AT&T vs BSD (1992) AT&T fa causa a Berkeley sostenendo che BSD contenesse codice AT&T. Berkeley vince ma la causa rallenta BSD di anni. **Linux nasce esattamente in quel buco** (1991) e si afferma proprio mentre BSD è bloccato in tribunale. Se la causa non fosse stata, oggi probabilmente useremmo BSD invece di Linux.

---

## 5. POSIX e standardizzazione

Negli anni '80 le varianti Unix divergono — System V e BSD hanno comandi e API leggermente diversi, e i Unix commerciali aggiungono estensioni proprietarie. È la **fase delle Unix Wars**.

### POSIX (1988)

**Portable Operating System Interface** — standard IEEE che definisce le API comuni a tutti i Unix. Se segui POSIX, il tuo codice gira su qualsiasi Unix.

### Single UNIX Specification (SUS)

Standard più ampio (include POSIX + altre cose) gestito da **The Open Group**, l'organizzazione che possiede il marchio "UNIX®".

### La certificazione UNIX

Per chiamarsi ufficialmente "UNIX®" un sistema deve:

1. Implementare la Single UNIX Specification
2. Passare i test di compliance
3. Pagare la licenza a The Open Group

Sistemi certificati UNIX oggi:

- **macOS** (l'unico consumer)
- **AIX, HP-UX, Solaris** (server enterprise)
- **z/OS** (mainframe IBM)

> [!note] Linux NON è UNIX certificato Linux non passa la certificazione (richiede tempo e soldi) e nessuno ha interesse a certificarlo. Per questo è **Unix-like** e non Unix.

---

## 6. Filesystem hierarchy — la struttura `/`

Unix definisce una gerarchia di directory standard, ancora oggi quasi identica:

|Directory|Contenuto|
|---|---|
|`/`|Root|
|`/bin`|Eseguibili essenziali|
|`/sbin`|Eseguibili amministrativi|
|`/etc`|File di configurazione|
|`/home`|Home directory utenti|
|`/usr`|Programmi e librerie utente|
|`/var`|Dati variabili (log, mail, ...)|
|`/tmp`|File temporanei|
|`/dev`|Device file|
|`/proc`|Pseudofilesystem processi (Linux, alcuni Unix)|
|`/opt`|Software opzionale di terze parti|

Linux segue questa struttura, BSD lievemente diversa, Solaris ha varianti minori.

---

## 7. Le shell

Unix è inseparabile dalla sua **shell**. Storia delle shell principali:

|Shell|Anno|Autore|Note|
|---|---|---|---|
|**sh** (Bourne shell)|1977|Stephen Bourne|Lo standard storico|
|**csh** (C shell)|1978|Bill Joy|Sintassi C-like, BSD|
|**ksh** (Korn shell)|1983|David Korn|Migliora sh, base per POSIX|
|**bash**|1989|Brian Fox (GNU)|"Bourne Again Shell", default Linux|
|**zsh**|1990|Paul Falstad|Default macOS dal 2019|
|**fish**|2005|—|Friendly, sintassi diversa|

> [!tip] sh è uno standard, bash è un programma `/bin/sh` di default punta a un'implementazione POSIX (su Linux spesso `dash`, su macOS bash o `zsh`). Script con `#!/bin/sh` devono essere POSIX-compatibili. Script `#!/bin/bash` possono usare estensioni bash (array, `[[ ]]`, ecc).

---

## 8. I Unix commerciali — un cenno per ciascuno

### Solaris (Sun → Oracle)

Originariamente SunOS (BSD-derived), poi Solaris (System V-derived). Forte negli ambienti enterprise anni '90-2000. Ha introdotto **ZFS**, **DTrace**, **Zones**. Oggi marginale.

### HP-UX (HP)

Hewlett-Packard Unix, su architettura HP PA-RISC e Itanium. Ancora in uso in ambienti legacy ma in declino.

### AIX (IBM)

IBM Unix su POWER. Ancora attivo, target server di fascia alta.

### IRIX (SGI)

Silicon Graphics Unix per workstation grafiche. Morto con SGI nei primi anni 2000.

### macOS (Apple)

Derivato da **NeXTSTEP** + **BSD** + kernel proprietario **XNU** (basato su Mach + componenti FreeBSD). L'unico Unix mainstream certificato per consumer.

---

## 9. Perché Unix è ancora rilevante oggi

Anche se i Unix commerciali sono morenti, i **concetti** di Unix sono dominanti più che mai:

- **Linux** è Unix-like → server, cloud, Android
- **macOS** è Unix certificato → laptop sviluppatori
- **iOS, Android** → Unix-like nella base
- **WSL** su Windows → Linux dentro Windows
- **Docker, container** → namespaces Linux, eredità Unix
- **Cloud** (AWS, GCP, Azure) → 90%+ delle macchine sono Linux

> [!abstract] Conclusione storica Unix come prodotto commerciale è quasi morto. Unix come **filosofia e modello** ha vinto su tutta la linea. Ogni server moderno, ogni smartphone, ogni Mac eredita direttamente i concetti del 1969.

---

## 10. Unix vs Linux — il confronto

|Aspetto|Unix|Linux|
|---|---|---|
|**Origine**|AT&T Bell Labs, 1969|Linus Torvalds, 1991|
|**Codice**|Proprietario, derivato AT&T o BSD|Scritto da zero, GPL|
|**Licenza**|Commerciale (eccetto BSD)|GPL v2 (free software)|
|**Certificazione**|Marchio UNIX® di The Open Group|Non certificato|
|**Architetture target**|Specifiche (SPARC, POWER, PA-RISC, x86)|Tutte (x86, ARM, RISC-V, PPC, MIPS, ...)|
|**Kernel**|Monolitico (System V, BSD) o ibrido (XNU)|Monolitico modulare|
|**Sviluppo**|Aziendale, chiuso|Aperto, comunitario + aziendale|
|**Distribuzioni**|Una per vendor (Solaris, AIX, ...)|Centinaia (Debian, Red Hat, Arch, ...)|
|**Filesystem nativi**|UFS, ZFS (Solaris), JFS (AIX), HFS+/APFS (macOS)|ext4, btrfs, XFS, ZFS (porting)|
|**Init system**|init/rc.d (legacy), SMF (Solaris), launchd (macOS)|systemd (default moderno), OpenRC, runit|
|**Package manager**|Vendor-specific (pkg, rpm originario, ...)|Distro-specific (apt, dnf, pacman, ...)|
|**Quota di mercato (server)**|<5% combinato|>95%|
|**Quota di mercato (desktop)**|macOS ~15%|~3%|
|**Quota di mercato (mobile)**|iOS ~25%|Android (Linux) ~70%|
|**Filosofia**|"Tutto è un file", piccoli tool componibili|Stessa filosofia, mantenuta|

### Compatibilità reale

|Cosa|Su Unix|Su Linux|
|---|---|---|
|Comandi POSIX (`ls`, `grep`, `awk`)|✅ Identici|✅ Identici|
|Bash script POSIX-compliant|✅ Funzionano|✅ Funzionano|
|System call POSIX|✅ Identiche|✅ Identiche|
|Estensioni GNU (`grep -P`, `sed -i`, ...)|❌ Spesso non disponibili|✅ Native|
|`/proc` filesystem|Varia|✅ Pieno|
|systemd|❌ No|✅ Default|
|Comandi specifici (`dtrace`, `truss`, `pkg`)|✅ Solaris-specifici|❌ Da port|

### La regola pratica

> [!tip] In contesto pentest / sysadmin 95% di quello che sai fare in Linux funziona identico in Solaris/AIX/HP-UX/macOS. Il restante 5% sono:
> 
> - Sintassi leggermente diversa di alcuni tool (es. `ps` su Solaris vs Linux)
> - Init system diverso
> - Package manager diverso
> - Path leggermente diversi (`/opt/sfw` su Solaris vs `/usr/local` su Linux)

---

## 11. Per chi legge HE7 — il pratico

HE7 nel capitolo "Hacking Unix" tratta tutti questi sistemi come categoria unica perché:

1. Stessa filosofia di permessi (UID, GID, root)
2. Stessi protocolli di rete (SSH, FTP, NFS, Sendmail, BIND)
3. Stessi pattern di vulnerabilità (buffer overflow, race condition, setuid abuse, path traversal)
4. Stessa metodologia di attacco (recon → enumeration → exploitation → privesc)

Le differenze sono **sintattiche** (come ottenere quella informazione su Solaris vs Linux), non **concettuali**.

---

## Takeaways

1. **Unix è del 1969**, ha definito i concetti che usi oggi (file, process, pipe, shell, permessi)
2. **Linux non è Unix** — è Unix-like, riscritto da zero, GPL
3. La causa **AT&T vs BSD** del 1992 è il motivo storico per cui Linux ha vinto invece di BSD
4. **POSIX** è lo standard che permette compatibilità tra Unix diversi
5. **macOS è l'unico Unix certificato mainstream** (consumer)
6. **Unix commerciale è morente** (<5% server) — Unix come filosofia ha vinto ovunque
7. Per pentest/sysadmin: **95% di Linux si traduce direttamente in altri Unix**, il 5% è sintassi/tool

---

## Wiki-links

- [[solaris]]
- [[bsd]]
- [[macos]]
- [[posix]]
- [[linux_kernel]]
- [[filesystem_hierarchy]]
- [[shell_scripting]]
- [[hacking_exposed_7_unix]]
- [[history_of_computing]]