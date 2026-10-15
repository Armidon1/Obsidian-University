---
title: Gaussian Output Networks
tags:
  - machine-learning
  - concetto
  - neural-networks
  - loss
---

# Gaussian Output Networks

> [!summary] In short
> Networks seen as predictors of the parameters of a distribution: choose p(t|λ), let the network output λ, minimise the negative log-likelihood. Gaussian → squared error, Bernoulli → binary cross-entropy, Categorical → multiclass cross-entropy.

**Recipe**: 1) fix $p(t\mid\lambda)$; 2) network predicts $\lambda=h(x;\theta)$; 3) minimise $J(\theta)=-\sum\log p(t\mid x;\theta)$; 4) predict $\arg\max_tp(t\mid x;\hat\theta)$.

| Task | Distribution | Output | Loss |
|---|---|---|---|
| regression | Normal | linear | sum of squared errors |
| binary | Bernoulli | sigmoid | binary CE |
| multiclass | Categorical | softmax | multiclass CE |

- **Homoscedastic**: only $\mu$ (σ fixed). **Heteroscedastic**: also $\sigma^2(x)$, made positive by squaring.

## Links

- **Related concepts**: [[Cross-Entropy Loss]] · [[Linear Regression]] · [[Feed-Forward Neural Network]] · [[Softmax Regression]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[09 - ML - Feed-Forward Neural Networks#4. What does the network output? Distributions and loss functions|Lecture 9 — 4. What does the network output? Distributions and loss functions]]
> - [[09 - ML - Feed-Forward Neural Networks#The recipe for constructing loss functions|Lecture 9 — The recipe for constructing loss functions]]
> - [[09 - ML - Feed-Forward Neural Networks#Regression|Lecture 9 — Regression]]
