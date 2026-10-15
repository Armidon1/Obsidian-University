---
title: Linear Assumption
tags:
  - machine-learning
  - concetto
  - regression
  - statistics
---

# Linear Assumption

> [!summary] In short
> The data are generated as $Y=\phi(X)^T\theta^\star+\varepsilon$ with noise independent of $X$, zero mean and variance $\sigma^2$; then the optimal predictor under squared loss is $\phi(x)^T\theta^\star$.

- No requirement on $X$.
- $f^*(x)=\mathbb{E}[Y\mid X=x]=\phi(x)^T\theta^\star$: knowing $\theta^\star$ is enough.
- $R(\theta)=(\theta^\star-\theta)^T\Sigma(\theta^\star-\theta)+\sigma^2$, $\Sigma=\mathbb{E}[\phi\phi^T]$: Bayes risk $\sigma^2$ + excess risk.

## Links

- **Related concepts**: [[Bias and Variance of OLS]] · [[Bayes Optimal Predictor]] · [[Risk Decomposition]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[02 - ML - Linear Regression and OLS#5. The linear assumption|Lecture 2 — 5. The linear assumption]]
> - [[02 - ML - Linear Regression and OLS#7. The risk of the OLS estimator|Lecture 2 — 7. The risk of the OLS estimator]]
