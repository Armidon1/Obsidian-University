---
title: Distribuzione di Pascal
tags:
  - probabilita-e-statistica
  - concetto
  - distribuzioni
  - pascal
---

# Distribuzione di Pascal

> [!summary] In breve
> Binomiale negativa $NB(p,n)$: numero di fallimenti prima dell'$n$-esimo successo in un processo di Bernoulli.

$$P(T_n=k)=\binom{k+n-1}kp^nq^k\qquad E[T_n]=\frac{nq}p\qquad\mathrm{Var}(T_n)=\frac{nq}{p^2}$$

- $T_n=Y_1+\dots+Y_n-n$ con $Y_i\sim\mathrm{Geom}(p)$ indipendenti.
- Il numero di **prove** $Y_1+\dots+Y_n$ ha media $\frac np$ (è il valore riportato, impropriamente, nella dispensa).
- $NB(p,1)$ = geometrica − 1.

## Collegamenti

- **Concetti correlati**: [[Distribuzione Geometrica]] · [[Distribuzione Binomiale]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[07 - PS - Pascal, Geometrica, Massimo e Minimo#Variabili aleatorie di Pascal|Lezione 7 — Variabili aleatorie di Pascal]]
