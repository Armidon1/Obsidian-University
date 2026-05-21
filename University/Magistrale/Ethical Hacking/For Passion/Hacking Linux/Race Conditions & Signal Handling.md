
## tags: [eth, unix-hacking, race-condition, signal-handling, privilege-escalation] capitolo: HE7 Ch.5 collegato: [[symlink_attacks]], [[toctou]], [[suid_binaries]], [[openssh_security]]

# Race Conditions & Signal Handling

## Idea Centrale

> Esiste una **finestra temporale** in cui un programma è in uno stato vulnerabile (privilegi elevati, stato incoerente). L'attaccante prova a colpire dentro quella finestra. "Win the race" = riuscire al timing giusto.

[[Symlink Attacks]] statico = caso degenere senza race (file preparato prima). Race condition = versione **dinamica** dove la finestra è temporale e va colpita ripetutamente fino al successo.

---

## Tipologie di Race Condition

|Tipo|Cosa swappi/inietti|Esempio|Note|
|---|---|---|---|
|**TOCTOU classico**|Filesystem state tra check e use|symlink swap tra `lstat()` e `open()`|versione dinamica del [[symlink_attacks]]|
|**Signal-handling race**|Signal asincrono in stato privilegiato|wu-ftpd 1996, regreSSHion 2024|sezione principale qui|
|**Parent process race**|Cambio del parent process in finestra check|pkexec CVE-2011-1485|TOCTOU su privilegio invece che file|
|**Thread race**|Accesso non sincronizzato a stato condiviso|data race su flag globali|classico in codice multithread|
|**Network race**|Risposta spoofata prima di quella vera|Kaminsky DNS attack|vedi [[dns_attacks]]|

Tutti condividono il principio: **una finestra temporale dove l'invariante di sicurezza è violata**.

---

## I Signal in UNIX (background)

Un **signal** è un meccanismo di notifica **asincrona** dal kernel (o da altri processi) a un processo.

```
processo: esegue linea N
              ↓
       SIGURG arriva
              ↓
   kernel sospende il processo
   chiama il signal handler registrato
   handler termina
              ↓
   processo riprende dalla linea N+1
```

### Caratteristica chiave: asincronia

Il signal può arrivare in **qualsiasi punto** del flusso. Il programma non sa quando. L'handler eredita lo stato attuale del processo (euid, variabili globali, file descriptor aperti, ecc.).

### Signal più rilevanti per security

|Signal|Numero|Quando arriva|Note|
|---|---|---|---|
|SIGPIPE|13|Scrittura su pipe/socket chiuso|Comune in network daemon|
|SIGURG|23|TCP urgent data (out-of-band)|Sfruttato in wu-ftpd|
|SIGCHLD|17|Figlio è terminato|Handler spesso vulnerabile|
|SIGTERM|15|Richiesta terminazione|Default kill|
|SIGKILL|9|Terminazione forzata|Non intercettabile|
|SIGALRM|14|Timer scaduto|Sfruttato in regreSSHion|
|SIGINT|2|Ctrl+C|Interrupt utente|

Esistono >30 signal totali. `kill -l` per la lista.

### Registrazione di handler

```c
#include <signal.h>

void my_handler(int sig) {
    // codice eseguito quando arriva il signal
    // ATTENZIONE: ereditato lo stato del flusso principale
}

signal(SIGPIPE, my_handler);
// oppure (più moderno, più sicuro):
struct sigaction sa = { .sa_handler = my_handler };
sigaction(SIGPIPE, &sa, NULL);
```

---

## Perché i Signal Handler sono Pericolosi

### 1. Ereditano lo stato di privilegio

Se il main code era in `setuid(0)` quando arriva il signal → handler esegue come root. Se l'handler torna al main senza ripristinare euid → il programma continua a girare con privilegi elevati.

### 2. Non-reentrancy

Molte funzioni standard (libc) **non sono async-signal-safe**: usano stato globale, mutex, allocazione dinamica. Chiamarle in un handler può corrompere lo stato.

Esempi NON sicuri dentro un handler:

- `printf`, `fprintf`, `syslog` — usano buffer globali
- `malloc`, `free` — usano heap state che può essere già occupato dal main code interrotto
- `pthread_*` — possono deadlockare

Lista completa funzioni async-signal-safe: `man 7 signal-safety`. È corta. In pratica solo syscall pure e poche helper.

### 3. Atomicità violata

Una sequenza tipo:

```c
setuid(0);
do_privileged_thing();
setuid(getuid());  // drop back
```

Non è atomica: il signal può arrivare nel mezzo. Se l'handler salta altrove, il `setuid(getuid())` non viene mai eseguito → privilegi persistono.

