---
title: Elaborazione di testi
aliases:
  - ASD — Elaborazione di testi
tags:
  - algoritmi-e-strutture-dati
  - stringhe
  - pattern-matching
  - trie
  - huffman
  - greedy
  - programmazione-dinamica
source: Goodrich, Tamassia - Strutture dati e algoritmi in Java (Zanichelli, 2015), cap. 13
---

# Elaborazione di testi

> [!abstract]
> Il testo resta uno dei dati più elaborati dai calcolatori. Questo capitolo usa i problemi sulle stringhe per presentare **quattro schemi di progettazione di algoritmi**:
> - **forza bruta** e algoritmi più furbi per il **pattern matching** (Boyer-Moore, Knuth-Morris-Pratt), che pre-elaborano il *pattern*;
> - i **trie**, alberi che pre-elaborano il *testo* per rendere veloci molte ricerche (motori di ricerca);
> - il **metodo greedy**, con la **codifica di Huffman** per la compressione;
> - la **programmazione dinamica**, con la moltiplicazione di matrici a catena e la **sotto-sequenza comune più lunga** (LCS).
>
> Riusa le [[09 - ASD - Code prioritarie|code prioritarie]] (Huffman), le [[10 - ASD - Mappe, tabelle hash e skip list|mappe e tabelle hash]] (Boyer-Moore, trie) e gli [[08 - ASD - Alberi|alberi]]; la programmazione dinamica è il contraltare del [[12 - ASD - Ordinamento e selezione|dividi-e-conquista]].
>
> Indice dei concetti: [[MOC - Algoritmi e Strutture Dati]]

---

## Abbondanza di testi digitalizzati

I calcolatori modificano, archiviano, visualizzano e trasmettono documenti, e le raccolte di testo crescono rapidamente: una grande raccolta supera facilmente il **petabyte** (mille terabyte). Esempi: istantanee (*snapshot*) del Web in HTML/XML, documenti locali, archivi di posta, aggiornamenti dei social network, flussi (*feed*) di microblogging. A questi si aggiungono dati che, pur non essendo linguaggio, si trattano come stringhe: ad esempio il **DNA**.

Il capitolo affronta:
- il **pattern matching**: cercare una stringa (il *pattern*) dentro un testo più lungo, prima con la forza bruta e poi con algoritmi più efficienti; poi strutture dati che organizzano il testo per ricerche rapide;
- la **compressione**, con il metodo **greedy** ("goloso"), che a volte dà soluzioni approssimate e per la compressione dà quella ottima;
- la **programmazione dinamica**, che risolve in tempo polinomiale problemi che sembrano esponenziali, applicata al confronto di stringhe simili ma non allineate (correttori ortografici, genetica).

_(libro, pp. 570–571)_

### Notazioni per stringhe di caratteri

Esempi di stringhe:

- $S$ = `"CGTAAACTGCTTTAATCAAACGC"` (DNA);
- $T$ = `"http://www.wiley.com"` (un URL).

I caratteri provengono da un **alfabeto** noto $\Sigma$ (per il DNA $\Sigma = \{A, C, G, T\}$). $\Sigma$ può essere un sottoinsieme di ASCII o Unicode; anche se fissato, la sua dimensione $|\Sigma|$ può essere grande (Unicode ha oltre un milione di caratteri), quindi entra nell'analisi asintotica.

In Java `String` è immutabile e `StringBuilder` modificabile ([[01 - ASD - Introduzione a Java|cap. 1]]); nel capitolo si usano **array di `char`** per poter scrivere `S[i]` invece di `S.charAt(i)`.

| Termine | Definizione (stringa $P$ di $n$ caratteri) |
|---|---|
| sottostringa $P[i..j]$ | $P[i]P[i+1]\cdots P[j]$, con $0 \le i \le j \le n-1$ |
| sottostringa propria | con $i > 0$ oppure $j < n - 1$ (esclude $P$ stessa) |
| stringa nulla | $P[i..j]$ con $i > j$, lunghezza 0 |
| prefisso | $P[0..j]$, con $0 \le j \le n-1$ |
| suffisso | $P[i..n-1]$, con $0 \le i \le n-1$ |

Per la stringa di DNA sopra: `"CGTAA"` è un prefisso, `"CGC"` un suffisso, `"TTAATC"` una sottostringa propria. La stringa nulla è prefisso e suffisso di ogni stringa.

_(libro, pp. 571–572)_

---

## Algoritmi di pattern matching

Vedi [[Pattern matching su stringhe]].

**Problema**: dato un testo di lunghezza $n$ e un pattern di lunghezza $m \le n$, stabilire se il pattern è una sottostringa del testo e, se sì, trovare l'indice della prima occorrenza (o tutte). È alla base di `text.contains(pattern)`, `text.indexOf(pattern)`, ed è un sotto-problema di `replace` e `split`. Le implementazioni restituiscono l'indice dell'occorrenza più a sinistra o, come `indexOf`, **-1** se non c'è.

### Forza bruta

Lo schema a **forza bruta** (*brute force*) elenca tutte le configurazioni possibili e sceglie quella giusta. Per il pattern matching: provare **tutti i possibili allineamenti** del pattern nel testo.

**Codice 13.1:**

```java
/** Restituisce l'indice minimo in cui inizia pattern nel testo (oppure -1). */
public static int findBrute(char[] text, char[] pattern) {
  int n = text.length;
  int m = pattern.length;
  for (int i=0; i <= n - m; i++) {        // prova tutti gli indici iniziali nel testo
    int k = 0;                            // k è un indice nel pattern
    while (k < m && text[i+k] == pattern[k])   // il k-esimo carattere corrisponde
      k++;
    if (k == m)                           // raggiunta la fine del pattern
      return i;                           // text[i..i+m-1] corrisponde al pattern
  }
  return -1;                              // ricerca fallita
}
```

#### Prestazioni

