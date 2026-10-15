---
title: Cross-Entropy Loss
tags:
  - machine-learning
  - concetto
  - classification
  - loss
---

# Cross-Entropy Loss

> [!summary] In short
> The negative log-likelihood of a Bernoulli (binary) or Categorical (multiclass) model: $-\sum\log p(t\mid x)$. It heavily punishes confident mistakes.

| | Formula |
|---|---|
| binary | $-\sum[t\log\sigma(h)+(1-t)\log(1-\sigma(h))]$ |
| multiclass | $-\sum\big[h_t-\log\sum_je^{h_j}\big]$ |

- Derived from KL divergence (Week 4) and from maximum likelihood (FNN recipe).
- In practice compute it from **logits** (`from_logits=True`) for numerical stability.

## Links

- **Related concepts**: [[Kullback-Leibler Divergence]] · [[Logistic Regression]] · [[Softmax Regression]] · [[Gaussian Output Networks]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[04 - ML - Logistic Regression and Softmax#Cross-entropy and log-likelihood|Lecture 4 — Cross-entropy and log-likelihood]]
> - [[09 - ML - Feed-Forward Neural Networks#Multi-class classification|Lecture 9 — Multi-class classification]]
