---
title: Gestione dei file
aliases:
  - SDC — Come vengono gestiti i file
  - Sistemi di Calcolo — Capitolo 8
tags:
  - sistemi-di-calcolo
  - file-system
  - inode
  - file-descriptor
  - link
source: Dispensa Sistemi di Calcolo.pdf (cap. 8, pp. 170–186)
---

# Gestione dei file

> [!abstract] Scopo del capitolo
> Il **file system** gestisce la memoria esterna, il livello più basso, grande e lento della gerarchia di memoria. Il capitolo descrive l'**albero delle directory** (FHS, percorsi assoluti e relativi), l'organizzazione interna di un file system Unix con **inode** e **blocchi** (riferimenti diretti e indiretti), la **tabella dei descrittori di file** di un processo, il **mount**, le system call sui file (**`open`, `close`, `read`, `write`, `lseek`**) e sulle directory (**`opendir`, `readdir`, `closedir`**), e i **link** simbolici e hard (`link`, `unlink`).
> Mappa dei concetti: [[MOC - Sistemi di Calcolo]] · Approfondimento lato OS: [[12 - SO - File System]]

## Il file system

![[SDC-p170-1.png]]

La mappa del sistema con evidenziato il modulo **File e I/O**: le system call `open`, `read`, `write`, `lseek`, `close`, `mount`, `umount`, `link`, `unlink`; il file system (file, path, inode) e i driver dei dispositivi. A livello hardware: dischi, dispositivi, reti.

> [!warning] Correzione
> Nella dispensa questa figura è didascalizzata "Figura 7.1".

Il **file system** è l'insieme di funzionalità e schemi organizzativi con cui un sistema si interfaccia con i **dispositivi di archiviazione** e ne gestisce i dati. Vedi [[File System]].

## File e directory

Un **file** è una sorgente (o un deposito) di informazioni accessibili in lettura e/o scrittura da un programma: di solito una sequenza di byte memorizzata in modo permanente su disco.

Un file system è organizzato come un **albero**: i nodi interni sono **directory**, le foglie sono directory o file.

- Un **file** ha soprattutto un **nome**, una **dimensione** e dei **permessi** di accesso (chi può leggerlo, scriverlo o eseguirlo, se contiene codice). Vedi [[Permessi e Ownership]].
- Una **directory** contiene altre directory e file, e anch'essa ha un nome e dei permessi.

I nomi hanno spesso un'**estensione** (`.c` per i sorgenti C, `.jpg` per le immagini), che descrive il contenuto ma è solo una convenzione (il comando `file` guarda il contenuto, non l'estensione).

### L'albero delle directory

