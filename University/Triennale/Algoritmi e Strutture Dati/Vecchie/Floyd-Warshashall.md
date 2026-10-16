# Floyd-Warshashall

>[!Definizione]
>L'algoritmo di Floyd-Warshall è un algoritmo basato sulla **Programmazione Dinamica** utilizzato per risolvere il problema dei **cammini minimi tra tutte le coppie di nodi** (All-Pairs Shortest Path) in un grafo pesato (orientato o non orientato).

A differenza di [[Dijkstra Algorithm]] (che parte da una singola sorgente), Floyd-Warshall calcola la distanza minima tra **ogni nodo $i$** e **ogni nodo $j$** contemporaneamente.

### ⚙️ Come Funziona (Il Cuore dell'Algoritmo)

L'idea chiave è considerare un vertice intermedio $k$ e chiedersi: _"Passando per il nodo $k$, il percorso da $i$ a $j$ diventa più breve rispetto al percorso diretto o a quello trovato finora?"_

La relazione di ricorrenza (il "rilassamento") è:

$$dist[i][j] = \min(dist[i][j], \quad dist[i][k] + dist[k][j])$$

Dove:

- $dist[i][j]$ è la distanza minima attualmente conosciuta tra $i$ e $j$.
    
- $k$ è il nodo intermedio che stiamo provando a inserire nel percorso.
    

### Caratteristiche Chiave

1. **Pesi Negativi:** Funziona correttamente anche con archi a peso negativo (a differenza di Dijkstra).
    
2. **Cicli Negativi:** È in grado di rilevare cicli negativi (se alla fine la distanza di un nodo da se stesso $dist[i][i]$ diventa negativa).
    
3. **Struttura Dati:** Solitamente utilizza una **Matrice di Adiacenza** per memorizzare le distanze.
    

### 📊 Complessità

Essendo basato su tre cicli annidati (per ogni nodo intermedio $k$, per ogni sorgente $i$, per ogni destinazione $j$):

- **Tempo:** $O(V^3)$ (dove $V$ è il numero di vertici).
    
- **Spazio:** $O(V^2)$ (per la matrice delle distanze).
    

---


## Funzionamento dettaglio 
Prima diciamo cos'è la [[Chiusura Transitiva]]: la chiusura transitiva di un grafo orientato G è un grafo G* che ha gli sessi vertici di G e ha un lato (u,v) se e solo se G ha un percorso orientato che va da u a v (compreso ovviamente il caso in cui (u,v) sia un lato di G). Perciò una sorta di estensione di G. Lo possiamo ricavare applicando n volte l'algoritmo DFS, applicando quindi DFS ogni volta per un vertice diverso. Però useremo una tecnica alternativa chiamato algoritmo di floyd-Marshall.
Il costo asintotico è O(n^3) contro il costo O(n(n+m)) del DFS ripetuto, però oltre ad essere più facile da implementare, in verità è anche più efficiente quando il grafo è denso oppure il grafo è sparso ma rappresentato mediante matrice delle adiacenze. Inoltre è più efficiente perché nascosto dalla sua notazione asintotica c'è un numero inferiore di operazioni elementari. Ovviamente pero quando il grafo è sparso oppure è rappresentato mediante mappa o lista delle adiacenze, è meglio calcolare la chiusura transitiva mediante il DFS ripetuto.

## 💻 Implementazione Java della Chiusura Transitiva

Questo codice mostra l'implementazione della chiusura transitiva basata sulla struttura del **Floyd-Warshall (o Warshall's Algorithm)**, ma applicata alla modifica diretta della struttura del grafo.

### Codice 14.10: `transitiveClosure`

```java
/**
 * Codice 14.10: Implementazione dell'algoritmo di Floyd-Warshall in Java.
 * Convertire il grafo g nella sua chiusura transitiva.
 */
public static <V, E> void transitiveClosure(Graph<V, E> g) {
    // k: Nodo Intermedio (Pivot)
    for (Vertex<V> k : g.vertices()) {
        
        // i: Nodo Sorgente
        for (Vertex<V> i : g.vertices()) {
            
            // Verifica se esiste il lato (i, k)
            // (Verifica se i e k sono diversi e se l'arco esiste)
            if (i != k && g.getEdge(i, k) != null) {
                
                // j: Nodo Destinazione
                for (Vertex<V> j : g.vertices()) {
                    
                    // Verifica se esiste il lato (k, j)
                    // (Verifica se j e k sono diversi e se l'arco esiste)
                    if (i != j && k != j && g.getEdge(k, j) != null) {
                        
                        // Se (i, j) non c'è ancora, aggiungilo (Chiusura Transitiva)
                        // Esiste un percorso i -> k -> j
                        if (g.getEdge(i, j) == null) {
                            g.insertEdge(i, j, null);
                        }
                    }
                }
            }
        }
    }
}
```

---

## 📜 Algoritmo Formale di Floyd-Warshall (Chiusura Transitiva)

Questa è la versione più formale dell'**Algoritmo di Warshall** (spesso chiamato Floyd-Warshall quando si riferisce alla chiusura transitiva). Lavora creando sequenze di grafi $G_k$ che rappresentano la raggiungibilità attraverso i primi $k$ vertici.

### Algoritmo FloydWarshall($\vec{G}$)

- **Input:** Un grafo orientato $\vec{G}$ con $n$ vertici.
    
- **Output:** La chiusura transitiva $\vec{G}^*$ di $\vec{G}$.
    

---

**Passaggi:**

1. Sia $v_1, v_2, \ldots, v_n$ una qualsiasi numerazione dei vertici di $\vec{G}$.
    
2. Sia $\vec{G}_0 = \vec{G}$.
    
3. `for` $k$ che va da $1$ a $n$ `do`:
    
    - $\vec{G}_k = \vec{G}_{k-1}$
        
    - `for` ogni coppia $i, j$, con $i, j \in \{1, \ldots, n\}$, $i \neq j, i \neq k, j \neq k$ `do`:
        
        - `if` i due lati $(v_i, v_k)$ e $(v_k, v_j)$ sono presenti in $\vec{G}_{k-1}$ `then`:
            
            - Aggiungi il lato $(v_i, v_j)$ a $\vec{G}_k$ (se non c'è già).
                
4. `return` $\vec{G}_n$.
    

---

Questi due schemi (l'implementazione pratica e la definizione formale) mostrano perfettamente come l'algoritmo iterativo di **$O(V^3)$** costruisca la chiusura transitiva.

