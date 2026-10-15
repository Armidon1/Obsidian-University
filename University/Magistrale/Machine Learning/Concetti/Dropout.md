---
title: Dropout
tags:
  - machine-learning
  - concetto
  - neural-networks
  - regularization
---

# Dropout

> [!summary] In short
> At each training iteration randomly remove links/units with probability p (set to 0), then restore them; it adds noise and prevents the network from relying too much on specific units.

- A **regularisation technique** (Erasmus Q8), combinable with L1/L2 and early stopping.
- At test time nothing is dropped (activations rescaled).

## Links

- **Related concepts**: [[Early Stopping]] · [[Overfitting]] · [[Stochastic Gradient Descent]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[10 - ML - Training Neural Networks#6. Regularisation|Lecture 10 — 6. Regularisation]]
