---
title: Distribuzione Binomiale
tags:
  - probabilita-e-statistica
  - concetto
  - distribuzioni
  - binomiale
---

# Distribuzione Binomiale

> [!summary] In breve
> Numero di successi in $n$ prove indipendenti con probabilità $p$: $P(X=i)=\binom ni p^i(1-p)^{n-i}$.

| PMF | $E[X]$ | $\mathrm{Var}(X)$ |
|---|:-:|:-:|
| $\binom nip^i(1-p)^{n-i}$, $i=0..n$ | $np$ | $np(1-p)$ |

- $X=\sum_{i=1}^nX_i$ con $X_i\sim B(p)$ indipendenti; estrazione **con** reinserimento.
- $B(n_1,p)+B(n_2,p)=B(n_1+n_2,p)$ se indipendenti.
- Ricorsione: $P(X=k+1)=\frac p{1-p}\cdot\frac{n-k}{k+1}P(X=k)$.
- Approssimazioni: Poisson ($n$ grande, $p$ piccolo), normale ($np(1-p)\ge10$).

## Collegamenti

- **Concetti correlati**: [[Distribuzione di Bernoulli]] · [[Distribuzione Ipergeometrica]] · [[Approssimazione di Poisson della Binomiale]] · [[Approssimazione Normale]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[06 - PS - Bernoulli, Binomiale, Ipergeometrica e Uniforme#Variabili aleatorie binomiali|Lezione 6 — Variabili aleatorie binomiali]]
> - [[06 - PS - Bernoulli, Binomiale, Ipergeometrica e Uniforme#Valore atteso e varianza|Lezione 6 — Valore atteso e varianza]]
> - [[06 - PS - Bernoulli, Binomiale, Ipergeometrica e Uniforme#Calcolo esplicito della distribuzione binomiale|Lezione 6 — Calcolo esplicito della distribuzione binomiale]]
