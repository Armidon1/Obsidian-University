---
title: Kernel Trick
tags:
  - machine-learning
  - concetto
  - svm
  - kernels
---

# Kernel Trick

> [!summary] In short
> Algorithms that only use scalar products can work in a huge or infinite feature space $\psi(x)$: keep $\theta=\sum_i\alpha_i\psi(x_i)$ and the kernel matrix $K_{ij}=\langle\psi(x_i),\psi(x_j)\rangle$, with cost depending on n, not on the feature dimension.

$$\langle\psi(x),\theta\rangle=\sum_j\alpha_j\,K(x,x_j)$$

| Kernel | $K(x,z)$ | Feature space |
|---|---|---|
| polynomial | $\sum_{i\le D}x^iz^i$, $(1+x^Tz)^D$ | finite |
| Gaussian / RBF | $e^{-\lVert x-z\rVert^2/2}$ | **infinite** |

Exam: the kernel trick maps data to a high-dimensional space without computing the coordinates explicitly.

## Links

- **Related concepts**: [[Soft-Margin SVM]] · [[Linear-in-Parameters Model]] · [[K-Nearest Neighbors]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[05 - ML - Perceptron, SVM and Kernels#3. The kernel trick|Lecture 5 — 3. The kernel trick]]
