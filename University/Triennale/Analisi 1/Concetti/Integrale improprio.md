---
title: Integrale improprio
tags:
  - analisi-1
  - concetto
  - integrali
---

# Integrale improprio

> [!summary] In breve
> Integrale su un intervallo illimitato o di una funzione illimitata, definito come limite: ∫ₐᵇ f = lim_{c→b⁻} ∫ₐᶜ f. Si studia con il confronto, come le serie.

| Integrale | Converge per |
|---|---|
| $\int_1^{+\infty} \frac{dx}{x^\alpha}$ | $\alpha > 1$ (vale $\frac{1}{\alpha - 1}$) |
| $\int_0^1 \frac{dx}{x^\alpha}$ | $\alpha < 1$ (vale $\frac{1}{1 - \alpha}$) |

- **Confronto**: $|f| \le g$ e $\int g$ converge $\Rightarrow$ $\int f$ converge.
- Con due estremi critici si spezza: $\int_{-\infty}^{+\infty} e^{-x^2}\,dx = \sqrt\pi$ (maggiorante $2xe^{-x^2}$ per $x \ge 1$).
- $\int_0^{+\infty} \frac{\sin x}{x}\,dx$ converge (per parti), ma non assolutamente.

## Collegamenti

- **Concetti correlati**: [[Criterio integrale per le serie]] · [[Criterio del confronto per le serie]] · [[Integrale di Riemann]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[06 - AN1 - Calcolo Integrale#Integrali Impropri|Lezione 6 — Integrali Impropri]]
> - [[06 - AN1 - Calcolo Integrale#Criterio del confronto per integrali impropri|Lezione 6 — Criterio del confronto per integrali impropri]]
