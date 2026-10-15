---
title: Vanishing and Exploding Gradients
tags:
  - machine-learning
  - concetto
  - neural-networks
---

# Vanishing and Exploding Gradients

> [!summary] In short
> Through many layers values and gradients get multiplied again and again: if the factors are small they vanish (slow, stalled learning), if large they explode (overflow, unstable learning, divergence).

| Problem | Cause | Effect |
|---|---|---|
| vanishing | parameters too small | approximation errors, slow convergence |
| exploding | parameters too large | representation errors, unstable learning |

Remedies: proper initialisation, ReLU, normalisation, (gradient clipping).

## Links

- **Related concepts**: [[Weight Initialization]] · [[Backpropagation]] · [[Activation Function]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[10 - ML - Training Neural Networks#5. Parameter initialisation|Lecture 10 — 5. Parameter initialisation]]
