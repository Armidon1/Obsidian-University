# 4 Week 4: Logistic and Softmax Regression

## 4.1 Classification with "Linear" Regression: Logistic Regression

We want to use our insight on linear regression for binary classification, i.e., in the supervised learning setting where the label set $Y$ consists of only two classes, let's say $\{0,1\}$.

We can use linear functions as a "score" for the likelihood of a certain $x$ to be associated with the label 1. To this end, we introduce the sigmoid function:

$$
\sigma(z) = \frac{1}{1+e^{-z}}
$$

The sigmoid function maps $\mathbb{R}$ in $[0, 1]$, meaning that we can interpret its output as probabilities. Moreover, its derivative has a very convenient form:

$$
\sigma'(z) = \frac{e^{-z}}{(1+e^{-z})^2} = \frac{1}{1+e^{-z}} \left( 1 - \frac{1}{1+e^{-z}} \right) = \sigma(z)(1 - \sigma(z))
$$

In this section, we predict the probabilities with the following rule:

$$
h_{\theta}(x)=\sigma(\phi(x)^{T}\theta)=\frac{1}{1+e^{-\phi(x)^{T}\theta}}
$$

This is called a logistic function, and ideally tells us how likely a given class is to realize!

Given the prediction made by the logistic predictor, it is immediate to design the corresponding prediction: if $h_{\theta}(x)\ge1/2$ then the predicted label is 1, otherwise, it is 0. Now the question is about what is a good loss for probabilities.

Given two probabilities $p$ and $q$ over a discrete support, we define the Kullback-Leibler divergence (KL in short) as:

$$
D_{KL}(p||q)=\sum_{i}p_{i}\log\frac{p_{i}}{q_{i}}
$$

where $p_i$ and $q_i$ are the probabilities of observing the $i^{th}$ outcome, and we adopt the convention that $0\times \log\frac{0}{q}=0$ and $p\times \log\frac{p}{0}=\infty$.

We have the following properties:
* The KL divergence is non-negative, and it is equal to zero only if $p=q$.
* It does not depend on the actual values of the support of the distribution.
* It weights the log of the probabilities by the probability of each class.

This gives us a tentative objective: minimize the KL divergence between the true conditional probability $p(y|x)$ and our predicted $h_{\theta}(x)$.

Let's now look at the empirical error over $n$ samples of the form $(x_{i},y_{i})$, where $y_{i}\in\{0,1\}$. For point $i$, the true distribution is $p_{i}=(1-y_{i},y_{i})$ and the predicted one is $q_i = (1-h_{\theta}(x_{i}), h_{\theta}(x_{i}))$.

We are measuring the KL divergence:

$$
D_{KL}(p_{i}||q_{i})=\sum_{k\in\{0,1\}}p_{i}(k)\log\frac{p_{i}(k)}{q_{i}(k)}
$$

$$
=y_{i}\log\frac{y_{i}}{h_{\theta}(x_{i})}+(1-y_{i})\log\frac{1-y_{i}}{1-h_{\theta}(x_{i})}
$$

The total empirical risk is $\frac{1}{n}\sum_{i=1}^{n}D_{KL}(p_{i}||q_{i})$:

$$
\frac{1}{n}\sum_{i=1}^{n}\left[y_{i}\log\frac{y_{i}}{h_{\theta}(x_{i})}+(1-y_{i})\log\frac{1-y_{i}}{1-h_{\theta}(x_{i})}\right]
$$

$$
=\frac{1}{n}\sum_{i=1}^{n}[y_{i}\log~y_{i}+(1-y_{i})\log(1-y_{i})]-\frac{1}{n}\sum_{i=1}^{n}[y_{i}\log~h_{\theta}(x_{i})+(1-y_{i})\log(1-h_{\theta}(x_{i}))]
$$

The first terms do not depend on the predictor, so our goal is to find $\theta$ that minimizes the negative log-likelihood, which is also called the cross-entropy:

$$
J(\theta)=-\frac{1}{n}\sum_{i=1}^{n}[y_{i}\log~h_{\theta}(x_{i})+(1-y_{i})\log(1-h_{\theta}(x_{i}))]
$$

Alternatively, we could aim at maximizing the (rescaled) log-likelihood:

$$
\hat{l}(\theta)=\frac{1}{n}\sum_{i=1}^{n}[y_{i}\log~h_{\theta}(x_{i})+(1-y_{i})\log(1-h_{\theta}(x_{i}))]=-J(\theta).
$$

Unfortunately, there is no closed formula for finding $\arg \max \hat{l}(\theta)$, but we can always resort to (stochastic) gradient descent (or ascent for maximization).

Let's compute the gradient of $\hat{l}(\theta)$ w.r.t a single $\theta_{j}$:

