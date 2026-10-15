---
title: Backpropagation
tags:
  - machine-learning
  - concetto
  - neural-networks
  - optimization
---

# Backpropagation

> [!summary] In short
> Computes all partial derivatives of the loss w.r.t. the weights by the chain rule, going backwards from the output and reusing the intermediate products; cost comparable to a forward pass.

1. **Forward pass**: store pre-activations $f$ and activations $h$.
2. **Backward pass**: start from $\partial L/\partial f^{\text{out}}$ and multiply local derivatives.

$$\frac{\partial L}{\partial\Omega^1_{11}}=(f^2-y)\cdot\Omega^2_{11}\cdot\operatorname{step}(f^1_1)\cdot h^1_1,\qquad\frac{\partial L}{\partial\Omega^1_{12}}=\underbrace{(f^2-y)\,\Omega^2_{11}\,\operatorname{step}(f^1_1)}_{\text{reused}}\cdot h^1_2$$

It computes gradients; the update is done by SGD/Adam.

## Links

- **Related concepts**: [[Gradient Descent]] · [[Adam Optimizer]] · [[ReLU]] · [[Vanishing and Exploding Gradients]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[10 - ML - Training Neural Networks#4. Backpropagation|Lecture 10 — 4. Backpropagation]]
