For the original source (important for the prof's theorem's proofs, see [[Original 4 ML|here]])
# Week 4: Logistic and Softmax Regression

## 1. Introduction to Logistic Regression: The Sigmoid Function

In this section, we transition from linear regression to **binary classification**. Unlike linear regression, where we predict continuous values, here our goal is to assign a label $y$ to an input $x$. Specifically, we operate in a **supervised learning** setting where the label set $Y$ consists of only two classes, usually denoted as ${0, 1}$.

While we could try to use the linear functions from regression to create a "score" for how likely an input $x$ belongs to class 1, the raw output of a linear function can be any real number (from $-\infty$ to $+\infty$). This is problematic because we want a probability, which must be between 0 and 1. To solve this, we introduce a specific mathematical tool called the **sigmoid function** (often denoted as $\sigma(z)$).

The sigmoid function is defined as: $$ \sigma(z) = \frac{1}{1 + e^{-z}} $$

This function has a crucial property: it maps any real number $\mathbb{R}$ into the interval $[0,1]$. This allows us to interpret the output directly as a **probability**. Additionally, this function is mathematically convenient because its derivative can be expressed in terms of the function itself. The derivative is calculated as: $$ \sigma'(z) = \sigma(z)(1 - \sigma(z)) $$ This simple form $\sigma(1-\sigma)$ becomes very useful later when calculating gradients for optimization.

Using this, we define our **logistic predictor** (or hypothesis) $h_\theta(x)$. We take the linear combination of our input and parameters ($\phi(x)^T \theta$) and pass it through the sigmoid function: $$ h_\theta(x) = \sigma(\phi(x)^T \theta) = \frac{1}{1 + e^{-\phi(x)^T \theta}} $$

Ideally, this value $h_\theta(x)$ tells us the likelihood that a given class (specifically class 1) is realized. To make a final classification decision, we apply a threshold: if $h_\theta(x) \geq 0.5$, we predict the label is **1**; otherwise, we predict **0**.

---

Here is the next section. In this part, we tackle the problem of measuring "error" when dealing with probabilities. Since we are no longer predicting raw numbers (like in Linear Regression) but rather probabilities, we need a new metric to compare our prediction against reality.

---

## 2. Defining the Loss: Kullback-Leibler Divergence

Now that we have a predictor $h_\theta(x)$ that outputs a probability, we need a way to evaluate how "good" or "bad" this prediction is. In other words, we need a loss function. When dealing with probability distributions, the standard tool for measuring the difference between two distributions, $p$ and $q$, is the **Kullback-Leibler (KL) divergence**.

Mathematically, given two discrete probability distributions $p$ and $q$, the KL divergence is defined as: $$ D_{KL}(p|q) = \sum_{i} p_i \log \frac{p_i}{q_i} $$ This formula might look abstract, but it has very intuitive properties:

1. **Non-negativity:** It is always greater than or equal to zero ($D_{KL} \ge 0$).
2. **Identity:** It is equal to zero _if and only if_ the distributions are identical ($p = q$).
3. **Weighting:** It weights the log-ratio of the probabilities by the _true_ probability $p$, meaning it cares most about the outcomes that actually happen.

In our specific case of binary classification, we want to minimize the divergence between the **true distribution** (which we call $p$) and our **predicted distribution** (which we call $q$).

- The **true distribution** $p_i$ for a specific data point is determined by the label $y_i$. If the label is 1, the probability of being class 1 is 100%. So, $p_i = (1-y_i, y_i)$.
- The **predicted distribution** $q_i$ comes from our logistic model: $q_i = (1-h_\theta(x_i), h_\theta(x_i))$.

When we plug these specific distributions into the general KL formula and sum over all our $n$ data points, we get the total empirical risk. However, many terms in this expansion depends only on $y$ and not on our parameters $\theta$, so they can be ignored during optimization. After removing those constant terms, we represent our objective as minimizing the **Negative Log-Likelihood** (also known as **Cross-Entropy**):

