# Approfondimento Processi Linux

Il codice è nel sorgente del kernel Linux, su GitHub. Le strutture chiave sono due:

---

## `task_struct` — il processo

Ogni processo è rappresentato da `struct task_struct` in `include/linux/sched.h`. Dentro c'è un puntatore a `files`:

```c
struct task_struct {
    ...
    struct files_struct *files;   // ← la tabella dei file descriptor
    ...
};
```

👉 https://github.com/torvalds/linux/blob/master/include/linux/sched.h (cerca `files_struct`)

---

## `files_struct` — la tabella dei FD

Definita in `include/linux/fdtable.h`:

```c
struct files_struct {
    atomic_t count;
    struct fdtable __rcu *fdt;    // ← puntatore alla tabella vera
    struct fdtable fdtab;         // ← tabella inline (ottimizzazione)
    ...
};

struct fdtable {
    unsigned int max_fds;
    struct file __rcu **fd;       // ← l'array di puntatori a file
    ...
};
```

👉 https://github.com/torvalds/linux/blob/master/include/linux/fdtable.h

`fd` è esattamente l'array di cui parla la slide: `fd[0]` → stdin, `fd[1]` → stdout, `fd[2]` → stderr, `fd[3]` → primo file aperto dal processo, ecc.

---

## `file` — la risorsa reale

Ogni cella dell'array punta a una `struct file` (definita in `include/linux/fs.h`), che contiene la posizione corrente nel file, i permessi, e un puntatore alle operazioni (`f_op`) — che cambiano a seconda che sia un file su disco, un socket, un device, ecc.

```c
struct file {
    struct path f_path;
    const struct file_operations *f_op;   // ← operazioni (read, write, ioctl...)
    atomic_long_t f_count;
    loff_t f_pos;                         // ← posizione corrente (offset)
    ...
};
```

👉 https://github.com/torvalds/linux/blob/master/include/linux/fs.h

---

## Come lo vedi a runtime su un processo reale

Senza leggere il kernel, puoi ispezionare la tabella FD di qualsiasi processo vivo:

```bash
ls -la /proc/<PID>/fd/
# lrwxrwxrwx 1 ... 0 -> /dev/pts/0   (stdin)
# lrwxrwxrwx 1 ... 1 -> /dev/pts/0   (stdout)
# lrwxrwxrwx 1 ... 2 -> /dev/pts/0   (stderr)
# lrwxrwxrwx 1 ... 4 -> socket:[12345]
```

`/proc/<PID>/fd/` è una vista diretta della `fdtable` di quel processo — ogni symlink è un FD, il target è la risorsa reale. Utile anche in post-exploitation per capire quali connessioni/file ha aperti un processo. Nota che i `/dev/pts/0` sono dei [[PTY]]

## come vederlo sul proprio OS

Sì, direttamente. Su Fedora:

```bash
# FD della tua shell corrente
ls -la /proc/$$/fd/
```

`$$` è una variabile bash che si espande automaticamente al PID del processo corrente. Vedrai i tre FD standard più eventuali file aperti dalla shell.

Per un processo specifico, prima trovi il PID:

```bash
# esempio: il tuo browser
pgrep firefox
ls -la /proc/<PID>/fd/
```

Oppure in modo più leggibile con `lsof` (list open files):

```bash
lsof -p $$          # tutti i file aperti dalla shell corrente
lsof -p <PID>       # di un processo specifico
```

Cosa interessante da fare: apri un file in un terminale

```bash
exec 5< /etc/hostname    # apri /etc/hostname sul FD numero 5
ls -la /proc/$$/fd/      # ora vedi fd/5 → /etc/hostname
exec 5<&-               # chiudi il FD 5
ls -la /proc/$$/fd/      # sparito
```

Stai manipolando direttamente la fdtable del processo — la stessa struttura del codice kernel che hai visto prima.

# Approfondimento su task_struct

Ecco la struttura ripulita, raggruppata per tema:Due cose da notare subito nel diagramma:

![[Pasted image 20260609103202.png]]

Il blocco **file descriptor** (amber) è quello che stai studiando — punta a `files_struct`, che contiene l'array `fd[]` con stdin/stdout/stderr e tutti i file aperti.

Il blocco **credenziali** (coral) contiene `struct cred` con `ruid`, `euid`, `suid` — è esattamente quello di cui parla tutta la sezione su `setuid()` nelle note 0x05.

Il blocco **stack canary** (rosso) è il `stack_canary` di 0x07 — il valore usato per rilevare buffer overflow. È un campo del processo stesso, non del binario.

Tutti i campi dentro `#ifdef CONFIG_*` (cgroups, BPF, NUMA, perf, lockdep...) non spariscono — ma esistono nel sorgente solo se il kernel è compilato con quella feature. Sul tuo Fedora quasi tutti ci sono, perché le distro abilitano quasi tutto.

# Identità del Processo

## `pid` e `tgid` in `task_struct`

Linux distingue due concetti che spesso si confondono: **thread** e **processo**.

Nel kernel, ogni thread è rappresentato da una propria `task_struct` — il kernel non ha un concetto separato di "processo con thread dentro". Ogni thread è una task. Da qui nasce il problema: come distingui un thread solitario (un processo classico) da un gruppo di thread che appartengono allo stesso programma?

La risposta sono questi due campi:

```c
pid_t  pid;   // Process ID — unico per ogni task nel sistema
pid_t  tgid;  // Thread Group ID — condiviso da tutti i thread dello stesso processo
```

**`pid`** è l'ID univoco della singola task. Due task non possono avere lo stesso `pid`. Se un programma crea tre thread, il kernel crea tre `task_struct` con tre `pid` diversi.

**`tgid`** è l'ID del gruppo. Tutti i thread dello stesso processo condividono lo stesso `tgid`, che corrisponde al `pid` del thread principale (quello creato per primo).

### Cosa vedi da userspace

Quando esegui `ps` o leggi `/proc`, il numero che chiami "PID del processo" è in realtà il `tgid`. La syscall `getpid()` restituisce `tgid`, non `pid`. La syscall `gettid()` restituisce `pid`.

