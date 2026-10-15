---
title: Convolutional Neural Network
tags:
  - machine-learning
  - concetto
  - neural-networks
  - cnn
---

# Convolutional Neural Network

> [!summary] In short
> Networks whose layers apply small kernels sliding over the input with shared weights (local connectivity + weight sharing): far fewer parameters, translation equivariance, better generalisation on images and signals.

- Hyperparameters: **kernel size, stride, dilation, padding**, number of **channels**.
- Output size: $\lfloor\frac{n+2p-k}{s}\rfloor+1$.
- Parameters depend only on the filter size, not on the input size.
- MNIST-1D: CNN 2,050 params beats FC 59,065 params on test error.
- Architectures: AlexNet (~60M), VGG (~138–144M). Tasks: classification, detection, segmentation.

## Links

- **Related concepts**: [[Receptive Field]] · [[Pooling]] · [[Upsampling and Transposed Convolution]] · [[Tensor]] · [[Deep Neural Network]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[11 - ML - Convolutional Neural Networks#1. Why convolutions|Lecture 11 — 1. Why convolutions]]
> - [[11 - ML - Convolutional Neural Networks#2. 1-D convolution|Lecture 11 — 2. 1-D convolution]]
> - [[11 - ML - Convolutional Neural Networks#Feature maps and hyperparameters|Lecture 11 — Feature maps and hyperparameters]]
> - [[11 - ML - Convolutional Neural Networks#7. Applications|Lecture 11 — 7. Applications]]