$$
\frac{\partial\hat{l}}{\partial\theta_{j}}=\frac{1}{n}\sum_{i=1}^{n}\left[\frac{y_{i}}{h_{\theta}(x_{i})}\frac{\partial h_{\theta}(x_{i})}{\partial\theta_{j}}+\frac{1-y_{i}}{1-h_{\theta}(x_{i})}\frac{\partial(1-h_{\theta}(x_{i}))}{\partial\theta_{j}}\right]
$$

$$
\frac{\partial h_{\theta}(x_{i})}{\partial\theta_{j}}=\frac{\partial\sigma(z_{i})}{\partial z_{i}}\frac{\partial z_{i}}{\partial\theta_{j}} \quad (\text{where } z_{i}=\phi(x_{i})^{T}\theta)
$$

$$
=\sigma(z_{i})(1-\sigma(z_{i}))\cdot\phi_{j}(x_{i})=h_{\theta}(x_{i})(1-h_{\theta}(x_{i}))\phi_{j}(x_{i})
$$

Plugging this back in:

$$
\frac{\partial\hat{l}}{\partial\theta_{j}}=\frac{1}{n}\sum_{i=1}^{n}\left[\frac{y_{i}}{h_{\theta}(x_{i})}h_{\theta}(x_{i})(1-h_{\theta}(x_{i}))\phi_{j}(x_{i})-\frac{1-y_{i}}{1-h_{\theta}(x_{i})}h_{\theta}(x_{i})(1-h_{\theta}(x_{i}))\phi_{j}(x_{i})\right]
$$

$$
=\frac{1}{n}\sum_{i=1}^{n}[y_{i}(1-h_{\theta}(x_{i}))-(1-y_{i})h_{\theta}(x_{i})]\phi_{j}(x_{i})
$$

$$
=\frac{1}{n}\sum_{i=1}^{n}[y_{i}-y_{i}h_{\theta}(x_{i})-h_{\theta}(x_{i})+y_{i}h_{\theta}(x_{i})]\phi_{j}(x_{i})
$$

$$
=\frac{1}{n}\sum_{i=1}^{n}[y_{i}-h_{\theta}(x_{i})]\phi_{j}(x_{i})
$$

Let's now look at the second derivative:

$$
\frac{\partial^{2}\hat{l}}{\partial\theta_{j}\partial\theta_{k}}=\frac{1}{n}\sum_{i=1}^{n}-\frac{\partial h_{\theta}(x_{i})}{\partial\theta_{k}}\phi_{j}(x_{i})=-\frac{1}{n}\sum_{i=1}^{n}h_{\theta}(x_{i})(1-h_{\theta}(x_{i}))\phi_{k}(x_{i})\phi_{j}(x_{i})
$$

In matrix form, this means that the Hessian is:

$$
H=-\frac{1}{n}\sum_{i=1}^{n}\sigma(z_{i})(1-\sigma(z_{i}))\phi(x_{i})\phi(x_{i})^{T}
$$

Since $\sigma(z_{i})\in[0,1]$, the term $\sigma(z_{i})(1-\sigma(z_{i}))$ is $\ge 0$. The matrix $\phi(x_{i})\phi(x_{i})^{T}$ is positive semi-definite. Therefore, the Hessian $H$ is negative semi-definite, which implies that the empirical log-likelihood $\hat{l}$ is concave. So, doing gradient ascent will converge to a global maximum.

In particular, the sequential formula for gradient ascent will be:

$$
\theta_{t+1}=\theta_{t}+\gamma_{t}\nabla\hat{l}(\theta_{t})=\theta_{t}+\frac{\gamma_{t}}{n}\sum_{i=1}^{n}(y_{i}-h_{\theta}(x_{i}))\phi(x_{i})
$$

Similarly, for stochastic gradient ascent, we can sample u.a.r. one of the $n$ points, and update with $\theta_{t+1}=\theta_{t}+\gamma_{t}(y_{i_{t}}-h_{\theta}(x_{i_{t}}))\phi(x_{i_{t}})$.

## 4.2 Multiclass Classification: Softmax Regression

We want to generalize the logistic regression to a multiclass setting, where the goal is to predict the label $Y=\{1,2,...,K\}$.

We compute a linear score for each class $s_{k}(x)=\phi(x)^{T}\theta^{(k)}$, then we transform these scores into probabilities using the soft-max function:

$$
\hat{p}_{k}(x)=\frac{e^{s_{k}(x)}}{\sum_{l=1}^{K}e^{s_{l}(x)}}
$$

We can interpret the $\hat{p}_{k}(x)$ as the probability of observing label $Y=k$ when $X=x$. Once we have the $\hat{p}_{k}(x)$, the most sensible strategy is to output the class with the largest estimated probability.

The empirical log-likelihood to maximize in this multiclass setting thus becomes (using one-hot encoding $y_{i}^{(k)}=1$ if $y_{i}=k$, 0 otherwise):

$$
\hat{l}(\Theta)=\frac{1}{n}\sum_{i=1}^{n}\sum_{k=1}^{K}y_{i}^{(k)}\log(\hat{p}_{k}(x_{i}))
$$

