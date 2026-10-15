---
title: Feed-Forward Neural Network
tags:
  - machine-learning
  - concetto
  - neural-networks
---

# Feed-Forward Neural Network

> [!summary] In short
> Layers of neurons (linear combination + non-linear activation), each layer fully connected only to the next one; a shallow FNN with ReLU computes a piecewise linear function with one kink per hidden unit.

$$y=a\Big(\theta_0+\sum_i\theta_ix_i\Big)\qquad h_{k}=a(\Omega_{k-1}h_{k-1}+\beta_{k-1}),\quad y=o(\Omega_Kh_K+\beta_K)$$

- Also called ANN or multi-layer perceptron.
- Without non-linear activations the whole network is linear.
- $n$ ReLU units in 1-D → $n+1$ linear regions.
- Design: width, depth, activations, loss (problem-dependent).

## Links

- **Related concepts**: [[Activation Function]] · [[ReLU]] · [[Universal Approximation Theorem]] · [[Deep Neural Network]] · [[Gaussian Output Networks]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[09 - ML - Feed-Forward Neural Networks#2. The neuron and the shallow network|Lecture 9 — 2. The neuron and the shallow network]]
> - [[09 - ML - Feed-Forward Neural Networks#5. Matrix notation|Lecture 9 — 5. Matrix notation]]
