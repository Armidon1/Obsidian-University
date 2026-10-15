---
title: Linear-in-Parameters Model
tags:
  - machine-learning
  - concetto
  - regression
  - feature-maps
---

# Linear-in-Parameters Model

> [!summary] In short
> Models $f_\theta(x)=\sum_j\phi_j(x)\theta_j=\phi(x)^T\theta$ with fixed feature maps $\phi_j$: possibly non-linear in $x$ but linear in $\theta$, so all the linear-regression algebra applies.

| Feature maps | Model |
|---|---|
| $1,x$ | line (intercept via the constant feature) |
| $1,x,\dots,x^M$ | polynomial of degree $M$ |
| $1,\sin\frac{2\pi x}{T}i,\cos\frac{2\pi x}{T}i$ | Fourier series |

- **Design matrix** $\Phi\in\mathbb{R}^{n\times d}$, $\Phi_{ij}=\phi_j(x_i)$ (one row per sample).
- The kernel trick lets $\phi$ be infinite-dimensional; neural networks **learn** $\phi$.

## Links

- **Related concepts**: [[Linear Regression]] · [[Polynomial Regression]] · [[Kernel Trick]] · [[Feed-Forward Neural Network]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[02 - ML - Linear Regression and OLS#2. The linear regression framework|Lecture 2 — 2. The linear regression framework]]
