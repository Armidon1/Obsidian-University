## 🌳 Albero Binario di Ricerca (BST - Binary Search Tree)

### 1. Definizione e Invariante

Un **BST** è un albero binario in cui, per **ogni nodo $u$**, vale la seguente **Proprietà di Ordinamento**:

- Tutte le chiavi nel **sottoalbero sinistro** sono **$\le$** della chiave di $u$.
    
- Tutte le chiavi nel **sottoalbero destro** sono **$\ge$** della chiave di $u$.
    

Questa proprietà permette di effettuare ricerche molto simili alla _Binary Search_ su array ordinati (dimezzando lo spazio di ricerca ad ogni passo).

![Immagine di binary search tree structure](https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcRgodecX8V1KDbrm7d4rkkGziZqHGPnURHLcbc25ArMayDmUcTaYS2UER68umx-IOuJSZ4oT0pMtGPNQI_G-z8tRtPfCYGh2wOPBg9VrlmNwryCuKM)


### 2. Le Operazioni Fondamentali

#### 🔍 Ricerca (`search(k)`)

Partendo dalla radice:

1. Se la chiave è uguale a $k$ $\to$ Trovato.
    
2. Se $k <$ chiave corrente $\to$ Vai a **sinistra**.
    
3. Se $k >$ chiave corrente $\to$ Vai a **destra**.
    
4. Se arrivi a `null` $\to$ Elemento non presente.
    

#### ➕ Inserimento (`insert(k)`)

