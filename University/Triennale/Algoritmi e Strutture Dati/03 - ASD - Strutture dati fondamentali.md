---
title: Strutture dati fondamentali
aliases:
  - ASD — Strutture dati fondamentali
tags:
  - algoritmi-e-strutture-dati
  - array
  - liste-concatenate
  - insertion-sort
  - equals
  - clone
source: Goodrich, Tamassia, Goldwasser - Algoritmi e strutture dati in Java (cap. 3)
---

# Strutture dati fondamentali

> [!abstract]
> Il capitolo presenta le due strutture "concrete" su cui sono costruite quasi tutte le altre del libro:
> - gli **array**, con accesso diretto per indice ma capacità fissa e inserimenti/rimozioni interni costosi (esempi: tabellone dei punteggi, insertion sort, cifrario di Cesare, tris);
> - le **liste concatenate** (semplici, circolari, doppie), che crescono e si riducono nodo per nodo e permettono inserimenti e rimozioni in tempo costante alle estremità.
>
> Chiudono il capitolo due problemi tipici dei riferimenti: **quando due oggetti sono uguali** (`==` contro `equals`) e **come copiare** una struttura (copia superficiale contro copia profonda).
> Il capitolo usa i [[02 - ASD - Progettazione orientata agli oggetti#Programmazione mediante tipi generici|tipi generici]] e le [[02 - ASD - Progettazione orientata agli oggetti#Classi annidate|classi annidate]] del cap. 2; queste liste diventeranno le implementazioni di pile e code nel [[06 - ASD - Pile, code e code doppie|cap. 6]] e delle liste posizionali nel [[07 - ASD - Liste e iteratori|cap. 7]]. Il costo delle operazioni, qui detto "tempo costante" o "proporzionale a $n$", sarà formalizzato nel [[04 - ASD - Analisi di algoritmi|cap. 4]].
> Mappa del corso: [[MOC - Algoritmi e Strutture Dati]].

---

## Array

Gli [[01 - ASD - Introduzione a Java#Array|array]] sono strutture dati concrete in cui si accede ai dati con un **indice intero**. Vediamo alcune applicazioni.

### Memorizzare in un array i punteggi di un gioco

Il primo esempio memorizza i **punteggi migliori** di un videogioco: è lo stesso schema che serve per qualunque sequenza ordinata di oggetti (pazienti di un ospedale, giocatori di una squadra, …).

Un punteggio è un oggetto con il nome del giocatore e il valore:

```java
public class GameEntry {
  private String name;   // nome del giocatore
  private int score;     // punteggio
  /** Costruisce una registrazione di punteggio usando i valori forniti. */
  public GameEntry(String n, int s) {
    name = n;
    score = s;
  }
  /** Restituisce il nome del giocatore. */
  public String getName() { return name; }
  /** Restituisce il punteggio memorizzato. */
  public int getScore() { return score; }
  /** Restituisce una stringa che rappresenta questo oggetto. */
  public String toString() {
    return "(" + name + ", " + score + ")";
  }
}
```

#### La classe Scoreboard

Il **tabellone** (`Scoreboard`) ha una capacità massima (10, 50, 500… a seconda del gioco, quindi la si passa al costruttore). I punteggi stanno nell'array `board`, **ordinati dal più alto al più basso** (il massimo in `board[0]`); le celle non usate valgono `null`.

```java
/** Classe che memorizza punteggi in un array in ordine non crescente. */
public class Scoreboard {
  private int numEntries = 0;     // numero di punteggi memorizzati
  private GameEntry[] board;      // array dei punteggi (nome e valore)
  /** Costruisce un tabellone vuoto con la capacità massima data. */
  public Scoreboard(int capacity) {
    board = new GameEntry[capacity];
  }
  // ... altri metodi
}
```

![[ASD-p114-1.png]]

La figura mostra un array di lunghezza 10 con 6 riferimenti a oggetti `GameEntry` nelle celle 0–5, in ordine decrescente di punteggio (Mike 1105, Rob 750, Paul 720, Anna 660, Rose 590, Jack 510); le celle 6–9 sono `null`. Ogni cella contiene un **riferimento** (il "telecomando"), non l'oggetto.

#### Aggiungere un punteggio

Un nuovo punteggio entra se il tabellone **non è pieno**, oppure se è **strettamente maggiore** dell'ultimo (il minimo) presente.

```java
/** Aggiunge un nuovo punteggio al tabellone (se è abbastanza alto). */
public void add(GameEntry e) {
  int newScore = e.getScore();
  // il nuovo punteggio ha diritto di entrare?
  if (numEntries < board.length || newScore > board[numEntries-1].getScore()) {
    if (numEntries < board.length)     // nessun punteggio deve uscire
      numEntries++;                    // quindi il numero totale aumenta
    // sposta a destra i punteggi più bassi per fare spazio al nuovo
    int j = numEntries - 1;
    while (j > 0 && board[j-1].getScore() < newScore) {
      board[j] = board[j-1];           // sposta un elemento da j-1 a j
      j--;
    }
    board[j] = e;                      // inserisce il nuovo punteggio
  }
}
```

- Se il tabellone è pieno, `numEntries` non cambia: il nuovo punteggio prende il posto dell'ultimo, che viene sovrascritto (esce dal tabellone).
- Il ciclo parte da `j = numEntries - 1` (dove finirà il punteggio minimo) e sposta a destra di una cella ogni punteggio inferiore a quello nuovo, finché trova la cella giusta.

![[ASD-p115-1.png]]

Inserimento di Jill (740): i riferimenti a Paul, Anna, Rose e Jack sono già stati spostati di una cella verso destra (le frecce curve), lasciando libera la cella 2. Mike (1105) e Rob (750) restano dove sono.

![[ASD-p116-1.png]]

Al termine `board[2] = e` mette Jill nella cella 2, la posizione corretta tra Rob (750) e Paul (720).

> [!tip] Variante
> Se non serve tenere i punteggi in ordine, inserimento e rimozione si fanno **senza cicli** (esercizio C-3.19): si aggiunge in fondo, e per rimuovere si sposta l'ultimo elemento nel buco.

#### Eliminare un punteggio

Per eliminare un punteggio (es. un giocatore scoperto a barare) si usa `remove(i)`: tutti i punteggi successivi scorrono di una cella **verso sinistra** per chiudere il buco.

![[ASD-p117-1.png]]

Rimozione di Paul (indice 3): Anna, Rose e Jack scorrono a sinistra (frecce curve) e la cella che era dell'ultimo torna `null`.

```java
/** Elimina e restituisce il punteggio all'indice i. */
public GameEntry remove(int i) throws IndexOutOfBoundsException {
  if (i < 0 || i >= numEntries)
    throw new IndexOutOfBoundsException("Invalid index: " + i);
  GameEntry temp = board[i];                 // salva l'oggetto da rimuovere
  for (int j = i; j < numEntries - 1; j++)   // da i in avanti
    board[j] = board[j+1];                   // sposta a sinistra
  board[numEntries - 1] = null;              // svuota l'ultima cella usata
  numEntries--;
  return temp;
}
```

- L'oggetto rimosso si salva in `temp` per poterlo restituire.
- Il ciclo si ferma a `numEntries - 1`, non alla capacità dell'array: non serve spostare le celle `null`. L'ultima iterazione esegue `board[numEntries-2] = board[numEntries-1]`, poi la cella `numEntries-1` viene messa a `null`.

> [!note] Conclusioni
> `add` e `remove` sono semplici, ma sono il modello di tecniche usate continuamente nel libro. Il loro limite è la **capacità fissa**: la classe `ArrayList` di Java la supera copiando tutto in un array più grande quando serve ([[07 - ASD - Liste e iteratori#Array dinamici|Paragrafo 7.2]]).

_(libro, pp. 112–118)_

### Ordinare un array

Vedi [[Ordinamento per inserimento]].

**Ordinare** (*sorting*) significa disporre gli elementi in ordine non decrescente. Gli algoritmi di ordinamento sono il tema del [[12 - ASD - Ordinamento e selezione|cap. 12]]; qui se ne vede uno semplice, l'**ordinamento per inserimento** (*insertion sort*), che riusa l'idea di `Scoreboard.add`.

Idea: si considera un elemento alla volta e lo si inserisce nella posizione giusta tra quelli che lo precedono (che sono già ordinati). Il primo elemento è banalmente in ordine; il secondo si scambia con il primo se è minore; il terzo scorre a sinistra finché non è a posto rispetto ai primi due; e così via.

```
Algorithm InsertionSort(A):
  Input: un array A di n elementi confrontabili
  Output: l'array A ordinato in modo non decrescente
  for k from 1 to n − 1 do
    inserisci A[k] nella posizione corretta tra A[0], A[1], ..., A[k]
```

![[ASD-p119-1.png]]

Esecuzione su 8 caratteri (`B C D A E H G F`). Ogni riga è un'iterazione del ciclo esterno; a sinistra c'è `cur`, l'elemento da inserire (grigio chiaro). Le copie della stessa riga sono le iterazioni del ciclo interno: "spostamento" quando un elemento più grande scorre a destra, "inserimento" quando `cur` viene posato nel buco. `C`, `D`, `E`, `H` non richiedono spostamenti; `A` deve scavalcare tre elementi; `G` scavalca `H`; `F` scavalca `H` e `G`. Alla fine l'array è `A B C D E F G H`.

```java
/** Ordinamento non decrescente di un array di caratteri per inserimento */
public static void insertionSort(char[] data) {
  int n = data.length;
  for (int k = 1; k < n; k++) {          // inizia dal secondo carattere
    char cur = data[k];                  // è il momento di inserire cur = data[k]
    int j = k;                           // trova l'indice j corretto per cur
    while (j > 0 && data[j-1] > cur) {   // data[j-1] deve scavalcare cur
      data[j] = data[j-1];               // fai scorrere data[j-1] a destra
      j--;                               // e considera il j precedente
    }
    data[j] = cur;                       // questo è il posto giusto per cur
  }
}
```

| Caso | Lavoro del ciclo interno |
|---|---|
| array già ordinato | 1 confronto per elemento, nessuno spostamento (caso migliore) |
| array ordinato al contrario | ogni elemento scorre fino all'inizio (caso peggiore) |

Nel [[04 - ASD - Analisi di algoritmi|cap. 4]] si vedrà che il caso peggiore costa $O(n^2)$ e il migliore $O(n)$.

_(libro, pp. 118–120)_

### I metodi di java.util per gli array e i numeri casuali

La classe **`java.util.Arrays`** raccoglie metodi **statici** utili sugli array (si invocano come `Arrays.sort(data)` dopo `import java.util.Arrays;`):

| Metodo | Effetto |
|---|---|
| `equals(A, B)` | `true` se A e B hanno la stessa lunghezza e gli stessi elementi nello stesso ordine |
| `fill(A, x)` | scrive `x` in ogni cella di A |
| `copyOf(A, n)` | nuovo array di dimensione `n` con i primi $k = \min(n, A.length)$ elementi di A; le celle in più ricevono il valore predefinito (0, `null`) |
| `copyOfRange(A, s, t)` | nuovo array di dimensione $t - s$ con gli elementi da `A[s]` ad `A[t-1]` (oltre la fine: valori predefiniti) |
| `toString(A)` | stringa `[a0, a1, ...]`, con `String.valueOf` per ogni elemento (`"null"` per i riferimenti nulli) |
| `sort(A)` | ordina A secondo l'ordinamento naturale degli elementi |
| `binarySearch(A, x)` | cerca `x` nell'array **ordinato** A: restituisce l'indice se c'è, altrimenti $-y-1$, dove $y$ è il punto in cui andrebbe inserito (quindi un valore negativo). La ricerca binaria è nel Paragrafo 5.1.3, [[05 - ASD - Ricorsione#Ricerca binaria]] |

#### Generazione di numeri pseudocasuali

Per collaudare programmi sugli array servono spesso dati casuali. **`java.util.Random`** genera numeri **pseudocasuali**: sembrano casuali ma sono determinati dai precedenti. Un generatore molto usato (lineare congruenziale) calcola

$$next = (a \cdot cur + b) \bmod n$$

con $a, b, n$ interi scelti opportunamente (Java usa qualcosa di simile con $n = 2^{48}$). La sequenza è statisticamente uniforme, sufficiente per giochi e collaudi, ma **prevedibile**: per la sicurezza servono sorgenti veramente casuali (es. segnali radio dallo spazio profondo).

Il primo valore è il **seme** (*seed*): lo stesso seme produce sempre la stessa sequenza. Per avere sequenze diverse a ogni esecuzione si usa un seme che cambia, come `System.currentTimeMillis()` (millisecondi dal 1° gennaio 1970).

| Metodo di `Random` | Restituisce |
|---|---|
| `nextBoolean()` | il prossimo `boolean` |
| `nextDouble()` | il prossimo `double` in $[0.0, 1.0)$ |
| `nextInt()` | il prossimo `int` |
| `nextInt(n)` | il prossimo `int` in $[0, n)$ |
| `setSeed(s)` | imposta il seme al `long` `s` |

> [!tip] Collegamento
> Generatori pseudocasuali e veramente casuali sono discussi dal punto di vista della sicurezza in [[PRNG (Pseudo-Random Number Generator)]] e [[TRNG (True Random Number Generator)]] (Cybersecurity).

```java
import java.util.Arrays;
import java.util.Random;
/** Programma che illustra alcuni usi degli array */
public class ArrayTest {
  public static void main(String[] args) {
    int data[] = new int[10];
    Random rand = new Random();                     // generatore pseudocasuale
    rand.setSeed(System.currentTimeMillis());       // seme = ora attuale
    // riempie l'array con numeri pseudocasuali da 0 a 99
    for (int i = 0; i < data.length; i++)
      data[i] = rand.nextInt(100);
    int[] orig = Arrays.copyOf(data, data.length);  // copia dell'array
    System.out.println("arrays equal before sort: " + Arrays.equals(data, orig));
    Arrays.sort(data);                              // ordina data (orig non cambia)
    System.out.println("arrays equal after sort: " + Arrays.equals(data, orig));
    System.out.println("orig = " + Arrays.toString(orig));
    System.out.println("data = " + Arrays.toString(data));
  }
}
```

```
arrays equal before sort: true
arrays equal after sort: false
orig = [41, 38, 48, 12, 28, 46, 33, 19, 10, 58]
data = [10, 12, 19, 28, 33, 38, 41, 46, 48, 58]
```

Ogni esecuzione produce un problema diverso, ed è proprio questo che rende utili i numeri casuali nei collaudi. Non sostituiscono però il ragionamento sui casi speciali: ad esempio `after sort` potrebbe stampare `true` se l'array generato fosse già ordinato. È molto improbabile (meno di 1 su 3 milioni: circa $1/10! \approx 1/3{,}6 \cdot 10^6$ se i valori sono distinti), ma possibile.

_(libro, pp. 120–123)_

### Una semplice crittografia che usa array di caratteri

La **crittografia** studia la **cifratura** (*encryption*), che trasforma il **testo in chiaro** (*plaintext*) in **testo cifrato** (*ciphertext*), e la **decifrazione** (*decryption*), che fa il contrario.

Il **cifrario di Cesare** sostituisce ogni lettera con quella che si trova $r$ posizioni più avanti nell'alfabeto, ricominciando dall'inizio dopo la Z (*wrap around*). Con $r = 3$: A→D, B→E, …, W→Z, X→A, Y→B, Z→C.

**Stringhe e array di caratteri.** Le `String` sono immutabili, quindi si converte la stringa in un array di caratteri, lo si modifica e si costruisce una nuova stringa:

- `S.toCharArray()`: da `"bird"` ad `{'b','i','r','d'}`;
- `new String(A)`: dall'array alla stringa `"bird"`.

**Array come codice di sostituzione.** Si numerano le lettere A=0, …, Z=25 e si memorizza la regola in un array `encoder`, dove `encoder[k]` è la lettera che sostituisce la $k$-esima. L'indice si ottiene sottraendo caratteri: in Java `c - 'A'` è la distanza tra i codici Unicode, quindi `'A' - 'A' = 0`, `'B' - 'A' = 1`, ecc.

![[ASD-p124-1.png]]

La figura mostra l'array di codifica per $r = 3$ (`D E F … Z A B C`, indici 0–25). Per cifrare `'T'` si calcola `'T' - 'A' = 84 - 65 = 19` (codici Unicode) e si legge `encoder[19] = 'W'`.

Per la cifratura con rotazione $r$ la lettera di indice $k$ diventa quella di indice $(k + r) \bmod 26$; per la decifrazione quella di indice $(k - r + 26) \bmod 26$ (il `+ 26` evita di applicare `%` a numeri negativi).

```java
/** Cifratura e decifrazione con il cifrario di Cesare. */
public class CaesarCipher {
  protected char[] encoder = new char[26];   // array per cifrare
  protected char[] decoder = new char[26];   // array per decifrare
  /** Costruttore che inizializza i due array */
  public CaesarCipher(int rotation) {
    for (int k = 0; k < 26; k++) {
      encoder[k] = (char) ('A' + (k + rotation) % 26);
      decoder[k] = (char) ('A' + (k - rotation + 26) % 26);
    }
  }
  /** Restituisce il messaggio cifrato. */
  public String encrypt(String message) {
    return transform(message, encoder);
  }
  /** Restituisce il messaggio decifrato. */
  public String decrypt(String secret) {
    return transform(secret, decoder);
  }
  /** Trasforma la stringa secondo il codice dato. */
  private String transform(String original, char[] code) {
    char[] msg = original.toCharArray();
    for (int k = 0; k < msg.length; k++)
      if (Character.isUpperCase(msg[k])) {   // una lettera da sostituire
        int j = msg[k] - 'A';                // valore da 0 a 25
        msg[k] = code[j];                    // sostituzione
      }
    return new String(msg);
  }
  /** Semplice main di collaudo */
  public static void main(String[] args) {
    CaesarCipher cipher = new CaesarCipher(3);
    System.out.println("Encryption code = " + new String(cipher.encoder));
    System.out.println("Decryption code = " + new String(cipher.decoder));
    String message = "THE EAGLE IS IN PLAY; MEET AT JOE'S.";
    String coded = cipher.encrypt(message);
    System.out.println("Secret: " + coded);
    String answer = cipher.decrypt(coded);
    System.out.println("Message: " + answer);   // di nuovo il testo in chiaro
  }
}
```

```
Encryption code = DEFGHIJKLMNOPQRSTUVWXYZABC
Decryption code = XYZABCDEFGHIJKLMNOPQRSTUVW
Secret: WKH HDJOH LV LQ SODB; PHHW DW MRH'V.
Message: THE EAGLE IS IN PLAY; MEET AT JOE'S.
```

Cifratura e decifrazione sono lo **stesso algoritmo** con array diversi, quindi sono implementate dall'unico metodo privato `transform`. Solo le maiuscole vengono trasformate; spazi e punteggiatura restano invariati.

_(libro, pp. 123–126)_

### Array bidimensionali e giochi posizionali

I **giochi posizionali** (strategia, simulazione, …) devono rappresentare oggetti in uno spazio a due dimensioni: lo strumento naturale è un **array bidimensionale** (o **matrice**), con un indice di **riga** e uno di **colonna**.

In Java gli array sono monodimensionali: un array bidimensionale è un **array di array**, cioè un array le cui celle contengono riferimenti ad altri array.

```java
int[][] data = new int[8][10];   // 8 righe, 10 colonne
data[i][i+1] = data[i][i] + 3;
j = data.length;                 // 8 (numero di righe)
k = data[4].length;              // 10 (lunghezza della riga 4)
```

![[ASD-p127-1.png]]

La matrice `data` ha 8 righe (0–7) e 10 colonne (0–9). Il primo indice sceglie la riga, il secondo la colonna: `data[3][5]` è 100, `data[6][2]` è 632.

#### Il gioco Tic-Tac-Toe

Il **tris** (Tic-Tac-Toe) si gioca su una scacchiera 3×3: i giocatori X e O piazzano a turno una pedina, iniziando da X, e vince chi allinea tre pedine su una riga, una colonna o una diagonale. È un gioco banale (O, giocando bene, pareggia sempre), ma mostra bene l'uso delle matrici, lo stesso che si fa per dama, scacchi e simulazioni.

La scacchiera è un `int[3][3]` con la codifica: **0** = libera, **1** = X, **−1** = O. Così un giocatore vince se la **somma** di una riga, colonna o diagonale vale **3** (X) o **−3** (O).

![[ASD-p128-1.png]]

La figura affianca una configurazione della scacchiera e l'array `board` che la rappresenta, con 1 al posto delle X, −1 al posto delle O e 0 nelle caselle libere.

```java
/** Simula una partita a Tic-Tac-Toe (non è in grado di giocare). */
public class TicTacToe {
  public static final int X = 1, O = -1;      // giocatori
  public static final int EMPTY = 0;          // casella libera
  private int board[][] = new int[3][3];      // scacchiera
  private int player;                         // giocatore di turno
  /** Costruttore */
  public TicTacToe() { clearBoard(); }
  /** Svuota la scacchiera */
  public void clearBoard() {
    for (int i = 0; i < 3; i++)
      for (int j = 0; j < 3; j++)
        board[i][j] = EMPTY;
    player = X;                               // il primo giocatore è X
  }
  /** Mette una X o una O nella posizione i,j. */
  public void putMark(int i, int j) throws IllegalArgumentException {
    if ((i < 0) || (i > 2) || (j < 0) || (j > 2))
      throw new IllegalArgumentException("Invalid board position");
    if (board[i][j] != EMPTY)
      throw new IllegalArgumentException("Board position occupied");
    board[i][j] = player;                     // simbolo del giocatore di turno
    player = -player;                         // cambio turno (O == -X)
  }
  /** Verifica se il giocatore indicato vince con la configurazione attuale. */
  public boolean isWin(int mark) {
    return ((board[0][0] + board[0][1] + board[0][2] == mark*3)     // riga 0
         || (board[1][0] + board[1][1] + board[1][2] == mark*3)     // riga 1
         || (board[2][0] + board[2][1] + board[2][2] == mark*3)     // riga 2
         || (board[0][0] + board[1][0] + board[2][0] == mark*3)     // colonna 0
         || (board[0][1] + board[1][1] + board[2][1] == mark*3)     // colonna 1
         || (board[0][2] + board[1][2] + board[2][2] == mark*3)     // colonna 2
         || (board[0][0] + board[1][1] + board[2][2] == mark*3)     // diagonale
         || (board[2][0] + board[1][1] + board[0][2] == mark*3));   // altra diagonale
  }
  /** Restituisce il vincitore, oppure 0 se pareggio o partita in corso. */
  public int winner() {
    if (isWin(X))
      return X;
    else if (isWin(O))
      return O;
    else
      return 0;
  }
  /** Descrizione testuale della scacchiera */
  public String toString() {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        switch (board[i][j]) {
          case X:     sb.append("X"); break;
          case O:     sb.append("O"); break;
          case EMPTY: sb.append(" "); break;
        }
        if (j < 2) sb.append("|");            // separatore di colonna
      }
      if (i < 2) sb.append("\n-----\n");      // separatore di riga
    }
    return sb.toString();
  }
  /** Gioca una partita di prova */
  public static void main(String[] args) {
    TicTacToe game = new TicTacToe();
    /* mosse di X: */       /* mosse di O: */
    game.putMark(1,1);      game.putMark(0,2);
    game.putMark(2,2);      game.putMark(0,0);
    game.putMark(0,1);      game.putMark(2,1);
    game.putMark(1,2);      game.putMark(1,0);
    game.putMark(2,0);
    System.out.println(game);
    int winningPlayer = game.winner();
    String[] outcome = {"O wins", "Tie", "X wins"};   // sfrutta -1, 0, 1
    System.out.println(outcome[1 + winningPlayer]);
  }
}
```

Output (Figura 3.9):

```
O|X|O
-----
O|X|X
-----
X|O|X
Tie
```

Dettagli da notare: `player = -player` alterna i turni sfruttando la codifica ±1; `outcome[1 + winningPlayer]` trasforma −1, 0, 1 negli indici 0, 1, 2. La classe registra solo le mosse: farla giocare con una strategia è un progetto a parte (esercizio P-8.67).

_(libro, pp. 126–130)_

---

## Liste semplicemente concatenate

Vedi [[Lista semplicemente concatenata]].

Gli array hanno due svantaggi: la **capacità è fissata** alla creazione, e **inserire o rimuovere in mezzo** costa molto, perché bisogna far scorrere gli elementi successivi. La **lista concatenata** (*linked list*) è l'alternativa: una sequenza lineare di **nodi**.

In una **lista semplicemente concatenata** (*singly linked list*) ogni nodo contiene:

- `element`: un riferimento all'elemento della sequenza;
- `next`: un riferimento al nodo successivo (`null` per l'ultimo).

![[ASD-p130-1.png]]

Un nodo: il campo `element` punta all'oggetto (il codice aeroportuale MSP), il campo `next` al nodo successivo.

La lista deve conoscere almeno il primo nodo, la **testa** (*head*): senza di essa non si raggiungerebbe nessun nodo. L'ultimo nodo è la **coda** (*tail*), riconoscibile perché ha `next == null`. Scorrere la lista seguendo i `next` dalla testa si chiama **attraversamento** (*traversing*), o *link hopping* / *pointer hopping*. Per efficienza la lista memorizza anche un riferimento esplicito a `tail` (per non dover attraversare tutto) e il numero di nodi, `size`.

![[ASD-p131-1.png]]

Lista di codici aeroportuali LAX → MSP → ATL → BOS: `head` punta al nodo di LAX, `tail` a quello di BOS, il cui `next` è $\varnothing$ (`null`).

Una proprietà fondamentale: la lista **non ha una dimensione prefissata** e usa spazio proporzionale al numero di elementi.

> [!tip] Collegamento
> In C la stessa struttura si realizza con le struct e i puntatori; vedi [[Lista Generica in C]] (Sistemi Operativi).

### Inserire un elemento all'inizio di una lista semplicemente concatenata

![[ASD-p131-2.png]]

(a) lista iniziale MSP → ATL → BOS; (b) si crea il nuovo nodo LAX (`newest`) e il suo `next` punta alla vecchia testa; (c) `head` viene spostato sul nuovo nodo.

```
Algorithm addFirst(e):
  newest = Node(e)        { nuovo nodo che contiene e }
  newest.next = head      { il nuovo nodo punta alla vecchia testa }
  head = newest           { la testa diventa il nuovo nodo }
  size = size + 1
```

L'ordine conta: `newest.next` va impostato **prima** di cambiare `head`, altrimenti si perde il riferimento alla vecchia testa. Se la lista era vuota (`head == null`), il nuovo nodo avrà `next = null`, come deve.

### Inserire un elemento alla fine di una lista semplicemente concatenata

![[ASD-p132-1.png]]

(a) lista MSP → ATL → BOS con `tail` su BOS; (b) si crea il nodo MIA con `next = null`; (c) il `next` di BOS punta a MIA e `tail` si sposta su MIA.

```
Algorithm addLast(e):
  newest = Node(e)        { nuovo nodo che contiene e }
  newest.next = null      { sarà l'ultimo }
  tail.next = newest      { il vecchio ultimo punta al nuovo }
  tail = newest           { tail diventa il nuovo nodo }
  size = size + 1
```

Anche qui l'ordine conta: si aggiorna `tail.next` **prima** di spostare `tail`. Lo pseudocodice non gestisce la lista vuota (in cui `tail` non esiste): il codice Java lo fa con un caso speciale.

### Eliminare un elemento da una lista semplicemente concatenata

![[ASD-p133-1.png]]

(a) lista LAX → MSP → ATL → BOS; (b) `head` passa al nodo successivo, MSP, e il nodo di LAX resta scollegato; (c) situazione finale (il vecchio nodo sarà eliminato dal garbage collector).

```
Algorithm removeFirst():
  if head == null then
    la lista è vuota
  head = head.next        { la testa diventa il nodo successivo (o null) }
  size = size − 1
```

> [!warning] Rimuovere l'ultimo nodo è costoso
> Anche conoscendo `tail`, per rimuovere l'ultimo nodo bisogna aggiornare il `next` del **penultimo**, e l'unico modo per raggiungerlo è attraversare la lista dalla testa. Per renderlo efficiente serve una [[#Liste doppiamente concatenate|lista doppiamente concatenata]].

_(libro, pp. 130–134)_

### Realizzare una lista semplicemente concatenata

La classe `SinglyLinkedList<E>` è **generica** (il tipo `E` degli elementi lo sceglie chi la usa) e offre:

| Metodo | Effetto |
|---|---|
| `size()` | numero di elementi |
| `isEmpty()` | `true` se la lista è vuota |
| `first()` | primo elemento (senza rimuoverlo), `null` se vuota |
| `last()` | ultimo elemento (senza rimuoverlo), `null` se vuota |
| `addFirst(e)` | aggiunge `e` all'inizio |
| `addLast(e)` | aggiunge `e` alla fine |
| `removeFirst()` | rimuove e restituisce il primo elemento, `null` se vuota |

Il nodo è una **classe annidata statica e privata**: gli utenti della lista non vedono nodi e collegamenti (incapsulamento), e il compilatore la distingue dai nodi di altre strutture.

```java
public class SinglyLinkedList<E> {
  //---------------- classe annidata Node ----------------
  private static class Node<E> {
    private E element;        // elemento memorizzato in questo nodo
    private Node<E> next;     // nodo successivo nella lista
    public Node(E e, Node<E> n) {
      element = e;
      next = n;
    }
    public E getElement() { return element; }
    public Node<E> getNext() { return next; }
    public void setNext(Node<E> n) { next = n; }
  } //------------- fine della classe annidata Node -------------

  // variabili di esemplare di SinglyLinkedList
  private Node<E> head = null;   // primo nodo (null se la lista è vuota)
  private Node<E> tail = null;   // ultimo nodo (null se la lista è vuota)
  private int size = 0;          // numero di nodi
  public SinglyLinkedList() { }  // lista inizialmente vuota

  // metodi di accesso
  public int size() { return size; }
  public boolean isEmpty() { return size == 0; }
  public E first() {             // primo elemento, senza rimuoverlo
    if (isEmpty()) return null;
    return head.getElement();
  }
  public E last() {              // ultimo elemento, senza rimuoverlo
    if (isEmpty()) return null;
    return tail.getElement();
  }

  // metodi di aggiornamento
  public void addFirst(E e) {    // aggiunge e all'inizio
    head = new Node<>(e, head);  // crea il nodo e lo collega
    if (size == 0)
      tail = head;               // caso speciale: il nuovo nodo è anche tail
    size++;
  }
  public void addLast(E e) {     // aggiunge e alla fine
    Node<E> newest = new Node<>(e, null);   // diventerà l'ultimo nodo
    if (isEmpty())
      head = newest;             // caso speciale: lista vuota
    else
      tail.setNext(newest);      // il nuovo nodo segue tail
    tail = newest;
    size++;
  }
  public E removeFirst() {       // rimuove e restituisce il primo elemento
    if (isEmpty()) return null;  // niente da rimuovere
    E answer = head.getElement();
    head = head.getNext();       // diventa null se c'era un solo nodo
    size--;
    if (size == 0)
      tail = null;               // caso speciale: lista ora vuota
    return answer;
  }
}
```

I casi speciali riguardano sempre la **lista vuota** o con **un solo nodo**, dove `head` e `tail` coincidono.

_(libro, pp. 134–135)_

---

## Liste concatenate circolari

Vedi [[Lista concatenata circolare]].

Molte applicazioni hanno dati con disposizione **ciclica**, senza un vero inizio o una vera fine: i turni di un gioco a più giocatori (A, B, C, poi di nuovo A…), una linea della metropolitana circolare, e soprattutto lo scheduling dei processi.

### Pianificazione circolare (round robin)

Il sistema operativo condivide la CPU tra molti processi con la **pianificazione circolare** (*round-robin scheduling*): ogni processo riceve una breve **porzione di tempo** (*time slice*), poi viene interrotto anche se non ha finito e la CPU passa al successivo, ciclicamente. I nuovi processi entrano nella coda e quelli che terminano ne escono.

![[ASD-p136-1.png]]

Le tre fasi ripetute: (1) si toglie il prossimo processo dalla coda di attesa; (2) gli si assegna una porzione di tempo di CPU; (3) lo si rimette in fondo alla coda.

Con una lista normale `L` si farebbe:

1. `p = L.removeFirst()`
2. assegna una porzione di tempo a `p`
3. `L.addLast(p)`

Ma è inefficiente: si elimina un nodo per ricrearne subito un altro con lo stesso elemento, aggiornando ogni volta `size` e i collegamenti.

> [!tip] Collegamento
> L'algoritmo di scheduling è trattato in [[Round Robin]] (Sistemi Operativi).

### Progettare e realizzare una lista concatenata circolare

Una **lista concatenata circolare** (*circularly linked list*) è una lista semplicemente concatenata in cui il `next` dell'ultimo nodo punta **di nuovo al primo** invece che a `null`.

![[ASD-p137-1.png]]

LAX → MSP → ATL → BOS, e il `next` di BOS (`tail`) torna a LAX (`head`).

La classe `CircularlyLinkedList` ha tutti i metodi di `SinglyLinkedList` più:

- `rotate()`: sposta il primo elemento in fondo alla lista.

Il round robin diventa: (1) assegna una porzione di tempo a `C.first()`; (2) `C.rotate()`. Niente nodi creati o distrutti.

**Ulteriore ottimizzazione**: non serve memorizzare `head`, perché la testa è sempre `tail.getNext()`. Basta `tail`, e il codice risulta più semplice ed efficiente anche quando `rotate` non serve.

### Operazioni su una lista concatenata circolare

**Rotazione**: non si spostano nodi né elementi, basta far avanzare `tail` di un passo.

![[ASD-p138-1.png]]

(a) prima: la sequenza è {LAX, MSP, ATL, BOS}, `tail` su BOS e la testa implicita (`(head)`, cioè `tail.getNext()`) su LAX; (b) dopo `rotate()`, `tail` è su LAX e la testa implicita su MSP: la sequenza è {MSP, ATL, BOS, LAX}.

**`addFirst`**: si crea un nodo e lo si inserisce subito dopo `tail` (cioè prima della testa). **`addLast`**: si chiama `addFirst` e poi si avanza `tail` sul nuovo nodo.

![[ASD-p138-2.png]]

Effetto di `addFirst(STL)` sulla lista (b) della figura precedente: il nuovo nodo STL (`newest`, variabile locale) viene inserito tra `tail` (LAX) e la vecchia testa MSP; il `next` di LAX ora punta a STL (la freccia tratteggiata è il vecchio collegamento verso MSP). STL è il nuovo primo elemento, raggiungibile come `tail.getNext()`.

**`removeFirst`**: il `next` di `tail` scavalca il primo nodo.

```java
public class CircularlyLinkedList<E> {
  // (classe annidata Node identica a quella di SinglyLinkedList)

  // variabili di esemplare
  private Node<E> tail = null;   // ultimo nodo (head non serve)
  private int size = 0;
  public CircularlyLinkedList() { }

  // metodi di accesso
  public int size() { return size; }
  public boolean isEmpty() { return size == 0; }
  public E first() {
    if (isEmpty()) return null;
    return tail.getNext().getElement();   // la testa è il SUCCESSIVO di tail
  }
  public E last() {
    if (isEmpty()) return null;
    return tail.getElement();
  }

  // metodi di aggiornamento
  public void rotate() {                  // il primo elemento va in fondo
    if (tail != null)                     // se vuota non fa nulla
      tail = tail.getNext();              // la vecchia testa diventa tail
  }
  public void addFirst(E e) {             // aggiunge e all'inizio
    if (size == 0) {
      tail = new Node<>(e, null);
      tail.setNext(tail);                 // punta circolarmente a se stesso
    } else {
      Node<E> newest = new Node<>(e, tail.getNext());
      tail.setNext(newest);
    }
    size++;
  }
  public void addLast(E e) {              // aggiunge e alla fine
    addFirst(e);                          // lo inserisce all'inizio
    tail = tail.getNext();                // e lo rende l'ultimo
  }
  public E removeFirst() {                // rimuove e restituisce il primo
    if (isEmpty()) return null;
    Node<E> head = tail.getNext();
    if (head == tail) tail = null;        // era l'unico nodo
    else tail.setNext(head.getNext());    // scavalca la vecchia testa
    size--;
    return head.getElement();
  }
}
```

Con un solo nodo, `tail.getNext()` è `tail` stesso: per questo `addFirst` su lista vuota crea un nodo che punta a sé e `removeFirst` controlla `head == tail`.

_(libro, pp. 136–139)_

---

## Liste doppiamente concatenate

Vedi [[Lista doppiamente concatenata]].

La lista semplice è **asimmetrica**: inserisce bene a entrambe le estremità e rimuove bene la testa, ma non rimuove bene la coda e, più in generale, non può rimuovere un nodo interno conoscendo solo il nodo stesso, perché non sa raggiungere il suo **predecessore** (il cui `next` va aggiornato).

La **lista doppiamente concatenata** (*doubly linked list*) dà a ogni nodo due riferimenti: **`next`** (successivo) e **`prev`** (precedente). Così diventano $O(1)$ anche gli inserimenti e le rimozioni in qualunque posizione.

### Sentinelle iniziale e finale

Per evitare i casi speciali alle estremità si aggiungono due nodi fittizi, le **sentinelle**, che non contengono elementi:

- **`header`** all'inizio;
- **`trailer`** alla fine.

![[ASD-p140-1.png]]

Lista che rappresenta {JFK, PVD, SFO}: tra `header` e `trailer` ogni nodo ha una freccia `next` verso destra e una `prev` verso sinistra.

In una lista vuota `header.next == trailer` e `trailer.prev == header`. In una lista non vuota `header.next` è il primo nodo vero e `trailer.prev` l'ultimo.

#### Vantaggio derivante dall'uso delle sentinelle

Con un po' di memoria in più la logica si semplifica molto:

- le sentinelle **non cambiano mai**: cambiano solo i nodi in mezzo;
- **ogni inserimento** avviene tra due nodi esistenti (al limite una sentinella);
- **ogni nodo da rimuovere** ha sempre un nodo a sinistra e uno a destra.

Per confronto, `SinglyLinkedList.addLast` ha bisogno di un `if` per la lista vuota (dove non esiste un ultimo nodo dopo cui inserire); con una sentinella iniziale quel caso sparirebbe.

### Inserimento e rimozione in una lista doppiamente concatenata

![[ASD-p141-1.png]]

Inserimento di PVD tra JFK e SFO: (a) prima; (b) si crea il nuovo nodo con `prev = JFK` e `next = SFO`; (c) si aggiornano `JFK.next` e `SFO.prev` perché puntino al nuovo nodo.

![[ASD-p142-1.png]]

Inserimento all'inizio: il nuovo nodo (PVD) va semplicemente tra `header` e il nodo che seguiva `header` (BWI). È lo stesso caso generale "inserisci tra due nodi".

![[ASD-p142-2.png]]

Rimozione di PVD: (a) prima; (b) i suoi vicini vengono collegati direttamente tra loro (`predecessore.next = successore`, `successore.prev = predecessore`), scavalcandolo; (c) il nodo non è più raggiungibile e la sua memoria viene recuperata dal **garbage collector** di Java. Grazie alle sentinelle lo stesso codice rimuove anche il primo e l'ultimo elemento.

### Realizzare una lista doppiamente concatenata

`DoublyLinkedList<E>` offre gli stessi metodi della lista semplice più **`removeLast()`**. Per non rompere l'incapsulamento i nodi restano privati, quindi non si possono ancora fare inserimenti/rimozioni interni dall'esterno: lo permetterà la lista posizionale del [[07 - ASD - Liste e iteratori#Liste posizionali|cap. 7]].

Internamente si usano due metodi privati che gestiscono il caso generale, `addBetween` e `remove`; i metodi pubblici diventano quasi banali.

```java
/** Un'implementazione di base di lista doppiamente concatenata. */
public class DoublyLinkedList<E> {
  //---------------- classe annidata Node ----------------
  private static class Node<E> {
    private E element;      // elemento memorizzato
    private Node<E> prev;   // nodo precedente
    private Node<E> next;   // nodo successivo
    public Node(E e, Node<E> p, Node<E> n) {
      element = e;
      prev = p;
      next = n;
    }
    public E getElement() { return element; }
    public Node<E> getPrev() { return prev; }
    public Node<E> getNext() { return next; }
    public void setPrev(Node<E> p) { prev = p; }
    public void setNext(Node<E> n) { next = n; }
  } //------------- fine della classe annidata Node -------------

  private Node<E> header;    // sentinella iniziale
  private Node<E> trailer;   // sentinella finale
  private int size = 0;
  /** Costruisce una nuova lista vuota. */
  public DoublyLinkedList() {
    header = new Node<>(null, null, null);      // crea header
    trailer = new Node<>(null, header, null);   // trailer preceduto da header
    header.setNext(trailer);                    // header seguito da trailer
  }
  public int size() { return size; }
  public boolean isEmpty() { return size == 0; }
  public E first() {
    if (isEmpty()) return null;
    return header.getNext().getElement();       // il primo segue header
  }
  public E last() {
    if (isEmpty()) return null;
    return trailer.getPrev().getElement();      // l'ultimo precede trailer
  }

  // metodi di aggiornamento pubblici
  public void addFirst(E e) {
    addBetween(e, header, header.getNext());    // subito dopo header
  }
  public void addLast(E e) {
    addBetween(e, trailer.getPrev(), trailer);  // subito prima di trailer
  }
  public E removeFirst() {
    if (isEmpty()) return null;
    return remove(header.getNext());
  }
  public E removeLast() {
    if (isEmpty()) return null;
    return remove(trailer.getPrev());
  }

  // metodi di aggiornamento privati
  /** Aggiunge e alla lista tra i due nodi dati. */
  private void addBetween(E e, Node<E> predecessor, Node<E> successor) {
    Node<E> newest = new Node<>(e, predecessor, successor);
    predecessor.setNext(newest);
    successor.setPrev(newest);
    size++;
  }
  /** Rimuove il nodo dato e ne restituisce l'elemento. */
  private E remove(Node<E> node) {
    Node<E> predecessor = node.getPrev();
    Node<E> successor = node.getNext();
    predecessor.setNext(successor);
    successor.setPrev(predecessor);
    size--;
    return node.getElement();
  }
}
```

| Operazione | Lista semplice | Lista circolare | Lista doppia (con sentinelle) |
|---|---|---|---|
| `addFirst`, `addLast` | $O(1)$ | $O(1)$ | $O(1)$ |
| `removeFirst` | $O(1)$ | $O(1)$ | $O(1)$ |
| `removeLast` | $O(n)$ (serve il penultimo) | $O(n)$ | $O(1)$ |
| `rotate` | — | $O(1)$ | — |
| Riferimenti per nodo | 1 (`next`) | 1 (`next`) | 2 (`next`, `prev`) |

_(libro, pp. 140–145)_

---

## Verifica di equivalenza

Vedi [[Metodo equals]].

Con i riferimenti "uguale" può voler dire due cose:

- `a == b`: **identità**, cioè `a` e `b` puntano allo **stesso oggetto** (o sono entrambi `null`);
- `a.equals(b)`: **equivalenza**, una nozione di più alto livello (es. due `String` distinte con la stessa sequenza di caratteri).

Salvo che serva proprio l'identità, si usa `equals`. La versione definita in `Object` si limita a restituire `a == b`: ogni classe deve **ridefinirla** se ha una nozione di equivalenza più significativa (come fa `String`, che confronta carattere per carattere).

Chi ridefinisce `equals` deve rispettare le proprietà di una **relazione di equivalenza**, su cui si basa la coerenza della libreria Java:

| Proprietà | Regola (per riferimenti non nulli) |
|---|---|
| Gestione di `null` | `x.equals(null)` è `false` |
| Riflessività | `x.equals(x)` è `true` |
| Simmetria | `x.equals(y)` e `y.equals(x)` danno lo stesso risultato |
| Transitività | se `x.equals(y)` e `y.equals(z)` allora `x.equals(z)` |

Con ereditarietà e generics rispettarle non è banale; il libro implementa `equals` solo per array e liste concatenate.

_(libro, pp. 145–146)_

### Verifica di equivalenza tra array

Gli array sono tipi riferimento ma non esemplari di una classe; per confrontarli:

| Espressione | Significato |
|---|---|
| `a == b` | stesso array |
| `a.equals(b)` | **uguale ad `a == b`**: gli array non ridefiniscono `Object.equals` |
| `Arrays.equals(a, b)` | stessa lunghezza ed elementi corrispondenti uguali (`==` per i primitivi, `a[k].equals(b[k])` per i riferimenti) |
| `Arrays.deepEquals(a, b)` | come sopra, ma se gli elementi sono array li confronta ricorsivamente con `deepEquals` |

Per gli **array multidimensionali** `Arrays.equals` non basta: le righe `a[0]` e `b[0]` sono array distinti in memoria anche se hanno lo stesso contenuto, quindi `a[k].equals(b[k])` (cioè `==`) dà `false`. Serve `Arrays.deepEquals`. Il problema generale è quello degli **oggetti composti**: bisogna decidere dove un oggetto "finisce".

### Verifica di equivalenza tra liste concatenate

Due `SinglyLinkedList` sono equivalenti se hanno la stessa lunghezza e gli elementi corrispondenti sono uguali secondo `equals`: si scorrono le due liste in parallelo.

```java
public boolean equals(Object o) {
  if (o == null) return false;
  if (getClass() != o.getClass()) return false;
  SinglyLinkedList other = (SinglyLinkedList) o;   // tipo non parametrico
  if (size != other.size) return false;
  Node walkA = head;                               // scorre la prima lista
  Node walkB = other.head;                         // scorre la seconda lista
  while (walkA != null) {
    if (!walkA.getElement().equals(walkB.getElement())) return false;  // differenza
    walkA = walkA.getNext();
    walkB = walkB.getNext();
  }
  return true;                                     // tutti i confronti riusciti
}
```

- Il parametro è `Object`, perché il metodo deve **ridefinire** `Object.equals(Object)`.
- Approccio prudente: due oggetti sono equivalenti solo se sono della **stessa classe** (`getClass()`), quindi una lista semplice e una doppia con gli stessi elementi non sono "uguali".
- Si usano i tipi **non parametrici** `SinglyLinkedList` e `Node`: per l'**erasure** di Java a runtime non si può sapere con quale `E` è stata creata l'altra lista. Se gli elementi sono di tipi incompatibili, lo dirà il loro `equals`.

_(libro, pp. 146–148)_

---

## Clonare strutture dati

Vedi [[Copia superficiale e copia profonda]].

Ci si aspetta che la **copia** di un oggetto abbia uno stato proprio, indipendente dall'originale. Ma se l'oggetto ha campi riferimento, la copia deve puntare agli **stessi** oggetti o a **copie** di essi? Per una rubrica (`AddressBook`): aggiungendo un contatto a una copia, deve comparire anche nell'altra? Cambiando un numero di telefono? Non c'è una risposta universale: ogni classe decide se e come può essere copiata.

- **Copia superficiale** (*shallow copy*): ogni campo della copia riceve lo stesso valore del campo originale (`duplicate.field = original.field`); per i campi riferimento significa **condividere** gli oggetti.
- **Copia profonda** (*deep copy*): anche (alcuni de)gli oggetti puntati vengono clonati.

`Object` ha un metodo `clone()` che fa una copia superficiale, ma è `protected` e lancia `CloneNotSupportedException`. Per rendere clonabile una classe bisogna:

1. dichiarare che implementa l'interfaccia **`Cloneable`** (così il `clone` ereditato non lancia l'eccezione);
2. definire un metodo **`clone()` pubblico**, che può limitarsi a chiamare `super.clone()` (copia superficiale) oppure clonare anche gli oggetti interni (copia profonda).

_(libro, pp. 148–149)_

### Clonare array

```java
int[] data = {2, 3, 5, 7, 11, 13, 17, 19};
int[] backup;
backup = data;   // attenzione: NON è una copia
```

![[ASD-p149-1.png]]

`backup = data` non crea un nuovo array: crea un **alias**, un secondo riferimento allo stesso array.

```java
backup = data.clone();
```

![[ASD-p150-1.png]]

`clone()` crea un **nuovo** array con gli stessi valori: dopo `data[4] = 23`, `backup` non cambia.

Se però l'array contiene **riferimenti**, `clone()` fa una copia superficiale:

![[ASD-p150-2.png]]

`guests = contacts.clone()` crea un nuovo array di 8 celle, ma ogni cella punta allo **stesso** oggetto `Person` della cella corrispondente di `contacts`: modificando una persona tramite `guests` la modifica si vede anche da `contacts`.

Per una copia profonda si clonano anche i singoli elementi (solo se `Person` è `Cloneable`):

```java
Person[] guests = new Person[contacts.length];
for (int k = 0; k < contacts.length; k++)
  guests[k] = (Person) contacts[k].clone();   // clone() restituisce Object
```

Per un **array bidimensionale** `clone()` copia solo l'array esterno (le righe restano condivise). `java.util.Arrays` non ha un `deepClone`, ma si scrive facilmente clonando ogni riga:

```java
public static int[][] deepClone(int[][] original) {
  int[][] backup = new int[original.length][];   // array di righe
  for (int k = 0; k < original.length; k++)
    backup[k] = original[k].clone();             // copia la riga k
  return backup;
}
```

_(libro, pp. 149–151)_

### Clonare liste concatenate

Si rende clonabile `SinglyLinkedList`:

```java
public class SinglyLinkedList<E> implements Cloneable {
```

e si scrive `clone()`. Per convenzione si parte da `super.clone()` (copia superficiale, poi un cast a `SinglyLinkedList<E>`). A quel punto la copia ha gli stessi valori dei campi: `size` va bene, ma `head` (e `tail`) punterebbero ai **nodi dell'originale**, quindi le due liste condividerebbero la catena. Serve una catena di **nodi nuovi**, che però puntano agli **stessi elementi** (gli elementi non vengono clonati).

```java
public SinglyLinkedList<E> clone() throws CloneNotSupportedException {
  // si parte sempre dal metodo ereditato
  SinglyLinkedList<E> other = (SinglyLinkedList<E>) super.clone();   // cast sicuro
  if (size > 0) {                       // serve una catena di nodi indipendente
    other.head = new Node<>(head.getElement(), null);
    Node<E> walk = head.getNext();      // scorre la lista originale
    Node<E> otherTail = other.head;     // ultimo nodo creato
    while (walk != null) {              // un nuovo nodo per ogni elemento
      Node<E> newest = new Node<>(walk.getElement(), null);
      otherTail.setNext(newest);        // collega il nodo precedente a questo
      otherTail = newest;
      walk = walk.getNext();
    }
  }
  return other;
}
```

> [!warning] Correzione
> Il libro dice che la classe ha "due campi, `size` e `head`", ma `SinglyLinkedList` ne ha **tre**: c'è anche `tail`. Il codice non aggiorna `other.tail`, che resta quindi un riferimento all'ultimo nodo **dell'originale**: un successivo `other.addLast(x)` attaccherebbe il nuovo nodo alla lista originale invece che alla copia. Va aggiunta, dopo il ciclo `while` (dentro l'`if`), la riga
> ```java
> other.tail = otherTail;   // la coda della copia è l'ultimo nodo creato
> ```

_(libro, pp. 151–152)_

---

> [!summary] Riepilogo
> - **Array**: accesso per indice in tempo costante, ma capacità fissa e inserimenti/rimozioni interni che richiedono di far scorrere gli elementi (`Scoreboard.add/remove`).
> - **Insertion sort**: inserisce ogni elemento tra i precedenti già ordinati; veloce su array quasi ordinati, lento su array al contrario.
> - `java.util.Arrays` (`equals`, `fill`, `copyOf`, `sort`, `binarySearch`, …) e `java.util.Random` (pseudocasuale, seme).
> - **Cifrario di Cesare** con array di sostituzione e aritmetica modulo 26; **matrici** come array di array (tris con codifica ±1).
> - **Lista semplice**: `head`, `tail`, `size`; inserimenti alle due estremità e `removeFirst` in $O(1)$, `removeLast` no.
> - **Lista circolare**: basta `tail` (la testa è `tail.next`); `rotate()` in $O(1)$, ideale per il round robin.
> - **Lista doppia** con sentinelle `header`/`trailer`: ogni inserimento è "tra due nodi", ogni rimozione "scavalca un nodo"; tutto $O(1)$.
> - `==` (identità) vs `equals` (equivalenza: riflessiva, simmetrica, transitiva, `false` con `null`); `Arrays.equals` vs `deepEquals`.
> - **Copia superficiale** vs **profonda**; `Cloneable` + `clone()` pubblico; per le liste serve una nuova catena di nodi (e il `tail` aggiornato).
