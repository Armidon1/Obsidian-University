---
title: Bagging
tags:
  - machine-learning
  - concetto
  - ensemble
---

# Bagging

> [!summary] In short
> Bootstrap aggregating: train M models on bootstrap samples (drawn with replacement) and average (regression) or majority-vote (classification) their predictions; reduces variance and mitigates overfitting.

| | Bagging | Boosting |
|---|---|---|
| training | parallel, independent | sequential |
| data | bootstrap samples | re-weighted set |
| reduces | variance | bias |

Random forests = bagging of trees.

## Links

- **Related concepts**: [[Random Forest]] · [[AdaBoost]] · [[Overfitting]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[13 - ML - Ensemble Methods#3. Bagging|Lecture 13 — 3. Bagging]]
> - [[06 - ML - Generalization Bounds and Tree Predictors#Random forests|Lecture 6 — Random forests]]