```
processo principale:   pid=1000, tgid=1000   ← tgid == pid: è il thread principale
thread figlio 1:       pid=1001, tgid=1000   ← stesso tgid, pid diverso
thread figlio 2:       pid=1002, tgid=1000
```

Da `ps` vedi solo `1000` — il `tgid`. Con `ps -L` (o `/proc/<tgid>/task/`) vedi tutti i thread e i loro `pid` individuali.

### La verifica diretta

```bash
ls /proc/$$/task/    # lista tutti i thread della shell corrente
```

Se la shell è single-threaded vedrai solo una directory col PID della shell stessa. Ogni subdirectory corrisponde a una `task_struct` — e il suo nome è il `pid` di quel thread.

# Scheduling

## Scheduling in Linux — dalla `task_struct` al kernel

Lo scheduler decide **quale task gira su quale CPU e per quanto tempo**. I campi rilevanti in `task_struct` sono tre gruppi:

### 1. Priorità

```c
int  prio;         // priorità dinamica (quella che usa lo scheduler)
int  static_prio;  // priorità statica — impostata da nice()
int  normal_prio;  // priorità "normale" calcolata da static_prio + policy
unsigned int rt_priority;  // priorità real-time (se policy RT)
```

`static_prio` va da 100 (massima) a 139 (minima) — corrisponde ai valori `nice` da -20 a +19 che conosci da userspace. Lo scheduler aggiusta `prio` dinamicamente in base al comportamento del processo (es. processo che aspetta molto I/O viene premiato).

### 2. La policy

```c
unsigned int policy;
```

Ogni task ha una **scheduling policy**. Le principali:

|Policy|Significato|
|---|---|
|`SCHED_NORMAL`|processi normali — usa CFS|
|`SCHED_FIFO`|real-time, niente preemption|
|`SCHED_RR`|real-time con time slice rotante|
|`SCHED_IDLE`|gira solo se non c'è nient'altro|
|`SCHED_DEADLINE`|per task con scadenze temporali precise|

### 3. `sched_entity` — il cuore del CFS

```c
struct sched_entity se;   // per SCHED_NORMAL (CFS)
struct sched_rt_entity rt; // per RT
struct sched_dl_entity dl; // per DEADLINE
```

`struct sched_entity` è la struttura che il **CFS (Completely Fair Scheduler)** usa per tenere traccia di quanto tempo CPU ha già ricevuto una task. Il campo chiave dentro `se` è `vruntime` — **virtual runtime**: il tempo CPU consumato dalla task, normalizzato per la sua priorità.

Lo scheduler mantiene un **red-black tree** (albero bilanciato) ordinato per `vruntime`. La task con il `vruntime` più basso — quella che ha ricevuto meno CPU — sta sempre a sinistra e viene scelta per girare. Questo è il meccanismo con cui CFS garantisce "fairness": nessuna task accumula troppo CPU senza che le altre vengano servite.

### 4. Stato della task

Non è un campo di scheduling puro, ma è strettamente collegato:

```c
unsigned int __state;
```

I valori principali:

|Stato|Significato|
|---|---|
|`TASK_RUNNING`|sta girando su una CPU, o pronta nella run queue|
|`TASK_INTERRUPTIBLE`|sleeping, svegliabile da segnale|
|`TASK_UNINTERRUPTIBLE`|sleeping, NON svegliabile da segnale|
|`TASK_ZOMBIE`|terminata, aspetta che il parent chiami `wait()`|

`TASK_UNINTERRUPTIBLE` è il motivo per cui a volte un processo non risponde a `kill -9` — sta aspettando I/O dal kernel in un punto in cui non può essere interrotto. È quello che vedi come stato `D` in `ps`.

### Come vederlo live

```bash
# stato e priorità di tutti i processi
ps -eo pid,tid,stat,pri,ni,comm

# vruntime e altri dettagli CFS per un processo specifico
cat /proc/<PID>/sched
```

`/proc/<PID>/sched` mostra direttamente i campi di `sched_entity` — `vruntime`, numero di context switch volontari e involontari, tempo totale su CPU. È la finestra diretta su quello che lo scheduler vede.

# Memoria Virtuale

## `mm_struct` — la mappa della memoria virtuale di un processo

Ogni processo ha il suo **spazio di indirizzi virtuale** — un'illusione che il kernel mantiene per far credere a ogni processo di avere la RAM tutta per sé. `mm_struct` è la struttura che descrive questo spazio.

```c
struct mm_struct *mm;         // spazio di indirizzi del processo
struct mm_struct *active_mm;  // mm attiva sulla CPU in questo momento
```

`active_mm` esiste perché i thread del kernel non hanno uno spazio utente proprio — "prendono in prestito" l'`mm` dell'ultimo processo utente che girava su quella CPU, così la page table rimane caricata e non serve un flush costoso.

---

### Cosa c'è dentro `mm_struct`

Tre componenti principali:

**1. La lista delle VMAs (Virtual Memory Areas)**

```c
struct maple_tree mm_mt;  // albero di tutte le VMA
```

Una **VMA** (`vm_area_struct`) descrive un intervallo contiguo di indirizzi virtuali con le stesse proprietà: permessi (r/w/x), se è backed da un file o anonimo, se è condiviso. Ogni segmento che vedi in `/proc/<PID>/maps` è una VMA.

```bash
cat /proc/$$/maps
```

```
55a3f2000000-55a3f2001000 r--p  ...  bash    ← testo (read-only)
55a3f2001000-55a3f200a000 r-xp  ...  bash    ← codice eseguibile
7ffd3a000000-7ffd3a021000 rw-p  ...  [stack]
7ffd3a021000-7ffd3a025000 r--p  ...  [vvar]
```

Ogni riga è una VMA. I permessi `r--`, `r-x`, `rw-` corrispondono ai flag dentro `vm_area_struct`.

**2. La page table**

```c
pgd_t *pgd;  // Page Global Directory — radice della page table
```

