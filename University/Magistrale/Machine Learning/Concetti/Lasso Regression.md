---
title: Lasso Regression
tags:
  - machine-learning
  - concetto
  - regularization
  - regression
---

# Lasso Regression

> [!summary] In short
> Least squares plus an L1 penalty $\lambda\lVert\theta\rVert_1$: some coefficients become exactly zero, so it performs implicit feature selection.

- Convex but not differentiable at $0$ (use sub-gradients).
- Geometric reason for sparsity: the L1 ball is a "diamond" with corners on the axes.

## Links

- **Related concepts**: [[Ridge Regression]] · [[Elastic Net]] · [[Overfitting]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[03 - ML - Overfitting, Regularization and Gradient Descent#Remedy 2 — regularization|Lecture 3 — Remedy 2 — regularization]]
