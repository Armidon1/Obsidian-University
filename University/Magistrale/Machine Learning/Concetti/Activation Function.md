---
title: Activation Function
tags:
  - machine-learning
  - concetto
  - neural-networks
---

# Activation Function

> [!summary] In short
> The non-linear function applied after each neuron's linear combination; hidden layers usually use ReLU, while the output activation depends on the task (linear, sigmoid, softmax).

| Layer / task | Activation |
|---|---|
| hidden | ReLU (also sigmoid, tanh) |
| output, regression | linear (identity) |
| output, binary | sigmoid |
| output, multiclass | softmax |

Must be (almost everywhere) differentiable for gradient-based training.

## Links

- **Related concepts**: [[ReLU]] · [[Sigmoid Function]] · [[Softmax Regression]] · [[Feed-Forward Neural Network]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[09 - ML - Feed-Forward Neural Networks#Activation functions for hidden units|Lecture 9 — Activation functions for hidden units]]
> - [[09 - ML - Feed-Forward Neural Networks#4. What does the network output? Distributions and loss functions|Lecture 9 — 4. What does the network output? Distributions and loss functions]]
