---
title: Polynomial Regression
tags:
  - machine-learning
  - concetto
  - regression
  - overfitting
---

# Polynomial Regression

> [!summary] In short
> Linear regression with feature maps $1,x,\dots,x^M$; the degree $M$ measures model complexity, and with $M=n-1$ the curve interpolates all points (zero training error, wild oscillations).

| $M$ | Behaviour (n = 10, sine + noise) |
|---|---|
| 0, 1 | underfitting |
| 3 | good fit |
| 9 | passes through every point, overfitting |

Remedies: more data ($n=100$ makes $M=9$ fine) or regularisation (Ridge).

## Links

- **Related concepts**: [[Overfitting]] · [[Ridge Regression]] · [[Linear-in-Parameters Model]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[03 - ML - Overfitting, Regularization and Gradient Descent#2. Polynomial regression and overfitting|Lecture 3 — 2. Polynomial regression and overfitting]]
