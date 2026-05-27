## tags: [eth, unix-hacking, privilege-escalation, dynamic-linking, library-hijack] capitolo: HE7 Ch.5 collegato: [[suid_binaries]], [[nfs_attacks]], [[symlink_attacks]], [[shared_library_hijack_freebsd]]

# Shared Library Hijacking

## Idea Centrale

> Se un attaccante può far caricare a un processo privilegiato una libreria condivisa che controlla, esegue codice arbitrario con i privilegi di quel processo.

È privilege escalation. Il caso FreeBSD/NSS (`roaringbeast`) che hai già nelle note è **un'istanza** di questa famiglia — qui la trattazione organica.

---

## Background: Static vs Dynamic Linking

Un programma può linkare il codice delle librerie in due modi:

| |Static linking|Dynamic linking|
|---|---|---|
|Dove sta il codice libreria|Copiato dentro il binario|File `.so` separato, condiviso|
|Dimensione binario|Grande|Piccolo|
|Aggiornamento libreria|Ricompilare tutto|Sostituire un solo `.so`|
|Superficie d'attacco|Minima|Il `.so` esterno è manipolabile|

```bash
# Vedi le librerie dinamiche di un binario
ldd /usr/bin/ls
    libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6
    ...

# Un binario statico non ha dipendenze
ldd /static/binary
    not a dynamic executable
```

Vantaggio dynamic: risparmio disco/RAM, fix centralizzato. **Costo di sicurezza**: chi controlla il `.so` controlla il codice eseguito.

---

## Il Dynamic Linker

Quando lanci un binario dynamic-linked, interviene il **dynamic linker** (`ld.so` / `ld-linux.so`): trova e carica le librerie necessarie prima che `main()` parta.

Ordine di ricerca delle librerie (semplificato):

```
1. LD_PRELOAD                       ← caricate per prime, override tutto
2. RPATH del binario (deprecato)    ← path embedded nel binario
3. LD_LIBRARY_PATH                  ← variabile d'ambiente
4. RUNPATH del binario              ← path embedded nel binario
5. /etc/ld.so.cache                 ← cache dei path standard
6. /lib, /usr/lib (default)
```

**Ogni elemento prima della riga 5 è un potenziale vettore di hijack.**

---

## Vettori di Hijack

### 1. LD_PRELOAD

```bash
LD_PRELOAD=/path/mylib.so ./programma
```

Forza il caricamento di una libreria **prima di tutte le altre**. Se la libreria definisce una funzione con lo stesso nome di una di sistema (`strcmp`, `getuid`, `fopen`...), la versione dell'attaccante vince — il programma chiama quella.

Uso legittimo: debugging, profiling, intercettazione di chiamate per testing.

### 2. LD_LIBRARY_PATH

```bash
LD_LIBRARY_PATH=/tmp/fakelibs ./programma
```

Aggiunge directory alla ricerca. Se metti in `/tmp/fakelibs` un `.so` con il nome di una libreria legittima, viene preferito a quello reale.

### 3. RPATH / RUNPATH

Path di ricerca **embedded nel binario stesso** a compile time. Insidioso perché non è una variabile d'ambiente — è dentro l'eseguibile.

```bash
# Ispeziona RPATH/RUNPATH di un binario
readelf -d /path/binary | grep -E 'RPATH|RUNPATH'
objdump -x /path/binary | grep PATH
```

Se l'RPATH include una directory scrivibile dall'attaccante → hijack senza toccare l'ambiente.

### 4. Librerie mancanti

Se un binario cerca `libfoo.so` che non esiste in un path scrivibile della catena di ricerca, l'attaccante ce la mette.

```bash
ldd /path/binary
    libfoo.so => not found     ← opportunità
```

### 5. Library replacement diretto

Se l'attaccante ha write access a `/lib` o `/usr/lib`, sostituisce direttamente una libreria di sistema. HE7: _"the system is toast"_.

---

## Perché è Devastante con i Binari SUID

Combinazione letale:

1. Binario SUID root ([[suid_binaries]]) → gira con privilegi root
2. È dynamic-linked → il linker carica librerie all'avvio
3. Se un vettore di hijack è rispettato → carica la libreria dell'attaccante
4. La libreria gira **con privilegi root**

### Proof of concept concettuale

```c
// Libreria malevola — concetto, constructor eseguito al load
#include <stdlib.h>
#include <unistd.h>

__attribute__((constructor))
void init() {
    setuid(0);
    setgid(0);
    system("/bin/sh");
}
```

```bash
gcc -shared -fPIC evil.c -o /tmp/evil.so
LD_PRELOAD=/tmp/evil.so /usr/bin/some_suid_binary
```

Il `constructor` viene eseguito automaticamente quando la libreria è caricata, prima ancora di `main()`.

> **Per questo i dynamic linker moderni IGNORANO `LD_PRELOAD` e `LD_LIBRARY_PATH` per binari SUID/SGID.** È la countermeasure fondamentale e standard da decenni. Il PoC sopra NON funziona su un sistema aggiornato — funziona solo su un binario non-SUID o su sistemi legacy.

---

## Case Study HE7 — in.telnetd (CERT CA-95.14, 1995)

L'esempio storico. Il punto sottile: la variabile d'ambiente viaggia **attraverso la rete**.

### Setup

Il protocollo Telnet (RFC 1408/1572) permetteva al client di passare variabili d'ambiente al server durante la connessione — pensato per comodità (`TERM`, `LANG`).

`in.telnetd` (demone telnet) gira come root. Alla connessione, esegue `/bin/login` per autenticare l'utente.

