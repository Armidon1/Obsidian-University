# ⚡ Algoritmo di Dijkstra (Shortest Path)

### 🎯 Obiettivo

Trovare la **distanza minima** (cammino più breve) da un vertice sorgente $s$ a tutti gli altri vertici $v$ in un grafo pesato con **pesi non negativi**.

### 🧠 Concetto: Il Metodo Greedy e la "Nuvola"

L'algoritmo applica il **metodo Greedy** (goloso) eseguendo una sorta di "attraversamento in ampiezza pesato".

- **La Nuvola ($C$):** L'algoritmo mantiene un insieme di vertici $C$ (la "nuvola") di cui ha già calcolato la distanza minima definitiva da $s$.
    
- **Espansione:** Ad ogni iterazione, l'algoritmo seleziona un vertice $u$ esterno alla nuvola che ha la distanza stimata minore ($D[u]$) e lo aggiunge a $C$.
    
- **Terminazione:** L'algoritmo termina quando tutti i vertici raggiungibili sono entrati nella nuvola.
    

---

### 🏷️ Etichette e Distanze

Per ogni vertice $v$, manteniamo un'etichetta $D[v]$:

- **$D[v]$:** Rappresenta la lunghezza del **miglior percorso trovato finora** da $s$ a $v$.
    
- **Inizializzazione:**
    
    - $D[s] = 0$ (distanza dalla sorgente a se stessa).
        
    - $D[v] = \infty$ per ogni $v \neq s$ (inizialmente sconosciuti).
        

---

### ⚙️ Procedura di Rilassamento (Relaxation)

È il cuore dell'algoritmo. Quando aggiungiamo un vertice $u$ alla nuvola, controlliamo se passando per $u$ possiamo raggiungere i suoi vicini $v$ con un percorso più breve di quello che conoscevamo prima.

Formula di Rilassamento:

$$if \ D[u] + w(u, v) < D[v] \ then$$

$$D[v] = D[u] + w(u, v)$$

- $u$: Vertice appena aggiunto alla nuvola (con distanza consolidata).
    
- $v$: Vertice adiacente a $u$.
    
- $w(u, v)$: Peso del lato tra $u$ e $v$.
    
- $D[u] + w(u, v)$: Nuova distanza proposta passando per $u$.
    

> **Significato:** "Prende un vecchio valore approssimato e controlla se può essere migliorato per avvicinarsi di più al valore vero."

---

### 💻 Pseudocodice (ShortestPath)

Snippet di codice

```
Algoritmo ShortestPath(G, s):
    Input: Un grafo G (pesi >= 0) e un vertice sorgente s
    Output: La lunghezza del percorso più breve da s a v per ogni v

    // 1. Inizializzazione
    for ogni vertice v in G do
        if v == s then D[v] = 0
        else D[v] = ∞
    
    // 2. Creazione della Coda Prioritaria (Priority Queue)
    Crea una coda prioritaria Q contenente tutti i vertici
    (Usa le etichette D come chiavi per l'ordinamento: min-heap)

    // 3. Ciclo Principale
    while Q non è vuota do
        // Estrai il vertice con etichetta minima (entra nella nuvola)
        u = Q.removeMin()
        
        // Rilassamento dei vicini
        for ogni lato (u, v) uscente da u do
            if v appartiene ancora a Q then
                // Esegui la procedura di rilassamento
                if D[u] + w(u, v) < D[v] then
                    D[v] = D[u] + w(u, v)
                    // Aggiorna la priorità di v nella coda Q
                    cambia la chiave associata a v in Q con il nuovo D[v]
    
    return l'etichetta D[v] di ciascun vertice v
```

---
## 💻 Codice: Implementazione Dijkstra (Java)

Questa implementazione calcola le distanze minime da un vertice sorgente `src` verso tutti i vertici raggiungibili.

