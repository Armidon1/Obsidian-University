---
title: Suddivisione di una Poisson
tags:
  - probabilita-e-statistica
  - concetto
  - poisson
---

# Suddivisione di una Poisson

> [!summary] In breve
> Se $N\sim\mathrm{Poi}(\lambda)$ eventi sono classificati indipendentemente nei tipi $1..r$ con probabilità $p_i$, i conteggi per tipo sono Poisson indipendenti di medie $\lambda p_i$.

$$P(N_1=n,N_2=m)=\frac{(\lambda p)^n}{n!}e^{-\lambda p}\cdot\frac{(\lambda q)^m}{m!}e^{-\lambda q}$$

- Si condiziona a $N=n+m$: $N_1\mid N\sim B(n+m,p)$.
- La congiunta si fattorizza → $N_1$, $N_2$ **indipendenti** (sorprendente: con $N$ fisso non lo sarebbero).
- Esempio: transistor difettosi $\mathrm{Poi}(10^5\cdot2\cdot10^{-5})=\mathrm{Poi}(2)$.

## Collegamenti

- **Concetti correlati**: [[Distribuzione di Poisson]] · [[Somma di Poisson Indipendenti]] · [[Distribuzione Binomiale]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[08 - PS - Distribuzione di Poisson#Somma di un numero Poisson di Bernoulli indipendenti|Lezione 8 — Somma di un numero Poisson di Bernoulli indipendenti]]