Correttezza immediata (ricerca esaustiva). Il ciclo esterno gira al più $n - m + 1$ volte, quello interno al più $m$: **$O(nm)$** nel caso peggiore.

> [!example] Esempio 13.1
> Testo `"abacaabaccabacabaabb"`, pattern `"abacab"`.

![[ASD-p574-1.png]]

I confronti sono numerati: al primo allineamento i primi 5 caratteri coincidono e il sesto no (6 confronti); poi il pattern avanza di una posizione alla volta; dopo 11 confronti non disegnati, l'ultimo allineamento (confronti 22–27) trova la corrispondenza. Totale **27 confronti**.

_(libro, pp. 572–574)_

### L'algoritmo di Boyer-Moore

Vedi [[Algoritmo di Boyer-Moore]].

Sembrerebbe necessario guardare ogni carattere del testo, ma **non è così**: l'algoritmo di Boyer-Moore (qui in versione semplificata) può saltarne una parte rilevante grazie a due euristiche:

- **Looking-glass** ("allo specchio"): in ogni allineamento i caratteri si confrontano **da destra a sinistra**.
- **Character-jump** ("salto di caratteri"): se `text[i] = c` non coincide con `pattern[k]`:
  - se $c$ **non compare** nel pattern, si sposta il pattern **completamente oltre** `text[i]`;
  - altrimenti lo si sposta finché **l'ultima occorrenza** di $c$ nel pattern non è allineata con `text[i]`.

Insieme permettono di saltare interi gruppi di caratteri: un errore vicino alla fine del pattern può far ripartire oltre quella posizione senza aver mai guardato i caratteri precedenti.

![[ASD-p575-1.png]]

Pattern `"sushi"`. Il primo confronto (ultimo carattere del pattern) trova `e` nel testo: `e` non è nel pattern, quindi il pattern salta interamente oltre, senza guardare i primi quattro caratteri del testo. Il secondo confronto trova `s`, che è nel pattern: lo si sposta per allineare la sua ultima `s` con quella del testo.

Se l'ultimo carattere coincide, si prosegue verso sinistra con lo stesso allineamento, finché non si trova l'intero pattern o un carattere diverso. In caso di errore con un carattere $c$ che compare nel pattern, ci sono due sotto-casi a seconda di dove sta la sua **ultima occorrenza** $j$ rispetto alla posizione $k$ dell'errore:

![[ASD-p576-1.png]]

$i$ è l'indice nel testo dell'errore, $k$ quello nel pattern, $j$ l'ultima occorrenza di `text[i]` nel pattern. (a) $j < k$: si sposta il pattern di $k - j$ posizioni per allineare le due `a`; l'indice $i$ avanza di $m - (j + 1)$. (b) $j > k$: l'ultima occorrenza è a destra (già "superata"), quindi si sposta il pattern di **una sola** posizione; $i$ avanza di $m - k$. (Sarebbe meglio cercare un'altra occorrenza più a sinistra, ma non si vuole pagare quella ricerca.)

Serve quindi una funzione:

