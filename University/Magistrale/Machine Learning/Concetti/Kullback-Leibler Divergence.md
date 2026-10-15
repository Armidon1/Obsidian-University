---
title: Kullback-Leibler Divergence
tags:
  - machine-learning
  - concetto
  - information-theory
---

# Kullback-Leibler Divergence

> [!summary] In short
> $D_{KL}(p\|q)=\sum_ip_i\log\frac{p_i}{q_i}$ measures how different $q$ is from $p$; it is non-negative, zero iff $p=q$, but not symmetric (not a metric).

- Minimising $D_{KL}(\text{data}\,\|\,\text{model})$ = minimising **cross-entropy** (the entropy of the data does not depend on the model).
- Exam (First Session Q4): the always-true property is $D_{KL}\ge0$ with equality iff $P=Q$.

## Links

- **Related concepts**: [[Cross-Entropy Loss]] · [[Logistic Regression]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[04 - ML - Logistic Regression and Softmax#1. Logistic regression|Lecture 4 — 1. Logistic regression]]
