---
title: Notazione O grande
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - notazione-asintotica
---

# Notazione O grande

> [!summary] In breve
> $f \in O(g)$ se esistono $c > 0$ ed $n_0$ tali che $f(n) \le c \cdot g(n)$ per ogni $n \ge n_0$: "$f$ cresce al più come $g$". È un **upper bound**.

$$O(g(n)) = \{\, f \mid (\exists c > 0)(\exists n_0)(\forall n \ge n_0)\ f(n) \le c\,g(n) \,\}$$

- $O(g)$ è un **insieme** di funzioni: si scrive $f = O(g)$ per abuso di notazione.
- Costanti moltiplicative e additive non contano; conta il termine dominante: $n^3 + 100n^2 \in O(n^3)$.
- Gerarchia: $\log n \in O(n^a) \subset O(2^{n^b})$.
- Se $f \in O(n)$ allora anche $f \in O(n^2)$: interessa il bound più stretto.

## Collegamenti

- **Concetti correlati**: [[Notazione Omega]] · [[Notazione Theta]] · [[Notazione asintotica]] · [[Delimitazioni superiori e inferiori]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[02 - MC - Notazione asintotica#Le notazioni O, Ω, Θ|Lezione 2 — Le notazioni O, Ω, Θ]]
> - [[02 - MC - Notazione asintotica#Regole pratiche per confrontare funzioni|Lezione 2 — Regole pratiche per confrontare funzioni]]
> - [[02 - MC - Notazione asintotica#Analisi asintotica e la notazione O|Lezione 2 — Analisi asintotica e la notazione O]]
