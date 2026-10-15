---
title: Linear Regression
tags:
  - machine-learning
  - concetto
  - regression
---

# Linear Regression

> [!summary] In short
> Fit a function linear in the parameters by minimising the mean squared error; in 1-D the best line passes through the mean point with slope cov(x,y)/var(x).

1-D OLS:
$$\hat m=\frac{\sum_i(x_i-\bar x)(y_i-\bar y)}{\sum_i(x_i-\bar x)^2},\qquad\hat q=\bar y-\hat m\bar x$$

> [!example] $(1,1),(1,3),(2,3),(3,5),(3,3)$: $\bar x=2,\bar y=3$, $\hat m=4/4=1$, $\hat q=1$ → $y=x+1$.

- General form: $f_\theta(x)=\phi(x)^T\theta$, closed form $\hat\theta=(\Phi^T\Phi)^{-1}\Phi^Ty$.
- MSE loss = maximum likelihood under Gaussian noise (the regression output layer of an FNN).

## Links

- **Related concepts**: [[Ordinary Least Squares]] · [[Linear-in-Parameters Model]] · [[Gradient Descent]] · [[Gaussian Output Networks]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[02 - ML - Linear Regression and OLS#1. Warm-up — linear regression in 1-D|Lecture 2 — 1. Warm-up — linear regression in 1-D]]
> - [[13 - ML - Ensemble Methods#Appendix — exercise session on linear regression|Lecture 13 — Appendix — exercise session on linear regression]]
