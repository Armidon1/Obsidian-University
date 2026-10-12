---
title: Comunicazione tra Processi
aliases:
  - SDC2 — Inter Process Communication
  - Sistemi di Calcolo 2 — Lezione 5
tags:
  - sistemi-di-calcolo-2
  - ipc
  - shared-memory
  - pipe
  - fifo
source: Appunti Filippo/5-interprocess_communication.pdf
---

# Comunicazione tra processi (IPC)

> [!abstract] Scopo della lezione
> I thread condividono la memoria, i processi no: ognuno vede solo il proprio spazio di indirizzi. Per collaborare servono meccanismi di **Inter-Process Communication**, offerti dal kernel. La lezione presenta la mappa dei meccanismi Linux, i due modelli di base (**memoria condivisa** e **message passing**), la shared memory **POSIX** (`shm_open`, `ftruncate`, `mmap`) con il produttore/consumatore, e poi le **pipe** anonime e le **FIFO** (named pipe), con le regole su atomicità, fine del flusso e `SIGPIPE` e un esempio client/server.
> Mappa dei concetti: [[MOC - Sistemi di Calcolo 2]]

> [!tip] Per gli esercizi
> Le primitive di shared memory, pipe e FIFO sono in [[SDC2 - Primitive C per UNIX System Programming (Sintesi)#5.1 Apertura|Primitive C — §5]] e [[SDC2 - Primitive C per UNIX System Programming (Sintesi)#6.1 Pipe (Anonime)|§6]].

## Processi indipendenti e cooperanti

Ogni processo ha il **proprio spazio di indirizzi** e può accedere solo a quello (grazie alla memoria virtuale, vedi [[Memoria Virtuale]]); il **kernel** invece può accedere a tutto.

I processi di un sistema possono essere:

- **indipendenti**: non possono influenzare l'esecuzione di altri processi né esserne influenzati;
- **cooperanti**: possono influenzare l'esecuzione di altri processi o esserne influenzati.

Motivi per far cooperare i processi:

- **condivisione di informazioni** (es. più processi che accedono allo stesso file o database);
- **velocizzazione del calcolo** (si divide un compito in sotto-compiti eseguiti in parallelo);
- **modularità** (l'applicazione è divisa in moduli, ognuno un processo);
- **comodità** (può essere più semplice lavorare con più processi, es. un utente che modifica, compila e stampa contemporaneamente).

![[SDC2-L05-001-000.png]]

L'applicazione complessiva è progettata come un insieme di **processi cooperanti** collegati tra loro.

L'**Inter-Process Communication (IPC)** è il meccanismo che i processi usano per **comunicare** e **sincronizzare** le loro azioni.

## Mappa dei meccanismi IPC in Linux

Vedi [[Inter-Process Communication]].

![[SDC2-L05-002-002.png]]

- **Comunicazione**:
  - **trasferimento di dati** (scambio di messaggi):
    - a **byte stream** (si invia un flusso di byte su un canale): **pipe** (tra processi parenti, o thread), **FIFO** (tra processi qualsiasi), **stream socket** (tra processi su computer diversi, vedi [[07 - SDC2 - Socket|lezione 7]]), pseudoterminali;
    - a **messaggi**: code di messaggi System V e POSIX, **datagram socket**;
  - **memoria condivisa**: shared memory System V e **POSIX**, **memory mapping** (anonimo o di file).
- **Segnali**: standard e realtime (visti in [[06 - SDC - Esecuzione dei programmi#Segnali|Sistemi di Calcolo]]).
- **Sincronizzazione**:
  - **semafori** System V e **POSIX**, questi ultimi **named** (identificati da una stringa: chiunque conosca il nome può usarli per sincronizzarsi con altri processi) o **unnamed** (quelli usati finora);
  - file lock (`fcntl`, `flock`), mutex e condition variable dei thread (non trattati nel corso).

## Modelli di IPC

I processi cooperanti hanno bisogno di un meccanismo IPC. La maggior parte dei sistemi offre due modelli:

- **memoria condivisa**: i processi usano una zona di memoria condivisa per scambiarsi i dati;
- **message passing**: i processi si mandano messaggi **attraverso il kernel**.

![[SDC2-L05-002-003.png]]

- **Shared memory**: la zona condivisa è mappata nello spazio di entrambi i processi; il processo 2 vi **scrive** e il processo 1 vi **legge** direttamente, senza passare dal kernel.
- **Message passing**: il processo 2 scrive in una **coda di messaggi nella memoria del kernel**, e il processo 1 la legge da lì.

| | Shared memory | Message passing |
| --- | --- | --- |
| Velocità | alta: dopo la creazione, gli accessi sono normali accessi in memoria | più lenta: ogni messaggio richiede **system call** e copie |
| Sincronizzazione | a carico del programmatore (semafori) | in parte implicita (receive bloccante) |
| Distribuibile su più macchine | no | sì |

Con il message passing c'è un vantaggio sulla **concorrenza** (niente dati condivisi da proteggere) ma uno svantaggio di **overhead** (ogni volta si passa per il kernel).

## Memoria condivisa

Vedi [[Shared Memory POSIX]].

Si crea una **regione di memoria condivisa** tra due o più processi con l'aiuto del kernel (system call). Poi i processi leggono e scrivono la regione **direttamente**, come un normale accesso in memoria con un puntatore. In questa fase il kernel **non è coinvolto**, quindi è veloce.

### Produttore/consumatore con shared memory

![[SDC2-L05-003-004.png]]

Il buffer (`item buffer[BUFFER_SIZE]`) e gli indici `in` e `out` stanno nella memoria condivisa, tra il processo produttore e il consumatore (lo schema del buffer circolare della [[02 - SDC2 - Concorrenza#Buffer circolare finito|lezione 2]]).

![[SDC2-L05-003-005.png]]

![[SDC2-L05-003-006.png]]

In entrambi i casi `in == out`: per distinguere un buffer **pieno** da uno **vuoto** si usano i semafori. Buffer pieno: `sem_empty == 0` e `sem_filled == BUFFER_SIZE`. Buffer vuoto: `sem_empty == BUFFER_SIZE` e `sem_filled == 0`.

![[SDC2-L05-003-007.png]]

```c
// Producer
while (true) {
    /* produce un elemento */
    sem_wait(sem_empty);           // semafori named: condivisi tra processi
    sem_wait(sem_cs);
    writeToBuffer(ITEM);
    in = (in + 1) % BUFFER_SIZE;
    sem_signal(sem_cs);
    sem_signal(sem_filled);
}

// Consumer
while (true) {
    sem_wait(sem_filled);
    sem_wait(sem_cs);
    readFromBuffer(ITEM);
    out = (out + 1) % BUFFER_SIZE;
    sem_signal(sem_cs);
    sem_signal(sem_empty);
    /* consuma l'elemento */
}
```

Tra processi diversi servono semafori **named** (o semafori unnamed messi a loro volta nella memoria condivisa, con `pshared = 1`). In POSIX `sem_signal` si chiama `sem_post`.

### API POSIX

| Funzione | Effetto |
| --- | --- |
| `shm_open()` | crea e/o apre un oggetto di memoria condivisa e restituisce un **file descriptor** |
| `ftruncate()` | ne fissa la **dimensione** (all'inizio è 0) |
| `mmap()` | **mappa** l'oggetto nello spazio di indirizzi del processo: da qui lo si legge e scrive con un puntatore (vedi [[mmap]]) |
| `close()` | chiude il descrittore (la mappatura resta valida) |
| `shm_unlink()` | **rimuove** l'oggetto; chi lo ha ancora aperto o mappato può continuare a usarlo |

> [!warning] Correzione
> Gli appunti citano `ltrunc()`: la funzione è **`ftruncate()`** (esiste anche `truncate()`, che lavora su un percorso).

![[SDC2-L05-004-008.png]]

```c
/* programma che SCRIVE nella shared memory */
int main() {
    const int SIZE = 4096;
    const char *name = "MY_PAGE";
    const char *msg = "Hello World!";
    int shm_fd;
    char *ptr;

    shm_fd = shm_open(name, O_CREAT | O_RDWR, 0666);   // apre (crea) la shared memory
    ftruncate(shm_fd, SIZE);                           // la dimensiona
    ptr = (char *) mmap(0, SIZE, PROT_WRITE, MAP_SHARED, shm_fd, 0);   // puntatore
    sprintf(ptr, "%s", msg);                           // scrive nella shared memory
    close(shm_fd);
    return 0;
}
```

![[SDC2-L05-004-009.png]]

```c
/* programma che LEGGE dalla shared memory */
int main() {
    const int SIZE = 4096;
    const char *name = "MY_PAGE";
    int shm_fd;
    char *ptr;

    shm_fd = shm_open(name, O_RDONLY, 0666);           // apertura in lettura
    ptr = (char *) mmap(0, SIZE, PROT_READ, MAP_SHARED, shm_fd, 0);
    printf("%s\n", ptr);                               // Hello World!
    close(shm_fd);
    shm_unlink(name);                                  // rimuove la shared memory
    return 0;
}
```

- `MAP_SHARED`: le scritture sono visibili agli altri processi che mappano lo stesso oggetto (con `MAP_PRIVATE` sarebbero private, copy-on-write).
- Su Linux gli oggetti di shared memory compaiono in `/dev/shm`. Si compila con `-lrt` sui sistemi più vecchi.

> [!warning] Correzione
> Nel codice del lettore c'è `shm_unlink(shm_fd)`: `shm_unlink` vuole il **nome**, quindi `shm_unlink(name)`.

## Message passing

Vedi [[Message Passing]].

In un sistema a messaggi i processi comunicano **senza variabili condivise**. Le primitive sono almeno due:

- `send(destination, message)` oppure `send(message)`;
- `receive(source, message)` oppure `receive(message)`.

I messaggi hanno dimensione **fissa** o **variabile**.

![[SDC2-L05-005-010.png]]

Il processo mittente consegna il messaggio al proprio **modulo di message passing** (nel kernel), che lo inoltra a quello del destinatario, dal quale il processo ricevente lo preleva. Il messaggio porta con sé l'ID del processo e il contenuto.

![[SDC2-L05-005-011.png]]

Lo stesso formato visto nella [[02 - SDC2 - Concorrenza#Formato di un messaggio|lezione 2]]: header (tipo, destinazione, sorgente, lunghezza, informazioni di controllo) e body. Nelle code di messaggi Unix non ci sono gli ID, solo il **tipo** del messaggio. Le informazioni di controllo dicono cosa fare se lo spazio nel buffer finisce, contengono numeri di sequenza, priorità… La disciplina della coda è di solito **FIFO**, ma può includere priorità.

## Pipe

Vedi [[Pipe e FIFO]].

Una **pipe** è un canale di comunicazione in cui mettere dei dati: permette una comunicazione **a senso unico** tra un processo padre e un figlio. È facile da usare e viene **rimossa automaticamente** quando i processi terminano.

Concetti di base:

- i processi comunicano **come se accedessero a file sequenziali**;
- "pipe" significa "tubo": la comunicazione è **monodirezionale**;
- una volta letti, i dati **spariscono** dalla pipe (a meno che qualcuno li riscriva);
- per l'OS una pipe è un **buffer** di dimensione limitata: un processo che scrive su una pipe piena si **blocca**;
- i processi che usano una pipe devono essere **parenti**, cioè legati da `fork()`: il figlio eredita i descrittori;
- le **named pipe** (FIFO) permettono di comunicare anche a processi **non parenti**;
- in Unix si usano tramite **descrittori di file** (vedi [[File Descriptor]]).

La pipe è un'astrazione simile a un file: si legge e si scrive come un file, con permessi controllati dal processo che la crea. Due tipi:

- **named pipe** (FIFO): qualsiasi processo che ne conosca il nome può collegarsi (tipicamente per IPC di lunga durata);
- **unnamed/anonymous pipe**: esiste solo tra un padre e i suoi figli.

La comunicazione può essere **full-duplex** o **half-duplex** (si può leggere e scrivere da una sola o da entrambe le estremità?). Le pipe Unix sono half-duplex: per comunicare nei due sensi servono due pipe.

### pipe() in Unix

![[SDC2-L05-006-012.png]]

```c
int pipe(int fd[2]);   // 0 se va bene, -1 in caso di errore
```

- **`fd[0]`**: descrittore aperto in **lettura** (si legge dalla pipe);
- **`fd[1]`**: descrittore aperto in **scrittura** (si scrive sulla pipe).

Si usano con le normali `read()` e `write()`.

Comportamento:

- leggere da una pipe **vuota** blocca finché non arrivano dati;
- scrivere su una pipe **piena** blocca finché qualcuno non legge abbastanza dati;
- su Linux una pipe ha capacità di **16 pagine** (65 536 byte con pagine da 4096 byte); la si può cambiare (`fcntl` con `F_SETPIPE_SZ`);
- si possono rendere lettura e scrittura non bloccanti (non nel corso).

**Atomicità delle scritture**:

- una scrittura di **n ≤ `PIPE_BUF`** byte (4096 su Linux) è **atomica**: i suoi byte non si mescolano con quelli di altri scrittori (se non c'è spazio per n byte, si blocca finché c'è);
- una scrittura di **n > `PIPE_BUF`** byte può essere **inframezzata** con altre `write`; il processo resta bloccato finché non ha scritto tutti gli n byte.

In modalità non bloccante: con n ≤ `PIPE_BUF` e spazio insufficiente, `write` fallisce con `errno = EAGAIN`; con n > `PIPE_BUF` può fare una scrittura **parziale** (ma non un errore).

**Fine del flusso e SIGPIPE**: le pipe non sono dispositivi fisici, quindi come fa un lettore a vedere la "fine del file"?

- Per convenzione, la fine arriva quando **tutti gli scrittori** che condividevano `fd[1]` lo hanno **chiuso**: da quel momento `read()` restituisce **0**.
- Se un processo scrive su `fd[1]` quando **tutte** le copie di `fd[0]` sono state chiuse (non ci sono più lettori), riceve il segnale **`SIGPIPE`** ("broken pipe"), che di default lo termina; se il segnale è ignorato, `write` fallisce con `EPIPE`.

> [!important] Chiudere i descrittori inutilizzati
> Ogni processo deve **chiudere i descrittori della pipe che non usa**. In particolare un lettore che ha ereditato la coppia (fd[0], fd[1]) deve chiudere la propria copia di **fd[1]** prima di leggere: altrimenti la condizione "tutti gli scrittori hanno chiuso" non si verifica mai (il lettore stesso è ancora uno "scrittore") e la `read` resta bloccata per sempre: **deadlock**.

#### Esempio: trasferire stringhe con una pipe

![[SDC2-L05-007-013.png]]

![[SDC2-L05-008-014.png]]

```c
#include <stdio.h>
#define Errore_(x) { puts(x); exit(1); }

int main(int argc, char *argv[]) {
    char messaggio[30];
    int pid, status, fd[2];

    int ret = pipe(fd);                      // crea la pipe
    if (ret == -1) Errore_("Errore nella creazione pipe");

    pid = fork();                            // crea il figlio, che eredita fd[0] e fd[1]
    if (pid == -1) Errore_("Errore nella fork");

    if (pid == 0) {                          // figlio: lettore
        close(fd[1]);                        // il lettore chiude l'estremità di scrittura
        while (read(fd[0], messaggio, 30) > 0)
            printf("letto messaggio: %s", messaggio);
        close(fd[0]);
        _exit(0);
    } else {                                 // padre: scrittore
        close(fd[0]);                        // lo scrittore chiude l'estremità di lettura
        puts("digitare testo da trasferire (quit per terminare):");
        do {
            fgets(messaggio, 30, stdin);
            write(fd[1], messaggio, 30);
            printf("scritto messaggio: %s", messaggio);
        } while (strcmp(messaggio, "quit\n") != 0);
        close(fd[1]);                        // fine del flusso: la read del figlio restituirà 0
        wait(&status);
    }
}
```

Il padre legge righe da tastiera e le scrive sulla pipe; il figlio le legge e le stampa. Quando il padre chiude `fd[1]`, la `read` del figlio restituisce 0 e il ciclo termina.

> [!warning] Correzione
> Nel codice originale manca la dichiarazione di `ret`, e `_exit()` è chiamata senza argomento: deve essere `_exit(0)`.

## FIFO (named pipe)

![[SDC2-L05-008-015.png]]

```c
int mkfifo(char *name, int mode);   // 0 se va bene, -1 in caso di errore
```

- `name`: il nome (percorso) della FIFO da creare;
- `mode`: i permessi di accesso (es. `0666`).

Una FIFO è un **file speciale** nel file system: per rimuoverla si usa **`unlink()`**.

- Normalmente l'**apertura** di una FIFO è **bloccante**: chi la apre in lettura si blocca finché qualcuno non la apre in scrittura, e viceversa. Per evitarlo si aggiunge il flag `O_NONBLOCK` ai flag di `open()`.
- Ogni FIFO deve avere sia un lettore sia uno scrittore: chi scrive su una FIFO **senza lettori** riceve **`SIGPIPE`**.

### Esempio: client/server con FIFO

![[SDC2-L05-008-016.png]]

1. Il server crea la FIFO pubblica `/serv` e la apre in lettura. 1.1. Legge le richieste che arrivano.
2. Il client crea una propria FIFO privata per la risposta (il cui nome è una lettera scelta dall'utente). 2.1. Scrive su `/serv` una richiesta che contiene il nome della sua FIFO di risposta. 2.2. Apre la propria FIFO e aspetta la risposta.
3. Il server, ricevuta la richiesta, apre la FIFO di risposta del client e scrive il risultato.

**Server**:

![[SDC2-L05-009-018.png]]

![[SDC2-L05-009-020.png]]

```c
typedef struct {
    long type;
    char fifo_response[20];
} request;

int main(int argc, char *argv[]) {
    char *response = "fatto";
    int pid, fd, fdc, ret;
    request r;

    ret = mkfifo("/serv", 0666);                       // 1
    if (ret == -1) { printf("Errore nella chiamata mkfifo\n"); exit(1); }
    fd = open("/serv", O_RDONLY);

    while (1) {
        ret = read(fd, &r, sizeof(request));           // 1.1
        if (ret != 0) {
            printf("Richiesto un servizio (fifo di restituzione = %s)\n", r.fifo_response);
            /* switch sul tipo di servizio */
            sleep(10);                                 // emula il tempo del servizio
            fdc = open(r.fifo_response, O_WRONLY);
            write(fdc, response, 20);                  // 3
            close(fdc);
            exit(0);
        }
    }
}
```

**Client**:

![[SDC2-L05-009-022.png]]

![[SDC2-L05-010-024.png]]

```c
int main(int argc, char *argv[]) {
    int pid, fd, fdc, ret;
    request r;
    char response[20];

    printf("Selezionare un carattere alfabetico minuscolo: ");
    scanf("%s", r.fifo_response);
    if (r.fifo_response[0] > 'z' || r.fifo_response[0] < 'a') {
        printf("carattere selezionato non valido, ricominciare operazione\n");
        exit(1);
    }
    r.fifo_response[1] = '\0';
    ret = mkfifo(r.fifo_response, 0666);               // 2
    if (ret == -1) { printf("\n servente sovraccarico - riprovare \n"); exit(1); }

    fd = open("/serv", O_WRONLY);
    if (fd == -1) {
        printf("\n servizio non disponibile \n");
        ret = unlink(r.fifo_response);
        exit(1);
    }
    write(fd, &r, sizeof(request));                    // 2.1
    close(fd);

    fdc = open(r.fifo_response, O_RDONLY);             // 2.2
    read(fdc, response, 20);
    printf("risposta = %s\n", response);
    close(fdc);
    unlink(r.fifo_response);
}
```

Se `mkfifo` per la FIFO del client fallisce (esiste già, quindi un altro client sta usando la stessa lettera), il client conclude che il server è "sovraccarico". Il client rimuove sempre la propria FIFO con `unlink`.

> [!note] Note sull'esempio
> - Creare `/serv` nella radice richiede i privilegi di root: in pratica si usa un percorso come `/tmp/serv`.
> - Il server, così com'è scritto, termina con `exit(0)` dopo la prima richiesta. Un server vero resterebbe nel ciclo (e userebbe un processo o un thread per richiesta, come nella [[07 - SDC2 - Socket|lezione 7]]).
> - Le scritture su `/serv` sono atomiche perché `sizeof(request)` ≤ `PIPE_BUF`: le richieste di client diversi non si mescolano.

## Pipe e FIFO a confronto

- Aprire una **pipe** dà **entrambi** i descrittori (lettura e scrittura); poi si chiude quello che non serve.
- Una **FIFO** si apre **o** in lettura **o** in scrittura, con `open()` sul suo nome.
- Si differenziano solo nell'**apertura** e nella **chiusura**: lettura e scrittura avvengono allo stesso modo (`read` e `write`).

| | Pipe | FIFO |
| --- | --- | --- |
| Creazione | `pipe(fd)` | `mkfifo(name, mode)` + `open()` |
| Processi | solo parenti (via `fork`) | qualsiasi, conoscendo il nome |
| Esistenza | finché è aperta | file nel file system, finché non si fa `unlink` |
| Direzione | monodirezionale | monodirezionale |
