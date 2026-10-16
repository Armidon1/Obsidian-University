---
title: Profondità e altezza di un albero
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - alberi
---

# Profondità e altezza di un albero

> [!summary] In breve
> La profondità di $p$ è il numero di antenati propri (archi dalla radice); l'altezza di $p$ è il numero di archi del cammino più lungo da $p$ a una foglia; l'altezza dell'albero è quella della radice.

$$\text{depth}(p) = \begin{cases} 0 & p \text{ radice} \\ 1 + \text{depth}(\text{parent}(p)) & \text{altrimenti} \end{cases}$$
$$\text{height}(p) = \begin{cases} 0 & p \text{ foglia} \\ 1 + \max_{c \text{ figlio}} \text{height}(c) & \text{altrimenti} \end{cases}$$

- `depth(p)`: $O(d_p + 1)$.
- `height(p)` ricorsiva: $O(n)$ (visita ogni nodo una volta, $\sum_p (c_p + 1) = O(n)$).
- Calcolare l'altezza come massimo delle profondità delle foglie costa $O(n^2)$ nel caso peggiore.

## Collegamenti

- **Concetti correlati**: [[Albero (ADT)]] · [[Proprietà degli alberi binari]] · [[Albero AVL]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[08 - ASD - Alberi#Calcolare profondità e altezza|Lezione 8 — Calcolare profondità e altezza]]
