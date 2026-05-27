# SUID Binaries

> [!abstract] In una riga Il SUID bit fa girare un programma con i privilegi del **proprietario del file**, non di chi lo lancia. È il meccanismo che permette a `passwd` di funzionare — ed è anche **l'amplificatore** che trasforma ogni bug userspace in privilege escalation. _"SUID root files kill. Period."_ (HE7)

## 0. Contesto — File and Directory Permissions

In UNIX _tutto è un file_ con permessi associati: binari, file di configurazione, device. Se i permessi sono deboli — out of the box o per mano dell'admin — la sicurezza dell'intero sistema crolla. HE7 individua **due avenue di abuso principali**:

1. **File SUID/SGID root** — l'oggetto di questa nota.
2. **File world-writable** — file/script/config scrivibili da chiunque. Se un file di config letto da root, uno script eseguito da root (cron!), o un binario è world-writable, l'attaccante lo modifica e ottiene esecuzione come root. Un binario **SUID root _e_ world-writable** è il jackpot: lo si sovrascrive direttamente.

Caso a parte, i **device** (`/dev`): permessi sbagliati su `/dev/kmem`, `/dev/mem` o sul disco raw = root garantito, perché leggi/scrivi direttamente la memoria del kernel o il filesystem bypassando ogni controllo → stessa idea di `[[kernel_flaws]]` (`/proc/pid/mem`).

## 1. Cos'è il SUID bit (e SGID, e sticky)

Il modello di permessi UNIX ha 3 bit standard (`rwx`) per owner/group/other, più **3 bit speciali**:

|Bit|Octal|Su un file eseguibile|Su una directory|
|---|---|---|---|
|**SUID**|4000|gira con EUID = owner del file|(nessun effetto standard)|
|**SGID**|2000|gira con EGID = group del file|nuovi file ereditano il group della dir|
|**Sticky**|1000|(storico: text segment)|solo l'owner del file può rinominarlo/cancellarlo|

Nel `ls -l` il SUID compare come `s` al posto della `x` dell'owner: `-rwsr-xr-x`. SGID = `s` nel campo group. Se il bit speciale è settato **ma manca la `x`**, appare in **maiuscolo** (`S`) — di solito segnale di un errore di configurazione.

```
-rwsr-xr-x  1 root root  /usr/bin/passwd
   ^
   SUID: chiunque esegue passwd, ma il processo gira come root
```

## 2. RUID / EUID / SUID — il concetto che conta

Ogni processo porta (almeno) tre UID:

- **RUID** (real) — chi _ha lanciato_ il processo. Non cambia.
- **EUID** (effective) — l'identità usata per i **controlli di permesso**. È questa che conta.
- **SUID** (saved) — copia "parcheggiata", per poter rilasciare e ri-acquisire privilegi.

All'`execve()` di un binario SUID root: `RUID = utente`, **`EUID = 0`**, `SUID(saved) = 0`. Il kernel fa i check sull'EUID → il processo _è_ root ai fini pratici.

> [!important] Privilege dropping — la fonte di mezza categoria di bug Un programma SUID ben scritto **rilascia i privilegi** appena possibile. Le primitive non sono equivalenti:
> 
> - `seteuid(uid)` — rilascio **temporaneo**: l'EUID cambia ma `SUID(saved)=0` resta → i privilegi si possono **riprendere**. Se l'attaccante ottiene code exec dopo un `seteuid`, può rifare `seteuid(0)`.
> - `setuid(uid)` chiamato da EUID 0 — rilascio **permanente**: azzera RUID/EUID/SUID. Irreversibile.
> - `setresuid()` — controllo esplicito dei tre, il modo _corretto_ e leggibile.
> 
> Bug classici: rilasciare l'UID ma scordare il GID; usare `seteuid` dove serviva `setuid`; non controllare il valore di ritorno (`setuid` **può fallire**, es. per `RLIMIT_NPROC`, e il processo prosegue da root credendo di averli rilasciati — classe di bug storica vista in Sendmail).

## 3. Perché esiste — i SUID legittimi