La **page table** traduce indirizzi virtuali → indirizzi fisici in RAM. Ogni accesso a memoria passa dal processore (MMU) che consulta questa struttura. Se la traduzione non esiste → **page fault** → il kernel interviene (carica la pagina da disco, alloca RAM, ecc.).

Su x86-64 la traduzione è a 4 livelli: PGD → PUD → PMD → PTE → frame fisico.

**3. Statistiche e limiti**

```c
unsigned long start_code, end_code;   // indirizzi del segmento testo
unsigned long start_data, end_data;   // segmento dati
unsigned long start_brk,  brk;        // heap — brk() lo espande
unsigned long start_stack;            // base dello stack
```

Questi sono i confini dei segmenti classici. `brk` è il limite corrente dell'heap — `malloc()` alla fine chiama `brk()` o `mmap()` per espanderlo.

---

### Il collegamento con la sicurezza (0x07/0x08)

`mm_struct` è dove vivono **ASLR** e **NX**:

**ASLR** — quando il kernel mappa le VMA, randomizza gli indirizzi base di stack, heap e librerie. Il campo `mm->mmap_base` viene calcolato con un offset casuale all'avvio del processo. È per questo che in ret2libc devi fare un leak dell'indirizzo di libc a runtime — non puoi sapere a priori dove è stata mappata.

**NX (No-Execute)** — ogni VMA ha un flag `VM_EXEC`. Se non è settato, la MMU impedisce l'esecuzione di codice in quella pagina. Lo stack di default non ha `VM_EXEC` → shellcode iniettato sullo stack → SIGSEGV. In 0x08 hai visto `execstack -s` che aggiunge `VM_EXEC` allo stack per i lab didattici.

---

### Vederlo live

```bash
# layout completo con permessi
cat /proc/$$/maps

# versione compatta con statistiche memoria
cat /proc/$$/status | grep -E "Vm|Rss"

# brk corrente (limite heap)
cat /proc/$$/status | grep VmData
```

```bash
# quanto stack sta usando la shell
cat /proc/$$/status | grep VmStk
```

La differenza tra `VmRSS` (resident — pagine fisicamente in RAM) e `VmSize` (virtuale — tutto lo spazio mappato) è spesso grande: un processo può avere GB di spazio virtuale mappato ma solo poche decine di MB realmente in RAM — le altre pagine sono su disco o non ancora allocate.

# File Descriptor

## La tabella dei file descriptor — dal kernel al processo

Siamo tornati al punto di partenza, ma ora hai il contesto completo per vederlo in profondità.

---

### La catena di strutture

`task_struct` non contiene direttamente l'array dei FD — c'è una catena di tre livelli:

```
task_struct
  └── struct files_struct *files
        └── struct fdtable *fdt
              └── struct file **fd   ← l'array vero
                    ├── fd[0] → struct file  (stdin)
                    ├── fd[1] → struct file  (stdout)
                    ├── fd[2] → struct file  (stderr)
                    ├── fd[3] → struct file  (primo file aperto)
                    └── ...
```

**Perché tre livelli e non uno?** `fdtable` esiste separata da `files_struct` per permettere la **RCU (Read-Copy-Update)**: quando la tabella deve crescere (es. apri il 1025° file), il kernel alloca una nuova `fdtable` più grande, copia i puntatori, poi sostituisce atomicamente il puntatore `fdt` — senza bloccare i lettori concorrenti.

---

### `files_struct` — il contenitore

```c
struct files_struct {
    atomic_t        count;      // reference count — quanti thread la condividono
    struct fdtable  *fdt;       // puntatore alla tabella attiva
    struct fdtable  fdtab;      // tabella inline (ottimizzazione per processi piccoli)
    spinlock_t      file_lock;  // lock per modifiche
    unsigned int    next_fd;    // prossimo FD libero da assegnare
    unsigned long   close_on_exec_init[1]; // bitmap: FD da chiudere su exec()
    unsigned long   open_fds_init[1];      // bitmap: quali FD sono aperti
};
```

`count > 1` quando più thread condividono la stessa tabella — è il caso dei thread creati con `clone(CLONE_FILES)`. Due thread dello stesso processo vedono gli stessi FD perché puntano alla **stessa** `files_struct`. Se uno apre un file, l'altro lo vede subito.

`close_on_exec` è la bitmap dei FD marcati `O_CLOEXEC` — vengono chiusi automaticamente quando il processo chiama `execve()`. È la difesa contro il leak di FD ai processi figli: se apri un socket e poi fai `exec()` di un altro programma, quel socket si chiude da solo.

---

### `fdtable` — la tabella vera

```c
struct fdtable {
    unsigned int        max_fds;  // dimensione attuale dell'array
    struct file __rcu **fd;       // l'array di puntatori
    unsigned long      *close_on_exec;
    unsigned long      *open_fds;
    unsigned long      *full_fds_bits;
    struct rcu_head     rcu;
};
```

`fd` è il vettore. `max_fds` parte da 64 — i primi 64 FD usano la `fdtab` inline dentro `files_struct`, senza allocazione heap. Se apri il 65° file, il kernel alloca una nuova `fdtable` con `max_fds` raddoppiato.

`open_fds` è una **bitmap** parallela all'array: il bit N è 1 se `fd[N]` è aperto. Trovare un FD libero è cercare il primo bit a 0 — operazione O(1) con le istruzioni bit-scan del processore.

---

### `struct file` — la risorsa reale

Ogni cella dell'array punta a una `struct file`:

```c
struct file {
    struct path             f_path;   // dentry + vfsmount → il file sul filesystem
    const struct file_operations *f_op;  // operazioni: read, write, ioctl...
    spinlock_t              f_lock;
    atomic_long_t           f_count;  // reference count
    unsigned int            f_flags;  // O_RDONLY, O_NONBLOCK, ecc.
    fmode_t                 f_mode;   // FMODE_READ, FMODE_WRITE
    loff_t                  f_pos;    // posizione corrente (offset)
    struct fown_struct      f_owner;  // per segnali asincroni
};
```

