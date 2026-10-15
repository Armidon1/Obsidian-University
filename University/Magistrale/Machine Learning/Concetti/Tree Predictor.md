---
title: Tree Predictor
tags:
  - machine-learning
  - concetto
  - decision-trees
  - classification
---

# Tree Predictor

> [!summary] In short
> A rooted tree whose internal nodes test one feature and whose leaves carry the majority label; it can fit any training set (infinite VC dimension), so its size is capped and it is grown greedily.

- Leaf error $=\min\{N_\ell^+,N_\ell^-\}$; $\hat R=\frac1n\sum_\ell\psi(N_\ell^+/N_\ell)N_\ell$, $\psi(z)=\min\{z,1-z\}$.
- Splitting never increases the training error (concavity of $\psi$).
- Greedy: split a leaf with misclassified points until $N$ nodes.
- $\lvert\mathcal{T}_N\rvert\le(2ed)^N$ → samples linear in $N$, logarithmic in $d$.
- Easy to interpret; axis-parallel decision boundaries.

## Links

- **Related concepts**: [[Impurity Measures]] · [[Random Forest]] · [[VC Dimension]] · [[AdaBoost]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[06 - ML - Generalization Bounds and Tree Predictors#2. Tree predictors|Lecture 6 — 2. Tree predictors]]
> - [[06 - ML - Generalization Bounds and Tree Predictors#Training a tree predictor|Lecture 6 — Training a tree predictor]]
> - [[06 - ML - Generalization Bounds and Tree Predictors#The VC dimension of tree predictors|Lecture 6 — The VC dimension of tree predictors]]
