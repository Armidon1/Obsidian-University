---
title: Expected and Empirical Risk
tags:
  - machine-learning
  - concetto
  - decision-theory
  - learning-theory
---

# Expected and Empirical Risk

> [!summary] In short
> The expected risk $R(f)=\mathbb{E}[\ell(f(X),Y)]$ is the true average loss under the unknown distribution; the empirical risk $\hat R(f)=\frac1n\sum_i\ell(f(x_i),y_i)$ is its estimate on the training set.

- $R(f)$: what we care about (performance on future data), not computable.
- $\hat R(f)$: what we can minimise (ERM). Training error.
- For a **fixed** $f$, $\hat R(f)\to R(f)$ (law of large numbers, Hoeffding). Because training **chooses** $f$ looking at the data, we need the bound **for all $f\in\mathcal{H}$ at once** → generalization bounds.
- Discrete case: $R(f)=\sum_{x,y}\ell(f(x),y)\,\mathbb{P}(X=x,Y=y)$.

> [!example] $\mathcal{X}=\{1,2,3\}$, $f(1)=f(3)=1,f(2)=0$, 0-1 loss: $R(f)=\mathbb{P}(2,1)+\mathbb{P}(3,0)=\frac1{12}+\frac1{12}=\frac16$.

## Links

- **Related concepts**: [[Loss Function]] · [[Generalization Bound]] · [[Overfitting]] · [[Bayes Optimal Predictor]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[01 - ML - Decision Theory and Naive Bayes#Expected risk|Lecture 1 — Expected risk]]
> - [[06 - ML - Generalization Bounds and Tree Predictors#1. Generalization bounds|Lecture 6 — 1. Generalization bounds]]
