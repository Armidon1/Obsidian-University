---
title: Bayes Optimal Predictor
tags:
  - machine-learning
  - concetto
  - decision-theory
---

# Bayes Optimal Predictor

> [!summary] In short
> The predictor that minimises the expected risk: for each $x$ it picks the label minimising the conditional expected loss. It needs full knowledge of the distribution and still has an irreducible (Bayes) error.

$$f^*(x)\in\arg\min_{z\in\mathcal{Y}}\ \mathbb{E}\big[\ell(z,Y)\mid X=x\big]$$

| Loss | $f^*(x)$ |
|---|---|
| 0-1 | most probable class $\arg\max_y\mathbb{P}(Y=y\mid x)$ |
| squared | $\mathbb{E}[Y\mid X=x]$ |
| absolute | median of $Y\mid X=x$ |

- Proof idea: $R(f)=\mathbb{E}_X\big[\mathbb{E}[\ell(f(X),Y)\mid X]\big]$, minimise pointwise.
- $R(f^*)$ = **Bayes error**: the first term of the risk decomposition, nothing can beat it.
- kNN: 1-NN error $\to\le2\times$ Bayes error.

## Links

- **Related concepts**: [[Expected and Empirical Risk]] · [[Likelihood Ratio Test]] · [[Risk Decomposition]] · [[Naive Bayes Classifier]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[01 - ML - Decision Theory and Naive Bayes#2. The Bayes optimal predictor|Lecture 1 — 2. The Bayes optimal predictor]]
> - [[07 - ML - K-Nearest Neighbors#4. Generalization bound for 1-NN|Lecture 7 — 4. Generalization bound for 1-NN]]
