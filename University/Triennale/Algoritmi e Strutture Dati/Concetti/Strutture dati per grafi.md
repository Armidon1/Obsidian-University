---
title: Strutture dati per grafi
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - grafi
---

# Strutture dati per grafi

> [!summary] In breve
> Quattro rappresentazioni: lista di lati, lista di adiacenze, mappa di adiacenze (quasi ottima in tutto) e matrice di adiacenze ($O(1)$ per `getEdge` ma spazio $O(n^2)$).

| | Lista di lati | Lista di adiacenze | Mappa di adiacenze | Matrice |
|---|---|---|---|---|
| spazio | $O(n+m)$ | $O(n+m)$ | $O(n+m)$ | $O(n^2)$ |
| `getEdge(u,v)` | $O(m)$ | $O(\min(d_u,d_v))$ | $O(1)$ atteso | $O(1)$ |
| `outgoingEdges(v)` | $O(m)$ | $O(d_v)$ | $O(d_v)$ | $O(n)$ |
| `insertVertex` | $O(1)$ | $O(1)$ | $O(1)$ | $O(n^2)$ |
| `removeVertex` | $O(m)$ | $O(d_v)$ | $O(d_v)$ | $O(n^2)$ |

Grafi reali di solito **sparsi** → liste/mappe; matrice (anche di bit) per grafi densi o per Floyd-Warshall.

## Collegamenti

- **Concetti correlati**: [[Grafo (ADT)]] · [[Tabella hash]] · [[Lista posizionale]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[14 - ASD - Algoritmi per grafi#Strutture dati per grafi|Lezione 14 — Strutture dati per grafi]]
