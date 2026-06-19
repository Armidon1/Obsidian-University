# Dynamic Linking — come un programma trova il suo codice a runtime

> [!abstract] In una frase 
> Un eseguibile dinamico **non contiene tutto il suo codice**: le funzioni di libreria (`printf`, `malloc`…) vivono in file `.so` separati, e un programma speciale — il **dynamic linker** (`ld.so`) — le carica e le "collega" al momento dell'avvio, _prima_ che parta `main()`. Capire questo meccanismo è la chiave per (a) capire come funziona davvero un processo Linux, e (b) capire un'intera famiglia di attacchi di privilege escalation: `LD_PRELOAD`, `LD_LIBRARY_PATH`, `/etc/ld.so.preload`, `.so` injection.

> [!tip] Come usare questa nota 
> Questa nota è il "pezzo teorico mancante" sotto a [[ETHL 0x05 — Hacking Unix p1]]. Lì gli attacchi (`LD_PRELOAD`, `.so` injection, CVE Screen) erano descritti _operativamente_; qui c'è il **perché** a livello di sistema operativo. Le sezioni 1–4 sono teoria pura (utile anche per esami di Sistemi Operativi / Architetture), le sezioni 5–8 collegano la teoria agli attacchi.

---

## 1. Static vs Dynamic Linking

### 1.1 Il problema che il linking risolve

Quando scrivi `printf("ciao")`, il codice macchina di `printf` non lo scrivi tu — sta nella **libreria standard C** (`libc`). Il **linking** è il processo che collega la _chiamata_ a `printf` nel tuo codice con la _definizione_ di `printf` nella libreria. Può avvenire in due momenti:

| |**Static linking**|**Dynamic linking**|
|---|---|---|
|Quando|a **compile-time** (una volta)|a **runtime** (ogni avvio)|
|Cosa contiene l'eseguibile|una **copia** del codice di libreria|solo **riferimenti** ("mi serve `libc.so.6`")|
|Dimensione binario|grande|piccolo|
|Aggiornamento libreria|richiede ri-compilazione|basta sostituire il `.so`|
|RAM|ogni processo ha la sua copia|il `.so` è **condiviso** tra processi|
|Vettori d'attacco|pochi|`LD_PRELOAD`, `.so` injection, ecc.|

> [!info] Perché "shared" object Il `.so` sta per **shared object**: la stessa copia in RAM di `libc` è mappata in (quasi) ogni processo del sistema. Risparmio enorme di memoria — ed è il motivo per cui i sistemi moderni usano dynamic linking quasi ovunque. Il prezzo è la complessità a runtime (e gli attacchi che vedremo).

## A livello di memoria, i processi come condividono la stessa shared library risparmiando spazio?

Ottima domanda — il pezzo mancante è come funziona la **memoria virtuale**.

---

### Ogni processo vive in una bolla isolata

Ogni processo ha il proprio **spazio di indirizzi virtuali** — vede la memoria come se fosse tutta sua, da `0x0000...` a `0xffff...`. Ma questi indirizzi virtuali non corrispondono direttamente alla RAM fisica.

Il kernel mantiene una **tabella di traduzione** (page table) per ogni processo che mappa indirizzi virtuali → indirizzi fisici in RAM.

---

### Come libc viene condivisa

Quando il primo processo carica libc, il kernel:

1. Legge il file `libc.so` dal disco
2. Lo carica in alcune pagine di **RAM fisica**
3. Mappa quelle pagine nello spazio virtuale del processo

Quando un secondo processo carica la stessa libc:

1. Il kernel vede che `libc.so` è già in RAM fisica
2. **Non la ricarica** — mappa le stesse pagine fisiche nello spazio virtuale del secondo processo

```
Processo A          RAM fisica          Processo B
spazio virtuale                         spazio virtuale

0x7f2d4bc00000 ──→  [pagine libc]  ←── 0x7f9a1de00000
(indirizzo A)       (una sola copia)    (indirizzo B)
```

Gli indirizzi virtuali sono diversi (ASLR), ma puntano alle **stesse pagine fisiche**. Nessuna copia duplicata.

---

### A livello assembly — cosa vede il processo

Il processo non sa nulla di tutto questo. Vede semplicemente:

```
la mia memoria virtuale:
  0x00400000   testo del mio programma
  0x7f2d4bc000  libc  ← sembra memoria normale
  0x7ffd3a2ce000  stack
```

