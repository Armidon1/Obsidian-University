---
title: Principal Component Analysis
tags:
  - machine-learning
  - concetto
  - dimensionality-reduction
  - unsupervised-learning
---

# Principal Component Analysis

> [!summary] In short
> Linear compression $y=U^Tx$ and recovery $\tilde x=Uy$ minimising the reconstruction error; U holds the top eigenvectors of the (centred) covariance matrix, i.e. the directions of maximal variance.

$$\min_{U^TU=I}\sum_i\lVert x_i-UU^Tx_i\rVert^2\iff\max_{U^TU=I}\operatorname{tr}(U^TSU),\qquad S=\tfrac1mX^TX$$

- Lemma: the optimal $W=U^T$ with orthonormal columns.
- $Su=\lambda u$, variance along $u$ = $\lambda$.
- Centre the data first. Yale faces: $\mathbb{R}^{2500}\to\mathbb{R}^{10}$ still recognisable.

## Links

- **Related concepts**: [[Autoencoder]] · [[OLS as Orthogonal Projection]] · [[Curse of Dimensionality]] · [[Feature Normalization]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[12 - ML - Dimensionality Reduction#2. PCA|Lecture 12 — 2. PCA]]
> - [[12 - ML - Dimensionality Reduction#Variance maximisation|Lecture 12 — Variance maximisation]]
