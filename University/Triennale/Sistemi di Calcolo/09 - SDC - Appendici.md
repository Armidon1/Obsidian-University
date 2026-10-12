---
title: Appendici della dispensa
aliases:
  - SDC — Appendici
  - Sistemi di Calcolo — Appendici A-D
tags:
  - sistemi-di-calcolo
  - ascii
  - shell
  - gdb
  - valgrind
  - elettronica
source: Dispensa Sistemi di Calcolo.pdf (appendici A–D, pp. 187–224)
---

# Appendici della dispensa

> [!abstract] Scopo
> Le appendici raccolgono il materiale di supporto pratico al corso: la **tabella ASCII** (A), l'uso della **shell** bash (B: comandi, `PATH`, permessi POSIX e `chmod`, redirezione, pipe, processi in background), il **debugging** con **gdb** e **Valgrind** (C) e i **prerequisiti di elettronica** per capire i circuiti delle porte logiche del capitolo 1 (D: legge di Ohm, transistor, breadboard).
> Mappa dei concetti: [[MOC - Sistemi di Calcolo]] · Guida completa a GDB già presente nel vault: [[GDB]]

## Appendice A: tabella ASCII a 7 bit

Vedi [[Codifica ASCII]].

La codifica **ASCII** base usa **7 bit**: 128 caratteri (codici 0–127), divisi in **caratteri di controllo** (0–31) e **caratteri stampabili** (32–126). Il 127 (DEL) è anch'esso di controllo.

> [!warning] Correzione
> La dispensa parla di "127 caratteri": con 7 bit i codici sono **128** (da 0 a 127).

### Caratteri di controllo

Sono caratteri non stampabili, usati storicamente per controllare periferiche come le stampanti. La colonna C indica la sequenza di escape usata in C nelle stringhe e nei letterali `char`.

| DEC | OCT | HEX | Simbolo | C | Descrizione |
| --- | --- | --- | --- | --- | --- |
| 0 | 000 | 00 | NUL | `\0` | null char (terminatore delle stringhe C) |
| 1 | 001 | 01 | SOH | | Start of Heading |
| 2 | 002 | 02 | STX | | Start of Text |
| 3 | 003 | 03 | ETX | | End of Text |
| 4 | 004 | 04 | EOT | | End of Transmission |
| 5 | 005 | 05 | ENQ | | Enquiry |
| 6 | 006 | 06 | ACK | | Acknowledgment |
| 7 | 007 | 07 | BEL | `\a` | Bell |
| 8 | 010 | 08 | BS | `\b` | Back Space |
| 9 | 011 | 09 | HT | `\t` | Horizontal Tab |
| 10 | 012 | 0A | LF | `\n` | Line Feed (a capo su Unix) |
| 11 | 013 | 0B | VT | `\v` | Vertical Tab |
| 12 | 014 | 0C | FF | `\f` | Form Feed |
| 13 | 015 | 0D | CR | `\r` | Carriage Return (Windows usa CR LF) |
| 14 | 016 | 0E | SO | | Shift Out / X-On |
| 15 | 017 | 0F | SI | | Shift In / X-Off |
| 16 | 020 | 10 | DLE | | Data Line Escape |
| 17 | 021 | 11 | DC1 | | Device Control 1 (XON) |
| 18 | 022 | 12 | DC2 | | Device Control 2 |
| 19 | 023 | 13 | DC3 | | Device Control 3 (XOFF) |
| 20 | 024 | 14 | DC4 | | Device Control 4 |
| 21 | 025 | 15 | NAK | | Negative Acknowledgement |
| 22 | 026 | 16 | SYN | | Synchronous Idle |
| 23 | 027 | 17 | ETB | | End of Transmit Block |
| 24 | 030 | 18 | CAN | | Cancel |
| 25 | 031 | 19 | EM | | End of Medium |
| 26 | 032 | 1A | SUB | | Substitute |
| 27 | 033 | 1B | ESC | `\e` | Escape (sequenze di controllo del terminale) |
| 28 | 034 | 1C | FS | | File Separator |
| 29 | 035 | 1D | GS | | Group Separator |
| 30 | 036 | 1E | RS | | Record Separator |
| 31 | 037 | 1F | US | | Unit Separator |

### Caratteri stampabili

Sono **95**, con codici da 32 a 126.

