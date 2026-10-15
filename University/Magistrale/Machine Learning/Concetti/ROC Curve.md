---
title: ROC Curve
tags:
  - machine-learning
  - concetto
  - binary-classification
  - evaluation
---

# ROC Curve

> [!summary] In short
> Plot of the best achievable TPR against the FPR as the threshold of the likelihood ratio test varies; the closer to the top-left corner (and the larger the AUC), the better.

- $x$-axis FPR, $y$-axis TPR; from $(0,0)$ (never positive) to $(1,1)$ (always positive).
- Diagonal = random classifier.
- Exercise 2.8 (Gaussians $\mathcal{N}(0,1)$ vs $\mathcal{N}(s,1)$): $\text{TPR}=1-\Phi\big(\Phi^{-1}(1-\text{FPR})-s\big)$.
- Useful when the right costs are unknown: choose the operating point later.

## Links

- **Related concepts**: [[Neyman-Pearson Lemma]] · [[Likelihood Ratio Test]] · [[Classification Metrics]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[01 - ML - Decision Theory and Naive Bayes#Neyman–Pearson and the ROC curve|Lecture 1 — Neyman–Pearson and the ROC curve]]
