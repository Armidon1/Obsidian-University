---
title: Notazione asintotica
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - analisi
  - matematica
---

# Notazione asintotica

> [!summary] In breve
> $O$, $\Omega$, $\Theta$ confrontano le funzioni ignorando costanti e termini di ordine inferiore: $f(n)$ è $O(g(n))$ se $f(n) \le c\,g(n)$ per ogni $n \ge n_0$.

- $f(n) = O(g(n))$: esistono $c > 0$, $n_0 \ge 1$ con $f(n) \le c\,g(n)$ per $n \ge n_0$ (limite **superiore**).
- $f(n) = \Omega(g(n))$: $f(n) \ge c\,g(n)$ da un certo $n_0$ (limite **inferiore**).
- $f(n) = \Theta(g(n))$: entrambe.

Regole: si tiene il termine dominante e si toglie la costante ($5n^2 + 3n\log n + 2 = O(n^2)$); un polinomio di grado $d$ è $O(n^d)$; $\log n^c = O(\log n)$.

Si dice il limite **più stretto** possibile ("$O(n)$", non "$O(n^2)$" se vale $O(n)$).

## Collegamenti

- **Concetti correlati**: [[Funzioni di crescita]] · [[Analisi del caso peggiore]] · [[Limite inferiore per l'ordinamento basato su confronti]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[04 - ASD - Analisi di algoritmi#La notazione "O-grande"|Lezione 4 — La notazione "O-grande"]]
