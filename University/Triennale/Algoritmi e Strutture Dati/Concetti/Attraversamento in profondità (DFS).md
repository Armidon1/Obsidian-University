---
title: Attraversamento in profondità (DFS)
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - grafi
  - attraversamenti
---

# Attraversamento in profondità (DFS)

> [!summary] In breve
> DFS esplora andando sempre più a fondo da un vertice non visitato e tornando indietro (backtracking) nei vicoli ciechi; in $O(n + m)$ trova raggiungibilità, componenti, cicli, albero ricoprente.

```java
public static <V,E> void DFS(Graph<V,E> g, Vertex<V> u,
       Set<Vertex<V>> known, Map<Vertex<V>,Edge<E>> forest) {
  known.add(u);
  for (Edge<E> e : g.outgoingEdges(u)) {
    Vertex<V> v = g.opposite(u, e);
    if (!known.contains(v)) { forest.put(v, e); DFS(g, v, known, forest); }
  }
}
```

- Lati **discovery** (albero DFS) e non dell'albero: **back** (verso un antenato), **forward**, **cross** (solo nei grafi orientati).
- Esiste un ciclo ⇔ DFS trova un lato back.
- Forte connettività: DFS da $s$ sul grafo e sul grafo invertito.
- Usato nella [[Garbage collection mark-sweep|garbage collection]] e nell'ordinamento topologico.

## Collegamenti

- **Concetti correlati**: [[Attraversamento in ampiezza (BFS)]] · [[Grafo (ADT)]] · [[Pila (ADT)]] · [[Garbage collection mark-sweep]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[14 - ASD - Algoritmi per grafi#Attraversamento in profondità (depth-first search)|Lezione 14 — Attraversamento in profondità (depth-first search)]]
