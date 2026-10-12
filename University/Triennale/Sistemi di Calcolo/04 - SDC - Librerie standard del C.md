---
title: Librerie standard del C
aliases:
  - SDC — Su quali librerie standard può contare un programmatore C
  - Sistemi di Calcolo — Capitolo 4
tags:
  - sistemi-di-calcolo
  - libc
  - posix
  - gestione-errori
  - strace
source: Dispensa Sistemi di Calcolo.pdf (cap. 4, pp. 76–94)
---

# Librerie standard del C

> [!abstract] Scopo del capitolo
> Quasi ogni programma usa funzioni di libreria, almeno per l'input e l'output. Il capitolo presenta la **libc** (parte dello standard **POSIX**): come consultare la documentazione con **`man`**, come gestire gli **errori** (codice di terminazione, `atexit`, `assert`, `errno`, pattern di cleanup), le funzioni principali su **stringhe**, **memoria**, **file e stream** (testo e binari), **ricerca e ordinamento** e **matematica**. Chiude con due strumenti per osservare cosa fa un programma: **`strace`** (system call) e **`ltrace`** (chiamate a librerie dinamiche).
> Mappa dei concetti: [[MOC - Sistemi di Calcolo]]

## Librerie e libc

Una **libreria** è una collezione coerente di funzioni progettate per uno scopo. La **libc** è la libreria standard del C e rientra nello standard **POSIX**.

