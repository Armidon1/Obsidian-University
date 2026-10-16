---
title: Integrazione per parti
tags:
  - analisi-1
  - concetto
  - integrali
  - metodi-di-integrazione
---

# Integrazione per parti

> [!summary] In breve
> ∫ f'g = fg − ∫ fg': inverte la regola del prodotto; si sposta la derivata sul fattore "complicato" con derivata semplice (ln, arctan, polinomi).

$$\int f'(x) g(x)\,dx = f(x)g(x) - \int f(x)g'(x)\,dx, \qquad \int_a^b f'g = \big[fg\big]_a^b - \int_a^b fg'$$

- **Trucco del fattore 1**: $\int \ln x = x\ln x - x$, $\int \arctan x = x\arctan x - \frac12\ln(1+x^2)$.
- **Integrali ciclici**: $\int e^x\cos x = \frac{e^x(\sin x + \cos x)}{2}$ (si ottiene $I = E - I$).
- $\int \cos^2 x = \frac{\sin x\cos x + x}{2}$ (con $\sin^2 = 1 - \cos^2$).
- Scelta: $f' = e^x$, $g = x$ in $\int xe^x$ (il contrario peggiora).

## Collegamenti

- **Concetti correlati**: [[Integrazione per sostituzione]] · [[Primitiva]] · [[Regole di derivazione]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[06 - AN1 - Calcolo Integrale#Integrazione per parti|Lezione 6 — Integrazione per parti]]
