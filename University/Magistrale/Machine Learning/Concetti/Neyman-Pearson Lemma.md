---
title: Neyman-Pearson Lemma
tags:
  - machine-learning
  - concetto
  - binary-classification
  - decision-theory
---

# Neyman-Pearson Lemma

> [!summary] In short
> If the conditional densities are continuous, the predictor maximising TPR subject to FPR ≤ α is a likelihood ratio test.

$$\max\ \text{TPR}\quad\text{s.t.}\quad\text{FPR}\le\alpha\quad\Longrightarrow\quad f(x)=\mathbb{1}\{L(x)\ge\eta_\alpha\}$$

- Not proved in class (proof in Hardt & Recht, Ch. 2).
- Consequence: the ROC curve = all LRTs as the threshold goes from $-\infty$ to $+\infty$.

## Links

- **Related concepts**: [[Likelihood Ratio Test]] · [[ROC Curve]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[01 - ML - Decision Theory and Naive Bayes#Neyman–Pearson and the ROC curve|Lecture 1 — Neyman–Pearson and the ROC curve]]