`f_op` è il punto chiave di **"tutto è un file"**: un file su disco, un socket, una pipe, `/dev/null` hanno tutti una `struct file`, ma `f_op->read` e `f_op->write` puntano a funzioni diverse. Quando chiami `read(fd, buf, n)` il kernel fa semplicemente `file->f_op->read(...)` — non sa e non gli importa se stai leggendo da disco o da rete.

`f_count` è il reference count della `struct file`. Due processi possono avere FD diversi che puntano alla **stessa** `struct file` — è quello che succede dopo `fork()`: padre e figlio condividono la stessa `struct file` (e quindi lo stesso `f_pos`). Se il padre legge 100 byte, il figlio riprende da lì.

---

### `fork()` vs `dup()` — differenza sottile

```
fork():                          dup(fd):
  padre: fd[3] ──┐               fd[3] ──┐
                 ├──► struct file         ├──► struct file
  figlio: fd[3] ─┘               fd[4] ──┘
```

Entrambi condividono la stessa `struct file` → stesso `f_pos`, stesso `f_flags`. È per questo che la shell può fare `2>&1` (redirigere stderr su stdout): `dup2(1, 2)` fa puntare `fd[2]` alla stessa `struct file` di `fd[1]`.

---

### Vederlo live — collegamento diretto

Quello che hai fatto prima con `ls /proc/$$/fd/` e `exec 5< /etc/hostname` stava manipolando esattamente questo array:

```bash
exec 5< /etc/hostname   # kernel alloca struct file, mette puntatore in fd[5]
ls -la /proc/$$/fd/     # leggi la fdtable del processo corrente
exec 5<&-               # fd[5] = NULL, f_count-- sulla struct file
```

`/proc/<PID>/fd/` è generato dal kernel leggendo direttamente la `fdtable` di quel processo — ogni symlink corrisponde a una cella non-NULL dell'array `fd[]`.

# Credenziali e Sicurezza

## `struct cred` — le credenziali di un processo

Hai già visto il comportamento di `ruid`/`euid`/`suid` nelle note 0x05. Ora vediamo dove vivono nel kernel e come il kernel li usa.

---

### La struttura

```c
struct cred {
    atomic_long_t   usage;        // reference count

    kuid_t          uid;          // real UID
    kgid_t          gid;          // real GID
    kuid_t          suid;         // saved UID
    kgid_t          sgid;         // saved GID
    kuid_t          euid;         // effective UID  ← quello che conta per i permessi
    kgid_t          egid;         // effective GID

    kuid_t          fsuid;        // UID per controlli filesystem
    kgid_t          fsgid;        // GID per controlli filesystem

    struct group_info *group_info; // gruppi supplementari

    kernel_cap_t    cap_inheritable; // capabilities ereditabili
    kernel_cap_t    cap_permitted;   // capabilities permesse
    kernel_cap_t    cap_effective;   // capabilities attive
    kernel_cap_t    cap_bset;        // bounding set
    ...
};
```

`kuid_t` non è un semplice `int` — è una struct che wrappa l'UID per gestire i **namespace** (container Docker, per esempio). Internamente ha un campo `val` che è il numero che conosci.

---

### I due puntatori in `task_struct`

```c
const struct cred __rcu  *real_cred;  // chi sei davvero
const struct cred __rcu  *cred;       // chi sei "adesso" (effective)
```

Normalmente puntano alla stessa struttura. Si separano solo durante operazioni privilegiate temporanee — un thread può cambiare `cred` senza toccare `real_cred`.

---

### Come il kernel controlla i permessi

Ogni volta che un processo prova a fare qualcosa — aprire un file, mandare un segnale, fare `bind()` su una porta — il kernel chiama funzioni come:

```c
uid_eq(current_euid(), file_inode->i_uid)  // sei il proprietario?
capable(CAP_NET_BIND_SERVICE)               // hai la capability?
```

`current_euid()` legge `current->cred->euid`. È sempre e solo l'`euid` che conta per i controlli, non il `ruid`.

---

### `fsuid` — il quarto UID che nessuno conosce

`fsuid` esiste per i server NFS. Uno scenario: un processo root (`euid=0`) vuole accedere a un file per conto di un utente normale, ma senza rinunciare ai propri privilegi root per altre operazioni. Abbassa solo `fsuid` a quello dell'utente — il kernel usa `fsuid` (non `euid`) per i controlli sul filesystem. Oggi è raramente rilevante, ma è lì.

---

### `struct cred` è immutabile — Copy-on-Write

Questo è il punto tecnico più importante: **una `struct cred` non viene mai modificata dopo la creazione**. Quando un processo cambia le sue credenziali (es. chiama `setuid()`), il kernel:

1. alloca una **nuova** `struct cred`
2. copia i valori dalla vecchia
3. modifica i campi necessari nella nuova
4. sostituisce atomicamente il puntatore `current->cred`
5. decrementa il reference count della vecchia

Questo design garantisce che un thread non veda mai credenziali parzialmente aggiornate di un altro thread — o vede la vecchia `cred` completa, o la nuova completa. Mai uno stato intermedio.

---

### Il collegamento diretto con 0x05

Tutto quello che hai studiato su `setuid()` passa da qui. Quando il tuo `.so` malevolo chiama `setuid(0)`:

```c
// dentro la syscall setuid() nel kernel — semplificato
int sys_setuid(uid_t uid) {
    struct cred *new = prepare_creds();  // copia la cred corrente

    if (capable(CAP_SETUID)) {
        // processo privilegiato: imposta tutti e tre
        new->uid  = uid;   // real
        new->euid = uid;   // effective
        new->suid = uid;   // saved
    } else {
        // non privilegiato: solo euid, e solo a uid o suid corrente
        if (uid != old->uid && uid != old->suid)
            return -EPERM;
        new->euid = uid;
    }

    return commit_creds(new);  // sostituisce current->cred atomicamente
}
```

`capable(CAP_SETUID)` controlla se `current->cred->cap_effective` ha il bit `CAP_SETUID` settato — che su un processo con `euid=0` è sempre vero. Da qui la differenza di comportamento tra processo privilegiato e non che hai in nota.

