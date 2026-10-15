---
title: Gradient Descent
tags:
  - machine-learning
  - concetto
  - optimization
---

# Gradient Descent

> [!summary] In short
> Iterative minimisation $\theta_t=\theta_{t-1}-\gamma_t\nabla F(\theta_{t-1})$; on convex functions it reaches the global minimum, for least squares with $\gamma=1/L$ the error shrinks by $(1-1/\kappa)^2$ per step.

- $\gamma$ = learning rate (step size): too small → slow, too large → oscillations/divergence.
- **Convex** $F$: every local minimum is global (Hessian PSD).
- Least squares: $\lVert\theta_t-\hat\theta\rVert^2\le(1-\frac1\kappa)^{2t}\lVert\theta_0-\hat\theta\rVert^2$, $\kappa=L/\mu$ condition number; $N=\frac\kappa2\log\frac1\varepsilon$ iterations.
- Cost per step $O(nd)$ → see SGD.
- Neural networks: non-convex loss, local minima → SGD, momentum, Adam.

## Links

- **Related concepts**: [[Stochastic Gradient Descent]] · [[Momentum]] · [[Adam Optimizer]] · [[Convex Function]] · [[Backpropagation]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[03 - ML - Overfitting, Regularization and Gradient Descent#4. Gradient descent|Lecture 3 — 4. Gradient descent]]
> - [[03 - ML - Overfitting, Regularization and Gradient Descent#Gradient descent for linear regression|Lecture 3 — Gradient descent for linear regression]]
> - [[10 - ML - Training Neural Networks#1. Fitting a model with gradient descent|Lecture 10 — 1. Fitting a model with gradient descent]]