Note, in this setting, we are optimizing over all the $K$ d-dimensional vectors $\theta^{(k)}$ for $k=1,...,K$. We use $\Theta$ to denote this set of $K$ vectors. We can compute the gradient with respect to the generic $\theta^{(k)}$, to get:

$$
\nabla_{\theta^{(k)}}\hat{l}(\Theta)=\frac{1}{n}\sum_{i=1}^{n}(y_{i}^{(k)}-\hat{p}_{k}(x_{i}))\phi(x_{i})
$$

So, the gradient ascent formula for the $k^{th}$ weight vector becomes:

$$
\theta_{t+1}^{(k)}=\theta_{t}^{(k)}+\gamma_{t}\frac{1}{n}\sum_{i=1}^{n}(y_{i}^{(k)}-\hat{p}_{k}(x_{i}))\phi(x_{i})
$$

We conclude our study of softmax regression by arguing that the loss function is indeed convex. Before doing so, we prove a preliminary lemma.

**Lemma 2.1.** The function $f:\mathbb{R}^{K}\rightarrow\mathbb{R}$ (log-sum-exp) defined as follows is convex:

$$
f(z_{1},...,z_{K})=\log\sum_{k=1}^{K}e^{z_{k}}
$$

**Proof.** We denote with $S$ the sum of the exponential terms, namely $S=\sum_{k}e^{z_{k}}$. We start by computing the partial derivatives:

$$
\frac{\partial f(z)}{\partial z_{i}}=\frac{e^{z_{i}}}{S}=\pi_{i}
$$

$$
\frac{\partial^{2}f(z)}{\partial z_{i}^{2}}=\frac{e^{z_{i}}S-e^{z_{i}}e^{z_{i}}}{S^{2}}=\frac{e^{z_{i}}}{S}\left(1-\frac{e^{z_{i}}}{S}\right)=\pi_{i}(1-\pi_{i})
$$

$$
\frac{\partial^{2}f(z)}{\partial z_{i}\partial z_{j}} = -\frac{e^{z_{i}}e^{z_{j}}}{S^{2}} = -\pi_{i}\pi_{j} \quad (i\ne j)
$$

We can write the Hessian matrix of $f$ in a convenient way: Denote with $\pi$ the K-dimensional vector such $\pi_{k}=e^{z_{k}}/S$. We have the following:

$$
H_{ij}=\frac{\partial^{2}f(z)}{\partial z_{i}\partial z_{j}}\Rightarrow H=diag(\pi)-\pi\pi^{T}
$$

This matrix $H$ is the covariance matrix of a multinomial distribution with probabilities $\pi$, and is known to be positive semi-definite. Therefore, $f(z)$ is convex. $\Pi$

**Theorem 2.2.** The function $\hat{l}(\Theta)$ is concave.

**Proof.** We rewrite $\hat{l}$ using $s_{k}(x_{i})=\phi(x_{i})^{T}\theta^{(k)}$:

$$
\hat{l}(\Theta)=\frac{1}{n}\sum_{i=1}^{n}\sum_{k=1}^{K}y_{i}^{(k)}\log\left(\frac{e^{s_{k}(x_{i})}}{\sum_{l}e^{s_{l}(x_{i})}}\right)
$$

$$
=\frac{1}{n}\sum_{i=1}^{n}\sum_{k=1}^{K}y_{i}^{(k)}\left(s_{k}(x_{i})-\log\sum_{l}e^{s_{l}(x_{i})}\right)
$$

$$
=\frac{1}{n}\sum_{i=1}^{n}\left[\left(\sum_{k=1}^{K}y_{i}^{(k)}s_{k}(x_{i})\right)-\left(\sum_{k=1}^{K}y_{i}^{(k)}\right)\log\sum_{l}e^{s_{l}(x_{i})}\right]
$$

(Since $\sum_{k}y_{i}^{(k)}=1$)

$$
=\frac{1}{n}\sum_{i=1}^{n}\left[\left(\sum_{k=1}^{K}y_{i}^{(k)}\phi(x_{i})^{T}\theta^{(k)}\right)-\log\sum_{l}e^{s_{l}(x_{i})}\right]
$$

The first term, $\sum_{k}y_{i}^{(k)}\phi(x_{i})^{T}\theta^{(k)}$ is a linear function of all the parameters in $\Theta$, therefore it is both concave and convex.

The second term is $-f(s(x_{i}))$, where $f$ is the log-sum-exp function from Lemma 2.1, and $s(x_{i})$ is the vector of scores, which is a linear map from $\Theta$. Since $f$ is convex (by Lemma 2.1) and composition with a linear map preserves convexity, $f(s(x_{i}))$ is convex in $\Theta$.

Therefore, $-f(s(x_{i}))$ is concave in $\Theta$. All in all, $\hat{l}(\Theta)$ is concave as it is the sum of two concave functions (a linear function and a concave function). $\Pi$