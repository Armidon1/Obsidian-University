---
title: AdaBoost
tags:
  - machine-learning
  - concetto
  - ensemble
  - boosting
---

# AdaBoost

> [!summary] In short
> Train weak learners in sequence on a re-weighted training set, up-weighting the examples misclassified so far; combine them by $\operatorname{sign}(\sum_tw_th_t)$ with $w_t=\frac12\log(\frac1{\varepsilon_t}-1)$. Training error ≤ $e^{-2\gamma^2T}$.

$$D^{(t+1)}_i\propto D^{(t)}_i\,e^{-w_ty_ih_t(x_i)}$$

> [!example] 4 samples, $h_1$ wrong only on sample 4: $\varepsilon_1=\frac14$, $w_1=\frac12\log3$, $D^{(2)}=\langle\frac16,\frac16,\frac16,\frac12\rangle$.

- Cost $O(T\,m)$ with an efficient weak learner.
- Regression: $h_s=\sum_tw_th_t$.

## Links

- **Related concepts**: [[Weak Learnability]] · [[Bagging]] · [[Random Forest]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[13 - ML - Ensemble Methods#2. AdaBoost (Adaptive Boosting)|Lecture 13 — 2. AdaBoost (Adaptive Boosting)]]