Quando esegue `call puts@plt → jmp [GOT[puts]]`, salta a un indirizzo nel suo spazio virtuale che corrisponde a libc — la CPU fa la traduzione in modo trasparente tramite la **MMU** (Memory Management Unit).

---

### Il problema dei dati — Copy-on-Write

Il codice di libc (`.text`) è **read-only** → può essere condiviso senza problemi, nessun processo lo modifica.

Ma libc ha anche dati (`.data`, variabili globali) che ogni processo potrebbe modificare diversamente. Qui entra il **Copy-on-Write (CoW)**:

```
Finché nessuno scrive:
  Processo A e B → stesse pagine fisiche (condivise)

Quando il processo A scrive su una pagina dati:
  kernel crea una copia privata di quella pagina solo per A
  Processo A → pagina privata (modificata)
  Processo B → pagina originale condivisa
```

Solo le pagine effettivamente modificate vengono copiate — il risparmio di memoria rimane massimo.

---

Puoi vederlo concretamente con `/proc/PID/maps`:

```bash
cat /proc/$(pgrep bash)/maps | grep libc

7f2d4bc00000-7f2d4bd45000 r-xp  libc.so  ← codice, read+execute, condiviso
7f2d4bd45000-7f2d4bf44000 ---p  libc.so  ← gap di protezione
7f2d4bf44000-7f2d4bf48000 r--p  libc.so  ← dati read-only
7f2d4bf48000-7f2d4bf4a000 rw-p  libc.so  ← dati scrivibili (CoW)
```

`r-xp` = read+execute, **p**rivate (CoW). Il codice appare "privato" ma fisicamente è condiviso — CoW significa che diventerebbe privato solo se qualcuno ci scrivesse, cosa che non succede mai per il codice.

---
### chiarimento condivisione memoria fisica

Hai ragione che ogni processo ha libc mappata nel proprio spazio virtuale. Il punto chiave è che **spazio virtuale e RAM fisica sono due cose separate**.

Pensa alla virtual memory come a una **mappa stradale** — segnare una strada sulla mappa non costruisce fisicamente la strada. Costa solo l'inchiostro per disegnarla.

```
Processo A                 RAM fisica               Processo B
page table:                                         page table:
0x7f2d → pagina 301 ───→  [pagina 301: printf]  ←─── 0x7f9a → pagina 301
0x7f2e → pagina 302 ───→  [pagina 302: malloc]  ←─── 0x7f9b → pagina 302
...                        [pagina 303: fopen]        ...
```

La page table di ogni processo è solo un **elenco di traduzione** — costa pochissimo (qualche kilobyte). Le pagine fisiche con il codice di libc esistono una volta sola.

---

#### Il costo effettivo con N processi

Mettiamo che libc occupi 2MB di codice:

```
Static linking (vecchio modo):
  100 processi × 2MB = 200MB di RAM fisica

Dynamic linking:
  2MB di RAM fisica (libc, una copia)
  + 100 × ~4KB di page table entries (le "mappe")
  = ~2.4MB totali
```

Le page table entries sono 8 byte per pagina da 4KB — per 2MB di libc sono circa 512 entries × 8 byte = 4KB per processo. Trascurabile.

---

#### Il tuo intuito era corretto, ma applicato alla cosa sbagliata

Hai ragione che "printf è definita da qualche parte nella memoria del processo" — è nella sua virtual memory. Ma virtual memory non è RAM. È uno spazio di indirizzi astratto che il processo usa come se fosse suo, ma fisicamente i byte di printf esistono in un solo posto nella RAM, condiviso da tutti.

La MMU fa questa traduzione in hardware, in modo trasparente, ad ogni accesso. Il processo non sa né gli importa — vede solo il suo spazio virtuale.

---
### 1.2 Verificare le dipendenze di un binario

```bash
ldd /bin/ls
#   linux-vdso.so.1
#   libselinux.so.1 => /lib/x86_64-linux-gnu/libselinux.so.1
#   libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6
#   /lib64/ld-linux-x86-64.so.2   ← il dynamic linker stesso
```

