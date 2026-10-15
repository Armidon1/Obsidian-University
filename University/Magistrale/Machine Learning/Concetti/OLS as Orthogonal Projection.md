---
title: OLS as Orthogonal Projection
tags:
  - machine-learning
  - concetto
  - regression
  - linear-algebra
---

# OLS as Orthogonal Projection

> [!summary] In short
> $P=\Phi(\Phi^T\Phi)^{-1}\Phi^T$ projects the target vector $y$ orthogonally onto the column space of $\Phi$; $\hat\theta$ are the coordinates of that projection.

- $v\in\operatorname{im}\Phi\Rightarrow Pv=v$; $v\perp\operatorname{im}\Phi\Rightarrow Pv=0$.
- Fitted values $\Phi\hat\theta=Py$ = closest achievable prediction vector to $y$.
- Residual $y-\Phi\hat\theta\perp$ every column of $\Phi$ ⇔ normal equations.
- Same idea in PCA: $UU^T$ projects onto the principal subspace.

## Links

- **Related concepts**: [[Ordinary Least Squares]] · [[Principal Component Analysis]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[02 - ML - Linear Regression and OLS#4. A geometric interpretation|Lecture 2 — 4. A geometric interpretation]]