$$ J(\theta) = - \frac{1}{n} \sum_{i=1}^{n} \left[ y_i \log h_\theta(x_i) + (1 - y_i) \log (1 - h_\theta(x_i)) \right] $$

This $J(\theta)$ is the function we must minimize to find the best parameters for our model.

---

Here is the third part. In this section, we focus on **optimization**. Since we cannot solve for the parameters $\theta$ directly with a simple formula (as we did in Linear Regression), we must use an iterative algorithm to find the best fit.

---

## 3. Optimization: Gradient Ascent and Convexity

Unlike linear regression, there is no "closed-form" solution (a simple equation) that gives us the optimal $\theta$ immediately. Therefore, we must rely on iterative optimization algorithms. Since our goal is to **maximize** the log-likelihood $\hat{l}(\theta)$, we use **Gradient Ascent** (or Gradient Descent if we are minimizing the negative log-likelihood).

To apply this algorithm, we first need to compute the **gradient**—the direction in which the function increases most steeply. Let's calculate the partial derivative with respect to a single parameter $\theta_j$. Through the chain rule and utilizing the convenient derivative property of the sigmoid function ($\sigma' = \sigma(1-\sigma)$), the math simplifies beautifully:

$$ \frac{\partial \hat{l}}{\partial \theta_j} = \frac{1}{n} \sum_{i=1}^{n} (y_i - h_\theta(x_i)) \phi_j(x_i) $$

This result is incredibly intuitive. The term $(y_i - h_\theta(x_i))$ represents the **error**: the difference between the true label and our prediction. We multiply this error by the input feature $\phi_j(x_i)$ and average it over all data points. This tells us exactly how to adjust $\theta_j$ to reduce the error.

But how do we know this algorithm will find the _best_ solution and not get stuck in a "local" peak? We look at the **Hessian matrix** (the matrix of second derivatives). It turns out that the Hessian for logistic regression is **negative semi-definite**. In simple terms, this means our objective function is shaped like a smooth hill (it is **concave**). Therefore, Gradient Ascent is guaranteed to converge to the **global maximum**—the absolute best parameters for our model.

Based on this, the update rule for **Gradient Ascent** at step $t$ is: $$ \theta_{t+1} = \theta_t + \gamma_t \frac{1}{n} \sum_{i=1}^{n} (y_i - h_\theta(x_i)) \phi(x_i) $$ where $\gamma_t$ is the learning rate. Alternatively, if the dataset is too large to sum over all $n$ points, we can use **Stochastic Gradient Ascent**, where we pick a single random point $i$ at each step and update: $$ \theta_{t+1} = \theta_t + \gamma_t (y_{i_t} - h_\theta(x_{i_t})) \phi(x_{i_t}) $$

---

## 4. Multiclass Classification: Softmax Regression

In the previous sections, we dealt with "binary" problems where the label $y$ could only be 0 or 1. However, in the real world, we often need to classify data into one of many different categories (e.g., identifying if an image contains a cat, a dog, or a bird). Here, the label set is $Y = {1, 2, ..., K}$.

To handle this, we generalize our approach. Instead of having a single parameter vector $\theta$, we now maintain a separate vector $\theta^{(k)}$ for _each_ class $k$. For a given input $x$, we compute a linear "score" $s_k(x)$ for every possible class: $$ s_k(x) = \phi(x)^T \theta^{(k)} $$

These scores can be any number (positive or negative), which is not useful for probabilities. To fix this, we apply the **Softmax Function**. This function does two things: it exponentiates the scores (making them all positive) and divides by the total sum of exponentials (ensuring they sum up to 1). The probability of observing class $k$ given input $x$ is: $$ \hat{p}_k(x) = \frac{e^{s_k(x)}}{\sum_{l=1}^K e^{s_l(x)}} $$

