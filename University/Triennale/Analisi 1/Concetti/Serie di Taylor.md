---
title: Serie di Taylor
tags:
  - analisi-1
  - concetto
  - taylor
  - serie
---

# Serie di Taylor

> [!summary] In breve
> Se f ∈ C^∞ e |f⁽ᵏ⁾| ≤ M^k, allora f(x) = Σ f⁽ᵏ⁾(x₀)/k! (x − x₀)^k: f è un "polinomio di grado infinito".

| Serie | Validità |
|---|---|
| $e^x = \sum \frac{x^k}{k!}$ | $\mathbb{R}$ |
| $\sin x = \sum (-1)^k \frac{x^{2k+1}}{(2k+1)!}$ | $\mathbb{R}$ |
| $\cos x = \sum (-1)^k \frac{x^{2k}}{(2k)!}$ | $\mathbb{R}$ |
| $\ln(1+x) = \sum_{k\ge1} (-1)^{k+1}\frac{x^k}{k}$ | $(-1, 1)$ |
| $\arctan x = \sum (-1)^k \frac{x^{2k+1}}{2k+1}$ | $(-1, 1)$ |
| $(1+x)^\alpha = \sum \binom\alpha k x^k$ | $(-1, 1)$ |

- Il resto di Lagrange tende a $0$ per il criterio del rapporto.
- Con $x = 1$: $e = \sum \frac1{k!}$. Con $x = i\vartheta$: la formula di Eulero $e^{i\vartheta} = \cos\vartheta + i\sin\vartheta$.

## Collegamenti

- **Concetti correlati**: [[Formula di Taylor]] · [[Serie numerica]] · [[Numero di Nepero]] · [[Numeri complessi]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[05 - AN1 - Calcolo Differenziale#Serie di Taylor|Lezione 5 — Serie di Taylor]]
> - [[11 - AN1 - Numeri Complessi#Formula di Eulero|Lezione 11 — Formula di Eulero]]
