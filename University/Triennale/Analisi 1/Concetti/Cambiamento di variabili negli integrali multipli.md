---
title: Cambiamento di variabili negli integrali multipli
tags:
  - analisi-1
  - concetto
  - integrali
  - più-variabili
---

# Cambiamento di variabili negli integrali multipli

> [!summary] In breve
> ∬_X f dx dy = ∬_{X'} f(φ(u, v)) |det J_φ(u, v)| du dv: il valore assoluto del determinante jacobiano misura come φ deforma le aree.

$$\iint_X f(x, y)\,dx\,dy = \iint_{X'} f(\varphi(u, v))\,|\det J_\varphi(u, v)|\,du\,dv$$

- Giustificazione: un quadratino $du\,dv$ va in un parallelogramma di area $|\det(\varphi_u, \varphi_v)|\,du\,dv$.
- Polari: $dx\,dy = \rho\,d\rho\,d\vartheta$ (non dimenticare $\rho$!). Esempi: $\iint xy$ su un settore $= \frac1{16}$; $\int e^{-x^2} = \sqrt\pi$; area $\frac12\int R^2(\vartheta)d\vartheta$ (spirale: $\frac43\pi^3$).
- Variabili su misura: $u = xy$, $v = \frac yx$ con $\det J_\varphi = \frac{1}{2v}$.
- $\det J_\varphi = \frac{1}{\det J_{\varphi^{-1}}}$.
- Stessa formula in $\mathbb{R}^3$ (cilindriche, sferiche).

## Collegamenti

- **Concetti correlati**: [[Coordinate polari]] · [[Matrice jacobiana]] · [[Integrazione per sostituzione]] · [[Coordinate cilindriche e sferiche]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[10 - AN1 - Integrali Multipli#Cambiamento di Variabili negli Integrali Doppi|Lezione 10 — Cambiamento di Variabili negli Integrali Doppi]]
> - [[10 - AN1 - Integrali Multipli#Altri esempi: aree in polari e l'integrale di Gauss|Lezione 10 — Altri esempi: aree in polari e l'integrale di Gauss]]
> - [[10 - AN1 - Integrali Multipli#Cambiamento di variabili negli integrali tripli|Lezione 10 — Cambiamento di variabili negli integrali tripli]]
