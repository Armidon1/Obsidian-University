
tags: [eth, unix-hacking, information-disclosure, memory-disclosure]
capitolo: HE7 Ch.5
collegato: [[symlink_attacks]], [[race_conditions_signals]], [[openssl_security]], [[integer_overflow_attacks]]
---

# Core File Manipulation

## Idea Centrale

> Un **core file** è uno snapshot della memoria di un processo morto. Se un processo privilegiato crasha mentre ha dati sensibili in RAM, e il core finisce accessibile a utenti non privilegiati, quei dati vengono leakati.

È una vulnerabilità di **information disclosure**, non di code execution. Categoria: memory disclosure via crash dump.

---

## Cos'è un Core Dump

Quando un processo crasha (segfault, abort, signal fatale non gestito), il kernel può salvare su disco l'intero stato di memoria del processo.

Contenuto di un core file:
- Stack completo (variabili locali, return address, argomenti)
- Heap completo (memoria allocata dinamicamente)
- Segmenti dati statici
- Stato dei registri CPU al momento del crash
- Memory mapping del processo

### Uso legittimo: post-mortem debugging

```bash
gdb /usr/bin/program /tmp/core.12345
(gdb) bt              # stack trace al momento del crash
(gdb) info registers  # stato CPU
(gdb) x/100x $rsp     # dump memoria dallo stack pointer
(gdb) info proc mappings
```

Indispensabile per debuggare crash difficili da riprodurre — anche per chi sviluppa exploit, per capire perché un tentativo crasha invece di funzionare.

---

## Perché è un Problema di Sicurezza

Il core contiene **tutto ciò che il processo aveva in RAM**. Se il processo è privilegiato e ha caricato dati sensibili:

| Processo | Cosa finisce nel core |
|---|---|
| ftpd, sshd, login | Hash da `/etc/shadow` letti per autenticazione |
| Apache + mod_ssl | Chiave privata TLS → vedi [[openssl_security]] |
| sudo | Password utente appena digitata |
| Database server | Dati di altri utenti, credenziali di connessione |
| GnuPG, ssh-agent | Chiavi private decrittate in RAM |

Se il core file è **world-readable**, un utente non privilegiato può copiarlo ed estrarne i segreti offline.

---

## Case Study HE7 — FTPD + PASV pre-auth

### Il bug

Vecchie versioni di `ftpd` crashavano se il client inviava il comando `PASV` (passive mode) **prima di autenticarsi**:

```
client → server: PASV          ← prima di USER / PASS
server: *crash*
kernel: scrive core dump
```

### Perché il core era pericoloso

1. `ftpd` gira **come root** all'avvio (bind sulla porta 21, porta privilegiata)
2. Nella fase pre-auth, `ftpd` ha già letto `/etc/shadow` in memoria (pronto a verificare login)
3. Il crash avviene mentre `ftpd` è ancora root → core file owned by root
4. Bug aggiuntivo: il core veniva scritto in `/` (root del filesystem) con permessi **world-readable** (mode 644)

### L'exploit

```bash
# Da utente non privilegiato sulla vittima:
$ ls -la /core
-rw-r--r-- 1 root root 8388608 /core      ← world-readable

$ cp /core /tmp/core_copy

# Estrazione degli hash (formato shadow $id$salt$hash)
$ strings /tmp/core_copy | grep -E '^\$[0-9a-z]+\$'
$6$xyz$abcdef...     ← hash di root
$6$abc$ghijkl...     ← hash di altri utenti

# Cracking offline
$ john /tmp/extracted_hashes
$ hashcat -m 1800 hashes.txt wordlist.txt   # -m 1800 = sha512crypt
```

Risultato: utente non privilegiato → hash → cracking offline → login privilegiato.

---

## Classe di Vulnerabilità

Pattern generale:

