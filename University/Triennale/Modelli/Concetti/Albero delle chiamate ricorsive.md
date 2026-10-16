---
title: Albero delle chiamate ricorsive
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - ricorsione
---

# Albero delle chiamate ricorsive

> [!summary] In breve
> Rappresenta l'esecuzione di un algoritmo ricorsivo: ogni nodo è una chiamata con il suo costo locale. Sommando i costi per livello si risolve l'equazione di ricorrenza.

Per $T(n) = 2T(n/2) + n$ (merge sort):

| livello | nodi | costo per nodo | costo del livello |
|---|---|---|---|
| 0 | 1 | $n$ | $n$ |
| 1 | 2 | $n/2$ | $n$ |
| $i$ | $2^i$ | $n/2^i$ | $n$ |

$\log n$ livelli × $n$ = $\Theta(n \log n)$.

- Fibonacci ricorsivo: l'albero ha $\Theta(\varphi^n)$ nodi perché ricalcola gli stessi valori.
- La **profondità** dell'albero è la dimensione massima della **pila dei record di attivazione** (spazio).

## Collegamenti

- **Concetti correlati**: [[Equazione di ricorrenza]] · [[Merge-sort]] · [[Numeri di Fibonacci]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[04 - MC - Algoritmi ricorsivi ed equazioni di ricorrenza#Albero delle chiamate (dagli appunti)|Lezione 4 — Albero delle chiamate (dagli appunti)]]
> - [[04 - MC - Algoritmi ricorsivi ed equazioni di ricorrenza#Spazio e pila dei record di attivazione|Lezione 4 — Spazio e pila dei record di attivazione]]
> - [[04 - MC - Algoritmi ricorsivi ed equazioni di ricorrenza#Calcolo dei numeri di Fibonacci|Lezione 4 — Calcolo dei numeri di Fibonacci]]
