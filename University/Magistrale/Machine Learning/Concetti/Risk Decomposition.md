---
title: Risk Decomposition
tags:
  - machine-learning
  - concetto
  - learning-theory
  - overfitting
---

# Risk Decomposition

> [!summary] In short
> $R(h)$ = Bayes error + bias of the class (approximation error) + estimation error; a richer class lowers the bias but raises the estimation error — the theory behind overfitting.

$$R(h)=\underbrace{R(h^\star)}_{\text{Bayes}}+\underbrace{\inf_{\mathcal{H}}R-R(h^\star)}_{\text{bias}}+\underbrace{R(h)-\inf_{\mathcal{H}}R}_{\text{estimation}}$$

- Estimation error of ERM: $O\big(\sqrt{(d\log(n/d)+\log(1/\delta))/n}\big)$.
- Large VC → overfitting; small VC → underfitting.

## Links

- **Related concepts**: [[Overfitting]] · [[VC Dimension]] · [[Bayes Optimal Predictor]] · [[Bias and Variance of OLS]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[06 - ML - Generalization Bounds and Tree Predictors#Risk decomposition|Lecture 6 — Risk decomposition]]
