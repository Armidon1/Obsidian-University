---
title: Hinge Loss
tags:
  - machine-learning
  - concetto
  - svm
  - loss
---

# Hinge Loss

> [!summary] In short
> $h(z)=(1-z)_+=\max\{0,1-z\}$ with $z=y\theta^Tx$: zero beyond the margin, linear otherwise. Convex but not differentiable at $z=1$, so sub-gradients are used.

- **Sub-gradient** $g$ at $x$: $F(y)\ge F(x)+g^T(y-x)\ \forall y$.
- Sub-gradient of the SVM objective: $\theta-\frac Cn\sum_iy_ix_i\,\mathbb{1}\{y_i\theta^Tx_i<1\}$.

## Links

- **Related concepts**: [[Soft-Margin SVM]] · [[Loss Function]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[05 - ML - Perceptron, SVM and Kernels#Soft-margin SVM|Lecture 5 — Soft-margin SVM]]