---

### Vederlo live

```bash
# le credenziali del processo corrente
cat /proc/$$/status | grep -E "^(Uid|Gid|Groups|CapEff)"
```

```
Uid:    1000    1000    1000    1000   ← ruid euid suid fsuid
Gid:    1000    1000    1000    1000
CapEff: 0000000000000000               ← nessuna capability attiva
```

Su un processo SUID root in esecuzione vedresti:

```
Uid:    1000    0    0    0    ← ruid=1000, euid=0 — è il SetUID in azione
```

Esattamente la struttura `cred` con `uid=1000` ed `euid=0` che descrive la sezione 7 delle tue note.

# Segnali

## Gestione dei segnali — le strutture nel kernel

---

### I campi in `task_struct`

```c
struct signal_struct    *signal;     // condiviso tra tutti i thread del processo
struct sighand_struct   *sighand;    // handler registrati — condiviso tra thread
sigset_t                blocked;     // segnali mascherati (bloccati)
sigset_t                real_blocked;
sigset_t                saved_sigmask;
struct sigpending       pending;     // coda segnali pendenti per questo thread
```

Tre strutture distinte con tre scopi diversi. È importante non confonderle.

---

### `sighand_struct` — la tabella degli handler

```c
struct sighand_struct {
    spinlock_t      siglock;
    refcount_t      count;
    struct k_sigaction action[_NSIG];  // _NSIG = 64 su Linux x86-64
};
```

`action[N]` contiene l'handler per il segnale N. Ogni entry è una `k_sigaction`:

```c
struct k_sigaction {
    struct sigaction sa;  // handler, flags, mask, restorer
};
```

`sa.sa_handler` è il puntatore alla funzione che hai registrato con `signal()` o `sigaction()`. Può essere:

|Valore|Significato|
|---|---|
|`SIG_DFL`|comportamento default (terminate, ignore, core dump...)|
|`SIG_IGN`|segnale ignorato|
|puntatore|funzione userspace da chiamare|

`sighand` è **condiviso tra tutti i thread** dello stesso processo — se un thread chiama `sigaction()`, cambia il comportamento per tutti. Ha senso: gli handler sono per processo, non per thread.

---

### `signal_struct` — lo stato del processo

```c
struct signal_struct {
    struct sigpending   shared_pending;  // coda segnali diretti al processo intero
    int                 group_exit_code; // exit code se killed da segnale
    struct task_struct  *curr_target;    // thread corrente che riceve i segnali
    ...
    // anche: limiti risorse, statistiche, job control (SIGSTOP/SIGCONT)
};
```

`shared_pending` vs `pending` in `task_struct` — questa è la distinzione chiave:

- **`task_struct.pending`** — segnali diretti a quel thread specifico (es. `tgkill()`)
- **`signal_struct.shared_pending`** — segnali diretti al processo intero (es. `kill()`)

Quando arriva `kill(pid, SIGTERM)`, il kernel mette il segnale in `shared_pending`. Poi sceglie un thread "disponibile" del processo (non bloccato, non in syscall critica) e lo sveglia. Non è deterministico quale thread lo riceve.

---

### `sigset_t blocked` — la maschera

```c
sigset_t blocked;
```

Una **bitmap** di 64 bit — un bit per segnale. Se il bit N è 1, il segnale N è **bloccato**: arriva nella coda `pending` ma non viene consegnato finché non viene sbloccato. È quello che fa `sigprocmask()`.

```bash
# maschera segnali del processo corrente
cat /proc/$$/status | grep SigBlk
# SigBlk: 0000000000000000  ← nessun segnale bloccato (shell normale)
```

Il valore è esadecimale — ogni bit corrisponde a un segnale. `0000000000000002` = bit 1 = SIGHUP bloccato.

> [!info] SIGKILL e SIGSTOP non possono essere bloccati Il kernel li ignora nella maschera. Non puoi bloccarli, non puoi catturarli, non puoi ignorarli. Sono hardcoded nel kernel — bypassano tutto il meccanismo degli handler. È per questo che `kill -9` funziona sempre (tranne su processi in stato `D` — `TASK_UNINTERRUPTIBLE` — che aspettano I/O kernel e non possono essere interrotti nemmeno da SIGKILL).

---

### Il percorso di un segnale — dalla syscall alla consegna

```
kill(pid, SIGTERM)
    │
    ▼
kernel: send_signal()
    │  aggiunge siginfo alla coda pending (shared o thread)
    │  setta il bit TIF_SIGPENDING nel thread target
    ▼
thread target: al ritorno da syscall o interrupt
    │  il kernel controlla TIF_SIGPENDING
    ▼
do_signal()
    │  per ogni segnale pendente non bloccato:
    │  ├── SIG_DFL → terminate / core / ignore / stop
    │  └── handler utente → costruisce un frame sullo stack utente
    ▼
esecuzione handler in userspace
    │
    ▼
sigreturn() — syscall speciale per tornare al contesto pre-segnale
```

Il punto interessante è **"costruisce un frame sullo stack utente"**: per eseguire il tuo handler, il kernel salva i registri correnti sullo stack utente e ci mette sopra un frame che simula una chiamata a funzione verso il tuo handler. Quando l'handler termina e chiama `sigreturn()`, il kernel ripristina i registri salvati e riprende l'esecuzione normale.

Questo meccanismo è rilevante per la binary exploitation — esistono tecniche ROP (`SROP` — Sigreturn-Oriented Programming) che abusano di `sigreturn()` per controllare arbitrariamente tutti i registri in una sola syscall, usando il fatto che il kernel si fida del frame sullo stack.

---

### Vederlo live

```bash
# segnali pendenti, bloccati, ignorati, catturati per la shell
cat /proc/$$/status | grep Sig

# SigPnd: 0000000000000000  ← nessun segnale pendente
# SigBlk: 0000000000000000  ← nessun segnale bloccato
# SigIgn: 0000000000384004  ← segnali ignorati (bitmap)
# SigCgt: 000000004b817efb  ← segnali con handler registrato
```