```java
/**
 * Calcola le distanze dal vertice src di tutti i vertici di g raggiungibili.
 */
public static <V> Map<Vertex<V>, Integer> shortestPathLengths(Graph<V, Integer> g, Vertex<V> src) {
    
    // 1. Mappa delle distanze stimate (Upper Bound)
    // d.get(v) è il limite superiore per la distanza di v da src
    Map<Vertex<V>, Integer> d = new ProbeHashMap<>();
    
    // 2. Mappa della "Nuvola" (Distanze definitive)
    // associa v al suo valore d finale (visitato)
    Map<Vertex<V>, Integer> cloud = new ProbeHashMap<>();
    
    // 3. Coda con Priorità Adattabile
    // pq avrà i vertici come valori, con d.get(v) come chiave (distanza)
    AdaptablePriorityQueue<Integer, Vertex<V>> pq;
    pq = new HeapAdaptablePriorityQueue<>();
    
    // 4. Mappa dei Token (Locator)
    // associa i vertici alla loro posizione (Entry) nella pq
    // Fondamentale per aggiornare le chiavi in O(log V) invece di O(V)
    Map<Vertex<V>, Entry<Integer, Vertex<V>>> pqTokens;
    pqTokens = new ProbeHashMap<>();
    
    // --- FASE DI INIZIALIZZAZIONE ---
    // per ogni vertice v del grafo, aggiunge una voce alla coda prioritaria, con
    // l'origine src avente distanza 0 e tutti gli altri vertici distanza infinita
    for (Vertex<V> v : g.vertices()) {
        if (v == src) 
            d.put(v, 0);
        else 
            d.put(v, Integer.MAX_VALUE);
        
        // Inserisce in PQ e salva il token (riferimento all'entry) per futuri aggiornamenti
        pqTokens.put(v, pq.insert(d.get(v), v)); 
    }
    
    // --- CICLO PRINCIPALE (Espansione della Nuvola) ---
    // ora inizia l'inserimento di vertici raggiungibili nella nuvola
    while (!pq.isEmpty()) {
        
        // Estrai il vertice con distanza minima (Greedy)
        Entry<Integer, Vertex<V>> entry = pq.removeMin();
        int key = entry.getKey();
        Vertex<V> u = entry.getValue();
        
        cloud.put(u, key);   // Aggiungi u alla nuvola (distanza definitiva)
        pqTokens.remove(u);  // u non è più presente in pq
        
        // Rilassamento dei vicini
        for (Edge<Integer> e : g.outgoingEdges(u)) {
            Vertex<V> v = g.opposite(u, e);
            
            if (cloud.get(v) == null) { // Se v non è ancora nella nuvola
                
                // esegui il rilassamento per il lato (u, v)
                int wgt = e.getElement();
                
                // Se troviamo un percorso migliore passando per u...
                if (d.get(u) + wgt < d.get(v)) {
                    d.put(v, d.get(u) + wgt); // aggiorna la stima d
                    
                    // AGGIORNAMENTO CHIAVE IN PQ (Cruciale!)
                    // Usa il token salvato per trovare v direttamente nella heap e aggiornare la priorità
                    pq.replaceKey(pqTokens.get(v), d.get(v)); 
                }
            }
        }
    }
    
    return cloud; // contiene soltanto i vertici raggiungibili
}
```

## Iterazioni
![[Pasted image 20251125185950.png]]
![[Pasted image 20251125185956.png]]![[Pasted image 20251125190001.png]]![[Pasted image 20251125190004.png]]

---

### 🔑 Analisi delle Strutture Dati Utilizzate

