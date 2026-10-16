---
title: Criterio integrale per le serie
tags:
  - analisi-1
  - concetto
  - serie
  - integrali
---

# Criterio integrale per le serie

> [!summary] In breve
> Se f ≥ 0 è decrescente su [1, +∞) e aₖ = f(k), allora Σ aₖ converge se e solo se ∫₁^∞ f converge.

$$\int_1^{n+1} f \le \sum_{k=1}^n a_k \le a_1 + \int_1^n f$$

- Si confronta la somma con l'area: rettangoli sopra e sotto la curva.
- Conseguenza: $\sum \frac{1}{k^\alpha}$ converge $\iff$ $\int_1^\infty \frac{dx}{x^\alpha}$ converge $\iff$ $\alpha > 1$.
- Funzione zeta di Riemann $\zeta(s) = \sum k^{-s}$, $s > 1$.

## Collegamenti

- **Concetti correlati**: [[Serie armonica]] · [[Integrale improprio]] · [[Serie numerica]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[06 - AN1 - Calcolo Integrale#Integrali impropri e serie|Lezione 6 — Integrali impropri e serie]]
> - [[02 - AN1 - Serie Numeriche#Serie armonica generalizzata|Lezione 2 — Serie armonica generalizzata]]
