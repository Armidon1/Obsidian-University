---
title: Logistic Regression and Softmax
aliases:
  - ML — Logistic Regression and Softmax
  - ML Week 4
tags:
  - machine-learning
  - classification
  - logistic-regression
  - softmax
  - cross-entropy
  - fusco
source: PDF/part1/Week 4 - Logistic & Softmax.pdf
---

# Logistic Regression and Softmax

> [!abstract]
> Fourth week of Part 1. We reuse the linear-in-parameters models of [[02 - ML - Linear Regression and OLS|Week 2]] for **classification**: a linear score $\phi(x)^T\theta$ is squashed by the **sigmoid** into a probability (logistic regression), and for $K$ classes $K$ scores are normalised by the **softmax** (softmax regression). The right loss for probabilities comes from the **Kullback–Leibler divergence** and turns out to be the **cross-entropy** (= negative log-likelihood). There is no closed form, but the log-likelihood is **concave**, so (stochastic) gradient ascent from [[03 - ML - Overfitting, Regularization and Gradient Descent|Week 3]] finds the global optimum.
>
> These are exactly the output layers and losses used in neural-network classifiers ([[09 - ML - Feed-Forward Neural Networks#Binary classification|Part 2]]); the sigmoid is also the first activation function we meet there.
>
> Index: [[MOC - Machine Learning]] · Previous version: [[4 - ML - Logistic and Softmax Regression]]

---

## 1. Logistic regression

See [[Sigmoid Function]] and [[Logistic Regression]].

**Goal.** Binary classification, $\mathcal{Y}=\{0,1\}$. Instead of predicting the label directly we would like to predict $\mathbb{P}(Y=1\mid X=x)$ — which, by [[01 - ML - Decision Theory and Naive Bayes#3. Binary classification|Week 1]], is exactly what the Bayes optimal predictor needs. A linear score $\phi(x)^T\theta\in\mathbb{R}$ is a good measure of "how much $x$ looks like class 1", but it is not a probability. We need a map $\mathbb{R}\to[0,1]$.

### The sigmoid

$$\sigma(z)=\frac{1}{1+e^{-z}}$$

![[ML-L04-01.png]]

*Figure 1 — the sigmoid function.* An S-shaped curve: $\sigma(z)\to0$ for $z\to-\infty$, $\sigma(0)=\frac12$, $\sigma(z)\to1$ for $z\to+\infty$; it is essentially flat outside $[-5,5]$. Large positive scores become probabilities close to 1, large negative ones close to 0.

Its derivative has a very convenient form:
$$\sigma'(z)=\frac{e^{-z}}{(1+e^{-z})^2}=\frac{1}{1+e^{-z}}\Big(1-\frac{1}{1+e^{-z}}\Big)=\sigma(z)\big(1-\sigma(z)\big).$$

> [!note] Logistic predictor
> $$h_\theta(x)=\sigma\big(\phi(x)^T\theta\big)=\frac{1}{1+e^{-\phi(x)^T\theta}}$$
> is the **logistic function**: our estimate of $\mathbb{P}(Y=1\mid X=x)$. The predicted label is $1$ if $h_\theta(x)\ge\frac12$, i.e. iff $\phi(x)^T\theta\ge0$: the decision boundary is a **hyperplane** in feature space.

> [!tip] Log-odds
> Inverting, $\phi(x)^T\theta=\log\frac{h_\theta(x)}{1-h_\theta(x)}$: logistic regression models the **log-odds** as a linear function of the features.

### Which loss for probabilities? KL divergence

See [[Kullback-Leibler Divergence]].

Squared error is not natural for probabilities (and would make the problem non-convex). We compare distributions instead. For two distributions $p,q$ over a discrete support:
$$D_{KL}(p\,\|\,q)=\sum_i p_i\log\frac{p_i}{q_i},\qquad\text{with }0\cdot\log\infty=0=0\cdot\log 0 .$$

Properties:
- $D_{KL}(p\|q)\ge0$, with equality iff $p=q$ (Gibbs' inequality);
- it does not depend on the *values* of the outcomes, only on their probabilities;
- it weighs the log-ratio of each outcome by its probability under $p$;
- it is **not symmetric** ($D_{KL}(p\|q)\neq D_{KL}(q\|p)$ in general) and therefore not a true distance — a classic exam question (First Session, Q4).

**Tentative objective:** make the predicted Bernoulli$(h_\theta(x))$ close to the conditional distribution of $Y$ given $X=x$. Empirically, for sample $i$ the "true" distribution is deterministic: label $y_i$ with probability 1. Summing the KL divergences:
$$\sum_{i=1}^n\Big[y_i\log\frac{y_i}{h_\theta(x_i)}+(1-y_i)\log\frac{1-y_i}{1-h_\theta(x_i)}\Big]=\underbrace{\sum_i\big[y_i\log y_i+(1-y_i)\log(1-y_i)\big]}_{=0,\ \text{independent of }\theta}-\sum_i\big[y_i\log h_\theta(x_i)+(1-y_i)\log(1-h_\theta(x_i))\big].$$
(The first sum is $0$ by the convention, since $y_i\in\{0,1\}$; the handout highlights it in red as "not depending on the predictor".)

### Cross-entropy and log-likelihood

See [[Cross-Entropy Loss]].

> [!important] Cross-entropy (binary)
> $$\text{CE}(\theta)=-\sum_{i=1}^n\Big[y_i\log h_\theta(x_i)+(1-y_i)\log\big(1-h_\theta(x_i)\big)\Big]$$
> Equivalently, **maximise the (normalised) log-likelihood**
> $$\hat\ell(\theta)=\frac1n\sum_{i=1}^n\Big[y_i\log h_\theta(x_i)+(1-y_i)\log\big(1-h_\theta(x_i)\big)\Big].$$

> [!tip] Why "log-likelihood"
> Under the model, $\mathbb{P}(Y=y_i\mid x_i)=h_\theta(x_i)^{y_i}(1-h_\theta(x_i))^{1-y_i}$. The likelihood of independent samples is the product of these; its log is exactly $n\hat\ell(\theta)$. So minimising cross-entropy = **maximum likelihood estimation**.

> [!example] What the loss punishes
> If $y_i=1$ the term is $-\log h_\theta(x_i)$: $0$ when the model is sure and right ($h=1$), $\approx0.69$ at $h=0.5$, and $\to\infty$ when the model is sure and wrong ($h\to0$). Confident mistakes are very expensive.

### Gradient (ascent)

There is **no closed form** for $\arg\max_\theta\hat\ell(\theta)$, but we can use (stochastic) gradient ascent. Using $\sigma'=\sigma(1-\sigma)$ and the chain rule ($\partial_{\theta_j}\phi(x)^T\theta=\phi_j(x)$):
$$\frac{\partial\hat\ell}{\partial\theta_j}=\frac1n\sum_{i=1}^n\Big[y_i\big(1-\sigma(\phi(x_i)^T\theta)\big)-(1-y_i)\,\sigma(\phi(x_i)^T\theta)\Big]\phi_j(x_i)=\frac1n\sum_{i=1}^n\big[y_i-h_\theta(x_i)\big]\phi_j(x_i).$$

> [!warning] Correzione
> In the second line of the derivative the handout drops the factor $\frac1n$ that appears in the first line. It does not matter for the direction of the step (it can be absorbed in the learning rate), but the equality as written is wrong.

The gradient has the same shape as in linear regression: **(error) × (feature)**, with the error now $y_i-h_\theta(x_i)$.

**Second derivatives:**
$$\frac{\partial^2\hat\ell}{\partial\theta_j\partial\theta_k}=-\frac1n\sum_i\sigma(\phi(x_i)^T\theta)\big(1-\sigma(\phi(x_i)^T\theta)\big)\phi_j(x_i)\phi_k(x_i),\qquad H=-\frac1n\sum_i h_\theta(x_i)\big(1-h_\theta(x_i)\big)\phi(x_i)\phi(x_i)^T .$$
Each term $c_i\,\phi(x_i)\phi(x_i)^T$ with $c_i=h(1-h)\ge0$ is PSD ($v^T\phi\phi^Tv=(\phi^Tv)^2\ge0$), so $H$ is **negative semi-definite**: $\hat\ell$ is **concave**, and gradient ascent converges to a global maximum.

> [!important] Updates
> **Gradient ascent:** $\displaystyle\theta_{t+1}=\theta_t+\frac{\gamma_t}{n}\sum_{i=1}^n\big(y_i-h_{\theta_t}(x_i)\big)\phi(x_i)$
>
> **Stochastic gradient ascent:** pick $i$ uniformly at random and $\theta_{t+1}=\theta_t+\gamma_t\big(y_i-h_{\theta_t}(x_i)\big)\phi(x_i)$.

Compare with the Perceptron update in [[05 - ML - Perceptron, SVM and Kernels#1. The Perceptron|Week 5]]: same structure, but the logistic one moves by an amount proportional to how wrong the *probability* is, also on correctly classified points (Simone's comparison: [[Perceptron vs Logistic Regression]]).

---

## 2. Multiclass classification — softmax regression

See [[Softmax Regression]].

Now $\mathcal{Y}=\{1,\dots,K\}$. Give each class its own parameter vector $\theta^{(k)}\in\mathbb{R}^d$ and **score** $s_k(x)=\phi(x)^T\theta^{(k)}$, then turn scores into probabilities with the **softmax**:
$$\hat p_k(x)=\frac{e^{s_k(x)}}{\sum_{\ell=1}^K e^{s_\ell(x)}} .$$

> [!note]
> $\hat p_k(x)$ is our estimate of $\mathbb{P}(Y=k\mid X=x)$: all positive and summing to 1. The predicted class is $\arg\max_k\hat p_k(x)=\arg\max_k s_k(x)$ (the exponential is increasing). With $K=2$ softmax reduces to the sigmoid of the score difference: $\hat p_1=\frac{1}{1+e^{-(s_1-s_2)}}$.

**Log-likelihood.** Encode labels one-hot: $y_i^{(k)}=1$ if $y_i=k$, else $0$. Then
$$\hat\ell(\Theta)=\frac1n\sum_{i=1}^n\sum_{k=1}^K y_i^{(k)}\log\hat p_k(x_i),$$
maximised over $\Theta=(\theta^{(1)},\dots,\theta^{(K)})$ ($K\cdot d$ parameters). Its opposite is the multiclass cross-entropy.

**Gradient.** Using $\partial\log\hat p_\ell/\partial s_k=\mathbb{1}\{\ell=k\}-\hat p_k$ and $\sum_\ell y_i^{(\ell)}=1$:
$$\nabla_{\theta^{(k)}}\hat\ell(\Theta)=\frac1n\sum_{i=1}^n\big(y_i^{(k)}-\hat p_k(x_i)\big)\phi(x_i),\qquad \theta^{(k)}_t=\theta^{(k)}_{t-1}+\gamma_t\nabla_{\theta^{(k)}}\hat\ell(\Theta_{t-1}).$$

> [!warning] Correzione
> The handout writes $\nabla_{\theta^{(k)}}\hat\ell=\frac1n\sum_i(\hat p_k(x_i)-y_i)\phi(x_i)$. Two issues: the sign is flipped (that is the gradient of the *cross-entropy*, i.e. of $-\hat\ell$; with it, the "gradient ascent" update would descend the likelihood), and $y_i$ should be the one-hot component $y_i^{(k)}$. With $K=2$ the correct formula gives back the logistic one.

### Concavity

> [!important] Lemma 2.1
> $f(z_1,\dots,z_K)=-\log\sum_{k=1}^K e^{z_k}$ is concave.

**Proof.** Let $S=\sum_ke^{z_k}$ and $\pi_k=e^{z_k}/S$ (a probability vector). Derivatives:
$$\frac{\partial f}{\partial z_i}=-\pi_i,\qquad\frac{\partial^2f}{\partial z_i^2}=-\frac{e^{z_i}(S-e^{z_i})}{S^2}=-\pi_i+\pi_i^2,\qquad\frac{\partial^2f}{\partial z_i\partial z_j}=\frac{e^{z_i+z_j}}{S^2}=\pi_i\pi_j .$$
So $H=\pi\pi^T-\operatorname{diag}(\pi)$ and for every $v\in\mathbb{R}^K$:
$$v^THv=\Big(\sum_k\pi_kv_k\Big)^2-\sum_k\pi_kv_k^2=-\Big(\mathbb{E}_\pi[V^2]-\mathbb{E}_\pi[V]^2\Big)=-\operatorname{Var}_\pi(V)\le0,$$
where $V$ is the random variable taking value $v_k$ with probability $\pi_k$. Hence $H$ is negative semi-definite and $f$ is concave. $\blacksquare$

> [!warning] Correzione
> Several typos in the handout's proof:
> - $\partial^2f/\partial z_i^2$ is written $+\frac{e^{z_i}(S-e^{z_i})}{S^2}$; the correct sign is **minus** (otherwise $H$ would not be $\pi\pi^T-\operatorname{diag}(\pi)$);
> - $\pi$ is called "the $d$-dimensional vector $p$" and $\operatorname{diag}(\pi)$ "$d\times d$": it is $K$-dimensional / $K\times K$;
> - it says "we conclude by showing that $H$ is positive semi-definite, which implies convexity", but then (correctly) shows $v^THv\le0$, i.e. **negative** semi-definite → **concavity**, which is what the Lemma states;
> - the sum $\sum_{k=1}^{T}$ should be $\sum_{k=1}^{K}$.

> [!important] Theorem 2.2
> $\hat\ell(\Theta)$ is concave.

**Proof.** Looking at the full Hessian (a $(K d)\times(K d)$ matrix) is painful; instead decompose $\hat\ell$ into simple pieces:
$$\hat\ell(\Theta)=\frac1n\sum_{i=1}^n\sum_{k=1}^K y_i^{(k)}\Big(s_k(x_i)-\log\sum_\ell e^{s_\ell(x_i)}\Big)=\frac1n\sum_{i=1}^n\Big(\sum_k y_i^{(k)}\phi(x_i)^T\theta^{(k)}-\log\sum_{\ell}e^{s_\ell(x_i)}\Big)$$
(using $\sum_k y_i^{(k)}=1$). The first term is **linear** in $\Theta$ (both convex and concave). The second is $f$ of Lemma 2.1 composed with the **linear** map $\Theta\mapsto(s_1(x_i),\dots,s_K(x_i))$, and a concave function of an affine map is concave. A sum of concave functions is concave. $\blacksquare$

> [!warning] Correzione
> The handout says the Hessian is a $(K\cdot\mathbf{n})\times(K\cdot\mathbf{n})$ matrix; the parameters are $K$ vectors in $\mathbb{R}^d$, so it is $(K\cdot\mathbf{d})\times(K\cdot\mathbf{d})$. It also refers to "Theorem 2.1" for what is Lemma 2.1.

| | Logistic regression | Softmax regression |
|---|---|---|
| Labels | $\{0,1\}$ | $\{1,\dots,K\}$ (one-hot) |
| Parameters | $\theta\in\mathbb{R}^d$ | $\theta^{(1)},\dots,\theta^{(K)}\in\mathbb{R}^d$ |
| Output | $\sigma(\phi^T\theta)$ | $\operatorname{softmax}(\phi^T\theta^{(1)},\dots,\phi^T\theta^{(K)})$ |
| Loss | binary cross-entropy | categorical cross-entropy |
| Gradient | $(y-h)\phi$ | $(y^{(k)}-\hat p_k)\phi$ |
| Optimisation | concave → gradient ascent | concave → gradient ascent |

---

## Pointers

Based on Andrew Ng, *CS229 lecture notes* (2022), Ch. 2, and Géron, *Hands-On Machine Learning* (2019), end of Ch. 4 (Notebook 2 on Classroom).

## Video

- [StatQuest: Logistic Regression](https://www.youtube.com/watch?v=yIYKR4sgzI8)
- [Logistic Regression Details Pt 2: Maximum Likelihood — StatQuest](https://m.youtube.com/watch?v=BfKanl1aSG0)
- [Odds and Log(Odds), Clearly Explained — StatQuest](https://www.youtube.com/watch?v=ARfXDSkQf1Y)
