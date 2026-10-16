---
title: Mappe, tabelle hash e skip list
aliases:
  - ASD — Mappe, tabelle hash e skip list
tags:
  - algoritmi-e-strutture-dati
  - mappe
  - tabelle-hash
  - hashing
  - skip-list
  - insiemi
source: Goodrich, Tamassia, Goldwasser - Algoritmi e strutture dati in Java (cap. 10)
---

# Mappe, tabelle hash e skip list

> [!abstract]
> La **mappa** (o array associativo) memorizza coppie **chiave-valore** con chiavi uniche e permette di trovare un valore **data la chiave**. Il capitolo:
> - definisce l'ADT mappa e una prima implementazione banale con una lista non ordinata ($O(n)$);
> - presenta le **tabelle hash**: funzioni di hash (codifica + compressione), gestione delle collisioni (**concatenazione separata**, **indirizzamento aperto** con esplorazione lineare/quadratica/doppio hashing), **fattore di carico** e rehashing: operazioni in tempo **atteso** $O(1)$;
> - introduce le **mappe ordinate** (ricerche "vicine" a una chiave: `ceilingEntry`, `floorEntry`, `subMap`…) con la tabella di ricerca ordinata e la ricerca binaria;
> - presenta la **skip list**, struttura **randomizzata** con ricerche e aggiornamenti in tempo atteso $O(\log n)$;
> - chiude con insiemi, multi-insiemi e multi-mappe.
>
> Le entry riprendono il [[09 - ASD - Code prioritarie#L'oggetto composito Entry|cap. 9]]; la ricerca binaria è quella del [[05 - ASD - Ricorsione#Ricerca binaria|cap. 5]]. Le mappe ordinate con garanzie di caso peggiore arriveranno con gli alberi di ricerca del [[11 - ASD - Alberi di ricerca|cap. 11]].
> Mappa del corso: [[MOC - Algoritmi e Strutture Dati]].

---

## Mappe

Vedi [[Mappa (ADT)]].

Una **mappa** (*map*) memorizza coppie $(k, v)$ chiamate **voci** (*entry*), dove $k$ è la **chiave di ricerca** (*search key*) e $v$ il valore. Le chiavi sono **tutte distinte**; l'associazione chiave → valore si chiama **mappatura** (*mapping*).

![[ASD-p402-1.png]]

La metafora dell'archivio: l'utente assegna un'etichetta (la **chiave**, es. "Q2 Report") a una cartella di documenti (il **valore**); la cartella etichettata è una **voce**, che viene messa nell'archivio a cassetti (la **mappa**) e si ritrova o si elimina tramite l'etichetta.

Le mappe si chiamano anche **array associativi** (*associative arrays*): la chiave fa da "indice", ma non deve essere numerica e non indica direttamente una posizione. Il Web stesso è una mappa: chiave = URL, valore = contenuto della pagina. Altri esempi:

- il sistema informativo di un'università: matricola → dati dello studente;
- il **DNS**: nome di host (www.wiley.com) → indirizzo IP (208.215.179.146);
- un social network: nome utente → informazioni dell'utente;
- i clienti di un'azienda: codice cliente → dati del cliente;
- un sistema grafico: nome di colore ('turquoise') → terna RGB (64, 224, 208).

### La mappa come tipo di dato astratto

| Metodo | Effetto |
|---|---|
| `size()` | numero di voci |
| `isEmpty()` | `true` se vuota |
| `get(k)` | valore associato a $k$, oppure `null` |
| `put(k, v)` | se $k$ non c'è aggiunge $(k, v)$ e restituisce `null`; altrimenti sostituisce il valore e restituisce il **vecchio** |
| `remove(k)` | rimuove la voce con chiave $k$ e ne restituisce il valore (`null` se non c'è) |
| `keySet()` | contenitore iterabile delle chiavi |
| `values()` | contenitore iterabile dei valori (con eventuali duplicati) |
| `entrySet()` | contenitore iterabile delle voci |

#### Mappe nel pacchetto java.util

È una versione semplificata di `java.util.Map` (che usa `java.util.Map.Entry` invece della nostra `Entry`). Poiché `get`, `put` e `remove` restituiscono `null` quando la chiave manca, c'è un'**ambiguità** se `null` è un valore ammesso: `get(k)` restituisce `null` sia se $k$ manca sia se $k$ è associata a `null`. Alcune implementazioni Java vietano `null` come valore (e come chiave); `java.util.Map` offre `containsKey(k)` per togliere il dubbio.

> [!example] Esempio 10.1
> | Metodo | Restituisce | Mappa |
> |---|---|---|
> | `isEmpty()` | true | {} |
> | `put(5, A)` | null | {(5,A)} |
> | `put(7, B)` | null | {(5,A), (7,B)} |
> | `put(2, C)` | null | {(5,A), (7,B), (2,C)} |
> | `put(8, D)` | null | {(5,A), (7,B), (2,C), (8,D)} |
> | `put(2, E)` | C | {(5,A), (7,B), (2,E), (8,D)} |
> | `get(7)` | B | invariata |
> | `get(4)` | null | invariata |
> | `get(2)` | E | invariata |
> | `size()` | 4 | invariata |
> | `remove(5)` | A | {(7,B), (2,E), (8,D)} |
> | `remove(2)` | E | {(7,B), (8,D)} |
> | `get(2)` | null | {(7,B), (8,D)} |
> | `remove(2)` | null | {(7,B), (8,D)} |
> | `isEmpty()` | false | {(7,B), (8,D)} |
> | `entrySet()` | {(7,B), (8,D)} | invariata |
> | `keySet()` | {7, 8} | invariata |
> | `values()` | {B, D} | invariata |

```java
public interface Map<K,V> {
  int size();
  boolean isEmpty();
  V get(K key);
  V put(K key, V value);
  V remove(K key);
  Iterable<K> keySet();
  Iterable<V> values();
  Iterable<Entry<K,V>> entrySet();
}
```

### Applicazione: frequenza delle parole in un testo

Per contare le occorrenze di ogni parola (analisi statistica di e-mail o articoli) una mappa è ideale: chiave = parola, valore = conteggio.

```java
/** Conta le parole di un documento e stampa la più frequente. */
public class WordCount {
  public static void main(String[] args) {
    Map<String,Integer> freq = new ChainHashMap<>();   // o un'altra mappa concreta
    // legge il documento; i delimitatori sono tutti i caratteri non alfabetici
    Scanner doc = new Scanner(System.in).useDelimiter("[^a-zA-Z]+");
    while (doc.hasNext()) {
      String word = doc.next().toLowerCase();   // in minuscolo
      Integer count = freq.get(word);           // conteggio attuale
      if (count == null)
        count = 0;                              // parola nuova
      freq.put(word, 1 + count);                // (ri)assegna il conteggio
    }
    int maxCount = 0;
    String maxWord = "no word";
    for (Entry<String,Integer> ent : freq.entrySet())   // trova la più frequente
      if (ent.getValue() > maxCount) {
        maxWord = ent.getKey();
        maxCount = ent.getValue();
      }
    System.out.print("The most frequent word is '" + maxWord);
    System.out.println("' with " + maxCount + " occurrences.");
  }
}
```

### La classe di base AbstractMap

![[ASD-p406-1.png]]

La gerarchia delle mappe del libro: le interfacce `Map` e `SortedMap` (che la estende); `AbstractMap` e `AbstractSortedMap`; le classi concrete `UnsortedTableMap`, `AbstractHashMap` (con le sottoclassi `ChainHashMap` e `ProbeHashMap`), `SortedTableMap` e `TreeMap` (cap. 11, con ulteriori sottoclassi).

`AbstractMap` fornisce:

- `isEmpty()` basato su `size()`;
- la classe annidata `MapEntry` (implementa `Entry`), con `setValue` che restituisce il vecchio valore;
- `keySet()` e `values()` ottenuti **adattando** `entrySet()` (come gli iteratori di elementi da posizioni del [[07 - ASD - Liste e iteratori#Implementazione di iteratori|cap. 7]]): le sottoclassi devono implementare solo `entrySet`.

```java
public abstract class AbstractMap<K,V> implements Map<K,V> {
  public boolean isEmpty() { return size() == 0; }
  //---------------- classe MapEntry annidata ----------------
  protected static class MapEntry<K,V> implements Entry<K,V> {
    private K k;   // chiave
    private V v;   // valore
    public MapEntry(K key, V value) {
      k = key;
      v = value;
    }
    public K getKey() { return k; }
    public V getValue() { return v; }
    protected void setKey(K key) { k = key; }
    protected V setValue(V value) {
      V old = v;
      v = value;
      return old;
    }
  } //------------- fine della classe MapEntry -------------

  // supporto per keySet
  private class KeyIterator implements Iterator<K> {
    private Iterator<Entry<K,V>> entries = entrySet().iterator();
    public boolean hasNext() { return entries.hasNext(); }
    public K next() { return entries.next().getKey(); }   // restituisce la chiave
    public void remove() { throw new UnsupportedOperationException(); }
  }
  private class KeyIterable implements Iterable<K> {
    public Iterator<K> iterator() { return new KeyIterator(); }
  }
  public Iterable<K> keySet() { return new KeyIterable(); }

  // supporto per values
  private class ValueIterator implements Iterator<V> {
    private Iterator<Entry<K,V>> entries = entrySet().iterator();
    public boolean hasNext() { return entries.hasNext(); }
    public V next() { return entries.next().getValue(); }   // restituisce il valore
    public void remove() { throw new UnsupportedOperationException(); }
  }
  private class ValueIterable implements Iterable<V> {
    public Iterator<V> iterator() { return new ValueIterator(); }
  }
  public Iterable<V> values() { return new ValueIterable(); }
}
```

### Una semplice implementazione di mappa non ordinata

`UnsortedTableMap` memorizza le voci in un `ArrayList` in ordine arbitrario. Tutte le operazioni iniziano con `findIndex`, una scansione lineare. Per rimuovere non si fa scorrere la lista: si sposta l'**ultima** voce nel buco ($O(1)$), tanto l'ordine non conta.

```java
public class UnsortedTableMap<K,V> extends AbstractMap<K,V> {
  /** Array interno delle voci. */
  private ArrayList<MapEntry<K,V>> table = new ArrayList<>();
  public UnsortedTableMap() { }
  /** Indice della voce con chiave key, oppure -1. */
  private int findIndex(K key) {
    int n = table.size();
    for (int j = 0; j < n; j++)
      if (table.get(j).getKey().equals(key))
        return j;
    return -1;                                    // non trovata
  }
  public int size() { return table.size(); }
  public V get(K key) {
    int j = findIndex(key);
    if (j == -1) return null;
    return table.get(j).getValue();
  }
  public V put(K key, V value) {
    int j = findIndex(key);
    if (j == -1) {
      table.add(new MapEntry<>(key, value));      // nuova voce
      return null;
    } else                                        // chiave già presente
      return table.get(j).setValue(value);        // restituisce il vecchio valore
  }
  public V remove(K key) {
    int j = findIndex(key);
    int n = size();
    if (j == -1) return null;
    V answer = table.get(j).getValue();
    if (j != n - 1)
      table.set(j, table.get(n-1));               // l'ultima voce riempie il buco
    table.remove(n-1);                            // e si toglie l'ultima cella
    return answer;
  }
  // supporto per entrySet
  private class EntryIterator implements Iterator<Entry<K,V>> {
    private int j = 0;
    public boolean hasNext() { return j < table.size(); }
    public Entry<K,V> next() {
      if (j == table.size()) throw new NoSuchElementException();
      return table.get(j++);
    }
    public void remove() { throw new UnsupportedOperationException(); }
  }
  private class EntryIterable implements Iterable<Entry<K,V>> {
    public Iterator<Entry<K,V>> iterator() { return new EntryIterator(); }
  }
  public Iterable<Entry<K,V>> entrySet() { return new EntryIterable(); }
}
```

`get`, `put` e `remove` sono $O(n)$ nel caso peggiore: serve qualcosa di molto più veloce.

_(libro, pp. 402–409)_

---

## Tabelle hash

Vedi [[Tabella hash]].

La **tabella hash** (*hash table*) è la struttura più usata per implementare una mappa.

**Riscaldamento**: se le chiavi fossero interi in $[0, N-1]$ basterebbe una **tabella di ricerca** (*lookup table*) di lunghezza $N$, con il valore di chiave $k$ nella cella $k$: tutte le operazioni in $O(1)$ nel caso peggiore.

![[ASD-p410-1.png]]

Una tabella di ricerca di lunghezza 11 per la mappa {(1,D), (3,Z), (6,C), (7,Q)}: il valore di ogni chiave sta nella cella con quell'indice; le altre celle sono vuote.

Due problemi: $N$ può essere molto più grande di $n$ (spreco), e le chiavi non sono sempre interi. L'idea della tabella hash: una **funzione di hash** porta ogni chiave in un indice $[0, N-1]$. Chiavi diverse possono finire nello stesso indice, quindi la tabella è un **array di bucket** ("secchi"), ognuno con le voci che la funzione assegna a quell'indice (un bucket vuoto può essere `null`).

![[ASD-p410-2.png]]

Un array di 11 bucket per la mappa {(1,D), (25,C), (3,F), (14,Z), (6,A), (39,C), (7,Q)} con una semplice funzione di hash: nel bucket 3 finiscono (25,C), (3,F), (14,Z) (tutte con $k \bmod 11 = 3$), nel bucket 6 finiscono (6,A) e (39,C).

### Funzioni di hash

Vedi [[Funzione di hash]].

Una **funzione di hash** $h$ porta ogni chiave $k$ in un intero di $[0, N-1]$, dove $N$ è la capacità dell'array di bucket $A$; la voce $(k, v)$ va in $A[h(k)]$. Se due chiavi hanno lo stesso valore di hash si ha una **collisione**. Una funzione di hash è **buona** se genera poche collisioni ed è veloce da calcolare.

La si scompone in due fasi:

![[ASD-p411-1.png]]

1. la **codifica di hash** (*hash code*) porta un oggetto qualsiasi in un **intero** (anche negativo, anche enorme);
2. la **funzione di compressione** porta quell'intero nell'intervallo $[0, N-1]$.

Vantaggio: la codifica non dipende dalla dimensione della tabella, quindi è riusabile con tabelle di ogni dimensione (anche ridimensionate dinamicamente); solo la compressione dipende da $N$.

#### Codifiche di hash

L'obiettivo è evitare collisioni già nei codici, perché la compressione non può separare due chiavi con lo stesso codice.

**Stringa di bit come intero.** Per tipi rappresentati con al massimo 32 bit (Java usa codici di hash a 32 bit) basta interpretare i bit come intero: cast a `int` per `byte`, `short`, `int`, `char`; `Float.floatToIntBits(x)` per `float`. Per tipi più lunghi (`long`, `double`) usare solo metà dei bit ignorerebbe informazione: meglio **combinare** le parti, sommandole (ignorando l'overflow) o facendone lo **xor**. In generale, vedendo $x$ come $(x_0, \dots, x_{n-1})$ interi a 32 bit: $\sum_i x_i$ oppure $x_0 \oplus x_1 \oplus \dots \oplus x_{n-1}$.

**Codifiche di hash polinomiali.** Somma e xor sono pessime quando conta l'**ordine** delle componenti (stringhe): sommando i codici dei caratteri collidono tutti gli anagrammi, come "tempoi" e "tempio" (l'esempio della traduzione italiana) oppure "stop", "tops", "pots", "spot". Si sceglie una costante $a \ne 0, 1$ e si usa

$$x_0 a^{n-1} + x_1 a^{n-2} + \dots + x_{n-2} a + x_{n-1}$$

calcolato con la **regola di Horner**: $x_{n-1} + a(x_{n-2} + a(x_{n-3} + \dots + a(x_1 + a x_0)\dots))$. Le potenze diverse distribuiscono l'influenza di ogni componente. Gli overflow si ignorano (conviene che $a$ abbia bit bassi non nulli). Sperimentalmente $a = 33, 37, 39, 41$ danno meno di 7 collisioni su oltre 50 000 parole inglesi.

**Codifiche di hash per scorrimento ciclico.** Al posto della moltiplicazione per $a$ si fa uno **scorrimento ciclico** della somma parziale: ad esempio ruotare di 5 bit `00111101100101101010100010101000` dà `10110010110101010001010100000111` (i 5 bit di sinistra passano in fondo). Non ha un significato aritmetico ma mescola bene i bit.

```java
static int hashCode(String s) {
  int h = 0;
  for (int i = 0; i < s.length(); i++) {
    h = (h << 5) | (h >>> 27);   // scorrimento ciclico di 5 posizioni
    h += (int) s.charAt(i);      // aggiunge il carattere
  }
  return h;
}
```

Il valore dello scorrimento conta (esperimento su oltre 230 000 parole inglesi; "Totale" = parole che collidono con almeno un'altra, "Massimo" = parole con lo stesso codice):

| Scorrimento | Totale | Massimo |
|---|---|---|
| 0 | 234 735 | 623 |
| 1 | 165 076 | 43 |
| 2 | 38 471 | 13 |
| 3 | 7 174 | 5 |
| 4 | 1 379 | 3 |
| **5** | **190** | **3** |
| 6 | 502 | 2 |
| 7 | 560 | 2 |
| 8 | 5 546 | 4 |
| 9 | 393 | 3 |
| 10 | 5 194 | 5 |
| 11 | 11 559 | 5 |
| 12 | 822 | 2 |
| 13 | 900 | 4 |
| 14 | 2 001 | 4 |
| 15 | 19 251 | 8 |
| 16 | 211 781 | 37 |

Con scorrimento 0 si ricade nella semplice somma dei caratteri.

#### Codifica di hash in Java

`Object` ha il metodo `hashCode()` (intero a 32 bit); la versione predefinita è spesso basata sull'**indirizzo** dell'oggetto. Regola fondamentale: **oggetti uguali devono avere lo stesso codice di hash**. Se una classe ridefinisce `equals` ([[03 - ASD - Strutture dati fondamentali#Verifica di equivalenza|cap. 3]]) deve ridefinire coerentemente `hashCode`: se `x.equals(y)` allora `x.hashCode() == y.hashCode()`. Altrimenti una mappa non ritroverebbe una chiave equivalente ma distinta.

`String` lo fa in modo eccellente (solo 12 collisioni sulle 230 000 parole); anche le classi involucro definiscono `hashCode`. Per la `SinglyLinkedList` del cap. 3 (uguaglianza elemento per elemento) un codice coerente combina con xor e scorrimento ciclico i codici degli elementi:

```java
public int hashCode() {
  int h = 0;
  for (Node walk = head; walk != null; walk = walk.getNext()) {
    h ^= walk.getElement().hashCode();   // xor bit a bit con il codice dell'elemento
    h = (h << 5) | (h >>> 27);           // scorrimento ciclico di 5 posizioni
  }
  return h;
}
```

> [!warning] Correzione
> Nel libro (sia in `hashCode(String)` sia nel Codice 10.6) lo scorrimento a destra è scritto `(h >> 27)`. `>>` replica il bit di segno: se `h` è negativo entrano bit 1 a sinistra e il risultato **non** è una rotazione ciclica. Serve `>>>` (scorrimento senza segno), come nel codice qui sopra, oppure `Integer.rotateLeft(h, 5)`.

#### Funzioni di compressione

**Metodo della divisione**: $i \mapsto i \bmod N$. Conviene $N$ **primo**: con codici $\{200, 205, 210, \dots, 600\}$ e $N = 100$ ci sono molte collisioni, con $N = 101$ nessuna. Una funzione di hash ben scelta dà a due chiavi diverse probabilità $1/N$ di collidere; ma anche con $N$ primo restano collisioni se i codici hanno uno schema del tipo $pN + q$.

**Metodo MAD** (*Multiply-Add-and-Divide*):

$$i \mapsto \big((a\,i + b) \bmod p\big) \bmod N$$

con $p$ primo maggiore di $N$ e $a, b$ interi casuali in $[0, p-1]$, $a > 0$. Elimina gli schemi ripetitivi e si avvicina a una funzione "buona", in cui due chiavi collidono con probabilità $1/N$, come se fossero gettate a caso nei bucket.

> [!tip] Collegamenti
> Le funzioni di hash **crittografiche** hanno requisiti diversi (irreversibilità, resistenza alle collisioni): vedi [[Funzioni Hash Crittografiche]] e [[Hashing]] (Cybersecurity). L'hashing per l'organizzazione dei file su disco è in [[Hashed File]] (Data Management).

_(libro, pp. 409–416)_

### Schemi di gestione delle collisioni

Le collisioni impediscono di mettere semplicemente $(k, v)$ in $A[h(k)]$.

#### Concatenazione separata

Vedi [[Concatenazione separata]].

Ogni bucket $A[j]$ contiene un **contenitore secondario** (ad esempio una piccola `UnsortedTableMap`) con tutte le voci tali che $h(k) = j$: è la **concatenazione separata** (*separate chaining*).

![[ASD-p417-1.png]]

Tabella di dimensione 13 con 10 chiavi intere e $h(k) = k \bmod 13$: nel bucket 2 ci sono 54, 28, 41; nel 5 c'è 18; nel 10 ci sono 10 e 36; nel 12 ci sono 25, 38, 12, 90.

Un'operazione su un bucket costa quanto la dimensione del bucket. Con una buona funzione di hash la dimensione attesa è $n/N$, quindi le operazioni costano $O(\lceil n/N \rceil)$. Il rapporto

$$\lambda = \frac{n}{N}$$

è il **fattore di carico** (*load factor*); se è limitato da una costante (preferibilmente $< 1$), le operazioni costano $O(1)$ **attesi**.

#### Indirizzamento aperto

Vedi [[Indirizzamento aperto]].

La concatenazione richiede strutture ausiliarie. Se lo spazio conta, con l'**indirizzamento aperto** (*open addressing*) ogni voce sta **direttamente** in una cella dell'array; serve $\lambda \le 1$ e codice più complesso per le collisioni.

**Esplorazione lineare** (*linear probing*): se $A[j]$ con $j = h(k)$ è occupata si prova $A[(j+1) \bmod N]$, poi $A[(j+2) \bmod N]$, … fino a una cella vuota. Anche la ricerca deve esplorare celle consecutive da $A[h(k)]$ finché trova la chiave o una cella vuota.

![[ASD-p418-1.png]]

Inserimento della chiave 15 con $h(k) = k \bmod 11$: $h(15) = 4$, ma le celle 4 (26), 5 (5), 6 (37), 7 (16) sono occupate; servono 4 tentativi prima di trovare libera la cella 8.

**Rimozione**: non si può svuotare la cella. Se dopo l'inserimento di 15 si svuotasse la cella di 37, una ricerca di 15 si fermerebbe sulla cella 6 vuota e fallirebbe. Si mette invece una **sentinella** ("defunta"): le ricerche la **saltano**, mentre `put` ricorda la prima sentinella incontrata per riusarla se la chiave non c'è. Ci si ferma anche tornando alla cella di partenza.

Difetto: l'esplorazione lineare crea **cluster** di celle consecutive occupate (soprattutto oltre metà riempimento), che rallentano le ricerche.

**Esplorazione quadratica** (*quadratic probing*): si provano $A[(h(k) + f(i)) \bmod N]$ con $f(i) = i^2$, $i = 0, 1, 2, \dots$ Evita i cluster di celle consecutive ma crea il **clustering secondario**. Con $N$ primo e tabella piena per meno della metà trova sempre una cella vuota; altrimenti no (esercizio C-10.42).

**Doppio hashing** (*double hashing*): una seconda funzione $h'$ e i tentativi $A[(h(k) + i \cdot h'(k)) \bmod N]$, $i = 1, 2, \dots$; $h'$ non può valere 0, una scelta tipica è $h'(k) = q - (k \bmod q)$ con $q < N$ primo ($N$ primo). Non crea cluster.

Altra variante: $f(i)$ generata da un generatore pseudocasuale inizializzato con i bit del codice di hash (sequenza ripetibile ma "arbitraria").

| Schema | Sequenza di esplorazione | Problema |
|---|---|---|
| Lineare | $h(k), h(k)+1, h(k)+2, \dots$ | cluster primari |
| Quadratica | $h(k), h(k)+1, h(k)+4, h(k)+9, \dots$ | clustering secondario; garanzie solo con $N$ primo e $\lambda < 0{,}5$ |
| Doppio hashing | $h(k)+i\,h'(k)$ | serve una seconda funzione |

#### Fattore di carico, rehashing ed efficienza

Bisogna tenere $\lambda$ sotto 1:

- con la **concatenazione separata**, vicino a 1 le collisioni aumentano: consigliato $\lambda < 0{,}9$ (Java usa $\lambda < 0{,}75$);
- con l'**indirizzamento aperto**, oltre 0,5 i cluster crescono: con esplorazione lineare $\lambda < 0{,}5$.

Quando un inserimento supera la soglia si **ridimensiona** la tabella e si reinseriscono tutte le voci (**rehashing**): i codici di hash restano, ma serve una nuova compressione per la nuova $N$. Conviene una nuova dimensione **prima e circa doppia** (esercizio C-10.32): così il costo del rehashing si **ammortizza** sugli inserimenti, come negli [[07 - ASD - Liste e iteratori#Array dinamici|array dinamici]].

#### Efficienza delle tabelle hash

Con una buona funzione di hash il numero atteso di chiavi per bucket è $\lceil n/N \rceil$, cioè $O(1)$ se $n$ è $O(N)$; il rehashing aggiunge $O(1)$ ammortizzato a `put` e `remove`. Nel caso peggiore (funzione pessima: tutte le chiavi nello stesso bucket) le operazioni diventano lineari.

| Metodo | Lista non ordinata | Tabella hash (atteso) | Tabella hash (caso peggiore) |
|---|---|---|---|
| `get` | $O(n)$ | $O(1)$ | $O(n)$ |
| `put` | $O(n)$ | $O(1)$ | $O(n)$ |
| `remove` | $O(n)$ | $O(1)$ | $O(n)$ |
| `size`, `isEmpty` | $O(1)$ | $O(1)$ | $O(1)$ |
| `entrySet`, `keySet`, `values` | $O(n)$ | $O(n)$ | $O(n)$ |

#### Un aneddoto relativo a hashing e sicurezza informatica

Nel 2003 alcuni ricercatori osservarono che il caso peggiore delle tabelle hash permette un attacco **DoS** (*denial of service*): con una funzione di hash deterministica si possono precalcolare tante stringhe corte con lo **stesso codice a 32 bit** (con tutti gli schemi visti, tranne il doppio hashing, chiavi con lo stesso codice sono indistinguibili nella risoluzione delle collisioni). Quasi tutti considerarono il rischio trascurabile (tranne gli sviluppatori di Perl, che lo corressero subito). A fine 2011 l'attacco fu dimostrato sui server web: i parametri di un URL (`?key1=val1&key2=val2…`) vengono messi in una tabella hash; se tutte le chiavi collidono gli inserimenti diventano **quadratici** e il server si blocca. Nel 2012 OpenJDK introdusse una funzione di hash con componente **casuale** per le stringhe (disabilitata di default in Java SE 7, attiva in Java SE 8).

_(libro, pp. 416–421)_

### Implementazione di tabella hash in Java

La classe astratta `AbstractHashMap` (che estende `AbstractMap`) non decide come sono fatti i bucket, ma fornisce la compressione **MAD con parametri casuali** e il **ridimensionamento** automatico. Le sottoclassi implementano:

| Metodo astratto | Compito |
|---|---|
| `createTable()` | crea una tabella vuota di lunghezza `capacity` |
| `bucketGet(h, k)` | come `get`, sapendo che $k$ va nel bucket $h$ |
| `bucketPut(h, k, v)` | come `put` nel bucket $h$ (e aggiorna `n`) |
| `bucketRemove(h, k)` | come `remove` nel bucket $h$ (e aggiorna `n`) |
| `entrySet()` | scandisce tutte le voci |

Il fattore di carico è tenuto $\le 0{,}5$: oltre, la capacità diventa $2N - 1$. Partendo da 17 le capacità sono 17, 33, 65, … cioè $2^k + 1$: per semplicità **non** sono numeri primi, anche se il paragrafo sul rehashing consiglia dimensioni prime.

```java
public abstract class AbstractHashMap<K,V> extends AbstractMap<K,V> {
  protected int n = 0;           // numero di voci
  protected int capacity;        // lunghezza della tabella
  private int prime;             // fattore primo
  private long scale, shift;     // parametri del MAD
  public AbstractHashMap(int cap, int p) {
    prime = p;
    capacity = cap;
    Random rand = new Random();
    scale = rand.nextInt(prime-1) + 1;
    shift = rand.nextInt(prime);
    createTable();
  }
  public AbstractHashMap(int cap) { this(cap, 109345121); }   // primo predefinito
  public AbstractHashMap() { this(17); }                      // capacità predefinita
  // metodi pubblici
  public int size() { return n; }
  public V get(K key) { return bucketGet(hashValue(key), key); }
  public V remove(K key) { return bucketRemove(hashValue(key), key); }
  public V put(K key, V value) {
    V answer = bucketPut(hashValue(key), key, value);
    if (n > capacity / 2)                 // fattore di carico <= 0.5
      resize(2 * capacity - 1);           // (o un primo vicino)
    return answer;
  }
  // metodi ausiliari
  private int hashValue(K key) {
    return (int) ((Math.abs(key.hashCode()*scale + shift) % prime) % capacity);
  }
  private void resize(int newCap) {
    ArrayList<Entry<K,V>> buffer = new ArrayList<>(n);
    for (Entry<K,V> e : entrySet())
      buffer.add(e);
    capacity = newCap;
    createTable();                        // con la nuova capacità
    n = 0;                                // verrà ricalcolato reinserendo
    for (Entry<K,V> e : buffer)
      put(e.getKey(), e.getValue());
  }
  // metodi astratti
  protected abstract void createTable();
  protected abstract V bucketGet(int h, K k);
  protected abstract V bucketPut(int h, K k, V v);
  protected abstract V bucketRemove(int h, K k);
}
```

#### Concatenazione separata

`ChainHashMap` usa come bucket delle `UnsortedTableMap`: risolvere un problema complicato usando la soluzione di uno più semplice si chiama **bootstrapping**. I bucket si creano **solo quando servono** (le celle restano `null` finché nessuna chiave ci finisce). `n` cambia solo se la dimensione del bucket cambia (un `put` su chiave esistente non aumenta le voci).

```java
public class ChainHashMap<K,V> extends AbstractHashMap<K,V> {
  private UnsortedTableMap<K,V>[] table;   // array di bucket
  public ChainHashMap() { super(); }
  public ChainHashMap(int cap) { super(cap); }
  public ChainHashMap(int cap, int p) { super(cap, p); }
  protected void createTable() {
    table = (UnsortedTableMap<K,V>[]) new UnsortedTableMap[capacity];
  }
  protected V bucketGet(int h, K k) {
    UnsortedTableMap<K,V> bucket = table[h];
    if (bucket == null) return null;
    return bucket.get(k);
  }
  protected V bucketPut(int h, K k, V v) {
    UnsortedTableMap<K,V> bucket = table[h];
    if (bucket == null)
      bucket = table[h] = new UnsortedTableMap<>();
    int oldSize = bucket.size();
    V answer = bucket.put(k, v);
    n += (bucket.size() - oldSize);       // la dimensione può essere aumentata
    return answer;
  }
  protected V bucketRemove(int h, K k) {
    UnsortedTableMap<K,V> bucket = table[h];
    if (bucket == null) return null;
    int oldSize = bucket.size();
    V answer = bucket.remove(k);
    n -= (oldSize - bucket.size());       // la dimensione può essere diminuita
    return answer;
  }
  public Iterable<Entry<K,V>> entrySet() {
    ArrayList<Entry<K,V>> buffer = new ArrayList<>();
    for (int h = 0; h < capacity; h++)
      if (table[h] != null)
        for (Entry<K,V> entry : table[h].entrySet())
          buffer.add(entry);
    return buffer;
  }
}
```

Con una buona funzione di hash e $n = O(N)$ i bucket hanno dimensione attesa $O(1)$: `get`, `put`, `remove` sono $O(1)$ attesi; `entrySet` (e quindi `keySet`, `values`) è $O(n + N)$.

#### Esplorazione lineare

`ProbeHashMap` usa l'indirizzamento aperto con esplorazione lineare e la sentinella `DEFUNCT` per le celle svuotate. Il cuore è `findSlot(h, k)`:

- cerca la chiave $k$ partendo dalla cella $h$, saltando le sentinelle e fermandosi a una cella **veramente vuota** (o tornando al punto di partenza);
- se trova $k` restituisce il suo indice $j \ge 0$;
- altrimenti restituisce $-(a + 1)$, dove $a$ è la **prima** cella disponibile (vuota o sentinella) incontrata, che è il posto per inserire.

```java
public class ProbeHashMap<K,V> extends AbstractHashMap<K,V> {
  private MapEntry<K,V>[] table;                                 // tutte null all'inizio
  private MapEntry<K,V> DEFUNCT = new MapEntry<>(null, null);    // sentinella
  public ProbeHashMap() { super(); }
  public ProbeHashMap(int cap) { super(cap); }
  public ProbeHashMap(int cap, int p) { super(cap, p); }
  protected void createTable() {
    table = (MapEntry<K,V>[]) new MapEntry[capacity];
  }
  /** true se la cella è vuota o contiene la sentinella. */
  private boolean isAvailable(int j) {
    return (table[j] == null || table[j] == DEFUNCT);
  }
  /** Indice della chiave, oppure -(a+1) dove a è dove si può inserire k. */
  private int findSlot(int h, K k) {
    int avail = -1;                            // nessuna cella disponibile ancora
    int j = h;                                 // indice durante la scansione
    do {
      if (isAvailable(j)) {                    // vuota o sentinella
        if (avail == -1) avail = j;            // prima cella disponibile
        if (table[j] == null) break;           // vuota: la ricerca fallisce
      } else if (table[j].getKey().equals(k))
        return j;                              // trovata
      j = (j+1) % capacity;                    // prossima cella (circolare)
    } while (j != h);                          // fermati se torni all'inizio
    return -(avail + 1);                       // ricerca fallita
  }
  protected V bucketGet(int h, K k) {
    int j = findSlot(h, k);
    if (j < 0) return null;                    // non trovata
    return table[j].getValue();
  }
  protected V bucketPut(int h, K k, V v) {
    int j = findSlot(h, k);
    if (j >= 0)                                // chiave trovata
      return table[j].setValue(v);
    table[-(j+1)] = new MapEntry<>(k, v);      // riconverte j nell'indice
    n++;
    return null;
  }
  protected V bucketRemove(int h, K k) {
    int j = findSlot(h, k);
    if (j < 0) return null;                    // niente da rimuovere
    V answer = table[j].getValue();
    table[j] = DEFUNCT;                        // cella disattivata
    n--;
    return answer;
  }
  public Iterable<Entry<K,V>> entrySet() {
    ArrayList<Entry<K,V>> buffer = new ArrayList<>();
    for (int h = 0; h < capacity; h++)
      if (!isAvailable(h)) buffer.add(table[h]);
    return buffer;
  }
}
```

Il valore $-(a+1)$ (e non $-a$) serve a distinguere il caso $a = 0$ da una chiave trovata all'indice 0.

_(libro, pp. 421–427)_

---

## Mappe ordinate

Vedi [[Mappa ordinata]].

La mappa normale fa solo **ricerche esatte**. La **mappa ordinata** (*sorted map*) aggiunge:

| Metodo | Restituisce |
|---|---|
| `firstEntry()` | la voce con chiave minima (`null` se vuota) |
| `lastEntry()` | la voce con chiave massima |
| `ceilingEntry(k)` | la voce con la minima chiave $\ge k$ |
| `floorEntry(k)` | la voce con la massima chiave $\le k$ |
| `lowerEntry(k)` | la voce con la massima chiave $< k$ |
| `higherEntry(k)` | la voce con la minima chiave $> k$ |
| `subMap(k1, k2)` | le voci con chiave $\ge k_1$ e $< k_2$ |

(In Java sono in `java.util.NavigableMap`, che estende `SortedMap`.) Esempio: eventi passati (transazioni) indicizzati per **time stamp**: una mappa normale ritrova un evento dato l'istante esatto, ma non sa elencare gli eventi in ordine né trovare quelli **vicini** a un istante; le tabelle hash anzi **sparpagliano** apposta chiavi simili.

### Tabelle di ricerca ordinate

La **tabella di ricerca ordinata** (*sorted search table*) memorizza le voci in un array **ordinato per chiave**: spazio $O(n)$ e soprattutto la possibilità di usare la **ricerca binaria**.

![[ASD-p428-1.png]]

Una mappa come tabella ordinata (solo le chiavi): 2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37 negli indici 0–15.

#### Ricerca binaria e ricerca di corrispondenze non esatte

La [[05 - ASD - Ricorsione#Ricerca binaria|ricerca binaria]] del cap. 5 restituiva `true`/`false`. Qui restituisce un **indice**: in caso di successo quello della chiave, altrimenti la posizione in cui la chiave **andrebbe inserita** (individuando così le chiavi immediatamente minore e maggiore). `findIndex(k)` restituisce l'indice della voce più a sinistra con chiave $\ge k$ (o `high + 1` se non ce n'è).

```java
public class SortedTableMap<K,V> extends AbstractSortedMap<K,V> {
  private ArrayList<MapEntry<K,V>> table = new ArrayList<>();
  public SortedTableMap() { super(); }
  public SortedTableMap(Comparator<K> comp) { super(comp); }
  /** Minimo indice in table[low..high] con chiave >= key (altrimenti high+1). */
  private int findIndex(K key, int low, int high) {
    if (high < low) return high + 1;           // niente da esaminare
    int mid = (low + high) / 2;
    int comp = compare(key, table.get(mid));
    if (comp == 0)
      return mid;                              // corrispondenza esatta
    else if (comp < 0)
      return findIndex(key, low, mid - 1);     // se c'è, è a sinistra di mid
    else
      return findIndex(key, mid + 1, high);    // se c'è, è a destra di mid
  }
  private int findIndex(K key) { return findIndex(key, 0, table.size() - 1); }

  public int size() { return table.size(); }
  public V get(K key) {
    int j = findIndex(key);
    if (j == size() || compare(key, table.get(j)) != 0) return null;   // non c'è
    return table.get(j).getValue();
  }
  public V put(K key, V value) {
    int j = findIndex(key);
    if (j < size() && compare(key, table.get(j)) == 0)   // chiave presente
      return table.get(j).setValue(value);
    table.add(j, new MapEntry<K,V>(key, value));          // inserisce al posto giusto
    return null;
  }
  public V remove(K key) {
    int j = findIndex(key);
    if (j == size() || compare(key, table.get(j)) != 0) return null;
    return table.remove(j).getValue();
  }
  /** La voce di indice j, o null se j non è valido. */
  private Entry<K,V> safeEntry(int j) {
    if (j < 0 || j >= table.size()) return null;
    return table.get(j);
  }
  public Entry<K,V> firstEntry() { return safeEntry(0); }
  public Entry<K,V> lastEntry() { return safeEntry(table.size()-1); }
  public Entry<K,V> ceilingEntry(K key) {
    return safeEntry(findIndex(key));
  }
  public Entry<K,V> floorEntry(K key) {
    int j = findIndex(key);
    if (j == size() || !key.equals(table.get(j).getKey()))
      j--;                                     // un posto indietro se non è esatta
    return safeEntry(j);
  }
  public Entry<K,V> lowerEntry(K key) {
    return safeEntry(findIndex(key) - 1);      // subito a sinistra del ceiling
  }
  public Entry<K,V> higherEntry(K key) {
    int j = findIndex(key);
    if (j < size() && key.equals(table.get(j).getKey()))
      j++;                                     // a destra della corrispondenza esatta
    return safeEntry(j);
  }
  // iteratori snapshot per entrySet() e subMap()
  private Iterable<Entry<K,V>> snapshot(int startIndex, K stop) {
    ArrayList<Entry<K,V>> buffer = new ArrayList<>();
    int j = startIndex;
    while (j < table.size() && (stop == null || compare(stop, table.get(j)) > 0))
      buffer.add(table.get(j++));
    return buffer;
  }
  public Iterable<Entry<K,V>> entrySet() { return snapshot(0, null); }
  public Iterable<Entry<K,V>> subMap(K fromKey, K toKey) {
    return snapshot(findIndex(fromKey), toKey);
  }
}
```

#### Analisi

| Metodo | Tempo |
|---|---|
| `size` | $O(1)$ |
| `get` | $O(\log n)$ |
| `put` | $O(n)$; $O(\log n)$ se la chiave c'è già |
| `remove` | $O(n)$ |
| `firstEntry`, `lastEntry` | $O(1)$ |
| `ceilingEntry`, `floorEntry`, `lowerEntry`, `higherEntry` | $O(\log n)$ |
| `subMap` | $O(s + \log n)$ con $s$ voci restituite |
| `entrySet`, `keySet`, `values` | $O(n)$ |

Le ricerche fanno una sola ricerca binaria ($O(\log n)$, [[05 - ASD - Ricorsione#Effettuare una ricerca binaria|Proposizione 5.2]]) più lavoro costante; `subMap` fa una ricerca binaria e poi $O(1)$ per ogni voce dell'intervallo. Inserimenti e rimozioni devono invece **far scorrere** gli elementi (`table.add`/`table.remove` di un `ArrayList`): $O(n)$. Le tabelle ordinate vanno bene quando ci sono **molte ricerche e pochi aggiornamenti**.

_(libro, pp. 427–432)_

### Due applicazioni di mappe ordinate

#### Una base di dati per voli aerei

Un sito di prenotazione cerca voli per (partenza, arrivo, data, ora). Si usa una mappa ordinata con chiavi `Flight` = quadrupla $k = (\text{partenza}, \text{arrivo}, \text{data}, \text{ora})$ ordinate **lessicograficamente**; il valore contiene numero di volo, posti in prima (F) e in turistica (Y), durata, prezzo. L'utente non vuole una corrispondenza esatta sull'orario: `ceilingEntry(k)` trova il primo volo dalla data/ora richiesta in poi, e `subMap(k1, k2)` tutti i voli di una fascia oraria. Ad esempio con $k_1 = $ (ORD, PVD, 05May, 09:30) e $k_2 = $ (ORD, PVD, 05May, 20:00):

```
(ORD, PVD, 05May, 09:53) : (AA 1840, F5, Y15, 02:05, $251)
(ORD, PVD, 05May, 13:29) : (AA 600,  F2, Y0,  02:16, $713)
(ORD, PVD, 05May, 17:39) : (AA 416,  F3, Y9,  02:09, $365)
(ORD, PVD, 05May, 19:50) : (AA 1828, F9, Y25, 02:13, $186)
```

#### Insieme dei massimi (maxima set)

Compromessi costo/prestazione: ad esempio auto con coppie (costo, velocità massima); si vuole l'auto più veloce che si può comprare con un budget $d$. Una coppia $(a, b)$ **domina** $(c, d) \ne (a, b)$ se $a \le c$ e $b \ge d$ (costa non di più e va almeno altrettanto). Una coppia è un **massimo** se nessuna la domina.

![[ASD-p433-1.png]]

Le coppie come punti (costo in ascissa, prestazione in ordinata): $p$ domina $c$, $d$, $e$ (stanno in basso a destra di $p$), ma non $a$, $b$ (costano meno) né $f$, $g$, $h$ (vanno più forte). Aggiungendo $p$ si possono eliminare $c$, $d$, $e$.

**Gestire un insieme dei massimi usando una mappa ordinata**: si memorizzano solo i massimi in una mappa ordinata **chiave = costo, valore = prestazione**. Tra i massimi, ordinati per costo crescente, anche la prestazione è crescente.

```java
/** Base di dati di coppie massime (costo, prestazione). */
public class CostPerformanceDatabase {
  SortedMap<Integer,Integer> map = new SortedTableMap<>();
  public CostPerformanceDatabase() { }
  /** La coppia con prestazione massima e costo <= cost (null se non c'è). */
  public Entry<Integer,Integer> best(int cost) {
    return map.floorEntry(cost);
  }
  /** Aggiunge la coppia (c, p). */
  public void add(int c, int p) {
    Entry<Integer,Integer> other = map.floorEntry(c);   // costo <= c
    if (other != null && other.getValue() >= p)          // va almeno altrettanto
      return;                                            // (c,p) è dominata
    map.put(c, p);
    // rimuove le coppie dominate dalla nuova
    other = map.higherEntry(c);                          // costo > c
    while (other != null && other.getValue() <= p) {     // velocità non maggiore
      map.remove(other.getKey());
      other = map.higherEntry(c);
    }
  }
}
```

- `best(c)` è un `floorEntry(c)`: tra i massimi con costo $\le c$ l'ultimo è il più veloce.
- `add(c, p)`: se la coppia con costo immediatamente $\le c$ è almeno altrettanto veloce, $(c, p)$ è dominata e si ignora; altrimenti la si inserisce e si eliminano le coppie successive (più care) che non sono più veloci.

Con `SortedTableMap`, `add` è $O(n)$ nel caso peggiore; con una **skip list** `best` costa $O(\log n)$ atteso e `add` $O((1 + r)\log n)$ atteso, dove $r$ è il numero di voci rimosse.

> [!note] Riferimento
> Il libro dice che la skip list verrà descritta "nel prossimo capitolo": in realtà è il prossimo **paragrafo** ([[#Skip list|10.4]]).

_(libro, pp. 432–434)_

---

## Skip list

Vedi [[Skip list]].

La tabella ordinata cerca in $O(\log n)$ ma aggiorna in $O(n)$; una lista concatenata aggiorna in $O(1)$ (una volta trovata la posizione) ma non permette la ricerca binaria (non ha accesso per indice). La **skip list** è un compromesso intelligente, efficiente sia nelle ricerche sia negli aggiornamenti (Java: `java.util.concurrent.ConcurrentSkipListMap`).

Una skip list $S$ per una mappa $M$ è una serie di liste $\{S_0, S_1, \dots, S_h\}$; ogni $S_i$ contiene un sottoinsieme delle voci di $M$ **ordinate per chiave**, più due sentinelle con chiavi $-\infty$ e $+\infty$. Inoltre:

- $S_0$ contiene **tutte** le voci di $M$;
- per $i = 1, \dots, h-1$, $S_i$ contiene un sottoinsieme **casuale** delle voci di $S_{i-1}$;
- $S_h$ contiene solo le sentinelle.

$h$ è l'**altezza** di $S$.

![[ASD-p435-1.png]]

Una skip list con 10 chiavi (12, 17, 20, 25, 31, 38, 39, 44, 50, 55) in $S_0$: $S_1$ contiene 12, 17, 25, 31, 44, 55; $S_2$ contiene 17, 25, 31, 55; $S_3$ contiene 17, 25, 55; $S_4$ contiene 17; $S_5$ solo le sentinelle.

Idealmente $S_{i+1}$ conterrebbe una voce sì e una no di $S_i$, ma questo non si impone: ogni voce di $S_i$ entra in $S_{i+1}$ con probabilità $1/2$, come se si **lanciasse una moneta**. Quindi ci si aspetta circa $n/2$ voci in $S_1$, $n/4$ in $S_2$, $n/2^i$ in $S_i$, e altezza circa $\log n$.

I numeri casuali vengono da generatori pseudocasuali (con seme, come `java.util.Random` del [[03 - ASD - Strutture dati fondamentali#Generazione di numeri pseudocasuali|cap. 3]]) o da dispositivi hardware; nell'analisi si suppone che siano abbastanza casuali. La casualità dà strutture **semplici** ed efficienti: ricerca **e** aggiornamenti in tempo $O(\log n)$ **atteso**. Il valore atteso non dipende dalla distribuzione delle chiavi ma solo dalle scelte casuali fatte negli inserimenti.

Una skip list si vede come una griglia di posizioni: i **livelli** (orizzontali, le liste $S_i$) e le **torri** (verticali, le copie della stessa voce in liste consecutive). Navigazione:

| Metodo | Restituisce |
|---|---|
| `next(p)` | la posizione dopo $p$ sullo stesso livello |
| `prev(p)` | la posizione prima di $p$ sullo stesso livello |
| `above(p)` | la posizione sopra $p$ nella stessa torre |
| `below(p)` | la posizione sotto $p$ nella stessa torre |

(`null` se non esiste). Si implementa con liste doppiamente concatenate per i livelli e per le torri: ogni metodo è $O(1)$.

### Operazioni di ricerca e modifica in una skip list

Tutto si basa su `SkipSearch(k)`, che trova in $S_0$ la posizione della voce con la **massima chiave $\le k$** (eventualmente $-\infty$).

#### Ricerca in una skip list

Si parte dalla **posizione iniziale** $s$ (la sentinella $-\infty$ di $S_h$, in alto a sinistra) e:

1. se `below(p)` è `null` si è arrivati al fondo e $p$ è la risposta; altrimenti si scende: `p = below(p)`;
2. si avanza a destra finché la chiave successiva è $\le k$ (**scansione in avanti**); può darsi che $p$ resti dov'è;
3. si torna al passo 1.

![[ASD-p437-1.png]]

Ricerca della chiave 50: da $-\infty$ in $S_5$ si scende in $S_4$ e si avanza a 17 (il successivo è $+\infty$); si scende in $S_3$ e si avanza a 25 (55 è troppo); in $S_2$ si avanza a 31; in $S_1$ a 44; in $S_0$ a 50, dove ci si ferma perché 55 > 50. Le posizioni evidenziate sono quelle esaminate.

```
Algorithm SkipSearch(k):
  Input: una chiave k
  Output: la posizione p in S0 con la massima chiave <= k
  p = s                          { posizione iniziale }
  while below(p) != null do
    p = below(p)                 { scende }
    while k >= key(next(p)) do
      p = next(p)                { avanza }
  return p
```

`get(k)` = `SkipSearch(k)` e confronto della chiave trovata con $k$. Il tempo atteso è $O(\log n)$ (dimostrazione sotto); dalla posizione trovata si implementano anche `ceilingEntry`, `subMap`, ecc.

#### Inserimento in una skip list

`put(k, v)`: si chiama `SkipSearch(k)`; se la chiave c'è si sostituisce il valore. Altrimenti si inserisce $(k, v)$ subito dopo $p$ in $S_0$ e si decide **a caso l'altezza della torre**: si lancia una moneta; se esce croce ci si ferma, se esce testa si inserisce la voce anche nel livello superiore (al posto giusto) e si rilancia. In Java un lancio equo è `new Random().nextBoolean()`.

```
Algorithm SkipInsert(k, v):
  Input: una chiave k e un valore v
  Output: la posizione più alta della torre della nuova voce
  p = SkipSearch(k)            { posizione in S0 della massima chiave <= k }
  q = null                     { posizione corrente nella torre della nuova voce }
  i = -1                       { altezza corrente della torre }
  repeat
    i = i + 1
    if i >= h then
      h = h + 1                { nuovo livello in cima alla skip list }
      t = next(s)
      s = insertAfterAbove(null, s, (-inf, null))   { alza la torre sinistra }
      insertAfterAbove(s, t, (+inf, null))          { alza la torre destra }
    q = insertAfterAbove(p, q, (k, v))              { alza la torre della nuova voce }
    while above(p) == null do
      p = prev(p)              { torna indietro sul livello }
    p = above(p)               { sale di un livello }
  until coinFlip() == tails
  n = n + 1
  return q
```

`insertAfterAbove(p, q, e)` crea una posizione con la voce $e$ dopo $p$ (sullo stesso livello) e sopra $q$, sistemando i collegamenti `next`, `prev`, `above`, `below`.

![[ASD-p439-1.png]]

Inserimento della chiave 42 con tre "testa" e poi "croce": la torre di 42 (tratto più spesso) arriva a $S_3$. Le bandierine indicano le posizioni $p$ dopo cui viene inserita la nuova voce a ogni livello (39 in $S_0$, 31 in $S_1$ e $S_2$, 25 in $S_3$), trovate tornando indietro finché esiste una posizione sopra.

#### Rimozione da una skip list

`remove(k)`: `SkipSearch(k)`; se la chiave non c'è si restituisce `null`, altrimenti si rimuove la posizione trovata e **tutte quelle sopra** (salendo con `above`), ricollegando i vicini orizzontali a ogni livello (pseudocodice nell'esercizio R-10.24). Tempo atteso $O(\log n)$.

![[ASD-p440-1.png]]

Rimozione della chiave 25 dalla skip list precedente: le posizioni della sua torre (tratteggiate) vengono eliminate in tutti i livelli da $S_0$ a $S_3$, e i vicini vengono collegati direttamente.

**Ottimizzazioni** (solo fattori costanti, ma utili in pratica):

- sopra $S_0$ servono solo le chiavi: una torre può essere un unico oggetto con una coppia chiave-valore e $j$ riferimenti avanti e indietro se arriva a $S_j$;
- le liste orizzontali possono essere **semplicemente** concatenate (solo `next`), perché inserimenti e rimozioni procedono dall'alto in basso e da sinistra a destra (esercizio C-10.55).

Sperimentalmente le skip list ottimizzate sono più veloci degli alberi AVL e di altri alberi bilanciati del [[11 - ASD - Alberi di ricerca|cap. 11]].

#### Gestione del livello più alto

Cosa fare se un inserimento vuole salire oltre il livello più alto? Due strategie:

- fissare un'altezza massima in funzione di $n$, ad esempio $h = \max\{10, 2\lceil\log n\rceil\}$ (o più sicuro $3\lceil\log n\rceil$), fermando la torre al livello massimo (salvo quando $\lceil\log n\rceil < \lceil\log(n+1)\rceil$, perché il limite sta per crescere);
- lasciar crescere la torre finché esce testa (è ciò che fa `SkipInsert`): la probabilità di superare $O(\log n)$ livelli è bassissima.

Entrambe danno tempo atteso $O(\log n)$ per ricerca, inserimento e rimozione.

### Analisi probabilistica delle prestazioni di una skip list

Nel **caso peggiore** la skip list non è interessante: se ogni torre arrivasse in cima, `get`, `put`, `remove` costerebbero $O(n + h)$ (e senza limite all'altezza un inserimento potrebbe crescere a lungo, anche se la probabilità di "testa per sempre" è zero). Ma è un caso estremamente improbabile: serve un'analisi probabilistica, che qui è informale.

#### Un limite superiore per l'altezza di una skip list

Una data voce ha una torre di altezza $\ge i$ con probabilità $1/2^i$ ($i$ teste di fila). La probabilità $P_i$ che il livello $i$ contenga almeno una posizione è al massimo la somma su tutte le $n$ voci (**union bound**):

$$P_i \le \frac{n}{2^i}$$

L'altezza supera $i$ con probabilità al massimo $P_i$. Ad esempio

$$P(h > 3\log n) \le P_{3\log n} \le \frac{n}{2^{3\log n}} = \frac{n}{n^3} = \frac{1}{n^2}$$

(con $n = 1000$, uno su un milione). In generale per $c > 1$: $P(h > c\log n) \le 1/n^{c-1}$. Quindi **con alta probabilità** l'altezza è $O(\log n)$.

#### Analisi del tempo d'esecuzione di una ricerca in una skip list

La ricerca ha due cicli: quello esterno scende (al massimo $h$ volte, cioè $O(\log n)$ con alta probabilità) e quello interno avanza. Sia $n_i$ il numero di chiavi esaminate avanzando al livello $i$. Dopo la posizione di partenza, ogni chiave esaminata al livello $i$ **non** può appartenere anche al livello $i+1$ (altrimenti la si sarebbe incontrata al livello sopra): ogni chiave "conta" con probabilità $1/2$, quindi il numero atteso di passi in avanti è il numero atteso di lanci prima di una testa, cioè **2**. Tempo atteso $O(1)$ per livello per $O(\log n)$ livelli: ricerca in **$O(\log n)$ atteso**. Analogamente inserimento e rimozione.

#### Utilizzo dello spazio in una skip list

Il numero atteso di posizioni al livello $i$ è $n/2^i$, quindi in totale

$$\sum_{i=0}^{h} \frac{n}{2^i} = n \sum_{i=0}^{h} \frac{1}{2^i}, \qquad \sum_{i=0}^{h}\frac{1}{2^i} = \frac{(1/2)^{h+1} - 1}{1/2 - 1} = 2\left(1 - \frac{1}{2^{h+1}}\right) < 2$$

(somma geometrica, [[04 - ASD - Analisi di algoritmi#Somme geometriche|Proposizione 4.5]]). Spazio atteso **$O(n)$**.

| Metodo | Tempo |
|---|---|
| `size`, `isEmpty` | $O(1)$ |
| `get` | $O(\log n)$ atteso |
| `put` | $O(\log n)$ atteso |
| `remove` | $O(\log n)$ atteso |
| `firstEntry`, `lastEntry` | $O(1)$ |
| `ceilingEntry`, `floorEntry`, `lowerEntry`, `higherEntry` | $O(\log n)$ atteso |
| `subMap` | $O(s + \log n)$ atteso, con $s$ voci |
| `entrySet`, `keySet`, `values` | $O(n)$ |

_(libro, pp. 435–443)_

---

## Insiemi, multi-insiemi e multi-mappe

Vedi [[Insiemi, multi-insiemi e multi-mappe]].

Tre astrazioni vicine alla mappa:

- un **insieme** (*set*): raccolta non ordinata **senza duplicati**, con verifica di appartenenza (*membership test*) efficiente;
- un **multi-insieme** (*multiset* o *bag*): come un insieme ma **con duplicati**;
- una **multi-mappa** (*multimap*): come una mappa, ma una chiave può avere **più valori** (es. l'indice analitico di un libro: termine → pagine).

### L'insieme come tipo di dato astratto

`java.util.Set` ha i metodi fondamentali:

| Metodo | Effetto |
|---|---|
| `add(e)` | aggiunge $e$ (se non c'è) |
| `remove(e)` | rimuove $e$ (se c'è) |
| `contains(e)` | `true` se $e$ appartiene all'insieme |
| `iterator()` | iteratore sugli elementi |

e le operazioni insiemistiche, che modificano l'insieme $S$ su cui sono invocate:

| Metodo | Operazione |
|---|---|
| `addAll(T)` | $S \leftarrow S \cup T = \{e : e \in S \text{ oppure } e \in T\}$ |
| `retainAll(T)` | $S \leftarrow S \cap T = \{e : e \in S \text{ e } e \in T\}$ |
| `removeAll(T)` | $S \leftarrow S - T = \{e : e \in S \text{ e } e \notin T\}$ |

Con il [[02 - ASD - Progettazione orientata agli oggetti#Classi astratte|template method]] si implementano usando solo i metodi fondamentali (come fa `java.util.AbstractSet`):

```java
public void addAll(Set<E> other) {
  for (E element : other)    // usa l'iteratore di other
    add(element);            // add ignora i duplicati
}
```

(`retainAll` richiede attenzione per non rimuovere elementi dall'insieme che si sta scorrendo, esercizio C-10.59.)

#### Insiemi ordinati

Se gli elementi sono confrontabili si ha l'**insieme ordinato** (*sorted set*), con `first()`, `last()`, `ceiling(e)`, `floor(e)`, `lower(e)`, `higher(e)`, `subSet(e1, e2)` (elementi $\ge e_1$ e $< e_2$), `pollFirst()` e `pollLast()` (rimuovono e restituiscono il minimo / il massimo). In Java: `java.util.SortedSet` e `java.util.NavigableSet`.

#### Implementazione di insiemi

Un insieme è una **mappa senza valori**: qualunque struttura per mappe va bene (memorizzando gli elementi come chiavi con valore `null`, o meglio direttamente, senza le entry). In Java:

| Classe | ADT | Struttura |
|---|---|---|
| `java.util.HashSet` | insieme | tabella hash |
| `java.util.concurrent.ConcurrentSkipListSet` | insieme ordinato | skip list |
| `java.util.TreeSet` | insieme ordinato | albero di ricerca bilanciato (cap. 11) |

### Il multi-insieme come tipo di dato astratto

Nel JCF due oggetti sono "uguali" secondo `equals` (es. due esemplari distinti della stringa "October" ritrovano la stessa chiave di una mappa). Per un multi-insieme come $\{a, a, a, a, b, c, c\}$ bisogna decidere se conservare **ogni esemplare** di $a$ o solo il **conteggio** (4). In entrambi i casi si adatta una mappa: chiave = un rappresentante, valore = un contenitore degli esemplari equivalenti oppure un contatore (come nel [[#Applicazione: frequenza delle parole in un testo|conteggio delle parole]]).

Il JCF non ha multi-insiemi; ci sono `Bag`/`SortedBag` in Apache Commons e `Multiset`/`SortedMultiset` in Google Guava (collezioni di elementi con **molteplicità**). L'interfaccia `Multiset` di Guava offre, tra gli altri:

| Metodo | Effetto |
|---|---|
| `add(e)` | aggiunge un'occorrenza di $e$ |
| `contains(e)` | `true` se c'è almeno un elemento uguale a $e$ |
| `count(e)` | numero di occorrenze di $e$ |
| `remove(e)` | rimuove un'occorrenza di $e$ |
| `remove(e, n)` | rimuove $n$ occorrenze di $e$ |
| `size()` | numero di elementi, duplicati compresi |
| `iterator()` | tutti gli elementi, ripetendo quelli multipli |

C'è anche un'`Entry` immutabile (elemento, molteplicità), e `SortedMultiset` aggiunge `firstEntry`, `lastEntry`, ecc.

### Il tipo di dato astratto multi-mappa

Una **multi-mappa** ammette più voci con la stessa chiave $(k, v)$ e $(k, v')$, come un dizionario con più definizioni per una parola. Due rappresentazioni: modificare la struttura per memorizzare voci con chiavi ripetute, oppure (più semplice) una mappa che associa a ogni chiave un **contenitore secondario** dei suoi valori, $k \mapsto \{v, v'\}$. Il JCF non ha multi-mappe; versione semplificata dell'interfaccia `Multimap` di Guava:

| Metodo | Effetto |
|---|---|
| `get(k)` | collezione dei valori associati a $k$ |
| `put(k, v)` | aggiunge $(k, v)$ senza sovrascrivere |
| `remove(k, v)` | rimuove una voce $(k, v)$ |
| `removeAll(k)` | rimuove tutte le voci con chiave $k$ |
| `size()` | numero di voci (contando le associazioni multiple) |
| `entries()` | tutte le voci |
| `keys()` | le chiavi di tutte le voci (con ripetizioni) |
| `keySet()` | le chiavi senza ripetizioni |
| `values()` | tutti i valori |

```java
public class HashMultimap<K,V> {
  Map<K,List<V>> map = new HashMap<>();   // mappa principale
  int total = 0;                          // numero totale di voci
  public HashMultimap() { }
  public int size() { return total; }
  public boolean isEmpty() { return (total == 0); }
  /** Tutti i valori associati alla chiave. */
  public Iterable<V> get(K key) {
    List<V> secondary = map.get(key);
    if (secondary != null)
      return secondary;
    return new ArrayList<>();             // lista vuota
  }
  /** Aggiunge (key, value). */
  public void put(K key, V value) {
    List<V> secondary = map.get(key);
    if (secondary == null) {
      secondary = new ArrayList<>();
      map.put(key, secondary);            // nuova lista secondaria
    }
    secondary.add(value);
    total++;
  }
  /** Rimuove (key, value), se esiste. */
  public boolean remove(K key, V value) {
    boolean wasRemoved = false;
    List<V> secondary = map.get(key);
    if (secondary != null) {
      wasRemoved = secondary.remove(value);
      if (wasRemoved) {
        total--;
        if (secondary.isEmpty())
          map.remove(key);                // toglie la lista vuota
      }
    }
    return wasRemoved;
  }
  /** Rimuove tutte le voci con la chiave data. */
  Iterable<V> removeAll(K key) {
    List<V> secondary = map.get(key);
    if (secondary != null) {
      total -= secondary.size();
      map.remove(key);
    } else
      secondary = new ArrayList<>();      // nessun valore rimosso
    return secondary;
  }
  /** Tutte le voci della multi-mappa. */
  public Iterable<Map.Entry<K,V>> entries() {
    List<Map.Entry<K,V>> result = new ArrayList<>();
    for (Map.Entry<K,List<V>> secondary : map.entrySet()) {
      K key = secondary.getKey();
      for (V value : secondary.getValue())
        result.add(new AbstractMap.SimpleEntry<K,V>(key, value));
    }
    return result;
  }
}
```

_(libro, pp. 444–449)_

---

> [!summary] Riepilogo
> - **Mappa**: voci (chiave unica, valore), `get`/`put`/`remove`, `keySet`/`values`/`entrySet`; lista non ordinata $O(n)$.
> - **Tabella hash**: funzione di hash = **codifica** (bit come intero, somma/xor, **polinomiale** con Horner, **scorrimento ciclico**; `equals` ⇒ stesso `hashCode`) + **compressione** (divisione con $N$ primo, **MAD** $((ai+b) \bmod p) \bmod N$).
> - Collisioni: **concatenazione separata** (bucket = mappe piccole) o **indirizzamento aperto** (lineare con sentinelle `DEFUNCT`, quadratica, doppio hashing). **Fattore di carico** $\lambda = n/N$ basso (0,5 / 0,75 / 0,9), **rehashing** a capacità circa doppia: $O(1)$ atteso, $O(n)$ nel caso peggiore (attacchi DoS per collisioni).
> - **Mappa ordinata**: `first/last/ceiling/floor/lower/higherEntry`, `subMap`. **Tabella ordinata** con ricerca binaria: ricerche $O(\log n)$, aggiornamenti $O(n)$. Applicazioni: voli aerei, insieme dei massimi.
> - **Skip list**: livelli $S_0 \supseteq S_1 \supseteq \dots$ costruiti lanciando monete; `SkipSearch` (scendi e avanza), inserimento con torre casuale, rimozione della torre; altezza $O(\log n)$ con alta probabilità, operazioni $O(\log n)$ **attese**, spazio $O(n)$ atteso.
> - **Insiemi** (unione, intersezione, differenza; ordinati), **multi-insiemi** (molteplicità), **multi-mappe** (chiave → lista di valori).
