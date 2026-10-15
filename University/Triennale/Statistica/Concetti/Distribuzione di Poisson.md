---
title: Distribuzione di Poisson
tags:
  - probabilita-e-statistica
  - concetto
  - distribuzioni
  - poisson
---

# Distribuzione di Poisson

> [!summary] In breve
> Numero di eventi rari in un intervallo, noto il numero medio $\lambda$: $P(X=i)=\frac{\lambda^i}{i!}e^{-\lambda}$, con media e varianza pari a $\lambda$.

| PMF | $E[X]$ | $\mathrm{Var}(X)$ |
|---|:-:|:-:|
| $\frac{\lambda^i}{i!}e^{-\lambda}$, $i\ge0$ | $\lambda$ | $\lambda$ |

- $\lambda$ proporzionale alla lunghezza dell'intervallo.
- Ricorsione: $P(X=i+1)=\frac\lambda{i+1}P(X=i)$, da $P(X=0)=e^{-\lambda}$.
- Esempi: refusi, chiamate a un call-center, guasti, particelle emesse.

## Collegamenti

- **Concetti correlati**: [[Approssimazione di Poisson della Binomiale]] · [[Somma di Poisson Indipendenti]] · [[Suddivisione di una Poisson]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[08 - PS - Distribuzione di Poisson#Variabile aleatoria di Poisson|Lezione 8 — Variabile aleatoria di Poisson]]
> - [[08 - PS - Distribuzione di Poisson#Valore atteso e varianza|Lezione 8 — Valore atteso e varianza]]
> - [[08 - PS - Distribuzione di Poisson#Calcolo esplicito della distribuzione di Poisson|Lezione 8 — Calcolo esplicito della distribuzione di Poisson]]
