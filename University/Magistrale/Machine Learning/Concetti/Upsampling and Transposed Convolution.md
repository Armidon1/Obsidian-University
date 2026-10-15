---
title: Upsampling and Transposed Convolution
tags:
  - machine-learning
  - concetto
  - cnn
---

# Upsampling and Transposed Convolution

> [!summary] In short
> Increase spatial size: duplicate values, max-unpool to the remembered max positions, interpolate bilinearly, or use a learnt transposed convolution (each input spreads to several outputs). 1×1 convolutions change the number of channels.

- Used by encoder–decoder networks for **semantic segmentation** (per-pixel classes).
- Transposed convolution's weight matrix = transpose of the downsampling one.

## Links

- **Related concepts**: [[Pooling]] · [[Convolutional Neural Network]] · [[Autoencoder]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[11 - ML - Convolutional Neural Networks#6. Upsampling|Lecture 11 — 6. Upsampling]]