Alcune operazioni richiedono privilegi per definizione e non c'è modo di farle da utente normale:

- **`passwd`** — deve scrivere `/etc/shadow`, leggibile solo da root. Archetipo del SUID.
- **`su` / `sudo`** — la transizione di privilegio _è_ il loro scopo.
- **`ping`** — storicamente serviva accesso ai raw socket (vedi §9: oggi non è più SUID).
- **`mount` / `umount`, `fusermount`** — montaggio filesystem.

HE7 è netto: la maggior parte dei vendor _"slap on the SUID bit like it was going out of style"_. Il problema non sono i SUID necessari, è la **proliferazione** di SUID non necessari.

## 4. Perché sono pericolosi — l'ombrello del Ch. 5

Punto centrale, e HE7 lo dice esplicitamente:

> _Buffer overflow, race conditions, and symlink attacks are virtually useless unless the program is SUID root._

Il SUID non è _di per sé_ una vulnerabilità: è l'**amplificatore**. Quasi ogni attacco di questo capitolo ha come precondizione "il processo bersaglio gira come root" — e nella stragrande maggioranza dei casi _quel processo è root perché è un binario SUID_. Senza SUID, lo stesso bug ti dà solo i tuoi stessi privilegi: inutile.

Tutte le note del capitolo, raccolte sotto l'ombrello:

|Nota|Cos'è davvero|Ruolo del SUID|
|---|---|---|
|`[[integer_overflow_attacks]]`, `[[dangling_pointers]]`|memory corruption nel binario|il binario è SUID → l'exec del payload è root|
|`[[symlink_attacks]]`|il SUID segue un symlink piazzato dall'attaccante|legge/scrive file come root|
|`[[race_conditions_signals]]` / `[[toctou]]`|finestra check→use nel SUID|l'azione vinta dalla race è root|
|`[[shared_library_hijacking]]`|far caricare al SUID una lib ostile|codice attaccante eseguito come root|
|`[[core_file_manipulation]]`|il SUID crasha e dumpa memoria|memory disclosure di un processo root|

In una frase, il filo conduttore del capitolo nella sua forma locale: **un SUID root + un qualsiasi bug di parsing/logica/memoria = privilege escalation**. È la versione "locale" del pattern _servizio root + parsing complesso + no auth = bug factory_ — dove "no auth" è implicito (il binario lo esegui tu).

## 5. Enumeration — cosa fa l'attaccante appena entra

Primo gesto dopo aver ottenuto un account utente: censire i SUID/SGID.

```bash
find / -type f -perm -4000 -ls 2>/dev/null   # SUID
find / -type f -perm -2000 -ls 2>/dev/null   # SGID
```

`-perm -4000`: il `-` significa _"almeno questi bit"_ (non "esattamente"). Trova ogni file con il SUID bit, a prescindere dal resto.

L'attaccante poi **non** guarda i SUID standard (`passwd`, `su`, `mount`...): cerca **l'anomalia** — binari custom, di vendor, fuori posto, o con storia di vulnerabilità. HE7 porta l'esempio di **`dosemu`**: la sua stessa documentazione dice di _non_ eseguirlo SUID root, eppure sul sistema di test era SUID e senza la restrizione in `/etc/dosemu.users`. È l'archetipo del **SUID non necessario per misconfigurazione** — esattamente ciò che l'attaccante cerca.

## 6. GTFOBins — quando il binario "legittimo" è l'exploit

Spesso non serve nessun bug: basta un binario SUID che, _per design_, sa eseguire comandi o leggere/scrivere file arbitrari. Se gira come root, quella feature legittima diventa privesc.

