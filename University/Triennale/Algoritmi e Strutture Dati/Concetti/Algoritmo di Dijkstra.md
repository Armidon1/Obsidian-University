---
title: Algoritmo di Dijkstra
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - grafi
  - percorsi-minimi
  - greedy
---

# Algoritmo di Dijkstra

> [!summary] In breve
> Calcola le distanze da una sorgente in un grafo con pesi **non negativi** facendo crescere una nuvola in ordine di distanza e rilassando i lati: $O((n + m)\log n)$ con heap, $O(n^2)$ con lista.

```text
D[s] = 0, D[v] = ∞; Q = coda prioritaria flessibile di tutti i vertici
while Q non vuota:
  u = Q.removeMin()                    // D[u] è definitivo
  per ogni lato (u, v) con v in Q:
    if D[u] + w(u,v) < D[v]: D[v] = D[u] + w(u,v); aggiorna la chiave di v
```

- Correttezza: quando $u$ entra nella nuvola $D[u] = d(s, u)$ (dimostrazione per assurdo che usa $w \ge 0$).
- Con pesi negativi può sbagliare.
- L'albero dei percorsi minimi si ricostruisce con $D[u] + w(u,v) = D[v]$.
- Heap di Fibonacci: $O(m + n\log n)$. In rete: [[Instradamento Link-State]].

## Collegamenti

- **Concetti correlati**: [[Coda prioritaria flessibile]] · [[Attraversamento in ampiezza (BFS)]] · [[Algoritmo di Prim-Jarník]] · [[Metodo greedy]] · [[Instradamento Link-State]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[14 - ASD - Algoritmi per grafi#L'algoritmo di Dijkstra|Lezione 14 — L'algoritmo di Dijkstra]]
