---
title: K-Nearest Neighbors
tags:
  - machine-learning
  - concetto
  - knn
  - non-parametric
  - classification
  - regression
---

# K-Nearest Neighbors

> [!summary] In short
> Predict the majority label (classification) or the average target (regression) of the k training points closest to the query. No training; cost O(dm) per query; needs normalised features and suffers the curse of dimensionality.

- 1-NN = Voronoi tessellation.
- Bound (1-NN, $\eta$ $c$-Lipschitz on $[0,1]^d$): $\mathbb{E}[L_D(h_S)]\le2L_D(h^\star)+4c\sqrt d\,m^{-1/(d+1)}$.
- Distances: Euclidean, Manhattan, Hamming.
- $k$ chosen by cross-validation (small $k$ → overfitting, $k=m$ → global majority).
- k-d trees: $O(d\log m)$ queries but size exponential in $d$.

> [!example] Patrizi exercise: $x=(4,5)$, $K=3$ → class 0; $K=5$ → class 1; $K=1$ tie between $(5,5)$ and $(4,4)$.

## Links

- **Related concepts**: [[Parametric vs Non-Parametric Models]] · [[Curse of Dimensionality]] · [[Feature Normalization]] · [[Bayes Optimal Predictor]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[07 - ML - K-Nearest Neighbors#2. The k-NN rule|Lecture 7 — 2. The k-NN rule]]
> - [[07 - ML - K-Nearest Neighbors#4. Generalization bound for 1-NN|Lecture 7 — 4. Generalization bound for 1-NN]]
> - [[07 - ML - K-Nearest Neighbors#6. Complexity|Lecture 7 — 6. Complexity]]
> - [[07 - ML - K-Nearest Neighbors#7. kNN regression|Lecture 7 — 7. kNN regression]]
