---
title: Assenza di Memoria
tags:
  - probabilita-e-statistica
  - concetto
  - geometrica
  - assenza-di-memoria
---

# Assenza di Memoria

> [!summary] In breve
> $P(X=k+m\mid X>k)=P(X=m)$: per una geometrica, aver già aspettato non cambia l'attesa residua.

$$P(X>x+y\mid X>y)=P(X>x)$$

- Dimostrazione: $\frac{P(X=k+m)}{P(X>k)}=\frac{p(1-p)^{k+m-1}}{(1-p)^k}=p(1-p)^{m-1}$.
- Unica distribuzione discreta priva di memoria (nel continuo: l'esponenziale).
- Niente "numeri ritardatari" al lotto.

## Collegamenti

- **Concetti correlati**: [[Distribuzione Geometrica]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[07 - PS - Pascal, Geometrica, Massimo e Minimo#Assenza di memoria|Lezione 7 — Assenza di memoria]]
