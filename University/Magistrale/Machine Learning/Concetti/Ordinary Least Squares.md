---
title: Ordinary Least Squares
tags:
  - machine-learning
  - concetto
  - regression
---

# Ordinary Least Squares

> [!summary] In short
> The minimiser of $\frac1n\lVert y-\Phi\theta\rVert^2$: if $\Phi^T\Phi$ is invertible, $\hat\theta=(\Phi^T\Phi)^{-1}\Phi^Ty$, the solution of the normal equations $\Phi^T\Phi\theta=\Phi^Ty$.

- Gradient $\nabla\hat R=\frac2n(\Phi^T\Phi\theta-\Phi^Ty)$, set to 0 → **normal equations**.
- $\Phi^T\Phi$ invertible ⇔ columns of $\Phi$ independent; needs $d\le n$.
- Cost $O(nd^2+d^3)$ → for large problems use gradient descent.
- Ridge: $(\Phi^T\Phi+cI)^{-1}\Phi^Ty$ is always invertible.

## Links

- **Related concepts**: [[OLS as Orthogonal Projection]] · [[Bias and Variance of OLS]] · [[Gradient Descent]] · [[Ridge Regression]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[02 - ML - Linear Regression and OLS#3. The Ordinary Least Squares estimator|Lecture 2 — 3. The Ordinary Least Squares estimator]]
> - [[03 - ML - Overfitting, Regularization and Gradient Descent#3. Computational complexity of OLS|Lecture 3 — 3. Computational complexity of OLS]]
