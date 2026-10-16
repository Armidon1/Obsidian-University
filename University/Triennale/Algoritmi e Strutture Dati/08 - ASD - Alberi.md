---
title: Alberi
aliases:
  - ASD — Alberi
tags:
  - algoritmi-e-strutture-dati
  - alberi
  - alberi-binari
  - attraversamenti
  - euler-tour
source: Goodrich, Tamassia, Goldwasser - Algoritmi e strutture dati in Java (cap. 8)
---

# Alberi

> [!abstract]
> Gli **alberi** sono la prima struttura dati **non lineare** del corso: la relazione tra gli elementi non è più "prima/dopo" ma **gerarchica** (genitore/figlio). Il capitolo definisce l'ADT albero (basato sulle **posizioni** del [[07 - ASD - Liste e iteratori#Liste posizionali|cap. 7]]), calcola **profondità** e **altezza**, introduce gli **alberi binari** e le loro proprietà numeriche, presenta tre implementazioni (struttura concatenata, array con numerazione per livelli, concatenata per alberi generici) e soprattutto gli **attraversamenti**: pre-ordine, post-ordine, in ampiezza, in ordine simmetrico e il **percorso di Eulero** che li unifica, con molte applicazioni.
> Gli alberi sono la base di heap ([[09 - ASD - Code prioritarie|cap. 9]]), alberi di ricerca ([[11 - ASD - Alberi di ricerca|cap. 11]]), trie ([[13 - ASD - Elaborazione di testi|cap. 13]]), alberi DFS/BFS e MST ([[14 - ASD - Algoritmi per grafi|cap. 14]]) e B-alberi ([[15 - ASD - Gestione della memoria e B-alberi|cap. 15]]). Il file system del [[05 - ASD - Ricorsione#File System|cap. 5]] era già un albero.
> Mappa del corso: [[MOC - Algoritmi e Strutture Dati]].

---

## Alberi generici

Gli alberi segnano una svolta nell'organizzazione dei dati: molti algoritmi diventano molto più veloci che con strutture lineari (array, liste), e gli alberi sono il modello naturale di file system, interfacce grafiche, basi di dati, siti web. La terminologia viene dagli alberi genealogici: **genitore** (*parent*), **figlio** (*child*), **antenato** (*ancestor*), **discendente** (*descendant*).

![[ASD-p311-1.png]]

Un albero genealogico: alcuni discendenti di Abramo (Genesi, capp. 25–36). Abramo è la radice; Ismaele, Isacco, Zimran, … sono i suoi figli; Esaù e Giacobbe sono figli di Isacco, e così via.

### Alberi: definizioni e proprietà

Vedi [[Albero (ADT)]].

Un **albero** è un ADT che memorizza elementi in modo gerarchico: ogni elemento, tranne quello in cima, ha un **genitore** e zero o più **figli**. L'elemento in cima è la **radice** (*root*) e si disegna in alto (al contrario degli alberi veri).

#### Definizione di albero

Formalmente un albero $T$ è un insieme di **nodi** che memorizzano elementi, con una relazione genitore-figlio tale che:

- se $T$ non è vuoto ha un nodo speciale, la **radice**, senza genitore;
- ogni nodo $v$ diverso dalla radice ha un **unico** genitore $w$; ogni nodo che ha $w$ come genitore è un figlio di $w$.

Un albero può essere **vuoto**. Questo permette una definizione **ricorsiva**: un albero è vuoto, oppure è formato da un nodo $r$ (la radice) e da un insieme, eventualmente vuoto, di sottoalberi le cui radici sono i figli di $r$.

![[ASD-p312-1.png]]

L'organigramma della finta azienda Electronics R'Us: 17 nodi. La radice è l'azienda; i suoi figli sono R&D, Sales, Purchasing, Manufacturing; Sales ha figli Domestic e International, International ha Canada, S. America, Overseas, e Overseas ha Africa, Europe, Asia, Australia; Manufacturing ha TV, CD, Tuner. I **nodi interni** sono Electronics R'Us, Sales, International, Overseas, Manufacturing.

#### Altre relazioni tra i nodi

- **Fratelli** (*siblings*): nodi con lo stesso genitore.
- **Nodo esterno** o **foglia** (*leaf*): senza figli. **Nodo interno**: con almeno un figlio.
- $u$ è **antenato** di $v$ se $u = v$ oppure $u$ è antenato del genitore di $v$; $v$ è **discendente** di $u$ se $u$ è antenato di $v$ (un nodo è antenato e discendente di sé stesso).
- Il **sottoalbero** di $T$ con radice $v$ è l'albero formato da tutti i discendenti di $v$ (compreso $v$).

![[ASD-p313-1.png]]

Il file system del [[05 - ASD - Ricorsione#File System|cap. 5]] visto come albero (Esempio 8.1): le cartelle sono nodi interni e i file sono foglie; in Unix/Linux la radice è la *root directory* `/`. `cs252/` è antenato di `papers/`, `pr3` è discendente di `cs016/`; il sottoalbero di radice `cs016/` contiene `cs016/`, `grades`, `homeworks/`, `programs/`, `hw1`, `hw2`, `hw3`, `pr1`, `pr2`, `pr3`.

#### Rami e percorsi negli alberi

- Un **ramo** (*edge*) è una coppia di nodi $(u, v)$ in cui uno è genitore dell'altro.
- Un **percorso** (*path*) è una sequenza di nodi in cui ogni coppia consecutiva è un ramo, ad esempio (`cs252/`, `projects/`, `demos/`, `market`).

#### Alberi ordinati

Un albero è **ordinato** (*ordered*) se i figli di ogni nodo hanno un ordine lineare significativo (primo figlio, secondo figlio, …), disegnato da sinistra a destra.

![[ASD-p313-2.png]]

Esempio 8.2: un libro è un albero ordinato. La radice è il libro; i figli sono Prefazione, Parte A, Parte B, Citazioni; sotto ci sono capitoli e sezioni, e le foglie sono paragrafi (¶), tabelle, figure. L'ordine dei figli conta.

Un albero genealogico è di solito ordinato (fratelli per data di nascita); un organigramma o una gerarchia di classi (come quella delle eccezioni del [[02 - ASD - Progettazione orientata agli oggetti#La gerarchia delle eccezioni in Java|cap. 2]]) no; un file system nemmeno, anche se il sistema operativo mostra i file in un certo ordine.

_(libro, pp. 310–314)_

### L'albero come tipo di dato astratto

Come per la lista posizionale, l'ADT albero usa le **posizioni** come astrazione dei nodi. Una posizione offre `getElement()`. L'albero offre:

| Metodi di accesso | |
|---|---|
| `root()` | posizione della radice (`null` se vuoto) |
| `parent(p)` | posizione del genitore di $p$ (`null` se $p$ è la radice) |
| `children(p)` | contenitore iterabile dei figli di $p$ (in ordine, se l'albero è ordinato) |
| `numChildren(p)` | numero di figli di $p$ |

| Metodi di interrogazione | |
|---|---|
| `isInternal(p)` | `true` se $p$ ha almeno un figlio |
| `isExternal(p)` | `true` se $p$ non ha figli |
| `isRoot(p)` | `true` se $p$ è la radice |

| Metodi generali | |
|---|---|
| `size()` | numero di posizioni (e di elementi) |
| `isEmpty()` | `true` se l'albero è vuoto |
| `iterator()` | iteratore sugli elementi (l'albero è `Iterable`) |
| `positions()` | contenitore iterabile di tutte le posizioni |

Una posizione non valida provoca `IllegalArgumentException`. I metodi per **creare o modificare** un albero non fanno parte dell'ADT generale: dipendono dall'implementazione e dall'applicazione.

#### Un'interfaccia albero in Java

```java
/** Un albero i cui nodi possono avere un numero arbitrario di figli. */
public interface Tree<E> extends Iterable<E> {
  Position<E> root();
  Position<E> parent(Position<E> p) throws IllegalArgumentException;
  Iterable<Position<E>> children(Position<E> p) throws IllegalArgumentException;
  int numChildren(Position<E> p) throws IllegalArgumentException;
  boolean isInternal(Position<E> p) throws IllegalArgumentException;
  boolean isExternal(Position<E> p) throws IllegalArgumentException;
  boolean isRoot(Position<E> p) throws IllegalArgumentException;
  int size();
  boolean isEmpty();
  Iterator<E> iterator();
  Iterable<Position<E>> positions();
}
```

#### La classe di base AbstractTree in Java

Come le classi `AbstractCollection`, `AbstractQueue`, `AbstractList` della libreria Java, una **classe astratta** implementa la parte di interfaccia che si può scrivere in modo generico ([[02 - ASD - Progettazione orientata agli oggetti#Classi astratte|cap. 2]]). Se una sottoclasse concreta fornisce `root()`, `parent(p)` e `children(p)`, tutto il resto può essere ereditato.

```java
/** Classe di base astratta che implementa in parte l'interfaccia Tree. */
public abstract class AbstractTree<E> implements Tree<E> {
  public boolean isInternal(Position<E> p) { return numChildren(p) > 0; }
  public boolean isExternal(Position<E> p) { return numChildren(p) == 0; }
  public boolean isRoot(Position<E> p) { return p == root(); }
  public boolean isEmpty() { return size() == 0; }
}
```

_(libro, pp. 314–316)_

### Calcolare profondità e altezza

Vedi [[Profondità e altezza di un albero]].

#### Profondità

La **profondità** (*depth*) di $p$ è il numero di antenati di $p$ diversi da $p$ stesso (la radice ha profondità 0; *International* ha profondità 2). Ricorsivamente:

- se $p$ è la radice, la profondità è 0;
- altrimenti è 1 più la profondità del genitore.

```java
/** Restituisce la profondità della posizione p. */
public int depth(Position<E> p) {
  if (isRoot(p))
    return 0;
  else
    return 1 + depth(parent(p));
}
```

Costo $O(d_p + 1)$, con $d_p$ la profondità di $p$; nel caso peggiore $O(n)$ (se ogni nodo interno ha un solo figlio, una posizione può avere profondità $n-1$). L'espressione $O(d_p + 1)$ è più informativa, perché $d_p$ può essere molto minore di $n$.

#### Altezza

L'**altezza** di un albero è la massima profondità delle sue posizioni (0 se è vuoto); la posizione più profonda è necessariamente una foglia. L'albero di Electronics R'Us ha altezza 4 (Africa e fratelli).

Un primo metodo, volutamente chiamato `heightBad` e privato:

```java
/** Restituisce l'altezza dell'albero. */
private int heightBad() {        // funziona, ma è quadratico nel caso peggiore
  int h = 0;
  for (Position<E> p : positions())
    if (isExternal(p))           // considera solo le foglie
      h = Math.max(h, depth(p));
  return h;
}
```

Scorrere le posizioni costa $O(n)$, ma chiama `depth` su ogni foglia: costo $O(n + \sum_{p \in L}(d_p + 1))$, dove $L$ è l'insieme delle foglie, che nel caso peggiore è $O(n^2)$ (esercizio C-8.31).

Meglio una definizione **ricorsiva** dell'altezza di una posizione:

- se $p$ è una foglia, l'altezza di $p$ è 0;
- altrimenti è 1 più il massimo delle altezze dei figli.

**Proposizione 8.3.** L'altezza della radice di un albero non vuoto, secondo la definizione ricorsiva, è uguale alla massima profondità delle foglie (esercizio R-8.3).

```java
/** Restituisce l'altezza del sottoalbero con radice p. */
public int height(Position<E> p) {
  int h = 0;                          // caso base: p è una foglia
  for (Position<E> c : children(p))
    h = Math.max(h, 1 + height(c));
  return h;
}
```

`height(root())` viene chiamato una volta per ogni posizione (scendendo dall'alto). Il lavoro non ricorsivo su $p$ è $O(c_p + 1)$, dove $c_p$ è il numero di figli di $p$ (si suppone che `children` costi così). Totale: $O\left(\sum_p (c_p + 1)\right) = O(n + \sum_p c_p)$.

**Proposizione 8.4.** In un albero di $n$ posizioni, $\sum_p c_p = n - 1$.
*Dimostrazione*: ogni posizione tranne la radice è figlia di esattamente un'altra, quindi contribuisce 1 alla somma.

Quindi `height` sulla radice costa **$O(n)$**.

_(libro, pp. 316–319)_

---

## Alberi binari

Vedi [[Albero binario]].

Un **albero binario** (*binary tree*) è un albero ordinato in cui:

1. ogni nodo ha **al massimo due** figli;
2. ogni figlio è etichettato come **figlio sinistro** (*left child*) o **figlio destro** (*right child*);
3. il figlio sinistro precede il destro.

Il sottoalbero con radice nel figlio sinistro (destro) di $v$ è il **sottoalbero sinistro** (**destro**) di $v$. Un albero binario è **proprio** (*proper*, o *full*, pieno) se ogni nodo ha **zero o due** figli, cioè ogni nodo interno ne ha esattamente due; altrimenti è **improprio**.

> [!example] Esempio 8.5 — Alberi di decisione
> Ogni nodo interno è una domanda sì/no; si va al figlio sinistro con "sì" e al destro con "no", seguendo un percorso dalla radice a una foglia, che è la **decisione**. Un **albero di decisione** (*decision tree*) è un albero binario proprio.

![[ASD-p320-1.png]]

Un albero di decisione per un investitore: "Sei una persona ansiosa?" → sì: conto di risparmio; no: "Avrai bisogno della maggior parte del denaro nei prossimi 5 anni?" → sì: fondo monetario; no: "Sei disposto ad accettare rischi in cambio di guadagni più elevati?" → sì: portafoglio azionario; no: portafoglio diversificato.

> [!example] Esempio 8.6 — Alberi di espressioni
> Un'espressione aritmetica è un albero binario con le **variabili/costanti** nelle foglie e gli **operatori** $+, -, \times, /$ nei nodi interni. Il valore di una foglia è la sua costante; il valore di un nodo interno è il risultato del suo operatore applicato ai valori dei figli. Con soli operatori binari l'albero è proprio; con operatori unari (come $-x$) può essere improprio.

![[ASD-p321-1.png]]

L'albero rappresenta $((((3+1)\times 3)/((9-5)+2)) - ((3\times(7-4))+6))$. Ad esempio il nodo "/" vale $\frac{(3+1)\cdot 3}{(9-5)+2} = \frac{12}{6} = 2$; il sottoalbero destro vale $3\cdot 3 + 6 = 15$, e la radice $2 - 15 = -13$.

#### Una definizione ricorsiva di albero binario

Un albero binario è:

- un albero vuoto, oppure
- un nodo radice $r$ con un elemento e due alberi binari, il sottoalbero sinistro e quello destro di $r$ (uno o entrambi possono essere vuoti).

### L'albero binario come tipo di dato astratto

Oltre ai metodi dell'albero, tre metodi di accesso:

| Metodo | Restituisce |
|---|---|
| `left(p)` | la posizione del figlio sinistro di $p$ (`null` se manca) |
| `right(p)` | la posizione del figlio destro di $p$ (`null` se manca) |
| `sibling(p)` | la posizione del fratello di $p$ (`null` se manca) |

```java
/** Un albero binario. */
public interface BinaryTree<E> extends Tree<E> {
  Position<E> left(Position<E> p) throws IllegalArgumentException;
  Position<E> right(Position<E> p) throws IllegalArgumentException;
  Position<E> sibling(Position<E> p) throws IllegalArgumentException;
}
```

#### La classe di base astratta AbstractBinaryTree

Usando `left` e `right` (ancora astratti) si implementano `sibling`, `numChildren` e `children`. `children` costruisce uno **snapshot** ([[07 - ASD - Liste e iteratori#Implementazione di iteratori|cap. 7]]): un `ArrayList` con il figlio sinistro (se c'è) e poi il destro.

```java
public abstract class AbstractBinaryTree<E> extends AbstractTree<E>
                                            implements BinaryTree<E> {
  /** Posizione del fratello di p (null se non esiste). */
  public Position<E> sibling(Position<E> p) {
    Position<E> parent = parent(p);
    if (parent == null) return null;   // p è la radice
    if (p == left(parent))             // p è il figlio sinistro
      return right(parent);            // (può essere null)
    else                               // p è il figlio destro
      return left(parent);             // (può essere null)
  }
  /** Numero di figli di p. */
  public int numChildren(Position<E> p) {
    int count = 0;
    if (left(p) != null)
      count++;
    if (right(p) != null)
      count++;
    return count;
  }
  /** Contenitore iterabile delle posizioni dei figli di p. */
  public Iterable<Position<E>> children(Position<E> p) {
    List<Position<E>> snapshot = new ArrayList<>(2);   // al massimo 2
    if (left(p) != null)
      snapshot.add(left(p));
    if (right(p) != null)
      snapshot.add(right(p));
    return snapshot;
  }
}
```

_(libro, pp. 319–322)_

### Proprietà degli alberi binari

Vedi [[Proprietà degli alberi binari]].

Il **livello** $d$ di un albero è l'insieme dei nodi di profondità $d$. In un albero binario il livello 0 ha al massimo 1 nodo, il livello 1 al massimo 2, il livello 2 al massimo 4: in generale il livello $d$ ha **al massimo $2^d$ nodi**.

![[ASD-p323-1.png]]

Il numero massimo di nodi per livello raddoppia scendendo: 1, 2, 4, 8, …

**Proposizione 8.7.** Sia $T$ un albero binario non vuoto con $n$ nodi, $n_E$ nodi esterni, $n_I$ nodi interni e altezza $h$:

| | Qualsiasi albero binario | Albero binario proprio |
|---|---|---|
| nodi | $h + 1 \le n \le 2^{h+1} - 1$ | $2h + 1 \le n \le 2^{h+1} - 1$ |
| nodi esterni | $1 \le n_E \le 2^h$ | $h + 1 \le n_E \le 2^h$ |
| nodi interni | $h \le n_I \le 2^h - 1$ | $h \le n_I \le 2^h - 1$ |
| altezza | $\log(n+1) - 1 \le h \le n - 1$ | $\log(n+1) - 1 \le h \le (n-1)/2$ |

Il limite superiore sui nodi viene dalla somma geometrica $1 + 2 + \dots + 2^h = 2^{h+1} - 1$; quello inferiore da un albero "a catena" (un nodo per livello). La conseguenza importante: **l'altezza di un albero binario con $n$ nodi è almeno logaritmica**, $h \ge \log(n+1) - 1$ (dimostrazioni nell'esercizio R-8.8).

#### Relazione tra nodi interni e nodi esterni in un albero binario proprio

**Proposizione 8.8.** In un albero binario proprio non vuoto, $n_E = n_I + 1$.

*Dimostrazione.* Si svuota l'albero mettendo i nodi in due "mucchietti", interni ed esterni.
- **Caso 1**: se $T$ ha un solo nodo $v$, lo si mette tra gli esterni.
- **Caso 2**: altrimenti si toglie una foglia $w$ e il suo genitore $v$ (interno), mettendo $w$ tra gli esterni e $v$ tra gli interni; se $v$ aveva un genitore $u$, si collega $u$ al fratello $z$ di $w$. L'albero resta binario e proprio.

![[ASD-p324-1.png]]

(a) la foglia $w$ e il genitore $v$ (cerchiati) stanno per essere rimossi; (b) dopo la rimozione; (c) il fratello $z$ di $w$ è stato collegato a $u$, il vecchio nonno.

Ogni passo del caso 2 toglie un interno e un esterno; alla fine resta un solo nodo, che va tra gli esterni. Quindi gli esterni sono uno in più degli interni. $\blacksquare$

La relazione non vale per alberi impropri o non binari (esercizi C-8.30–C-8.32).

_(libro, pp. 323–324)_

---

## Implementare alberi

`AbstractTree` e `AbstractBinaryTree` sono astratte: manca la rappresentazione interna. Le principali alternative:

### Una struttura concatenata per alberi binari

Ogni nodo contiene riferimenti all'**elemento**, al **genitore** e ai figli **sinistro** e **destro** (`null` se mancano; il genitore della radice è `null`). L'albero tiene un riferimento alla **radice** e il numero di nodi **size**.

![[ASD-p325-1.png]]

(a) un nodo con i campi `parent`, `left`, `right`, `element`; (b) un albero binario di 5 nodi con gli elementi Baltimore, Chicago, New York, Providence, Seattle: ogni nodo punta al genitore e ai figli; i riferimenti mancanti sono $\varnothing$.

#### Operazioni per la modifica di un albero binario concatenato

L'efficienza degli aggiornamenti dipende dalla rappresentazione, quindi ogni implementazione definisce i propri. Per l'albero binario concatenato:

| Metodo | Effetto |
|---|---|
| `addRoot(e)` | crea la radice in un albero vuoto con elemento $e$ (errore se non è vuoto) |
| `addLeft(p, e)` | crea il figlio sinistro di $p$ (errore se esiste già) |
| `addRight(p, e)` | crea il figlio destro di $p$ (errore se esiste già) |
| `set(p, e)` | sostituisce l'elemento in $p$, restituendo il vecchio |
| `attach(p, T1, T2)` | attacca $T_1$ e $T_2$ come sottoalberi sinistro e destro della **foglia** $p$; $T_1$ e $T_2$ diventano vuoti |
| `remove(p)` | rimuove $p$ sostituendolo con il suo unico figlio (se c'è); errore se $p$ ha due figli |

Sono tutte $O(1)$ nel caso peggiore (con sentinelle `attach` e `remove` sarebbero più semplici, esercizio C-8.38).

#### Implementazione in Java di un albero binario mediante struttura concatenata

`LinkedBinaryTree` estende `AbstractBinaryTree`. Come in `LinkedPositionalList`, i nodi (classe annidata `Node`) sono le posizioni. Convenzione per i nodi rimossi: il loro `parent` punta **a sé stesso**. Il metodo `createNode` è un **metodo-fabbrica** (*factory method*): le sottoclassi possono ridefinirlo per usare nodi più ricchi ([[11 - ASD - Alberi di ricerca|Paragrafo 11.2.1]]).

```java
/** Albero binario concreto con nodi concatenati. */
public class LinkedBinaryTree<E> extends AbstractBinaryTree<E> {
  //---------------- classe Node annidata ----------------
  protected static class Node<E> implements Position<E> {
    private E element;
    private Node<E> parent;
    private Node<E> left;
    private Node<E> right;
    public Node(E e, Node<E> above, Node<E> leftChild, Node<E> rightChild) {
      element = e;
      parent = above;
      left = leftChild;
      right = rightChild;
    }
    public E getElement() { return element; }
    public Node<E> getParent() { return parent; }
    public Node<E> getLeft() { return left; }
    public Node<E> getRight() { return right; }
    public void setElement(E e) { element = e; }
    public void setParent(Node<E> parentNode) { parent = parentNode; }
    public void setLeft(Node<E> leftChild) { left = leftChild; }
    public void setRight(Node<E> rightChild) { right = rightChild; }
  } //------------- fine della classe Node -------------

  /** Metodo-fabbrica: crea un nuovo nodo con elemento e. */
  protected Node<E> createNode(E e, Node<E> parent, Node<E> left, Node<E> right) {
    return new Node<E>(e, parent, left, right);
  }

  protected Node<E> root = null;   // radice
  private int size = 0;            // numero di nodi
  public LinkedBinaryTree() { }    // albero vuoto

  // metodo ausiliario
  /** Valida la posizione e la restituisce come nodo. */
  protected Node<E> validate(Position<E> p) throws IllegalArgumentException {
    if (!(p instanceof Node))
      throw new IllegalArgumentException("Not valid position type");
    Node<E> node = (Node<E>) p;
    if (node.getParent() == node)  // convenzione: nodo rimosso
      throw new IllegalArgumentException("p is no longer in the tree");
    return node;
  }

  // metodi di accesso (non già in AbstractBinaryTree)
  public int size() { return size; }
  public Position<E> root() { return root; }
  public Position<E> parent(Position<E> p) throws IllegalArgumentException {
    return validate(p).getParent();
  }
  public Position<E> left(Position<E> p) throws IllegalArgumentException {
    return validate(p).getLeft();
  }
  public Position<E> right(Position<E> p) throws IllegalArgumentException {
    return validate(p).getRight();
  }

  // metodi di aggiornamento
  /** Mette e nella radice di un albero vuoto. */
  public Position<E> addRoot(E e) throws IllegalStateException {
    if (!isEmpty()) throw new IllegalStateException("Tree is not empty");
    root = createNode(e, null, null, null);
    size = 1;
    return root;
  }
  /** Crea il figlio sinistro di p con elemento e. */
  public Position<E> addLeft(Position<E> p, E e) throws IllegalArgumentException {
    Node<E> parent = validate(p);
    if (parent.getLeft() != null)
      throw new IllegalArgumentException("p already has a left child");
    Node<E> child = createNode(e, parent, null, null);
    parent.setLeft(child);
    size++;
    return child;
  }
  /** Crea il figlio destro di p con elemento e. */
  public Position<E> addRight(Position<E> p, E e) throws IllegalArgumentException {
    Node<E> parent = validate(p);
    if (parent.getRight() != null)
      throw new IllegalArgumentException("p already has a right child");
    Node<E> child = createNode(e, parent, null, null);
    parent.setRight(child);
    size++;
    return child;
  }
  /** Sostituisce l'elemento in p. */
  public E set(Position<E> p, E e) throws IllegalArgumentException {
    Node<E> node = validate(p);
    E temp = node.getElement();
    node.setElement(e);
    return temp;
  }
  /** Attacca t1 e t2 come sottoalberi sinistro e destro della foglia p. */
  public void attach(Position<E> p, LinkedBinaryTree<E> t1,
                     LinkedBinaryTree<E> t2) throws IllegalArgumentException {
    Node<E> node = validate(p);
    if (isInternal(p)) throw new IllegalArgumentException("p must be a leaf");
    size += t1.size() + t2.size();
    if (!t1.isEmpty()) {                 // t1 diventa il sottoalbero sinistro
      t1.root.setParent(node);
      node.setLeft(t1.root);
      t1.root = null;
      t1.size = 0;
    }
    if (!t2.isEmpty()) {                 // t2 diventa il sottoalbero destro
      t2.root.setParent(node);
      node.setRight(t2.root);
      t2.root = null;
      t2.size = 0;
    }
  }
  /** Rimuove il nodo in p sostituendolo con il suo figlio (se c'è). */
  public E remove(Position<E> p) throws IllegalArgumentException {
    Node<E> node = validate(p);
    if (numChildren(p) == 2)
      throw new IllegalArgumentException("p has two children");
    Node<E> child = (node.getLeft() != null ? node.getLeft() : node.getRight());
    if (child != null)
      child.setParent(node.getParent());   // il nonno diventa genitore
    if (node == root)
      root = child;                        // il figlio diventa radice
    else {
      Node<E> parent = node.getParent();
      if (node == parent.getLeft())
        parent.setLeft(child);
      else
        parent.setRight(child);
    }
    size--;
    E temp = node.getElement();
    node.setElement(null);                 // aiuta il garbage collector
    node.setLeft(null);
    node.setRight(null);
    node.setParent(node);                  // convenzione per i nodi rimossi
    return temp;
  }
}
```

> [!note] Nota sul codice OCR
> Nella scansione del libro, il secondo blocco di `attach` sembra riferirsi a `t1` (`if (!t1.isEmpty())`, `t1.root = null`): è un errore di lettura della scansione, il codice corretto (riportato sopra) agisce su `t2`.

#### Prestazioni dell'albero binario implementato con struttura concatenata

| Metodo | Tempo |
|---|---|
| `size`, `isEmpty` | $O(1)$ |
| `root`, `parent`, `left`, `right`, `sibling`, `children`, `numChildren` | $O(1)$ |
| `isInternal`, `isExternal`, `isRoot` | $O(1)$ |
| `addRoot`, `addLeft`, `addRight`, `set`, `attach`, `remove` | $O(1)$ |
| `depth(p)` | $O(d_p + 1)$ |
| `height` | $O(n)$ |

Spazio $O(n)$: un `Node` per posizione più `root` e `size`.

_(libro, pp. 325–331)_

### Albero binario rappresentato con un array

Vedi [[Albero binario su array]].

Si numerano le posizioni con la **numerazione per livelli** (*level numbering*) $f(p)$:

- se $p$ è la radice, $f(p) = 0$;
- se $p$ è figlio **sinistro** di $q$, $f(p) = 2f(q) + 1$;
- se $p$ è figlio **destro** di $q$, $f(p) = 2f(q) + 2$.

I nodi di ogni livello sono numerati da sinistra a destra. La numerazione si basa sulle posizioni **potenziali**, quindi i numeri di un albero concreto possono non essere consecutivi.

![[ASD-p332-1.png]]

(a) lo schema generale: 0 alla radice, 1–2 al livello 1, 3–6 al livello 2, 7–14 al livello 3; (b) un albero di espressione: dato che il nodo 6 non ha figli, i numeri 13 e 14 non sono usati, mentre compaiono 15, 16, 19, 20, 25, 26.

L'elemento in posizione $p$ si memorizza in $A[f(p)]$:

![[ASD-p333-1.png]]

Un albero di espressione e l'array che lo rappresenta: la radice "/" in cella 0, "∗" in 1, "+" in 2, ecc.; le celle 9, 10, 13, 14 sono vuote (posizioni non usate).

Vantaggio: navigare costa solo aritmetica:

$$\text{left}(p) = 2f(p)+1, \qquad \text{right}(p) = 2f(p)+2, \qquad \text{parent}(p) = \left\lfloor \frac{f(p)-1}{2} \right\rfloor$$

Svantaggi:

- lo spazio dipende dalla **forma**: con $f_M$ il massimo numero usato, serve $N = 1 + f_M$; nel caso peggiore $N = 2^n - 1$ (esercizio R-8.14), proibitivo per alberi generici. Per gli **heap** del [[09 - ASD - Code prioritarie|cap. 9]] invece $N = n$ e la rappresentazione è perfetta;
- molte modifiche sono lente: rimuovere un nodo e "promuovere" il suo unico figlio costa $O(n)$, perché si spostano nell'array anche tutti i discendenti.

### Struttura concatenata per alberi generici

In un albero generico il numero di figli non è limitato: ogni nodo memorizza un **contenitore** (array o lista) di riferimenti ai figli.

![[ASD-p334-1.png]]

(a) il nodo ha i campi `parent`, `element` e `children` (un contenitore); (b) un nodo (New York) con il suo contenitore di quattro figli (Baltimore, Chicago, Providence, Seattle), ognuno dei quali punta al genitore.

| Metodo | Tempo |
|---|---|
| `size`, `isEmpty` | $O(1)$ |
| `root`, `parent`, `isRoot`, `isInternal`, `isExternal` | $O(1)$ |
| `numChildren(p)` | $O(1)$ |
| `children(p)` | $O(c_p + 1)$ |
| `depth(p)` | $O(d_p + 1)$ |
| `height` | $O(n)$ |

Spazio $O(n)$. (La didascalia della Tabella 8.2 del libro parla di "albero binario", ma la tabella si riferisce all'albero **generico**.)

_(libro, pp. 331–334)_

---

## Algoritmi di attraversamento di alberi

Vedi [[Attraversamenti di un albero]].

Un **attraversamento** (*traversal*) è un modo sistematico di **visitare** tutte le posizioni di un albero; la "visita" può essere qualunque azione, da incrementare un contatore a un'elaborazione complessa.

### Attraversamenti in pre-ordine e post-ordine per alberi generici

**Pre-ordine** (*preorder*): si visita prima la radice, poi ricorsivamente i sottoalberi dei figli (nell'ordine dei figli, se l'albero è ordinato).

```
Algorithm preorder(p):
  visita p                          { prima della ricorsione }
  for each figlio c in children(p) do
    preorder(c)                     { attraversa il sottoalbero di c }
```

![[ASD-p335-1.png]]

Pre-ordine del documento "Pubblicazione": l'ordine di visita è Pubblicazione, Titolo, Sommario, §1, §1.1, §1.2, §2, §2.1, §2.2, §2.3, §3, §3.1, §3.2, Citazioni: è l'ordine di lettura del documento.

#### Attraversamento in post-ordine

**Post-ordine** (*postorder*): prima ricorsivamente i sottoalberi, poi la radice.

```
Algorithm postorder(p):
  for each figlio c in children(p) do
    postorder(c)                    { attraversa il sottoalbero di c }
  visita p                          { dopo la ricorsione }
```

![[ASD-p336-1.png]]

Post-ordine dello stesso albero: Titolo, Sommario, §1.1, §1.2, §1, §2.1, §2.2, §2.3, §2, §3.1, §3.2, §3, Citazioni, Pubblicazione. Ogni nodo viene visitato dopo tutti i suoi discendenti (come `diskUsage` del cap. 5).

#### Analisi del tempo d'esecuzione

Come per `height`: la parte non ricorsiva su $p$ costa $O(c_p + 1)$ (se la visita è $O(1)$) e per la Proposizione 8.4 il totale è **$O(n)$**, ottimo perché bisogna visitare $n$ posizioni.

### Attraversamento in ampiezza (breadth-first) di un albero

Si visitano **tutte le posizioni di profondità $d$ prima di quelle di profondità $d+1$**: è l'attraversamento **in ampiezza** (*breadth-first*). È tipico dei programmi di gioco: un **albero di gioco** (*game tree*) rappresenta le mosse possibili a partire dalla configurazione iniziale (la radice).

![[ASD-p337-1.png]]

Parte dell'albero di gioco del tris (ignorando le simmetrie): la radice è la scacchiera vuota (1); i figli sono le mosse di X (2, 3, 4); poi le risposte di O (5–16). I numeri sono l'ordine di visita in ampiezza.

Il computer non può esplorare l'albero completo: esamina tutte le mosse, poi tutte le risposte, e così via, scendendo quanto permette il tempo. L'algoritmo **non è ricorsivo** e usa una **coda** (FIFO, [[06 - ASD - Pile, code e code doppie#Code (queue)|cap. 6]]):

```
Algorithm breadthfirst():
  inizializza la coda Q con root()
  while Q non è vuota do
    p = Q.dequeue()                 { p è il più vecchio della coda }
    visita p
    for each figlio c in children(p) do
      Q.enqueue(c)                  { i figli saranno visitati dopo }
```

$n$ `enqueue` e $n$ `dequeue`: **$O(n)$**. Sui grafi diventerà la **BFS** ([[14 - ASD - Algoritmi per grafi|cap. 14]]).

### Attraversamento in ordine simmetrico di un albero binario

Specifico degli alberi binari: l'attraversamento **in ordine simmetrico** (*inorder*) visita $p$ **dopo** il sottoalbero sinistro e **prima** del destro: informalmente, i nodi "da sinistra a destra".

```
Algorithm inorder(p):
  if p ha un figlio sinistro lc then
    inorder(lc)                     { sottoalbero sinistro }
  visita p
  if p ha un figlio destro rc then
    inorder(rc)                     { sottoalbero destro }
```

![[ASD-p338-1.png]]

In ordine simmetrico l'albero di espressione viene visitato come $3 + 1 \times 3 / 9 - 5 + 2 - 3 \times 7 - 4 + 6$: è la notazione infissa usuale, ma senza parentesi.

#### Alberi di ricerca binari

Un **albero di ricerca binario** (*binary search tree*) per un insieme ordinato $S$ (senza duplicati) è, in questo capitolo, un albero binario **proprio** in cui ogni posizione **interna** $p$ memorizza un elemento $e(p)$ di $S$ e:

- gli elementi nel sottoalbero **sinistro** di $p$ sono **minori** di $e(p)$;
- gli elementi nel sottoalbero **destro** sono **maggiori** di $e(p)$.

Quindi l'attraversamento **in ordine simmetrico** visita gli elementi **in ordine crescente**.

![[ASD-p339-1.png]]

Un albero di ricerca di interi (le foglie, quadratini neri, non contengono elementi). La ricerca di 42 segue il percorso continuo 58 → 31 → 42 (trovato); la ricerca di 70 segue il tratteggiato 58 → 90 → 62 → 75 e finisce in una foglia (non trovato).

Per cercare $v$ si scende dalla radice: se $v < e(p)$ si va a sinistra, se $v = e(p)$ si è trovato, se $v > e(p)$ si va a destra; arrivati a una foglia la ricerca fallisce. È un albero di decisione a tre vie. Il tempo è proporzionale all'**altezza**, che (Proposizione 8.7) va da $\log(n+1) - 1$ a $n - 1$: gli alberi di ricerca rendono al meglio quando sono **bassi**. È il tema del [[11 - ASD - Alberi di ricerca|cap. 11]].

_(libro, pp. 334–339)_

### Implementare attraversamenti di alberi in Java

`iterator()` si ottiene adattando `positions()` (come in `LinkedPositionalList`):

```java
//---------------- classe ElementIterator annidata ----------------
/** Adatta l'iterazione di positions() per restituire elementi. */
private class ElementIterator implements Iterator<E> {
  Iterator<Position<E>> posIterator = positions().iterator();
  public boolean hasNext() { return posIterator.hasNext(); }
  public E next() { return posIterator.next().getElement(); }   // l'elemento!
  public void remove() { posIterator.remove(); }
}
/** Iteratore sugli elementi dell'albero. */
public Iterator<E> iterator() { return new ElementIterator(); }
```

Si offrono metodi pubblici per ogni attraversamento e si sceglie quello predefinito per `positions()`: in `AbstractTree` il **pre-ordine**.

```java
public Iterable<Position<E>> positions() { return preorder(); }
```

#### Attraversamento in pre-ordine

Si usa un iteratore **snapshot**: un metodo privato ricorsivo riempie una lista (un iteratore pigro è l'esercizio C-8.47).

```java
/** Aggiunge a snapshot le posizioni del sottoalbero di radice p. */
private void preorderSubtree(Position<E> p, List<Position<E>> snapshot) {
  snapshot.add(p);                     // in pre-ordine p prima dei sottoalberi
  for (Position<E> c : children(p))
    preorderSubtree(c, snapshot);
}
/** Lista delle posizioni dell'albero in pre-ordine. */
public Iterable<Position<E>> preorder() {
  List<Position<E>> snapshot = new ArrayList<>();
  if (!isEmpty())
    preorderSubtree(root(), snapshot);
  return snapshot;
}
```

Il caso base è implicito: se $p$ non ha figli il ciclo non viene eseguito.

#### Attraversamento in post-ordine

```java
private void postorderSubtree(Position<E> p, List<Position<E>> snapshot) {
  for (Position<E> c : children(p))
    postorderSubtree(c, snapshot);
  snapshot.add(p);                     // in post-ordine p dopo i sottoalberi
}
public Iterable<Position<E>> postorder() {
  List<Position<E>> snapshot = new ArrayList<>();
  if (!isEmpty())
    postorderSubtree(root(), snapshot);
  return snapshot;
}
```

#### Attraversamento in ampiezza

```java
/** Lista delle posizioni dell'albero in ampiezza. */
public Iterable<Position<E>> breadthfirst() {
  List<Position<E>> snapshot = new ArrayList<>();
  if (!isEmpty()) {
    Queue<Position<E>> fringe = new LinkedQueue<>();
    fringe.enqueue(root());            // si parte dalla radice
    while (!fringe.isEmpty()) {
      Position<E> p = fringe.dequeue();
      snapshot.add(p);
      for (Position<E> c : children(p))
        fringe.enqueue(c);             // i figli in fondo alla coda
    }
  }
  return snapshot;
}
```

#### Attraversamento in ordine simmetrico per alberi binari

Va in `AbstractBinaryTree`, che lo rende anche il `positions()` **predefinito** per gli alberi binari (e quindi anche l'ordine di `iterator()`).

```java
private void inorderSubtree(Position<E> p, List<Position<E>> snapshot) {
  if (left(p) != null)
    inorderSubtree(left(p), snapshot);
  snapshot.add(p);
  if (right(p) != null)
    inorderSubtree(right(p), snapshot);
}
public Iterable<Position<E>> inorder() {
  List<Position<E>> snapshot = new ArrayList<>();
  if (!isEmpty())
    inorderSubtree(root(), snapshot);
  return snapshot;
}
/** Ridefinisce positions: per gli alberi binari l'ordine predefinito è simmetrico. */
public Iterable<Position<E>> positions() {
  return inorder();
}
```

| Attraversamento | Ordine | Struttura usata | Dove |
|---|---|---|---|
| Pre-ordine | nodo, poi figli | ricorsione | `AbstractTree` (predefinito) |
| Post-ordine | figli, poi nodo | ricorsione | `AbstractTree` |
| In ampiezza | livello per livello | coda | `AbstractTree` |
| Simmetrico | sinistro, nodo, destro | ricorsione | `AbstractBinaryTree` (predefinito) |

_(libro, pp. 339–343)_

### Applicazioni di attraversamenti di alberi

#### Sommario di un documento

Un **pre-ordine** dell'albero di un documento genera il **sommario**:

```java
for (Position<E> p : T.preorder())
  System.out.println(p.getElement());
```

```
(a) senza rientri        (b) con rientri
Pubblicazione            Pubblicazione
Titolo                     Titolo
Sommario                   Sommario
§1                         §1
§1.1                         §1.1
§1.2                         §1.2
§2                         §2
§2.1                         §2.1
...                        ...
```

Per i rientri si potrebbe stampare `spaces(2*T.depth(p)) + p.getElement()`, ma chiamare `depth` su ogni posizione costa $O(n^2)$ nel caso peggiore (come `heightBad`). Meglio una ricorsione dall'alto che **passa la profondità come parametro**: $O(n)$ (più il tempo per stampare gli spazi).

```java
/** Stampa in pre-ordine il sottoalbero di T con radice p e profondità d. */
public static <E> void printPreorderIndent(Tree<E> T, Position<E> p, int d) {
  System.out.println(spaces(2*d) + p.getElement());   // rientro in base a d
  for (Position<E> c : T.children(p))
    printPreorderIndent(T, c, d+1);                   // il figlio ha profondità d+1
}
// prima invocazione: printPreorderIndent(T, T.root(), 0)
```

Per aggiungere **etichette numeriche** calcolate dalla struttura (non presenti negli elementi), ad esempio per Electronics R'Us:

```
Electronics R'Us
  1 R&D
  2 Sales
    2.1 Domestic
    2.2 International
      2.2.1 Canada
      2.2.2 S. America
```

si passa la **lista delle etichette** del percorso dalla radice (per Domestic, $\{2, 1\}$). Per non copiare la lista a ogni livello si usa **sempre la stessa lista**: ogni invocazione aggiunge temporaneamente un elemento in fondo e lo toglie prima di terminare ("non lasciare traccia").

```java
/** Stampa con etichette il sottoalbero di T con radice p. */
public static <E>
void printPreorderLabeled(Tree<E> T, Position<E> p, ArrayList<Integer> path) {
  int d = path.size();                     // profondità = lunghezza del percorso
  System.out.print(spaces(2*d));           // rientro, poi etichetta
  for (int j = 0; j < d; j++) System.out.print(path.get(j) + (j == d-1 ? " " : "."));
  System.out.println(p.getElement());
  path.add(1);                             // etichetta del primo figlio
  for (Position<E> c : T.children(p)) {
    printPreorderLabeled(T, c, path);
    path.set(d, 1 + path.get(d));          // incrementa l'ultima etichetta
  }
  path.remove(d);                          // ripristina il percorso
}
```

#### Calcolo dell'occupazione di spazio su disco

È un **post-ordine** (lo spazio di una cartella si conosce solo dopo quello dei figli), ma `postorder()` non basta: serve che **i figli restituiscano un valore al genitore**. Soluzione ad hoc (come `diskUsage`):

```java
/** Spazio totale del sottoalbero di T con radice p (l'elemento è lo spazio locale). */
public static int diskSpace(Tree<Integer> T, Position<Integer> p) {
  int subtotal = p.getElement();
  for (Position<Integer> c : T.children(p))
    subtotal += diskSpace(T, c);
  return subtotal;
}
```

#### Rappresentazione di un albero mediante una stringa con parentesi

La sola sequenza in pre-ordine non basta a ricostruire l'albero. Una rappresentazione compatta è la **stringa con parentesi** $P(T)$: se $T$ ha una sola posizione $p$, $P(T)$ = `p.getElement()`; altrimenti

$$P(T) = \texttt{p.getElement()} + \texttt{"("} + P(T_1) + \texttt{", "} + \dots + \texttt{", "} + P(T_k) + \texttt{")"}$$

dove $T_1, \dots, T_k$ sono i sottoalberi dei figli. Per Electronics R'Us:

```
Electronics R'Us (R&D, Sales (Domestic, International (Canada,
S. America, Overseas (Africa, Europe, Asia, Australia))),
Purchasing, Manufacturing (TV, CD, Tuner))
```

È un pre-ordine con la punteggiatura aggiunta prima del ciclo sui figli ("("), tra i figli (", ") e dopo (")"):

```java
/** Stampa la stringa con parentesi del sottoalbero di T con radice p. */
public static <E> void parenthesize(Tree<E> T, Position<E> p) {
  System.out.print(p.getElement());
  if (T.isInternal(p)) {
    boolean firstTime = true;
    for (Position<E> c : T.children(p)) {
      System.out.print((firstTime ? " (" : ", "));   // carattere giusto
      firstTime = false;                             // poi sempre virgola
      parenthesize(T, c);                            // ricorsione su un figlio
    }
    System.out.print(")");
  }
}
```

#### L'attraversamento in ordine simmetrico per disegnare alberi

Per disegnare un albero binario (con $x$ crescente verso destra e $y$ crescente verso il basso, origine in alto a sinistra):

- $x(p)$ = numero di posizioni visitate **prima** di $p$ nell'ordine simmetrico;
- $y(p)$ = profondità di $p$.

![[ASD-p347-1.png]]

Il disegno risultante: ogni nodo ha una colonna diversa (0–12) data dal suo rango in ordine simmetrico e una riga (0–4) data dalla profondità; così nessun nodo si sovrappone e ogni sottoalbero sinistro sta a sinistra del genitore.

```java
/** Assegna le coordinate; invocazione iniziale: layout(T, T.root(), 0, 0). */
public static <E> int layout(BinaryTree<E> T, Position<E> p, int d, int x) {
  if (T.left(p) != null)
    x = layout(T, T.left(p), d+1, x);    // x viene incrementato
  p.getElement().setX(x++);              // post-incremento
  p.getElement().setY(d);
  if (T.right(p) != null)
    x = layout(T, T.right(p), d+1, x);   // x viene incrementato
  return x;
}
```

Il metodo riceve la $x$ da assegnare al nodo più a sinistra del sottoalbero e restituisce la prima $x$ libera alla sua destra.

_(libro, pp. 343–348)_

### Percorso di Eulero

Vedi [[Percorso di Eulero]].

Non tutte le applicazioni rientrano negli schemi rigidi. Il **percorso** (o cammino) **di Eulero** (*Euler tour traversal*) li unifica: si "cammina" attorno all'albero partendo dalla radice verso il figlio più a sinistra, tenendo i rami sempre alla propria sinistra come se fossero muri.

![[ASD-p348-1.png]]

Il percorso di Eulero sull'albero di espressione: una linea continua che gira attorno a ogni nodo e scende e risale lungo ogni ramo.

Il costo è $O(n)$: ogni ramo (sono $n - 1$) si percorre due volte, una in discesa e una in salita. Ogni posizione $p$ si incontra in due momenti:

- **pre-visita**: la prima volta, passando alla sua sinistra;
- **post-visita**: l'ultima volta, risalendo alla sua destra.

Tra le due c'è, ricorsivamente, il percorso di Eulero di ogni sottoalbero (ad esempio quello del nodo "/" contiene quelli dei suoi due sottoalberi). Negli alberi binari c'è anche la visita **in ordine simmetrico**, quando il percorso passa **sotto** il nodo (dopo il sottoalbero sinistro, prima del destro).

```
Algorithm eulerTour(T, p):
  pre-visita di p
  for each figlio c in T.children(p) do
    eulerTour(T, c)                  { ricorsione su ogni sottoalbero }
  post-visita di p
```

```mermaid
flowchart LR
    A[pre-visita p] --> B[percorso del sottoalbero sinistro]
    B --> C["visita in ordine (solo binari)"]
    C --> D[percorso del sottoalbero destro]
    D --> E[post-visita p]
```

Esempio di attraversamento "nuovo": contare i **discendenti** di ogni posizione. Si tiene un contatore che si incrementa a ogni pre-visita; il numero di discendenti di $p$ è la differenza tra il contatore alla post-visita e alla pre-visita di $p$, più uno (per $p$ stesso), perché tutti e soli i discendenti di $p$ vengono pre-visitati in quell'intervallo. Tutto in $O(n)$.

_(libro, pp. 348–349)_

---

> [!summary] Riepilogo
> - **Albero**: radice, genitore unico, figli; foglie e nodi interni; antenati/discendenti; sottoalberi; alberi ordinati. ADT basato su posizioni (`root`, `parent`, `children`, …), `AbstractTree` ricava il resto da `root`, `parent`, `children`.
> - **Profondità** $O(d_p+1)$; **altezza** ricorsiva $O(n)$ grazie a $\sum c_p = n-1$ (`heightBad` è $O(n^2)$).
> - **Albero binario** (proprio se 0 o 2 figli): alberi di decisione, di espressione. Livello $d$ ha al massimo $2^d$ nodi; $\log(n+1)-1 \le h \le n-1$; nei proprî $n_E = n_I + 1$.
> - Implementazioni: **concatenata** (tutto $O(1)$, `createNode` factory method, nodo rimosso con `parent == this`), **array con numerazione per livelli** ($2f+1$, $2f+2$, $\lfloor(f-1)/2\rfloor$; spazio fino a $2^n-1$), **generica** con contenitore di figli.
> - **Attraversamenti** $O(n)$: pre-ordine (sommari), post-ordine (spazio su disco), in ampiezza con una coda (alberi di gioco), simmetrico (espressioni, **alberi di ricerca**, disegno), **percorso di Eulero** che li unifica (pre-visita, visita in ordine, post-visita).
