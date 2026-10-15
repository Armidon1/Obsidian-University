---
title: Approssimazione Normale
tags:
  - probabilita-e-statistica
  - concetto
  - normale
  - approssimazione-normale
---

# Approssimazione Normale

> [!summary] In breve
> Per il TLC, la binomiale con $np(1-p)\ge10$ e la Poisson con $\lambda\ge10$ si approssimano con una normale di stessa media e varianza.

| Distribuzione | Condizione | Approssimazione |
|---|---|---|
| $B(n,p)$ | $np(1-p)\ge10$ | $\frac{X-np}{\sqrt{np(1-p)}}\dot\sim N(0,1)$ |
| $\mathrm{Poi}(\lambda)$ | $\lambda\ge10$ | $\frac{X-\lambda}{\sqrt\lambda}\dot\sim N(0,1)$ |

- Con $n$ grande ma $np$ piccolo usare Poisson, non la normale.
- Per valori singoli usare la correzione di continuità: $P(X=k)\approx P(k-\frac12<Y<k+\frac12)$.

## Collegamenti

- **Concetti correlati**: [[Teorema del Limite Centrale]] · [[Approssimazione di Poisson della Binomiale]] · [[Distribuzione Binomiale]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[09 - PS - Distribuzione Normale e Teorema del Limite Centrale#Approssimazione normale della binomiale|Lezione 9 — Approssimazione normale della binomiale]]
> - [[09 - PS - Distribuzione Normale e Teorema del Limite Centrale#Approssimazione normale della Poisson|Lezione 9 — Approssimazione normale della Poisson]]
> - [[10 - PS - Formulario e Domande d'Orale#Quale approssimazione usare|Lezione 10 — Quale approssimazione usare]]
