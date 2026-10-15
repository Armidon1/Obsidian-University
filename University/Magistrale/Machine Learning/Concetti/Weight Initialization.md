---
title: Weight Initialization
tags:
  - machine-learning
  - concetto
  - neural-networks
---

# Weight Initialization

> [!summary] In short
> Weights are drawn at random from N(0, σ²) with σ² tied to the layer sizes — He: 2/D_h, or 4/(D_h + D_{h+1}) — so that activations and gradients keep a stable scale across layers.

- Too small $\sigma^2$ → vanishing values/gradients; too large → exploding.
- Each weight matrix gets its own variance; libraries provide initialisers.

## Links

- **Related concepts**: [[Vanishing and Exploding Gradients]] · [[ReLU]] · [[Backpropagation]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[10 - ML - Training Neural Networks#5. Parameter initialisation|Lecture 10 — 5. Parameter initialisation]]
