## 🌲 Algoritmo di Kruskal (MST)

### 1. Concetto Chiave: La Foresta di Cluster

A differenza di **[[Prim-Jarník]]** (che fa crescere un _unico_ albero a partire da una radice), l'algoritmo di **Kruskal** gestisce una **foresta** di alberi disgiunti (detti "cluster").

- **Inizio:** Ogni vertice è un piccolo albero isolato.
    
- **Processo:** L'algoritmo fonde ("merge") ripetutamente coppie di alberi collegandoli con il lato più leggero disponibile.
    
- **Fine:** Quando tutti i cluster sono fusi in uno solo, abbiamo l'MST.
    

### 2. Strategia Greedy

L'algoritmo segue una logica molto semplice:

1. Prende in esame i lati in ordine di **peso crescente** (dal più leggero al più pesante).
    
2. Per ogni lato $(u, v)$:
    
    - Se $u$ e $v$ appartengono a **cluster diversi** $\rightarrow$ Aggiungi il lato all'MST e **unisci** (Union) i due cluster.
        
    - Se $u$ e $v$ appartengono allo **stesso cluster** $\rightarrow$ Ignora il lato (aggiungerlo creerebbe un ciclo).
        

### 3. Pseudocodice

Snippet di codice

```java
Algoritmo Kruskal(G):
    Input: Un grafo G semplice, connesso e pesato
    Output: Un albero ricoprente minimo T

    // 1. Inizializzazione
    for ogni vertice v in G do
        definisci un cluster elementare C(v) = {v}
    
    crea una coda prioritaria Q contenente tutti i lati di G (chiave = peso)
    inizializza T = insieme vuoto
    
    // 2. Ciclo di unione (fino a n-1 lati)
    while T ha meno di n - 1 lati do
        (u, v) = lato restituito da Q.removeMin()
        
        // Trova i cluster di appartenenza
        ClusterA = find(u)
        ClusterB = find(v)
        
        // Se sono diversi, fondi e aggiungi
        if ClusterA != ClusterB then
            aggiungi il lato (u, v) a T
            unisci (union) ClusterA e ClusterB
    
    return T
```

---

### 💻 Implementazione Java (Codice Unificato)

Il codice sfrutta una struttura dati **Union-Find** (qui chiamata classe `Partition`) per gestire i cluster in modo efficiente.


```java
/**
 * Calcola un MST di un grafo g usando l'algoritmo di Kruskal.
 */
public static <V> PositionalList<Edge<Integer>> MST(Graph<V, Integer> g) {
    
    // 1. Lista Risultato (L'MST finale)
    PositionalList<Edge<Integer>> tree = new LinkedPositionalList<>();
    
    // 2. Coda Prioritaria per i lati (Ordinamento per peso)
    PriorityQueue<Integer, Edge<Integer>> pq = new HeapPriorityQueue<>();
    
    // 3. Struttura "Partition" (Union-Find) per gestire i cluster disgiunti
    Partition<Vertex<V>> forest = new Partition<>();
    
    // 4. Mappa per tracciare la posizione di ogni vertice nella struttura Partition
    Map<Vertex<V>, Position<Vertex<V>>> positions = new ProbeHashMap<>();

    // FASE A: Inizializzazione
    // Ogni vertice crea il proprio gruppo (makeGroup) e mettiamo tutti i lati nella PQ
    for (Vertex<V> v : g.vertices()) {
        positions.put(v, forest.makeGroup(v));
    }

    for (Edge<Integer> e : g.edges()) {
        pq.insert(e.getElement(), e); // Chiave = Peso del lato
    }

    int size = g.numVertices();

    // FASE B: Ciclo Principale (Greedy)
    // Continua finché l'albero non è completo (size - 1 lati) o finiscono i lati
    while (tree.size() != size - 1 && !pq.isEmpty()) {
        
        // Estrai il lato più leggero
        Entry<Integer, Edge<Integer>> entry = pq.removeMin();
        Edge<Integer> edge = entry.getValue();
        Vertex<V>[] endpoints = g.endVertices(edge);
        
        // Trova i rappresentanti dei cluster dei due estremi (FIND operation)
        Position<Vertex<V>> a = forest.find(positions.get(endpoints[0]));
        Position<Vertex<V>> b = forest.find(positions.get(endpoints[1]));
        
        // Se i cluster sono diversi (Niente ciclo)
        if (a != b) {
            tree.addLast(edge);    // Aggiungi all'MST
            forest.union(a, b);    // Fondi i due gruppi (UNION operation)
        }
    }
    
    return tree;
}
```

---

### ⏱️ Analisi della Complessità