> [!warning] `ldd` non è sicuro su binari non fidati `ldd` può **eseguire** il binario (o suoi pezzi) per risolvere le dipendenze. Su un binario sospetto usa invece:
> 
> ```bash
> objdump -p /bin/ls | grep NEEDED
> readelf -d /bin/ls | grep NEEDED
> ```
> 
> Queste leggono solo l'**header ELF** staticamente, senza eseguire nulla. (Vedi [[strace & ldd]].)

---

## 2. Chi fa partire un programma: il dynamic linker

### 2.1 La catena di avvio

Quando lanci `./ls`, **non** è il kernel a eseguire direttamente il codice di `ls`. La sequenza reale è (in linea generale senza distinguere lazy binding oppure binding immediato):

```
tu:        ./ls
kernel:    legge l'header ELF di ls → trova il campo "INTERP"
           ( = /lib64/ld-linux-x86-64.so.2 )
kernel:    carica ED ESEGUE ld.so, passandogli ls come argomento
ld.so:     1. legge le librerie richieste da ls (campi DT_NEEDED)
           2. le trova su disco e le mappa in memoria
           3. esegue i CONSTRUCTOR di tutte le librerie caricate
           4. risolve i simboli (non è esattamente così, vedi §4) 
           5. SOLO ORA salta a _start → main() di ls
```

**NOTA**: Se consideriamo lazy binding, la risoluzione dei simboli avviene a run time del main(), cioè esattamente quando per la prima volta tale funzione viene chiamata. Se il binding è immediato, allora la risoluzione dei simboli avviene prima dell'esecuzione del costruttore (quindi del punto 3) e se non è presente una funzione chiamata dal processo nella libreria, restituisce `abort`. 

Il punto chiave: **c'è sempre uno step intermedio invisibile** (`ld.so`) prima che il tuo programma "vero" inizi. Tutti gli attacchi di questa famiglia colpiscono _quello step_, non il programma target.

> [!info] L'INTERP — provalo
> 
> ```bash
> readelf -l /bin/ls | grep interpreter
> #  [Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
> ```
> 
> È letteralmente scritto dentro il binario quale linker usare. Un binario **statico** non ha questo campo (non gli serve nessun linker a runtime).

### 2.2 Dove ld.so cerca le librerie (ordine)

`ld.so` cerca un `.so` richiesto in quest'ordine (semplificato — vedi `man ld.so`):

