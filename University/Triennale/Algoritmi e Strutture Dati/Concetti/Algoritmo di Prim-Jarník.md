---
title: Algoritmo di Prim-Jarník
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - grafi
  - mst
  - greedy
---

# Algoritmo di Prim-Jarník

> [!summary] In breve
> Fa crescere un MST da un vertice aggiungendo ogni volta il lato più leggero che collega la nuvola a un vertice esterno; come Dijkstra ma con $D[v]$ = peso del miglior lato verso la nuvola. $O(m\log n)$ con heap.

- Rilassamento: `if w(u,v) < D[v]: D[v] = w(u,v); connect(v) = (u,v)` (Dijkstra usa invece $D[u] + w(u,v)$).
- Correttezza: proprietà del taglio con $V_1$ = nuvola.
- Coda prioritaria flessibile: $n$ inserimenti, $n$ `removeMin`, $\le m$ `replaceKey`; $O(n^2)$ con lista non ordinata.

## Collegamenti

- **Concetti correlati**: [[Albero ricoprente minimo (MST)]] · [[Algoritmo di Dijkstra]] · [[Algoritmo di Kruskal]] · [[Coda prioritaria flessibile]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[14 - ASD - Algoritmi per grafi#L'algoritmo di Prim-Jarník|Lezione 14 — L'algoritmo di Prim-Jarník]]
