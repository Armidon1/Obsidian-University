---
title: Varianza della Somma
tags:
  - probabilita-e-statistica
  - concetto
  - varianza
  - covarianza
---

# Varianza della Somma

> [!summary] In breve
> $\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)+2\mathrm{Cov}(X,Y)$; se le v.a. sono indipendenti (o solo incorrelate) le varianze si sommano.

$$\mathrm{Var}\Big(\sum_iX_i\Big)=\sum_i\mathrm{Var}(X_i)+\sum_{i\ne j}\mathrm{Cov}(X_i,X_j)$$
$$\mathrm{Var}(X-Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)-2\mathrm{Cov}(X,Y)$$

- Attenzione: $\mathrm{Var}(X+X)=4\mathrm{Var}(X)$, non $2\mathrm{Var}(X)$.
- Usi: varianza della binomiale ($np(1-p)$), della media campionaria ($\sigma^2/n$), dell'ipergeometrica (covarianze negative).

## Collegamenti

- **Concetti correlati**: [[Variance]] · [[Covariance]] · [[Media Campionaria]] · [[Distribuzione Ipergeometrica]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[04 - PS - Valore Atteso, Varianza e Covarianza#Covarianza e varianza della somma|Lezione 4 — Covarianza e varianza della somma]]
> - [[04 - PS - Valore Atteso, Varianza e Covarianza#Formula della varianza di una somma|Lezione 4 — Formula della varianza di una somma]]
