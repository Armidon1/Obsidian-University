---
title: Naive Bayes Classifier
tags:
  - machine-learning
  - concetto
  - classification
  - decision-theory
---

# Naive Bayes Classifier

> [!summary] In short
> A method to estimate the Bayes optimal predictor assuming that the features are independent given the class: the likelihood factorises and the number of parameters drops from exponential to linear in d.

$$\mathbb{P}(X=x\mid Y=y)=\prod_{i=1}^d\mathbb{P}(X_i=x_i\mid Y=y)$$

| | Without assumption | Naive Bayes |
|---|---|---|
| discrete, $n$ values per feature, 2 classes | $2n^d$ | $2dn$ |
| Gaussian features | $O(d^2)$ (full $\Sigma$) | $O(d)$ (diagonal) |

- Avoids the **curse of dimensionality**; poor when features are strongly correlated.
- Not one classifier but an estimation method (plug-in into the Bayes rule).

## Links

- **Related concepts**: [[Bayes Optimal Predictor]] · [[Likelihood Ratio Test]] · [[Curse of Dimensionality]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[01 - ML - Decision Theory and Naive Bayes#4. Naive Bayes classifier|Lecture 1 — 4. Naive Bayes classifier]]
