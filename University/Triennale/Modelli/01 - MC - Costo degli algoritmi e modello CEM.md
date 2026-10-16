---
title: Costo degli algoritmi e modello CEM
aliases:
  - MC — Costo degli algoritmi e modello CEM
tags:
  - modelli-di-calcolo
  - complessita
  - analisi-algoritmi
  - cem
source: Introduzione alla complessità di calcolo - Fabrizio D_Amore.pdf (prefazione, §1.1–1.2.2); appunti di Clelia (24/02–03/03/2022)
---

# Costo degli algoritmi e modello CEM

> [!abstract]
> Il corso parte da una domanda: **cosa può essere calcolato da un calcolatore, e quanto costa farlo?** La prima metà (*cosa*) è la teoria della calcolabilità, che si vedrà dalla [[06 - MC - Cardinalità e diagonalizzazione|lezione 6]] in poi; questa lezione inizia la seconda metà (*quanto costa*), la teoria della complessità. Il problema è definire il costo di un algoritmo in modo **oggettivo**: indipendente dal calcolatore, dal linguaggio, dal compilatore e dai dati di prova. La soluzione è contare le operazioni elementari eseguite da una macchina astratta, la **CEM** (*C Elementary Machine*), in funzione della **dimensione dell'input** e nel **caso peggiore**. La [[02 - MC - Notazione asintotica|lezione successiva]] aggiunge l'ultimo ingrediente: la notazione asintotica.
> Mappa del corso: [[MOC - Modelli di Calcolo]].

## Cosa può essere calcolato, e quanto costa

La prima parte della domanda fu studiata **prima che esistessero i calcolatori**: negli anni '30 diversi ricercatori si chiesero cosa significasse davvero "calcolabile", non solo per i calcoli numerici ma per i problemi della matematica e della logica. Proposero dei **modelli di calcolo astratti**: un insieme di operazioni ammissibili e di regole per scrivere ed eseguire programmi, eseguibili anche a mano, senza una macchina fisica (la [[Macchina di Turing|macchina di Turing]] è il più famoso). Gli obiettivi erano due:

1. stabilire i **limiti** dei modelli di calcolo: esistono calcoli "impossibili"?
2. individuare gli **elementi essenziali** del calcolo: modelli molto semplici che però risolvano tutto ciò che risolvono modelli più complessi.

Sulla scia del teorema di Gödel, la risposta al primo punto è netta: **esistono problemi che non possono essere risolti da un elaboratore** (vedi [[07 - MC - Halting Problem|Halting Problem]]).

La teoria della calcolabilità però non considera **quanto** sia costoso, in tempo e memoria, risolvere un problema. Non ha molto senso dire che un problema è risolubile se la soluzione richiede tutti i calcolatori del pianeta per mille anni. La **teoria della complessità** studia cosa si può calcolare *in pratica*. La dispensa ha due obiettivi:

1. definire **in termini matematici il costo di un algoritmo**, ottenendo una valutazione indipendente dal linguaggio di programmazione, dall'elaboratore e dai dati di prova (capitolo 1, lezioni 1–5);
2. mostrare che **non tutti i problemi sono risolubili in modo efficiente** (capitolo 2, [[14 - MC - Classi P e NP e NP-completezza|lezione 14]]).

## Introduzione: complessità di calcolo

L'analisi della complessità spiega **come si comporta un algoritmo al crescere dell'input**. Se l'algoritmo impiega 1 secondo su un input di dimensione 1000, quanto impiegherà raddoppiando l'input? Lo stesso tempo, la metà, il quadruplo? Saperlo permette di prevedere il comportamento con 2000 o 10000 utenti senza dover fare test di quelle dimensioni.

> [!important] Definizioni
> - La **complessità di calcolo** (o complessità computazionale) di un **algoritmo** è la quantità di **risorse** richieste per la sua esecuzione.
> - La complessità computazionale di un **problema** è la **minima** complessità di un algoritmo (noto o ignoto) che lo risolve.

