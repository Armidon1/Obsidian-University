---
title: Sigmoid Function
tags:
  - machine-learning
  - concetto
  - classification
  - activation
---

# Sigmoid Function

> [!summary] In short
> $\sigma(z)=\frac1{1+e^{-z}}$ squashes a real score into $(0,1)$, so it can be read as a probability; its derivative is $\sigma(z)(1-\sigma(z))$.

- $\sigma(0)=\frac12$, $\sigma(-z)=1-\sigma(z)$, inverse = log-odds $\log\frac{p}{1-p}$.
- Output activation for **binary classification** (Bernoulli parameter).
- A "squashing" function (universal approximation theorem); saturates for large $\lvert z\rvert$ → small gradients.

## Links

- **Related concepts**: [[Logistic Regression]] · [[Activation Function]] · [[Softmax Regression]] · [[Cross-Entropy Loss]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[04 - ML - Logistic Regression and Softmax#The sigmoid|Lecture 4 — The sigmoid]]
> - [[09 - ML - Feed-Forward Neural Networks#Binary classification|Lecture 9 — Binary classification]]
