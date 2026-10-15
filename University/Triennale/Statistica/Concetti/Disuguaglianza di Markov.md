---
title: Disuguaglianza di Markov
tags:
  - probabilita-e-statistica
  - concetto
  - disuguaglianze
---

# Disuguaglianza di Markov

> [!summary] In breve
> Se $X\ge0$, per ogni $a>0$: $P(X\ge a)\le E[X]/a$.

**Dimostrazione (discreto)**
$$E[X]=\sum_ix_ip(x_i)\ge\sum_{x_i\ge a}x_ip(x_i)\ge a\sum_{x_i\ge a}p(x_i)=a\,P(X\ge a)$$

- Usa solo la media; vale per ogni distribuzione non negativa.
- È il mattone da cui si ricava [[Disuguaglianza di Chebyshev]].

## Collegamenti

- **Concetti correlati**: [[Disuguaglianza di Chebyshev]] · [[Expected Value]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[05 - PS - Disuguaglianze e Legge dei Grandi Numeri#Disuguaglianza di Markov|Lezione 5 — Disuguaglianza di Markov]]