Once we have these probabilities, our prediction strategy is simple: we choose the class with the highest probability $\hat{p}_k(x)$.

To train this model, we need to maximize the **Log-Likelihood**. We use "one-hot encoding" for our labels, denoted as $y_i^{(k)}$ (which equals 1 if the true label is $k$, and 0 otherwise). The objective function $\hat{l}(\Theta)$ sums the log-probability of the _correct_ class for every data point: $$ \hat{l}(\Theta) = \frac{1}{n} \sum_{i=1}^n \sum_{k=1}^K y_i^{(k)} \log(\hat{p}_k(x_i)) $$

Finally, we need to update our parameters using Gradient Ascent. Surprisingly, even though the math for Softmax looks more complex, the gradient formula ends up looking almost identical to the binary logistic case. The gradient for the parameter vector of class $k$ is: $$ \nabla_{\theta^{(k)}} \hat{l}(\Theta) = \frac{1}{n} \sum_{i=1}^n (y_i^{(k)} - \hat{p}_k(x_i)) \phi(x_i) $$ This means the update rule is driven by the difference between the **observed truth** ($y_i^{(k)}$) and our **predicted probability** ($\hat{p}_k(x_i)$).

---

## 5. Convexity Analysis: Proving the Global Maximum

To be certain that Gradient Ascent will find the true optimal parameters for Softmax Regression, we must prove that our objective function $\hat{l}(\Theta)$ is **concave**. If it is concave, it has no "local maxima" where the algorithm could get stuck; the only peak is the global best solution. To prove this, we rely on a preliminary mathematical tool called the **Log-Sum-Exp** lemma.

### Lemma 2.1: The Log-Sum-Exp Function

First, let's look at a helper function, the "log-sum-exp" function, defined as: $$ f(z) = \log \left( \sum_{k=1}^K e^{z_k} \right) $$ We need to prove that this specific function is **convex**. We do this by analyzing its second derivative (the Hessian matrix).

1. **First Derivative:** If we take the derivative with respect to $z_i$, we get $\frac{e^{z_i}}{S}$, where $S$ is the sum of all exponentials. This is actually just the probability $\pi_i$.
2. **Second Derivative (Hessian):** When we differentiate again, we find that the Hessian matrix $H$ takes a special form: $$ H = \text{diag}(\pi) - \pi \pi^T $$ This matrix happens to be the **covariance matrix** of a multinomial distribution. In linear algebra, covariance matrices are always **positive semi-definite**. Because the Hessian is positive semi-definite, the function $f(z)$ is **convex**.

### Theorem 2.2: Concavity of the Log-Likelihood

Now we apply this lemma to our main objective function, the log-likelihood $\hat{l}(\Theta)$. We can rewrite the log-likelihood by splitting it into two distinct terms:

$$ \hat{l}(\Theta) = \frac{1}{n} \sum_{i=1}^n \left[ \underbrace{\sum_{k=1}^K y_i^{(k)} \phi(x_i)^T \theta^{(k)}}_{\text{Term 1}} - \underbrace{\log \left( \sum_{l} e^{s_l(x_i)} \right)}_{\text{Term 2}} \right] $$

Let's analyze these two terms separately:

1. **Term 1 (Linear):** This part involves $\phi(x)^T \theta$. Since it is a linear function of the parameters $\theta$, it is technically both convex and concave (it is "flat").
2. **Term 2 (Log-Sum-Exp):** This is exactly the function $f(s(x))$ we analyzed in Lemma 2.1. We proved $f$ is **convex**. However, in our formula, there is a **minus sign** in front of it. The negative of a convex function is a **concave** function.

**Conclusion:** The total function $\hat{l}(\Theta)$ is the sum of a linear function (concave) and a negative convex function (concave). Since the sum of concave functions is also concave, **$\hat{l}(\Theta)$ is concave**. This mathematically guarantees that performing Gradient Ascent on Softmax Regression will always converge to the global maximum.

---