| DEC | HEX | Car. | | DEC | HEX | Car. | | DEC | HEX | Car. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 32 | 20 | *spazio* | | 64 | 40 | `@` | | 96 | 60 | `` ` `` |
| 33 | 21 | `!` | | 65 | 41 | `A` | | 97 | 61 | `a` |
| 34 | 22 | `"` | | 66 | 42 | `B` | | 98 | 62 | `b` |
| 35 | 23 | `#` | | 67 | 43 | `C` | | 99 | 63 | `c` |
| 36 | 24 | `$` | | 68 | 44 | `D` | | 100 | 64 | `d` |
| 37 | 25 | `%` | | 69 | 45 | `E` | | 101 | 65 | `e` |
| 38 | 26 | `&` | | 70 | 46 | `F` | | 102 | 66 | `f` |
| 39 | 27 | `'` | | 71 | 47 | `G` | | 103 | 67 | `g` |
| 40 | 28 | `(` | | 72 | 48 | `H` | | 104 | 68 | `h` |
| 41 | 29 | `)` | | 73 | 49 | `I` | | 105 | 69 | `i` |
| 42 | 2A | `*` | | 74 | 4A | `J` | | 106 | 6A | `j` |
| 43 | 2B | `+` | | 75 | 4B | `K` | | 107 | 6B | `k` |
| 44 | 2C | `,` | | 76 | 4C | `L` | | 108 | 6C | `l` |
| 45 | 2D | `-` | | 77 | 4D | `M` | | 109 | 6D | `m` |
| 46 | 2E | `.` | | 78 | 4E | `N` | | 110 | 6E | `n` |
| 47 | 2F | `/` | | 79 | 4F | `O` | | 111 | 6F | `o` |
| 48 | 30 | `0` | | 80 | 50 | `P` | | 112 | 70 | `p` |
| 49 | 31 | `1` | | 81 | 51 | `Q` | | 113 | 71 | `q` |
| 50 | 32 | `2` | | 82 | 52 | `R` | | 114 | 72 | `r` |
| 51 | 33 | `3` | | 83 | 53 | `S` | | 115 | 73 | `s` |
| 52 | 34 | `4` | | 84 | 54 | `T` | | 116 | 74 | `t` |
| 53 | 35 | `5` | | 85 | 55 | `U` | | 117 | 75 | `u` |
| 54 | 36 | `6` | | 86 | 56 | `V` | | 118 | 76 | `v` |
| 55 | 37 | `7` | | 87 | 57 | `W` | | 119 | 77 | `w` |
| 56 | 38 | `8` | | 88 | 58 | `X` | | 120 | 78 | `x` |
| 57 | 39 | `9` | | 89 | 59 | `Y` | | 121 | 79 | `y` |
| 58 | 3A | `:` | | 90 | 5A | `Z` | | 122 | 7A | `z` |
| 59 | 3B | `;` | | 91 | 5B | `[` | | 123 | 7B | `{` |
| 60 | 3C | `<` | | 92 | 5C | `\` | | 124 | 7C | `\|` |
| 61 | 3D | `=` | | 93 | 5D | `]` | | 125 | 7D | `}` |
| 62 | 3E | `>` | | 94 | 5E | `^` | | 126 | 7E | `~` |
| 63 | 3F | `?` | | 95 | 5F | `_` | | | | |

(La dispensa riporta anche la colonna ottale, che vale semplicemente il valore decimale in base 8.)

> [!tip] Trucchi da ricordare
> - Le cifre `'0'`–`'9'` sono 48–57: `c - '0'` converte una cifra nel suo valore.
> - Maiuscole 65–90 e minuscole 97–122 distano **32** (`0x20`): `c ^ 0x20` scambia maiuscola e minuscola. È il motivo per cui `memcmp("ant","Ant",3) > 0` nel [[04 - SDC - Librerie standard del C#Memoria|capitolo 4]].
> - Gli hexdump che si vedono in gdb e objdump si leggono con questa tabella (es. `0x41` = `A`).

_(dispensa, pp. 187–190)_

## Appendice B: la shell dei comandi

Vedi [[Shell e Comandi Unix]].

Una **shell** è un programma che permette di inserire comandi testuali da far eseguire al sistema: un'**interfaccia a riga di comando** (*command-line interface*, CLI). La dispensa usa **bash**, la shell di default di macOS (fino a Catalina) e delle principali distribuzioni Linux.

Aprendo un terminale si attiva una shell che mostra il **prompt**, normalmente terminato da `$` seguito dal cursore: indica che la shell è **pronta a ricevere comandi**. Prima del `$` ci sono di solito utente, nome del computer e directory corrente:

```
studente@c1565:~$
```

`studente` è l'utente, `c1565` il computer, `~` la directory corrente, cioè la **home** dell'utente, che raccoglie i suoi file, directory e impostazioni.

In ogni istante la shell ha una **directory corrente**, a cui si riferiscono tutti i **percorsi relativi** (vedi [[08 - SDC - Gestione dei file#Percorsi assoluti e relativi|capitolo 8]]). Ogni comando ha la forma `nome-comando [parametri]` e si esegue con Invio.

Due tipi di comandi:

- **esterni**: `nome-comando` è un **file eseguibile**, e lanciarlo crea un **nuovo processo** (con [[fork]] + [[exec e Variabili d'Ambiente|exec]]);
- **interni** (*built-in*): eseguiti direttamente dalla shell, **senza** nuovi processi.

| Comando | Tipo | Descrizione |
| --- | --- | --- |
| `pwd` | interno | mostra il percorso assoluto della directory corrente |
| `cd` | interno | cambia la directory corrente |
| `ls` | esterno | elenca il contenuto di una directory |
| `touch` | esterno | crea un file vuoto o ne aggiorna la data di modifica |
| `mv` | esterno | rinomina o sposta un file o una directory |
| `mkdir` | esterno | crea una directory vuota |
| `rmdir` | esterno | elimina una directory vuota |
| `rm` | esterno | elimina un file o una directory |
| `cp` | esterno | copia un file o una directory |

> [!question] Perché `cd` deve essere interno?
> La directory corrente è un attributo del **processo**. Se `cd` fosse un programma esterno cambierebbe la directory del **proprio** processo figlio, che poi termina, lasciando invariata quella della shell.

### Invocazione di un comando

Se il comando è un **percorso** (assoluto o relativo) a un binario, la shell lo esegue direttamente. Altrimenti:

1. controlla se è un **alias** (una scorciatoia definita dal sistema o dall'utente, es. `alias foo="cmd --opzione"`): se sì, esegue il comando associato (ripetendo la procedura ricorsivamente se quel comando non è un percorso);
2. controlla se è una funzione **built-in** della shell;
3. cerca un **binario** con quel nome nelle directory elencate nella variabile d'ambiente **`PATH`**, separate da `:`, ad esempio

   ```
   /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
   ```

   Le directory sono esaminate **nell'ordine**: se più directory contengono un binario con lo stesso nome, vince la prima.

Il built-in **`type`** dice cosa verrà eseguito:

```
$ type type
type is a shell builtin
$ type ls
ls is aliased to `ls --color=auto'
$ type cp
cp is /bin/cp
```

