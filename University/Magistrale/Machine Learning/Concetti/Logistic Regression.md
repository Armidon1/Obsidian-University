---
title: Logistic Regression
tags:
  - machine-learning
  - concetto
  - classification
---

# Logistic Regression

> [!summary] In short
> Binary classifier $h_\theta(x)=\sigma(\phi(x)^T\theta)$ estimating $P(Y=1\mid x)$, trained by maximising the log-likelihood (minimising cross-entropy); concave objective, no closed form, solved by gradient ascent.

$$\hat\ell(\theta)=\frac1n\sum_i\big[y_i\log h_\theta(x_i)+(1-y_i)\log(1-h_\theta(x_i))\big],\qquad\nabla\hat\ell=\frac1n\sum_i(y_i-h_\theta(x_i))\phi(x_i)$$

- Decision boundary: hyperplane $\phi(x)^T\theta=0$.
- Hessian $-\frac1n\sum h(1-h)\phi\phi^T$ is NSD → concave → global optimum.
- = a neural network with no hidden layer and a sigmoid output.

## Links

- **Related concepts**: [[Sigmoid Function]] · [[Cross-Entropy Loss]] · [[Softmax Regression]] · [[Perceptron Algorithm]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[04 - ML - Logistic Regression and Softmax#1. Logistic regression|Lecture 4 — 1. Logistic regression]]
> - [[04 - ML - Logistic Regression and Softmax#Gradient (ascent)|Lecture 4 — Gradient (ascent)]]
