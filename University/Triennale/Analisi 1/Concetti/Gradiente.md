---
title: Gradiente
tags:
  - analisi-1
  - concetto
  - più-variabili
  - derivate
---

# Gradiente

> [!summary] In breve
> ∇f = (∂f/∂x₁, …, ∂f/∂x_N): punta nella direzione di massima crescita di f, la sua norma è la pendenza massima, ed è ortogonale alle curve di livello.

$$\nabla f(x_0) = Df(x_0) = \left(\frac{\partial f}{\partial x_1}(x_0), \dots, \frac{\partial f}{\partial x_N}(x_0)\right)$$

- **Teorema del gradiente**: $\frac{\partial f}{\partial v} = \nabla f \cdot v$ (se $f$ è differenziabile).
- $\max_{\|v\|=1} \frac{\partial f}{\partial v} = \|\nabla f\|$, raggiunto per $v = \frac{\nabla f}{\|\nabla f\|}$; $-\nabla f$ è la direzione di massima discesa ([[Gradient Descent]]).
- $\nabla f \perp$ curve di livello.
- Punti critici: $\nabla f(x_0) = 0$ ([[Teorema di Fermat]] in $\mathbb{R}^N$).

## Collegamenti

- **Concetti correlati**: [[Derivate parziali]] · [[Derivata direzionale]] · [[Curve di livello]] · [[Gradient Descent]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[08 - AN1 - Calcolo Differenziale in più Variabili#Gradiente|Lezione 8 — Gradiente]]
> - [[08 - AN1 - Calcolo Differenziale in più Variabili#Proprietà geometriche del gradiente|Lezione 8 — Proprietà geometriche del gradiente]]
