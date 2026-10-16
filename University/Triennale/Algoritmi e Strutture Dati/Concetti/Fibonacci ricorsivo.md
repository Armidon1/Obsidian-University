---
title: Fibonacci ricorsivo
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - ricorsione
---

# Fibonacci ricorsivo

> [!summary] In breve
> La ricorsione binaria $F_n = F_{n-1} + F_{n-2}$ ricalcola gli stessi valori ed è esponenziale; restituendo la coppia $(F_n, F_{n-1})$ si ottiene una ricorsione lineare $O(n)$.

- **Ingenua** (`fibonacciBad`): numero di chiamate $c_n > 2^{n/2}$ → esponenziale.
- **Buona** (`fibonacciGood`): ogni chiamata restituisce `{F(n), F(n-1)}` e ne fa una sola → $O(n)$.

La stessa ricorrenza, $n(h) = 1 + n(h-1) + n(h-2)$, dimostra che gli alberi AVL hanno altezza logaritmica. L'idea di non ricalcolare i sotto-problemi è quella della [[Programmazione dinamica|programmazione dinamica]].

## Collegamenti

- **Concetti correlati**: [[Ricorsione lineare, binaria e multipla]] · [[Programmazione dinamica]] · [[Albero AVL]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[05 - ASD - Ricorsione#Una ricorsione inefficiente per calcolare i numeri di Fibonacci|Lezione 5 — Una ricorsione inefficiente per calcolare i numeri di Fibonacci]]