---

## Case Study 1 — wu-ftpd v2.4 (1996)

### Setup

Server FTP. Quando utente loggato, server gira con `euid=user`. Registra due handler:

- `SIGPIPE` → chiama `dologout()` quando connessione cade
- `SIGURG` → torna al main command loop quando arriva comando ABOR

### Flusso normale di logout

```c
void dologout() {
    setuid(0);                          // (a) PRIVILEGE RAISE
    write_lastlog();                    // (b) scrive log come root
    close(xferlog);                     // (c) chiude transfer log
    unlink_self_from_process_table();   // (d) cleanup
    exit(0);                            // (e) EXIT
}
```

Finestra di vulnerabilità: da **(a)** a **(e)**, alcuni millisecondi con `euid=0`.

### Exploit timeline

```
tempo →

euid=user ──┬── (dologout) ─────────────┬── exit
            │                           │
         SIGPIPE                    (mai raggiunto)
            │                           │
            └─ euid=0 ─┬────────────────┘
                       │
                  FINESTRA (~ms)
                       │
              ⚡ SIGURG dall'attaccante
                       │
              handler SIGURG: torna al main loop
                       │
              euid=0 PERSISTENTE
                       │
              attaccante invia comandi FTP normali
                       │
              server li esegue come root
```

### Come l'attaccante triggera i signal

|Signal|Come triggerarlo|
|---|---|
|SIGPIPE|Chiudere bruscamente la connessione dati durante un transfer|
|SIGURG|Inviare comando `ABOR` (genera TCP urgent data sul control channel)|

### Risultato

L'attaccante è loggato come prima (sembra utente normale), ma il server processa i suoi comandi successivi con euid=0:

- `retr /etc/shadow` → scarica shadow
- `stor /etc/passwd` → uploada un passwd modificato
- Game over

---

## Case Study 2 — pkexec (CVE-2011-1485, 2011)

`pkexec` (parte di PolicyKit) permette esecuzione di comandi come altro utente con autorizzazione.

### Il bug

pkexec verifica i privilegi guardando il **processo padre**. Schema semplificato:

```c
// pseudocodice pkexec
parent_uid = get_parent_process_uid();   // CHECK
verify_authorization(parent_uid);
// ... finestra ...
execute_command_as_root();               // USE
```

### Exploit

Tra CHECK e USE c'è una finestra. L'attaccante invoca `pkexec` con un parent process, poi sostituisce il parent (via `exec`) con un binario SUID root (come `/usr/bin/chsh`). Quando pkexec arriva al USE, l'euid effettivo del parent è cambiato → autorizza con privilegi alterati → root shell.

```
[augustus]$ ./pwnit
[+] Configuring inotify for proper pid.
[+] Launching pkexec.
# whoami
root
```

`inotify` viene usato per sincronizzare il timing — l'exploit aspetta l'evento giusto sul filesystem per fare lo swap al millisecondo corretto.

### Bug class

TOCTOU su privilegio, non su filesystem. Pattern identico a [[symlink_attacks]] race-based, ma il "file" sostituito è l'identità del processo padre.

---

## Case Study 3 — regreSSHion (CVE-2024-6387, 2024)

Race condition nel signal handler di **sshd**. Esattamente la stessa classe di bug di wu-ftpd, 28 anni dopo.

### Il bug

Il handler di `SIGALRM` in sshd chiama funzioni non async-signal-safe (incluse `syslog()` → `malloc()`). Se il signal arriva mentre il main code è in una funzione che usa lo stesso heap → corruzione → controllo del flusso.

### Sfruttabilità

- Pre-auth (nessuna credenziale necessaria)
- Remote code execution
- In pratica difficile: richiede ore/giorni di tentativi per vincere la race
- Funziona contro glibc Linux, non OpenBSD

### Storia

Il fix di un bug del 2006 (CVE-2006-5051) è stato accidentalmente regredito in OpenSSH 8.5p1 (2020). Bug del 2006 reintrodotto silenziosamente, scoperto solo nel 2024.

Per i dettagli vedi [[openssh_security]].

---

## Async-Signal-Safety — la regola d'oro

Dentro un signal handler, puoi chiamare solo funzioni **async-signal-safe**. Le sicure (estratto):

```
_exit, abort, accept, access, alarm, bind, chdir, chmod, chown,
close, connect, dup, dup2, execle, execve, _exit, fchdir, fchmod,
fchown, fcntl, fork, fstat, fsync, getegid, geteuid, getgid, getpid,
getppid, getuid, kill, link, listen, lseek, lstat, mkdir, open,
pipe, poll, read, readlink, recv, recvfrom, send, sendto, setgid,
setpgid, setsid, setuid, sigaction, sigaddset, sigdelset, signal,
sleep, socket, stat, symlink, time, umask, unlink, wait, waitpid,
write
```