**[GTFOBins](https://gtfobins.github.io)** è il catalogo di riferimento: per ogni binario elenca come abusarlo se è SUID (o sudo, o con capability). Esempi tipici:

```bash
# find SUID root  →  -exec spawna una shell; -p tiene i privilegi
find . -exec /bin/sh -p \; -quit

# bash SUID root  →  -p evita il drop automatico dei privilegi
bash -p

# less / more / man SUID  →  da pager:  !/bin/sh
# vim SUID  →  :!/bin/sh   oppure  :py import os;os.execl(...)
# awk SUID  →  awk 'BEGIN{system("/bin/sh")}'
# cp SUID   →  sovrascrivi /etc/passwd o un altro SUID
# env SUID  →  env /bin/sh -p
```

> [!note] Perché `-p` ovunque Le shell moderne, all'avvio, se rilevano `EUID != RUID` **rilasciano l'EUID** per sicurezza. Il flag `-p` (privileged) disattiva quel drop. Senza `-p`, una `/bin/sh` lanciata da un SUID restituirebbe una shell _non_ privilegiata.

## 7. Pattern di exploitation

Oltre a GTFOBins, le classi ricorrenti quando il SUID è custom o buggato:

- **CVE noto / memory corruption** — il SUID ha un overflow o UAF: si lancia l'exploit (`[[integer_overflow_attacks]]`, `[[dangling_pointers]]`).
- **PATH hijacking** — il SUID invoca un altro programma per **nome relativo** (`system("ls")`, `execlp("backup", ...)`). L'attaccante mette un `ls` malevolo in testa al `PATH`.
- **Command injection** — il SUID passa input non sanitizzato a `system()`/`popen()` → metacaratteri di shell.
- **Symlink / TOCTOU** — `[[symlink_attacks]]`, `[[toctou]]`.
- **SUID world-writable** — se hai permesso di scrittura sul binario stesso, lo sostituisci e basta.
- **Library hijacking residuo** — `LD_PRELOAD` è bloccato (vedi §8), ma restano RPATH, lib mancanti, ecc. → `[[shared_library_hijacking]]`.

## 8. Cosa il sistema già difende — le mitigazioni "secure-execution"

Il SUID non è terra di nessuno: all'`execve` di un binario SUID il kernel attiva la **secure-execution mode** (flag `AT_SECURE`), e loader/libc reagiscono:

- **`LD_PRELOAD` e `LD_LIBRARY_PATH` vengono ignorati** per i binari SUID. È _il_ motivo per cui il preload classico non funziona contro un SUID — e perché `[[shared_library_hijacking]]` contro i SUID deve ripiegare su RPATH o lib mancanti.
- **Niente core dump** di default per i processi SUID (`fs.suid_dumpable = 0`) → `[[core_file_manipulation]]`.
- Le **shell** rilasciano i privilegi se `EUID != RUID` (da qui il flag `-p`).
- L'opzione di mount **`nosuid`** disattiva del tutto il SUID bit su un filesystem (standard per `/tmp`, `/home`, supporti rimovibili).

## 9. Stato moderno — capabilities, il superamento del SUID

Il limite del SUID è la **granularità zero**: `EUID = 0` significa _tutto_ il potere di root, anche se al programma serviva una sola facoltà. A `ping` non serviva poter leggere `/etc/shadow` — gli serviva solo aprire raw socket.

Linux ha spezzato `root` in ~40 **capabilities** indipendenti. Oggi:

```bash
getcap /usr/bin/ping
# /usr/bin/ping cap_net_raw=ep      ← niente SUID bit
```

`ping` non è più SUID root su una distro moderna: ha la file capability `CAP_NET_RAW`. Si gestiscono con `getcap` / `setcap`. Risultato: la lista dei SUID su un sistema 2026 è molto più corta di quella di HE7 (2012).

> [!warning] Le capabilities non sono una bacchetta magica Alcune capability **sono** root travestito: `CAP_SYS_ADMIN` (così potente da essere chiamata "il nuovo root"), `CAP_DAC_OVERRIDE` (ignora ogni permesso su file), `CAP_SETUID`, `CAP_SYS_MODULE`, `CAP_SYS_PTRACE`. Un binario con una di queste è pericoloso quanto un SUID root. GTFOBins cataloga anche gli abusi via capability.

Altri tasselli moderni: **`no_new_privs`** (un processo e i suoi figli non possono più guadagnare privilegi via SUID — usato da seccomp e dai sandbox), `NoNewPrivileges=` negli unit systemd, e il confinamento **SELinux/AppArmor** — che, come nota HE7, ha già fermato exploit SUID perché _un processo confinato non può fare più di quanto possa il suo parent_.

## 10. Sticky bit e directory world-writable (`/tmp`)

`/tmp` deve essere scrivibile da tutti (`1777`), ma senza protezione _chiunque potrebbe cancellare o rinominare i file di chiunque_ — il che abilita in pieno i `[[symlink_attacks]]` e i `[[toctou]]`: sostituisco il tuo file con un symlink tra il tuo check e la tua write.

Il **sticky bit** sulla directory (`+t`, octal `1000`, la `t` finale in `drwxrwxrwt`) chiude questo: in una dir con sticky bit, **solo l'owner del file** (o l'owner della dir, o root) può rinominarlo/cancellarlo. È la difesa base che rende `/tmp` non completamente ostile.