Ricordando la [[01 - SDC - Cosa è un sistema di calcolo#Panoramica del funzionamento|Figura 1.2]]: un programma C può chiamare sia le funzioni della libreria standard sia altre funzioni POSIX che lo interfacciano con il kernel. Alcune funzioni della libc chiamano a loro volta funzioni POSIX/system call (`printf` deve produrre output sul terminale, quindi usa `write`); altre no (`strlen` calcola soltanto). Vedi [[Architettura a Strati]].

_(dispensa, p. 76)_

## Documentazione: man

Il comando `man` mostra la documentazione delle funzioni di libreria installate, tra cui tutta la libc (`man man` per la guida di `man` stesso). Esempio, `man strlen`:

```
STRLEN(3)                Linux Programmer's Manual               STRLEN(3)
NAME
       strlen - calculate the length of a string
SYNOPSIS
       #include <string.h>
       size_t strlen(const char *s);
DESCRIPTION
       The strlen() function calculates the length of the string pointed to by
       s, excluding the terminating null byte ('\0').
RETURN VALUE
       The strlen() function returns the number of bytes in the string pointed to by s.
```

La documentazione è divisa in **sezioni**:

1. **comandi** (programmi da riga di comando);
2. **chiamate a sistema**;
3. **librerie**.

Se un nome compare in più sezioni bisogna indicare quale: `man 3 printf` (la funzione C; `man printf` mostrerebbe il comando di shell `printf` della sezione 1), `man 2 write` (la system call).

_(dispensa, pp. 76–77)_

## Gestione degli errori

Vedi [[Gestione degli Errori in C]].

### Codice di terminazione

Un processo restituisce sempre un **intero** al processo che l'ha creato: il **codice di terminazione** (*exit status*). Vale **0 se il programma è terminato con successo**, un valore diverso da zero altrimenti. Si emette con `exit`, `_exit` (o `_Exit`), `abort`, oppure con il `return` dal `main`. Il padre lo legge con `wait` (vedi [[06 - SDC - Esecuzione dei programmi#Attesa della terminazione di un figlio: wait|capitolo 6]]); in shell è in `$?`.

### atexit: un gestore per la terminazione

Per evitare che una terminazione prematura lasci operazioni a metà (ad esempio un file troncato), si può installare un **handler** eseguito automaticamente prima di terminare:

```c
#include <stdlib.h>
int atexit(void (*function)(void));
```

- `function`: puntatore alla funzione da eseguire alla terminazione con `exit` o con `return` dal `main` (vedi [[Puntatori a Funzione]]);
- restituisce 0 in caso di successo, un valore diverso da zero in caso di errore.

```c
#include <stdio.h>
#include <stdlib.h>
void handler() { printf("uscita dal programma\n"); }
int main() {
    atexit(handler);
    return 0;          // stampa: "uscita dal programma"
}
```

Si possono installare più handler: vengono eseguiti in **ordine inverso** rispetto all'installazione. Non vengono eseguiti con `_exit` o `abort`, che terminano subito.

### Errori non recuperabili: assert

Sono errori che indicano un **bug** e devono far terminare il programma. Si segnalano con la macro `assert`:

```c
#include <assert.h>
assert(test);
```

Se `test` vale zero, il programma termina con un codice diverso da zero e stampa su `stderr` un messaggio come `Assertion failed: (<test>), function main, file <nomefile.c>, line <n>`. Compilando con `-DNDEBUG` le `assert` vengono eliminate.

### Errori recuperabili ed errno

Un errore è **recuperabile** se il programma può continuare, eventualmente dopo una pulizia (*cleanup*). Ad esempio, una funzione che carica un file in memoria non dovrebbe far terminare il programma se il file non esiste. Quando possibile, gli errori dovrebbero essere tutti recuperabili.

Due convenzioni per segnalare un errore al chiamante:

1. **libreria standard C**: restituisce `NULL` se la funzione restituisce un puntatore e, di solito, un valore diverso da 0 se restituisce un intero (con eccezioni: `strtol` restituisce 0);
2. **funzioni POSIX** (esclusa la libc): restituiscono **0 in caso di successo** e un valore diverso da 0, tipicamente **−1**, in caso di errore.

In entrambi i casi viene impostata la variabile globale **`errno`** (in `<errno.h>`) con un codice che specifica il problema. `perror` (in `<stdio.h>`) stampa un messaggio leggibile relativo all'errore della chiamata immediatamente precedente.

Pattern di gestione con cleanup:

```c
int mia_funzione() {
    int res, *buffer = NULL;
    ...
    buffer = malloc(...);
    if (buffer == NULL) goto cleanup;   // errore
    ...
    res = chiamata(...);
    if (res != 0) goto cleanup;         // errore
    ...
    free(buffer);
    return 0;
cleanup:
    ...
    if (buffer != NULL) free(buffer);   // libera ciò che è stato allocato
    return -1;
}
```

Il `goto` andrebbe normalmente evitato perché rende il codice meno leggibile (Dijkstra, 1968), ma qui è il modo più pulito per avere **un solo punto di uscita** che libera tutte le risorse. È la stessa tecnica usata nel kernel Linux e in [[08 - SO - disastrOS#Invocazione di una syscall|disastrOS]].

_(dispensa, pp. 77–79)_

## Stringhe

Vedi [[Funzioni della libc]].

Una stringa C è un array di `char` terminato da `'\0'`.

| Funzione | Header | Cosa fa | Restituisce |
| --- | --- | --- | --- |
| `size_t strlen(const char *s)` | `string.h` | lunghezza, **escluso** il terminatore | numero di caratteri |
| `char *strcpy(char *dest, const char *src)` | `string.h` | copia `src` in `dest` (terminatore incluso) | `dest` |
| `char *strcat(char *dest, const char *src)` | `string.h` | concatena `src` in fondo a `dest` | `dest` |
| `int strcmp(const char *s1, const char *s2)` | `string.h` | confronto lessicografico | < 0, 0, > 0 |
| `int sprintf(char *str, const char *fmt, ...)` | `stdio.h` | come `printf`, ma scrive nella stringa `str` | caratteri scritti (escluso `'\0'`), < 0 se errore |
| `int sscanf(char *str, const char *fmt, ...)` | `stdio.h` | come `scanf`, ma legge dalla stringa | argomenti letti (`EOF` se l'input finisce prima) |
| `char *strtok(char *str, const char *delim)` | `string.h` | divide in token | prossimo token o `NULL` |
| `int atoi(const char *nptr)` | `stdlib.h` | converte in `int` il prefisso numerico | il numero (0 se non c'è) |

```c
char dest[6];                 // 5 caratteri + 1 per il terminatore
strcpy(dest, "hello");        // hello

char d2[12] = "hello";        // 5 + 6 + 1
strcat(d2, " world");         // hello world

strcmp("abacus", "root");     // < 0
strcmp("root", "root");       // 0
strcmp("root", "abacus");     // > 0

char buffer[9];
sprintf(buffer, "(%d,%.1f)", 10, 3.14);   // "(10,3.1)": 8 caratteri + '\0'

int i; float d;
int res = sscanf("a 13 2.7", "a %d %f", &i, &d);   // res=2, i=13, d=2.7

char str[] = "hello, world!";
char *t = strtok(str, "! ,");
while (t != NULL) { printf("%s\n", t); t = strtok(NULL, "! ,"); }  // hello / world

atoi("971esempio");   // 971
atoi("esempio");      // 0
```

> [!warning] Buffer overflow
> `strcpy`, `strcat` e `sprintf` **non controllano lo spazio** nella destinazione: se è troppo piccola scrivono oltre la fine del buffer (*buffer overflow*, la classica vulnerabilità sfruttata negli exploit). Meglio usare le varianti con limite: `strncpy`, `strncat`, `snprintf`.

> [!note] strtok
> - Alla prima chiamata si passa la stringa, alle successive `NULL` (`strtok` ricorda la posizione in una variabile statica, quindi non è rientrante; esiste `strtok_r`).
> - **Modifica il buffer** di input, sostituendo i separatori con `'\0'`: non si può usare su una stringa letterale (`char *s = "..."`), che sta in memoria di sola lettura.

`atol` e `atoll` convertono in `long` e `long long`; `strtol` gestisce anche gli errori (vedi `man`). In alternativa ad `atoi` si può usare `sscanf`.

_(dispensa, pp. 79–83)_

## Memoria

| Funzione | Cosa fa |
| --- | --- |
| `void *memcpy(void *dest, const void *src, size_t n)` | copia **n byte** da `src` a `dest` (le aree non devono sovrapporsi; altrimenti `memmove`) |
| `int memcmp(const void *s1, const void *s2, size_t n)` | confronta i primi n byte: > 0 se nella prima coppia diversa il byte di s1 è maggiore, < 0 se è minore, 0 se uguali |
| `void *memset(void *s, int c, size_t n)` | imposta n byte al valore `c` (ne usa gli 8 bit bassi) |

```c
char dest[6];
memcpy(dest, "hello", 6);            // copia anche il terminatore

memcmp("hell", "hello", 4);          // 0 (confronta solo 4 byte)
memcmp("ant", "Ant", 3);             // > 0 ('a' = 97 > 'A' = 65)
memcmp("Ant", "ant", 3);             // < 0

char buf[6];
memset(buf, '*', 5); buf[5] = '\0';  // "*****"
```

A differenza delle funzioni `str*`, le `mem*` lavorano su **byte grezzi** di lunghezza esplicita e non si fermano a `'\0'`.

_(dispensa, pp. 83–84)_

## File e stream

Uno **stream** è un generico canale di I/O.

### Canali standard: stdin, stdout, stderr

Quando un processo parte in un sistema Unix-like vengono creati tre canali (*standard stream*):

- **stdin**: di default collegato alla **tastiera**; lo usano ad esempio `getchar`, `getc`, `scanf`;
- **stdout**: di default collegato al **terminale** che ha lanciato il processo; lo usa `printf`;
- **stderr**: anch'esso collegato al terminale; si usa per messaggi di **errore** e diagnostica (`fprintf(stderr, ...)`).

stdout e stderr vanno di default nella stessa destinazione, quindi le loro uscite possono alternarsi o mescolarsi sul terminale. Si possono **redirigere** separatamente (vedi [[09 - SDC - Appendici#Redirezione di stdin, stdout e stderr|Appendice B]]). Corrispondono ai file descriptor 0, 1 e 2 ([[File Descriptor]]).

### fopen e fclose

```c
#include <stdio.h>
FILE *fopen(const char *pathname, const char *mode);   // NULL in caso di errore
int fclose(FILE *stream);                              // 0, oppure EOF ed errno
```

`mode` è la modalità di apertura: `"r"` lettura, `"w"` scrittura (crea o tronca il file), `"a"` aggiunta in fondo, `"r+"`/`"w+"` lettura e scrittura (vedi `man 3 fopen`).

```c
#include <stdio.h>
#include <assert.h>
int main() {
    FILE* f = fopen("miofile.txt", "w");
    assert(f != NULL);
    fprintf(f, "hello world");
    fclose(f);
    return 0;
}
```

> [!warning] Correzione
> Nella dispensa il parametro di `fclose` è descritto come "percorso e nome del file da chiudere": in realtà `stream` è il **puntatore `FILE*`** restituito da `fopen`.

### File di testo: printf, fprintf, scanf, fscanf, fgets

```c
int printf(const char *format, ...);                 // = fprintf(stdout, ...)
int fprintf(FILE *stream, const char *format, ...);
int scanf(const char *format, ...);                  // = fscanf(stdin, ...)
int fscanf(FILE *stream, const char *format, ...);
char *fgets(char *str, int size, FILE *stream);
```

- `printf`/`fprintf` restituiscono il numero di caratteri scritti (negativo se errore).
- `scanf`/`fscanf` restituiscono il **numero di argomenti letti** (negativo o `EOF` se errore o fine dell'input): è il modo per capire se la lettura è andata a buon fine.

Esempio di `printf` con argomenti posizionali: `printf("%1$s %1$s %s %s\n", "hello", "world");` stampa `hello hello hello world`.

> [!note]
> La sintassi `%1$s` (argomenti posizionali) è un'estensione POSIX, e mischiare argomenti posizionali e non posizionali nella stessa stringa di formato è formalmente non definito. È meglio non farlo nel codice reale.

Esempio di `fscanf` che riconosce righe di formati diversi:

```c
FILE* f = fopen("prova.txt", "r");
for (;;) {
    int x = 0, y = 0, res;
    res = fscanf(f, "a %d %d\n", &x, &y);
    if (res < 2) res = fscanf(f, "b %d %d\n", &x, &y);
    if (res < 2) res = fscanf(f, "c %d %d\n", &x, &y);
    printf("%d: %d %d\n", res, x, y);
    if (res == 0 || res == EOF) break;
}
fclose(f);
```

Con `prova.txt` = `c 1 2`, `a 3 4`, `b 6 0`, `a 7 8`, `d 9 10`, `a 1 3`, l'output è `2: 1 2`, `2: 3 4`, `2: 6 0`, `2: 7 8`, `0: 0 0`. Il programma si ferma su `d 9 10` perché il caso `d` non è gestito: nessun formato combacia e `res` vale 0.

`fgets` legge **una riga intera**, ritorno a capo compreso, e aggiunge `'\0'`:

```c
#define N 127
char *line = malloc((N+1) * sizeof(char));
char *res = fgets(line, N, stdin);
assert(res != NULL);
printf("%s", res);     // il '\n' è già in res
free(line);
```

> [!warning] Correzione
> La dispensa dice che il buffer deve essere grande almeno `size+1`. In realtà `fgets` legge **al più `size−1`** caratteri e aggiunge il terminatore, quindi basta un buffer di `size` byte. L'esempio (buffer di N+1 byte, `size = N`) è comunque corretto, con un byte in più.

### File binari: fwrite e fread

```c
size_t fwrite(const void *ptr, size_t size, size_t nitems, FILE *stream);
size_t fread(void *ptr, size_t size, size_t nitems, FILE *stream);
```

Scrivono/leggono `nitems` elementi di `size` byte ciascuno, a partire da `ptr`, e restituiscono il **numero di elementi** effettivamente scritti/letti. Entrambe fanno avanzare la posizione corrente nel file.

> [!warning] Correzione
> La dispensa dice che `fwrite` scrive "verso un flusso di input": è un flusso di **output**.

```c
// scrittura
int buffer[5] = { 7, 12, 5, 8, 23 };
FILE *f = fopen("numeri.dat", "w");
int numelem = fwrite(buffer, sizeof(int), 5, f);   // 5
fclose(f);

// lettura
int *buf = malloc(1024 * sizeof(int));
f = fopen("numeri.dat", "r");
int n = fread(buf, sizeof(int), 1024, f);          // 5: il file contiene solo 5 interi
fclose(f);
```

Il file `numeri.dat` contiene i **byte** degli interi (20 byte, in little-endian), non il loro testo: aprendolo con un editor si vedono caratteri incomprensibili. Vedi [[Endianness]].

_(dispensa, pp. 84–90)_

## Ricerca e ordinamento: bsearch e qsort

```c
#include <stdlib.h>
void *bsearch(const void *key, const void *base, size_t nel, size_t width,
              int (*compar)(const void *, const void *));
void qsort(void *base, size_t nel, size_t width,
           int (*compar)(const void *, const void *));
```

Sono **generiche**: lavorano su array di qualsiasi tipo perché ricevono la dimensione di un elemento (`width`) e un **comparatore**, cioè un [[Puntatori a Funzione|puntatore a funzione]] che restituisce < 0, 0 o > 0. È lo stesso schema delle liste generiche viste in [[03 - SO - Programmazione OOP in C|Sistemi Operativi]].

- `bsearch` fa una **ricerca binaria** in un array **già ordinato** e restituisce il puntatore all'elemento trovato, o `NULL`. Con più occorrenze ne restituisce una qualsiasi.
- `qsort` **ordina** l'array sul posto.

```c
int comparator(const void *x, const void *y) {
    int xt = *(int*)x, yt = *(int*)y;
    return xt - yt;
}

int v[] = { 2, 4, 5, 7, 9 }, key = 7;
int *res = bsearch(&key, v, 5, sizeof(int), comparator);   // *res == 7

int w[] = { 7, 4, 5, 3, 2 };
qsort(w, 5, sizeof(int), comparator);                      // 2 3 4 5 7
```

> [!tip] Overflow nel comparatore
> `return xt - yt;` può andare in overflow con valori molto grandi di segno opposto. Una versione sicura è `return (xt > yt) - (xt < yt);`.

_(dispensa, pp. 90–91)_

## Funzioni matematiche

Bisogna aggiungere `-lm` alla riga di comando per collegare la **libreria matematica** (`man math.h` per l'elenco). Esempio:

```c
#include <math.h>
double sqrt(double x);   // NaN ed errno = EDOM se x < 0
printf("%f\n", sqrt(2)); // 1.414214
```

_(dispensa, p. 92)_

## Tracciare le system call: strace

Vedi [[strace e ltrace]].

`strace programma` mostra le **system call** effettuate da un programma. Con il solito `hello.c` compilato con `-O1`:

```
$ strace ./hello > /dev/null
...
arch_prctl(ARCH_SET_FS, 0x7fdf1094f540) = 0
mprotect(0x7fdf10944000, 12288, PROT_READ) = 0
...
munmap(0x7fdf10950000, 178959)          = 0
fstat(1, {st_mode=S_IFCHR|0620, ...})   = 0
brk(NULL)                               = 0x55bab6e53000
brk(0x55bab6e74000)                     = 0x55bab6e74000
write(1, "hello world\n", 12)           = 12
exit_group(0)                           = ?
+++ exited with 0 +++
```

- `strace` scrive il proprio output su **stderr**, il programma su **stdout**: redirigendo stdout su `/dev/null` (un "pozzo" che scarta tutto ciò che riceve) si vede solo l'output di `strace`.
- Le prime chiamate (non tutte riportate) preparano l'ambiente di esecuzione **prima del `main`** (caricamento delle librerie con `mmap`/`mprotect`, ecc.).
- `fstat(1, …)` controlla che tipo di file è stdout; `brk` allarga lo heap per il buffer di `printf`.
- La `printf` finisce per invocare la system call **`write` sul descrittore 1** (stdout): un esempio di funzione libc che usa una system call.
- Il `return 0` porta alla system call `exit_group(0)`.

Lo stesso strumento era citato in [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Esempio: printf|Sistemi Operativi]].

_(dispensa, pp. 92–93)_

## Tracciare le chiamate di libreria: ltrace

`ltrace` intercetta le chiamate alle **librerie dinamiche**:

```c
#include <math.h>
#include <stdio.h>
double f(double x) { return sqrt(x); }
int main() { double y = f(2.0); printf("%f\n", y); return 0; }
```

```
$ gcc mytest.c -o mytest -lm
$ ltrace ./mytest > /dev/null
sqrt(1, 0x7ffca1dee0e8, 0x7ffca1dee0f8, 0x7fa8fd1d6578) = 0x4000000000000000
printf("%f\n", 1.414214)                                = 9
+++ exited (status 0) +++
```

`ltrace` vede le chiamate a `sqrt` e `printf`. Gli argomenti di `sqrt` appaiono strani perché `ltrace` non conosce il prototipo e interpreta come interi dei registri che in realtà contengono `double`. Non vede la chiamata a `f`, che è una funzione del programma e non di una libreria.

| | strace | ltrace |
| --- | --- | --- |
| Intercetta | system call (confine user/kernel) | chiamate a librerie dinamiche (`.so`) |
| Esempio | `write`, `brk`, `exit_group` | `printf`, `sqrt`, `malloc` |

_(dispensa, pp. 93–94)_
