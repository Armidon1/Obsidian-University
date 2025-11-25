## 🔗 Cos'è la Chiusura Transitiva?

In termini semplici, la chiusura transitiva di un grafo risponde alla domanda: **"Esiste un percorso (indipendentemente dalla lunghezza) per andare dal nodo A al nodo B?"**

Se immaginiamo un grafo $G$, la sua chiusura transitiva $G^*$ è un grafo che:

1. Ha gli stessi vertici di $G$.
    
2. Ha un arco diretto $(u, v)$ se e solo se nel grafo originale $G$ esiste un **cammino** (una sequenza di uno o più archi) che porta da $u$ a $v$.
    

> **In sintesi:** Trasforma la "raggiungibilità indiretta" (cammini) in "connessione diretta" (archi).

---

### Definizione Formale

Dato un grafo orientato $G = (V, E)$, la chiusura transitiva è un grafo $G^* = (V, E^*)$ tale che:

$$(u, v) \in E^* \iff \exists \text{ un cammino da } u \text{ a } v \text{ in } G$$

### Esempio Pratico

Immagina una rete di dipendenze software:

- Il Modulo A dipende dal Modulo B ($A \to B$).
    
- Il Modulo B dipende dal Modulo C ($B \to C$).
    

Nel grafo originale non c'è un arco diretto tra A e C.

Nella chiusura transitiva, aggiungiamo l'arco $A \to C$, rendendo esplicito che A dipende indirettamente da C.

---

### Come si calcola? (Collegamento con Floyd-Warshall)

Dato che hai appena studiato **Floyd-Warshall**, ecco un'ottima notizia: l'algoritmo per calcolare la chiusura transitiva è una sua variante semplificata, chiamata **Algoritmo di Warshall**.

Invece di lavorare con somme e minimi (distanze), lavora con operazioni booleane (`OR` e `AND`):

1. **Matrice di Adiacenza Booleana:** $M[i][j] = 1$ se c'è un arco, $0$ altrimenti.
    
2. **Logica di aggiornamento:** Se esiste un percorso da $i$ a $k$ **E** un percorso da $k$ a $j$, allora esiste un percorso da $i$ a $j$.
    

Formula:

$$M[i][j] = M[i][j] \lor (M[i][k] \land M[k][j])$$

La complessità rimane $O(V^3)$.

---

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
