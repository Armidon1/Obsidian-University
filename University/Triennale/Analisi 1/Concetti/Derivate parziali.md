---
title: Derivate parziali
tags:
  - analisi-1
  - concetto
  - più-variabili
  - derivate
---

# Derivate parziali

> [!summary] In breve
> ∂f/∂xᵢ è la derivata di f rispetto a xᵢ tenendo ferme le altre variabili: la pendenza di f lungo la direzione dell'asse i.

$$\frac{\partial f}{\partial x_i}(x_0) = \lim_{h\to0} \frac{f(x_0 + he_i) - f(x_0)}{h}$$

- Si calcolano derivando in modo ordinario e trattando le altre variabili come costanti: $f = 2x^3y - y^2 + 3xy \Rightarrow f_x = 6x^2y + 3y$, $f_y = 2x^3 - 2y + 3x$.
- Geometricamente: pendenza della curva ottenuta tagliando il grafico con il piano $y = y_0$ (per $f_x$).

> [!warning] Derivabile non implica continua
> $\frac{xy}{x^2+y^2}$ (con $f(0,0) = 0$) ha $f_x(0,0) = f_y(0,0) = 0$ ma non è continua in $(0, 0)$. Serve la [[Differenziabilità]].

## Collegamenti

- **Concetti correlati**: [[Gradiente]] · [[Differenziabilità]] · [[Derivata direzionale]] · [[Matrice hessiana]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[08 - AN1 - Calcolo Differenziale in più Variabili#Derivate parziali|Lezione 8 — Derivate parziali]]
