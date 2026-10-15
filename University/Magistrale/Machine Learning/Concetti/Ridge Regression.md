---
title: Ridge Regression
tags:
  - machine-learning
  - concetto
  - regularization
  - regression
---

# Ridge Regression

> [!summary] In short
> Least squares plus an L2 penalty $\lambda\lVert\theta\rVert_2^2$: shrinks all coefficients, keeps the problem convex and differentiable and makes the matrix always invertible.

$$\min_\theta\ \frac1{2n}\lVert\Phi\theta-y\rVert^2+\lambda\lVert\theta\rVert_2^2\qquad\Rightarrow\qquad\hat\theta=(\Phi^T\Phi+2n\lambda I)^{-1}\Phi^Ty$$

- $\lambda$ too large → underfitting (flat curve); tuned on validation data.
- Same penalty = **weight decay** in neural networks; the $\frac12\lVert\theta\rVert^2$ term of the SVM.

## Links

- **Related concepts**: [[Lasso Regression]] · [[Elastic Net]] · [[Overfitting]] · [[Soft-Margin SVM]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[03 - ML - Overfitting, Regularization and Gradient Descent#Remedy 2 — regularization|Lecture 3 — Remedy 2 — regularization]]
> - [[10 - ML - Training Neural Networks#6. Regularisation|Lecture 10 — 6. Regularisation]]
