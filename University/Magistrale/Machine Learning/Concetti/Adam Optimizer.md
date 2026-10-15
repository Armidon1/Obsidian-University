---
title: Adam Optimizer
tags:
  - machine-learning
  - concetto
  - optimization
  - neural-networks
---

# Adam Optimizer

> [!summary] In short
> Adaptive moment estimation: momentum on the gradient and on the squared gradient, step $\alpha\,m/(\sqrt v+\epsilon)$ (normalised per parameter). The standard algorithm to train neural networks.

$$m\leftarrow\beta m+(1-\beta)g,\quad v\leftarrow\gamma v+(1-\gamma)g^2,\quad\varphi\leftarrow\varphi-\alpha\frac{m}{\sqrt v+\epsilon}$$

- Hyperparameters $\alpha,\beta,\gamma$ (typ. $10^{-3},0.9,0.999$).
- Book version adds bias correction $\tilde m=m/(1-\beta^{t+1})$, $\tilde v=v/(1-\gamma^{t+1})$.
- Normalised gradients alone keep only the sign and bounce around the minimum; Adam smooths the path.

## Links

- **Related concepts**: [[Momentum]] · [[Stochastic Gradient Descent]] · [[Backpropagation]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[10 - ML - Training Neural Networks#Normalised gradients|Lecture 10 — Normalised gradients]]
> - [[10 - ML - Training Neural Networks#Adam|Lecture 10 — Adam]]
