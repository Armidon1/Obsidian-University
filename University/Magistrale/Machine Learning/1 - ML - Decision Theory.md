# Week 1: Decision Theory

## 1.1 Introduction

In these notes, we briefly cover the basic notions of decision theory.

**The setting** follows: there is a joint distribution $D$ over $\mathcal{X}\times\mathcal{Y}$, where $\mathcal{X}$ is the input or feature space and $\mathcal{Y}$ is the label space.

We aim to find a good **predictor**, i.e., a function $f:\mathcal{X}\rightarrow\mathcal{Y}$ that maps feature vectors to the corresponding label $y\in\mathcal{Y}$. To mathematically measure the performance of any such predictor, we need to specify a performance metric.

We then assume to have a **loss function** $l:\mathcal{Y}\times\mathcal{Y}\rightarrow\mathbb{R}$. In practice, $l(a,b)$ measures the loss when the predictor guesses label $a$, while the actual label is $b$.

**Example 1.1.** We report here the most common loss functions:
* The 0-1 loss, common for classification: $l(a,b)=\mathbb{I}\{a\ne b\}$
* The squared loss for regression: $l(a,b)=(a-b)^{2}$
* The absolute loss for regression: $l(a,b)=|a-b|$

**Example 1.2 (Binary Classification).** Consider a binary classification task, i.e., when $\mathcal{Y}=\{0,1\}$. Any loss for this problem is fully specified by four numbers: $l(1,1)$ (the loss value for true positive TP), $l(0,0)$ (for true negative TN), $l(1,0)$ (for false positive), and $l(0,1)$ (for false negative).

While the distribution $D$ is given by the environment, the loss function is a modeling choice of the model designer. Depending on the application at hand, you may want to choose specific loss functions.

>[!Definition] Definition 1.3 (Expected Risk).
> Given distribution $D$ on $\mathcal{X}\times\mathcal{Y}$ and loss function $l:\mathcal{Y}\times\mathcal{Y}\rightarrow\mathbb{R}$, the expected risk of a predictor $f:\mathcal{X}\rightarrow\mathcal{Y}$ is defined as:
$$R(f)=\mathbb{E}[l(f(X),Y)]$$Which is equals to $$R(f) = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} \underbrace{l(f(x), y)}_{\text{il valore della funzione}} \cdot \underbrace{P(X=x, Y=y)}_{\text{la probabilità della coppia}}$$

We remark that the expectation in the definition of risk is with respect to the random sampling of $(X, Y)$ according to $D$.

**Example 1.4.** Consider a binary classification task on $\mathcal{X}=\{1,2,3\}$ with the 0-1 loss, and a predictor $f$ that maps $\{1,3\}$ in $1$ and $\{2\}$ in $0$. We want to compute its expected risk when $(X, Y)$ follows the following distribution:
* $\mathbb{P}(X=1,Y=0)=0$
* $\mathbb{P}(X=1,Y=1)=1/6$
* $\mathbb{P}(X=2,Y=0)=1/2$
* $\mathbb{P}(X=2,Y=1)=1/12$
* $\mathbb{P}(X=3,Y=0)=1/12$
* $\mathbb{P}(X=3,Y=1)=1/6$

We have the following calculation:
$$R(f)=\frac{1}{12}\cdot1+\frac{1}{12}\cdot1=\frac{1}{6}$$

It is then natural to conclude that the best predictor given a fixed distribution $D$ and loss function $l$ is one that minimizes the expected risk. (better explanation [[Spiegazione Example 1.4 ML|here]])

>[!Definition] Definition 1.5 ((Bayes) Optimal Predictor).
> Given distribution $D$ on $\mathcal{X}\times\mathcal{Y}$ and loss function $l:\mathcal{Y}\times\mathcal{Y}\rightarrow\mathbb{R}$, a predictor $f:\mathcal{X}\rightarrow\mathcal{Y}$ is said to be optimal if it minimizes the expected risk $R(f)$.

Exploiting the rules of conditional expectation, it is fairly easy to derive a closed formula for the optimal predictor: it maps features to the label that minimizes the loss, given the realized feature.

>[!Definition] 
**Theorem 1.6.** The optimal predictor $f^{*}$ is defined as follows:
$$f^{*}(x) = \arg \min_{z} \mathbb{E}[l(z, Y) | X = x] \quad \forall x \in \mathcal{X}$$\*Note:* the expectation in the definition is only with respect to $Y$, and it is conditioned with respect to $X=x$. Furthermore, the optimal predictor may not be unique, as the arg min could contain more than one element for some $x$.

