---
title: Programmazione dinamica
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - progettazione-algoritmi
---

# Programmazione dinamica

> [!summary] In breve
> Si risolvono tutti i sotto-problemi, descritti da pochi indici, dal più piccolo al più grande, memorizzandone le soluzioni in una tabella: trasforma problemi apparentemente esponenziali in polinomiali.

Ingredienti:
1. **sotto-problemi semplici**, parametrizzati da pochi indici;
2. **ottimalità dei sotto-problemi**: una soluzione ottima è composta da soluzioni ottime dei sotto-problemi;
3. **sovrapposizione dei sotto-problemi**: gli stessi sotto-problemi servono più volte (altrimenti basterebbe il dividi-e-conquista).

| Problema | Sotto-problema | Tempo |
|---|---|---|
| moltiplicazione di matrici a catena | $N_{i,j} = \min_k (N_{i,k} + N_{k+1,j} + d_i d_{k+1} d_{j+1})$ | $O(n^3)$ |
| [[Sotto-sequenza comune più lunga (LCS)|LCS]] | $L_{j,k}$ sui prefissi | $O(nm)$ |
| [[Chiusura transitiva e Floyd-Warshall|Floyd-Warshall]] | percorsi con intermedi in $\{v_1..v_k\}$ | $O(n^3)$ |

## Collegamenti

- **Concetti correlati**: [[Sotto-sequenza comune più lunga (LCS)]] · [[Dividi-e-conquista]] · [[Metodo greedy]] · [[Fibonacci ricorsivo]] · [[Chiusura transitiva e Floyd-Warshall]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[13 - ASD - Elaborazione di testi#Programmazione dinamica|Lezione 13 — Programmazione dinamica]]