```bash
# decodifica manuale: bit 1 = SIGHUP, bit 2 = SIGINT, ecc.
# per vedere quali segnali ha catturati bash:
kill -l   # lista tutti i segnali con i loro numeri
```

`SigCgt` per bash avrà molti bit settati — la shell cattura SIGINT (Ctrl+C), SIGTERM, SIGCHLD (figli terminati), SIGWINCH (resize terminale) e altri per gestirli internamente invece di terminare.

# Relazione tra Processi

## L'albero dei processi — struttura e campi

---

### I campi in `task_struct`

```c
struct task_struct __rcu  *real_parent;  // chi mi ha creato con fork()
struct task_struct __rcu  *parent;       // chi riceve SIGCHLD quando muoio
struct list_head           children;     // lista dei miei figli
struct list_head           sibling;      // link nella lista dei fratelli
struct task_struct        *group_leader; // thread principale del mio processo
```

`real_parent` e `parent` di solito puntano allo stesso processo. Si separano quando usi `ptrace()` — il debugger diventa `parent` (riceve SIGCHLD), ma `real_parent` resta il processo originale. È come `strace` e `gdb` intercettano i segnali del processo tracciato.

`children` e `sibling` non sono puntatori semplici — sono `struct list_head`, nodi di una **lista doppiamente linkata circolare**. Ogni figlio è nella lista `children` del padre, e ha il suo nodo `sibling` per collegarsi agli altri figli dello stesso padre.---

![[Pasted image 20260609103612.png]]

### I due alberi separati

Nota che PID 1 e PID 2 sono fratelli ma gestiscono mondi diversi:

**PID 1 (systemd)** — padre di tutti i processi userspace. Ogni servizio, ogni shell, ogni comando che lanci è un discendente di PID 1.

**PID 2 (kthreadd)** — padre di tutti i kernel thread. I processi che vedi con `ps aux` con nome tra parentesi quadre (`[kworker]`, `[ksoftirqd]`, `[migration]`) sono figli di kthreadd. Non hanno `mm` — il campo `mm` in `task_struct` è NULL perché girano interamente in kernel space.

**PID 0 (swapper/idle)** — non è un processo reale, non appare in `ps`. È il thread idle del kernel — gira quando non c'è nient'altro da fare. Ha creato PID 1 e PID 2 durante il boot, ma non compare nell'albero visibile.

---

### Il processo orfano — adozione da PID 1

Se un processo padre termina prima dei suoi figli, i figli diventano **orfani**. Il kernel li riadotta automaticamente a PID 1:

```
bash (PID 891) → fork() → figlio (PID 892)
bash termina
    kernel: figlio.real_parent = PID 1
    kernel: figlio.parent      = PID 1
```

PID 1 chiama `wait()` in loop per raccogliere gli exit code degli orfani — altrimenti diventerebbero **zombie**: processo terminato ma la cui `task_struct` rimane in memoria perché nessuno ha letto il suo exit code.

---

### Vederlo live

```bash
# l'albero completo
pstree -p

# solo la tua shell e i suoi antenati
pstree -p -s $$

# navigare i puntatori a mano
cat /proc/$$/status | grep PPid   # real_parent
cat /proc/1/status  | grep -E "^(Name|Pid|PPid)"

# tutti i figli diretti di PID 1
ls /proc/1/task/    # thread di systemd
pgrep -P 1          # PID di tutti i figli di PID 1
```

# Tempo e Contatori

## Tempi CPU — i campi in `task_struct`

---

### I campi principali

```c
u64  utime;          // tempo passato in userspace (nanosecondi)
u64  stime;          // tempo passato in kernel space (syscall, interrupt)
u64  gtime;          // tempo passato in guest (VM virtualizzata)
u64  start_time;     // quando è nato il processo (nanosecondi dal boot)
u64  start_boottime; // come start_time ma include il tempo di sospensione

struct prev_cputime prev_cputime;  // snapshot precedente per calcoli delta

unsigned long  nvcsw;   // voluntary context switches (processo cede volontariamente)
unsigned long  nivcsw;  // involuntary context switches (preemption dello scheduler)

unsigned long  min_flt; // page fault minori (pagina già in RAM, solo da mappare)
unsigned long  maj_flt; // page fault maggiori (pagina da caricare da disco)
```

---

### `utime` vs `stime` — la distinzione che conta

Ogni nanosecondo che il processo è in esecuzione finisce in uno dei due:

**`utime`** — il processo stava girando nel suo codice, in userspace. Calcoli, cicli, logica applicativa. Il processore era in **ring 3**.

**`stime`** — il processo aveva chiamato una syscall e il kernel stava lavorando per suo conto. `read()`, `write()`, `mmap()`, `fork()` — tutto il tempo passato in kernel space mentre il processo aspetta la risposta. Il processore era in **ring 0**.

Questo è il `%usr` vs `%sys` che vedi in `top` e `htop`. Un processo con `stime` alto fa molte syscall — tipico di server I/O-bound. Un processo con `utime` alto fa calcoli puri — tipico di encoder video, crittografia, simulazioni.

---

### Come il kernel aggiorna i contatori

Non c'è un timer per processo. Il kernel aggiorna `utime`/`stime` in due momenti:

**1. Al context switch** — quando lo scheduler toglie la CPU a un processo, calcola quanto tempo è passato dall'ultimo switch e lo somma al contatore giusto (user o kernel a seconda di dove stava girando il thread).

**2. Al tick dell'orologio** — su sistemi `CONFIG_HZ` classici, ogni interrupt del timer (tipicamente 250 Hz su Linux moderno) il kernel guarda chi sta girando e incrementa il suo contatore. È un'approssimazione — risoluzione di 4ms.

I kernel moderni usano **`CONFIG_NO_HZ_FULL`** (tickless) — non ci sono tick periodici sui core occupati da un solo processo. I contatori vengono aggiornati solo agli eventi reali (syscall, interrupt). Più preciso, meno overhead.

---

