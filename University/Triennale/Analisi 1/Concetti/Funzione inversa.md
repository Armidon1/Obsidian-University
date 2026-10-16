---
title: Funzione inversa
tags:
  - analisi-1
  - concetto
  - funzioni
---

# Funzione inversa

> [!summary] In breve
> Se f è biettiva, f⁻¹ "disfa" f: f⁻¹(f(x)) = x. I grafici sono simmetrici rispetto a y = x; se f è derivabile con f'(x₀) ≠ 0, (f⁻¹)'(y₀) = 1/f'(x₀).

- $f(x) = y \iff x = f^{-1}(y)$; $f^{-1} \neq \frac1f$.
- **Continuità** (Teorema 4.6): $f$ continua e strettamente monotona su un intervallo $\Rightarrow$ $f^{-1}$ continua. Senza intervallo può fallire.
- **Derivata**: $(f^{-1})'(y_0) = \frac{1}{f'(x_0)}$, $y_0 = f(x_0)$. Tangente orizzontale di $f$ ↔ tangente verticale di $f^{-1}$.
- In più variabili: $J_{f^{-1}}(y) = J_f(x)^{-1}$ (invertibilità locale).

| $f$ | $f^{-1}$ | $(f^{-1})'$ |
|---|---|---|
| $e^x$ | $\ln x$ | $\frac1x$ |
| $\sin$ su $[-\frac\pi2, \frac\pi2]$ | $\arcsin$ | $\frac{1}{\sqrt{1-x^2}}$ |
| $\tan$ su $(-\frac\pi2, \frac\pi2)$ | $\arctan$ | $\frac{1}{1+x^2}$ |

## Collegamenti

- **Concetti correlati**: [[Funzione iniettiva, suriettiva e biettiva]] · [[Logaritmo]] · [[Funzioni circolari inverse]] · [[Trasformazione regolare di coordinate]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[03 - AN1 - Funzioni Reali di una Variabile Reale#Funzione inversa|Lezione 3 — Funzione inversa]]
> - [[04 - AN1 - Funzioni Continue#Continuità della funzione inversa|Lezione 4 — Continuità della funzione inversa]]
> - [[05 - AN1 - Calcolo Differenziale#Derivazione delle funzioni inverse|Lezione 5 — Derivazione delle funzioni inverse]]