Mitigazioni moderne che si aggiungono allo sticky bit:

- **`fs.protected_symlinks`** / **`fs.protected_hardlinks`** (sysctl, on by default) — un processo non segue un symlink in una dir sticky+world-writable se il symlink non è suo. Disinnesca alla radice gran parte dei symlink attack su `/tmp`.
- **`PrivateTmp=yes`** negli unit systemd — ogni servizio ottiene un `/tmp` privato via mount namespace: due processi non si vedono nemmeno i file temporanei.

## 11. Countermeasures (sintesi HE7 + moderno)

- **Inventario e potatura**: `find / -perm -4000` (e `-2000`), e per _ogni_ file chiedersi se il SUID è davvero necessario — man page, HOWTO, doc del progetto. HE7: rimarrai sorpreso da quanti non servono. Testare in ambiente di prova prima di togliere bit a tappeto.
- **`nosuid`** come opzione di mount su tutto ciò che non deve eseguire SUID (`/tmp`, `/home`, `/mnt`, removibili).
- **Capabilities** al posto del SUID root dove possibile (§9).
- **`no_new_privs`**, sandbox seccomp, `NoNewPrivileges=` per i servizi.
- **SELinux / AppArmor** per confinare anche ciò che resta SUID.
- Niente **SUID su script** (ignorato dai kernel moderni proprio per le race; storicamente disastroso).

## 12. Taglio Q5 — codice C

Esempio minimo nel formato d'esame (codice → vettore → attacco):

```c
/* compilato e installato -rwsr-xr-x root root  →  SUID root */
int main(void) {
    setuid(0);
    system("ls -l /var/backups");   // VULN: "ls" per nome relativo
    return 0;
}
```

**Vettore.** `system()` esegue `/bin/sh -c "ls ..."`, e `sh` risolve `ls` tramite `PATH`, che è **ereditato dall'attaccante**.

**Attacco.**

```bash
cd /tmp
echo '/bin/sh -p' > ls && chmod +x ls
export PATH=/tmp:$PATH
/percorso/del/suid          # "ls" eseguito = la nostra shell, EUID 0
```

**Fix.** Path assoluto (`/bin/ls`), o meglio `execve` diretto senza shell, e sanitizzazione esplicita di `PATH`/ambiente all'avvio. Nota che qui `setuid(0)` _non aiuta_ — anzi rende permanente l'EUID 0 con cui gira lo shellcode.

## Collegamenti

- `[[symlink_attacks]]`, `[[toctou]]` — abusi che richiedono un SUID per avere impatto; lo sticky bit di §10 è la loro contromisura
- `[[race_conditions_signals]]` — finestre di race in un SUID
- `[[shared_library_hijacking]]` — §8 spiega _perché_ `LD_PRELOAD` non funziona contro un SUID
- `[[core_file_manipulation]]` — §8: i SUID non dumpano core di default
- `[[integer_overflow_attacks]]`, `[[dangling_pointers]]` — memory corruption che diventa privesc solo perché il binario è SUID
- `[[kernel_flaws]]` — mempodipper sfrutta proprio la transizione di privilegio `execve` + SUID; e un kernel bug rende ogni protezione SUID irrilevante