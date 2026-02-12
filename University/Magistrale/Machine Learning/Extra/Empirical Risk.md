# 2.1.3 Concept: The Empirical Risk ($\hat{R}$)

In Supervised Learning, specifically in Linear Regression, we need a metric to evaluate how well our model fits the data. This metric is the **Empirical Risk** (often called Empirical Mean Square Error or MSE).

## 1. Definition

The Empirical Risk is the **average squared error** calculated strictly on the available training dataset of $n$ samples. It measures the discrepancy between the true labels $y_i$ and the predictions made by our model $f_\theta(x_i)$.

### The Formula (Scalar Notation)

For a dataset $S = {(x_1, y_1), \dots, (x_n, y_n)}$ and a predictor $f_\theta$, the empirical risk is defined as:

$$ \hat{R}(\theta) = \frac{1}{n} \sum_{i=1}^{n} (y_i - f_\theta(x_i))^2 $$

In the specific case of 1-D Linear Regression ($f(x) = mx + q$), this becomes: $$ \hat{R}(m, q) = \frac{1}{n} \sum_{i=1}^{n} (mx_i + q - y_i)^2 $$

### The Formula (Matrix Notation)

To make calculations efficient in higher dimensions, we express this using the target vector $y$ and the feature matrix $\Phi$. The sum of squared errors becomes the squared Euclidean norm of the difference vector:

$$ \hat{R}(\theta) = \frac{1}{n} |y - \Phi\theta|_2^2 $$

---

## 2. Why "Empirical"? (The Proxy Concept)

The term "Empirical" means "based on observation". This distinguishes it from the theoretical "Expected Risk" ($R(\theta)$).

- **The Goal:** We _want_ to minimize the **Expected Risk** $R(\theta) = \mathbb{E}[(Y - f(X))^2]$, which represents the error on infinite future data.
- **The Problem:** We cannot calculate the Expected Risk because we do not know the true data distribution $D$.
- **The Solution:** We use the $n$ observed samples as a **proxy** for the true distribution. We assume that minimizing the error on the _sample_ (Empirical Risk) will also minimize the error on the _population_ (Expected Risk).

> **Note:** As discussed, the Empirical Risk acts as a **simple arithmetic mean** (weight $1/n$ for each point), whereas the Expected Risk is a **weighted mean** based on true probabilities.

---

## 3. Properties for Optimization

Why do we love this specific function?

1. **Convexity:** The function is a quadratic polynomial (shaped like a bowl). This guarantees that any local minimum is the **global minimum**.
2. **Coercivity:** As the parameters $\theta$ grow to infinity, the error also grows to infinity. This ensures a minimum exists.
3. **Differentiability:** We can easily take partial derivatives with respect to $\theta$ and set them to zero to find the solution analytically (OLS Estimator).

---

## 4. Summary Table

|Feature|Empirical Risk $\hat{R}(\theta)$|Expected Risk $R(\theta)$|
|:--|:--|:--|
|**Formula**|$\frac{1}{n} \sum (y_i - f(x_i))^2$|$\mathbb{E}[(Y - f(X))^2]$|
|**Data Source**|Training Set ($n$ samples)|True Distribution ($D$)|
|**Role**|**Optimization Objective** (What we minimize)|**Evaluation Goal** (What we care about)|
|**Knowledge**|Fully Known|Unknown (Estimated)|

---