---
title: Hard-Margin SVM
tags:
  - machine-learning
  - concetto
  - svm
  - linear-classifiers
---

# Hard-Margin SVM

> [!summary] In short
> $\min\frac12\lVert\theta\rVert^2$ s.t. $y_i\theta^Tx_i\ge1$: among separating hyperplanes, the one with the largest margin $1/\lVert\theta\rVert$.

- Proposition: any solution has optimal margin $\gamma^\star$.
- Infeasible if the data are not separable → soft margin.
- The solution depends only on the **support vectors** (points on the margin).

## Links

- **Related concepts**: [[Soft-Margin SVM]] · [[Margin]] · [[Kernel Trick]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[05 - ML - Perceptron, SVM and Kernels#2. Support Vector Machines|Lecture 5 — 2. Support Vector Machines]]