NON sicure (esempi comuni):

- `printf`, `scanf`, `fprintf`, `sprintf` (buffered I/O)
- `malloc`, `free`, `realloc`, `calloc`
- `syslog`
- `pthread_*` (funzioni thread)
- `strdup`, `strtok`
- `localtime`, `gmtime` (usano buffer statici)

Pattern sicuro:

```c
volatile sig_atomic_t flag = 0;

void handler(int sig) {
    flag = 1;   // solo set di flag, niente di più
}

int main() {
    signal(SIGUSR1, handler);
    while (1) {
        if (flag) {
            // gestisci il signal qui, nel main loop
            // dove ogni funzione è sicura
            flag = 0;
            do_safe_handling();
        }
        // ... main work
    }
}
```

---

## Discovery / Detection

### Identificare race condition in un binario

```bash
# Trova SUID + signal handler
find / -perm -4000 -type f 2>/dev/null | \
  xargs -I{} sh -c 'objdump -d "{}" 2>/dev/null | grep -l signal && echo "{}"'

# Strace per vedere setuid e signal in azione
strace -e trace=signal,setuid,setgid -f /usr/bin/some_suid 2>&1 | less

# Tempo di esecuzione di sezioni critiche
strace -T -e trace=setuid /usr/bin/program
```

### Exploit framework

In CTF/HTB tipicamente vedi pattern:

1. Race condition in cron script che fa operazioni con privilegi
2. PID-based race in `/proc/<pid>/`
3. Symlink race tra `stat` e `open`
4. `chmod`/`chown` race su file appena creato

Tool utili: `pspy` (vedi processi in real time senza root), watch loops in bash, `inotify` per sincronizzare exploit con eventi filesystem.

---

## Countermeasures

### A livello di codice

|Pratica|Cosa fa|
|---|---|
|Signal handler **minimali**|Set flag globale + return, gestisci nel main loop|
|Solo funzioni **async-signal-safe** dentro handler|Vedi lista sopra|
|`sigprocmask()` per bloccare signal in sezioni critiche|Riduce finestra a zero|
|`setuid()` early drop, no raise temporaneo|Niente finestra di privilegio|
|Privilege separation (master+worker)|Il processo privilegiato non gestisce input untrusted|
|File operations con `O_NOFOLLOW` + `openat()`|Niente race su path traversal|
|`lstat` + open con file descriptor stesso, non path|Atomico|

### A livello di sistema

|Mitigazione|Effetto|
|---|---|
|`fs.protected_symlinks=1`|Riduce TOCTOU su /tmp|
|Privilege separation by default|sshd, Apache, ecc. usano già master+worker|
|SELinux / AppArmor|MAC riduce impatto post-exploit|
|Rimuovere SUID non necessari|Meno superficie per race-su-privilegi|
|Audit periodico CVE|Race condition vengono scoperte continuamente|

---

## TL;DR esame

1. Race condition = finestra temporale di vulnerabilità + "winning the race" = colpire in quella finestra
2. Tipi: TOCTOU filesystem, signal-handling, parent process, thread, network
3. Signal = notifica asincrona; handler eredita stato del processo (incluso euid)
4. Pericoli signal handler: non-reentrancy, atomicità violata, ereditarietà privilegi
5. Caso storico wu-ftpd 1996: SIGURG iniettato durante dologout() con euid=0 → handler torna al main loop → euid=0 persistente → root remoto
6. Caso pkexec CVE-2011-1485: TOCTOU su parent process tra check e use
7. Caso moderno regreSSHion (2024): stesso pattern di wu-ftpd, 28 anni dopo — la classe di bug non muore
8. Async-signal-safety: funzioni utilizzabili in handler sono ristrette (no malloc, printf, syslog)
9. Fix programmatici: handler minimi (solo flag), sigprocmask in sezioni critiche, drop privilegi early
10. Filo conduttore: [[symlink_attacks]] statico → TOCTOU dinamico → signal race = stessa famiglia di bug temporali

---

## Concetto Chiave

> Asincronia + privilegi temporanei + handler non-atomic-safe = race condition exploitable.

Il pattern è universale e ricorrente: wu-ftpd 1996, pkexec 2011, regreSSHion 2024. Cambia solo il contesto, la classe è la stessa. Per l'esame: se vedi codice con `setuid(0)` + signal handler registrato, sospetta race. Se vedi `lstat` seguito da `open` senza file descriptor passing, sospetta TOCTOU.