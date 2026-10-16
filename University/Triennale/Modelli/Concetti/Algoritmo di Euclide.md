---
title: Algoritmo di Euclide
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - ricorsione
  - mcd
---

# Algoritmo di Euclide

> [!summary] In breve
> Calcola $\mathrm{MCD}(a, b)$ con $\mathrm{MCD}(a, 0) = a$ e $\mathrm{MCD}(a, b) = \mathrm{MCD}(b, a \bmod b)$. Fa $O(\log b)$ chiamate: lineare nella dimensione dell'input.

```c
int mcd(int a, int b) {        /* a >= b */
   if(b == 0) return a;
   else return mcd(b, a % b);
}
```

- **Correttezza**: ogni divisore comune di $(a, b)$ divide $(b, a \bmod b)$ e viceversa.
- **Analisi banale**: $b$ decresce, quindi $O(b) = O(2^z)$ chiamate (non tight).
- **Analisi accurata**: $b_{k-1} = q_k b_k + b_{k+1} \ge b_k + b_{k+1} > 2 b_{k+1}$: **ogni due chiamate il secondo argomento si dimezza**. Quindi $\le 2\log_2 b$ chiamate: $O(z)$.

Esempio: $\mathrm{MCD}(512, 10) \to \mathrm{MCD}(10, 2) \to \mathrm{MCD}(2, 0) = 2$.

## Collegamenti

- **Concetti correlati**: [[Algoritmo pseudopolinomiale]] · [[Equazione di ricorrenza]] · [[Classe P]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[04 - MC - Algoritmi ricorsivi ed equazioni di ricorrenza#Calcolo del massimo comun divisore: l'algoritmo di Euclide|Lezione 4 — Calcolo del massimo comun divisore: l'algoritmo di Euclide]]
> - [[04 - MC - Algoritmi ricorsivi ed equazioni di ricorrenza#Un'analisi più accurata|Lezione 4 — Un'analisi più accurata]]