Nel caso di `ls`, l'alias espande in `ls --color=auto`, e il secondo `ls` viene cercato **ignorando l'alias** (per evitare una ricorsione infinita). Si può sempre forzare un binario specifico indicandone il **percorso** (es. `/bin/ls`).

### Manipolazione del file system

```bash
pwd                       # /home/studente/Scrivania
cd /home/studente         # percorso assoluto
cd ..                     # directory genitore
cd ../Scrivania           # Scrivania della directory genitore
cd                        # torna alla home
ls [dir]                  # contenuto della directory (corrente se omessa)
ls -l [dir]               # formato lungo: tipo, permessi, dimensione, data
touch hello.c             # crea il file vuoto o ne aggiorna la data
mv hello.c hello2.c       # rinomina (se hello2.c non è una directory esistente)
mv hello.c pippo          # sposta hello.c nella directory pippo
mkdir pippo               # crea la directory
rmdir pippo               # elimina la directory se vuota
rm hello.c                # elimina il file
rm -rf pippo              # elimina la directory e tutto il contenuto (attenzione!)
cp hello.c hello-copia.c  # copia un file
cp hello.c pippo          # copia il file nella directory pippo
cp -R pippo pluto         # copia ricorsiva: se pluto non esiste, diventa la copia di pippo;
                          # se esiste, pippo viene copiata DENTRO pluto
cp -R pippo/ pluto        # copia il CONTENUTO di pippo dentro pluto
```

Esempi di `ls -l`:

```
-rw-r--r--  9 anna     staff   306 Oct  8 18:10 hello.c
drwxr-xr-x  8 studente staff   272 Sep 27 13:16 foto
```

