---
title: Loss Function
tags:
  - machine-learning
  - concetto
  - decision-theory
---

# Loss Function

> [!summary] In short
> $\ell(a,b)$ is the price paid when predicting $a$ while the truth is $b$. It is a modelling choice of the designer, while the data distribution is given by the environment.

| Loss | $\ell(a,b)$ | Task |
|---|---|---|
| 0-1 | $\mathbb{1}\{a\ne b\}$ | classification |
| squared | $(a-b)^2$ | regression → best predictor = conditional **mean** |
| absolute | $\lvert a-b\rvert$ | regression → best predictor = conditional **median** |
| hinge | $(1-yz)_+$ | SVM |
| cross-entropy | $-\log p(t)$ | probabilistic classification |

- Binary classification: any loss = 4 numbers $\ell(1,1),\ell(0,0),\ell(1,0),\ell(0,1)$ (TP, TN, FP, FN).
- Asymmetric costs move the decision threshold (a missed attack ≠ a false alarm).

## Links

- **Related concepts**: [[Expected and Empirical Risk]] · [[Bayes Optimal Predictor]] · [[Cross-Entropy Loss]] · [[Hinge Loss]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[01 - ML - Decision Theory and Naive Bayes#1. The setting|Lecture 1 — 1. The setting]]
