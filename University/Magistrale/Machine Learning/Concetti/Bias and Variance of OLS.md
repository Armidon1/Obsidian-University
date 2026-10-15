---
title: Bias and Variance of OLS
tags:
  - machine-learning
  - concetto
  - regression
  - statistics
---

# Bias and Variance of OLS

> [!summary] In short
> Under the linear assumption OLS is unbiased, its variance is $\frac{\sigma^2}{n}\mathbb{E}[\hat\Sigma^{-1}]$, and its expected excess risk is about $\sigma^2 d/n$.

$$\mathbb{E}[\hat\theta]=\theta^\star,\qquad\mathbb{V}[\hat\theta]=\sigma^2\,\mathbb{E}\big[(\Phi^T\Phi)^{-1}\big]=\frac{\sigma^2}{n}\mathbb{E}\big[\hat\Sigma^{-1}\big]$$
$$\mathbb{E}[R(\hat\theta)]=\sigma^2+\frac{\sigma^2}{n}\mathbb{E}\big[\operatorname{Tr}(\Sigma\hat\Sigma^{-1})\big]\approx\sigma^2+\frac{\sigma^2d}{n}$$

- Key step: $\hat\theta-\theta^\star=(\Phi^T\Phi)^{-1}\Phi^T\varepsilon$, $\mathbb{E}[\varepsilon\varepsilon^T]=\sigma^2I$.
- More features $d$ → more variance; more data $n$ → less.

## Links

- **Related concepts**: [[Linear Assumption]] · [[Ordinary Least Squares]] · [[Overfitting]] · [[Risk Decomposition]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[02 - ML - Linear Regression and OLS#6. Estimating θ⋆ — bias and variance of OLS|Lecture 2 — 6. Estimating θ⋆ — bias and variance of OLS]]
> - [[02 - ML - Linear Regression and OLS#7. The risk of the OLS estimator|Lecture 2 — 7. The risk of the OLS estimator]]
