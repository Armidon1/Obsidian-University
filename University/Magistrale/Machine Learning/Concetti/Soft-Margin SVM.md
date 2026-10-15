---
title: Soft-Margin SVM
tags:
  - machine-learning
  - concetto
  - svm
  - linear-classifiers
---

# Soft-Margin SVM

> [!summary] In short
> Relax the constraints with slack variables $\xi_i\ge0$ paid with weight C; eliminating the slacks gives the unconstrained convex problem $\frac12\lVert\theta\rVert^2+\frac Cn\sum_i(1-y_i\theta^Tx_i)_+$, solved by stochastic sub-gradient descent.

- $\xi_i=0$ outside margin, $0<\xi_i\le1$ inside but correct, $\xi_i>1$ misclassified.
- Large $C$ ≈ hard margin; small $C$ = wider, more tolerant margin.
- SGD step: margin error → $\theta\leftarrow\theta-\eta_t(\theta-Cy_ix_i)$; else $\theta\leftarrow(1-\eta_t)\theta$; $\eta_t=\frac1{Ct}$.
- = Ridge regulariser + hinge loss. Very similar to the Perceptron.

## Links

- **Related concepts**: [[Hinge Loss]] · [[Hard-Margin SVM]] · [[Kernel Trick]] · [[Ridge Regression]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[05 - ML - Perceptron, SVM and Kernels#Soft-margin SVM|Lecture 5 — Soft-margin SVM]]