$$\text{last}(c) = \begin{cases} \text{indice dell'occorrenza più a destra di } c \text{ nel pattern} \\ -1 \quad \text{se } c \text{ non compare nel pattern} \end{cases}$$

Con un alfabeto piccolo basta un array indicizzato dal codice del carattere ($O(1)$ per accesso, ma dimensione $|\Sigma|$ e tempo per inizializzarlo). Il libro preferisce una **tabella hash** ([[Tabella hash]]) che contiene solo i caratteri presenti: spazio $O(\min(m, |\Sigma|))$, accesso $O(1)$ atteso.

**Codice 13.2:**

```java
/** Restituisce l'indice minimo in cui inizia pattern nel testo (oppure -1). */
public static int findBoyerMoore(char[] text, char[] pattern) {
  int n = text.length;
  int m = pattern.length;
  if (m == 0) return 0;                               // ricerca banale di una stringa vuota
  Map<Character,Integer> last = new HashMap<>();      // la mappa della funzione 'last'
  for (int i=0; i < n; i++)
    last.put(text[i], -1);           // -1 come default per tutti i caratteri del testo
  for (int k=0; k < m; k++)
    last.put(pattern[k], k);         // l'occorrenza più a destra sarà l'ultima memorizzata
  // inizia con la fine del pattern allineata con l'indice m-1 del testo
  int i = m-1;                       // indice nel testo
  int k = m-1;                       // indice nel pattern
  while (i < n) {
    if (text[i] == pattern[k]) {     // trovato un carattere che corrisponde
      if (k == 0) return i;          // trovato un intero pattern che corrisponde
      i--;                           // altrimenti esamina il carattere precedente
      k--;                           // nel testo e nel pattern
    } else {
      i += m - Math.min(k, 1 + last.get(text[i]));   // decide come fare il salto
      k = m - 1;                     // riparte dalla fine del pattern
    }
  }
  return -1;                         // ricerca fallita
}
```

> [!tip] Leggere il salto `i += m - Math.min(k, 1 + last(c))`
> - se $j = \text{last}(c) < k$, il minimo è $j + 1$ e $i$ avanza di $m - (j+1)$: caso (a);
> - se $j > k$, il minimo è $k$ e $i$ avanza di $m - k$: caso (b), pattern spostato di uno;
> - se $c$ non compare, $j = -1$, il minimo è 0 e $i$ avanza di $m$: il pattern salta oltre $c$.

La correttezza deriva dal fatto che `last` indica l'**ultima** occorrenza: spostando il pattern non si salta mai una possibile corrispondenza (*match*).

![[ASD-p577-1.png]]

Esecuzione su un testo simile all'Esempio 13.1, con la tabella last: $a = 4$, $b = 5$, $c = 3$, $d = -1$. Grazie ai salti bastano **13 confronti** (contro i 27 della forza bruta); ad esempio il confronto 7 trova una `d`, che non è nel pattern, e il pattern salta oltre.

#### Prestazioni

Con una tabella tradizionale il caso peggiore è $O(nm + |\Sigma|)$: calcolare last costa $O(m + |\Sigma|)$ (la dipendenza da $|\Sigma|$ sparisce con la tabella hash), la ricerca $O(nm)$ come la forza bruta. Un caso peggiore: testo $= \underbrace{aaa\cdots a}_{n}$, pattern $= b\underbrace{aa\cdots a}_{m-1}$. A ogni allineamento le $m-1$ `a` coincidono e l'errore arriva solo sulla `b`; poiché `a` compare nel pattern a destra della posizione dell'errore (caso (b)), il pattern avanza di una sola posizione.

Ma il caso peggiore è **rarissimo** su testo in inglese: in media si fanno circa **0,24 confronti per carattere** del testo con un pattern di 5 caratteri. L'algoritmo di Boyer-Moore originale raggiunge $O(n + m + |\Sigma|)$ nel caso peggiore aggiungendo un'altra euristica di scorrimento per le corrispondenze parziali, basata sulla stessa idea di KMP.

_(libro, pp. 574–578)_

### L'algoritmo di Knuth-Morris-Pratt

Vedi [[Algoritmo di Knuth-Morris-Pratt]].

Forza bruta e Boyer-Moore **sprecano informazione**: dopo molti caratteri coincidenti e un errore, ripartono dall'allineamento successivo dimenticando cosa hanno già visto. L'algoritmo **KMP** (Knuth, Morris, Pratt) evita lo spreco e ottiene **$O(n + m)$** nel caso peggiore, che è ottimo (ogni algoritmo deve leggere almeno una volta testo e pattern). L'idea: **pre-calcolare le auto-sovrapposizioni** del pattern, così da sapere subito di quanto spostarlo dopo un errore.

![[ASD-p579-1.png]]

Pattern `"amalgamation"`. Se l'errore avviene nella posizione indicata dalla freccia (dopo aver letto `amalgama`), si può spostare il pattern fino alla seconda configurazione senza ricontrollare `ama`: il suffisso `ama` di ciò che si è letto coincide con il prefisso `ama` del pattern. Se poi anche lì c'è errore, si può ancora riusare la `a` condivisa.

#### La funzione fallimento

La **funzione fallimento** (*failure function*) $f(k)$ è la lunghezza del **più lungo prefisso del pattern che è anche suffisso** di `pattern[1..k]` (si esclude `pattern[0]` perché lo spostamento sarà almeno di una posizione). Intuitivamente: se fallisce il confronto con `pattern[k+1]`, $f(k)$ dice quanti caratteri appena letti si possono riusare.

> [!example] Esempio 13.2
> Pattern `"amalgamation"`:
>
> | $k$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
> |---|---|---|---|---|---|---|---|---|---|---|---|---|
> | $P[k]$ | a | m | a | l | g | a | m | a | t | i | o | n |
> | $f(k)$ | 0 | 0 | 1 | 0 | 0 | 1 | 2 | 3 | 0 | 0 | 0 | 0 |
>
> Ad esempio $f(7) = 3$: `pattern[1..7]` = `malgama` termina con `ama`, che è anche prefisso del pattern.

#### Implementazione

Il ciclo principale confronta `text[j]` e `pattern[k]`: se coincidono avanza in entrambi (o segnala il match); se no e $k > 0$, **resta su `text[j]`** e ripiega nel pattern a `fail[k-1]`; se l'errore è sul primo carattere, avanza nel testo.

**Codice 13.3:**

```java
/** Restituisce l'indice minimo in cui inizia pattern nel testo (oppure -1). */
public static int findKMP(char[] text, char[] pattern) {
  int n = text.length;
  int m = pattern.length;
  if (m == 0) return 0;                       // ricerca banale di una stringa vuota
  int[] fail = computeFailKMP(pattern);       // calcolata da un metodo privato
  int j = 0;                                  // indice nel testo
  int k = 0;                                  // indice nel pattern
  while (j < n) {
    if (text[j] == pattern[k]) {              // pattern[0..k] corrisponde fin qui
      if (k == m - 1) return j - m + 1;       // corrispondenza completa
      j++;                                    // altrimenti estende la corrispondenza
      k++;
    } else if (k > 0)
      k = fail[k-1];                          // riutilizza il suffisso di P[0..k-1]
    else
      j++;
  }
  return -1;                                  // ricerca fallita
}
```

#### Costruzione della funzione fallimento di KMP

Si confronta il pattern **con se stesso** con la stessa logica (un *bootstrap*): ogni volta che due caratteri coincidono si pone $f(j) = k + 1$. Poiché $j > k$, il valore $f(k-1)$ usato è sempre già calcolato.

**Codice 13.4:**

```java
private static int[] computeFailKMP(char[] pattern) {
  int m = pattern.length;
  int[] fail = new int[m];             // tutte le sovrapposizioni inizialmente zero
  int j = 1;
  int k = 0;
  while (j < m) {                      // calcola fail[j], se non è zero
    if (pattern[j] == pattern[k]) {    // finora k+1 caratteri corrispondono
      fail[j] = k + 1;
      j++;
      k++;
    } else if (k > 0)                  // k segue un prefisso che corrisponde
      k = fail[k - 1];
    else                               // nessuna corrispondenza
      j++;
  }
  return fail;
}
```

#### Prestazioni

Si analizza il ciclo con $s = j - k$, lo **spostamento** totale del pattern rispetto all'inizio ($s \le n$). A ogni iterazione:

- `text[j] == pattern[k]`: $j$ e $k$ aumentano di 1, $s$ invariato;
- `text[j] != pattern[k]` e $k > 0$: $j$ non cambia, $k$ diventa $f(k-1) < k$, quindi $s$ aumenta di $k - f(k-1) \ge 1$;
- `text[j] != pattern[k]` e $k = 0$: $j$ aumenta di 1 e $k$ non cambia, quindi anche $s$ **aumenta** di 1.

> [!warning] Correzione
> Per il terzo caso il libro scrive che "$j$ aumenta di un'unità e $s$ **diminuisce** di un'unità, perché $k$ non cambia". Poiché $s = j - k$, se $j$ cresce e $k$ resta fermo $s$ **aumenta** di uno; è anche ciò che serve alla conclusione successiva ("$j$ o $s$ aumenta di almeno un'unità").

A ogni iterazione $j$ o $s$ cresce di almeno 1 ed entrambi sono $\le n$: al più **$2n$ iterazioni**. Il calcolo della funzione fallimento è analogo, $O(m)$.

**Proposizione 13.3.** KMP risolve il pattern matching in tempo $O(n + m)$.

Correttezza: ogni confronto saltato è ridondante, perché la funzione fallimento garantisce che quei caratteri sono già stati verificati.

![[ASD-p582-1.png]]

Esecuzione sui dati dell'Esempio 13.1, con la funzione fallimento di `"abacab"`: $f = (0, 0, 1, 0, 1, 2)$. Al primo allineamento l'errore è al confronto 6 (su `b`, $k = 5$): $k$ diventa $f(4) = 1$, quindi il pattern si sposta di 4 e la `a` già letta non viene riconfrontata ("non viene eseguito alcun confronto"). Totale **19 confronti** contro i 27 della forza bruta.

_(libro, pp. 578–582)_

---

## Trie

Boyer-Moore e KMP **pre-elaborano il pattern**. L'approccio complementare **pre-elabora il testo**: conviene quando si fanno **molte ricerche sullo stesso testo** (ad esempio un sito che cerca dentro l'*Amleto*, o un motore di ricerca), così il costo iniziale si ripaga.

