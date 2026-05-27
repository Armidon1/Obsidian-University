# World-writable Files

> [!abstract] In una riga Un file world-writable è modificabile da chiunque. Non è un problema _di per sé_ — diventa privilege escalation quando qualcosa di **privilegiato** legge, esegue o si fida di quel file. È l'altra metà, insieme ai `[[suid_binaries]]`, delle "due avenue di abuso" dei permessi secondo HE7.

## 1. Cos'è

Il permesso di scrittura per _other_ (`o+w`, l'ultimo `w` in `-rw-rw-rw-`, octal `2`): qualunque utente del sistema può modificare il file. Di solito è messo per **comodità** — esattamente come il SUID bit — e con le stesse conseguenze.

```bash
find / -perm -2  -type f -print 2>/dev/null   # file world-writable
find / -perm -2  -type d -print 2>/dev/null   # directory world-writable
find / -perm -o+w ...                          # forma equivalente
```

`-perm -2`: il `-` significa _"almeno il bit world-write è settato"_.

## 2. Il principio — chi consuma il file?

Un file world-writable conta **solo in funzione di chi lo usa**. `/tmp/scratch.txt` world-writable: irrilevante. `/etc/rc.d/rc3.d/S99local` world-writable: root compromise. La domanda da farsi sempre: _un processo privilegiato esegue, legge o si fida di questo file?_

Tassonomia "cosa è il file" → "che attacco":

|File world-writable|Chi lo consuma|Attacco|
|---|---|---|
|**Script di init / startup** (`S99local`, rc)|root, al boot|inietti comandi → root al prossimo reboot|
|**Cron job / script di cron**|root o altro, a intervallo|inietti comandi → exec privilegiata ricorrente|
|**File di config** (`sshd_config`, `sudoers`, `/etc/passwd`)|demone/programma privilegiato|cambi il comportamento; `/etc/passwd` world-writable = root immediato|
|**Startup file utente** (`.bashrc`, `.profile`, `.login`)|quell'utente, al login|aspetti che logghi → shell con i suoi privilegi|
|**Libreria condivisa**|ogni processo che la linka|code exec → `[[shared_library_hijacking]]`|
|**Binario** (peggio se anche **SUID**)|chi lo lancia|lo sostituisci → `[[suid_binaries]]`|

## 3. I due casi HE7

### Caso A — startup script world-writable

`/etc/rc.d/rc3.d/S99local` è world-writable. Al boot viene eseguito **come root**. L'attaccante vi appende una riga:

```bash
echo '/bin/cp /bin/sh /tmp/.sh ; /bin/chmod 4755 /tmp/.sh' >> /etc/rc.d/rc3.d/S99local
```

Al prossimo reboot, root crea una copia di `sh` in `/tmp/.sh` e la rende **SUID root** (`4755`). L'attaccante a quel punto esegue `/tmp/.sh` e ottiene una shell root. È il loop completo: world-writable → esecuzione privilegiata → `[[suid_binaries|SUID]]` shell come backdoor persistente.

### Caso B — directory world-writable e il principio che conta

`/home/public` è una **directory** world-writable. Qui scatta il punto più importante della sezione:

> [!important] Directory permissions > file permissions Creare, cancellare o rinominare un file è governato dai permessi della **directory contenitore**, non da quelli del file. Per `rm`/`mv` di un file ti servono `w`+`x` sulla _dir_; i permessi del file stesso non c'entrano.
> 
> Conseguenza: in una directory world-writable, un file `-r--r--r--` (o persino `chmod 000`) di proprietà di un altro utente **può comunque essere cancellato e ricreato** da chiunque. Il file sembra protetto, la directory dice il contrario — e vince la directory.

Quindi in `/home/public` l'attaccante usa `mv` per **sostituire** il `.login` o `.bashrc` di un utente — anche se quei file non sono scrivibili — con una versione che crea una shell SUID. Quando l'utente logga, la backdoor è pronta.

Questo principio è anche la radice di mezzo capitolo: è ciò che rende possibili i `[[symlink_attacks]]` e i `[[toctou]]` in `/tmp` (sostituire un file con un symlink tra check e use) — e il motivo per cui `/tmp` ha bisogno dello **sticky bit** (vedi `[[suid_binaries]]` §10).

## 4. La causa a monte — umask

I file non nascono world-writable per caso: è la **umask** del processo che li crea a deciderlo. La umask è la maschera di bit _tolti_ ai permessi di default. Una umask sana (`022`) → file `644`, dir `755`: niente world-write. Una umask lasca (`000`, `002`), o un processo/installer che fa un `chmod` esplicito troppo permissivo, produce file world-writable. Auditare la umask di servizi e script di installazione è prevenzione a monte.

## 5. Countermeasures

- **Censire e correggere**: `find / -perm -2 -type f` e `-type d`. Per ogni risultato, chiedersi se c'è un _motivo valido_. File di init, config di sistema, startup utente → mai world-writable. Eccezione legittima: alcuni device in `/dev`. Testare le modifiche.
- **`umask`** restrittiva (`022` o `027`) per shell, servizi e script di installazione.
- **Sticky bit** sulle directory che _devono_ restare world-writable (`/tmp`, `/var/tmp`) → `[[suid_binaries]]` §10. Limita cancellazione/rename al solo owner del file.
- **Attributi estesi del filesystem** — HE7 li cita di sfuggita, vale la pena espandere:
    - Linux **`chattr +i`** (immutable): il file non si può modificare, rinominare o cancellare — nemmeno da root — finché il flag è attivo. Ideale per i file di config critici.
    - **`chattr +a`** (append-only): si può solo aggiungere in coda. Perfetto per i log: un attaccante non può ripulirli.
    - BSD: flag **`schg`** (system immutable) + **securelevel**: a securelevel ≥ 1 i flag di sistema non sono rimovibili a runtime, neanche da root — per toglierli serve riavviare in single-user. Questo chiude il buco "tanto root fa `chattr -i`".
- **Integrity monitoring** (AIDE, Tripwire) per accorgersi se un file critico cambia.

## Collegamenti

- `[[suid_binaries]]` — la coppia HE7; un binario world-writable _e_ SUID è il jackpot; lo sticky bit (§10 di quella nota) è la difesa delle directory world-writable
- `[[symlink_attacks]]`, `[[toctou]]` — il principio "directory > file" di §3 è la loro precondizione
- `[[shared_library_hijacking]]` — una libreria world-writable è code exec diretta come root
- `[[race_conditions_signals]]` — la sostituzione di file in directory world-writable è il terreno delle race