---
title: Mini-Batch and Epoch
tags:
  - machine-learning
  - concetto
  - neural-networks
  - optimization
---

# Mini-Batch and Epoch

> [!summary] In short
> A mini-batch is the random subset of training samples used for one SGD step; an epoch is one full pass over the training set (all mini-batches used once).

- Mini-batches are drawn without reusing samples until the epoch ends.
- Training typically runs many epochs.
- Larger batches: less noisy gradient, more cost per step; GPUs parallelise them.

## Links

- **Related concepts**: [[Stochastic Gradient Descent]] · [[Adam Optimizer]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[10 - ML - Training Neural Networks#2. SGD, mini-batches and epochs|Lecture 10 — 2. SGD, mini-batches and epochs]]
