---
title: Funzioni circolari inverse
tags:
  - analisi-1
  - concetto
  - funzioni-elementari
  - trigonometria
---

# Funzioni circolari inverse

> [!summary] In breve
> arcsin, arccos e arctan sono le inverse di sin, cos e tan ristrette a intervalli di monotonia ([−π/2, π/2], [0, π], (−π/2, π/2)).

| Funzione | Dominio → immagine | Derivata |
|---|---|---|
| $\arcsin$ | $[-1, 1] \to [-\frac\pi2, \frac\pi2]$ | $\frac{1}{\sqrt{1 - x^2}}$ |
| $\arccos$ | $[-1, 1] \to [0, \pi]$ | $\frac{-1}{\sqrt{1 - x^2}}$ |
| $\arctan$ | $\mathbb{R} \to (-\frac\pi2, \frac\pi2)$ | $\frac{1}{1 + x^2}$ |

- $\arcsin(\sin x) = x$ solo per $x \in [-\frac\pi2, \frac\pi2]$.
- $\arctan x + \arctan\frac1x = \pm\frac\pi2$ (segno di $x$).
- $\int \frac{dx}{1+x^2} = \arctan x + c$: compare nell'integrazione delle funzioni razionali.

## Collegamenti

- **Concetti correlati**: [[Funzioni circolari]] · [[Funzione inversa]] · [[Integrazione di funzioni razionali]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[04 - AN1 - Funzioni Continue#Inverse delle funzioni circolari|Lezione 4 — Inverse delle funzioni circolari]]
> - [[05 - AN1 - Calcolo Differenziale#Derivazione delle funzioni inverse|Lezione 5 — Derivazione delle funzioni inverse]]
> - [[05 - AN1 - Calcolo Differenziale#Caratterizzazione delle funzioni costanti|Lezione 5 — Caratterizzazione delle funzioni costanti]]