### `nvcsw` e `nivcsw` — i context switch

```c
unsigned long nvcsw;   // voluntary — il processo ha chiamato sleep(), wait(), I/O bloccante
unsigned long nivcsw;  // involuntary — lo scheduler lo ha interrotto (time slice scaduta)
```

Il rapporto tra i due rivela il comportamento del processo:

- **`nvcsw` >> `nivcsw`** — processo I/O-bound: cede volontariamente la CPU spesso perché aspetta dati. Buon cittadino per lo scheduler.
- **`nivcsw` >> `nvcsw`** — processo CPU-bound: lo scheduler deve interromperlo perché non cede mai. Tipico di calcolo intensivo.

---

### `min_flt` e `maj_flt` — i page fault

Collegamento diretto con `mm_struct`:

**`min_flt`** (minor fault) — la pagina era già in RAM ma non mappata nella page table di questo processo. Nessun I/O da disco. Costo basso — il kernel aggiorna solo la page table.

**`maj_flt`** (major fault) — la pagina non era in RAM, andava caricata da disco (o da swap). Costo alto — attesa I/O, processo sospeso.

Un `maj_flt` alto dopo il primo avvio è normale (caricamento del codice in RAM). Se persiste, il sistema è sotto pressione di memoria e sta swappando.

---

### Vederlo live

```bash
# utime + stime in clock tick (dividi per 100 per secondi)
cat /proc/$$/stat | awk '{print "utime="$14, "stime="$15}'

# versione leggibile con tutto
/usr/bin/time -v ls    # esegui un comando e stampa statistiche complete
```

L'output di `time -v` mostra esattamente questi campi:

```
User time (seconds): 0.00        ← utime
System time (seconds): 0.00      ← stime
Voluntary context switches: 1    ← nvcsw
Involuntary context switches: 0  ← nivcsw
Major (I/O) page faults: 0       ← maj_flt
Minor (reclaiming a frame) page faults: 104  ← min_flt
```

```bash
# monitoraggio live con aggiornamento al secondo
watch -n1 "cat /proc/$$/status | grep -E 'voluntary'"

# context switch di tutti i processi ordinati
pidstat -w 1
```

---

### Il collegamento con lo scheduling

`utime + stime` è il tempo CPU totale consumato — è esattamente il `vruntime` che il CFS usa per decidere chi gira dopo. Un processo che ha consumato tanto CPU ha `vruntime` alto e sta in fondo alla coda del red-black tree. Un processo che ha appena fatto I/O e si è svegliato ha `vruntime` basso — lo scheduler lo favorisce per compensare l'attesa.

# File system

## `fs_struct` — il contesto filesystem del processo

---

### Il campo in `task_struct`

```c
struct fs_struct *fs;
```

Un puntatore. Piccolo, ma rappresenta due concetti fondamentali: **dove sei** nel filesystem e **qual è il tuo confine**.

---

### La struttura

```c
struct fs_struct {
    int         users;     // quanti thread condividono questa struttura
    spinlock_t  lock;
    seqcount_spinlock_t seq;
    int         umask;     // maschera permessi per file creati (es. 022)
    int         in_exec;   // flag: stiamo eseguendo execve()?
    struct path root;      // root directory — la "/" di questo processo
    struct path pwd;       // current working directory — dove sei adesso
};
```

Solo quattro campi che contano davvero: `root`, `pwd`, `umask`, e il fatto che è **condivisibile tra thread**.

---

### `pwd` — la directory corrente

È quello che restituisce `getcwd()` e che vedi con `pwd` nella shell. Ogni `chdir()` aggiorna questo campo nella `fs_struct` del processo.

```bash
cat /proc/$$/cwd    # symlink alla pwd del processo corrente
ls -la /proc/$$/cwd
# lrwxrwxrwx ... /proc/1234/cwd -> /home/utente
```

Quando lanci `./suid-calc` nella `.so` injection, il binario cerca `./libcalc.so` partendo da `fs->pwd` — è letteralmente il path relativo a questo campo. Ecco perché "controllare la directory corrente" significa controllare cosa trova con path relativi.

---

### `root` — la root directory del processo

Normalmente è `/` per tutti. Ma può essere diversa — è il meccanismo di **`chroot()`**:

```c
chroot("/var/jail");  // kernel: current->fs->root = /var/jail
```

Dopo `chroot()`, il processo vede `/var/jail` come se fosse `/`. Non può risalire oltre — ogni `..` dalla nuova root rimane sulla nuova root. È la base delle sandbox e dei container.

> [!warning] `chroot` non è una vera sandbox Un processo root dentro un chroot può uscirne. La tecnica classica: crea una directory dentro il chroot, fai `chroot` di nuovo su quella directory, poi risali con `../../..`. Il kernel non impedisce a root di cambiare root di nuovo. Per una sandbox reale servono i **namespace** (quello che usano Docker e i container moderni) — isolamento molto più forte a livello kernel.

---

### `umask` — la maschera dei permessi

Quando crei un file, il kernel applica `~umask` ai permessi richiesti:

```
open("file", O_CREAT, 0666)  con umask=022
→ permessi effettivi = 0666 & ~022 = 0644  (rw-r--r--)
```

`umask 022` è il default su quasi tutti i sistemi — impedisce che i file creati siano scrivibili da gruppo e altri per default. La shell eredita l'umask dal genitore e la può cambiare con `umask`.

---

### Condivisione tra thread

Come `files_struct`, anche `fs_struct` ha un contatore `users`. Thread creati con `clone(CLONE_FS)` condividono la stessa `fs_struct` — se un thread fa `chdir()`, tutti gli altri thread del processo vedono la nuova directory corrente.

Questo è il comportamento normale dei thread POSIX. Se invece vuoi thread con directory correnti indipendenti, devi creare processi separati (senza `CLONE_FS`).

---

### Vederlo live

```bash
# directory corrente e root di ogni processo
ls -la /proc/$$/cwd    # pwd
ls -la /proc/$$/root   # root (normalmente /)

# per un processo in chroot (es. container) la root sarà diversa
ls -la /proc/<PID>/root
```

