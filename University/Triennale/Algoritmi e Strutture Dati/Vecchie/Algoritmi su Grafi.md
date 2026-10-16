[[Grafo]], [[Grafo Pesato]]
## 🧠 Flashcards: Algoritmi su Grafi

### 1. [[DFS]] (Depth-First Search)

- **Logica:** "Vai in profondità finché puoi, poi torna indietro (backtrack)."
    
- **Implementazione:** Ricorsiva (usa lo Stack di sistema) o Iterativa con Stack esplicito.
    
- **Struttura Dati Chiave:** `known` (Set/Map) per marcare i visitati ed evitare loop.
    
- **Complessità:** $O(V + E)$
    

### 2. [[BFS]] (Breadth-First Search)

- **Logica:** "Esplora a macchia d'olio, livello per livello." (Trova cammini minimi su grafi non pesati).
    
- **Implementazione:** Iterativa.
    
- **Struttura Dati Chiave:** `Queue` (Coda FIFO) per gestire l'ordine di visita $L_0, L_1, L_2...$.
    
- **Complessità:** $O(V + E)$
    

### 3. [[Floyd-Warshashall]] (Chiusura Transitiva)

- **Logica:** "Se posso andare da **i** a **k** e da **k** a **j**, allora posso andare da **i** a **j**."
    
- **Implementazione:** 3 cicli `for` annidati (k, i, j).
    
- **Dettaglio:** Verifica se il lato $(i, j)$ manca. Se manca, ma esistono $(i, k)$ e $(k, j)$, aggiunge $(i, j)$.
    
- **Complessità:** $O(V^3)$ (Costo alto, ma codice semplicissimo).
    

### 4. [[Ordinamento Topologico]] (Kahn's Algorithm)

- **Logica:** "Fai prima ciò che non ha prerequisiti." (Solo per DAG).
    
- **Implementazione:** Iterativa, basata sulla rimozione progressiva dei nodi "liberi".
    
- **Strutture Dati Chiave:**
    
    - `inCount` (Map): Tiene traccia _live_ del grado entrante (dipendenze residue).
        
    - `Stack` / `Queue`: Contiene i vertici con `inCount == 0` (pronti).
        
- **Complessità:** $O(V + E)$
    

### 5. [[Dijkstra Algorithm]] (Shortest Path)

- **Logica:** Greedy ("Prendi sempre il nodo più vicino non ancora chiuso").
    
- **Implementazione:** Espansione della "nuvola" dei visitati tramite rilassamento.
    
- **Strutture Dati Chiave (Java Optimized):**
    
    - `cloud` (Map): Distanze definitive (chiuse).
        
    - `HeapAdaptablePriorityQueue`: Per estrarre il minimo e fare `replaceKey` in $O(\log V)$.
        
    - `pqTokens` (Map): Ponte tra vertice e la sua Entry nella PQ (per aggiornare velocemente).
        
    - `D` (Map): Stime (Upper Bound) delle distanze.
        
- **Complessità:** $O((V + E) \log V)$
    

---

### 6. [[Prim-Jarník]] (MST - Approccio "Nuvola")

- **Logica:** Fai crescere un **unico albero** partendo da una radice arbitraria. Ad ogni passo, ingloba il vertice esterno collegato alla nuvola con il **lato più leggero**.
    
- **Differenza Cruciale vs Dijkstra:** L'etichetta $D[v]$ rappresenta il peso del **singolo lato** che collega $v$ alla nuvola ($w(u,v)$), NON la somma del percorso dalla radice.
    
- **Strutture Dati Chiave:**
    
    - `PriorityQueue`: Contiene i vertici esterni, ordinati per $D[v]$.
        
    - `connect` (Map): Memorizza _quale_ lato ha generato il valore $D[v]$ (il "padre" nell'MST).
        
- **Complessità:** $O(E \log V)$ (con Heap binario).
    

### 7. [[Kruskal]] (MST - Approccio "Cluster")

- **Logica:** "Gestisci una foresta". Ordina tutti i lati per peso (dal più leggero) e unisci i vertici se appartengono a **cluster diversi**.
    
- **Implementazione:** Scansiona i lati ordinati e usa una struttura dati per verificare la connettività ed evitare cicli.
    
- **Strutture Dati Chiave:**
    
    - `PriorityQueue` (o Sorting): Per estrarre i lati in ordine crescente di peso.
        
    - **`Union-Find` (Partition):** Struttura fondamentale con operazioni `find()` (con path compression) e `union()` (by size) per gestire i cluster in tempo quasi costante.
        
- **Complessità:** $O(E \log V)$ (Dominata dall'ordinamento dei lati).
    