La complessità totale è **$O(m \log n)$** (dove $m$ è il numero di lati e $n$ il numero di vertici).

1. **Ordinamento Lati (o PQ):** Inserire/Estrarre tutti i lati dalla Priority Queue costa $O(m \log m)$ o $O(m \log n)$.
    
2. **Operazioni sui Cluster (Union-Find):** Grazie alle euristiche di bilanciamento (Path Compression + Union by Rank), le operazioni `find` e `union` sono quasi costanti (tecnicamente $O(\alpha(n))$, la funzione inversa di Ackermann).
    

Quindi il "collo di bottiglia" è l'ordinamento dei lati: **$O(m \log n)$**.

---

### Iterazione
![[Pasted image 20251125190953.png]]![[Pasted image 20251125190958.png]]![[Pasted image 20251125191008.png]]![[Pasted image 20251125191013.png]]![[Pasted image 20251125191017.png]]![[Pasted image 20251125191021.png]]

## 🧩 Strutture Union-Find (Partizioni Disgiunte)

### 1. Definizione e Scopo

La struttura dati Union-Find (o Disjoint-Set) gestisce una partizione di un universo di elementi in insiemi disgiunti (chiamati cluster).

Ogni elemento appartiene a uno e un solo cluster. Ogni cluster è identificato da un leader (rappresentante).

- **Applicazione Principale:** Algoritmo di Kruskal (per verificare se due nodi sono già connessi e per unire le componenti connesse).
    

### 2. ADT Partizione: Le Operazioni

L'interfaccia astratta prevede tre metodi fondamentali che lavorano su oggetti di tipo `Posizione` (che contengono l'elemento):

- **`makeCluster(x)`:** Crea un nuovo cluster contenente solo l'elemento $x$ e restituisce la sua posizione. (Inizialmente $x$ è il leader di se stesso).
    
- **`find(p)`:** Restituisce la posizione del **leader** del cluster a cui appartiene $p$. (Serve a capire "in che gruppo sto?").
    
- **`union(p, q)`:** Fonde i due cluster che contengono le posizioni $p$ e $q$ in un unico cluster.
    

---

### 3. Implementazione A: Basata su Sequenze
![[Pasted image 20251125191555.png]]

Ogni cluster è una lista/sequenza. Ogni elemento punta all'oggetto "sequenza", che fa da identificatore.

- **Logica `union(A, B)`:** Si spostano tutti gli elementi della sequenza più piccola in quella più grande. Si aggiornano i riferimenti di tutti gli elementi spostati.
    
- **Complessità:**
    
    - `makeCluster`, `find`: $O(1)$.
        
    - `union`: $O(\min(n_p, n_q))$.
        
    - **Analisi Ammortizzata:** Una serie di $k$ operazioni su $n$ elementi costa $O(k + n \log n)$.
        

> **Limite:** Anche se efficiente, il costo di aggiornare i puntatori durante l'unione può essere oneroso per insiemi molto grandi.

#### Dettaglio
si usa una collezione di sequenze per ciascun cluster. Ogni oggetto p di tipo posizione memorizza al suo interno un riferimento all'elemento associato a x che a sua volta ha un riferimento alla sequenza che contiene p, perché tale sequenza rappresenta il cluster che contiene l'elemento di p.
Con questa rappresentazione è facile implementare le operazioni makeCluster(x) e find(p) in modo che vengano eseguite in un tempo O(1) facendo in modo che la prima posizione di una sequenza ricopra il ruolo di leader. L'operazione union (p, q) deve unire due sequenze in una sola e aggiornare i riferimenti cluster al cluster di appartenenza nelle posizioni di uno dei due cluster: scegliamo di implementare questa operazione eliminando tutte le posizioni dalla sequenza di dimensione minore, inserendole in quella di dimensione maggioreOgni volta che togliamo una posizione dal cluster più piccolo, A, e la inseriamo nel cluster più grande, B, aggiorniamo il riferimento cluster presente in quella posizione in modo che punti a B. Quindi l'operazione union (p, q) viene eseguita in un tempo O(min(np, nq)) dove np, nq sono, rispettivamente, le cardinalità dei cluster contenenti p e q. Questo tempo è chiaramente O(n) se n è il numero di elementi dell'universo partizionato. Vedremo, però, ora un'analisi ammortizzata che mostra come questa implementazione sia ben migliore di quanto appaia dall'analisi del caso peggiore.

Proposizione 14.26: Usando l'implementazione della partizione basata su sequenze, l'esecuzione di una serie di k operazioni makeCluster, union e find in una partizione inizialmente vuota contenente al massimo n elementi richiede un tempo O(k + n * log(n)) .

---