`hello.c` è un file (`-`), leggibile e scrivibile da `anna`, di 306 byte, modificato l'8 ottobre alle 18:10. `foto` è una directory (`d`) leggibile, scrivibile e attraversabile da `studente`.

> [!note]
> In `ls -l` la seconda colonna è il **numero di hard link**, non un contatore generico (vedi [[Link Hard e Soft]]).

### Altri comandi utili

| Comando | Uso |
| --- | --- |
| `geany [file] &` | editor di testo grafico (in background con `&`) |
| `cat file` | invia il contenuto del file su stdout |
| `less file` | visualizza un file scorrendolo con le frecce (`q` per uscire) |
| `man [sezione] cmd` | documentazione: sezione 1 comandi, 2 system call, 3 librerie (es. `man 3 malloc`) |
| `env` | mostra le variabili d'ambiente (`SHELL`, `USER`, `PATH`…) |
| `head [-n 5] file` | prime n righe (default 10) |
| `tail [-n 5] file` | ultime n righe (default 10) |
| `which cmd` | percorso del binario di un comando esterno (non gestisce built-in e alias) |
| `whereis cmd` | binario e documentazione di un comando (es. `/bin/cp`, `/usr/share/man/man1/cp.1.gz`) |
| `grep parola file` | righe che contengono `parola`; `-v` quelle che non la contengono; `-n` con il numero di riga |
| `ln [-s] target nome` | crea un hard link (o simbolico con `-s`) |

> [!warning] Correzione
> Nella descrizione di `ln` la dispensa rimanda al "Paragrafo 8.3" per i link: i link sono trattati nel **§8.5**.

### Permessi POSIX e chmod

Vedi [[Permessi e Ownership]].

```
$ ls -l
lrwxrwxrwx 1 biar stud   15 ott 12 17:09 last.log -> output/file.log
drwxrwxr-x 2 biar stud 4096 ott 12 17:09 output
-rwxrwxr-x 1 biar stud    0 ott  4 15:43 test
-rw-rw-r-- 1 biar stud 8696 set 30 12:07 test.c
```

Per ogni elemento:

1. **tipo** (primo carattere): `-` file normale, `l` link simbolico, `d` directory;
2. **permessi** (9 caratteri);
3. **numero di hard link**;
4. **utente** proprietario;
5. **gruppo** proprietario;
6. **dimensione** (per le directory non si somma il contenuto: tipicamente 4096);
7. data e
8. ora dell'ultima modifica;
9. **nome** (per un link simbolico anche la destinazione).

I 9 caratteri dei permessi sono tre gruppi `rwx`, per **u**ser (proprietario), **g**roup (gruppo proprietario) e **o**ther (tutti gli altri):

| Permesso | Su un file | Su una directory |
| --- | --- | --- |
| `r` | leggere il contenuto | **elencare** gli elementi (`ls`) |
| `w` | scrivere il contenuto | creare, rinominare, eliminare elementi (serve anche `x`) |
| `x` | eseguire il file | **accedere** alla directory (`cd`) |

`-` indica l'assenza del permesso. Questa è la **notazione simbolica**.

**Notazione ottale**: ogni gruppo `rwx` è un numero di 3 bit $b_2 b_1 b_0$ (r = 4, w = 2, x = 1), quindi una cifra ottale da 0 a 7:

| Bit | Ottale | Permessi |
| --- | --- | --- |
| 000 | 0 | nessuno |
| 001 | 1 | `--x` |
| 010 | 2 | `-w-` |
| 100 | 4 | `r--` |
| 101 | 5 | `r-x` |
| 110 | 6 | `rw-` |
| 111 | 7 | `rwx` |

Tre cifre, in ordine **ugo**: `514` = `r-x` per l'utente, `--x` per il gruppo, `r--` per gli altri.

`chmod` accetta entrambe le notazioni:

```bash
chmod ugo=rwx file     # tutti i permessi a tutti
chmod u=rwx,go=r file  # rwx al proprietario, sola lettura a gruppo e altri
chmod 750 file         # rwxr-x---
chmod 741 file         # rwxr----x
chmod u+x script.sh    # aggiunge l'esecuzione al proprietario
```

> [!warning] Correzione
> Nell'esempio della dispensa `chmod u=rwx, go=r file` c'è uno **spazio** dopo la virgola: la forma corretta è `chmod u=rwx,go=r file` (con lo spazio, `go=r` verrebbe interpretato come nome di file).

### Redirezione di stdin, stdout e stderr

Vedi [[File Descriptor]].

