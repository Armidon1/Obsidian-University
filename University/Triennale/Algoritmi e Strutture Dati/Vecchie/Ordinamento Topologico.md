# ORDINAMENTO TOPOLOGICO (Topological Sort)

### Definizione e Condizione Necessaria

L'ordinamento topologico è un concetto applicabile esclusivamente ai **Grafi Orientati Aciclici (DAG - Directed Acyclic Graph)**.

- **Condizione d'Esistenza:** Un grafo orientato $G$ ammette un ordinamento topologico **se e solo se** è **aciclico** (non contiene cicli orientati).
    
- Definizione Formale: Dato un grafo orientato $G$ con $n$ vertici, un ordinamento topologico è una disposizione dei vertici:
    
    $$v_1, v_2, \ldots, v_n$$
    
    tale che, per ogni lato orientato $(v_i, v_j)$ di $G$, si ha sempre che l'indice della sorgente è minore dell'indice della destinazione:
    
    $$i < j$$
    
- **Concetto Intuitivo:** Dispone i vertici in una sequenza da sinistra a destra in modo che **tutti i percorsi orientati** seguano sempre tale disposizione. (Ad esempio, è perfetto per la schedulazione di attività con dipendenze).
    

---

### 🛠️ Dettagli di Implementazione (Algoritmo di Kahn)

L'implementazione sfrutta la nozione di **grado di ingresso** (In-Degree) per determinare i vertici che non hanno dipendenze non ancora soddisfatte.

#### 1. Strutture Dati e Inizializzazione

- **Mappa `inCount`:** Una mappa (tipicamente una tabella hash) che memorizza il **numero di lati entranti** (In-Degree) per ogni vertice.
    
    - **Vantaggio:** L'uso di una tabella hash o l'indicizzazione diretta (se i vertici sono numerati $0$ a $n-1$) consente l'accesso in **tempo costante** $O(1)$ ai conteggi dei gradi di ingresso.
        
- **Lista (o Coda):** Una struttura dati per contenere i vertici con $\text{In-Degree} = 0$, da cui l'algoritmo parte.
    
- **Lista Risultato:** La lista finale che conterrà l'ordinamento topologico.
    

#### 2. Processo Iterativo

L'algoritmo funziona iterativamente:

1. Inizializza $\text{inCount}$ per tutti i vertici.
    
2. Aggiunge tutti i vertici con $\text{In-Degree} = 0$ alla lista iniziale.
    
3. Finché la lista non è vuota:
    
    - Estrae un vertice $u$ (con $\text{In-Degree} = 0$) e lo aggiunge alla Lista Risultato.
        
    - Per ogni vicino $v$ di $u$:
        
        - Decrementa il $\text{In-Degree}$ di $v$.
            
        - Se $\text{In-Degree}[v]$ raggiunge $0$, aggiunge $v$ alla lista dei vertici da elaborare.
            

#### 3. **Effetto Collaterale: Rilevamento di Cicli**

Questo algoritmo funge da efficace **check per i cicli** nel grafo:

- Se l'algoritmo termina e la **Lista Risultato contiene meno di $n$ vertici**, allora il grafo **contiene almeno un ciclo orientato**. I vertici mancanti fanno parte di tale ciclo.
    

### ⏱️ Complessità

Assumendo che la mappa $\text{inCount}$ e le operazioni sui vertici siano $O(1)$ (grazie all'uso di hash/indicizzazione):

- **Tempo:** $O(V + E)$ (Lineare), poiché ogni vertice e ogni lato vengono elaborati al massimo due volte. Questa è la complessità ottimale per gli algoritmi di visita di grafi.
    

---

## 💻 Codice 14.11: Implementazione dell'Algoritmo di Ordinamento Topologico in Java


```java
/**
 * Codice 14.11: Implementazione dell'algoritmo di ordinamento topologico in Java.
 * Restituisce una lista dei vertici del DAG g in ordine topologico.
 */
public static <V, E> PositionaList<Vertex<V>> topologicalSort(Graph<V, E> g) {
    // 1. Lista dei vertici in ordine topologico (Output)
    PositionaList<Vertex<V>> topo = new LinkedListPositionaList<>();
    
    // 2. Contenitore dei vertici che non hanno più vincoli (Ready Queue/Stack)
    Stack<Vertex<V>> ready = new LinkedStack<>();
    
    // 3. Mappa che tiene traccia del grado entrante residuo di ciascun vertice
    Map<Vertex<V>, Integer> inCount = new ProbeHashMap<>();

    // FASE 1: Inizializzazione dei conteggi
    for (Vertex<V> u : g.vertices()) {
        inCount.put(u, g.inDegree(u)); // Inizializza con il grado entrante effettivo
        
        if (inCount.get(u) == 0) { // Se u non ha lati entranti
            ready.push(u);         // Allora è libero da vincoli e pronto per l'elaborazione
        }
    }

    // FASE 2: Elaborazione (Estrarre i vertici senza vincoli e aggiornare i vicini)
    while (!ready.isEmpty()) {
        
        Vertex<V> u = ready.pop(); // Estrae un vertice pronto (grado 0)
        topo.addLast(u);           // Aggiunge u all'ordinamento finale

        // Considera tutti i vicini uscenti da u
        for (Edge<E> e : g.outgoingEdges(u)) {
            Vertex<V> v = g.opposite(u, e);
            
            // Senza u, v ha un vincolo in meno (decremento del grado)
            inCount.put(v, inCount.get(v) - 1); 
            
            // Se il conteggio residuo raggiunge zero
            if (inCount.get(v) == 0) {
                ready.push(v); // Allora v è ora pronto per essere elaborato
            }
        }
    }

    // FASE 3: Risultato
    // (NOTA: Se topo.size() < g.vertices().size(), esiste un ciclo)
    return topo;
}
```

---

### 📝 Riepilogo delle Strutture Dati

|**Variabile**|**Tipo Java**|**Ruolo nell'Algoritmo**|**Obiettivo**|
|---|---|---|---|
|`topo`|`PositionaList`|Lista di Output|Memorizza l'ordine topologico finale.|
|`ready`|`Stack` (o Coda)|Contenitore di lavoro|Mantiene i vertici con $\text{In-Degree} = 0$, pronti per essere estratti.|
|`inCount`|`Map` (`ProbeHashMap`)|Mappa Hash|Mantiene il conteggio dinamico dei vincoli (lati entranti) per ogni vertice.|

