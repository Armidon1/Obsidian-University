---
title: Binomio di Newton
tags:
  - analisi-1
  - concetto
  - combinatoria
---

# Binomio di Newton

> [!summary] In breve
> (a + b)^n = Σ (n su k) a^k b^(n−k): i coefficienti dello sviluppo di una potenza di binomio sono i coefficienti binomiali.

$$(a + b)^n = \sum_{k=0}^n \binom nk a^k b^{n-k}$$

- Esempio: $(a + b)^4 = b^4 + 4ab^3 + 6a^2b^2 + 4a^3b + a^4$.
- Usi nel corso: $(x^n)' = nx^{n-1}$ dal rapporto incrementale; limitatezza di $\left(1 + \frac1n\right)^n$.
- Si generalizza a esponenti reali con Taylor: $(1 + x)^\alpha = \sum_k \binom\alpha k x^k + o(x^n)$.

## Collegamenti

- **Concetti correlati**: [[Coefficiente binomiale]] · [[Numero di Nepero]] · [[Formula di Taylor]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[00 - AN1 - Concetti Fondamentali#La formula|Lezione 0 — La formula]]
> - [[05 - AN1 - Calcolo Differenziale#Derivate delle funzioni elementari|Lezione 5 — Derivate delle funzioni elementari]]
