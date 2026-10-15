---
title: Hoeffding Inequality
tags:
  - machine-learning
  - concetto
  - probability
  - learning-theory
---

# Hoeffding Inequality

> [!summary] In short
> For n i.i.d. Bernoulli(μ) variables with mean $\hat Z$: $P(|\hat Z-\mu|>\varepsilon)\le2e^{-2\varepsilon^2n}$ — the empirical mean concentrates exponentially fast (called Chernoff bound in the handout).

- Applied to $Z_i=\ell(h(x_i),y_i)$: $\hat Z=\hat R(h)$, $\mu=R(h)$.
- Much stronger than Chebyshev ($\propto\frac1{n\varepsilon^2}$).

## Links

- **Related concepts**: [[Union Bound]] · [[Generalization Bound]] · [[Disuguaglianza di Chebyshev]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[06 - ML - Generalization Bounds and Tree Predictors#Mathematical preliminaries|Lecture 6 — Mathematical preliminaries]]
