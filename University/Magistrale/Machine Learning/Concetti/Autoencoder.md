---
title: Autoencoder
tags:
  - machine-learning
  - concetto
  - dimensionality-reduction
  - neural-networks
---

# Autoencoder

> [!summary] In short
> A network trained to reproduce its input, $\min\sum\lVert x-g(f(x))\rVert^2$, through a bottleneck: the encoder f gives a non-linear compressed code, the decoder g can generate data from codes.

- Unsupervised (target = input).
- Keep the encoder for dimensionality reduction; the decoder fed with arbitrary codes → generative AI.
- Linear $f,g$ + squared loss = same subspace as PCA.
- Bottleneck = forces a compressed representation (Second Session Q8).

## Links

- **Related concepts**: [[Principal Component Analysis]] · [[Feed-Forward Neural Network]] · [[Upsampling and Transposed Convolution]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[12 - ML - Dimensionality Reduction#3. Autoencoders|Lecture 12 — 3. Autoencoders]]
