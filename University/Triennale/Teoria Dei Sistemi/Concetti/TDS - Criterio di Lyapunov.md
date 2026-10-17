---
title: TDS - Criterio di Lyapunov
tags:
  - teoria-dei-sistemi
  - concetto
  - stabilita
  - sistemi-non-lineari
---

# TDS - Criterio di Lyapunov

> [!summary] In breve
> Se esiste $V(x)>0$ con $\dot V<0$ (o $\Delta V<0$ nel discreto) l\'equilibrio è asintoticamente stabile; con $\dot V\le0$ semplicemente stabile. Per i sistemi lineari è necessario e sufficiente.

- Idea: un'energia che diminuisce lungo il moto. $\dot V=\nabla V\cdot f(x)$, senza risolvere il sistema.
- Solo sufficiente: se non si trova $V$, non si conclude nulla.
- Globale: $V$ radialmente illimitata (e $\dot V<0$ ovunque); La Salle per $\dot V\le0$.
- Lineare continuo: $A'Q+QA=-P$, $Q=\int_0^\infty e^{A't}Pe^{At}dt$.
- Lineare discreto: $A'QA-Q=-P$, $Q=\sum_t(A')^tPA^t$.

## Collegamenti

- **Concetti correlati**: [[TDS - Linearizzazione]] · [[TDS - Stabilità]] · [[TDS - Punti di equilibrio]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[13 - TDS - Criterio di Lyapunov e stabilità nel tempo discreto#Criterio di Lyapunov|Lezione 13 — Criterio di Lyapunov]]
> - [[13 - TDS - Criterio di Lyapunov e stabilità nel tempo discreto#Criterio di Lyapunov per i sistemi lineari|Lezione 13 — Criterio di Lyapunov per i sistemi lineari]]
> - [[14 - TDS - Stabilità nel tempo discreto ed esempi#Criterio di Lyapunov per tempo discreto|Lezione 14 — Criterio di Lyapunov per tempo discreto]]
