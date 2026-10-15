---
title: Softmax Regression
tags:
  - machine-learning
  - concetto
  - classification
  - multiclass
---

# Softmax Regression

> [!summary] In short
> Multiclass extension of logistic regression: one linear score per class, normalised by $\operatorname{softmax}_k(s)=e^{s_k}/\sum_\ell e^{s_\ell}$; trained by maximising a concave log-likelihood.

- Gradient: $\nabla_{\theta^{(k)}}\hat\ell=\frac1n\sum_i(y_i^{(k)}-\hat p_k(x_i))\phi(x_i)$.
- Concavity: $-\log\sum e^{z_k}$ is concave (Hessian $\pi\pi^T-\operatorname{diag}\pi$, $v^THv=-\operatorname{Var}\le0$).
- $K=2$ → sigmoid of the score difference.
- Softmax = output layer of multiclass neural networks; the exponentials amplify differences; outputs depend on each other.

## Links

- **Related concepts**: [[Logistic Regression]] · [[Cross-Entropy Loss]] · [[Sigmoid Function]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[04 - ML - Logistic Regression and Softmax#2. Multiclass classification — softmax regression|Lecture 4 — 2. Multiclass classification — softmax regression]]
> - [[09 - ML - Feed-Forward Neural Networks#Multi-class classification|Lecture 9 — Multi-class classification]]
