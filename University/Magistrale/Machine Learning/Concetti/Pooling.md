---
title: Pooling
tags:
  - machine-learning
  - concetto
  - cnn
---

# Pooling

> [!summary] In short
> Downsampling that summarises each region with one value: max pooling keeps the maximum, mean pooling the average. No parameters; reduces size and adds robustness to small shifts.

> [!example] $\begin{smallmatrix}1&3&5&3\\6&2&0&8\\4&6&1&4\\2&8&0&3\end{smallmatrix}$ with $2\times2$ blocks → max $\begin{smallmatrix}6&8\\8&4\end{smallmatrix}$, mean $\begin{smallmatrix}3&4\\5&2\end{smallmatrix}$, sub-sampling $\begin{smallmatrix}1&5\\4&1\end{smallmatrix}$.

Other downsampling: stride $>1$.

## Links

- **Related concepts**: [[Convolutional Neural Network]] · [[Upsampling and Transposed Convolution]] · [[Receptive Field]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[11 - ML - Convolutional Neural Networks#5. Downsampling|Lecture 11 — 5. Downsampling]]
