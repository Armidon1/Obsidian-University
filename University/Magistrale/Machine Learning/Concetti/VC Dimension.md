---
title: VC Dimension
tags:
  - machine-learning
  - concetto
  - learning-theory
---

# VC Dimension

> [!summary] In short
> The size of the largest set of points that the hypothesis class can shatter (label in every possible way). It measures complexity, characterises learnability, and the samples needed grow linearly with it.

To show $\text{VC}=d$: exhibit $d$ shattered points **and** show no $d+1$ points can be shattered.

| Class | VC |
|---|---|
| intervals on $\mathbb{R}$ | 2 |
| half-planes in $\mathbb{R}^2$ / hyperplanes in $\mathbb{R}^d$ | 3 / $d+1$ |
| discs in $\mathbb{R}^2$ | 3 |
| axis-aligned rectangles | 4 |
| triangles in $\mathbb{R}^2$ | 7 |
| finite $\mathcal{H}$ | $\le\log_2\lvert\mathcal{H}\rvert$ |
| all trees | $\infty$ |

## Links

- **Related concepts**: [[Generalization Bound]] · [[Risk Decomposition]] · [[Tree Predictor]] · [[Overfitting]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[06 - ML - Generalization Bounds and Tree Predictors#Infinite families — the VC dimension|Lecture 6 — Infinite families — the VC dimension]]
> - [[06 - ML - Generalization Bounds and Tree Predictors#The VC dimension of tree predictors|Lecture 6 — The VC dimension of tree predictors]]
