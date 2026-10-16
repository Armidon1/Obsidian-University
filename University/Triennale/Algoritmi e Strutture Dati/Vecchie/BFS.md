# BFS

> [!Definizione]
> La **Ricerca in Ampiezza (BFS - Breadth-First Search)** è un algoritmo di attraversamento utilizzato per esplorare un **grafo** o un **albero** nel modo più **largo** possibile.

![[bfs 1.webp]]
---

## 🗺️ Concetto Chiave

La strategia della BFS può essere riassunta come "visita i vicini prima di visitare i vicini dei vicini":

- **Esplorazione a Livelli:** L'algoritmo visita prima tutti i vertici che si trovano a distanza $k$ dal nodo di partenza, prima di passare a visitare i vertici a distanza $k+1$.
    
- **Strumento Chiave:** Viene implementata utilizzando una **coda (Queue)** (FIFO - First In, First Out) per gestire i vertici da visitare, garantendo così l'ordine di esplorazione a livelli.
    
- **Applicazione Tipica:** È l'algoritmo ideale per trovare il **cammino minimo** (il minor numero di archi) tra due nodi in un grafo non pesato.
    

Data la tua formazione in Ingegneria Informatica, la sua complessità temporale è importante: è **$O(V + E)$** (Vertici + Archi).

## Meccanismo
Un attraversamento BFS procede per fasi successive e suddivide i vertici in livelli. Parte da un vertice, s, che viene posto al livello 0. Nella prima fase, colora come "visitati" tutti i vertici adiacenti al vertice di partenza s: questi vertici si trovano a un lato di distanza dal vertice di partenza e vengono posti al livello 1. Nella seconda fase, consentiamo a tutti gli esploratori di spostarsi di due passi (cioè di due lati) dal vertice di partenza: i nuovi vertici in cui giungono, che sono quelli adiacenti ai vertici di livello 1 e che non hanno ancora ricevuto l'assegnazione di un livello, vengono posti al livello 2 e colorati come "visitati". La procedura continua in modo analogo, terminando quando, esaminando un livello, non si trovano più nuovi vertici. 

## Pseudocodice
```java
Algoritmo BFS(G, u):
    // Inizializzazione: si usano liste posizionali 
    // per i livelli (o una coda FIFO)
    -Crea una lista posizionale 'level' che contiene 
    tutti i vertici del livello corrente
    -Inserisci u come 'contrassegnato' (visitatato)
    -Inserisci alla fine di 'level' il vertice u

    while il livello corrente 'level' non è vuoto do
        // Prepara il contenitore per il livello successivo
        -crea una nuova lista posizionale 'nextLevel' in 
        cui inserire i vertici del livello successivo
        
        // Esamina tutti i vertici nel livello corrente
        for ogni vertice u in 'level' do
            
            // Esamina i vicini di u
            for ogni lato uscente e = (u, v) incidente ad u do
                
                if il vertice opposto v del lato (u, v) non 
                è contrassegnato do
                    // 1. Aggiungi il nuovo vertice al livello successivo
                    -aggiungi v a 'nextLevel'
                    
                    // 2. Contrassegna come visitato
                    -contrassegna v
                    
                    // 3. Registra il lato di scoperta
                    -inserisci nell'insieme di vertici raggiungibili 
                      da u il vertice v come chiave 
                      e il lato (u, v) come valore 
                      (lato di tipo "discovery")
        
        // Passa al livello successivo
        -assegna livello corrente 'level' uguale al livello 
          successivo 'nextLevel'
```
### Java Implementation

```java
public static <V,E> void BFS(Graph<V, E> g, Vertex<V> s,Set<Vertex<V>> known, Map<Vertex<V>, Edge<E>> forest) {
  PositionalList<Vertex<V>> level = new LinkedPositional List<>();
  known.add(s);
  level.addLast(s);
  while (!level.isEmpty()) {
    PositionalList<Vertex<V>> nextLevel = new LinkedPositionalList<>();
    for (Vertex<V> u : level) 
      for (Edge<E> e: g.outgoingEdges (u)) {
        Vertex<V> v = g.opposite(u, e); 
        if (!known.contains(v)) {
          known.add(v);
          forest.put(v, e)
          nextLevel.addLast(v);
        }
      }
    level = nextLevel;
  }
}
```

In un BFS di un grafo non orientato tutti i lati che non fanno parte sono lati di tipo cross. in un Grafo orientato tutti i lati che non fanno parte sono lati di tipo cross o back.
La più grande proprietà che ha il BFS è che individua automaticamente tutti i i percorsi minimi da u a v. Si vedrà che però questo vale solo per i  grafi non pesati.
Per esplorare l'intero grafo, nel caso in cui il primo metodo BFS non esplora completamente, si può implementare la stessa versione di DFSComplete ma con il BFS. Per ricostruire il percorso minimo da u a v si può usare il constructPath.
esempio di proprietà BFS:
L’altezza di un albero di visita in ampiezza (BFS) dipende dalla struttura del grafo e dall’ordine in cui i nodi vengono visitati. In generale, l’altezza dell’albero BFS può variare da un minimo di 1 (quando tutti i nodi sono collegati in una catena lineare) a un massimo di V-1 (quando il grafo è un albero e la radice dell’albero BFS è una delle foglie).

Il numero di foglie in un albero BFS dipende anche dalla struttura del grafo e dall’ordine in cui i nodi vengono visitati. In generale, il numero di foglie può variare da 1 (quando il grafo è un albero e la radice dell’albero BFS è una delle foglie) a V (quando tutti i nodi sono collegati in una catena lineare).

Il grado minimo e massimo di un nodo in un albero BFS è sempre 1 e V-1 rispettivamente, poiché ogni nodo può avere al massimo un genitore e V-1 figli. Tuttavia, il grado dei nodi nel grafo originale può essere diverso dal grado dei nodi nell’albero BFS.

### DIFFERENZE TRA DFS E BFS
Confrontando le funzionalità di [[DFS]] e [[BFS]], si vede che entrambi gli algoritmi possono essere utilizzati per trovare in modo efficiente l'insieme dei vertici che sono raggiungibili a partire da un vertice assegnato, così come per determinare percorsi verso tali vertici. Tuttavia, l'algoritmo BFS garantisce che quei percorsi comprendano il numero minimo di lati. In un grafo non orientato, entrambi gli algoritmi possono essere utilizzati per verificare se il grafo è connesso, per individuare i suoi componenti connessi e per identificare un ciclo al suo interno. In un grafo orientato, l'algoritmo DFS è più adatto a risolvere alcuni problemi, come la ricerca di un ciclo orientato o l'individuazione dei suoi componenti fortemente connessi.