---
title: Formula di Taylor
tags:
  - analisi-1
  - concetto
  - taylor
---

# Formula di Taylor

> [!summary] In breve
> f(x) = Σ_{k≤n} f⁽ᵏ⁾(x₀)/k! (x − x₀)^k + Rₙ(x): il polinomio di grado ≤ n che meglio approssima f vicino a x₀, con resto di Peano o(·) o di Lagrange.

$$T_n(x) = \sum_{k=0}^n \frac{f^{(k)}(x_0)}{k!}(x - x_0)^k, \qquad R_n = o((x - x_0)^n) \ \ (\text{Peano}) = \frac{f^{(n+1)}(c)}{(n+1)!}(x - x_0)^{n+1} \ \ (\text{Lagrange})$$

| Sviluppo ($x \to 0$) | |
|---|---|
| $e^x$ | $1 + x + \frac{x^2}{2} + \frac{x^3}{6} + o(x^3)$ |
| $\sin x$ | $x - \frac{x^3}{6} + o(x^4)$ |
| $\cos x$ | $1 - \frac{x^2}{2} + \frac{x^4}{24} + o(x^5)$ |
| $\ln(1+x)$ | $x - \frac{x^2}{2} + \frac{x^3}{3} + o(x^3)$ |
| $\arctan x$ | $x - \frac{x^3}{3} + o(x^4)$ |
| $\sqrt{1+x}$ | $1 + \frac x2 - \frac{x^2}{8} + o(x^2)$ |

Applicazioni: limiti (sviluppare il denominatore, poi il numeratore allo stesso ordine), estremi locali ($f^{(n)}(x_0)$ con $n$ pari/dispari), calcolo numerico con stima dell'errore ($\cos\frac12 \approx \frac{337}{384}$, $\sqrt{30} \approx \frac{219}{40}$).

## Collegamenti

- **Concetti correlati**: [[Simbolo o-piccolo]] · [[Serie di Taylor]] · [[Derivata]] · [[Limiti notevoli]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[05 - AN1 - Calcolo Differenziale#Polinomio di Taylor|Lezione 5 — Polinomio di Taylor]]
> - [[05 - AN1 - Calcolo Differenziale#Sviluppi di Taylor notevoli|Lezione 5 — Sviluppi di Taylor notevoli]]
> - [[05 - AN1 - Calcolo Differenziale#Calcolo dei limiti con Taylor|Lezione 5 — Calcolo dei limiti con Taylor]]
> - [[05 - AN1 - Calcolo Differenziale#Calcolo numerico|Lezione 5 — Calcolo numerico]]
