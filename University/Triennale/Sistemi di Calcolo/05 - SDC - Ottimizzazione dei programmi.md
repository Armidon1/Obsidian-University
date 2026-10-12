---
title: Ottimizzazione dei programmi
aliases:
  - SDC — Come vengono ottimizzati i programmi
  - Sistemi di Calcolo — Capitolo 5
tags:
  - sistemi-di-calcolo
  - ottimizzazione
  - prestazioni
  - profiling
  - gcc
source: Dispensa Sistemi di Calcolo.pdf (cap. 5, pp. 95–118)
---

# Ottimizzazione dei programmi

> [!abstract] Scopo del capitolo
> Ottimizzare significa far usare meno risorse a un programma **senza cambiarne il significato**. Il capitolo spiega perché le prestazioni contano (la "moneta" con cui si comprano le altre qualità del software, e la fine della crescita gratuita del clock), **cosa** ottimizzare (metriche, scala dei tempi, **speedup** e **legge di Amdahl**, **profiling** con `clock_gettime`, `getrusage` e `gprof`) e **come**: i livelli `-O` di `gcc` e le singole tecniche, distinguendo quelle che **fa già il compilatore** da quelle che deve fare **il programmatore**.
> Mappa dei concetti: [[MOC - Sistemi di Calcolo]]

## Cosa significa ottimizzare

