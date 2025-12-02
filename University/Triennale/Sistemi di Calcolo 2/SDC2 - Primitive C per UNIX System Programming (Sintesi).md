Vedi l'originale più chiaro [[SDC2 - Primitive C per UNIX System Programming.pdf|qui]]
# Primitive C per UNIX System Programming

**Autori:** Leonardo Aniello, Daniele Cono D'Elia, Riccardo Lazzeretti
**Dipartimento:** Ingegneria Informatica, Automatica e Gestionale "A. Ruberti", Sapienza Università di Roma
**Ultimo aggiornamento:** 09 dicembre 2019

-----

## 1\. Operazioni su file e descrittori

Per operare su file e descrittori, è opportuno includere `<fcntl.h>` ed `<unistd.h>`.

### 1.1 Apertura di un file

```c
int open(const char* pathname, int flags, mode_t mode);
```

La funzione restituisce un descrittore per il file specificato in `pathname`.

* **flags**: Deve obbligatoriamente contenere una delle seguenti modalità di accesso:
* `O_RDONLY` (sola lettura)
* `O_WRONLY` (sola scrittura)
* `O_RDWR` (lettura e scrittura)
* Si possono specificare ulteriori flag (e.g., `O_APPEND`, `O_TRUNC`) concatenandoli tramite OR bit a bit.
* `O_CREAT`: il file viene creato se non è già presente nel sistema.
* `O_CREAT | O_EXCL`: restituisce errore se il file da creare esiste già.
* **mode**: Necessario solo se si specifica `O_CREAT`. Indica i permessi di creazione (es. codifica ottale `0660` o macro di `<sys/stat.h>`).
* **Return**: Descrittore (intero \>= 0) in caso di successo. -1 in caso di errore (errno impostata).

### 1.2 Lettura da un descrittore

```c
ssize_t read(int fd, void *buf, size_t count);
```

Tenta di leggere `count` bytes dal descrittore `fd` e memorizzarli in `buf`.

* **Return**: Numero di byte letti, o 0 se raggiunta la fine del file (EOF).
* Nota: Il numero di byte letti può essere minore di quello richiesto (es. EOF, buffer disponibile limitato, interruzione da segnale).
* In caso di errore: -1 (errno impostata).

### 1.3 Scrittura su un descrittore

```c
ssize_t write(int fd, void *buf, size_t count);
```

Tenta di scrivere `count` bytes su `fd` leggendoli da `buf`.

* **Return**: Numero di byte effettivamente scritti.
* Nota: Può essere inferiore al richiesto (es. spazio insufficiente, interruzione da segnale).
* In caso di errore: -1 (errno impostata).

### 1.4 Chiusura di un descrittore

```c
int close(int fd);
```

Chiude un descrittore di file (o socket/pipe) rendendolo riutilizzabile.

* **Return**: 0 in caso di successo. -1 in caso di errore.

### 1.5 Rimozione di un file

```c
int unlink(const char* pathname);
```

Rimuove il nome `pathname` dal filesystem. Se è l'ultimo hardlink, il file viene rimosso.

* Se ci sono descrittori aperti, la rimozione è posticipata alla chiusura dell'ultimo descrittore.
* **Return**: 0 in caso di successo. -1 in caso di errore.

-----

## 2\. Esecuzione concorrente

### 2.1 Creazione di un processo figlio

```c
pid_t fork(void);
```

Crea un nuovo processo duplicando il chiamante. Richiede `<unistd.h>`.

* Padre e figlio hanno spazi di memoria separati.
* **Return**: 0 nel processo figlio; PID del figlio nel processo padre.
* In caso di fallimento: -1.

### 2.2 Attesa terminazione di un processo figlio

```c
pid_t wait(int *status);
```

Il padre attende la terminazione dei figli. Richiede `<sys/wait.h>`.

* **status**: Se diverso da NULL, contiene info sullo stato del figlio terminato.
* **Return**: PID del figlio terminato. -1 in caso di errore.

### 2.3 Creazione di un thread

Includere `<pthread.h>` e linkare con `-lpthread`.

> [\!WARNING] Nota
> Le funzioni thread non usano `errno`, ma restituiscono il codice di errore direttamente.

```c
int pthread_create(pthread_t *thread, const pthread_attr_t *attr, void *(*start_routine)(void*), void *arg);
```

* **attr**: Attributi del thread (usare `NULL` per default).
* **start\_routine**: Funzione eseguita dal thread. Prende `arg` come argomento.
* **Return**: 0 successo. Codice errore in caso di fallimento.