Si esegue una ricerca per $k$. Quando si arriva a un puntatore `null` (dove l'elemento "dovrebbe" essere), si crea lì il nuovo nodo foglia.

#### ❌ Cancellazione (`delete(k)`)

È l'operazione più complessa. Ci sono 3 casi:

1. **Nodo Foglia:** Si rimuove semplicemente (il puntatore dal padre diventa `null`).
    
2. **Nodo con 1 Figlio:** Si "scavalca" il nodo, collegando il padre direttamente all'unico figlio (come in una lista linkata).
    
3. **Nodo con 2 Figli:** Non si può rimuovere il nodo senza rompere l'albero.
    
    - Si trova il **Successore** (il nodo più piccolo del sottoalbero destro).
        
    - Si sovrascrive il valore del nodo da cancellare con il valore del successore.
        
    - Si cancella fisicamente il successore (che ricade nel caso 1 o 2).
        

### 3. Visita Simmetrica (In-Order Traversal)

Una caratteristica unica del BST: se visiti l'albero in ordine **(Sinistra $\to$ Radice $\to$ Destra)**, ottieni le chiavi ordinate in modo **crescente**.

---

### 4. Analisi della Complessità (Il problema dell'altezza)

Le prestazioni dipendono dall'**altezza $h$** dell'albero.

|**Caso**|**Struttura**|**Altezza h**|**Costo Operazioni (Search/Insert)**|
|---|---|---|---|
|**Ottimo/Medio**|Albero Bilanciato|$O(\log n)$|**$O(\log n)$**|
|**Pessimo**|Albero Degenerato (es. inserimento sequenziale 1, 2, 3...)|$O(n)$|**$O(n)$** (Lento come una lista!)|

---

### 5. Evoluzione: Alberi Bilanciati (Balanced Search Trees)

Per evitare il caso pessimo $O(n)$, esistono varianti che si **auto-bilanciano** dopo ogni inserimento/cancellazione per mantenere l'altezza sempre vicina a $\log n$.

- **Alberi AVL:** I primi inventati. Mantengono rigida la differenza di altezza tra figli sinistro e destro (massimo 1). Usano le **rotazioni**.
    
- **Alberi Red-Black:** Usati in Java (`TreeMap`), C++ (`std::map`). Usano "colori" sui nodi e regole meno rigide dell'AVL, rendendo gli inserimenti più veloci.
    
- **Splay Trees:** Spostano l'elemento appena cercato in radice (ottimi per accessi frequenti agli stessi dati).
    

---

### 🧠 Flashcard: Search Trees

- **Logica:** "A sinistra i minori, a destra i maggiori."
    
- **Best/Avg Case:** $O(\log n)$ (simile a Binary Search).
    
- **Worst Case:** $O(n)$ (se l'albero diventa una linea).
    
- **Soluzione al Worst Case:** Usare alberi bilanciati (AVL, Red-Black) che garantiscono sempre $O(\log n)$.
    
- **Output Ordinato:** Basta fare una visita simmetrica (In-Order).
    

---
Ecco la nota per Obsidian che chiarisce la relazione fondamentale tra **Alberi** (in particolare gli Alberi di Ricerca) e **Grafi**.

In Ingegneria Informatica, questa distinzione è cruciale: spesso un problema sui grafi può essere risolto molto più velocemente se scopriamo che il grafo è, in realtà, un albero.

---

## 🔗 Relazione: Albero vs Grafo

### 1. Il Concetto Insiemistico

La definizione più semplice e potente è questa:

> **Un Albero è un caso specifico di [[Grafo]].**

Matematicamente parlando, l'insieme degli alberi è un **sottoinsieme** dell'insieme dei grafi.

$$Tree \subset Graph$$

### 2. Definizione Formale

Un albero è un grafo $G = (V, E)$ che soddisfa contemporaneamente queste proprietà:

1. **Connesso:** Esiste un percorso tra ogni coppia di nodi.
    
2. **Aciclico:** Non contiene cicli (non puoi tornare al punto di partenza senza ripercorrere un arco all'indietro).
    
3. **Vincolo Archi-Vertici:** Se ha $N$ vertici, ha esattamente $N-1$ lati.
    

### 3. Confronto Strutturale

|**Caratteristica**|**Grafo Generico**|**Albero (Tree)**|
|---|---|---|
|**Cicli**|Ammessi (potenzialmente infiniti loop).|**Assolutamente vietati.**|
|**Radice**|Non esiste un concetto nativo di "inizio" (salvo definire una sorgente $s$).|Esiste un **unico nodo Radice** (Root).|
|**Genitori/Figli**|Concetto di "Vicini" o "Adiacenti". Relazione paritaria.|Gerarchia stretta: Padre $\to$ Figlio.|
|**Percorsi**|Possono esistere molteplici percorsi tra A e B.|Esiste un **unico percorso** tra due nodi qualsiasi.|
|**Modello Mentale**|Rete (Stradale, Social Network).|Gerarchia (File System, DOM HTML, Organigramma).|

---

### 4. Il "Ponte" Algoritmico: Spanning Trees

Hai appena studiato Prim e Kruskal. Cosa fanno esattamente?

Prendono un Grafo (che può avere cicli e $N^2$ lati) e lo "potano" trasformandolo in un Albero (lo Spanning Tree o [[Albero Ricoprente Minimo]]).

- **[[Grafo]]:** Rappresenta tutte le _possibili_ connessioni.
    
- **Albero (MST):** Rappresenta l'ossatura essenziale per mantenere tutto connesso col minimo costo.
    

### 5. Differenze nell'Attraversamento

Anche gli algoritmi di visita cambiano nome ma fanno cose simili:

- **Grafo:** Usiamo **[[DFS]]** e **[[BFS]]**. Dobbiamo usare un set `visited` (o `known`) per non finire in un ciclo infinito.
    
- **Albero:** Usiamo **Pre-order, In-order, Post-order**.
    
    - _Nota:_ Queste sono in realtà varianti della DFS!
        
    - _Vantaggio:_ Sugli alberi **non serve il set `visited`** (se ci muoviamo solo dalla radice verso le foglie, non torneremo mai su un nodo già visto).
        

### 6. Implementazione in Codice (Differenza pratica)

- **Grafo:** Solitamente implementato con **Liste di Adiacenza** (`Map<Node, List<Node>>`) o Matrici.
    
    Java
    
    ```
    class Graph { Map<Vertex, List<Vertex>> adjVertices; }
    ```
    
- **Albero (Binario):** Implementato con riferimenti espliciti ai figli.
    
    Java
    
    ```
    class TreeNode { TreeNode left; TreeNode right; }
    ```
    
    _Nota come l'albero sia una struttura "ricorsiva per definizione", mentre il grafo è spesso una collezione piatta di nodi e archi._
    

---

