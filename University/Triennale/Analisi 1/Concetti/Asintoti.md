---
title: Asintoti
tags:
  - analisi-1
  - concetto
  - studio-di-funzione
---

# Asintoti

> [!summary] In breve
> Rette a cui il grafico si avvicina indefinitamente: verticali (f → ±∞ per x → c), orizzontali (f → l per x → ±∞), obliqui y = mx + q con m = lim f/x e q = lim (f − mx).

| Tipo | Condizione |
|---|---|
| verticale $x = c$ | $\lim_{x\to c^\pm} f(x) = \pm\infty$ |
| orizzontale $y = l$ | $\lim_{x\to\pm\infty} f(x) = l \in \mathbb{R}$ |
| obliquo $y = mx + q$ | $m = \lim_{x\to\pm\infty} \frac{f(x)}{x} \neq 0$, $q = \lim_{x\to\pm\infty}(f(x) - mx)$ finiti |

- Esempi: $\tan$ ha asintoti verticali in $\frac\pi2 + k\pi$; $\tanh$ ha $y = \pm1$; $\ln(e^{3x+2} + 5)$ ha $y = 3x + 2$ a $+\infty$.
- Un asintoto obliquo esclude quello orizzontale dalla stessa parte.

## Collegamenti

- **Concetti correlati**: [[Studio di funzione]] · [[Limite di funzione]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[03 - AN1 - Funzioni Reali di una Variabile Reale#Limiti ed asintoti|Lezione 3 — Limiti ed asintoti]]
> - [[05 - AN1 - Calcolo Differenziale#Asintoti obliqui|Lezione 5 — Asintoti obliqui]]
