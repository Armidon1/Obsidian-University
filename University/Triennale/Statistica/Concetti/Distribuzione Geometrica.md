---
title: Distribuzione Geometrica
tags:
  - probabilita-e-statistica
  - concetto
  - distribuzioni
  - geometrica
---

# Distribuzione Geometrica

> [!summary] In breve
> Numero di prove fino al primo successo: $P(X=k)=p(1-p)^{k-1}$, $k\ge1$.

| PMF | $E[X]$ | $\mathrm{Var}(X)$ | CDF |
|---|:-:|:-:|:-:|
| $pq^{k-1}$ | $\frac1p$ | $\frac q{p^2}$ | $1-(1-p)^k$ |

- $P(X>k)=(1-p)^k$ (le prime $k$ prove falliscono).
- Media: derivata della serie geometrica $\sum q^i=\frac1{1-q}$.
- Priva di memoria; il minimo di geometriche indipendenti è geometrico.
- Variante "fallimenti": $P(Y=k)=p(1-p)^k$, $k\ge0$.

## Collegamenti

- **Concetti correlati**: [[Assenza di Memoria]] · [[Massimo e Minimo di Variabili Indipendenti]] · [[Distribuzione di Pascal]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[07 - PS - Pascal, Geometrica, Massimo e Minimo#Variabili aleatorie geometriche|Lezione 7 — Variabili aleatorie geometriche]]
> - [[07 - PS - Pascal, Geometrica, Massimo e Minimo#Valore atteso|Lezione 7 — Valore atteso]]
> - [[07 - PS - Pascal, Geometrica, Massimo e Minimo#Varianza|Lezione 7 — Varianza]]