Un **trie** (si pronuncia come l'inglese *try*, dal centro della parola *retrieval*) è un albero che memorizza stringhe per un pattern matching veloce. L'applicazione principale è l'*information retrieval* (ad esempio cercare una sequenza di DNA in una base di dati genomica). Supporta il **pattern matching** e il **prefix matching**: trovare tutte le stringhe di un insieme $S$ che iniziano con una data stringa $X$.

### Trie standard

Vedi [[Trie]].

Sia $S$ un insieme di $s$ stringhe sull'alfabeto $\Sigma$ in cui **nessuna stringa è prefisso di un'altra**. Il **trie standard** di $S$ è un albero ordinato $T$ in cui:

- ogni nodo tranne la radice è etichettato con un carattere di $\Sigma$;
- i figli di un nodo interno hanno etichette distinte;
- $T$ ha $s$ foglie, ognuna associata a una stringa di $S$: concatenando le etichette dal figlio della radice alla foglia si ottiene la stringa.

![[ASD-p583-1.png]]

Trie standard per {bear, bell, bid, bull, buy, sell, stock, stop}. Le parole con un prefisso comune condividono il cammino: `bear` e `bell` condividono `b-e`, `stock` e `stop` condividono `s-t-o`.

L'ipotesi "nessuna stringa è prefisso di un'altra" garantisce che ogni stringa finisca in una foglia (è simile al vincolo dei codici a prefisso di Huffman, [[#Compressione del testo e metodo greedy|più avanti]]). La si può sempre ottenere aggiungendo un carattere terminatore che non sta in $\Sigma$.

Un nodo interno ha tra 1 e $|\Sigma|$ figli; un cammino dalla radice a un nodo di profondità $k$ corrisponde a un prefisso di lunghezza $k$ di qualche stringa, e per ogni carattere che può seguire quel prefisso c'è un figlio. Così il trie memorizza **una volta sola i prefissi comuni**. Con un alfabeto di due caratteri è un albero binario (eventualmente improprio). In pratica il grado medio è basso, e cala in profondità.

**Proposizione 13.4.** Un trie standard per $s$ stringhe di lunghezza totale $n$ su $\Sigma$ ha:
- altezza uguale alla lunghezza della stringa più lunga;
- al più $|\Sigma|$ figli per nodo interno;
- $s$ foglie;
- al più $n + 1$ nodi (caso peggiore: nessun prefisso comune, ogni nodo interno tranne la radice ha un figlio).

**Ricerca.** Per cercare $X$ si scende seguendo i suoi caratteri: se il cammino esiste e **termina in una foglia**, $X \in S$. Se non esiste o termina in un nodo interno, $X \notin S$ (nel trie sopra: `bull` finisce in una foglia; `bet` non ha cammino; `be` finisce in un nodo interno). Si visitano al più $m + 1$ nodi e in ognuno si cerca il figlio giusto in $O(|\Sigma|)$, quindi $O(m|\Sigma|)$; con una tabella hash o un array diretto per nodo si scende a $O(1)$ per nodo, cioè **$O(m)$**.

**Word matching.** Con un trie si fa il *word matching*: stabilire se il pattern è esattamente **una delle parole** del testo (non una sottostringa qualsiasi). Si inseriscono nel trie tutte le parole del documento.

![[ASD-p585-1.png]]

(a) Il testo, con gli indici dei caratteri; le *stop word* (articoli, preposizioni) sono escluse perché violerebbero spesso il vincolo dei prefissi. (b) Il trie delle parole: ogni foglia memorizza gli indici in cui la parola inizia nel testo; ad esempio `stock` compare agli indici 17, 40, 51, 62.

Si estende facilmente al prefix matching, ma **non** a pattern arbitrari (un suffisso proprio di una parola, o un pattern a cavallo di due parole).

**Costruzione.** Si inseriscono le stringhe una alla volta: si scende lungo il cammino di $X$ finché si può, poi si appende una catena di nuovi nodi con i caratteri rimanenti. Inserire una stringa di lunghezza $m$ costa $O(m|\Sigma|)$, o $O(m)$ atteso con tabelle hash; costruire tutto il trie costa $O(n)$ atteso, con $n$ lunghezza totale delle stringhe.

Il difetto del trie standard è lo **spazio**: molti nodi con un solo figlio. Da qui il trie compresso.

_(libro, pp. 582–586)_

### Trie compresso

Un **trie compresso** (*compressed trie*, detto anche **Patricia trie**) garantisce che ogni nodo interno abbia **almeno due figli**, comprimendo le catene di nodi con un solo figlio in un unico arco.

Un nodo interno $v$ è **ridondante** se non è la radice e ha un solo figlio. Una catena di $k \ge 2$ archi $(v_0, v_1)(v_1, v_2)\cdots(v_{k-1}, v_k)$ è **ridondante** se $v_1, \dots, v_{k-1}$ sono ridondanti e $v_0$, $v_k$ non lo sono. Il trie compresso si ottiene sostituendo ogni catena ridondante con un unico arco $(v_0, v_k)$ e dando a $v_k$ come etichetta la concatenazione delle etichette di $v_1, \dots, v_k$.

![[ASD-p586-1.png]]

Trie compresso per lo stesso insieme {bear, bell, bid, bull, buy, sell, stock, stop}: le etichette ora sono stringhe (`ar`, `ll`, `id`, `ell`, …). Oltre alle foglie è stato compresso anche il nodo interno `to`, condiviso da `stock` e `stop`. (Il trie standard ha otto nodi ridondanti.)

**Proposizione 13.5.** Un trie compresso per $s$ stringhe su un alfabeto di dimensione $d$ ha: nodi interni con almeno 2 e al più $d$ figli; $s$ foglie; **$O(s)$ nodi**.

Ma le etichette ora sono più lunghe: il vantaggio vero si ha quando il trie è un **indice ausiliario** per stringhe già memorizzate altrove. Se le stringhe stanno in un array $S[0], \dots, S[s-1]$, ogni etichetta si rappresenta con una terna $(i, j, k)$ che indica la sottostringa $S[i][j..k]$.

![[ASD-p588-1.png]]

(a) Le stringhe nell'array $S$ (`see`, `bear`, `sell`, `stock`, `bull`, `buy`, `bid`, `hear`, `bell`, `stop`). (b) Il trie compresso con le etichette come terne: ad esempio $(1, 0, 0)$ è `b` (carattere 0 di `bear`), $(7, 0, 3)$ è l'intera `hear`.

Lo spazio del trie passa da $O(n)$ a $O(s)$ (le stringhe vanno comunque memorizzate). La ricerca non è necessariamente più veloce: si confrontano comunque tutti i caratteri del pattern con le etichette.

_(libro, pp. 586–587)_

### Trie dei suffissi

Vedi [[Trie dei suffissi]].

Applicazione principale: le stringhe di $S$ sono **tutti i suffissi** di una stringa $X$. È il **trie dei suffissi** (*suffix trie*, o albero dei suffissi). La rappresentazione compatta si semplifica ancora: ogni etichetta è una coppia $j..k$ che indica $X[j..k]$. Per rispettare il vincolo dei prefissi si aggiunge in fondo a $X$ un carattere speciale `$` fuori da $\Sigma$ e si memorizzano i suffissi $X[j..n-1]\$$ per $j = 0, \dots, n-1$.

![[ASD-p589-1.png]]

(a) Trie dei suffissi di $X$ = `"minimize"` (8 suffissi): dalla radice partono `e`, `i`, `mi`, `nimize`, `ze`. (b) Rappresentazione compatta: ogni etichetta è un intervallo di indici in `minimize`, ad esempio `0..1` = `mi`, `2..7` = `nimize`.

#### Risparmiare spazio

La lunghezza totale dei suffissi è $1 + 2 + \dots + n = \frac{n(n+1)}{2}$: memorizzarli esplicitamente costa $O(n^2)$.

**Proposizione 13.6.** La rappresentazione compatta del trie dei suffissi di una stringa di lunghezza $n$ usa spazio $O(n)$.

#### Costruzione

Con l'algoritmo incrementale costa $O(|\Sigma| n^2)$, ma esiste un algoritmo specifico (complesso, non riportato) che costruisce il trie dei suffissi compatto in **$O(n)$**.

#### Uso di un trie dei suffissi

$P$ è sottostringa di $X$ **se e solo se** si può seguire il cammino di $P$ dalla radice (ogni sottostringa è un prefisso di qualche suffisso). Se ogni nodo $v$ con etichetta $j..k$ e stringa $Y$ di lunghezza $y$ sul cammino dalla radice soddisfa $X[k - y + 1..k] = Y$, si trova anche l'indice dell'occorrenza: la ricerca costa **$O(m)$**, indipendentemente da $n$.

_(libro, pp. 587–590)_

### Indicizzazione nei motori di ricerca

Un *web crawler* raccoglie le pagine e le memorizza; il **motore di ricerca** (*search engine*) restituisce le pagine più rilevanti che contengono le **parole chiave** (*keyword*) date.

#### Indici inversi

Vedi [[Indice inverso]].

La struttura centrale è l'**indice inverso** (*inverted index*, o *inverted file*): una mappa di coppie $(w, L)$, con $w$ una parola (**termine indice**) e $L$ la **lista di occorrenza** delle pagine che la contengono. Realizzazione:

1. un **array** con le liste di occorrenza (in ordine qualunque);
2. un **trie compresso** dei termini indice, le cui foglie contengono l'indice nell'array della lista corrispondente.

Il trie è abbastanza piccolo da stare in **memoria centrale**; le liste, enormi, stanno **su disco**.

- **Una parola chiave**: è un word matching: si cerca nel trie e si restituisce la lista.
- **Più parole chiave** (pagine che le contengono tutte): si recuperano le liste e se ne fa l'**intersezione**; per farla in modo efficiente le liste sono ordinate per indirizzo di pagina o realizzate come mappe ([[10 - ASD - Mappe, tabelle hash e skip list#Insiemi, multi-insiemi e multi-mappe|insiemi]]).

In più i motori ordinano le pagine per **rilevanza** (*ranking*), uno dei problemi centrali del settore.

> [!example] Collegamento
> La stessa struttura, nei DBMS, si usa per gli indici su attributi testuali: vedi [[Inverted List]] (Data Management).

_(libro, pp. 590–591)_

---

## Compressione del testo e metodo greedy

Data una stringa $X$ su un alfabeto (ASCII, Unicode), si vuole codificarla con una stringa binaria $Y$ **più corta**: meno banda e tempo di trasmissione, più documenti nello stesso spazio.

ASCII usa codici a **lunghezza fissa** (7 o 8 bit per carattere); Unicode era nato a 16 bit fissi, ma le codifiche diffuse usano meno bit per i caratteri frequenti. La **codifica di Huffman** usa **parole di codice** (*code-word*) di lunghezza variabile: più **corte** per i caratteri **frequenti**, più lunghe per quelli rari, ottimizzate sulle frequenze $f(c)$ della stringa specifica.

Per poter decodificare senza ambiguità, nessuna parola di codice deve essere **prefisso** di un'altra: è una **codifica a prefisso** (*prefix code*). Il risparmio è grande quando le frequenze sono molto variabili, come nelle lingue naturali.

La codifica si rappresenta con un **albero binario** $T$: ogni arco verso un figlio sinistro vale `0`, verso un figlio destro `1`; ogni foglia è un carattere e la sua parola di codice è la sequenza di bit dalla radice alla foglia. Poiché i caratteri stanno **solo nelle foglie**, nessun codice è prefisso di un altro. Ogni foglia ha la frequenza del suo carattere, ogni nodo interno la somma delle frequenze delle foglie del suo sottoalbero.

![[ASD-p592-1.png]]

$X$ = `"a fast runner need never be afraid of the dark"`. (a) Frequenze: spazio 9, a 5, b 1, d 3, e 7, f 3, h 1, i 1, k 1, n 4, o 1, r 5, s 1, t 2, u 1, v 1 (totale 46). (b) L'albero di Huffman: la radice ha frequenza 46, i caratteri frequenti (spazio, a, r, e) sono vicini alla radice. Ad esempio `r` = `011` (3 bit) e `h` = `10111` (5 bit).

### L'algoritmo di codifica di Huffman

Vedi [[Codifica di Huffman]].

Si parte con un albero di un solo nodo per ognuno dei $d$ caratteri distinti; a ogni passo si **fondono i due alberi con frequenza minima** in un nuovo albero con frequenza pari alla somma; si ripete finché ne resta uno.

```text
Algoritmo Huffman(X):
    Input:  una stringa X di lunghezza n con d caratteri distinti
    Output: l'albero di codifica per X
    calcola la frequenza f(c) di ogni carattere c di X
    inizializza una coda prioritaria Q
    for ogni carattere c in X do
        crea un albero binario T con la sola radice, che contiene c
        inserisci T in Q con chiave f(c)
    while Q.size() > 1 do
        sia e1 = Q.removeMin() la voce con chiave f1 e valore T1
        sia e2 = Q.removeMin() la voce con chiave f2 e valore T2
        crea un nuovo albero binario T con T1 e T2 come sottoalberi sinistro e destro
        inserisci T in Q con chiave f1 + f2
    sia e = Q.removeMin() la voce con valore T
    return l'albero T
```

Con una [[Coda prioritaria (ADT)|coda prioritaria]] a [[Heap binario|heap]], ogni iterazione costa $O(\log d)$; le iterazioni sono $d - 1$; contare le frequenze costa $O(n)$. Totale **$O(n + d \log d)$**.

L'intuizione della correttezza: esiste sempre un codice ottimo in cui i due caratteri **meno frequenti** differiscono solo nell'ultimo bit (sono fratelli in fondo all'albero). Fonderli in un "super-carattere" e ripetere il ragionamento porta al risultato.

**Proposizione 13.7.** L'algoritmo di Huffman costruisce in tempo $O(n + d\log d)$ un codice a prefisso **ottimo** per una stringa di lunghezza $n$ con $d$ caratteri distinti.
### Il metodo greedy

Vedi [[Metodo greedy]].

Huffman è un esempio di **metodo greedy** ("goloso"), uno schema per **problemi di ottimizzazione** (costruire una struttura minimizzando o massimizzando un costo):

1. si parte da una condizione iniziale nota, con il suo costo;
2. a ogni passo si fa la **scelta localmente migliore** tra quelle ammissibili;
3. non si torna mai indietro.

Non sempre porta all'ottimo, ma lo fa per i problemi con la **proprietà di scelta greedy**: un ottimo globale si raggiunge con una sequenza di scelte localmente ottime. Il codice di Huffman è uno di questi problemi; altri esempi sono gli algoritmi di Prim-Jarník, Kruskal e Dijkstra del [[14 - ASD - Algoritmi per grafi|capitolo 14]].

_(libro, pp. 591–594)_

---

## Programmazione dinamica

Vedi [[Programmazione dinamica]].

La **programmazione dinamica** (*dynamic programming*) è applicabile a moltissimi problemi, come il dividi-e-conquista. Spesso produce algoritmi **polinomiali** per problemi che sembrano **esponenziali**, e di solito sono brevi: pochi cicli annidati che **riempiono una tabella**.

### Moltiplicazione matriciale a catena

Si vuole calcolare $A = A_0 \cdot A_1 \cdots A_{n-1}$, dove $A_i$ è una matrice $d_i \times d_{i+1}$. Con l'algoritmo standard, moltiplicare $B$ ($d \times e$) per $C$ ($e \times f$) dà $A$ ($d \times f$) con
$$A[i][j] = \sum_{k=0}^{e-1} B[i][k] \cdot C[k][j]$$
cioè $d \cdot e \cdot f$ moltiplicazioni scalari. Il prodotto è **associativo** ($B(CD) = (BC)D$): il risultato non dipende dalle parentesi, ma il **costo** sì.

> [!example] Esempio 13.8
> $B$ è $2 \times 10$, $C$ è $10 \times 50$, $D$ è $50 \times 20$.
> - $B \cdot (C \cdot D)$: $10 \cdot 50 \cdot 20 + 2 \cdot 10 \cdot 20 = 10000 + 400 = 10400$ moltiplicazioni;
> - $(B \cdot C) \cdot D$: $2 \cdot 10 \cdot 50 + 2 \cdot 50 \cdot 20 = 1000 + 2000 = 3000$ moltiplicazioni.

Il **problema della moltiplicazione matriciale a catena** chiede dove mettere le parentesi per **minimizzare** le moltiplicazioni scalari.

#### Definizione di sotto-problemi

La forza bruta prova tutte le parentesizzazioni, che sono tante quanti gli alberi binari con $n$ foglie: un numero **esponenziale**. Prima osservazione: il problema si scompone in **sotto-problemi**. Sia $N_{i,j}$ il minimo numero di moltiplicazioni per calcolare $A_i \cdots A_j$; si vuole $N_{0,n-1}$.

#### Definizione di soluzioni ottimali

Seconda osservazione, l'**ottimalità dei sotto-problemi**: qualunque parentesizzazione di $A_i \cdots A_j$ termina con una moltiplicazione $(A_i \cdots A_k)(A_{k+1} \cdots A_j)$ per qualche $k \in \{i, \dots, j-1\}$, e in una soluzione ottima anche i due sotto-prodotti devono essere calcolati in modo ottimo (altrimenti sostituendo un sotto-calcolo con uno migliore si migliorerebbe il totale, contraddizione).

#### Progettazione di un algoritmo mediante programmazione dinamica

$$N_{i,j} = \min_{i \le k < j} \big\{ N_{i,k} + N_{k+1,j} + d_i\, d_{k+1}\, d_{j+1} \big\}, \qquad N_{i,i} = 0$$

I sotto-problemi **si sovrappongono** (lo stesso $N_{i,k}$ serve a molti $N_{i,j}$), quindi il dividi-e-conquista ricalcolerebbe tutto più volte. Si calcolano invece **dal basso verso l'alto** (*bottom-up*), memorizzandoli in una tabella: prima $N_{i,i} = 0$, poi $N_{i,i+1}$, poi $N_{i,i+2}$, … fino a $N_{0,n-1}$.

**Codice 13.6:**

```java
public static int[][] matrixChain(int[] d) {
  int n = d.length - 1;                    // numero di matrici
  int[][] N = new int[n][n];               // matrice n x n inizializzata con zeri
  for (int b=1; b < n; b++)                // numero di prodotti in una sotto-catena
    for (int i=0; i < n - b; i++) {        // inizio della sotto-catena
      int j = i + b;                       // fine della sotto-catena
      N[i][j] = Integer.MAX_VALUE;         // usato come "infinito"
      for (int k=i; k < j; k++)
        N[i][j] = Math.min(N[i][j], N[i][k] + N[k+1][j] + d[i]*d[k+1]*d[j+1]);
    }
  return N;
}
```

Tre cicli annidati, ognuno al più $n$ iterazioni: **$O(n^3)$** invece di un tempo esponenziale.

> [!example] Verifica sull'Esempio 13.8
> $d = (2, 10, 50, 20)$. $N_{0,1} = 2 \cdot 10 \cdot 50 = 1000$, $N_{1,2} = 10 \cdot 50 \cdot 20 = 10000$. $N_{0,2} = \min(N_{0,0} + N_{1,2} + 2\cdot10\cdot20,\ N_{0,1} + N_{2,2} + 2\cdot50\cdot20) = \min(10400, 3000) = 3000$ ✓.

_(libro, pp. 594–596)_

### DNA e allineamento di sequenze di caratteri

Vedi [[Sotto-sequenza comune più lunga (LCS)]].

Misurare la somiglianza tra due stringhe serve in genetica (due porzioni di DNA) e nell'ingegneria del software (due versioni di un sorgente: è il problema risolto dal programma Unix `diff`).

Una **sotto-sequenza** (*subsequence*) di $X = x_0 x_1 \cdots x_{n-1}$ è una stringa $x_{i_1} x_{i_2} \cdots x_{i_k}$ con $i_1 < i_2 < \dots < i_k$: caratteri di $X$ **nello stesso ordine ma non necessariamente consecutivi**. Ad esempio `AAAG` è sotto-sequenza di `CGATAATTGAGA`. (A differenza della sottostringa, che è contigua.)

Il problema **LCS** (*longest common subsequence*): date $X$ (lunghezza $n$) e $Y$ (lunghezza $m$), trovare la **più lunga stringa che sia sotto-sequenza di entrambe**. La forza bruta elenca le $2^n$ sotto-sequenze di $X$ e verifica ognuna in $O(m)$: $O(2^n m)$, inaccettabile.

#### Le componenti di una soluzione che usa la programmazione dinamica

La programmazione dinamica serve per problemi di **ottimizzazione** che hanno:

| Proprietà | Significato |
|---|---|
| **sotto-problemi semplici** | il problema si scompone ripetutamente in sotto-problemi descritti da pochi indici ($i$, $j$, $k$, …) |
| **ottimalità dei sotto-problemi** | una soluzione ottima si compone da soluzioni ottime dei sotto-problemi |
| **sovrapposizione dei sotto-problemi** | sotto-problemi diversi condividono sotto-problemi comuni (per questo conviene la tabella) |

#### Applicazione della programmazione dinamica al problema LCS

$L_{j,k}$ = lunghezza della LCS dei prefissi $X[0..j-1]$ e $Y[0..k-1]$. Se $j = 0$ o $k = 0$, $L_{j,k} = 0$. Per $j, k \ge 1$:

- **$x_{j-1} = y_{k-1}$**: l'ultimo carattere comune appartiene a una LCS dei due prefissi (se una LCS non lo usasse, si potrebbe sostituirne l'ultimo carattere o aggiungerlo, ottenendo una sotto-sequenza comune lunga almeno uguale). Quindi
$$L_{j,k} = 1 + L_{j-1,k-1}$$
- **$x_{j-1} \ne y_{k-1}$**: nessuna sotto-sequenza comune può finire con **entrambi** i caratteri; ne va scartato almeno uno:
$$L_{j,k} = \max(L_{j-1,k},\ L_{j,k-1})$$

![[ASD-p598-1.png]]

(a) $X$ = `GTTCCTAATA`, $Y$ = `CGATAATTGAGA`: gli ultimi caratteri sono entrambi `A`, quindi $L_{10,12} = 1 + L_{9,11}$. (b) Per i prefissi `GTTCCTAAT` e `CGATAATTGAG` gli ultimi caratteri (`T`, `G`) differiscono: $L_{9,11} = \max(L_{9,10}, L_{8,11})$.

#### L'algoritmo LCS

Valgono l'ottimalità e la sovrapposizione dei sotto-problemi ($L_{j,k}$ serve per $L_{j+1,k}$, $L_{j,k+1}$, $L_{j+1,k+1}$). Si riempie una tabella $(n+1) \times (m+1)$ inizializzata a 0.

**Codice 13.7:**

```java
/** Restituisce la tabella L[j][k] con la lunghezza LCS tra X[0..j-1] e Y[0..k-1]. */
public static int[][] LCS(char[] X, char[] Y) {
  int n = X.length;
  int m = Y.length;
  int[][] L = new int[n+1][m+1];
  for (int j=0; j < n; j++)
    for (int k=0; k < m; k++)
      if (X[j] == Y[k])                    // allineamento di questa corrispondenza
        L[j+1][k+1] = L[j][k] + 1;
      else                                 // decide di ignorare un carattere
        L[j+1][k+1] = Math.max(L[j][k+1], L[j+1][k]);
  return L;
}
```

> [!warning] Correzione
> Nel Codice 13.7 del libro la tabella è allocata come `new int[n+1][n+1]`: deve essere `new int[n+1][m+1]` (righe per i prefissi di $X$, colonne per quelli di $Y$). Con $m > n$ l'accesso `L[j+1][k+1]` uscirebbe dai limiti.

Due cicli annidati con corpo $O(1)$: **$O(nm)$**, contro $O(2^n m)$ della forza bruta.

La tabella dà la **lunghezza** $L_{n,m}$, non la sotto-sequenza. La si **ricostruisce a ritroso**: partendo da $L_{n,m}$, se $x_{j-1} = y_{k-1}$ il carattere fa parte della soluzione e si va a $L_{j-1,k-1}$; altrimenti si va verso il maggiore tra $L_{j-1,k}$ e $L_{j,k-1}$; ci si ferma quando si trova uno 0. Ogni passo decrementa $j$ o $k$: **$O(n + m)$**.

**Codice 13.8:**

```java
/** Restituisce la più lunga sotto-sequenza comune a X e Y, nota la tabella LCS. */
public static char[] reconstructLCS(char[] X, char[] Y, int[][] L) {
  StringBuilder solution = new StringBuilder();
  int j = X.length;
  int k = Y.length;
  while (L[j][k] > 0)                      // rimangono caratteri comuni
    if (X[j-1] == Y[k-1]) {
      solution.append(X[j-1]);
      j--;
      k--;
    } else if (L[j-1][k] >= L[j][k-1])
      j--;
    else
      k--;
  // restituisce, come array di char, la versione invertita di solution
  return solution.reverse().toString().toCharArray();
}
```

> [!warning] Correzione
> Nel Codice 13.8 del libro il tipo di ritorno è `char`, ma il metodo restituisce `toCharArray()`, cioè un `char[]` (come dice anche il commento): la firma corretta è `public static char[] reconstructLCS(...)`.

![[ASD-p600-1.png]]

La tabella $L$ per $X$ = `GTTCCTAATA` (righe) e $Y$ = `CGATAATTGAGA` (colonne). Il cammino evidenziato parte da $L_{10,12} = 6$ e risale; ogni passo **in diagonale** usa un carattere comune (gli indici corrispondenti sono evidenziati nelle intestazioni). La LCS ha lunghezza 6; la si ottiene leggendo i caratteri dei passi diagonali, che `reconstructLCS` raccoglie dall'ultimo al primo e poi inverte.

_(libro, pp. 597–600)_

> [!summary] Riepilogo del capitolo
> - **Pattern matching**: forza bruta $O(nm)$; **Boyer-Moore** (confronti da destra, salti con `last`) $O(nm)$ nel caso peggiore ma velocissimo in pratica; **KMP** (funzione fallimento) $O(n + m)$ garantito.
> - **Trie**: pre-elaborano il testo; trie standard ($O(n)$ nodi, ricerca $O(m)$), **compresso** ($O(s)$ nodi), **dei suffissi** (ricerca di qualunque sottostringa in $O(m)$, spazio $O(n)$); base degli **indici inversi** dei motori di ricerca.
> - **Metodo greedy**: scelte localmente ottime; funziona con la proprietà di scelta greedy. **Huffman** costruisce il codice a prefisso ottimo in $O(n + d\log d)$ fondendo i due alberi meno frequenti.
> - **Programmazione dinamica**: sotto-problemi semplici, ottimali e sovrapposti, risolti bottom-up in una tabella. Moltiplicazione a catena $O(n^3)$, **LCS** $O(nm)$ con ricostruzione $O(n+m)$.