1. **`LD_PRELOAD`** (env var) e **`/etc/ld.so.preload`** (file) — i "preload", caricati per primi
2. **`RPATH`** del binario (se presente, e se non c'è RUNPATH)
3. **`LD_LIBRARY_PATH`** (env var)
4. **`RUNPATH`** del binario
5. La **cache** `/etc/ld.so.cache` (generata da `ldconfig` da `/etc/ld.so.conf`)
6. I path di default: `/lib`, `/usr/lib`, `/lib/x86_64-linux-gnu`, …

> [!note] ldconfig e la cache `ld.so` non scandaglia le directory ogni volta (sarebbe lento): legge una cache binaria, `/etc/ld.so.cache`, ricostruita da `ldconfig` quando installi librerie. `ldconfig -p` ti mostra cosa contiene.

---

## 3. PRELOAD vs LIBRARY_PATH — aggiungere vs sostituire

Questa è **la** distinzione concettuale che spiega perché alcuni attacchi funzionano sempre e altri falliscono. Riprende il punto 12 delle [[ETHL 0x05 — Hacking Unix p1#10. Trappole d'esame|trappole d'esame]].

### 3.1 `LD_LIBRARY_PATH` / RPATH — **SOSTITUISCE**

Dice a `ld.so`: _"quando cerchi una libreria che il binario richiede, guarda anche in queste directory"_.

- Scatta **solo** se il nome combacia con una dipendenza reale del binario (es. `libcap.so.2`).
- Il tuo file fake **prende il posto** di quello vero.
- **Problema**: il binario si aspetta certe funzioni (simboli) in quella libreria. Se il tuo fake non le esporta → "symbol not found" → crash (se binding immediato) o crash alla prima chiamata (se lazy). guarda anche in [[ETHL 0x05 — Hacking Unix p1]]

### 3.2 `LD_PRELOAD` / `/etc/ld.so.preload` — **AGGIUNGE**

Dice a `ld.so`: _"carica questa libreria **in più**, prima di tutte le altre, a prescindere da cosa chiede il binario"_.

- Il nome è **arbitrario**: `/tmp/libhax.so`, `/tmp/pippo.so`, qualunque cosa. Non deve combaciare con nessuna dipendenza.
- Non sostituisce niente → non rompe nessun simbolo che il binario si aspetta.
- Caricata **per prima** → il suo constructor parte prima di tutto.

> [!success] La regola da ricordare **PRELOAD aggiunge, LIBRARY_PATH sostituisce.** Sostituire è fragile (devi rispettare il "contratto" dei simboli che il binario si aspetta). Aggiungere è robusto (il binario non sa nemmeno che la tua libreria esiste, non ti chiede niente, non può rompersi). È per questo che gli exploit preferiscono il preload.

## RPATH e RUNPATH

Entrambi sono percorsi di ricerca delle librerie **embedded direttamente nel binario** a compile-time — un modo per dire al dynamic linker "cerca le librerie anche qui", senza dipendere da variabili d'ambiente.

---

### La differenza pratica

Ricorda l'ordine di ricerca di `ld.so` che avevi nella nota:

```
1. LD_PRELOAD
2. RPATH          ← viene prima di LD_LIBRARY_PATH
3. LD_LIBRARY_PATH
4. RUNPATH        ← viene dopo LD_LIBRARY_PATH
5. /etc/ld.so.cache
6. /lib, /usr/lib...
```

**RPATH** — meccanismo vecchio. Ha priorità **sopra** `LD_LIBRARY_PATH` → non può essere sovrascritto a runtime dall'utente.

**RUNPATH** — meccanismo nuovo, lo sostituisce. Viene **dopo** `LD_LIBRARY_PATH` → può essere sovrascritto a runtime.

Come si impostano a compile-time:

```bash
gcc programma.c -Wl,-rpath,/opt/mylibs          # imposta RPATH
gcc programma.c -Wl,-rpath,/opt/mylibs \
                -Wl,--enable-new-dtags           # imposta RUNPATH invece
```

---

### Perché interessano in security

Se RPATH o RUNPATH contengono un percorso **scrivibile dall'attaccante** o **relativo**, diventano un vettore:

```bash
# binario compilato con RPATH="."  (directory corrente)
# l'attaccante mette una libreria malevola nella stessa directory
# ld.so la carica al posto di quella legittima
```

Si vede in pentest quando trovi binari con RPATH che include `/tmp`, directory home, o semplicemente `.` — è una misconfiguration sfruttabile esattamente come un PATH insicuro nei cronjob che hai visto nel lab.

```bash
# verifica RPATH/RUNPATH di un binario
readelf -d ./binario | grep -E "RPATH|RUNPATH"
```

---

## 4. Caricamento vs Risoluzione dei simboli — due fasi distinte

Errore mentale comune: trattare "carico la libreria" come **un evento unico**. In realtà sono **due fasi separate** che possono avvenire in **momenti diversi**.

### 4.1 Cos'è un "simbolo"

Un **simbolo** è il nome di una funzione (o variabile globale) esportata da una libreria. `printf` è un simbolo di `libc.so.6`. Quando `ls` chiama `printf`, il suo codice contiene solo un riferimento al _nome_; il linker deve trovare l'**indirizzo reale** in memoria e collegarlo. Questo collegamento è la **risoluzione del simbolo**.

### 4.2 Le due fasi

| |**Fase A — Caricamento**|**Fase B — Risoluzione simboli**|
|---|---|---|
|Cosa fa|mappa il `.so` in RAM, esegue i **constructor**|per ogni funzione usata, trova l'indirizzo reale|
|Quando|**sempre** allo startup, prima di `main()`|dipende dal **binding** (vedi sotto)|
|Se fallisce|quasi mai (basta che il file esista)|"symbol not found" → abort|

### 4.3 Binding: lazy vs immediato

**Quando** avviene la Fase B dipende da come è stato compilato/linkato il binario:

- **Lazy binding** (default): la risoluzione di una funzione avviene solo alla sua **prima chiamata**, _durante_ `main()`. Implementato via PLT/GOT (vedi §4.4). → I constructor (Fase A) partono **sempre**, indisturbati.
- **Immediato / "now"** (`-z now`, o `LD_BIND_NOW=1`): **tutti** i simboli vengono risolti allo startup, _prima_ dei constructor. → Se manca un simbolo, **abort prima** che il constructor parta.

> [!danger] Perché questo conta per gli attacchi (slide 45 di [[ETHL 0x05 — Hacking Unix p1]]) Con `LD_LIBRARY_PATH` (sostituzione) il tuo fake non esporta i simboli reali. Se il binario è `-z now`, la Fase B fallisce **prima** che il tuo constructor parta → **niente shell**. Se è lazy, il constructor parte (Fase A) e ottieni la shell _prima_ che il programma crashi alla prima chiamata mancante.
> 
> Con `LD_PRELOAD` (aggiunta) **questo problema non esiste**: il binario non chiama nessun simbolo della tua libreria, quindi non c'è nessun simbolo da risolvere, quindi non c'è niente che possa fallire. Solo Fase A, sempre.

### 4.4 (Approfondimento) PLT e GOT — come è implementato il lazy binding

Per chi vuole il dettaglio architetturale:

- **GOT** (Global Offset Table): tabella di puntatori. Una entry per ogni simbolo esterno (ed anche eventuali struct necessari per il processo). All'inizio puntano a codice del linker.
- **PLT** (Procedure Linkage Table): piccoli stub di codice. Quando `ls` chiama `printf`, in realtà salta a `printf@plt`, che la prima volta invoca il linker per risolvere l'indirizzo, lo scrive nella GOT, e le volte successive ci salta direttamente.

> [!info] Collegamento alla binary exploitation [[ETHL 0x07 — Binary Exploitation p1]] 
> GOT e PLT sono anche bersagli di attacco (GOT overwrite) e oggetto di mitigazioni come **RELRO** (Relocation Read-Only): `partial RELRO` / `full RELRO` rendono la GOT non scrivibile dopo lo startup. `full RELRO` implica binding immediato. Lo vedrai in binary exploitation — qui basta sapere che esiste il collegamento.

---

### 4.4 PLT e GOT — come è implementato il lazy binding

Il problema concreto: quando `ls` chiama `printf`, il compilatore sa che `printf` è in libc — ma con [[ASLR]] attivo non sa a quale indirizzo sarà caricata libc a runtime. Il codice compilato deve contenere qualcosa tipo "chiama printf, ma l'indirizzo te lo dico dopo". GOT e PLT sono quel "dopo".

**GOT — Global Offset Table** Tabella di puntatori dentro l'eseguibile — una entry per ogni funzione di libreria usata. All'avvio è vuota (o punta a stub del linker). Man mano che le funzioni vengono chiamate per la prima volta, `ld.so` la popola con gli indirizzi reali.

**PLT — Procedure Linkage Table** Stub di codice fissi nell'eseguibile — uno per ogni funzione esterna. Ogni chiamata a `puts()` nel codice passa prima dallo stub PLT, che consulta la GOT:

```
il tuo codice
    │  call puts
    ▼
puts@plt (stub PLT)
    │  jmp [GOT[puts]]        ← leggi l'indirizzo dalla GOT e salta lì
    ▼
Prima chiamata:
  GOT[puts] punta ancora al linker
    → ld.so trova puts in libc, scrive l'indirizzo reale in GOT[puts]
    → libc puts() eseguita

Seconda chiamata:
  GOT[puts] ora punta direttamente a libc puts()
    → nessun passaggio intermedio
```

> [!warning] GOT overwrite 
> La GOT è **dati scrivibili** senza RELRO. Se un attaccante riesce a scrivere a un indirizzo arbitrario, può sovrascrivere `GOT[puts]` con l'indirizzo di `system`. La prossima chiamata a `puts(stringa)` eseguirà `system(stringa)`. Full RELRO rende la GOT read-only dopo il caricamento, impedendo questa tecnica.

> [!info] Collegamento con le difese `partial RELRO` → alcune sezioni read-only, GOT ancora scrivibile `full RELRO` → GOT completamente read-only + binding immediato forzato Vedi [[ASLR]] e [[ETHL 0x07 — Binary Exploitation p1]] per il contesto exploitation.

---

## 6. I tre vettori d'attacco basati sul linking

Tutti e tre sfanno la stessa cosa — **far eseguire codice tuo nel contesto privilegiato di un altro processo** — ma sfruttano canali diversi del linker. È il [[ETHL 0x05 — Hacking Unix p1#1.3 Il Confused Deputy Problem|Confused Deputy]] applicato al dynamic linker.

### 6.1 `LD_PRELOAD` (variabile d'ambiente) — via sudo

```bash
sudo LD_PRELOAD=/tmp/evil.so qualsiasi_comando
```

- Funziona solo se i sudoers **preservano** la variabile (`env_keep += "LD_PRELOAD"`, assenza di `env_reset`/`env_delete`).
- **Ignorato sui binari SetUID** (vedi §7).

### 6.2 `LD_LIBRARY_PATH` (variabile d'ambiente) — via sudo

```bash
sudo LD_LIBRARY_PATH=/tmp /usr/sbin/bridge   # /tmp/libcap.so.2 fake
```

- Sostituzione → fragile (simboli, `-z now`).
- Stesse restrizioni di env (sudoers) e SetUID.

### 6.3 `/etc/ld.so.preload` (file globale) — via scrittura arbitraria

Questo è il caso della macchina **[[Wall]]** (HTB) con Screen 4.5.0.

- È un **file**, non una variabile d'ambiente → **non** soggetto alla restrizione SetUID del §7. Vale per **ogni** binario dinamico eseguito sul sistema.
- Per scriverci serve essere root… oppure sfruttare un altro bug (un SetUID con scrittura arbitraria) per crearlo.

> [!example] Catena completa su Wall (Screen 4.5.0, CVE-2017-5618)
> 
> 1. `screen` è **SetUID root** e ha un bug: la sua opzione di logging (`-L`) crea file **come root senza controllare i permessi** → **scrittura arbitraria come root**.
> 2. Si usa quel bug per creare `/etc/ld.so.preload` contenente `/tmp/libhax.so`.
> 3. `/tmp/libhax.so` ha un constructor (`dropshell`) che: rende `/tmp/rootshell` di proprietà root e SetUID (`chmod 04755`), poi cancella `/etc/ld.so.preload` (pulizia).
> 4. Si ri-esegue un qualsiasi binario (es. `screen -ls`) → `ld.so` legge il preload → carica `libhax.so` → parte `dropshell` → `/tmp/rootshell` diventa una backdoor SetUID root.
> 5. `/tmp/rootshell` fa `setuid(0); execvp("/bin/sh")` → **shell root**.
> 
> Nota didattica importante: l'effetto su `ld.so.preload` è **one-shot** (il constructor lo cancella subito). Il preload è solo il _vettore temporaneo_ per creare la backdoor _permanente_ (`/tmp/rootshell`). Lasciare `ld.so.preload` attivo sarebbe distruttivo (ogni processo del sistema caricherebbe la lib) e rumorosissimo per un IDS.

> [!info] Perché usare `setuid(0)` e non `system("/bin/sh")` nel constructor? Si poteva, ma il constructor di Screen gira nel contesto di `screen`, e l'autore preferisce creare un SetUID binario riutilizzabile (`rootshell`) invece di una shell usa-e-getta. Sul _perché_ `setuid(0)` dà root pieno (vs drop dei privilegi) → [[ETHL 0x05 — Hacking Unix p1#7. Nota su setuid - privilegiato vs no]].

---

## 7. Perché le variabili `LD_*` sono ignorate sui binari SetUID

> [!warning] Punto d'esame centrale Quando `ld.so` rileva che sta avviando un binario **SetUID/SetGID** (cioè `ruid != euid` o `rgid != egid`), **scarta** le variabili d'ambiente "pericolose": `LD_PRELOAD`, `LD_LIBRARY_PATH`, e altre. Sono trattate come **untrusted** perché l'ambiente è controllato dall'utente che lancia il programma — proprio chi non dovrebbe poter influenzare un processo privilegiato.

Questo spiega l'asimmetria fondamentale:

|Vettore|Funziona su SetUID?|Funziona via sudo?|
|---|---|---|
|`LD_PRELOAD` (env)|❌ no (scartato)|✅ se sudoers lo preserva|
|`LD_LIBRARY_PATH` (env)|❌ no (scartato)|✅ se sudoers lo preserva|
|`/etc/ld.so.preload` (file)|✅ **sì** (è un file, non env)|n/a|

> [!info] Il "buco" concettuale La difesa di `ld.so` è "non fidarti dell'**ambiente** quando il programma è privilegiato". Ma `/etc/ld.so.preload` è un **file di sistema**, non parte dell'ambiente dell'utente — quindi è considerato fidato (in condizioni normali è scrivibile solo da root). Il bug di Screen 4.5.0 viola proprio questa assunzione: dà a un non-root la capacità di scrivere quel file. Il linker si fida del file; il file non meritava fiducia.

---

## 8. Difese (lato sistemista)

|Vettore|Difesa|
|---|---|
|`LD_PRELOAD`/`LD_LIBRARY_PATH` via sudo|`env_reset` nei sudoers (default moderno), `env_delete += LD_*`|
|`.so` injection (path relativo in `dlopen`)|usare **path assoluti** per `dlopen`; RPATH/RUNPATH sicuri|
|`/etc/ld.so.preload`|il file deve essere scrivibile **solo da root**; monitorarne l'integrità (es. con auditd/AIDE)|
|SetUID con scrittura arbitraria (Screen)|patch/aggiornare; rimuovere il bit SetUID se non necessario; **minimo privilegio**|
|GOT overwrite|**full RELRO** + PIE + binding immediato|

> [!quote] Principio generale Il dynamic linker è un **deputy fidato e potentissimo**: esegue codice (constructor) e risolve simboli per conto di ogni programma. Ogni vettore di questa nota consiste nel **convincere il linker a caricare codice controllato dall'attaccante** in un contesto privilegiato. La difesa è sempre la stessa: **non far controllare all'attaccante né l'ambiente né i percorsi né i file** che il linker consulta in un processo privilegiato. È il minimo privilegio applicato al linker.

---

## 9. Comandi utili (cheat-sheet)

```bash
# Dipendenze di un binario (sicuro, statico)
readelf -d /bin/ls | grep NEEDED
objdump -p /bin/ls | grep NEEDED

# Quale interprete (linker) usa
readelf -l /bin/ls | grep interpreter

# Cosa c'è nella cache delle librerie
ldconfig -p | grep libc

# Vedere il linking a runtime (quali .so apre, ENOENT su path relativi)
strace ./binario 2>&1 | grep -iE "open|access|no such file"

# Forzare binding immediato (per testare resistenza a LD_LIBRARY_PATH)
LD_BIND_NOW=1 ./binario

# Compilare una shared library con constructor
gcc -shared -fPIC -o evil.so evil.c

# Trovare i SetUID (primo recon post-foothold)
find / -type f \( -perm -u+s -o -perm -g+s \) -ls 2>/dev/null

# Capabilities (alternativa al SetUID)
getcap -r / 2>/dev/null
```

---

## 10. Richiamo attivo (a libro chiuso)

> [!question] Verifica
> 
> 1. Differenza tra static e dynamic linking: 3 conseguenze pratiche.
> 2. Descrivi la catena di avvio di `./ls` dal kernel a `main()`. Dov'è il punto in cui `ld.so` interviene?
> 3. Cosa significa che `/etc/ld.so.preload` "aggiunge" mentre `LD_LIBRARY_PATH` "sostituisce"? Perché aggiungere è più robusto per un attaccante?
> 4. Quali sono le due fasi del caricamento di una libreria? Quale dipende dal binding lazy/immediato?
> 5. Un fake `libcap.so.2` via `LD_LIBRARY_PATH` su un binario `-z now` fallisce. Perché? Come lo aggiusti (due modi)?
> 6. Perché un constructor parte anche se il binario non chiama nessuna funzione della tua libreria?
> 7. Perché `ld.so` ignora `LD_PRELOAD` sui binari SetUID ma onora `/etc/ld.so.preload`?
> 8. Spiega l'intera catena di Wall (Screen 4.5.0) in termini di scrittura arbitraria + dynamic linking. Perché l'effetto su `ld.so.preload` è one-shot?
> 9. Cosa sono PLT e GOT, e che ruolo hanno nel lazy binding?
> 10. Tre difese contro gli attacchi basati sul linking.

---

## Collegamenti

- [[ETHL 0x05 — Hacking Unix p1]] — il contesto operativo (SUID, sudo, GTFOBins, gli exploit)
- [[strace & ldd]] — strumenti per ispezionare il linking
- [[Sudo]] — l'ambiente sudo e `env_keep`
- [[GTFOBins]] — catalogo di abusi di binari
- [[ETHL 0x04 — Web Security p2]] — il Confused Deputy nel contesto web (injection)