Per il tuo esame di Ingegneria, è fondamentale capire **perché** sono state usate queste specifiche strutture (evidenziate in azzurro nell'immagine):

1. **`d` (ProbeHashMap):**
    
    - Serve per mantenere le stime _correnti_ delle distanze. Inizialmente $\infty$, diminuiscono man mano che troviamo percorsi migliori (Rilassamento).
        
2. **`cloud` (ProbeHashMap):**
    
    - Rappresenta l'insieme $S$ dei vertici la cui distanza minima è **certa**. Una volta che un vertice entra in `cloud`, non ne usciamo più.
        
3. **`pq` (HeapAdaptablePriorityQueue):**
    
    - Questa non è una coda prioritaria standard. È "Adattabile".
        
    - In una PQ standard, non puoi modificare la priorità di un elemento già inserito (dovresti rimuoverlo e reinserirlo, costo $O(V)$).
        
    - In una PQ Adattabile, grazie ai metodi come `replaceKey`, puoi aggiornare la priorità in **$O(\log V)$**.
        
4. **`pqTokens` (ProbeHashMap):**
    
    - Questo è il "ponte" tra i vertici e la loro posizione fisica dentro la Coda Prioritaria.
        
    - Senza questa mappa, per aggiornare la distanza di `v`, dovresti cercare `v` dentro la PQ (lento). Con questa mappa, hai un puntatore diretto all'entry di `v` nella PQ.
        

### ⏱️ Complessità Totale

Grazie all'uso di `AdaptablePriorityQueue` e `pqTokens`:

- Ogni vertice viene estratto una volta: $O(V \log V)$.
    
- Ogni lato viene rilassato una volta, e un rilassamento costa $O(\log V)$ (per la `replaceKey`): $O(E \log V)$.
    

**Totale:** $O((V + E) \log V)$.

Senza la coda adattabile (usando un array semplice o una ricerca lineare), la complessità salirebbe a $O(V^2)$.

### Costo algoritmo di Dijkstra
Esso dipende sia dal ciclo for e while che sta fuori per un totale di O(n+m), che dalla struttura dati utilizzata per la struttura dati Q che ordina i vertici. Per quest'ultima, posiamo usare un una coda prioritaria modificabile implementata tramite un heap che permette di avere un costo per ciascuna operazione di O(logn), mentre se usiamo una sequenza non ordinata avremo O(n), permettendo in quest'ultimo caso di aggiornare in un tempo O(1) il valore di una chiave, a patto che Q usi voci "consapevoli della propria posizione". In totale avremo che mediante un heap il costo sia di O((n+m)logn) e mediante sequenza non ordinata O(n^2 + mn) ~ O(n^2). 
Preferiamo l'heap quando il numero di lati sia piccolo cioè m<(n^2)/logn, viceversa per la sequenza non ordinata.
Se usiamo un heap Fibonacci riusciremo anche ad avere un tempo di esecuzione pari a O(m + nlogn).

## 🌳 Ricostruzione dell'Albero dei Percorsi Minimi (spTree)

### 📌 Contesto

L'algoritmo di Dijkstra (o Bellman-Ford) restituisce come output primario una mappa delle distanze $d$ (uno scalare per ogni vertice). Non ci dice _quale_ strada prendere.

Per ottenere la struttura topologica del percorso (la sequenza di lati), dobbiamo ricostruire un **Shortest Path Tree (SPT)**.

### ⚙️ Logica dell'Algoritmo

L'approccio è di "ingegneria inversa" sul risultato di Dijkstra.

Per ogni vertice $v$ raggiungibile, cerchiamo tra i suoi lati entranti $(u, v)$ quello che soddisfa l'equazione di rilassamento esatta:

$$D[v] == D[u] + w(u, v)$$

Se questa uguaglianza è vera, significa che il lato $(u, v)$ è proprio l'ultimo "ponte" usato per arrivare a $v$ nel percorso minimo.

---

### 💻 Codice 14.14: Implementazione `spTree`

```java
/**
 * Ricostruisce un albero dei percorsi più brevi avente radice s, data la mappa d con le distanze.
 * L'albero è rappresentato come una mappa tra ciascun vertice v raggiungibile da s (tranne s)
 * e il lato e = (u, v) usato per raggiungere v dal suo genitore u nell'albero.
 */
public static <V> Map<Vertex<V>, Edge<Integer>> spTree(Graph<V, Integer> g, Vertex<V> s, Map<Vertex<V>, Integer> d) {
    
    // Mappa risultato: associa ad ogni nodo il "LATO PADRE" che lo connette alla sorgente
    Map<Vertex<V>, Edge<Integer>> tree = new ProbeHashMap<>();
    
    // Iteriamo su tutti i vertici che hanno una distanza calcolata (raggiungibili)
    for (Vertex<V> v : d.keySet()) {
        
        // La sorgente non ha padri, la saltiamo
        if (v != s) {
            
            // Analizziamo solo i lati ENTRANTI in v (chi punta a me?)
            for (Edge<Integer> e : g.incomingEdges(v)) {
                Vertex<V> u = g.opposite(v, e); // u è il potenziale genitore
                int wgt = e.getElement();       // peso del lato
                
                // VERIFICA CRUCIALE (Reverse Relaxation Check)
                // "La mia distanza è uguale alla distanza del mio vicino + il peso del lato tra noi?"
                if (d.get(v) == d.get(u) + wgt) {
                    tree.put(v, e); // Trovato! Questo è il lato del percorso minimo
                    // Nota: potremmo aggiungere un 'break' qui se ci basta un solo percorso,
                    // dato che in un albero ogni nodo ha un solo padre.
                }
            }
        }
    }
    
    return tree;
}
```

### 📝 Analisi della tua nota manoscritta

Hai scritto:

> _"In pratica prende ogni vertice, si ricava il lato e controlla se la lunghezza coincida con quello trovato da shortest path algorithm"_

È una sintesi perfetta.

1. **Input:** Prendi $v$ e la sua distanza definitiva $D[v]$.
    
2. **Test:** Provi tutti i vicini $u$.
    
3. **Conferma:** Se $D[u] + peso == D[v]$, allora hai trovato il "pezzo" di strada mancante.
    

---

