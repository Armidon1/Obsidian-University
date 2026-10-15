---
title: Stochastic Gradient Descent
tags:
  - machine-learning
  - concetto
  - optimization
---

# Stochastic Gradient Descent

> [!summary] In short
> Gradient descent where the full gradient is replaced by the gradient of one random sample (or a mini-batch): unbiased, much cheaper per step, and its noise helps escape local minima.

$$g(\theta)=\nabla\ell_{i_t}(\theta),\quad i_t\sim\text{Unif}\{1..n\}\qquad\mathbb{E}[g]=\nabla\Big(\tfrac1n\textstyle\sum_i\ell_i\Big)$$

| | per-step cost | gradient |
|---|---|---|
| GD | $O(nd)$ | exact |
| SGD | $O(d)$ | unbiased, noisy |
| mini-batch | $O(\lvert B\rvert d)$ | variance $/\lvert B\rvert$ |

Also used for logistic regression (gradient ascent) and SVM (sub-gradient).

## Links

- **Related concepts**: [[Gradient Descent]] · [[Mini-Batch and Epoch]] · [[Momentum]] · [[Adam Optimizer]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[03 - ML - Overfitting, Regularization and Gradient Descent#5. Stochastic gradient descent|Lecture 3 — 5. Stochastic gradient descent]]
> - [[10 - ML - Training Neural Networks#2. SGD, mini-batches and epochs|Lecture 10 — 2. SGD, mini-batches and epochs]]
