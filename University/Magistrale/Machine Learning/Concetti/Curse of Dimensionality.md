---
title: Curse of Dimensionality
tags:
  - machine-learning
  - concetto
  - knn
  - learning-theory
---

# Curse of Dimensionality

> [!summary] In short
> In high dimension the space is mostly empty: to keep data dense (and nearest neighbours close) the number of samples must grow exponentially with d.

- From the 1-NN bound: $m\ge\big(\frac{4c\sqrt d}{\varepsilon}\big)^{d+1}$.
- Covering $[0,1]^d$ with cubes of side 0.1 needs $10^d$ cubes.
- Remedies: assumptions (Naive Bayes), dimensionality reduction (PCA, autoencoders), models with strong inductive bias.

## Links

- **Related concepts**: [[K-Nearest Neighbors]] · [[Naive Bayes Classifier]] · [[Principal Component Analysis]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[07 - ML - K-Nearest Neighbors#5. The curse of dimensionality|Lecture 7 — 5. The curse of dimensionality]]
