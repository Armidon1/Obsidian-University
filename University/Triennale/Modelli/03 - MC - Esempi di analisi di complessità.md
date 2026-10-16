---
title: Esempi di analisi di complessità
aliases:
  - MC — Esempi di analisi di complessità
tags:
  - modelli-di-calcolo
  - complessita
  - analisi-algoritmi
  - pseudopolinomiale
source: Introduzione alla complessità di calcolo - Fabrizio D_Amore.pdf (§1.3); Esempi algoritmi ricorsione.pdf; appunti di Clelia (04/03/2022)
---

# Esempi di analisi di complessità

> [!abstract]
> Questa lezione applica gli strumenti delle [[01 - MC - Costo degli algoritmi e modello CEM|lezioni 1]] e [[02 - MC - Notazione asintotica|2]] (CEM, caso peggiore, notazione asintotica, istruzione dominante) ad algoritmi concreti: ricerca binaria, ordinamento a bolle, potenza, test di primalità, schema di Horner. Il filo conduttore è la differenza fra **valore** e **dimensione** dell'input: `potenza(a, b)` fa $b$ moltiplicazioni, un numero che sembra "lineare", ma $b$ si scrive con $\log_2 b$ bit, quindi il costo è **esponenziale** nella dimensione dell'input. Sono gli algoritmi **pseudopolinomiali**, che torneranno con l'[[04 - MC - Algoritmi ricorsivi ed equazioni di ricorrenza#Calcolo del massimo comun divisore: l'algoritmo di Euclide|algoritmo di Euclide]] e con la [[14 - MC - Classi P e NP e NP-completezza#La classe P|definizione della classe P]].
> Mappa del corso: [[MOC - Modelli di Calcolo]].

## Ricerca binaria

Vedi [[Ricerca binaria]] (ASD).

```c
11. /*
12.    restituisce indice della posizione di k
13.    oppure -1 se k non presente; assume n > 0
14. */
15. int ricercaBinaria(int a[], int n, int k) {
16.    int primo = 0, ultimo = n - 1, media;
17.    while(primo <= ultimo) {
18.       media = (primo + ultimo) / 2;
19.       if(a[media] == k) return media;
20.       else if(a[media] < k) primo = media + 1;
21.       else ultimo = media - 1;
22.    }
23.    return -1;
24. }
```

Il vettore è ordinato. A ogni passo si confronta $k$ con l'elemento centrale dell'intervallo $[\mathit{primo}, \mathit{ultimo}]$: se è uguale si è trovato, se è minore si cerca nella metà destra, altrimenti in quella sinistra.

Costo su CEM nel caso peggiore:

- riga 16: due assegnazioni, costo 2;
- l'istruzione condizionale alle righe 19–21 ha costo massimo 3 (nel percorso più lungo si valutano due espressioni semplici e si esegue un'assegnazione);
- ciclo `while` alle righe 17–22: detto $q \ge 0$ il numero di iterazioni, il test costa 1 e il corpo al più $1 + 3 = 4$, quindi $q$ iterazioni costano $(q + 1) + 4q = 5q + 1$;
- il `return` a riga 23 costa 1.

**Quante iterazioni?** A ogni iterazione la differenza $\mathit{ultimo} - \mathit{primo}$ si dimezza (precisamente $d_{i+1} = \lfloor (d_i - 1)/2 \rfloor$), quindi il numero massimo di dimezzamenti è $\lfloor \log_2 n \rfloor + 1$, che è anche il massimo valore di $q$. Il ciclo costa al più $5\lfloor \log_2 n \rfloor + 6$.

Lo stesso ragionamento a parole: dopo un confronto la ricerca prosegue su metà degli elementi, dopo due su un quarto, dopo $m$ su $n/2^m$. Ci si ferma quando l'elemento è trovato o la tavola ha un solo elemento: nel caso peggiore il numero di confronti è il più piccolo $m$ tale che

$$\frac{n}{2^m} \le 1 \iff n \le 2^m \iff m \ge \log_2 n$$

Costo totale su CEM:

$$2 + (5\lfloor \log_2 n \rfloor + 6) + 1 = 5\lfloor \log_2 n \rfloor + 9 = O(\log_2 n)$$

> [!note] Dagli appunti di Clelia
> L'istruzione dominante è `media = (primo + ultimo) / 2` (riga 18). Il costo è circa $5 \log n$, che è $O(\log n)$ ma anche $\Omega(\log n)$: quindi $\Theta(\log n)$. La dimensione dell'input è $z = c \cdot n$ (il vettore), quindi $n = z/c$ e il costo è $\Theta(\log(z/c)) = \Theta(\log z)$.

**Confronto con la ricerca sequenziale** ([[01 - MC - Costo degli algoritmi e modello CEM#Esempio: ricerca sequenziale|lezione 1]]): in spazio sono sostanzialmente equivalenti (`ricercaSequenziale` usa $n + 3$ variabili intere, `ricercaBinaria` $n + 5$: entrambe $O(n)$), ma in tempo c'è un **salto esponenziale**: logaritmico contro lineare.

> [!example] Valore e dimensione (dagli appunti)
> ```c
> for(i = 0; i < n; i++) a = a + 1;
> ```
> - Se l'input è **un intero** $n$, la dimensione è $z = |n| = \log n$, quindi $n = 2^z$ e il costo è $\Theta(n) = \Theta(2^z)$: **esponenziale**.
> - Se l'input è **un array di $n$ celle**, $z = c \cdot n$ e il costo è $\Theta(n) = \Theta(z/c) = \Theta(z)$: **lineare**.
>
> Lo stesso codice ha costi di classe diversa a seconda di cosa sia l'input.

## Ordinamento a bolle (bubble sort)

L'ordinamento a bolle cerca di trarre vantaggio da un eventuale ordinamento parziale del vettore. Prima una versione semplificata, che consiste di $n$ fasi:

1. **Prima fase**: si parte da $A[n]$ e si fanno confronti e scambi: si confronta $A[n]$ con $A[n-1]$ e, se $A[n] < A[n-1]$, si scambiano (non rispettano l'ordine crescente); poi $A[n-1]$ con $A[n-2]$, poi $A[n-2]$ con $A[n-3]$, e così via fino ad $A[2]$ e $A[1]$. Alla fine **l'elemento più piccolo è risalito in prima posizione**.
2. **Seconda fase**: analoga, ma si arriva fino al confronto fra $A[3]$ e $A[2]$. Il secondo più piccolo finisce in seconda posizione.
3. In generale, al termine della fase $i$ l'$i$-esimo elemento più piccolo è in posizione $i$.

Se a ogni elemento si associa un peso pari al suo valore, gli elementi più leggeri risalgono in cima come **bolle**: da qui il nome.

> [!example] Esecuzione (Figura 1.3 della dispensa)
> Vettore iniziale $A = [3, 6, 4, 2]$ (in figura dall'alto in basso; $j$ indica il confronto fra $A[j-1]$ e $A[j]$):
>
> | passo | vettore | confronto |
> |---|---|---|
> | (a) | 3, 6, 4, 2 | $A[3]=4$ e $A[4]=2$: scambio |
> | (b) | 3, 6, 2, 4 | $A[2]=6$ e $A[3]=2$: scambio |
> | (c) | 3, 2, 6, 4 | $A[1]=3$ e $A[2]=2$: scambio |
> | (d) | 2, 3, 6, 4 | fine prima fase: il minimo è in cima |
> | (e) | 2, 3, 6, 4 | $A[3]=6$ e $A[4]=4$: scambio |
> | (f) | 2, 3, 4, 6 | $A[2]=3$ e $A[3]=4$: niente |
> | (g) | 2, 3, 4, 6 | terza fase: $A[3]=4$ e $A[4]=6$: niente |
> | (h) | 2, 3, 4, 6 | nessuno scambio: il vettore è ordinato |

**Miglioramento.** Non sempre servono $n - 1$ fasi: il vettore può risultare ordinato prima. Se durante una fase **non avviene nessuno scambio**, il vettore è ordinato; se avviene almeno uno scambio, non si può saperlo. La versione definitiva usa una variabile booleana `ordinato`, posta a `true` all'inizio di ogni fase e a `false` a ogni scambio: se a fine fase è ancora vera, ci si ferma.

> [!warning] Programma mancante
> La dispensa dice "Il programma che lo implementa è il seguente:" ma il codice non compare. Una versione coerente con la descrizione (indici da 1 a $n$, la bolla parte dal fondo):
> ```c
> void bubbleSort(int A[], int n) {      /* A[1..n] */
>    int i = 1, j, t, ordinato = 0;
>    while(i < n && !ordinato) {
>       ordinato = 1;
>       for(j = n; j > i; j--)            /* confronto A[j-1] e A[j] */
>          if(A[j] < A[j-1]) {
>             t = A[j]; A[j] = A[j-1]; A[j-1] = t;
>             ordinato = 0;
>          }
>       i++;
>    }
> }
> ```

**Costo.** Dipende dalla configurazione dei dati:

- **caso migliore**: vettore già ordinato in senso crescente. Basta una scansione, senza scambi, che verifica l'ordinamento: $O(n)$;
- **caso peggiore**: servono tutte le $n - 1$ fasi, il che accade quando il vettore è ordinato in senso **decrescente**.

> [!example] Caso peggiore (Figura 1.4)
> | (a) | (b) | (c) | (d) | (e) | (f) |
> |---|---|---|---|---|---|
> | 6 | 1 | 1 | 1 | 1 | 1 |
> | 5 | 6 | 2 | 2 | 2 | 2 |
> | 4 | 5 | 6 | 3 | 3 | 3 |
> | 3 | 4 | 5 | 6 | 4 | 4 |
> | 2 | 3 | 4 | 5 | 6 | 5 |
> | 1 | 2 | 3 | 4 | 5 | 6 |
>
> Ogni colonna è il vettore alla fine di una fase: a ogni fase **un solo** elemento va nella posizione definitiva.

I confronti sono $n - 1$ nella prima fase, $n - 2$ nella seconda, $n - i$ nella fase $i$:

$$(n-1) + (n-2) + \dots + 2 + 1 = \frac{n(n-1)}{2}$$

La complessità del bubble sort ottimizzato è $O(n^2)$ (e, poiché questo numero di confronti si raggiunge, $\Theta(n^2)$ nel caso peggiore).

> [!tip] Esercizio della dispensa
> *Si analizzi la complessità della versione semplificata.* Esegue sempre tutte le fasi, indipendentemente dai dati: $\Theta(n^2)$ anche nel caso migliore.

### Tabelle riassuntive

**Tabella 1.3 — costi asintotici di caso peggiore** ($z$ = dimensione dell'input; la base del logaritmo non conta, perché cambiarla equivale a moltiplicare per una costante):

| algoritmo | costo asintotico |
|---|---|
| `ricercaSequenziale` | $\Theta(z)$ |
| `ricercaBinaria` | $\Theta(\log z)$ |
| `potenza` | $\Theta(2^z)$ |
| `primo` | $\Theta(2^{z/2})$ |
| ordinamento a bolle | $\Theta(n^2)$ |

**Tabella 1.4 — istruzioni dominanti** (ricostruita: nella dispensa l'impaginazione delle colonne è saltata):

| algoritmo | istruzione dominante | esecuzioni | riga |
|---|---|---|---|
| `ricercaSequenziale(a,n,k)` | `(i < n) && (a[i] < k)` | $n + 1$ | 7 |
| | `i = i + 1` | $n$ | 7 |
| `ricercaBinaria(a,n,k)` | `primo <= ultimo` | $\lfloor \log_2 n \rfloor + 2$ | 17 |
| | `media = (primo+ultimo)/2` | $\lfloor \log_2 n \rfloor + 1$ | 18 |
| | `if(a[media] == k)` | $\lfloor \log_2 n \rfloor + 1$ | 19 |
| | `if(a[media] < k)`, `primo = media + 1` | $\lfloor \log_2 n \rfloor + 1$ | 20 |
| | `ultimo = media - 1` | $\lfloor \log_2 n \rfloor + 1$ | 21 |
| `potenza(a, b)` | `b > 0` | $b + 1$ | 31 |
| | `f = f * a`, `b = b - 1` | $b$ | 32, 33 |
| `primo(n)` | `d <= sqrt(n)` | $\lceil \sqrt n / 2 \rceil$ | 46 |
| | `d += 2`, `if(!(n % d))` | $\lceil \sqrt n / 2 \rceil - 1$ | 46, 47 |

> [!note] Riga incompleta
> La tabella della dispensa contiene anche una riga "`????` — `a[i]=potenza(a[i],exp)` — $n$ — riga 60", relativa a un algoritmo (alla riga 60) che non compare nel testo. È un residuo di una versione precedente: va ignorata.

## Calcolo della potenza di un numero

Questo esempio evidenzia l'importanza di riconoscere **quale parte dell'input è davvero rilevante** per il costo.

```c
25. /*
26.    determina la potenza a^b
27.    assume b >= 0
28. */
29. int potenza(int a, int b) {
30.    int f = 1;
31.    while(b > 0) {
32.       f = f * a;
33.       b = b - 1;
34.    }
35.    return f;
36. }
```

L'algoritmo calcola $a^b$ con $b$ moltiplicazioni. Su CEM: costi unitari per le assegnazioni alle righe 30, 32 e 33; il ciclo `while` alle righe 31–34 costa $3b + 1$ ($b$ iterazioni, quindi $b + 1$ test e $2b$ assegnazioni); il `return` costa 1. Totale $3b + 3$.

- Il costo dipende **solo da $b$**: al variare di $a$ il tempo non cambia apprezzabilmente. L'analista esperto riconosce a priori le parti di input non significative per il costo.
- $3b + 3$ è funzione del **valore** di $b$, non della **dimensione** $|b|$. Con $z = |b| = \lfloor \log_2 b \rfloor + 1$ si ha $b = O(2^z)$: la complessità è $O(2^z)$, **esponenziale**.

(La dispensa scrive "$b = O(2^b)$ e quindi la complessità è $O(2^b)$": l'esponente giusto è $z$, la dimensione.)

> [!warning] Overflow
> Una nota interna della dispensa ("ALB: questo esempio ha il problema che possiamo andare in overflow") avverte che con `int` il risultato $a^b$ esce presto dall'intervallo rappresentabile. Per l'analisi del costo non cambia nulla, ma sulla CEM si sta implicitamente usando l'ipotesi di "interi di grandezza arbitraria a costo unitario" (vedi l'[[01 - MC - Costo degli algoritmi e modello CEM#Perché i costi uniformi non sono "grossolani"|avvertimento sulla CEM]]).

### Potenza intera (dalle slide di esempi)

Le slide "Algoritmi — esempi di analisi" (2023) riprendono lo stesso problema con due versioni.

**Potenza banale** ($a \ge 0$, $b > 0$):

```c
int potenza(int a, int b) {
   int r = a;
   for(int i = 2; i <= b; i++)
      r *= a;
   return r;
}
```

- istruzione dominante: `r *= a`, eseguita $b - 1$ volte;
- dimensione dell'input $z = |b| \simeq \log_2 b$, quindi $2^z \simeq b$;
- costo $\Theta(b) = \Theta(2^z)$ in funzione della dimensione dell'input.

**Potenza++ (quadrati successivi)**: sfrutta la rappresentazione binaria di $b$.

```c
long potenza_pp(long a, int b) {
   long r = 1;
   while(b > 0) {
      int lsb = b & 0x1;     /* bit meno significativo di b */
      if(lsb) r *= a;
      a *= a;                /* a, a^2, a^4, a^8, ... */
      b >>= 1;               /* scorre al bit successivo */
   }
   return r;
}
```

Esempio: $47 = 1 \cdot 32 + 0 \cdot 16 + 1 \cdot 8 + 1 \cdot 4 + 1 \cdot 2 + 1 \cdot 1$, quindi
$$2^{47} = 2^{32} \cdot 2^{8} \cdot 2^{4} \cdot 2^{2} \cdot 2$$
e i fattori $2, 2^2, 2^4, 2^8, \dots$ si ottengono **elevando al quadrato ripetutamente**. Il ciclo fa un'iterazione per bit di $b$: costo $\Theta(\log b) = \Theta(|b|)$, **lineare** nella dimensione dell'input.

> [!example] Le due versioni a confronto: $6^{15}$
> La versione banale fa 14 moltiplicazioni: $r = 36, 216, 1296, 7776, 46656, \dots, 470184984576$.
>
> La versione per quadrati ($15 = 1111_2$, tutti i bit a 1) fa 4 iterazioni:
>
> | $a$ | $b$ | $r$ dopo l'iterazione | lsb |
> |---|---|---|---|
> | 6 | 15 | 6 | 1 |
> | 36 | 7 | 216 | 1 |
> | 1296 | 3 | 279936 | 1 |
> | 1679616 | 1 | 470184984576 | 1 |
>
> Entrambe restituiscono $6^{15} = 470\,184\,984\,576$. Con $b$ di 1000 bit la prima farebbe circa $2^{1000}$ moltiplicazioni, la seconda circa 1000.

## Test di primalità

Un altro esempio per chiarire la differenza fra dimensione e valore dell'input, su un intero positivo $n$ (primo se ammette come soli divisori 1 e $n$). L'algoritmo non verifica tutti i possibili divisori: considera solo $\{2\} \cup \{3, 5, 7, 9, \dots, \lfloor\sqrt n\rfloor\}$, cioè 2 e i dispari fino a $\sqrt n$. Infatti, se $n$ non ha divisori $\le \sqrt n$, non ne ha nessuno (se $n = d \cdot e$ con $d \le e$, allora $d \le \sqrt n$).

```c
37. int primo(int n) {
38. /*
39.    restituisce 1 se n è primo
40.    oppure un divisore <= sqrt(n)
41.    assume n > 1
42. */
43.    int d;
44.    if(n <= 3) return 1;                  /* n è 2 o 3 */
45.    if(!(n % 2)) return 2;                /* n è pari */
46.    for(d = 3; d <= sqrt(n); d += 2)      /* inutile testare i pari */
47.       if(!(n % d))                       /* n è divisibile per d */
48.          return d;
49.    return 1;                             /* n è primo */
50. }
```

Il caso peggiore è quando $n$ è primo maggiore di 3: si arriva al `return 1` della riga 49. Il costo è $3 + (p + 1) + p + p + 1 = 3p + 5$, con $p$ numero massimo di iterazioni del `for`; le istruzioni alle righe 46 e 47 sono dominanti ed eseguite $p$ volte. Si provano tutti i dispari fra 3 e $\sqrt n$:

$$p = \left\lceil \frac{\sqrt n}{2} \right\rceil - 1 \approx \frac{\sqrt n}{2}$$

Il costo in funzione di $n$ è $O(\sqrt n / 2)$, **sub-lineare** nel valore. In funzione di $z = |n| = \lfloor \log_2 n \rfloor + 1 \approx \log_2 n + 1$: $n \approx 2^{z-1}$, $\sqrt n \approx 2^{(z-1)/2}$, e il costo è $O(2^{(z-3)/2})$, cioè $O(2^{z/2})$: **esponenziale**.

> [!important] Valore contro dimensione
> In `potenza` e in `primo`, esprimere il costo in funzione del **valore** dell'input ($n$) invece che della sua **dimensione** ($|n|$) cambia profondamente la funzione di costo: sub-lineare contro esponenziale. Per un'analisi corretta e standardizzata non bisogna mai confondere i due concetti.
>
> Un algoritmo il cui costo è polinomiale nel **valore** numerico dell'input ma esponenziale nella sua **dimensione** si dice **pseudopolinomiale** (vedi [[Algoritmo pseudopolinomiale]]). Clelia annota: se il costo di un problema è polinomiale il problema è **trattabile**, se è esponenziale è **intrattabile**. `potenza` banale e `primo` sono pseudopolinomiali; `potenza_pp` è polinomiale. (Esiste anche un test di primalità polinomiale nella dimensione, l'algoritmo AKS del 2002: è per questo che la [[14 - MC - Classi P e NP e NP-completezza#Teoria dell'NP-completezza: conclusioni|tabella "facile/difficile"]] mette la primalità fra i problemi facili.)

## Algoritmo di Horner

Calcola il valore di un polinomio $a_0 + a_1 x + \dots + a_n x^n$ in un punto $x$, con i coefficienti memorizzati dal termine noto a quello di grado massimo.

```c
double horner(double a[], int n, double x) {
   double res = a[n];
   for(int i = n-1; i >= 0; i--)
      res = res * x + a[i];
   return res;
}
```

Si basa sulla riscrittura $a_0 + x(a_1 + x(a_2 + \dots + x(a_{n-1} + x\,a_n)))$: invece di calcolare ogni potenza $x^i$, si moltiplica e si somma $n$ volte.

- operazione dominante: `res = res * x + a[i]`, eseguita $n$ volte ($n$ = grado del polinomio);
- costo $\Theta(n)$, lineare nella dimensione dell'input (i coefficienti sono $n + 1$).

## Sort ricorsivo

L'ultima slide di esempi introduce l'analisi ricorsiva, oggetto della [[04 - MC - Algoritmi ricorsivi ed equazioni di ricorrenza|lezione successiva]]:

```c
void sort(int *a, int n) {
   if(n == 1) return;
   sort(a + 1, n - 1);              /* ordina gli ultimi n-1 */
   int p = a[0];
   int i = 1;
   while((a[i] < p) && (i < n)) {   /* inserisce a[0] al suo posto */
      a[i - 1] = a[i];
      i++;
   }
   a[i - 1] = p;
   return;
}
```

È un ordinamento per inserimento ricorsivo: si ordinano ricorsivamente gli ultimi $n - 1$ elementi, poi si fa scorrere il primo verso destra finché non trova il suo posto. Il costo deriva da istruzioni a costo costante, dal ciclo (al più $n - 1$ iterazioni) e dalla ricorsione:

$$T(n) = T(n-1) + cn \qquad T(1) = c'$$

Srotolando: $T(n) = T(n-k) + c\sum_{i=0}^{k-1}(n - i) = T(n-k) + c\,(n + (n-1) + \dots + (n-k+1))$, che per $k = n - 1$ dà $T(n) \in \Theta(n^2)$.

> [!warning] Correzione
> La condizione del ciclo è scritta `(a[i] < p) && (i < n)`: quando `i` arriva a `n` si legge `a[n]`, **fuori dal vettore**, prima di controllare `i < n`. Per sfruttare la valutazione cortocircuitata di `&&` l'ordine corretto è `(i < n) && (a[i] < p)`, come nel `while` di `ricercaSequenziale`.

## Riepilogo

> [!summary]
> - **Ricerca binaria**: $5\lfloor \log_2 n \rfloor + 9$ su CEM, $\Theta(\log n)$; salto esponenziale rispetto alla ricerca sequenziale.
> - **Bubble sort**: $\Theta(n)$ nel caso migliore (con la variabile `ordinato`), $n(n-1)/2$ confronti e $\Theta(n^2)$ nel caso peggiore (vettore decrescente).
> - **Potenza** banale: $\Theta(b) = \Theta(2^z)$, esponenziale nella dimensione; per **quadrati successivi**: $\Theta(\log b) = \Theta(z)$.
> - **Primalità** per tentativi: $O(\sqrt n) = O(2^{z/2})$, esponenziale nella dimensione.
> - **Horner**: $\Theta(n)$.
> - Mai confondere **valore** e **dimensione** dell'input: è la definizione di algoritmo **pseudopolinomiale**.
