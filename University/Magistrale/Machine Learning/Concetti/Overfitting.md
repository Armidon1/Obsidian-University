---
title: Overfitting
tags:
  - machine-learning
  - concetto
  - learning-theory
  - overfitting
---

# Overfitting

> [!summary] In short
> When the model is too complex for the data, the training error keeps decreasing but the test error grows: the model learns the noise and loses generalization.

- Signature: gap between training and test error (U-shaped test curve vs complexity).
- Theory: risk decomposition — complexity ↑ ⇒ bias ↓ but estimation error ↑ (VC dimension).
- Remedies:

| Remedy | Where |
|---|---|
| more data | Week 3 |
| L1 / L2 regularisation | Ridge, Lasso, weight decay |
| limit complexity | max nodes of a tree, choice of $k$ in kNN |
| early stopping, dropout | neural networks |
| ensembles (bagging, random forests) | variance reduction |

## Links

- **Related concepts**: [[Risk Decomposition]] · [[VC Dimension]] · [[Ridge Regression]] · [[Early Stopping]] · [[Dropout]] · [[Bagging]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[03 - ML - Overfitting, Regularization and Gradient Descent#2. Polynomial regression and overfitting|Lecture 3 — 2. Polynomial regression and overfitting]]
> - [[06 - ML - Generalization Bounds and Tree Predictors#Risk decomposition|Lecture 6 — Risk decomposition]]
> - [[10 - ML - Training Neural Networks#6. Regularisation|Lecture 10 — 6. Regularisation]]
