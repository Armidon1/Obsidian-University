---
title: Matrice jacobiana
tags:
  - analisi-1
  - concetto
  - più-variabili
  - derivate
---

# Matrice jacobiana

> [!summary] In breve
> Per f : ℝᴺ → ℝᴹ, J_f è la matrice M×N delle derivate parziali ∂fᵢ/∂xⱼ (righe = gradienti delle componenti); generalizza la derivata e rende la regola della catena un prodotto di matrici.

$$J_f = \begin{pmatrix} \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_N} \\ \vdots & & \vdots \\ \frac{\partial f_M}{\partial x_1} & \cdots & \frac{\partial f_M}{\partial x_N} \end{pmatrix}, \qquad f(x) = f(x_0) + J_f(x_0)(x - x_0) + o(\|x - x_0\|)$$

- **Catena**: $J_{g\circ f}(x_0) = J_g(f(x_0))\,J_f(x_0)$.
- **Inversa locale**: $\det J_f(x_0) \neq 0 \Rightarrow$ $f$ invertibile vicino a $x_0$ con $J_{f^{-1}} = J_f^{-1}$.
- $|\det J|$ è il fattore di scala delle aree/volumi negli integrali multipli.

## Collegamenti

- **Concetti correlati**: [[Trasformazione regolare di coordinate]] · [[Cambiamento di variabili negli integrali multipli]] · [[Gradiente]] · [[Regole di derivazione]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[09 - AN1 - Funzioni a Valori Vettoriali#Matrice jacobiana|Lezione 9 — Matrice jacobiana]]
> - [[09 - AN1 - Funzioni a Valori Vettoriali#Derivata della funzione composta|Lezione 9 — Derivata della funzione composta]]
