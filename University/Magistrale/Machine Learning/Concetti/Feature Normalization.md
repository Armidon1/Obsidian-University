---
title: Feature Normalization
tags:
  - machine-learning
  - concetto
  - preprocessing
---

# Feature Normalization

> [!summary] In short
> Rescaling features so that none dominates distances or gradients just because of its unit: z-score $(x-\mu)/\sigma$ or min-max scaling to $[a,b]$. Lossless and almost always recommended.

$$z=\frac{x-\mu}{\sigma}\qquad x'=a+\frac{(x-\min)(b-a)}{\max-\min}$$

- kNN: age vs income, cm vs dm change the neighbours.
- Neural networks: a (non-trained) normalisation layer after the input; PCA needs centred data.

## Links

- **Related concepts**: [[K-Nearest Neighbors]] · [[Principal Component Analysis]] · [[Tensor]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[07 - ML - K-Nearest Neighbors#3. Feature scale and normalisation|Lecture 7 — 3. Feature scale and normalisation]]
> - [[10 - ML - Training Neural Networks#7. TensorFlow, normalisation layer and tensors|Lecture 10 — 7. TensorFlow, normalisation layer and tensors]]
