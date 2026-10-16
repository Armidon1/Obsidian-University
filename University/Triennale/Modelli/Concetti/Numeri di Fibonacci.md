---
title: Numeri di Fibonacci
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - ricorsione
---

# Numeri di Fibonacci

> [!summary] In breve
> $F_0 = 0$, $F_1 = 1$, $F_n = F_{n-1} + F_{n-2}$. Forma chiusa $F_n = (\varphi^n - (1-\varphi)^n)/\sqrt 5$ con $\varphi = (1 + \sqrt 5)/2$. La ricorsione diretta fa $\Theta(\varphi^n)$ chiamate, l'iterazione $O(n)$.

| versione | costo nel valore $n$ | costo nella dimensione $z$ |
|---|---|---|
| ricorsiva diretta | $\Theta(\varphi^n)$, $O(2^n)$ | doppiamente esponenziale |
| iterativa (due variabili) | $O(n)$ | $O(2^z)$ |

- La ricorsione ricalcola gli stessi valori: per $n = 6$ si fanno 15 attivazioni, contro $F_6 = 8$.
- Forma chiusa con la **funzione generatrice** $s(x) = \sum F_i x^i = \dfrac{x}{1 - x - x^2}$ e i fratti semplici.
- $F_n$ è l'intero più vicino a $\varphi^n / \sqrt 5$.

## Collegamenti

- **Concetti correlati**: [[Fibonacci ricorsivo]] · [[Albero delle chiamate ricorsive]] · [[Equazione di ricorrenza]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[04 - MC - Algoritmi ricorsivi ed equazioni di ricorrenza#Calcolo dei numeri di Fibonacci|Lezione 4 — Calcolo dei numeri di Fibonacci]]
> - [[04 - MC - Algoritmi ricorsivi ed equazioni di ricorrenza#Forma chiusa dei numeri di Fibonacci|Lezione 4 — Forma chiusa dei numeri di Fibonacci]]