```bash
# umask corrente della shell
umask          # es. 0022

# crea un file e verifica i permessi risultanti
touch /tmp/test_umask
ls -la /tmp/test_umask
# -rw-r--r-- ← 0644, non 0666, per via di umask 022
```

```bash
# vedere la root di tutti i processi — i container avranno path diversi
for pid in /proc/[0-9]*; do
  root=$(readlink $pid/root 2>/dev/null)
  [ "$root" != "/" ] && echo "$pid → $root"
done
```

L'ultimo comando è utile in post-exploitation per trovare processi dentro chroot o container — se `root` non è `/`, quel processo vive in un ambiente isolato.

# Stack canary

## Stack canary — dal kernel alla binary exploitation

Perfetto punto di chiusura del giro su `task_struct` — questo campo lo hai già incontrato in 0x07, ora vedi come funziona sotto il cofano.

---

### Il campo in `task_struct`

```c
#ifdef CONFIG_STACKPROTECTOR
    unsigned long stack_canary;
#endif
```

Un singolo `unsigned long` — 8 byte su x86-64. Esiste solo se il kernel è compilato con `CONFIG_STACKPROTECTOR`, che su tutte le distro moderne (incluso Fedora) è attivo.

---

### Il problema che risolve

Un buffer overflow classico sovrascrive il buffer, poi i dati locali, poi il **saved RBP**, poi il **return address**. Se l'attaccante controlla il return address, controlla l'esecuzione.

```
stack frame senza canary:

[ buffer        ]  ← overflow parte da qui
[ variabili     ]
[ saved RBP     ]
[ return address ]  ← destinazione dell'attacco
```

Il canary si mette in mezzo — tra i dati locali e il return address:

```
stack frame con canary:

[ buffer        ]  ← overflow parte da qui
[ variabili     ]
[ CANARY        ]  ← sentinella
[ saved RBP     ]
[ return address ]
```

Per sovrascrivere il return address devi prima sovrascrivere il canary. Prima di fare `ret`, il prologo verifica che il canary sia intatto. Se è cambiato → `__stack_chk_fail()` → processo terminato con `SIGABRT`.

---

### Da dove viene il valore del canary

Qui entra `task_struct`. All'avvio del processo il kernel genera un valore casuale e lo mette in `current->stack_canary`:

```c
// arch/x86/kernel/process_64.c
void arch_setup_new_exec(void) {
    current->stack_canary = get_random_canary();
    ...
}
```

`get_random_canary()` genera 8 byte casuali con un vincolo: il byte meno significativo è sempre `0x00`. Questo serve a troncare le stringhe — se l'overflow avviene tramite `strcpy()` o `gets()`, il null byte ferma la copia prima che il canary venga letto completamente.

Il valore in `task_struct` è la **fonte di verità** — ogni stack frame del processo usa quel valore come canary.

---

### Come arriva sullo stack — il meccanismo

Il compilatore (`gcc -fstack-protector`) inserisce automaticamente codice nel prologo e nell'epilogo di ogni funzione:

```c
// codice C originale
void funzione(char *input) {
    char buf[64];
    strcpy(buf, input);
}
```

```asm
; prologo — inserito dal compilatore
push rbp
mov  rbp, rsp
sub  rsp, 0x50

; leggi il canary da gs:[0x28]  ← Thread Local Storage
mov  rax, QWORD PTR fs:[0x28]
mov  QWORD PTR [rbp-0x8], rax  ; mettilo sullo stack

; ... corpo della funzione ...

; epilogo — verifica
mov  rax, QWORD PTR [rbp-0x8]  ; rileggi dal stack
xor  rax, QWORD PTR fs:[0x28]  ; confronta con l'originale
jne  __stack_chk_fail           ; se diverso → abort
leave
ret
```

`fs:[0x28]` è il **Thread Control Block (TCB)** — una struttura in Thread Local Storage che contiene, tra le altre cose, una copia del canary presa da `task_struct`. Ogni thread ha il suo TCB, mappato a un indirizzo fisso accessibile via segmento `fs`.

---

### La catena completa---

![[Pasted image 20260609103717.png]]

### Perché il byte meno significativo è sempre `0x00`

```
canary tipico su x86-64:  0x3f8a2c91b74e6200
                                            ^^
                                            sempre 00
```

Su x86-64 è **little-endian** — il byte `0x00` sta in memoria all'indirizzo più basso, cioè **subito dopo il buffer**. Se l'overflow viaggia tramite una funzione string (`strcpy`, `gets`, `scanf %s`), il null byte ferma la scrittura prima che il canary venga toccato. Non è una difesa completa — un overflow binario (es. `memcpy` con lunghezza controllata) non si ferma — ma elimina la classe più comune di exploit naive.

---

### Perché il canary non basta — il collegamento con 0x08

Hai visto in 0x08 tre tecniche che bypassano o evitano il canary:

**ret2function / ret2libc** — se riesci a fare un **leak** del canary (es. format string, read oltre i limiti), lo riscrivi identico nello stack overflow. Il check passa, il return address è già sotto il tuo controllo.

**ROP** — stesso ragionamento: leak + riscrivi.

**Heap overflow / use-after-free** — il canary protegge solo lo stack. Overflow sull'heap non lo tocca.

Per questo il canary da solo non è sufficiente — serve insieme ad ASLR (rende difficile il leak utile) e NX (impedisce shellcode diretto). È la difesa a strati che hai visto in 0x07.

---

### Vederlo live

```bash
# verifica che il binario abbia il canary compilato
checksec --file=/bin/ls
# STACK CANARY: Enabled  ← presente

# un binario senza canary (didattico)
gcc -fno-stack-protector -o no_canary test.c
checksec --file=./no_canary
# STACK CANARY: No canary found

# il valore di fs:[0x28] del processo corrente
# (richiede un piccolo programma C con inline asm, oppure GDB)
# in GDB:
# (gdb) p *(unsigned long*)(*(unsigned long*)($fs_base + 0x28))
```