### 4. Implementazione B: Basata su Alberi (Forest) 🏆
![[Pasted image 20251125191608.png]]

Questa è l'implementazione standard per alte prestazioni.

Ogni cluster è rappresentato da un albero (non necessariamente binario).

- **Nodi:** Sono le posizioni `p`.
    
- **Riferimenti:** Ogni nodo punta solo al suo **genitore** (`parent`).
    
- **Radice:** La radice punta a se stessa ed è il **leader** del cluster.
    

#### Funzionamento Base

- **`find(p)`:** Risale i puntatori `parent` da $p$ fino alla radice. Costo: $O(h)$ dove $h$ è l'altezza dell'albero.
    
- **`union(p, q)`:** Trova le due radici e fa puntare una radice all'altra. Costo: $O(1)$ (dopo aver fatto le find).
    

⚠️ **Problema:** Senza accorgimenti, l'albero può degenerare in una lista (sbilanciato), rendendo la `find` $O(n)$.
![[Pasted image 20251125191620.png]]

#### Dettaglio
Una struttura dati alternativa per rappresentare una partizione usa una collezione di alberi per memorizzare gli n elementi, associando ciascun albero a un diverso cluster. Nello specifico, implementiamo ogni albero con una struttura dati concatenata, i cui nodi sono gli oggetti di tipo "posizione". Consideriamo che ciascuna posizione p sia un nodo con una variabile di esemplare, element, che fa riferimento al proprio elemento, x, e una variabile di esemplare, parent, che fa riferimento al nodo genitore. Per convenzione, se p è la radice dell'albero a cui appartiene, assegniamo al suo campo parent un riferimento a se stessa.

Con questa struttura dati per la partizione, l'operazione find(p) viene eseguita risalendo dalla posizione p fino alla radice del suo albero, cosa che richiede un tempo O(n) nel caso peggiore. L'operazione union(p, q) può essere implementata facendo in modo che uno dei due alberi diventi un sottoalbero dell'altro: per prima cosa si trovano le due radici, poi in un ulteriore tempo O(1) si fa in modo che il riferimento parent di una delle radici punti all'altra radice. A un primo esame questa implementazione non sembra in alcun modo migliore della struttura dati basata su sequenze, ma, per renderla più veloce, possiamo aggiungere queste due semplici tecniche euristiche:

Euristica "Unione in base alla dimensione": (union-by-size) In ciascuna posizione p memorizziamo anche il numero di elementi presenti nel sottoalbero avente radice in p. Durante un'operazione union, facciamo in modo che la radice del cluster più piccolo diventi un figlio dell'altra radice, poi aggiorniamo la dimensione memo- rizzata in quest'ultima.

Euristica "Compressione del Percorso: (path compression) Durante un'operazione find, in ogni posizione q che viene visitata si assegna la radice come genitore.

Usando l'implementazione della partizione basata su alberi, con le due strategie euristiche funion-by-size e path compression, l'esecuzione di una serie di le operazioni make-Cluster, union e find in una partizione inizialmente vuota contenente al massimo n elementi richiede un tempo O((k) log* n).
![[Pasted image 20251125191629.png]]
---

### 🚀 Le Due Euristiche di Ottimizzazione

Per ottenere prestazioni eccezionali ($O(\log^* n)$), si applicano due euristiche combinate:

#### 1. Unione per Dimensione (Union-by-Size)

Quando si esegue `union(p, q)`, non si attacca un albero a caso sotto l'altro.

- **Regola:** Si attacca sempre la radice dell'albero **più piccolo** (con meno nodi) come figlia della radice dell'albero **più grande**.
    
- **Effetto:** L'altezza degli alberi rimane logaritmica ($O(\log n)$).
    

#### 2. Compressione del Percorso (Path Compression)

Applicata durante l'operazione `find(p)`.

- **Regola:** Mentre risaliamo da $p$ verso la radice, facciamo in modo che **tutti i nodi attraversati** puntino direttamente alla radice trovata.
    
- **Effetto:** Appiattisce drasticamente l'albero. Le successive `find` su quei nodi saranno $O(1)$.
    

---

### 📊 Analisi della Complessità (Logaritmo Iterato)

Utilizzando Alberi + Union-by-Size + Path Compression, la complessità per una sequenza di $k$ operazioni è:

$$O(k \cdot \log^* n)$$

Dove $\log^* n$ (logaritmo iterato) è il numero di volte che devi applicare il logaritmo a $n$ per ottenere un valore $\le 1$.

- Per tutti i numeri pratici nell'universo (fino a $2^{65536}$), $\log^* n \le 5$.
    
- **In pratica:** Le operazioni sono considerate **tempo costante** $O(1)$ ammortizzato.
    

---
