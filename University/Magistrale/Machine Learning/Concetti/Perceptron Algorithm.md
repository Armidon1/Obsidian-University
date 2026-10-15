---
title: Perceptron Algorithm
tags:
  - machine-learning
  - concetto
  - classification
  - linear-classifiers
---

# Perceptron Algorithm

> [!summary] In short
> For linearly separable data with labels ±1: whenever $y\,x^T\theta<1$ (margin error) update $\theta\leftarrow\theta+yx$. It makes at most $(2+D^2)/\gamma^{\star2}$ mistakes (Novikoff).

```
θ ← 0
repeat: pick (x, y); if y·xᵀθ < 1: θ ← θ + y·x
```
- Mistake bound: $\lVert\theta\rVert$ grows $\ge m\gamma^\star$ (linearly) but $\le\sqrt{m(2+D^2)}$ → $m\le(2+D^2)/\gamma^{\star2}$. Independent of $n$ and $d$.
- Running time $O(nM)$ visits ($M$ mistakes).
- Stacked in layers → multi-layer perceptron (FNN).

## Links

- **Related concepts**: [[Margin]] · [[Hard-Margin SVM]] · [[Logistic Regression]] · [[Feed-Forward Neural Network]] · [[Perceptron]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[05 - ML - Perceptron, SVM and Kernels#1. The Perceptron|Lecture 5 — 1. The Perceptron]]
> - [[05 - ML - Perceptron, SVM and Kernels#Margin and Novikoff's theorem|Lecture 5 — Margin and Novikoff's theorem]]
