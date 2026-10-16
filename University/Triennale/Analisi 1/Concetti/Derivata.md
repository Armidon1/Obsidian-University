---
title: Derivata
tags:
  - analisi-1
  - concetto
  - derivate
---

# Derivata

> [!summary] In breve
> f'(x₀) = lim (f(x₀+h) − f(x₀))/h: la pendenza della retta tangente e il tasso di variazione istantaneo. Derivabile ⇒ continua, non viceversa.

$$f'(x_0) = \lim_{h\to0} \frac{f(x_0 + h) - f(x_0)}{h}, \qquad t(x) = f(x_0) + f'(x_0)(x - x_0)$$

- Equivalente: $f(x) = f(x_0) + f'(x_0)(x - x_0) + o(x - x_0)$ (migliore approssimazione lineare).
- Derivata destra/sinistra: $|x|$ ha $f'_\pm(0) = \pm1$ (punto angoloso).
- Derivate successive $f'', \dots, f^{(n)}$; classi $C^n$.
- Il metodo di Newton $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$ usa la tangente (Erone è un caso particolare).

| $f$ | $f'$ |
|---|---|
| $x^r$ | $rx^{r-1}$ |
| $e^x$ | $e^x$ |
| $\ln x$ | $\frac1x$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |

## Collegamenti

- **Concetti correlati**: [[Regole di derivazione]] · [[Simbolo o-piccolo]] · [[Teorema di Lagrange]] · [[Derivate parziali]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[05 - AN1 - Calcolo Differenziale#Il problema della tangente|Lezione 5 — Il problema della tangente]]
> - [[05 - AN1 - Calcolo Differenziale#Derivata, definizione e prime proprietà|Lezione 5 — Derivata, definizione e prime proprietà]]
> - [[05 - AN1 - Calcolo Differenziale#Derivabilità e continuità|Lezione 5 — Derivabilità e continuità]]
