---
title: Algoritmo di Kruskal
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - grafi
  - mst
  - greedy
---

# Algoritmo di Kruskal

> [!summary] In breve
> Considera i lati in ordine di peso crescente e aggiunge un lato se collega due cluster diversi (fondendoli), lo scarta se creerebbe un ciclo; con union-find costa $O(m\log n)$.

```text
ogni vertice è un cluster; Q = lati per peso
while T ha meno di n-1 lati:
  (u,v) = Q.removeMin()
  if find(u) ≠ find(v): aggiungi (u,v) a T; union(u, v)
```

- Correttezza: proprietà del taglio con $V_1$ = cluster di $u$.
- Tempo dominato dall'ordinamento dei lati, $O(m\log m) = O(m\log n)$; la gestione dei cluster costa $O(m + n\log n)$ (o quasi lineare con union-find ottimizzato).

## Collegamenti

- **Concetti correlati**: [[Albero ricoprente minimo (MST)]] · [[Partizione union-find]] · [[Algoritmo di Prim-Jarník]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[14 - ASD - Algoritmi per grafi#L'algoritmo di Kruskal|Lezione 14 — L'algoritmo di Kruskal]]
