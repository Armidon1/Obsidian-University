---
title: ReLU
tags:
  - machine-learning
  - concetto
  - neural-networks
  - activation
---

# ReLU

> [!summary] In short
> Rectified Linear Unit $\max\{0,z\}$: zero for negative inputs, identity for positive ones; its derivative is the step function. The default hidden activation.

- $\operatorname{ReLU}(\theta_0+\theta_1x)$: bias moves the kink, weight changes the slope.
- Not differentiable at 0 (irrelevant in practice).
- In backprop: $\partial\operatorname{ReLU}(f)/\partial f=\operatorname{step}(f)$.
- He initialisation $\sigma^2=2/D_h$ is designed for ReLU.

## Links

- **Related concepts**: [[Activation Function]] · [[Feed-Forward Neural Network]] · [[Backpropagation]] · [[Weight Initialization]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[09 - ML - Feed-Forward Neural Networks#ReLU|Lecture 9 — ReLU]]