**Proof.** We start by writing down explicitly the expected risk for a generic predictor $f$:
$$R(f) = \mathbb{E}_X \left[ \mathbb{E}_{Y|X} [ l(f(X), Y) \mid X ] \right]$$
The predictor $f^{*}$ minimizes the term $\mathbb{E}[l(f(X),Y)|X]$ for each $x\in\mathcal{X}$ therefore it is optimal (see details [[Spiegazione theroem 1.6 ML|here]]). End Of Proof

The expression above may seem mysterious, but it is fairly simple if applied to specific distributions.

For instance, if $\mathcal{Y}$ is discrete, then it can be rewritten as:
$$f^{*}(x)=\arg \min_{z\in\mathcal{Y}}\sum_{y\in\mathcal{Y}}l(z,y)\mathbb{P}(Y=y|X=x)$$

Similarly, if $Y$ conditioned on $X=x$ admits a probability density function $p_{Y|X=x}$ for any $x\in\mathcal{X}$, then the optimal predictor is:
$$f^{*}(x)=\arg \min_{z\in\mathcal{Y}}\int_{\mathcal{Y}}l(z,y)p_{Y|X=x}(y)dy$$

**Example 1.7.** The predictor studied in Exercise 1.4 is optimal for that problem.

**Important:**
* Computing the Bayes optimal predictor requires exact knowledge of $D$ on $\mathcal{X}\times\mathcal{Y}$.
* There is an inherent risk that is unavoidable! There is generally no perfect predictor.

---
>[!question]
**Exercise 1.8.** Consider a regression problem on $\mathcal{X}\times\mathcal{Y}$, with $\mathcal{Y}=\mathbb{R}$ and the quadratic loss defined as $l(a,b)=(a-b)^{2}$. Compute the optimal predictor. [[Soluzione Exercise 1.8 ML|Solution here]]
>
**Exercise 1.9.** Consider a regression problem on $\mathcal{X}\times\mathcal{Y}$, with $\mathcal{Y}=\mathbb{R}$, and the absolute loss defined as $l(a,b)=|a-b|$. Compute the optimal predictor. *Hint: Assume that $Y$ conditioned on $X=x$ always admits a density function. [[Soluzione Exercise 1.9 ML|Solution here]]*
>
**Exercise 1.10.** Consider a classification task on $k$ classes with the 0-1 loss. Compute the expected risk of the randomized predictor that outputs a class uniformly at random, independently of the $x$ observed. [[Soluzione Exercise 1.10 ML|Solution here]]
>
**Exercise 1.11.** Consider the binary classification problem with $\mathcal{Y}=\{-1,1\}$ and the 0-1 loss. Relate the risk of a predictor $f$ to that of its opposite $-f$. [[Soluzione Exercise 1.11 ML|Solution here]]
>
**Exercise 1.12 (Multi-Variate Independent Gaussians).** Consider a multi-class classification problem where $\mathcal{X}=\mathbb{R}^{d}$, $\mathcal{Y}=\{1,2,...,k\}$, and the loss is the 0-1 loss. We make an assumption on the random variable $X=(X_{1},...,X_{d})$: conditioning on any $Y=j$, $X_{i}$ is an independent gaussian distribution with mean $\mu_{i}^{j}$ and standard deviation $\sigma_{i}^{j}$. Compute the optimal predictor. [[Soluzione Exercise 1.12 ML|Solution here]]

---

## 1.2 Binary Classification

In binary classification, the label set $\mathcal{Y}$ comprises only two outcomes: true/false, accept/reject, positive/negative. We use $\mathcal{Y}=\{0,1\}$ for simplicity. Any loss function for a binary classification problem is thus characterised by four numbers, corresponding to the elements of $\{0,1\}^{2}$.

>[!Proposition]
> 
**Proposition 2.1.** In binary classification with loss $l$, the optimal predictor is given by:
$$f^{*}(x)=\mathbb{I}\left\{\mathbb{P}(Y=1|X=x)\ge\frac{l(0,1)-l(0,0)}{l(1,0)-l(1,1)}\mathbb{P}(Y=0|X=x)\right\}$$

**Proof.** Consider any fixed $x\in\mathcal{X}$ we want to understand what the best outcome to predict is. We can compute explicitly the expected loss for the two options we have:
$$
\begin{cases}
l(1,1)\mathbb{P}(Y=1|X=x)+l(1,0)\mathbb{P}(Y=0|X=x) & \text{if we predict 1} \\
l(0,1)\mathbb{P}(Y=1|X=x)+l(0,0)\mathbb{P}(Y=0|X=x) & \text{if we predict 0}
\end{cases}
$$
	Therefore, it is optimal to predict 1 if the first equation is smaller than or equal to the second one, and 0 otherwise. The statement of the Proposition follows by rearranging terms. $\square$. Guarda la spiegazione [[Spiegazione Binary Classification 2.1|qui]]