### Il bug

`in.telnetd` accettava **qualsiasi** variabile d'ambiente dal client — incluse quelle pericolose come `LD_PRELOAD` — e le passava all'ambiente di `/bin/login`.

### Catena dell'attacco

```
1. Attaccante piazza una libreria malevola sul target
   (vettore: FTP anonimo world-writable, share NFS scrivibile [[nfs_attacks]], ecc.)

2. Attaccante si connette via telnet; nel handshake del protocollo
   imposta LD_PRELOAD = /path/della/lib/malevola

3. in.telnetd (root) riceve la variabile, la mette nell'ambiente

4. in.telnetd esegue /bin/login

5. Il dynamic linker, eseguendo /bin/login, vede LD_PRELOAD
   → carica la libreria malevola

6. Codice della libreria eseguito nel contesto di /bin/login → root
```

Punto subdolo: l'attacco avviene **pre-autenticazione**. L'attaccante inietta `LD_PRELOAD` attraverso il protocollo telnet stesso, senza shell preliminare. Doveva solo aver piazzato la `.so` da qualche parte.

---

## Confronto con il Caso FreeBSD/NSS (roaringbeast)

Stesso principio, vettore diverso — vedi [[shared_library_hijack_freebsd]]:

| |in.telnetd|FreeBSD NSS / roaringbeast|
|---|---|---|
|Processo root bersaglio|`/bin/login` via in.telnetd|`ftpd` via inetd|
|Come si carica la lib malevola|`LD_PRELOAD` via protocollo telnet|`nsswitch.conf` modificato → NSS lookup|
|Come la lib arriva sul target|FTP anon / NFS / qualsiasi|Upload via FTP anonimo|
|Risultato|Root|Reverse shell come root|

Entrambi: **fai sì che un processo root carichi codice che controlli**. È la famiglia "shared library hijack".

---

## Discovery / Enumeration

```bash
# Binari SUID nel sistema
find / -perm -4000 -type f 2>/dev/null

# Per ogni SUID, controlla dipendenze dinamiche
ldd /path/suid_binary

# Cerca librerie "not found" (opportunità di hijack)
ldd /path/binary | grep "not found"

# Ispeziona RPATH/RUNPATH (vettore embedded)
readelf -d /path/binary | grep -E 'RPATH|RUNPATH'

# Verifica se RPATH punta a directory scrivibili
ls -ld $(readelf -d /path/binary | grep RPATH | sed 's/.*\[\(.*\)\]/\1/')

# Controlla permessi delle directory di libreria di sistema
ls -ld /lib /usr/lib /usr/local/lib

# LinPEAS / GTFOBins automatizzano gran parte di questo
```

GTFOBins (gtfobins.github.io) elenca binari con tecniche note — primo posto da controllare per LD_PRELOAD su binari `sudo`-abilitati.

---

## Countermeasures

|Mitigazione|Cosa fa|
|---|---|
|**Linker ignora LD_PRELOAD/LD_LIBRARY_PATH per SUID/SGID**|Fix fondamentale, standard da decenni — neutralizza il vettore principale|
|`/lib`, `/usr/lib` protette (owner root, no write altri)|Se compromesse "the system is toast"|
|Minimizzare i binari SUID|Meno bersagli per l'escalation|
|Audit RPATH/RUNPATH dei binari|`readelf -d` — nessun path verso directory scrivibili|
|Non passare env untrusted attraverso confini di privilegio|La lezione di in.telnetd — i servizi moderni sanitizzano l'ambiente|
|Verifica integrità librerie (package manager, AIDE)|Detecta library replacement|
|`noexec` su filesystem dove non serve eseguire|Limita dove piazzare `.so` malevole|
|Static linking per binari sensibili|Elimina la dipendenza esterna manipolabile|
|`sudo` con `env_reset` (default moderno)|`sudo` pulisce l'ambiente, rimuove LD_*|

---

## TL;DR esame

1. Dynamic linking = codice libreria in `.so` esterni condivisi; comodo ma il `.so` è manipolabile
2. Il dynamic linker cerca le librerie in un ordine; LD_PRELOAD, LD_LIBRARY_PATH, RPATH/RUNPATH sono tutti vettori prioritari
3. LD_PRELOAD = forza una libreria a caricarsi per prima → override delle funzioni di sistema
4. Con un binario SUID root: la libreria dell'attaccante gira come root → privilege escalation
5. Caso HE7 in.telnetd (CA-95.14, 1995): LD_PRELOAD iniettato via protocollo telnet pre-auth → /bin/login carica lib malevola → root
6. RPATH è il vettore più insidioso: embedded nel binario, si ispeziona con `readelf -d`
7. Fix fondamentale: i linker moderni ignorano LD_PRELOAD/LD_LIBRARY_PATH per i SUID
8. `/lib` e `/usr/lib` vanno protette come i file più sensibili
9. Discovery: `find -perm -4000`, `ldd`, `readelf -d`, GTFOBins

---

## Concetto Chiave

> Shared library hijack = far eseguire a un processo privilegiato codice che l'attaccante controlla, sfruttando il meccanismo di caricamento dinamico.

Il pattern si ripete con vettori diversi: LD_PRELOAD (in.telnetd), NSS lookup ([[shared_library_hijack_freebsd]]), RPATH, library replacement. La domanda da farsi a un esame: _quale meccanismo legittimo decide quale codice questo processo root eseguirà, e posso influenzarlo?_ È la stessa logica di [[symlink_attacks]] (influenzare quale file un processo apre) applicata al codice invece che ai dati.