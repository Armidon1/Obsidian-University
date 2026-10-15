---
title: Somma di Poisson Indipendenti
tags:
  - probabilita-e-statistica
  - concetto
  - poisson
---

# Somma di Poisson Indipendenti

> [!summary] In breve
> La somma di Poisson indipendenti di parametri $\lambda_1,\dots,\lambda_n$ è Poisson di parametro $\lambda_1+\dots+\lambda_n$ (riproducibilità).

$$P(U+V=k)=\sum_{i=0}^ke^{-\lambda}\frac{\lambda^i}{i!}e^{-\mu}\frac{\mu^{k-i}}{(k-i)!}=e^{-(\lambda+\mu)}\frac{(\lambda+\mu)^k}{k!}$$

- Dimostrazione: scomposizione $\{U+V=k\}=\bigcup_i\{U=i,V=k-i\}$, indipendenza, binomio di Newton.
- Condizionando alla somma: $Y_1\mid Y=n\sim B(n,\lambda_1/\lambda)$.

## Collegamenti

- **Concetti correlati**: [[Distribuzione di Poisson]] · [[Suddivisione di una Poisson]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[08 - PS - Distribuzione di Poisson#Somma di Poisson indipendenti|Lezione 8 — Somma di Poisson indipendenti]]
> - [[08 - PS - Distribuzione di Poisson#Distribuzione di una Poisson condizionata alla somma di Poisson|Lezione 8 — Distribuzione di una Poisson condizionata alla somma di Poisson]]
