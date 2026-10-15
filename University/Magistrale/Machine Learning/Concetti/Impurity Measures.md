---
title: Impurity Measures
tags:
  - machine-learning
  - concetto
  - decision-trees
---

# Impurity Measures

> [!summary] In short
> Strictly concave surrogates of the leaf error $\min\{z,1-z\}$ used to choose splits: Gini index $2z(1-z)$ and scaled entropy; they reward splits that purify the leaves even when the error does not change.

| Impurity | $\psi(z)$ |
|---|---|
| misclassification | $\min\{z,1-z\}$ |
| Gini | $2z(1-z)$ |
| entropy (scaled) | $-\frac z2\log_2z-\frac{1-z}2\log_2(1-z)$ |

All $=0$ on pure leaves, max $\frac12$ at $z=\frac12$.

## Links

- **Related concepts**: [[Tree Predictor]] · [[Random Forest]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[06 - ML - Generalization Bounds and Tree Predictors#Impurity measures|Lecture 6 — Impurity measures]]
