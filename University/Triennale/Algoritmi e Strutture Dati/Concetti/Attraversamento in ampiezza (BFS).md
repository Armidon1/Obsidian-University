---
title: Attraversamento in ampiezza (BFS)
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - grafi
  - attraversamenti
---

# Attraversamento in ampiezza (BFS)

> [!summary] In breve
> BFS visita i vertici per livelli di distanza (in numero di lati) dalla sorgente, con una coda: in $O(n + m)$ trova i percorsi con il minimo numero di lati.

- Livello 0 = $\{s\}$; livello $i+1$ = vicini non visitati del livello $i$.
- Il percorso nell'albero BFS da $s$ a $v$ ha il **minimo numero di lati**.
- Lati non dell'albero: tutti **cross** nei grafi non orientati; back o cross in quelli orientati.
- Implementazione equivalente con un'unica [[Coda (ADT)|coda FIFO]].
- Con pesi diversi serve [[Algoritmo di Dijkstra|Dijkstra]] ("BFS pesato").

## Collegamenti

- **Concetti correlati**: [[Attraversamento in profondità (DFS)]] · [[Coda (ADT)]] · [[Algoritmo di Dijkstra]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[14 - ASD - Algoritmi per grafi#Attraversamento in ampiezza|Lezione 14 — Attraversamento in ampiezza]]
