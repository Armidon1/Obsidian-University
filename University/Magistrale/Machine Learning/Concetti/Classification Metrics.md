---
title: Classification Metrics
tags:
  - machine-learning
  - concetto
  - binary-classification
  - evaluation
---

# Classification Metrics

> [!summary] In short
> The confusion matrix (TP, FP, TN, FN) normalised per true class gives TPR (recall), FPR, TNR (specificity), FNR; precision and F1 look at the predicted positives.

| Metric | Formula | Also called |
|---|---|---|
| TPR | $P(f=1\mid Y=1)$ | recall, sensitivity, power |
| FNR | $1-$TPR | type II error, missed detection |
| FPR | $P(f=1\mid Y=0)$ | type I error, size, false alarm |
| TNR | $1-$FPR | specificity |
| Precision | $P(Y=1\mid f=1)$ | $1-$ false discovery rate |
| F1 | $\frac{2\,\text{Prec}\cdot\text{Rec}}{\text{Prec}+\text{Rec}}$ | harmonic mean |

With unbalanced classes accuracy is misleading: always use per-class rates.

## Links

- **Related concepts**: [[ROC Curve]] · [[Likelihood Ratio Test]] · [[Loss Function]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[01 - ML - Decision Theory and Naive Bayes#Confusion matrix and rates|Lecture 1 — Confusion matrix and rates]]