Since there are only two possible outcomes for $Y$, it is easier to write the optimal predictor as follows, applying the definition of conditional probability (o meglio, non proprio la definizione di probabilità condizionata ma il [[Conditional Probability#3. Teorema di Bayes|Teorema di Bayes]]):

$$f^{*}(x)=\mathbb{I}\left\{\frac{\mathbb{P}(X=x|Y=1)}{\mathbb{P}(X=x|Y=0)}\ge\frac{[l(1,0)-l(0,0)]\mathbb{P}(Y=0)}{[l(0,1)-l(1,1)]\mathbb{P}(Y=1)}\right\}$$
Vedi la spiegazione [[Spiegazione Decision Teory 2.1.2|Qui]]


Note, the right-hand-side term appearing in this rewriting of the optimal predictor is independent from $x$, while the left-hand-side term is important enough to get its own name.

>[!Definition 2.2] (Likelihood Ratio and Test). 
>The likelihood ratio is the ratio of the likelihood functions:
$$\mathcal{L}(x)=\frac{\mathbb{P}(X=x|Y=1)}{\mathbb{P}(X=x|Y=0)}$$
A likelihood ratio test is a predictor of the form $\mathbb{I}\{\mathcal{L}(x)\ge\eta\}$, for some scalar $\eta>0$.

In the previous expression the $\eta$ was:$$\eta = \frac{[l(1,0)-l(0,0)]\mathbb{P}(Y=0)}{[l(0,1)-l(1,1)]\mathbb{P}(Y=1)}$$
It is often useful not to focus directly on the likelihood function but to apply some monotone function to simplify the calculations. In fact, $\mathbb{I}\{\mathcal{L}(x)\ge\eta\} = \mathbb{I}\{h(\mathcal{L}(x))\ge h(\eta)\}$, for any monotonically increasing function. [[ML 1 2.1.3|Spiegazione]]

>[!question]
**Exercise 2.3.** Compute the optimal predictor for the binary classification problem, where the loss is $l(a,b)=\mathbb{I}\{a\ne b\}$ and the two labels are equally likely, i.e., $\mathbb{P}(Y=1)=\mathbb{P}(Y=0)$. [[Spiegazione Exercise 2.3 ML]]
>
>**Exercise 2.4.** Compute the optimal predictor for the following binary classification problem. The labels are such that $\mathbb{P}(Y=1)=10^{-6}$, while $X$ behaves according to $\mathcal{N}(0,1)$ if $Y=0$ or according to $\mathcal{N}(s,1)$ otherwise, for some $s\in\mathbb{R}$. The loss function is ([[Spiegazione Exercise 2.4 ML]]):
>$$\begin{cases} l(0,0)=0 \\l(1,1)=-10^{6}
\end{cases}
\quad
\begin{cases}
l(1,0)=100 \\
l(0,1)=0
\end{cases}
>$$
**Exercise 2.5.** Compute the optimal predictor for the following binary classification problem with 0-1 loss. The two labels have the same probability, i.e., $\mathbb{P}(Y=1)=\mathbb{P}(Y=0)=1/2$. $X$ conditioned on $Y=0$ is a standard 2-dimensional gaussian, while conditioning on $Y=1$ is a gaussian centered in $(1,1)$ with covariance matrix $1/2\cdot I$ (where $I$ is the two dimensional identity matrix). [[Spiegazione Exercise 2.5 ML]]

There are only four possible outcomes for a binary classifier $f$. The following table:

|              | $Y=0$          | $Y=1$          |
| ------------ | -------------- | -------------- |
| **$f(X)=0$** | true negative  | false negative |
| **$f(X)=1$** | false positive | true positive  |

If we normalize with respect to the corresponding populations, we get the following rates that characterize a predictor:

* **True Positive Rate:** $TPR=\mathbb{P}(f(X)=1|Y=1)$, also called power, sensitivity, or recall.
* **False Negative Rate:** $FNR=1-TPR=\mathbb{P}(f(X)=0|Y=1)$, also known as type II error or probability of missed detection.
* **False Positive Rate:** $FPR=\mathbb{P}(f(X)=1|Y=0)$, also known as size, type I error, or probability of false alarm.
* **True Negative Rate:** $TNR=1-FPR=\mathbb{P}(f(X)=0|Y=0)$, also known as specificity.

Starting from these rates, there are a few metrics that are massively implemented in machine learning:
* **Precision:** $\mathbb{P}(Y=1|f(X)=1)$
* **F1-score:** $F_{1}$ is the harmonic mean of precision and recall.
    $$F_{1}=\frac{2\cdot Precision\cdot Recall}{Precision+Recall}$$
* **False discovery rate:** expected ratio of false positives over the total number of positives.

Suppose we want to maximize the true positive rate subject to a constraint on the false positive rate. Namely, we want to find the predictor that solves:
$$\max TPR \text{ subject to } FPR\le\alpha.$$

The following Theorem (that we do not prove) states that the right thing to do is to look at the likelihood ratio test.

**Theorem 2.6 (Neyman-Pearson Lemma).** Suppose that the conditional densities $f(x|y)$ are continuous. Then the optimal predictor that maximizes TPR with an upper bound on FPR is a likelihood ratio test.

Finally, imagine that you do not have a clear idea of what the right loss function for your problem is, but want to get the best out of the problem at hand. In other words, you may want to understand the better trade-off between recall (TPR) and size (FPR). A helpful tool is to plot for any $\alpha\in[0,1]$ what is the best TPR achievable with the constraint that $FPR\le\alpha$ in the FPR-TPR plane.

**Remark 2.7.** By Theorem 2.6, the ROC curve is given by varying the threshold in the likelihood ratio test from negative to positive infinity.

**Exercise 2.8.** Plot the ROC curve for the classification problem described in Exercise 2.4.

## 1.3 Naive Bayes Classifier

Everything worked so far by assuming full knowledge of the joint distribution $D$ over $\mathcal{X}\times\mathcal{Y}$. This is an unrealistic assumption: what's the use of learning if we know everything?

We want to estimate the conditional probabilities (i.e., the ones appearing in the left-hand side of the likelihood ratio $\mathcal{L}(x)$), for feature $x$, that is a $d$-dimensional object (either continuous or discrete). Instead of trying to learn $\mathbb{P}(X=x|Y=y)$ for all possible pairs $(x, y)$, the Naive Bayes Classifier makes the optimistic (and naive) assumption that all the coordinates $X_{1},X_{2},...,X_{d}$ of $X$ are independent, conditionally on $Y=y$.

**Example 3.1 (Discrete Random Variables).** Consider the case in which $Y=\{0,1\}$, and $\mathcal{X}=\mathcal{X}_{1}\times...\times\mathcal{X}_{d}$ is a discrete set with $|\mathcal{X}_{i}|=n_{i}$. A priori, we would need to learn $2\cdot\prod_{i}n_{i}$ numbers, namely all the $\mathbb{P}(X=(x_{1},...,x_{d})|Y=y)$.

The naive Bayes classifier assumes that all the coordinates of $x$ are independent given $Y=y$ therefore:
$$\mathbb{P}(X=(x_{1},...,x_{d})|Y=y)=\prod_{i=1}^{d}\mathbb{P}(X_{i}=x_{i}|Y=y)$$
We must only learn $2\cdot\sum_{i}n_{i}$ numbers. This is an exponentially smaller number!

**Example 3.2 (Continuous Random Variables).** Consider a multi-class classification setting where $\mathcal{X}=\mathbb{R}^{d}$ and the loss function is the 0-1. The problem is that we cannot learn in full generality a continuous number of points in a naive way!

There is a classical statistical way around it: instead of estimating the probability density function directly, we assume that the underlying distribution has a specific shape, characterized by a few parameters, and we then estimate such parameters!

For instance, we can assume that $X$ given $Y=y$ behaves as a multivariate Gaussian distribution (this is the Gaussian Naive Bayes classifier used on the iris dataset). This means that it is characterized by the covariance matrix $\Sigma\in\mathbb{R}^{d\times d}$ and mean $\mu\in\mathbb{R}^{d}$, and thus we would need to estimate $O(d^{2})$ numbers.

The naive Bayes classifier assumes that the dimensions are independent, so we would only need to learn $d$ variances and $d$ means, for a total of $O(d)$ numbers.
Remember: you have already computed the optimal predictor for this case in Exercise 1.12.

**Important:** The Naive Bayes Classifier is not one single classifier, but a method to estimate the optimal predictor. In particular, it makes the naive assumption that all the $X_{i}$ are independent, conditionally on $Y=y$. This assumption may bring poor results when the data exhibits strong (and asymmetric) correlations, but it avoids the curse of dimensionality.