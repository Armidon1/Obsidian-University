---
title: Notazione Omega
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - notazione-asintotica
---

# Notazione Omega

> [!summary] In breve
> $f \in \Omega(g)$ se esistono $c > 0$ ed $n_0$ tali che $f(n) \ge c \cdot g(n)$ per ogni $n \ge n_0$: "$f$ cresce almeno come $g$". È un **lower bound**.

$$\Omega(g(n)) = \{\, f \mid (\exists c > 0)(\exists n_0)(\forall n \ge n_0)\ f(n) \ge c\,g(n) \,\}$$

- $f \in O(g) \iff g \in \Omega(f)$.
- Le costanti si fissano **prima** del "per ogni $n$": con l'ordine invertito ogni funzione sarebbe $\Omega$ di ogni altra.
- Il lower bound di un **algoritmo** non è il lower bound del **problema** (vedi [[Delimitazioni superiori e inferiori]]).

## Collegamenti

- **Concetti correlati**: [[Notazione O grande]] · [[Notazione Theta]] · [[Delimitazioni superiori e inferiori]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[02 - MC - Notazione asintotica#Le notazioni O, Ω, Θ|Lezione 2 — Le notazioni O, Ω, Θ]]
> - [[02 - MC - Notazione asintotica#Proprietà delle notazioni|Lezione 2 — Proprietà delle notazioni]]
