---
title: Likelihood Ratio Test
tags:
  - machine-learning
  - concetto
  - decision-theory
  - binary-classification
---

# Likelihood Ratio Test

> [!summary] In short
> In binary classification the Bayes optimal predictor compares the likelihood ratio $L(x)=\frac{P(x\mid Y=1)}{P(x\mid Y=0)}$ with a threshold $\eta$ that depends only on costs and priors.

$$f^*(x)=\mathbb{1}\Big\{L(x)\ge\eta\Big\},\qquad \eta=\frac{[\ell(1,0)-\ell(0,0)]\,\mathbb{P}(Y=0)}{[\ell(0,1)-\ell(1,1)]\,\mathbb{P}(Y=1)}$$

- 0-1 loss + equal priors → $\eta=1$ (maximum likelihood).
- Any increasing $h$ (e.g. $\log$) can be applied to both sides: Gaussians become quadratic inequalities.
- Sweeping $\eta$ traces the **ROC curve**; by Neyman–Pearson the LRT is also optimal under an FPR constraint.

## Links

- **Related concepts**: [[Bayes Optimal Predictor]] · [[ROC Curve]] · [[Neyman-Pearson Lemma]] · [[Classification Metrics]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[01 - ML - Decision Theory and Naive Bayes#The optimal predictor is a threshold|Lecture 1 — The optimal predictor is a threshold]]
> - [[01 - ML - Decision Theory and Naive Bayes#Likelihood ratio|Lecture 1 — Likelihood ratio]]