Nei sistemi UNIX-like (*nix: Linux, macOS) tutti i file accessibili stanno in un **unico albero** complessivo. La **directory radice** `/` contiene tutti i dati del sistema. L'albero è un "collage" di più **file system** diversi, **montati** in punti dell'albero (vedi [[#Mount e umount]]).

L'organizzazione tipica è il **Filesystem Hierarchy Standard** (FHS):

![[SDC-p171-1.png]]

Sotto `/` ci sono `bin` (programmi di base), `dev` (dispositivi), `etc` (configurazione), `home` (le directory degli utenti), `sbin` (programmi di sistema), `usr` (programmi e librerie installati)… Il percorso evidenziato porta a `/home/tom/documents/text`.

Ogni directory, tranne la radice, ha una **directory genitore**; una directory contenuta in un'altra è sua **figlia** (`tom` e `other` sono figlie di `home`). I file system *nix sono **case-sensitive**: `/home/tom/documents/text` è diverso da `/home/tom/documents/Text`.

### Percorsi assoluti e relativi

Un **percorso** (*path*) identifica la posizione di un file o di una directory.

- **Percorso assoluto**: elenca tutte le directory da attraversare **a partire dalla radice** `/`. Es.: `/home/anna/Scrivania/foto-montagna.jpg`.
- **Percorso relativo**: descrive la posizione **rispetto a una directory di riferimento** (di solito la directory corrente). Es.: rispetto a `/home`, il file precedente è `anna/Scrivania/foto-montagna.jpg`.

Due percorsi relativi speciali:

- **`..`**: la **directory genitore**. Rispetto a `/home/anna/Scrivania`, `../Documenti` è `/home/anna/Documenti`;
- **`.`**: la **directory stessa**. `./hello` è il file `hello` nella directory di riferimento (per questo si lancia un programma con `./prog`).

_(dispensa, pp. 170–172)_

## Organizzazione di un file system

### Inode e blocchi

Vedi [[Inode]].

Nei sistemi derivati da UNIX ogni file, directory e dispositivo ha una struttura chiamata **inode**, caricata dal disco e tenuta in memoria in un array. Questa gestione uniforme permette di trattare allo stesso modo file, directory e dispositivi. L'inode contiene i **metadati**; i dati veri stanno in **blocchi** di dimensione fissa allocati su disco.

Un inode contiene:

- **numero dell'inode** (indice nella tabella degli inode);
- **tipo** di file (regolare, directory…);
- **permessi** (lettura, scrittura, esecuzione);
- **numero di hard link** al file;
- **User ID** e **Group ID** del proprietario;
- **dimensione**;
- tempo di **ultimo accesso**, di **ultima modifica del file** e di **ultima modifica dell'inode**;
- **riferimenti diretti** ai blocchi: gli indici dei primi blocchi del file;
- **riferimento indiretto singolo**: l'indice di un blocco che contiene indici di blocchi dati;
- **riferimento indiretto doppio**: l'indice di un blocco che contiene indici di blocchi che contengono indici di blocchi dati.

> [!important] L'inode non contiene il nome del file
> Il nome sta nei blocchi dati delle **directory**, che sono **file speciali** contenenti coppie **(nome, numero di inode)**. È questo che rende possibili gli hard link: più nomi per lo stesso inode.

![[SDC-p173-1.png]]

L'inode, oltre ai metadati, ha n riferimenti diretti (`blocco 0`…`blocco n`) a blocchi dati di **livello 0**; il riferimento `blocchi liv. 1` punta a un blocco di indici che punta a blocchi dati di livello 1; il riferimento `blocchi liv. 2` punta a un blocco di indici che punta ad altri blocchi di indici, che puntano ai blocchi dati di livello 2. I dati si allocano a multipli di blocco, quindi anche il file più piccolo occupa un blocco. I file piccoli usano solo riferimenti diretti, quelli grandi anche gli indiretti.

#### Dimensione massima di un file

Scenario realistico: blocchi da **4096 byte**, indici da **4 byte** (32 bit), quindi ogni blocco di indici contiene 4096 / 4 = **1024** riferimenti. Nell'inode:

- **12** riferimenti diretti;
- **1** indirezione **singola** (1024 blocchi dati);
- **1** indirezione **doppia** (1024 × 1024 blocchi dati).

$$(12 + 1024 + 1024 \cdot 1024) \cdot 4096 = 4\,299\,210\,752 \text{ byte}$$

poco più di **4 GiB** (4 294 967 296 byte). Con un'indirezione **tripla** si superano i 16 TiB.

#### Esempi di occupazione

| File | Blocchi dati | Blocchi di indici | Totale su disco |
| --- | --- | --- | --- |
| 256 byte | 1 | 0 | 1 blocco = 4096 byte |
| 16000 byte | 4 (⌈16000/4096⌉) | 0 | 4 blocchi = 16384 byte |
| 4 MiB = 4194304 byte | 1024 = 12 (liv. 0) + 1012 (liv. 1) | 1 | 1025 blocchi = 4198400 byte |
| 813 MiB = 852492288 byte | 208128 = 12 + 1024 + 207092 (liv. 2) | 1 + 1 + 203 = 205 | 208333 blocchi = 853331968 byte |

Per il file da 813 MiB: 207092 blocchi di livello 2 richiedono ⌈207092/1024⌉ = 203 blocchi di indici di secondo livello, più il blocco di primo livello dell'indirezione doppia e quello dell'indirezione singola.

> [!warning] Correzione
> La dispensa calcola il totale come "208228 + 205 = 208433 blocchi, 853741568 byte". In realtà 208128 + 205 = **208333** blocchi, cioè 208333 · 4096 = **853 331 968** byte.

L'allocazione minima è **un blocco**: con molti file più piccoli di un blocco si spreca spazio (frammentazione interna, vedi [[Frammentazione]]).

#### ls -i e stat

`ls -i` mostra il numero di inode (prima colonna):

```
$ ls /usr -ila
total 324
786433 drwxr-xr-x  11 root root   4096 Dec 20 14:18 .
     2 drwxr-xr-x  17 root root   4096 Dec 20 18:26 ..
932223 drwxr-xr-x   4 root root   4096 Dec 19 21:15 avr
787352 drwxr-xr-x   5 root root  98304 Dec 20 14:17 bin
...
789017 lrwxrwxrwx   1 root root      3 Nov 19 23:24 lib64 -> lib
...
```

`..` (cioè `/`) ha inode 2, quello tipico della radice. `lib64 -> lib` è un link simbolico (tipo `l`).

`stat` mostra i campi principali di un inode:

```
$ stat /bin/ls
  File: /bin/ls
  Size: 137776      Blocks: 272        IO Block: 4096   regular file
Device: 802h/2050d  Inode: 799795      Links: 1
Access: (0755/-rwxr-xr-x)  Uid: (0/root)   Gid: (0/root)
Access: 2019-12-19 20:57:23.000000000 +0100
Modify: 2019-11-12 12:00:56.000000000 +0100
Change: 2019-12-19 20:57:23.510021617 +0100
 Birth: 2019-12-19 20:57:23.510021617 +0100
```

`/bin/ls` è un file **regolare** di 137776 byte, inode 799795, **1 link**, permessi `0755`. `Blocks: 272` conta blocchi da **512 byte**: 272 · 512 = 139264 byte = 34 blocchi da 4096.

> [!warning] Correzione
> La dispensa dice che il file "occupa 272 blocchi di 4096 ciascuno". In `stat` il campo **Blocks** è espresso in unità da **512 byte**, mentre `IO Block: 4096` è la dimensione di blocco del file system.

_(dispensa, pp. 172–175)_

### Tabella dei descrittori di file di un processo

Vedi [[File Descriptor]].

![[SDC-p175-1.png]]

Ogni processo ha la propria **tabella dei descrittori di file**, le cui entry puntano a una **tabella dei file aperti** (condivisa nel sistema), che contiene tra l'altro:

- la **posizione corrente** nel file;
- la **modalità di apertura** (lettura, scrittura…);
- l'**indice dell'inode** del file.

Gli indici della tabella dei descrittori sono i **file descriptor**: le system call li usano per riferirsi a un canale (un file, una directory, un dispositivo…). Le prime tre entry sono aperte automaticamente all'avvio: **stdin (0)**, **stdout (1)**, **stderr (2)**.

Nella figura il processo figlio, creato con `fork`, **condivide** con il genitore un'entry della tabella dei file aperti (quindi anche la posizione corrente), mentre un altro processo ha la propria entry verso un altro file.

I descrittori di un processo con PID x si vedono in `/proc/x/fd`:

```
$ ls -l /proc/21569/fd
lrwx------ 1 studente studente 64 Dec 21 04:50 0 -> /dev/pts/0
lrwx------ 1 studente studente 64 Dec 21 04:50 1 -> /dev/pts/0
lrwx------ 1 studente studente 64 Dec 21 04:50 2 -> /dev/pts/0
l-wx------ 1 studente studente 64 Dec 21 04:50 3 -> /home/studente/Desktop/miofile.txt
```

I descrittori 0, 1 e 2 puntano tutti a `/dev/pts/0`, il **terminale** in cui gira la shell; il 3 è un file regolare aperto in sola scrittura dal processo.

_(dispensa, pp. 175–176)_

## Mount e umount

Vedi [[Mount]].

I file system sono visti come **dispositivi**, rappresentati da file speciali in `/dev`:

```
$ file /dev/sda1
/dev/sda1: block special (8/1)
```

Per usare un file system bisogna **montarlo** sull'albero delle directory. `df` mostra i file system montati e i loro **mount point**:

```
$ df
Filesystem   Size  Used Avail Use% Mounted on
dev          2.0G     0  2.0G   0% /dev
run          2.0G  820K  2.0G   1% /run
/dev/sda2     29G   12G   16G  42% /
tmpfs        2.0G  8.0K  2.0G   1% /dev/shm
...
/dev/sda1    488M   55M  398M  13% /boot
```

`/dev/sda2` è montato sulla radice `/`, `/dev/sda1` su `/boot`.

Per montare: `mount dispositivo mount_point`.

```
$ mkdir /home/studente/Desktop/temp
$ touch /home/studente/Desktop/temp/prova
$ sudo mount /dev/sda2 /home/studente/Desktop/temp
$ ls /home/studente/Desktop/temp
bin  boot  dev  etc  home  lib  lib64  lost+found  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

- Servono privilegi di amministratore (`sudo`).
- Dopo il mount, il mount point si riferisce alla **radice del file system montato**, anch'esso ad albero.
- Su una directory si può montare **un solo file system alla volta**.
- Il mount **non è permanente**: si perde al riavvio o allo spegnimento (per renderlo permanente si usa `/etc/fstab`).
- I file preesistenti nel mount point **diventano invisibili** finché il file system non viene smontato: qui `prova` non si vede più.

Per smontare: `umount mount_point` (anch'esso con `sudo`), che ripristina la situazione precedente:

```
$ sudo umount /home/studente/Desktop/temp
$ ls /home/studente/Desktop/temp
prova
```

_(dispensa, pp. 176–177)_

## Operazioni su file e directory

Nel [[04 - SDC - Librerie standard del C#File e stream|capitolo 4]] si sono viste le funzioni della libc (`fopen`, `fprintf`…). Qui si usano le **system call** su cui la libc si basa: offrono funzionalità più di base (si legge e scrive byte per byte, senza buffer né formattazione), ma permettono anche cose che la libc non offre, come esplorare gli attributi di un file, scorrere una directory o impostare i permessi.

| libc (stream, `FILE*`) | System call (descrittore, `int`) |
| --- | --- |
| `fopen` / `fclose` | `open` / `close` |
| `fwrite` / `fread` | `write` / `read` |
| `fseek` / `ftell` | `lseek` |

### open e close

```c
#include <fcntl.h>
int open(const char *pathname, int flags);
int open(const char *pathname, int flags, mode_t mode);
```

- `pathname`: percorso e nome del file;
- `flags`: modalità di apertura, in OR tra loro (`O_RDONLY`, `O_WRONLY`, `O_RDWR`, `O_CREAT`, `O_TRUNC`, `O_APPEND`…, vedi `man 2 open`);
- `mode` (opzionale): i permessi del file se viene creato (es. `0640`);
- restituisce il **file descriptor**, oppure −1.

```c
#include <fcntl.h>   // open
#include <unistd.h>  // write, close
#include <assert.h>
#include <string.h>  // strlen

int main() {
    // apre in sola scrittura dopo averlo svuotato; lo crea se non esiste
    int fd = open("miofile.txt", O_CREAT | O_WRONLY | O_TRUNC, 0640);
    assert(fd != -1);
    char *str = "hello world";
    write(fd, str, strlen(str));
    close(fd);
    return 0;
}
```

`open` restituisce **sempre il descrittore più piccolo** libero nella tabella del processo (di solito 3, perché 0, 1 e 2 sono già occupati). È su questa regola che si basa la redirezione dell'output (chiudere 1 e poi aprire un file fa sì che il file diventi lo stdout).

`0640` significa `rw-r-----`: lettura e scrittura per il proprietario, sola lettura per il gruppo, nulla per gli altri (vedi [[09 - SDC - Appendici#Permessi POSIX e chmod|Appendice B]]).

```c
#include <unistd.h>
int close(int fd);   // 0, oppure -1 ed errno
```

### write e read

```c
#include <unistd.h>
ssize_t write(int fd, const void *buf, size_t count);
ssize_t read(int fd, void *buf, size_t count);
```

- `write` scrive `count` byte dal buffer `buf` sul canale `fd` e **sposta in avanti la posizione corrente** dei byte scritti; restituisce il numero di byte scritti, o −1.
- `read` legge **fino a** `count` byte dal canale e li scrive in `buf`, spostando in avanti la posizione; restituisce il numero di byte **letti** (0 a fine file), o −1.

> [!warning] Correzione
> Nella descrizione di `read` la dispensa dice "count: numero di byte da scrivere": è il numero **massimo di byte da leggere**.

```c
int main() {
    int fd = open("miofile.txt", O_RDONLY);   // sola lettura
    assert(fd != -1);
    char str[512];
    ssize_t r = read(fd, str, sizeof(str));   // legge al più 512 byte
    close(fd);
    printf("letti %lu byte: ", r);            // letti 11 byte
    fwrite(str, sizeof(char), r, stdout);     // hello world
    printf("\n");
    return 0;
}
```

Si stampa con `fwrite` e non con `printf("%s")`, perché `read` **non aggiunge il terminatore** `'\0'`.

### lseek: accesso casuale

Per accedere in modo non sequenziale (non possibile su tutti i canali: ad esempio non sul terminale) si usa `lseek`, che **sposta la posizione corrente**:

```c
#include <unistd.h>
off_t lseek(int fd, off_t offset, int whence);
```

- `offset`: spiazzamento rispetto al punto di riferimento;
- `whence`: `SEEK_SET` (inizio del file), `SEEK_CUR` (posizione corrente), `SEEK_END` (fine del file);
- restituisce la **nuova posizione** in byte dall'inizio del file, o −1.

Leggere gli ultimi 5 byte di un file:

```c
int fd = open("miofile.txt", O_RDONLY);
char str[512];
off_t pos = lseek(fd, -5, SEEK_END);        // 5 byte prima della fine
ssize_t r = read(fd, str, sizeof(str));     // legge fino alla fine
close(fd);
printf("letti %lu byte dalla posizione %lu: ", r, pos);   // 5 byte dalla posizione 6
fwrite(str, sizeof(char), r, stdout);                     // world
```

`lseek(fd, 0, SEEK_CUR)` restituisce la posizione corrente senza spostarla (l'equivalente di `ftell`).

> [!warning] Correzione
> La dispensa scrive `SEEK_CURR`: la costante è **`SEEK_CUR`**.

### Lavorare con le directory

```c
#include <dirent.h>
DIR *opendir(const char *dirname);         // NULL ed errno in caso di errore
struct dirent *readdir(DIR *dirp);         // prossima entry, NULL a fine directory o in caso di errore
int closedir(DIR *dirp);                   // 0, oppure -1 ed errno
```

- `opendir` apre la directory `dirname` e restituisce un puntatore a una struttura `DIR` che la rappresenta;
- `readdir` restituisce **una entry alla volta**, in una `struct dirent` con:
  - `ino_t d_ino`: numero di inode;
  - `char d_name[]`: nome del file o della directory;
- `closedir` chiude la directory.

> [!warning] Correzione
> La dispensa descrive il parametro `dirname` di `opendir` come "descrittore del canale aperto su cui lavorare": è il **percorso** della directory da aprire.

Esempio: cercare un nome in una directory.

```c
#include <dirent.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    int found = 0;
    DIR *dirp;
    struct dirent* dp;
    if (argc < 3) return (printf("usage: findname dirname name\n"), -1);
    dirp = opendir(argv[1]);
    if (dirp == NULL) return -1;
    while ((dp = readdir(dirp)) != NULL) {
        if (strcmp(dp->d_name, argv[2]) == 0) { found = 1; break; }
    }
    printf("%s\n", found ? "trovato" : "non trovato");
    closedir(dirp);
    return 0;
}
```

Si noti che `readdir` restituisce coppie (nome, inode): è proprio il contenuto di una directory.

_(dispensa, pp. 177–182)_

## Link

Vedi [[Link Hard e Soft]].

Un **link** è un **alias** di un file: lo fa apparire in più directory senza duplicare i dati. Le modifiche fatte attraverso il link sono visibili anche dal file originale. Due tipi: **simbolici** (soft) e **hard**.

### Symbolic link

È un **file che contiene il percorso** del file originale.

- Può stare anche su un **file system diverso**.
- Se l'originale viene spostato, il link diventa **indefinito** (appeso).
- Cancellare il link **non** cancella l'originale.
- Ha un **inode diverso** da quello del file linkato.

`ln -s target link_name` crea un link simbolico:

```
$ touch /home/studente/miofile.txt
$ ls -i /home/studente/miofile.txt
1193992 /home/studente/miofile.txt
$ ln -s /home/studente/miofile.txt /home/studente/Desktop/miofile.txt
$ ls -li /home/studente/Desktop/miofile.txt
1328271 lrwxrwxrwx 1 studente studente 26 Dec 21 03:40 Desktop/miofile.txt -> /home/studente/miofile.txt
```

Inode diversi (1193992 e 1328271), tipo `l`, dimensione 26 byte (la lunghezza del percorso). `ls -l` mostra `link_name -> target`.

### Hard link

È a tutti gli effetti un **altro nome per lo stesso file**, indistinguibile dall'originale.

- Deve stare **nello stesso file system** dell'originale.
- Tutti gli hard link, compreso l'"originale", hanno lo **stesso inode**.
- Il file viene cancellato solo quando **tutti** gli hard link sono stati eliminati.

`ln target link_name` crea un hard link:

```
$ touch /home/studente/miofile.txt
$ ls -i /home/studente/miofile.txt
1193992 /home/studente/miofile.txt
$ ln /home/studente/miofile.txt /home/studente/Desktop/miofile.txt
$ ls -i /home/studente/Desktop/miofile.txt
1193992 /home/studente/Desktop/miofile.txt
```

Stesso inode: sono due nomi dello stesso file. Nell'inode c'è un **contatore degli hard link** (il campo `Links` di `stat`): quando arriva a 0, il file e il suo inode vengono eliminati.

```
$ rm /home/studente/miofile.txt
$ ls -i /home/studente/Desktop/miofile.txt
1193992 /home/studente/Desktop/miofile.txt
```

Il secondo nome resta valido; eliminato anche quello, il file sparisce.

| | Symbolic link | Hard link |
| --- | --- | --- |
| Contenuto | il percorso del target | è lo stesso file |
| Inode | diverso | **uguale** |
| Altri file system | sì | no |
| Se si cancella il target | il link resta appeso | il file sopravvive finché c'è un link |
| Comando | `ln -s` | `ln` |

#### La system call link

```c
#include <unistd.h>
int link(const char *oldpath, const char *newpath);   // 0, oppure -1 ed errno
```

Crea un nuovo nome (hard link) `newpath` per il file esistente `oldpath`. Un `ln` semplificato:

```c
#include <unistd.h>
#include <stdio.h>
int main(int argc, char* argv[]) {
    if (argc < 3) return printf("missing arguments\n"), -1;
    int res = link(argv[1], argv[2]);
    if (res == -1) perror("error in creating link: ");
    return res;
}
```

#### La system call unlink

Il comando `unlink pathname` (una versione semplificata di `rm`) elimina l'hard link `pathname`. Da programma si usa la system call:

```c
#include <unistd.h>
int unlink(const char *pathname);   // 0, oppure -1 ed errno
```

```c
int main(int argc, char* argv[]) {
    if (argc < 2) return printf("pathname mancante\n"), -1;
    int res = unlink(argv[1]);
    if (res == -1) perror("error in deleting name: ");
    return res;
}
```

**Cancellare un file in Unix significa togliergli un nome**: il file sparisce davvero solo quando il contatore dei link arriva a 0 (e nessun processo lo tiene aperto).

_(dispensa, pp. 183–185)_

## Bibliografia della dispensa

- [Chaitin et al. 1981] G. J. Chaitin et al., *Register allocation via coloring*, Computer Languages 6:47–57, 1981 (vedi [[05 - SDC - Ottimizzazione dei programmi#Le ottimizzazioni dei compilatori sono le migliori possibili?|capitolo 5]]).
- [Balch 2003] M. Balch, *Complete Digital Design*, McGraw-Hill, 2003 (vedi [[01 - SDC - Cosa è un sistema di calcolo#Logica sequenziale e flip-flop|capitolo 1]]).
- [Dijkstra 1968] E. W. Dijkstra, *Go To Statement Considered Harmful*, CACM 11(3), 1968 (vedi [[04 - SDC - Librerie standard del C#Errori recuperabili ed errno|capitolo 4]]).

_(dispensa, p. 186)_