Idealmente un programma dovrebbe usare il minimo di risorse: tenere occupata la CPU il meno possibile e usare poca memoria (la dispensa non tratta altre risorse come l'energia).

Ottimizzare un programma dal punto di vista **prestazionale** significa modificarlo in modo che:

1. resti **corretto**: un'ottimizzazione che cambia la semantica del programma non è ammissibile;
2. richieda **meno risorse di calcolo**, ad esempio eseguendo meno istruzioni o istruzioni più veloci.

L'ottimizzazione avviene a due livelli:

1. **codice**: a parità di algoritmo, si modificano la struttura e le istruzioni usate;
2. **algoritmo**: la scelta dell'algoritmo può dare guadagni **molto più grandi** di qualunque ottimizzazione del codice.

E può essere fatta da due soggetti:

1. il **compilatore**: applica automaticamente molte trasformazioni (con `gcc -O1` il codice è già molto più efficiente che senza opzioni);
2. il **programmatore**: il compilatore non sempre riesce. La scelta dell'algoritmo spetta al programmatore, e a volte il compilatore deve fare **assunzioni conservative** per non rendere il programma scorretto, che il programmatore invece può rilassare.

> [!important] Il punto del capitolo
> Capire **quali ottimizzazioni fa già il compilatore** e quali no, per non perdere tempo a fare a mano ciò che `gcc -O1` fa da solo e concentrarsi su ciò che solo il programmatore può fare.

_(dispensa, p. 95)_

## Quanto conta ottimizzare le prestazioni

![[SDC-p096-1.png]]

La figura riporta 42 anni di dati sui microprocessori, in scala logaritmica: il numero di **transistor** (arancione) continua a crescere esponenzialmente; la **frequenza** (verde) e la **potenza** dissipata (rosso) si appiattiscono intorno al 2004–2005; le prestazioni **single-thread** (blu) rallentano; il numero di **core logici** (nero) inizia a crescere proprio quando la frequenza si ferma.

I programmatori professionisti danno spesso più peso ad altre qualità del software: **correttezza, affidabilità, robustezza, usabilità, verificabilità, manutenibilità, riparabilità, evolvibilità, riusabilità, portabilità, leggibilità, modularità**. Migliorarle spesso costa prestazioni:

- la **modularità** rende le parti riusabili, ma introduce più chiamate e salti rispetto a un programma "monolitico";
- la **robustezza** (controllare precondizioni, gestire casi imprevisti) richiede più istruzioni.

Allora perché ottimizzare? Perché **le prestazioni sono la "moneta" con cui si "comprano" le altre qualità**: rendendo più efficienti alcune parti, ci si può permettere di rendere le altre meno efficienti ma più pulite.

Per anni l'aumento del clock ha dato ai programmatori questa moneta **gratis**: il software sempre più pesante era compensato dall'hardware sempre più veloce. Gordon Moore previde negli anni '70 che il numero di transistor sarebbe raddoppiato ogni 18 mesi (poi corretto in 24): è la **legge di Moore**.

Il **2004** è stato un punto di svolta: alzare ancora la frequenza era insostenibile per il **surriscaldamento**, quindi i produttori sono passati ai processori **multi-core**. Da quel momento un programma non diventa più veloce da solo cambiando CPU: per sfruttare più core deve essere scritto in modo **parallelo**, uno sforzo spesso notevole. Programmare applicazioni parallele corrette ed efficienti è una delle grandi sfide attuali dell'ingegneria del software (vedi anche [[Symmetric Multiprocessing]]).

_(dispensa, pp. 96–97)_

## Cosa ottimizzare

Prima di ottimizzare bisogna capire **quali parti** sono critiche. Il programmatore deve:

1. stimare il **miglioramento complessivo** che si otterrebbe ottimizzando una parte, per capire se ne vale la pena (→ legge di Amdahl);
2. identificare le porzioni di codice che consumano la maggior parte del tempo o della memoria: gli **hot spot** o **colli di bottiglia**. Si usano i **performance profiler**.

### Metriche di prestazioni

Gli obiettivi dipendono dall'applicazione:

- **latenza**: durata di una singola operazione, dall'inizio alla fine;
- **throughput**: numero di operazioni completate per unità di tempo (anche se alcune singole operazioni sono lente);
- **spazio** occupato dai dati, per applicazioni con grandi moli di dati;
- **consumo di energia**, soprattutto su dispositivi mobili.

### Scala degli eventi

Per capire dove nascono i colli di bottiglia bisogna avere un'intuizione dei **tempi relativi** delle operazioni. La colonna "riscalata" moltiplica tutto in modo che un ciclo di clock duri 1 secondo:

| Evento | Latenza effettiva | Latenza riscalata |
| --- | --- | --- |
| Ciclo di clock | 0.4 ns | 1 s |
| Accesso cache L1 | 0.9 ns | 2 s |
| Accesso cache L2 | 2.8 ns | 7 s |
| Accesso cache L3 | 28 ns | 1 min |
| Accesso RAM DDR3 | 100 ns | 4 min |
| Accesso disco SSD | 50–150 µs | 1.5–4 giorni |
| Accesso disco a rotazione | 1–10 ms | 1–9 mesi |
| Pacchetto Internet continentale/intercontinentale | 65–141 ms | 5–11 anni |

Se un ciclo di clock durasse un secondo, leggere dalla RAM richiederebbe 4 minuti e leggere da un disco meccanico mesi. Per questo l'uso della **memoria** (cache, località) è spesso più importante del numero di istruzioni: vedi [[07 - SDC - Gestione dei dati in memoria centrale#Come ottenere le migliori prestazioni usando la memoria|capitolo 7]] e la [[Gerarchia di Memoria]].

_(dispensa, pp. 97–98)_

### Speedup e legge di Amdahl

Vedi [[Speedup e Legge di Amdahl]].

> [!definition] Speedup
> Se T è il tempo di esecuzione originale e T' quello dopo un'ottimizzazione, lo **speedup** è
> $$S = \frac{T}{T'}$$
> È un numero adimensionale; se S > 1 il programma ottimizzato è più veloce.

**Esempio 1**: T = 10 s, T' = 7 s, quindi $S = 10/7 \approx 1.42$ ("1.42x").

> [!definition] Legge di Amdahl
> Si divide il programma in due parti: A, che richiede $T_A = \alpha T$, e B, che richiede $T_B = (1-\alpha)T$. Se si rende A **k volte più veloce**:
> $$S = \frac{1}{\frac{\alpha}{k} + 1 - \alpha}$$
>
> *Dimostrazione*: $T' = \frac{T_A}{k} + T_B = \frac{\alpha T}{k} + (1-\alpha)T = \left(\frac{\alpha}{k} + 1 - \alpha\right)T$, quindi $S = \frac{T}{T'} = \frac{1}{\frac{\alpha}{k} + 1 - \alpha}$.

**Esempio 2**: si dimezza il tempo di una parte che pesa il 40% del totale: k = 2, α = 0.4, quindi

$$S = \frac{1}{\frac{0.4}{2} + 1 - 0.4} = \frac{1}{0.8} = 1.25$$

> [!tip] La conseguenza da ricordare
> Anche con k → ∞ (la parte A diventa istantanea), $S \to \frac{1}{1-\alpha}$. Se la parte ottimizzata pesa il 40%, il guadagno massimo è 1/0.6 ≈ **1.67x**, per quanto si lavori. Conviene ottimizzare le parti con **α grande**, cioè gli hot spot: per questo prima si **misura** (profiling) e poi si ottimizza.

(Amdahl la formulò per stimare il guadagno della parallelizzazione su più processori; questa è la variante per programmi sequenziali.)

_(dispensa, pp. 98–99)_

## Profilazione delle prestazioni

Vedi [[Profiling]].

La **profilazione** analizza il tempo (o un'altra metrica) richiesto dalle singole parti di un programma durante un'esecuzione. Due approcci:

- **instrumentare** il codice a mano, con chiamate alle system call di misurazione del tempo;
- usare un **profiler**, che raccoglie automaticamente i dati.

### System call di misurazione del tempo

![[SDC-p099-1.png]]

La figura è la mappa del [[01 - SDC - Cosa è un sistema di calcolo#Panoramica del funzionamento|capitolo 1]] con evidenziato il modulo **Timing** del kernel: `sleep`, `clock_gettime`, `getrusage`, con i temi di **risoluzione** e **latenza**, appoggiati al **timer** hardware.

Due famiglie di funzioni:

- `clock` e `getrusage` misurano il **tempo di CPU** usato dal processo, in modalità **utente** o **sistema** (ad esempio nelle system call). Non contano il tempo passato **in attesa** di un evento senza usare la CPU.
- `gettimeofday` e `clock_gettime` misurano il **tempo reale** (*wall clock time*), a partire da un istante fissato detto **epoca** (UNIX epoch o POSIX time, 1 gennaio 1970 00:00:00 UTC, esclusi i secondi intercalari).

Schema di misurazione:

```c
long start = misura_tempo();     // oppure double
// porzione di codice da misurare
long elapsed = misura_tempo() - start;
printf("Tempo richiesto: %ld\n", elapsed);
```

Una primitiva di misurazione ha due caratteristiche:

- **risoluzione**: il minimo intervallo misurabile;
- **latenza**: il tempo che impiega la funzione di misurazione stessa.

La durata da misurare dovrebbe essere **almeno un ordine di grandezza** maggiore sia della risoluzione sia della latenza, per tenere l'errore sotto il 10%. Se la porzione è troppo breve, la si **ripete** più volte e si divide il tempo totale per il numero di ripetizioni. Attenzione però: le ripetizioni successive trovano i dati già **in cache**, il che distorce la misura.

| | Tempo reale (`clock_gettime`) | Tempo di processo (`getrusage`) |
| --- | --- | --- |
| Precisione | alta | minore |
| Disturbi | include il tempo dato ad **altri processi** | conta solo il tempo del processo |

#### clock_gettime

```c
#include <time.h>
int clock_gettime(clockid_t clk_id, struct timespec *tp);
```

- `clk_id`: quale clock usare. Per misurare intervalli in modo affidabile si usa **`CLOCK_MONOTONIC`**, che non salta all'indietro se qualcuno cambia l'ora di sistema.
- `tp`: riceve il tempo in `tv_sec` (secondi) e `tv_nsec` (nanosecondi da sommare).
- Restituisce 0, oppure −1 ed `errno`.

Esempio: misura di un bubble sort su un array ordinato al contrario (il caso peggiore):

```c
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <time.h>
#define NUM 5000   // provare con 5

double get_real_time_msec() {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec*1E03 + ts.tv_nsec*1E-06;
}

void sort(int *v, int n) {
    int i, j;
    for (i=0; i<n; ++i)
        for (j=1; j<n; ++j)
            if (v[j-1] > v[j]) { int tmp = v[j-1]; v[j-1] = v[j]; v[j] = tmp; }
}

int main() {
    int i, *v = malloc(NUM*sizeof(int));
    assert(v != NULL);
    for (i=0; i<NUM; ++i) v[i] = NUM-i-1;
    double start = get_real_time_msec();
    sort(v, NUM);
    double elapsed = get_real_time_msec() - start;
    printf("Tempo richiesto da sort: %f msec\n", elapsed);
    free(v);
    return EXIT_SUCCESS;
}
```

Con NUM = 5 il tempo è così piccolo da essere confrontabile con la risoluzione e la latenza della misura: è l'esperimento per vedere il problema della misurabilità.

#### getrusage

```c
#include <sys/resource.h>
int getrusage(int who, struct rusage *r_usage);
```

- `who`: `RUSAGE_SELF` (il processo chiamante) o `RUSAGE_CHILDREN` (i suoi figli terminati);
- `r_usage->ru_utime`: tempo in modalità **utente**; `r_usage->ru_stime`: tempo in modalità **sistema** (entrambi `struct timeval`, con `tv_sec` e `tv_usec` in microsecondi);
- restituisce 0, oppure −1 ed `errno`.

```c
#include <sys/resource.h>
double get_user_time_msec() {
    struct rusage ru;
    getrusage(RUSAGE_SELF, &ru);
    return ru.ru_utime.tv_sec*1E03 + ru.ru_utime.tv_usec*1E-03;
}
```

_(dispensa, pp. 99–103)_

### gprof

`gprof` è uno dei profiler più usati su Linux/UNIX: **misura il tempo speso in ciascuna funzione**, così si individuano le funzioni **hot**.

1. Si compila con **`gcc -pg`** (vengono profilate solo le funzioni compilate con questa opzione).
2. Si **esegue normalmente** il programma (un po' più lento del solito): i profili vengono salvati nel file binario **`gmon.out`**.
3. Si visualizza il report con **`gprof nome-eseguibile`**.

Esempio:

```c
// test-profile.c
#include <string.h>
#include <stdlib.h>
#define M 100000
#define N 10000
void init(int *v, int n) { memset(v, n*sizeof(int), 255); }
void A(int *v, int n) { int i; for (i=0; i<n; i++) v[i] = v[i] / 2; }
void B(int *v, int n) { int i; for (i=0; i<n; i++) v[i] = v[i] >> 1; }
int main() {
    int* v = malloc(N*sizeof(int)), i;
    init(v, N);
    for (i=0; i<M; i++) { A(v, N); B(v, N); }
    free(v);
    return 0;
}
```

```
$ gcc test-profile.c -pg -O1 -o test-profile
$ ./test-profile
$ ls
gmon.out  test-profile  test-profile.c
$ gprof test-profile > report.txt
```

La prima tabella del report (*flat profile*):

```
Each sample counts as 0.01 seconds.
  %   cumulative   self              self     total
 time   seconds   seconds    calls  us/call  us/call  name
 63.86      0.56     0.56   100000     5.56     5.56  A
 37.15      0.88     0.32   100000     3.23     3.23  B
  0.00      0.88     0.00        1     0.00     0.00  init
```

- `% time`: percentuale del tempo totale usata dalla funzione;
- `self seconds`: secondi spesi nella funzione, **escluse** le funzioni chiamate;
- `calls`: numero di chiamate;
- `total us/call`: tempo medio per chiamata **incluse** le sottochiamate, in **microsecondi**;
- `name`: nome della funzione.

A pesa circa il 64% e B circa il 37%: gli sforzi andrebbero concentrati su **A**. Entrambe sono chiamate 100000 volte.

> [!note] Perché A è più lenta di B
> A e B fanno la stessa cosa, ma `v[i] / 2` su un `int` con segno non si può tradurre in un semplice `sar`: serve una correzione per arrotondare verso 0 (vedi [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Shift: SHL, SHR, SAL, SAR|capitolo 3]]). `v[i] >> 1` è un solo shift.

> [!warning] Correzioni
> - Nella dispensa `total us/call` è descritto "in millisecondi": *us* sta per **microsecondi** (µs).
> - Nell'esempio `memset(v, n*sizeof(int), 255)` gli ultimi due argomenti sono invertiti: la firma è `memset(ptr, valore, n)`, quindi andrebbe scritto `memset(v, 255, n*sizeof(int))`. Così com'è, scrive 255 byte di valore `(n*4) & 0xFF`.

`gprof` fa **misure approssimate** per campionamento, con precisione di 0.01 s: le funzioni che durano meno di 10 ms non compaiono. Ha senso solo se l'esecuzione dura abbastanza da raccogliere dati significativi.

_(dispensa, pp. 103–106)_

## Tecniche di ottimizzazione

Due strade principali per rendere più veloce un programma:

1. **ridurre il numero di istruzioni eseguite** (il "lavoro" o *work* totale su un dato input): la tecnica più importante;
2. **ridurre il tempo per istruzione**: non tutte le istruzioni costano uguale (una somma è più veloce di una divisione).

### Livelli di ottimizzazione in gcc

Vedi [[Ottimizzazioni del Compilatore]].

La dispensa analizza il codice IA32 generato da `gcc 4.8.2` (versioni diverse possono dare risultati diversi). Il livello si sceglie con `-Ox`:

| Opzione | Effetto |
| --- | --- |
| `-O0` | default: compilazione rapida, debugging prevedibile, nessuna ottimizzazione |
| `-O1` (o `-O`) | ottimizza; richiede più tempo e molta più memoria per funzioni grandi |
| `-O2` | quasi tutte le ottimizzazioni che **non aumentano la dimensione** del codice; la libc è tipicamente compilata così |
| `-O3` | ancora di più, anche a costo di codice più grande (es. inlining) |
| `-Os` | ottimizza per la **dimensione**: le ottimizzazioni di `-O2` che non ingrandiscono il codice, più altre |

Ogni livello include quelli precedenti. Si possono attivare o disattivare singole ottimizzazioni, ad esempio `-fomit-frame-pointer` (vista nel [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Stack frame e registro EBP|capitolo 3]]). Il salto da `-O0` a `-O1` dà il **miglioramento maggiore**; gli altri passaggi hanno di solito effetti meno marcati.

> [!warning] Correzione
> Il testo rimanda a "`-fomit-frame-pointer` vista nel Capitolo 4": è nel **capitolo 3** (§3.2.3.2).

_(dispensa, pp. 106–107)_

### Ridurre il numero di istruzioni eseguite

Il modo più efficace è usare **algoritmi efficienti**: per ordinare n elementi un algoritmo O(n log n) batte un O(n²) per n abbastanza grande, anche di ordini di grandezza. Qui però ci si concentra sulle ottimizzazioni del **codice**, basate sull'**analisi del testo del programma a tempo di compilazione**.

#### Constant folding

Si sostituiscono le **espressioni con operandi costanti** con il loro risultato.

| C originale | Dopo constant folding |
| --- | --- |
| `int f() { return 8+(14/2)*3; }` | `int f() { return 29; }` |

```asm
# gcc -O1 -S -fomit-frame-pointer test-cf.c
f: movl $29, %eax
   ret
```

`gcc` lo fa già a `-O1`: **non serve farlo a mano**.

#### Constant propagation

Se a una variabile viene assegnata una costante, le occorrenze successive della variabile si possono sostituire con quella costante. Si applica insieme al constant folding.

| C originale | Constant propagation | + constant folding |
| --- | --- | --- |
| `x = 8; return x-2;` | `x = 8; return 8-2;` | `x = 8; return 6;` |

```asm
# gcc -O1                    # senza ottimizzazioni
f: movl $8, x                f: movl $8, x
   movl $6, %eax                movl x, %eax
   ret                          subl $2, %eax
                                ret
```

`x = 8` resta perché `x` è una **variabile globale**, che altre funzioni potrebbero leggere. Lo fa `gcc -O1`.

#### Common subexpression elimination

Le **sottoespressioni ripetute** si calcolano una volta sola e si riusa il valore.

| C originale | Dopo CSE |
| --- | --- |
| `return (x + y)*(x + y);` | `int z = x + y; return z * z;` |

```asm
# gcc -O1: x+y calcolato una volta sola
f: movl  8(%esp), %eax
   addl  4(%esp), %eax
   imull %eax, %eax
   ret
```

Senza ottimizzazioni, `x+y` viene calcolato due volte (una con `leal`, una con `addl`). `gcc -O1` fa la CSE, ma **a volte va fatta a mano**: ad esempio se l'espressione contiene **chiamate a funzione** il cui codice il compilatore non conosce (non può sapere se due chiamate restituiscono lo stesso valore).

> [!note]
> L'intestazione dell'esempio senza ottimizzazioni nella dispensa dice `test-cp.c`, ma si riferisce a `test-cse.c`.

#### Loop-invariant code motion (hoisting)

Vedi [[Loop-Invariant Code Motion]].

Si individuano nel corpo di un ciclo le parti che calcolano **sempre lo stesso valore** a ogni iterazione (*loop-invariant*) e le si **sposta prima del ciclo** (*code motion*): vengono eseguite una volta sola.

**Esempio 1**: lo fa il compilatore.

| C originale | Hoisting manuale |
| --- | --- |
| `int s = 1;`<br>`for (; n>0; n--) s *= 7+x;` | `int s = 1, z = 7+x;`<br>`for (; n>0; n--) s *= z;` |

```asm
# gcc -O1
f:   movl  8(%esp), %edx
     testl %edx, %edx
     jle   .L4
     movl  $1, %eax
     movl  4(%esp), %ecx
     addl  $7, %ecx        # 7+x calcolato PRIMA del ciclo
.L3: imull %ecx, %eax      # corpo del ciclo
     subl  $1, %edx
     jne   .L3
     ret
.L4: movl  $1, %eax
     ret
```

**Esempio 2**: lo deve fare il programmatore.

```c
int has_space(const char* s) {
    int i;
    for (i=0; i<strlen(s); i++)          // strlen ricalcolata a ogni iterazione!
        if (s[i]==' ') return 1;
    return 0;
}
// versione corretta
int has_space(const char* s) {
    int i, n = strlen(s);
    for (i=0; i<n; i++)
        if (s[i]==' ') return 1;
    return 0;
}
```

`strlen` costa O(n) e viene chiamata a ogni iterazione: la funzione originale costa **Θ(n²)** invece di O(n). È un **performance bug**, cioè un'inefficienza che non dovrebbe esserci (bug così si trovano anche in software reale, ad esempio nel programma `wf` di Fedora 17).

**Perché il compilatore non lo fa?** Nell'esempio 1 il codice da spostare è visibile e il compilatore può verificare che sia invariante. Con una **chiamata a funzione** non sa, in generale, quale codice verrà eseguito (potrebbe essere deciso a runtime, caricando una libreria dinamica), né se la funzione ha **effetti collaterali**: se `strlen` tenesse un contatore delle proprie invocazioni, spostarla cambierebbe il comportamento. **In mancanza di informazioni, il compilatore sceglie l'opzione più conservativa**: non fa un'ottimizzazione che potrebbe cambiare la semantica. Tocca al programmatore.

#### Loop unrolling

Si riduce di un fattore k il numero di iterazioni, facendo in un'iterazione il lavoro di k iterazioni consecutive. Così diminuiscono i **test** e i **salti** del ciclo.

```c
// originale
int sum(int *v, int n) {
    int i, s = 0;
    for (i=0; i<n; ++i) s += v[i];
    return s;
}
// unrolling di fattore 3
int sum(int *v, int n) {
    int i, s = 0;
    for (i=0; i+2<n; i+=3) {
        s += v[i];
        s += v[i+1];
        s += v[i+2];
    }
    for (; i<n; ++i) s += v[i];   // elementi rimanenti se n non è multiplo di 3
    return s;
}
```

Il secondo `for` serve per gli ultimi elementi quando la dimensione non è multipla di 3. I compilatori lo fanno spesso da soli.

#### Function inlining

Si **sostituisce una chiamata a funzione con il corpo** della funzione chiamata. Conviene per funzioni piccole chiamate spesso (ad esempio in un ciclo).

Vantaggi:

1. si evitano le istruzioni per il passaggio dei parametri, la `call`, la gestione dello stack frame e la `ret`;
2. il codice del chiamato è dentro il chiamante, quindi si possono applicare ottimizzazioni **globali** (es. constant propagation tra le due funzioni);
3. migliora la **località spaziale** del codice: meno salti verso codice che non è in cache.

Svantaggio: il codice diventa più grande (*code bloat*), di solito senza grande impatto.

| C originale | Inlining manuale |
| --- | --- |
| `int sqr(int x) { return x*x; }`<br>`... v[i] = sqr(i);` | `... v[i] = i*i;` |

```asm
# gcc -O3 (oppure -finline-functions)
.L6: movl  %eax, %edx           # inizio ciclo
     imull %eax, %edx           # i*i: sqr non viene chiamata
     movl  %edx, (%ebx,%eax,4)
     addl  $1, %eax
     cmpl  %ecx, %eax
     jne   .L6
```

`gcc` lo applica a `-O3` o con `-finline-functions`.

_(dispensa, pp. 107–113)_

### Ridurre il costo delle istruzioni

Si sostituiscono istruzioni con alternative più veloci, o si cambia il contesto in cui vengono eseguite.

#### Register allocation

I registri sono la memoria più veloce: il compilatore cerca di tenere in registro gli oggetti usati spesso (ad esempio le variabili di un ciclo). In C si può suggerirlo con `register int x;`, ma i compilatori moderni tengono comunque le variabili nei registri, che ci sia `register` o no.

L'**allocazione dei registri** associa a ogni variabile, in ogni porzione di codice, un registro o una locazione di memoria. I registri sono pochi: a volte una variabile va spostata da un registro in memoria per liberarlo (**register spilling**). `gcc` alloca i registri automaticamente già a `-O1`.

```c
void f(int n) { while (n--) g(); }
```

| `-O0` (nessuna allocazione) | `-O1` |
| --- | --- |
| `f:  jmp L3`<br>`L4: call g`<br>`L3: movl 4(%esp), %eax`<br>`    leal -1(%eax), %edx`<br>`    movl %edx, 4(%esp)`<br>`    testl %eax, %eax`<br>`    jne L4`<br>`    ret` | `f:  pushl %ebx`<br>`    movl 8(%esp), %ebx`<br>`    testl %ebx, %ebx`<br>`    je L3`<br>`L5: call g`<br>`    subl $1, %ebx`<br>`    jne L5`<br>`L3: popl %ebx`<br>`    ret` |

Con `-O0` `n` vive sempre in memoria (`4(%esp)`): ogni iterazione fa **due accessi a memoria** (una lettura e una scrittura). Con `-O1` `n` viene caricata una volta in `%ebx` e resta lì.

> [!question] Perché `%ebx` e non un registro caller-save?
> Perché `%ebx` è **callee-save**: `g` è obbligata a preservarlo, quindi `f` non deve salvarlo e ripristinarlo attorno a **ogni** chiamata a `g` nel ciclo. Lo salva una volta sola nel prologo. Vedi [[Registri Caller-save e Callee-save]].

#### Strength reduction

Si sostituisce un'istruzione con una **meno costosa**. Moltiplicare per una potenza di 2 equivale a uno shift a sinistra; dividere per una potenza di 2 a uno shift (aritmetico) a destra. A volte si usano anche somme e sottrazioni. Shift, somme e sottrazioni sono molto più veloci di moltiplicazioni e divisioni.

| Operazione | Equivalente più efficiente |
| --- | --- |
| `x / 8` | `x >> 3` |
| `x * 64` | `x << 6` |
| `x * 2` | `x << 1` oppure `x + x` |
| `x * 15` | `(x << 4) - x` |

> [!warning] Attenzione con i negativi
> `x / 8 == x >> 3` vale solo per `x` **non negativo** (o `unsigned`). Per `x` negativo lo shift aritmetico arrotonda verso −∞ e la divisione C verso 0 (es. −9/8 = −1, ma −9 >> 3 = −2). Il compilatore lo sa e aggiunge una correzione.

```c
int f(int x) { return 17*x; }
```

```asm
f: movl 4(%esp), %eax    # eax = x
   movl %eax, %edx       # edx = x
   sall $4, %edx         # edx = x << 4 = 16x
   addl %edx, %eax       # eax = 16x + x = 17x
   ret
```

Anche moltiplicazioni con **entrambi i fattori non costanti** in un ciclo si possono trasformare in somme ripetute:

```c
for (i=0; i<n; i++) v[i] = i*k;              // originale
for (i=0, c=0; i<n; i++) { v[i] = c; c += k; }  // strength reduction
```

`gcc` lo fa già a `-O1`.

#### Allineamento dei dati in memoria

Vedi [[Allineamento e Padding]].

Per convenzione, ogni oggetto di s byte inizia a un indirizzo x **multiplo di s** (x mod s = 0): uno `short` a indirizzo pari, un `int` a un multiplo di 4. Su alcuni processori un accesso **disallineato** è più lento o genera addirittura un'eccezione. Per garantire l'allineamento il compilatore inserisce spazio inutilizzato tra oggetti consecutivi: il **padding**. È un classico **compromesso tempo-spazio**: codice più veloce, ma più memoria.

L'allineamento si applica ovunque:

- **data**: variabili globali;
- **stack frame**: parametri e variabili locali;
- **heap**: ogni blocco allocato inizia a un multiplo di una potenza di 2, tipicamente 16 byte;
- **codice**: l'indirizzo di una funzione è spesso allineato alla dimensione di una linea di cache (tipicamente 64 byte);
- **strutture**: i campi di tipi primitivi.

Esempio:

```c
struct S {
    char a;
    int b;
    short c;
    char d;
    int e;
    char f;
};
```

![[SDC-p116-1.png]]

Le celle grigie sono i campi, quelle bianche il padding. `a` sta all'offset 0; `b` (int) deve stare a un multiplo di 4, quindi 3 byte di padding e `b` agli offset 4–7; `c` (short) a 8–9; `d` a 10; `e` (int) richiede un multiplo di 4, quindi 1 byte di padding ed `e` a 12–15; `f` a 16. Infine 3 byte di padding finale, perché **la dimensione della struct deve essere un multiplo della dimensione del suo campo più grande** (4): così, in un array di struct, ogni elemento resta allineato. Totale: **20 byte** per 13 byte di dati.

#### Altre ottimizzazioni

Più avanti si vedranno ottimizzazioni legate all'hardware: riordinare le istruzioni per sfruttare il **pipelining** ([[06 - SDC - Esecuzione dei programmi#Pipelining|capitolo 6]]) e riordinare gli accessi alla memoria per sfruttare la **cache** ([[07 - SDC - Gestione dei dati in memoria centrale#Esempi|capitolo 7]]).

_(dispensa, pp. 113–117)_

### Ridurre lo spazio di memoria

- **Codice**: il compilatore può ridurlo, ad esempio con `gcc -Os`.
- **Dati**: scegliendo la rappresentazione più adatta. Ad esempio un array occupa meno memoria di una struttura collegata (niente puntatori `next`).

#### Ottimizzare lo spazio delle struct

Basta **ordinare i campi dal più grande al più piccolo**:

```c
struct S {
    int b;
    int e;
    short c;
    char a;
    char d;
    char f;
};
```

![[SDC-p117-1.png]]

Ora `b` (0–3), `e` (4–7), `c` (8–9), `a` (10), `d` (11), `f` (12), più 3 byte di padding finale: **16 byte** invece di 20 (−20%).

#### Dead code elimination

Si eliminano le porzioni di codice che **non possono mai essere eseguite**.

| C originale | Dopo DCE |
| --- | --- |
| `if (0) return 10;`<br>`return 20;` | `return 20;` |

```asm
f: movl $20, %eax
   ret
```

`gcc` lo fa **anche senza** opzioni di ottimizzazione.

_(dispensa, pp. 117–118)_

### Le ottimizzazioni dei compilatori sono le migliori possibili?

No. I compilatori usano algoritmi sofisticati ma **non sempre ottengono il risultato ottimo**: ad esempio l'allocazione dei registri è in generale un problema **NP-completo** (Chaitin et al., 1981), quindi si usano algoritmi approssimati.

Si può analizzare l'assembly generato (`gcc -S`) e modificarlo a mano, ma con **molta cautela**:

1. spesso un'apparente ottimizzazione ha poco impatto o peggiora le cose: ha senso solo se le istruzioni modificate sono un vero **collo di bottiglia** (misurato col profiling);
2. il **rischio di introdurre errori** è molto alto.

## Riepilogo: chi fa cosa

| Ottimizzazione | La fa `gcc`? | Quando serve il programmatore |
| --- | --- | --- |
| Scelta dell'algoritmo | no | sempre |
| Constant folding / propagation | sì, `-O1` | — |
| Common subexpression elimination | sì, `-O1` | se ci sono chiamate a funzione |
| Loop-invariant code motion | sì, `-O1`, se il codice è visibile | se ci sono chiamate a funzione (es. `strlen`) |
| Loop unrolling | sì (livelli alti) | raramente |
| Function inlining | sì, `-O3` / `-finline-functions` | raramente |
| Register allocation | sì, `-O1` | — |
| Strength reduction | sì, `-O1` | — |
| Ordinamento dei campi delle struct | no (lo vieta lo standard C) | sempre |
| Dead code elimination | sì, anche `-O0` | — |

_(dispensa, p. 118)_
