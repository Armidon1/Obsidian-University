---
title: Margin
tags:
  - machine-learning
  - concetto
  - linear-classifiers
  - svm
---

# Margin

> [!summary] In short
> The distance of a separating hyperplane from its closest training point, $\gamma(\theta)=\min_i\frac{|x_i^T\theta|}{\lVert\theta\rVert}$; a large margin makes the problem easy (few Perceptron mistakes) and is what SVMs maximise.

- Distance point–hyperplane: $\operatorname{dist}(x,H_\theta)=\frac{\lvert x^T\theta\rvert}{\lVert\theta\rVert}$.
- **Classification error**: $y\,x^T\theta<0$; **margin error**: $y\,x^T\theta<1$ (fixes the scale of $\theta$).
- If $\min_iy_ix_i^T\theta=1$ then $\gamma(\theta)=1/\lVert\theta\rVert$: max margin ⇔ min norm.

## Links

- **Related concepts**: [[Perceptron Algorithm]] · [[Hard-Margin SVM]] · [[Soft-Margin SVM]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[05 - ML - Perceptron, SVM and Kernels#Margin and Novikoff's theorem|Lecture 5 — Margin and Novikoff's theorem]]
> - [[05 - ML - Perceptron, SVM and Kernels#2. Support Vector Machines|Lecture 5 — 2. Support Vector Machines]]