### 2.4 Uscita da un thread

```c
void pthread_exit(void *value_ptr);
```

Termina il thread e rende `value_ptr` disponibile al `pthread_join`.

* Nel main thread: permette al processo di proseguire finché tutti gli altri thread terminano.
* **Nota**: Non restituire indirizzi di variabili locali.

### 2.5 Sincronizzazione tra thread

#### Join

```c
int pthread_join(pthread_t thread, void **value_ptr);
```

Sospende il chiamante fino alla terminazione di `thread`.

* **value\_ptr**: Se non NULL, riceve il valore passato a `pthread_exit`.
* **Return**: 0 successo, codice errore altrimenti.

#### Detach

```c
int pthread_detach(pthread_t thread);
```

Indica che le risorse del thread possono essere reclamate alla sua terminazione (senza join).

-----

## 3\. Semafori

Header: `<semaphore.h>`. Linkare libreria `pthread`.

### 3.1 Semafori anonimi

**Inizializzazione**

```c
int sem_init(sem_t *sem, int pshared, unsigned int value);
```

* `pshared`: 0 per thread dello stesso processo, 1 per processi condivisi.
* `value`: valore iniziale.
* Return: 0 successo, -1 errore.

**Distruzione**

```c
int sem_destroy(sem_t *sem);
```

Distrugge un semaforo anonimo.

### 3.2 Operazioni

**Wait (Decremento)**

```c
int sem_wait(sem_t *sem);
```

Decrementa il semaforo. Se valore negativo, si blocca finché non viene incrementato.

**Post (Incremento)**

```c
int sem_post(sem_t *sem);
```

Incrementa il semaforo. Sblocca eventuali thread in attesa.

**Get Value**

```c
int sem_getvalue(sem_t *sem, int *sval);
```

Legge il valore corrente in `sval`. Su Linux, se ci sono thread in attesa, scrive 0.

### 3.3 Semafori Named

Usare `<fcntl.h>` e `<sys/stat.h>`.

**Apertura/Creazione**

```c
sem_t *sem_open(const char *name, int oflag, mode_t mode, unsigned int value);
```

* **name**: Stringa tipo `/NomeSemaforo`.
* **oflag**: `O_CREAT`, `O_EXCL`.
* **mode/value**: Richiesti solo con `O_CREAT`.
* **Return**: Indirizzo semaforo o `SEM_FAILED` in caso di errore.

### 3.4 Chiusura e Distruzione Named

* `sem_close(sem_t *sem)`: Chiude il descrittore nel processo.
* `sem_unlink(const char *name)`: Rimuove il semaforo dal sistema (distrutto quando tutti chiudono).

-----

## 4\. Socket

### 4.1 Strutture Dati

Indirizzo endpoint: `struct sockaddr_in`:

* `sin_family`: `AF_INET`
* `sin_addr.s_addr`: IP (`INADDR_ANY` per tutte le interfacce).
* `sin_port`: Numero porta.
* `sin_zero`: Padding (inizializzare a 0).

### 4.2 Creazione Socket

Header: `<sys/socket.h>`.

```c
int socket(int domain, int type, int protocol);
```

* `domain`: `AF_INET` (IPv4).
* `type`: `SOCK_STREAM` (TCP) o `SOCK_DGRAM` (UDP).
* `protocol`: 0.
* Return: Descrittore o -1.

### 4.3 Connessione (Client)

```c
int connect(int socket, const struct sockaddr *address, socklen_t address_len);
```

Tenta connessione verso `address`. Fare cast a `struct sockaddr*`.

### 4.4 Accettare Connessioni (Server)

Sequenza: `bind` -\> `listen` -\> `accept`.

1. **Bind**: `int bind(int socket, const struct sockaddr *address, socklen_t address_len);`
Collega il descrittore a un indirizzo/porta.
2. **Listen**: `int listen(int sockfd, int backlog);`
Abilita socket a ricevere connessioni. `backlog` è la coda richieste pendenti.
3. **Accept**: `int accept(int socket, struct sockaddr *address, socklen_t *address_len);`
Attende e accetta una connessione. Restituisce un *nuovo* descrittore per la connessione specifica.

### 4.5 I/O su Socket

**TCP (o connessi)**

* `send(int sockfd, const void *buf, size_t len, int flags)`: Equivalente a `write` se flags=0.
* `recv(int sockfd, void *buf, size_t len, int flags)`: Equivalente a `read` se flags=0. Ritorna 0 se connessione chiusa dalla controparte.

