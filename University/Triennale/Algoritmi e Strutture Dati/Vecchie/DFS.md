
>[!Definizione]
>La **Ricerca in Profondità (DFS - Depth-First Search)** è un algoritmo di attraversamento utilizzato per esplorare tutti i vertici e gli archi di un **grafo** o di un **albero**.
![[bfs-vs-dfs-(1).png]]
---

## 🧭 Concetto Chiave

La strategia della DFS può essere riassunta come "vai più in fondo che puoi":

- **Esplorazione Profonda:** Partendo da un vertice iniziale (radice), l'algoritmo esplora il più possibile lungo ogni ramo, o **profondità**, prima di tornare indietro (backtrack) e analizzare gli altri rami.
    
- **Meccanismo:** Tipicamente, la DFS è implementata in modo **ricorsivo** o utilizzando una **pila (stack)** per memorizzare i vertici da visitare.
    
- **Obiettivo:** Viene usata per trovare le componenti connesse, rilevare cicli, ordinare topologicamente un grafo orientato o, più semplicemente, per visitare tutti i nodi raggiungibili.
    

> **Analogia:** Pensa a come esploreresti un **labirinto**. Invece di guardare tutti i bivi vicini (come fa la BFS), scegli una strada e la percorri fino a un vicolo cieco. Solo allora torni indietro per provare l'ultimo bivio che avevi ignorato.

---

### Complessità

La complessità temporale della DFS è **$O(V + E)$** (dove $V$ è il numero di vertici e $E$ è il numero di archi), assumendo che il grafo sia rappresentato con **liste di adiacenza**, poiché ogni vertice e ogni arco viene visitato esattamente una volta.


## Pseudocodice
```C
Algoritmo DFS(G, u):
    // 1. Contrassegna il vertice u come visitato
    contrassegna il vertice u come visitato

    // 2. Esamina tutti i lati uscenti da u
    for ogni lato e = (u, v) uscente da u do
        if il vertice v non è stato visitato then
            // 2a. Se v è nuovo, (u, v) è un lato di scoperta
            contrassegna e come lato di tipo "discovery" per il vertice v
            
            // 2b. Invoca ricorsivamente la DFS su v
            invoca ricorsivamente DFS(G, v)
        // [Nota: Qui si gestirebbero anche i lati di tipo "back" o "cross", se l'obiettivo fosse la classificazione completa.]
```
### Implementazione via JAVA
```java
public static <V,E> void DFS(Graph<V, G> g, Vertex<V> u, Set<Vertex<V>> known, Map<Vertex<V>, Edge<E>> forest){
  known.add(u);
  
  for (Edge<E> e : g.getOutgoingEdge(u){
    Vertex<V> v = g.opposite(u, e);
    if (!known.contains(v)){
      forest.put(v, e);
      DFS(g, v, kwown, forest);
    }
  }
}
```

## Esempio di proprietà DFS

L’altezza di un albero di visita in profondità (DFS) dipende dalla struttura del grafo e dall’ordine in cui i nodi vengono visitati. In generale, l’altezza dell’albero DFS può variare da un minimo di 1 (quando tutti i nodi sono collegati in una catena lineare) a un massimo di V-1 (quando il grafo è un albero e la radice dell’albero DFS è una delle foglie).

Il numero di foglie in un albero DFS dipende anche dalla struttura del grafo e dall’ordine in cui i nodi vengono visitati. In generale, il numero di foglie può variare da 1 (quando il grafo è un albero e la radice dell’albero DFS è una delle foglie) a V (quando tutti i nodi sono collegati in una catena lineare).

Il grado minimo e massimo di un nodo in un albero DFS è sempre 1 e 3 rispettivamente, poiché ogni nodo può avere al massimo un genitore e due figli. Tuttavia, il grado dei nodi nel grafo originale può essere diverso dal grado dei nodi nell’albero DFS.

## VERIFICA DI CONNETTIVITÀ DI UN GRAFO

se abbiamo un grafo non orientato, dopo dfs, se known.size() == n, dove n è il numero di vertici, allora G è connesso.
Se abbiamo un grafo orientato, usiamo un implementazione modificata di DFS dove si considera anzichè g.getOutGoingEdges(), useremo g.getOutIncomingEdges().

## INDIVIDUARE TUTTI I COMPONENTI CONNESSI CON DFS

Se abbiamo un grafo non orientato, la prima volta di DFS potrebbe non raggiungere tutti i vertici di un grafo, facciamo ripartire DFS per quei vertici non raggiunti ancora. Avremo una nuova foresta alla fine, ed il numero delle componenti connessi viene trovato da g.numVertices() -  forest.size(). tutto questo con il metodo DFSComplete quì sotto:
```java
public static <V, E> Map<Vertex<V>, Edge<E>> DFSComplete(Graph<V,E> g){
  Map<Vertex<V>,Edge<E>> forest = new ProbeHashMap();
  Set<Vertex<V>> known = new HashSet();
  for (Vertex<V> u : g.vertices())
    if (!known.contains(u))
      DFS(g,u,known,forest);
  return forest
  
}
```

## INDIVIDUARE CICLI CON DFS

Tanto nei grafi orientati quanto in quelli non orientati, esiste un ciclo se e solo se l'attraversamento DFS di quel grafo individua un lato back. 
Dal punto di vista algoritmico, nel caso di un grafo non orientato individuare un lato back è semplice, perché tutti i lati che non fanno parte dell'albero DFS (cioè che non sono di tipo discovery) sono di tipo back. 
Nel caso di un grafo orientato, è necessario apportare qualche modifica all'implementazione del metodo DFS per poter assegnare la categoria giusta ai lati che non fanno parte dell'albero DFS, che possono essere di tipo back, forward o cross. Quando viene esplorato un lato orientato che porta a un vertice già visitato, dobbiamo capire se tale vertice sia un antenato di quello attuale nell'albero DFS che si va costruendo. Questo problema può essere risolto, ad esempio, usando un altro insieme contenente tutti I vertici per i quali è attiva un'invocazione ricorsiva di DFS.

## RICOSTRUIRE UN PERCORSO DA u A v CON DFS

Dopo aver usato DFS, sfuttiamo la mappa forest per ricostruire una lista tramite una LinkedPositionalList:
```java
public static <V, E> PositionalList<Edge<E>> constructPath(Graph<V,E> g, Vertex<V> u, Vertex<V> v, Map<Vertex<V>,Edge<E>> forest){
  PositionalList<Edge<E>> path = new LinkedPositionalList();
  
  if (forest.get(v) != null){
    Vertex<V> walk = v;
    while (walk != u){
      Edge<E> edge = forest.get(walk);
      path.addFirst(edge);
      walk = g.opposite(walk, edge);
    }
    
  }
  return path;
}
```

### DIFFERENZE TRA DFS E BFS
Confrontando le funzionalità di [[DFS]] e [[BFS]], si vede che entrambi gli algoritmi possono essere utilizzati per trovare in modo efficiente l'insieme dei vertici che sono raggiungibili a partire da un vertice assegnato, così come per determinare percorsi verso tali vertici. Tuttavia, Falgoritmo BFS garantisce che quei percorsi comprendano il numero minimo di lati. In un grafo non orientato, entrambi gli algoritmi possono essere utilizzati per verificare se il grafo è connesso, per individuare i suoi componenti connessi e per identificare un ciclo al suo interno. In un grafo orientato, l'algoritmo DFS è più adatto a risolvere alcuni problemi, come la ricerca di un ciclo orientato o l'individuazione dei suoi componenti fortemente connessi.