# 2.1.1 Concept: Empirical Mean & Empirical Risk

In Linear Regression, the word "Empirical" appears in two distinct but related contexts: the properties of the data itself ($\bar{x}$) and the error metric we minimize ($\hat{R}$). This note clarifies both and explains why we use them.

## 1. The Empirical Mean (Data Statistics)

The **Empirical Mean** is simply the average value of a variable calculated from the observed data samples. It represents the "center of mass" of your dataset.

Given $n$ pairs of data points $(x_1, y_1), \dots, (x_n, y_n)$, we define:

- **Empirical Mean of Inputs:** $\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$
- **Empirical Mean of Outputs:** $\bar{y} = \frac{1}{n} \sum_{i=1}^{n} y_i$

### Why is this important?

In the derivation of the OLS estimator (Section 2.1), we discovered a fundamental geometric property: $$ q = \bar{y} - m\bar{x} $$ This implies that **the optimal regression line always passes through the point $(\bar{x}, \bar{y})$**. The model is anchored to the empirical mean of the data.

---

## 2. The Empirical Risk (The Cost Function)

When we train a model, we want to minimize error. Ideally, we would minimize the error on _all future data_ (Expected Risk), but we can't see the future. We only have our specific dataset of size $n$.

Therefore, we minimize the **Empirical Mean Square Error (Empirical Risk)**. This is the average squared error calculated _only_ on the available data.

$$ \hat{R}(f) = \frac{1}{n} \sum_{i=1}^{n} (y_i - f(x_i))^2 $$

- The symbol $\hat{R}$ (R-hat) denotes that this is an _estimate_ based on limited data.
- We use the $n$ samples as a **proxy** for the true distribution $D$.

---

## 3. Empirical vs. Expected (The Crucial Distinction)

It is vital to distinguish between what we _do_ and what we _want_.

|Concept|Symbol|Definition|Role|
|:--|:--|:--|:--|
|**Empirical Risk**|$\hat{R}(\theta)$|Average error on the **training set** ($n$ samples).|**Optimization Objective:** We take derivatives of _this_ to find $\hat{\theta}$.|
|**Expected Risk**|$R(\theta)$|Expected error on **unseen data** (infinite samples).|**Evaluation Goal:** This measures generalization. We cannot calculate it directly, but we estimate it theoretically (Section 2.7).|

**The Connection:** By minimizing the **Empirical Risk** (fitting the data we have), we _hope_ to minimize the **Expected Risk** (fitting the reality).

- If $n$ is large (Law of Large Numbers), the empirical values converge to the true values.
- The OLS estimator uses the empirical covariance and variance to approximate the true relationship between $X$ and $Y$.

---

Questa nota si inserisce perfettamente dopo il "Warm-Up" e prima della generalizzazione, fungendo da glossario concettuale.