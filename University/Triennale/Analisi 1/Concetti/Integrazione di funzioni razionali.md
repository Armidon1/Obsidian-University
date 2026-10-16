---
title: Integrazione di funzioni razionali
tags:
  - analisi-1
  - concetto
  - integrali
  - metodi-di-integrazione
---

# Integrazione di funzioni razionali

> [!summary] In breve
> Per ∫ p/q: si divide se grado(p) ≥ grado(q), poi si scompone r/q in fratti semplici secondo il segno del discriminante di q; restano solo log e arctan.

1. Divisione: $\frac pq = s + \frac rq$, $\deg r < \deg q$.
2. Linearità: $\int s$ è un polinomio.
3. $q(x) = ax^2 + bx + c$:

| $\Delta$ | Scomposizione | Primitiva |
|---|---|---|
| $> 0$ | $\frac{A}{x - x_1} + \frac{B}{x - x_2}$ | $A\ln\lvert x - x_1\rvert + B\ln\lvert x - x_2\rvert$ |
| $= 0$ | $\frac{A}{x - x_0} + \frac{B}{(x - x_0)^2}$ | $A\ln\lvert x - x_0\rvert - \frac{B}{x - x_0}$ |
| $< 0$ | $\frac{Aq' + B}{q}$ | $A\ln\lvert q\rvert + \frac{\beta B}{\gamma}\arctan\frac{x + \alpha}{\beta}$ |

con $q = \gamma\left(1 + \left(\frac{x + \alpha}{\beta}\right)^2\right)$ (completamento del quadrato). Le costanti si trovano confrontando i coefficienti.

## Collegamenti

- **Concetti correlati**: [[Primitiva]] · [[Funzioni circolari inverse]] · [[Numeri complessi]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[06 - AN1 - Calcolo Integrale#Integrazione di Funzioni Razionali|Lezione 6 — Integrazione di Funzioni Razionali]]
