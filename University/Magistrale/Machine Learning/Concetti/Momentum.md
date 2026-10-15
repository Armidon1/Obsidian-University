---
title: Momentum
tags:
  - machine-learning
  - concetto
  - optimization
  - neural-networks
---

# Momentum

> [!summary] In short
> Replace the gradient with an exponentially weighted average of past gradients, $m_{t+1}=\beta m_t+(1-\beta)\nabla L$, and step along it: damps oscillations and accelerates along consistent directions.

$$m_{t+1}\leftarrow\beta m_t+(1-\beta)\nabla L(\varphi_t),\qquad\varphi_{t+1}\leftarrow\varphi_t-\alpha m_{t+1},\qquad\beta\in[0,1)$$

$\beta=0$ → plain SGD. Larger $\beta$ → longer memory.

## Links

- **Related concepts**: [[Adam Optimizer]] · [[Stochastic Gradient Descent]] · [[Gradient Descent]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[10 - ML - Training Neural Networks#Momentum|Lecture 10 — Momentum]]