```
processo privilegiato carica dati sensibili in RAM
            ↓
trigger di crash (bug, input malformato, signal)
            ↓
kernel scrive core dump su disco
            ↓
core file accessibile a utenti non privilegiati
            ↓
estrazione segreti offline
```

Modi per triggerare il crash:
- Input malformato che causa SIGSEGV ([[integer_overflow_attacks]] che non riescono a sfruttare l'exec → almeno crashano)
- Format string bug che crasha
- Race condition che lascia il processo in stato incoerente → crash ([[race_conditions_signals]])
- Comando inatteso pre-auth (come PASV nel caso FTPD)
- Signal fatale iniettato dall'esterno

---

## Difese

### `ulimit -c` — controllo a livello processo

```bash
ulimit -c              # mostra il limite corrente di dimensione core
ulimit -c 0            # disabilita core dump per shell e processi figli
ulimit -c unlimited    # abilita senza limite
```

Permanente di sistema in `/etc/security/limits.conf`:

```
*    hard    core    0
```

### Linux moderno — protezione automatica SUID

Il kernel Linux di default **non dumpa core di processi setuid**, esattamente per evitare questo leak:

```bash
cat /proc/sys/fs/suid_dumpable
# 0 = nessun core per binari SUID (default sicuro)
# 1 = core normale anche per SUID (insicuro)
# 2 = core dumpato ma owned root, mode 600 (compromesso)
```

### systemd-coredump

Su sistemi systemd, i core non finiscono più in `/` o `core.PID` ma sono catturati centralmente:

```bash
coredumpctl list           # cores registrati
coredumpctl info <PID>     # dettagli
coredumpctl gdb <PID>      # apri in gdb direttamente
```

Salvati in `/var/lib/systemd/coredump/` con permessi root-only e compressi.

### core_pattern

```bash
cat /proc/sys/kernel/core_pattern
# path letterale, oppure |programma che riceve il core su stdin
# su sistemi moderni tipicamente: |/lib/systemd/systemd-coredump
```

---

## Discovery (pentest)

```bash
# Cerca core file ovunque
find / -name "core" -o -name "core.*" 2>/dev/null

# Location storiche da controllare
ls -la / /tmp /var /home/*/

# File grandi con nome core (i core sono voluminosi)
find / -type f -size +1M -name "core*" 2>/dev/null

# Verifica le protezioni di sistema
cat /proc/sys/fs/suid_dumpable
cat /proc/sys/kernel/core_pattern
ulimit -c
```

Un core owned by root e world-readable = potenziale jackpot. Su sistemi moderni con systemd l'accesso a `/var/lib/systemd/coredump/` è limitato → meno fruttuoso ma da verificare comunque per misconfigurazioni.

---

## TL;DR esame

1. Core file = snapshot della memoria di un processo crashato (stack + heap + registri)
2. Uso legittimo = post-mortem debugging in gdb
3. Rischio = se processo privilegiato crasha con dati sensibili in RAM (hash shadow, chiavi TLS, password) e il core è accessibile → leak
4. Caso HE7: FTPD crasha su PASV pre-auth → core world-readable in `/` → contiene hash da `/etc/shadow` → cracking offline → root
5. Classe: information disclosure via crash dump
6. Difese: `ulimit -c 0`, `fs.suid_dumpable=0` (default Linux moderno), systemd-coredump con permessi restrittivi
7. Discovery: `find / -name "core*"`, controlla owner e permessi

---

## Concetto Chiave

Il core dump è un **trade-off**: utile per il sysadmin (debug di crash), pericoloso per la sicurezza (espone memoria). Il punto da ricordare per l'esame non è il bug FTPD specifico, ma la **categoria**: qualsiasi crash di un processo privilegiato è un potenziale leak di memoria se il core non è protetto. È il parente "passivo" di Heartbleed ([[openssl_security]]) — lì la memoria viene leakata senza crash via out-of-bounds read, qui viene leakata col crash via core dump. In entrambi i casi: memoria di un processo privilegiato che finisce in mano sbagliata.