| Sintassi | Effetto |
| --- | --- |
| `cmd id> file` | redirige il canale `id` sul file, **sovrascrivendolo** (`id` omesso = 1, stdout) |
| `cmd id>> file` | come sopra, ma **appende** in coda al file |
| `cmd &> file` | redirige **sia stdout che stderr** sul file (`&>>` per appendere) |
| `cmd < file` | il file diventa lo stdin del comando |
| `cmd1 \| cmd2` | **pipe**: lo stdout di `cmd1` diventa lo stdin di `cmd2` |

```bash
ls -l > file.log                  # equivale a ls -l 1> file.log
ls -l 1> out.log 2> error.log     # stdout e stderr su file diversi
ls -l >> file.log                 # append
ls -l &> file.log                 # entrambi i canali
ls -l | grep str                  # solo le righe di ls che contengono "str"
```

La **pipe** riflette la filosofia UNIX: ogni utility fa **una sola cosa** di base, e gli obiettivi complessi si ottengono componendo le utility in una **pipeline**.

In C la redirezione si ottiene chiudendo un descrittore e aprendo un file (che prende il descrittore più piccolo libero), oppure con `dup2`. È quello che fa la shell tra la `fork` e la `exec`.

### Esecuzione in background e terminazione

Di default un comando gira in **foreground**: la shell aspetta che termini e l'input da tastiera va allo stdin del processo. Due modi per riavere la shell:

1. lanciare in foreground e poi **sospendere** il processo con **CTRL+Z**:

   ```
   ^Z
   [1]+  Stopped                 cmd arg1 arg2
   ```

   `1` è l'**id del job** nella shell. Poi:
   - **`fg 1`**: lo riporta in foreground;
   - **`bg 1`**: lo fa continuare in **background**. Lo stdin non è più collegato alla tastiera: se il processo prova a leggere da stdin si blocca finché non torna in foreground.

   `jobs` elenca i job della shell:

   ```
   $ jobs
   [1]+  Stopped                 cmd-1 arg1
   [2]-  Running                 cmd-2 &
   ```

2. lanciare **direttamente in background** con **`&`**:

   ```
   $ cmd &
   [1] 25818
   ```

   La shell stampa l'id del job (locale alla shell) e il **PID** (globale nel sistema). `ps` mostra i processi della shell corrente:

   ```
   $ ps
     PID TTY          TIME CMD
   19519 pts/21   00:00:00 bash
   25818 pts/21   00:00:02 cmd
   28936 pts/21   00:00:00 ps
   ```

Per **terminare** un processo:

1. se è in **foreground** nella shell corrente: **CTRL+C**, che invia una **richiesta** di terminazione (il segnale `SIGINT`): il processo può fare pulizia o anche **ignorarla**;
2. in **qualsiasi stato** e da qualsiasi shell: **`kill PID`**, che invia `SIGTERM` (anch'esso ignorabile). Se il processo non collabora, **`kill -9 PID`** invia `SIGKILL`, che **non può essere ignorato né gestito**: il sistema operativo termina il processo forzatamente.

Vedi [[Segnali]] e [[06 - SDC - Esecuzione dei programmi#Segnali|capitolo 6]].

_(dispensa, pp. 191–209)_

## Appendice C: debugging di un programma C

Il **debugging** è l'attività di analisi di un programma per trovare la causa di errori o comportamenti inattesi, con gli strumenti detti *debugging tools*.

### Compilare con le informazioni di debug

Quasi tutti gli strumenti richiedono le **informazioni di debug** (corrispondenza tra codice macchina e righe di sorgente, nomi delle variabili…), che si aggiungono con **`gcc -g`**:

```bash
gcc -g programma.c -o programma
gcc -g -m32 programma.c file.s -o programma   # anche con file assembly IA32
```

Il binario funziona esattamente come prima, ma è un po' più grande su disco.

### gdb

Vedi [[GDB]] (la guida completa nel vault).

#### Preparazione: il comando go

Il corso consiglia di definire un comando personalizzato `go` nel file `~/.gdbinit`:

```
define go
    start
    layout src
    layout regs
    focus cmd
end
```

`go` avvia il programma fermandosi all'inizio del `main` (`start`), mostra il **sorgente** e i **registri** e lascia il focus alla riga di comando.

#### Avvio e comandi

```bash
gdb ./e
```

| Categoria | Comando | Effetto |
| --- | --- | --- |
| Avvio | `go` | avvia e si ferma alla prima istruzione del `main` |
| | `run [arg ...]` | (ri)lancia il programma con eventuali argomenti |
| | `quit` (o CTRL+D) | esce da gdb |
| Esecuzione | `cont` (`c`) | riprende l'esecuzione dopo un breakpoint |
| | `step` (`s`) | esegue una singola istruzione, **entrando** nelle funzioni |
| | `next` (`n`) | esegue un'istruzione; se è una chiamata, la esegue **tutta** fino al return |
| | `finish` | esegue fino alla fine della funzione corrente |
| Breakpoint | `break e.c:20` | breakpoint alla riga 20 di `e.c` (anche file `.s`) |
| | `break e.c:20 if x == 0` | breakpoint **condizionale** |
| | `info break` | elenca i breakpoint |
| | `clear e.s:20` | rimuove il breakpoint su una posizione |
| | `delete 1` | rimuove il breakpoint numero 1 |
| Stato | `print $eax` (`p`) | contenuto di un registro |
| | `print x` | variabile nello stack frame corrente |
| | `x addr` | contenuto della memoria all'indirizzo `addr` |
| | `x $eax + 4` | memoria all'indirizzo dato da un'espressione |
| | `x/nfu addr` | memoria con un formato (vedi sotto) |
| Altri | `start` | si posiziona all'inizio del `main` (non serve con `go`) |
| | `file <eseguibile>` | carica un eseguibile |
| | `frame n` | seleziona il frame n (per ispezionare le variabili del chiamante) |
| | `where` / `backtrace` | posizione corrente / elenco dei frame attivi (vedi [[Stack Frame]]) |
| | `list` | mostra il sorgente della funzione corrente |
| | `refresh` | ridisegna lo schermo |

> [!note] `finish` su assembly scritto a mano
> `finish` funziona male sul codice assembly scritto a mano: servono **direttive di debug** che marcano inizio e fine di una funzione. Il compilatore le aggiunge automaticamente quando traduce il C.

#### Il formato nfu

In `x/nfu addr`:

- **n**: quante unità mostrare (default 1), utile per gli array;
- **f**: il formato: `x` esadecimale, `d` intero con segno, `u` senza segno, `o` ottale, `t` binario, `a` indirizzo, `c` carattere, `f` virgola mobile, `s` stringa;
- **u**: la dimensione di un'unità: `b` 1 byte, `h` 2 byte, `w` 4 byte, `g` 8 byte.

Le parti si possono omettere (si usano dei default).

```
(gdb) x/2uh addr   # due interi senza segno da 2 byte a partire da addr
(gdb) x/s addr     # una stringa C a partire da addr
(gdb) x/4xw $esp   # le prime 4 word dello stack in esadecimale
```

#### Usi tipici

- **Segmentation fault**: `run` fino al crash → `backtrace` per vedere la pila delle chiamate → `p` e `x` per ispezionare variabili, registri e memoria → `frame` per guardare le variabili dei chiamanti.
- **Analisi passo passo**: `break` all'inizio della funzione o di un ciclo → `run` → `step`/`next` → `p`/`x`.

### Valgrind

Vedi [[Valgrind]].

**Valgrind** individua molti errori comuni dei programmi C:

- **accessi non validi** alla memoria (causa di *segmentation fault*);
- uso di **variabili non inizializzate** (causa di errori logici);
- **mancata deallocazione** di blocchi (i **memory leak**, vedi [[07 - SDC - Gestione dei dati in memoria centrale#Allocazione dinamica|capitolo 7]]).

```bash
valgrind --tool=memcheck ./programma arg1 arg2   # memcheck è il tool di default
```

Struttura dell'output (ogni riga di Valgrind inizia con `==PID==`, per distinguerla dall'output del programma):

```
==22103== Memcheck, a memory error detector
==22103== Copyright (C) 2002-2015, and GNU GPL'd
==22103== Using Valgrind-3.11.0 and LibVEX;
==22103== Command: ./programma arg1 arg2
// output del programma
==22103== // eventuali errori, segnalati appena rilevati
==22103== HEAP SUMMARY:
==22103==     in use at exit: 19,628 bytes in 12 blocks
==22103==   total heap usage: 229 allocs, 217 frees, 98,068 bytes allocated
==22103== LEAK SUMMARY:
==22103==    definitely lost: 0 bytes in 0 blocks
==22103==    indirectly lost: 0 bytes in 0 blocks
==22103==      possibly lost: 0 bytes in 0 blocks
==22103==    still reachable: 19,628 bytes in 12 blocks
==22103==         suppressed: 0 bytes in 0 blocks
==22103== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```

- intestazione: il tool (`memcheck`), licenza e versione;
- il comando eseguito;
- l'output del programma, con gli **errori** di Valgrind inseriti nel punto in cui vengono rilevati;
- il **report sull'heap**: Valgrind traccia `malloc`, `calloc`, `realloc` e `free`, e nell'`HEAP SUMMARY` e nel `LEAK SUMMARY` segnala la memoria mai liberata (`--leak-check=full` per i dettagli).

#### Esempio: lettura di memoria non inizializzata

```c
// unitialized-var.c
#include <stdio.h>
int main() {
    int a;
    printf("%d\n", a);   // riga 5: a non è mai stata inizializzata
    return 0;
}
```

Eseguito normalmente stampa un valore qualsiasi e sembra funzionare. Sotto Valgrind:

```
==11028== Use of uninitialised value of size 4
==11028==    at 0x40A621B: _itoa_word (_itoa.c:179)
==11028==    by 0x40AA1F1: vfprintf (vfprintf.c:1631)
==11028==    by 0x40B05B5: printf (printf.c:33)
==11028==    by 0x804842B: main (unitialized-ptr.c:5)
==11028== Conditional jump or move depends on uninitialised value(s)
...
==11028== ERROR SUMMARY: 22 errors from 6 contexts
```

Un solo errore nel codice produce **molti** errori a runtime. Strategia: correggere **il primo errore**, ricompilare e rieseguire Valgrind. Con **`--track-origins=yes`** Valgrind risale all'origine del valore:

```
==11105== Uninitialised value was created by a stack allocation
==11105==    at 0x804841C: main (unitialized-ptr.c:5)
```

È una variabile locale (*stack allocation*) mai inizializzata. (Valgrind indica la riga 5, ma la dichiarazione è alla riga 4: non è sempre preciso.) La correzione è `int a = 1;`. Il valore stampato prima era **garbage**: dipende dal contesto di esecuzione e varia tra macchine e sistemi.

> [!note]
> Nell'output l'eseguibile risulta chiamato `unitialized-ptr` invece di `unitialized-var`: è un'incoerenza dell'esempio della dispensa, che non cambia nulla.

#### Esempio: salto condizionato su un valore non inizializzato

```c
#include <stdio.h>
void foo(int *a) {
    if (a == NULL)      // a non è inizializzato
        return;
    printf("a is %d\n", *a);
}
int main() {
    int *a;             // puntatore non inizializzato
    foo(a);
    return 0;
}
```

Il programma stampa `a is -16219251` e sembra funzionare, ma Valgrind segnala:

```
==24424== Conditional jump or move depends on uninitialised value(s)
==24424==    at 0x40053E: foo (uninit-var.c:5)
==24424==    by 0x40056E: main (uninit-var.c:12)
==24424== ERROR SUMMARY: 1 errors from 1 contexts
```

L'`if` dipende da un valore non inizializzato (e dereferenziare `a` potrebbe causare un segmentation fault).

Altri errori rilevati da Valgrind:

- accesso (lettura, scrittura, esecuzione) a memoria **non valida** (es. oltre la fine di un array allocato con `malloc`);
- **memory leak**;
- **invalid free**: `free` su puntatori non validi o doppia `free`.

_(dispensa, pp. 210–220)_

## Appendice D: prerequisiti di elettronica

Nozioni di base per capire i circuiti delle [[Porte Logiche]] del [[01 - SDC - Cosa è un sistema di calcolo#Porte logiche|capitolo 1]].

### Resistenze e prima legge di Ohm

Il circuito più semplice: **batteria**, **interruttore**, **resistenza** e **LED** (diodo a emissione luminosa). L'interruttore controlla l'accensione del LED.

![[SDC-p220-1.png]]

Lo stesso circuito disegnato con due convenzioni: a sinistra la batteria è esplicita; a destra il polo positivo è indicato con la tensione (+5V) e quello negativo con il simbolo della **massa** (la "piramide rovesciata" a trattini).

Il **LED**, come ogni diodo, ha due terminali: l'**anodo**, più lungo, collegato al polo **positivo**, e il **catodo**, più corto, collegato al **negativo**. Per limitare la corrente e non danneggiarlo si usa una **resistenza**, secondo la **prima legge di Ohm**:

$$V = R \cdot i$$

con V in **Volt**, R in **Ohm** (Ω) e i in **Ampere**. Un LED lavora tipicamente tra **10 e 30 mA**. Con 5 V servono quindi resistenze tra

$$R = \frac{5}{0.030} \approx 166\,\Omega \quad\text{e}\quad R = \frac{5}{0.010} = 500\,\Omega$$

(per questo nei circuiti del corso si usano 220 Ω).

#### Codice colori delle resistenze

Le resistenze si producono in valori discreti, indicati da **bande colorate**:

| Colore | 1ª cifra | 2ª cifra | 3ª cifra | Moltiplicatore | Tolleranza |
| --- | --- | --- | --- | --- | --- |
| Nero | 0 | 0 | 0 | 10⁰ | |
| Marrone | 1 | 1 | 1 | 10¹ | 1% |
| Rosso | 2 | 2 | 2 | 10² | 2% |
| Arancio | 3 | 3 | 3 | 10³ | – |
| Giallo | 4 | 4 | 4 | 10⁴ | – |
| Verde | 5 | 5 | 5 | 10⁵ | 0.5% |
| Blu | 6 | 6 | 6 | 10⁶ | 0.25% |
| Viola | 7 | 7 | 7 | 10⁷ | 0.10% |
| Grigio | 8 | 8 | 8 | 10⁸ | 0.05% |
| Bianco | 9 | 9 | 9 | 10⁹ | – |
| Oro | – | – | – | 10⁻¹ | 5% |
| Argento | – | – | – | 10⁻² | 10% |

**Esempio 1**: resistenza a **4 bande**: rosso (2), nero (0), argento (moltiplicatore 10⁻²), oro (tolleranza 5%):

![[SDC-p222-1.png]]

$$R = 20 \cdot 10^{-2} = 0.2\,\Omega \pm 5\%$$

**Esempio 2**: resistenza a **5 bande**: rosso (2), rosso (2), nero (0), nero (moltiplicatore 10⁰), marrone (tolleranza 1%):

![[SDC-p222-2.png]]

$$R = 220 \cdot 10^0 = 220\,\Omega \pm 1\%$$

È proprio la resistenza adatta al circuito del LED.

### Transistor

I **transistor** hanno due funzioni: possono fare da **interruttori controllati elettricamente** (dalla presenza di corrente su un terminale, invece che da un pulsante) e possono **amplificare** un segnale. Per le porte logiche interessa la prima.

La dispensa usa transistor **NPN**, con tre terminali: **collettore**, **base** ed **emettitore**. Semplificando: con il collettore collegato al positivo e l'emettitore a massa, una **piccola corrente sulla base** fa fluire corrente tra collettore ed emettitore, e il transistor si comporta come un **interruttore chiuso**; senza corrente sulla base è un **interruttore aperto**.

![[SDC-p222-3.png]]

La resistenza da **10 kΩ** sulla base limita la corrente a 5 / 10000 = **0.5 mA**. Chiudendo l'interruttore, la base riceve corrente, il transistor "si chiude" e la corrente da +5V attraversa la resistenza da 220 Ω e il LED fino a massa: il **LED si accende**. È il mattone delle porte AND (transistor in serie), OR (in parallelo) e NOT del capitolo 1.

### Breadboard

Una **breadboard** è una base che permette di montare circuiti, anche complessi, **senza saldare** i componenti: ideale per la prototipazione.

![[SDC-p223-1.png]]

Lungo i lati lunghi ci sono due file orizzontali, una per il **positivo** (rossa) e una per il **negativo** (blu), che corrono per tutta la lunghezza. Al centro ci sono molte file corte, perpendicolari: i rettangoli neri mostrano quali fori sono **collegati elettricamente** tra loro. Nei fori si inseriscono i cavetti (*jumper*) e i terminali dei componenti. Un **Arduino** alimenta la breadboard a **5 V** prendendo corrente dalla porta USB.

![[SDC-p224-1.png]]

Il circuito della Figura D.1.1 montato sulla breadboard: pulsante, resistenza e LED rosso, alimentati dall'Arduino.

> [!warning] Correzione
> La dispensa numera entrambe le figure della breadboard "D.3.1": la seconda, citata nel testo come Figura D.3.2, è il circuito di Figura D.1.1 montato sulla breadboard.

L'Arduino e la sua programmazione sono trattati in [[04 - SO - Hardware e AVR|Sistemi Operativi]].

_(dispensa, pp. 220–224)_
