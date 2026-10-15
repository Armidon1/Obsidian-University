---
title: Generalization Bound
tags:
  - machine-learning
  - concetto
  - learning-theory
---

# Generalization Bound

> [!summary] In short
> A guarantee that, with probability at least 1−δ over the training set, $|R(h)-\hat R(h)|\le\varepsilon$ for every h in the class; the samples needed grow with log|H| (finite) or with the VC dimension (infinite).

| Class | Condition on $n$ |
|---|---|
| finite $\mathcal{H}$ | $n\ge\frac1{2\varepsilon^2}\ln\frac{2\lvert\mathcal{H}\rvert}\delta$ |
| VC dimension $d$ | $n\in\Omega\big(\frac{d\log(1/\varepsilon)+\log(1/\delta)}{\varepsilon^2}\big)$ |

Finite case proof = union bound + Hoeffding: $\mathbb{P}(\max_h\lvert R-\hat R\rvert>\varepsilon)\le2\lvert\mathcal{H}\rvert e^{-2\varepsilon^2n}$.

## Links

- **Related concepts**: [[Union Bound]] · [[Hoeffding Inequality]] · [[VC Dimension]] · [[Risk Decomposition]] · [[Expected and Empirical Risk]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[06 - ML - Generalization Bounds and Tree Predictors#1. Generalization bounds|Lecture 6 — 1. Generalization bounds]]
> - [[06 - ML - Generalization Bounds and Tree Predictors#Finite families of classifiers|Lecture 6 — Finite families of classifiers]]