**UDP (o non connessi)**

* `sendto(...)`: Specifica destinatario `dest_addr`.
* `recvfrom(...)`: Restituisce mittente in `src_addr`.

### 4.6 Utility Indirizzi

Header: `<arpa/inet.h>`.

* `htons(uint16_t hostshort)`: Host to Network Short (per porte).
* `ntohs(uint16_t netshort)`: Network to Host Short.
* `inet_addr(const char *cp)`: Converte stringa "x.y.z.w" in `in_addr_t` (network byte order).
* `inet_ntop(...)`: Converte indirizzo rete in stringa.

-----

## 5\. Shared Memory

Header: `<sys/mman.h>`, `<sys/stat.h>`, `<fcntl.h>`. Linkare `-lrt`.

### 5.1 Apertura

```c
int shm_open(const char* pathname, int flags, mode_t mode);
```

Simile a `open`. Restituisce descrittore.

**Dimensionamento**

```c
int ftruncate(int fd, off_t length);
```

Imposta dimensione memoria condivisa a `length` bytes.

**Mapping**

```c
void *mmap(void *addr, size_t length, int prot, int flags, int fd, off_t offset);
```

Mappa la shared memory nel processo.

* `addr`: 0 (kernel decide).
* `prot`: `PROT_READ`, `PROT_WRITE`, etc..
* `flags`: `MAP_SHARED` (visibile ad altri processi).
* Return: Puntatore memoria o `MAP_FAILED`.

### 5.2 Chiusura

1. `munmap(void *addr, size_t length)`: Cancella mapping.
2. `close(fd)`: Chiude descrittore.
3. `shm_unlink(const char* pathname)`: Rimuove la memoria dal sistema (distruzione reale dopo unmap di tutti).

-----

## 6\. Pipe e FIFO

### 6.1 Pipe (Anonime)

```c
int pipe(int pipefd[2]);
```

Canale unidirezionale tra processi (tipicamente padre-figlio).

* `pipefd[0]`: Lettura.
* `pipefd[1]`: Scrittura.

### 6.2 Duplicazione Descrittori

* `dup(int oldfd)`: Crea copia usando primo descrittore libero.
* `dup2(int oldfd, int newfd)`: Copia `oldfd` in `newfd` (chiudendo `newfd` se aperto).

### 6.3 FIFO (Named Pipe)

```c
int mkfifo(const char *pathname, mode_t mode);
```

Crea una FIFO nel filesystem. Va poi aperta con `open`.

* Rimozione con `unlink`.

-----

## A. Complementi C

### A.1 Gestione Memoria (`<stdlib.h>`, `<string.h>`)

* `malloc(size_t size)`: Alloca memoria.
* `calloc(size_t nmemb, size_t size)`: Alloca array e inizializza a zero.
* `realloc(void *ptr, size_t size)`: Cambia dimensione allocazione.
* `free(void *ptr)`: Rilascia memoria.
* `memset(void *s, int c, size_t n)`: Riempie memoria con byte costante.
* `memcpy(void *dest, const void *src, size_t n)`: Copia memoria.

### A.2 Gestione Stringhe

* `strlen`: Lunghezza stringa.
* `sprintf`: Stampa formattata su buffer stringa.
* `strtok(char *str, const char *delim)`: Tokenizer stringhe (non thread-safe\!).
* Prima chiamata: passare `str`. Chiamate successive: passare `NULL`.

### A.3 Macro gestione errori

Esempio di macro per gestire errori e `errno`:

```c
#define GENERIC_ERROR_HELPER(cond, errCode, msg) do { \
if (cond) { \
fprintf(stderr, "%s: %s\n", msg, strerror(errCode)); \
exit(EXIT_FAILURE); \
} \
} while (0)

#define ERROR_HELPER(ret, msg) GENERIC_ERROR_HELPER((ret < 0), errno, msg)
#define PTHREAD_ERROR_HELPER(ret, msg) GENERIC_ERROR_HELPER((ret != 0), ret, msg)
```

### A.4 Debugging con GDB

Compilare con `-g -O0`.

1. Avvio: `gdb ./eseguibile`.
2. Esecuzione: `run arg1 arg2`.
3. Dopo crash (segfault), ispezionare stack: `bt` (backtrace).
* Cercare il frame associato al proprio codice per individuare la linea dell'errore.