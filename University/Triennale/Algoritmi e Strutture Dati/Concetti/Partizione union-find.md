---
title: Partizione union-find
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - strutture-dati
  - union-find
---

# Partizione union-find

> [!summary] In breve
> Struttura per insiemi disgiunti con `makeCluster`, `union` e `find` (leader del cluster); con alberi, unione per dimensione e compressione del percorso, $k$ operazioni costano $O(k\log^* n)$.

| Implementazione | `find` | `union` | $k$ operazioni |
|---|---|---|---|
| sequenze (sposta la più piccola nella più grande) | $O(1)$ | $O(\min(n_p, n_q))$ | $O(k + n\log n)$ |
| alberi + union-by-size + path compression | quasi $O(1)$ | quasi $O(1)$ | $O(k\log^* n)$ |

- **Union-by-size**: la radice dell'albero più piccolo diventa figlia dell'altra.
- **Path compression**: durante `find` ogni nodo visitato viene collegato direttamente alla radice.
- $\log^* n \le 5$ per ogni $n \le 2^{65536}$.

## Collegamenti

- **Concetti correlati**: [[Algoritmo di Kruskal]] · [[Analisi ammortizzata]] · [[Albero (ADT)]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[14 - ASD - Algoritmi per grafi#Partizioni disgiunte e strutture union-find|Lezione 14 — Partizioni disgiunte e strutture union-find]]