Le risorse che interessano sono il **tempo** di calcolo e lo **spazio** (memoria usata). Delle due la più importante, e quella considerata nel seguito, è il tempo: in pratica è quasi sempre la risorsa critica, anche perché il costo delle memorie continua a scendere. (Ci sono eccezioni: negli smartphone ridurre il tempo significa consumare meno energia, e nei sistemi embedded dell'IoT i processori costano meno di un euro ma hanno pochissima memoria.)

> [!note] Qualità e proprietà
> Non si confondano le **qualità** di un algoritmo (come l'efficienza) con le sue **proprietà** (correttezza, finitezza…): le proprietà devono essere sempre soddisfatte, le qualità possono mancare ma aumentano il valore dell'algoritmo.

L'analisi riguarda il **calcolo**, non le altre cose che fanno i computer (traffico di rete, input/output con l'utente). E non ha solo interesse teorico: le considerazioni di efficienza guidano le scelte del progettista, insieme ai requisiti del dominio applicativo. Lo strumento per farlo è la **capacità di confrontare algoritmi**.

### Upper bound e lower bound: l'idea

Vedi anche [[Delimitazioni superiori e inferiori]].

Negli appunti di Clelia (lezione del 24/02/2022) il punto di partenza è il **costo effettivo**: il numero di microistruzioni macchina eseguite, una misura che non dipende dal tempo (secondi). La curva del costo in funzione della dimensione dell'input è spesso irregolare; la si **delimita** sopra e sotto con due curve più semplici:

- **upper bound** (limite superiore): "costa *al più* così";
- **lower bound** (limite inferiore): "costa *almeno* così".

Se non si conosce il costo preciso, a volte si sa comunque che è sicuramente inferiore o superiore a qualcosa. Interessa l'**andamento asintotico**; idealmente le due curve hanno lo stesso andamento e il costo è "schiacciato" fra le due (*analisi tight*, come nel teorema dei carabinieri). Si studiano i **casi peggiori**. Le definizioni precise sono nella [[02 - MC - Notazione asintotica|lezione 2]].

## Valutazione dell'efficienza degli algoritmi

Un programma è più efficiente di un altro se richiede meno risorse. Se si potesse misurare il tempo in secondi, basterebbe eseguire i due programmi con un cronometro (esistono i *profiler*, che misurano i millisecondi e aiutano a trovare i colli di bottiglia). Ma questo metodo **non è attendibile**, perché il risultato dipende:

- dall'**elaboratore**: il confronto vale solo sulla stessa macchina;
- dal **linguaggio**: per input piccoli un cattivo algoritmo in assembly può battere un buon algoritmo in Python; e a parità di linguaggio conta il **compilatore** (o l'interprete);
- dai **dati di ingresso**: i due programmi devono ricevere gli stessi dati;
- dalla **significatività** dei dati: un'esecuzione sola non basta, ma dopo quante prove si può decidere?

Persone diverse, con prove diverse, potrebbero arrivare a conclusioni opposte. Si vuole invece una misura che confronti gli algoritmi **a livello di idea**, ignorando linguaggio, hardware e set di istruzioni della CPU.

## Calcolo del costo di esecuzione di un programma

Vedi [[Modello di costo CEM]].

Il costo si esprime come **funzione matematica della dimensione dell'input**. Per non dipendere dall'elaboratore si contano le **operazioni elementari** eseguite da una macchina ispirata all'architettura di **von Neumann** e completamente dedicata.

![[MC-L01-01.png]]

La figura (*Fig. 1.1*) mostra l'architettura classica di von Neumann: la **CPU**, composta da unità aritmetico-logica (ALU) e unità di controllo, comunica con la **memoria centrale** (la griglia di celle), che a sua volta scambia dati con la **memoria di massa** e con le **periferiche di I/O**. Programma e dati stanno nella stessa memoria; la CPU esegue un'istruzione alla volta. Contare le istruzioni eseguite da questa macchina è il modo naturale di misurare il tempo.

Si introduce allora una macchina astratta, la **CEM** (*C Elementary Machine*). La differenza fondamentale rispetto alla macchina di von Neumann è che la CEM **esegue direttamente algoritmi scritti in un linguaggio ad alto livello**: si fa riferimento al C, ma la trattazione si adatta a qualunque linguaggio o allo pseudo-codice.

> [!note] Dagli appunti di Clelia
> La CEM è un'invenzione del docente e ha valenza solo teorica: è un "acceleratore" per l'analisi asintotica, utile sia per algoritmi iterativi sia ricorsivi. Si immagina un C **interpretato** riga per riga, senza compilatore.

> [!important] Definizione 1 (costo su CEM)
> Ogni **operazione elementare** ha **costo unitario**. Il costo di un'istruzione composta è la somma dei costi delle sue componenti. Per le istruzioni di controllo di flusso e di ciclo si imputa un costo unitario per ogni **test**, più il costo delle istruzioni eseguite.

In particolare:

- **istruzione semplice** (assegnazione, lettura, scrittura): costo pari al numero di celle di memoria a cui assegna un valore, quindi **unitario** per le istruzioni semplici della CEM (in Python `x = 1` costa 1, ma `x = (1, 2, 3, 4)` aggiorna quattro celle e costa 4);
- **ciclo**: costo totale dei test di fine ciclo (unitari, quindi pari al numero di volte che il test viene eseguito) più il costo totale del corpo, tenendo conto di quante volte è eseguito;
- **if**: costo del test più costo del ramo eseguito (per `if-else` il ramo vero o quello falso);
- **chiamata di sottoprogramma**: costo di tutte le istruzioni del sottoprogramma, comprese eventuali altre chiamate.

**Tabella 1.1 — costi delle istruzioni C** (con le annotazioni di Clelia):

| costrutto C | costo |
|---|---|
| valutazione di espressione semplice (che non invoca funzioni) | unitario (es. `x+1`, `x+y+z`, `a*b+c/8`) |
| valutazione di espressione complessa (che invoca funzioni) | 1 + somma dei costi delle funzioni chiamate |
| assegnazione a variabile o a elemento di array/struct | costo dell'espressione assegnata + costo dell'eventuale espressione che definisce l'indice (trascurabile se unitario) |
| istruzione composta | somma dei costi delle istruzioni componenti |
| chiamata di funzione | costo della funzione (unitario per `malloc`/`free`; dimensione dell'area allocata per `calloc`) + 1 |
| `return <expr>;` | costo valutazione `<expr>` (+1, asintoticamente irrilevante) |
| `if(<expr>)...` | costo valutazione `<expr>` + costo istruzione eseguita |
| `switch(<expr>)...` | costo valutazione `<expr>` + somma costi istruzioni eseguite (nel caso peggiore tutte, se non ci sono `break`) |
| `while(<expr>)...` con $p$ iterazioni | $(p+1) \cdot$ costo valutazione `<expr>` + $p \cdot$ costo istruzione eseguita |
| `do...while(<expr>);` con $p$ iterazioni | $p \cdot$ costo valutazione `<expr>` + $p \cdot$ costo istruzione eseguita |
| `for(<ist1>;<expr>;<ist2>)...` con $p$ iterazioni | costo `<ist1>` + $(p+1) \cdot$ costo `<expr>` + $p \cdot$ costo `<ist2>` + $p \cdot$ costo istruzione eseguita |

Il $+1$ nel `while` è l'ultima valutazione del test, quella che esce dal ciclo.

> [!example] Costi unitari (dagli appunti)
> - `x = 1`: costo 1 (non è proprio vero, dipende; ma è un'approssimazione);
> - `x = x + 1`: costo 1, non 2 (somma e assegnazione insieme);
> - `<variabile> = <espressione semplice>`: 1; `A + B` e `A + B*C`: 1;
> - `A + f(A)`: $1 + \text{costo di } f(A)$;
> - `return x`: 1; `return pippo(A)`: $1 + \text{costo}(\texttt{pippo}(A))$.

### Perché i costi uniformi non sono "grossolani"

Con la CEM hanno lo stesso costo (unitario) `x = 1` e

```c
a[j-1] = x * j + (beta / 2) - gamma / (3 * delta + 8);
```

che richiede moltiplicazioni e divisioni. Sembra un'ipotesi arbitraria, addirittura errata. Ma se $t_1$ è il tempo della prima istruzione e $t_2$ quello della seconda, esiste una costante $c$ tale che

$$c \cdot t_1 \ge t_2$$

cioè $t_2$ supera $t_1$ al più di un **fattore costante**. Lo stesso vale per ogni altra istruzione, con costanti diverse. Clelia lo formalizza così: se $c$ è il costo minimo di un'istruzione semplice (es. `x = 0`) e $C$ il massimo (es. `x = y*z + h/8`), ogni istruzione semplice costa $d$ con $c \le d \le C$. I costi uniformi **introducono errori, ma non differenze asintotiche**.

Il vantaggio è grande: si può prescindere dal linguaggio e ragionare direttamente sull'algoritmo in linguaggio naturale. Bisogna però fare attenzione a non considerare unitarie operazioni che non lo sono: in Python, per esempio, le operazioni su stringhe non costano in generale 1.

> [!warning] Abusare del modello
> Clelia annota un avvertimento del docente (lezione del 04/03/2022): la CEM assume **memoria infinita** e che **ogni intero in memoria abbia grandezza arbitraria** a costo unitario. Se si abusa di queste ipotesi si ottengono risultati assurdi. Per esempio, per l'unicità della scomposizione in fattori primi, un intero $N = 2^{a_1} 3^{a_2} 5^{a_3} 7^{a_4} \cdots$ può **codificare un intero programma** (gli esponenti $a_i$ descrivono le righe): se manipolare $N$ costasse 1, si "eseguirebbero" programmi interi in un passo. Per questo esistono modelli più "duri", come la **RAM** (*Random Access Machine*) a costi uniformi o logaritmici.

## Analisi nel caso peggiore in funzione della dimensione dell'input

Vedi [[Dimensione dell'input]] e [[Analisi del caso peggiore]].

Il costo dipende quasi sempre dai dati di ingresso: ordinare 10 elementi richiede meno tempo che ordinarne 10000. Per questo **la dimensione dell'input è l'argomento della funzione di costo**.

> [!important] Dimensione dell'input
> Per **dimensione** (o taglia) dell'input si intende la **quantità di memoria necessaria per memorizzare i dati** di input. Per l'ordinamento di un insieme, è il numero di elementi.
>
> Clelia: è il **numero di bit necessari e sufficienti** per descrivere l'input. Se l'input è un **intero** $N$, la dimensione non è $N$ ma il suo **logaritmo**: $|N| = \lfloor \log_2 N \rfloor + 1$ bit.

Anche a parità di dimensione, il costo dipende dai particolari dati: si distinguono **caso migliore**, **caso peggiore** e **caso medio**. Per una valutazione oggettiva non si deve dipendere da casi fortunati:

> [!important] Definizione 2 (valutazione del costo di un programma)
> Il costo di un programma si valuta **in funzione della dimensione dell'input**, con riferimento al **caso peggiore** (quello in cui l'esecuzione impiega più tempo), assumendo che il costo di ogni istruzione semplice sia pari a uno.

### Esempio: ricerca sequenziale

Gli elementi di un insieme sono memorizzati in un vettore `a`; la dimensione dell'input è il numero di elementi $n$.

```c
1. int ricercaSequenziale(int a[], int n, int k) {
2. /*
3.    restituisce indice della posizione di k
4.    oppure -1 se k non presente; assume n > 0
5. */
6.    int i = 0;
7.    while((i < n) && (a[i] < k)) i = i + 1;
8.    if((i == n) || (a[i] > k)) return -1;
9.    else return i;
10. }
```

Il ciclo avanza finché `a[i] < k`: il vettore è supposto **ordinato** (lo annota Clelia), quindi la scansione si ferma al primo elemento $\ge k$. La riga 8 restituisce $-1$ se si è arrivati in fondo o se l'elemento trovato è maggiore di $k$.

Il costo dipende dall'elemento cercato: 1 confronto se è il primo, 2 se è il secondo, $i$ se è l'$i$-esimo. Il **caso peggiore** è la ricerca dell'ultimo elemento, o di un elemento più grande di tutti, perché si esaminano tutte le componenti. Costo nel caso peggiore:

- l'assegnazione a riga 6 costa 1;
- il ciclo `while` a riga 7, con $p$ iterazioni ($0 \le p \le n$), costa $(p+1) + p = 2p + 1$ (test e corpo); al massimo $2n + 1$;
- l'`if` alle righe 8–9 costa 2 (test semplice e `return`).

Totale su CEM nel caso peggiore: $1 + (2n+1) + 2 = 2n + 4$: **la complessità è proporzionale a $n$**.

> [!warning] Correzione
> Nel codice della dispensa la riga 8 è `if((i == n) || (a[i] > k) return -1;`, con una parentesi chiusa mancante (qui è stata aggiunta). Il testo poi parla di "assegnazioni nelle linee 6., 16. e 18.", ma questo programma ha un'unica assegnazione iniziale, alla riga 6 (le righe 16 e 18 appartengono alla ricerca binaria della [[03 - MC - Esempi di analisi di complessità#Ricerca binaria|lezione 3]]). Clelia arriva a $2n + 3$ invece di $2n + 4$ contando 1 per la riga 9: la differenza è una costante additiva, asintoticamente irrilevante.

> [!tip] Dimensione vera dell'input (dagli appunti)
> L'input di `ricercaSequenziale` è il vettore ($n \cdot \text{cost}$ byte), più $n$ e $k$: $z = n \cdot \text{cost} + \log n + \log k$. I termini non crescono indipendentemente: $n \cdot \text{cost}$ domina $\log n$, e $\log k$ è limitato dalla dimensione delle celle (costante). Quindi $z \approx n \cdot \text{cost}$ e il costo è una funzione lineare di $z$. Le funzioni $10n + 5$ e $10000n + 5$ sono asintoticamente uguali: entrambe $O(n)$.
>
> Attenzione invece ai salti: passare da $\log x$ a $x$, o da $x$ a $2^x$, è un **salto esponenziale**. Confondere il valore di un numero con la sua dimensione cambia completamente la classe di costo (vedi [[03 - MC - Esempi di analisi di complessità#Calcolo della potenza di un numero|potenza]] e [[03 - MC - Esempi di analisi di complessità#Test di primalità|primalità]]).

### Problemi di decisione

Negli appunti compare anche (25/02/2022) il primo accenno ai **problemi di decisione**, quelli con risposta **sì o no**. Si possono modellare come problemi di **appartenenza a un insieme**: l'insieme delle istanze con risposta sì. Un problema di calcolo si può spesso trasformare in uno di decisione: "risolvere $2x^2 - 10x + 7 = 0$" diventa "date l'equazione e i valori $x_1 = 3$, $x_2 = 7$, sono queste le soluzioni?". Per un problema $P$ bisogna definire l'**istanza** (i dati di ingresso): l'insieme di tutte le possibili istanze è lo spazio su cui si lavora. Per i problemi di decisione esistono algoritmi efficienti, inefficienti, oppure **nessun algoritmo**: i problemi **indecidibili** sono molti più di quelli decidibili ([[06 - MC - Cardinalità e diagonalizzazione|lezione 6]]).

## Ingredienti dell'analisi

> [!summary] Riepilogo
> L'analisi di un algoritmo (dagli appunti di Clelia) è:
> - **asintotica** (conta l'andamento per input grandi, [[02 - MC - Notazione asintotica|lezione 2]]);
> - nel **caso peggiore**;
> - **in funzione della dimensione dell'input** (in bit, non del valore);
> - a **costi uniformi** (le istruzioni elementari costano 1 sulla CEM).
>
> Il costo su CEM di `ricercaSequenziale` è $2n + 4$: lineare.
