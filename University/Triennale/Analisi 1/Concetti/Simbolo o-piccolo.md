---
title: Simbolo o-piccolo
tags:
  - analisi-1
  - concetto
  - limiti
  - taylor
---

# Simbolo o-piccolo

> [!summary] In breve
> f = o(g) per x → x₀ se f/g → 0: f è trascurabile rispetto a g. Indica una qualità (un resto), non una quantità.

- Esempi: $\ln x = o(x)$ ($x \to +\infty$); $1 - \cos x = o(x)$ ($x \to 0$); $x^5 = o(x^4)$ ($x \to 0$).
- $f$ derivabile in $x_0$ $\iff$ $f(x) = f(x_0) + A(x - x_0) + o(x - x_0)$.
- Regole: $c\,o(f) = o(f)$, $o(f) \pm o(f) = o(f)$, $x^m o(x^n) = o(x^{m+n})$, $o(x^m) = o(x^n)$ per $m \ge n$.

> [!warning] Non è un numero
> $o(f) - o(f) \neq 0$, e $o(x^4) = o(x^2)$ ma non viceversa.

## Collegamenti

- **Concetti correlati**: [[Formula di Taylor]] · [[Successioni asintotiche]] · [[Notazione asintotica]] · [[Derivata]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[05 - AN1 - Calcolo Differenziale#Il simbolo o-piccolo|Lezione 5 — Il simbolo o-piccolo]]
> - [[05 - AN1 - Calcolo Differenziale#Calcolo dei limiti con Taylor|Lezione 5 — Calcolo dei limiti con Taylor]]
