# Definition
>[!Definition] Definition 1.3 (Expected Risk).
> Given distribution $D$ on $\mathcal{X}\times\mathcal{Y}$ and loss function $l:\mathcal{Y}\times\mathcal{Y}\rightarrow\mathbb{R}$, the expected risk of a predictor $f:\mathcal{X}\rightarrow\mathcal{Y}$ is defined as:
$$R(f)=\mathbb{E}[l(f(X),Y)]$$Which is equals to $$R(f) = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} \underbrace{l(f(x), y)}_{\text{il valore della funzione}} \cdot \underbrace{P(X=x, Y=y)}_{\text{la probabilità della coppia}}$$

# 2.7 Concept: The Expected Risk ($R(\theta)$)

While the **[[Empirical Risk]]** is what we _minimize_ (the tool), the **Expected Risk** is what we _care about_ (the goal). It measures the generalization performance of our model on the real world, not just on the data we have collected.

## 1. Definition and Goal

The Expected Risk $R(\theta)$ quantifies the average squared error of a predictor $f_\theta(x)$ on a new, unseen data point $(X, Y)$ drawn from the true (unknown) distribution $D$.

### The Formula

$$ R(\theta) = \mathbb{E}_{(X,Y) \sim D} [(Y - \phi(X)^T \theta)^2] $$

- Unlike the empirical sum, this is an **Expectation** (a weighted average based on probability).
- It weighs every possible scenario by how likely it is to happen in reality.

---

## 2. Decomposition under Linear Assumption

If we assume the "Linear Assumption" holds ($Y = \phi(X)^T \theta^* + \epsilon$), we can derive an exact formula for the risk of any parameter vector $\theta$ (Proposition 3.5). This reveals that error comes from two distinct places.

$$ R(\theta) = \underbrace{(\theta^* - \theta)^T \Sigma (\theta^* - \theta)}_{\text{Estimation Error}} + \underbrace{R(\theta^*)}_{\text{Irreducible Noise}} $$

### Component 1: The Irreducible Noise ($R(\theta^*) = \sigma^2$)

Even if we knew the perfect parameters $\theta^*$, we would not get zero error.

- The world is noisy ($\epsilon$).
- $R(\theta^*) = \sigma^2$ represents the "Noise Floor". No model can ever beat this.

### Component 2: The Estimation Error

This is the "penalty" for not knowing the truth.

- It depends on the distance between our weights and the truth: $(\theta^* - \theta)$.
- It is weighted by the **Covariance Matrix** $\Sigma = \mathbb{E}[\phi(X)\phi(X)^T]$. This means errors matter more in directions where data is dense (high variance).

---

## 3. The Risk of the OLS Estimator

Since we compute $\hat{\theta}$ using random data, $\hat{\theta}$ itself is a random variable. We calculate the **Expected Value of the Risk** over all possible training sets (Proposition 3.6).

$$ \mathbb{E}[R(\hat{\theta})] = \sigma^2 + \frac{\sigma^2}{n} \mathbb{E}[\text{Tr}(\Sigma \hat{\Sigma}^{-1})] $$

Where:

- $\sigma^2$ is the noise.
- $n$ is the sample size.
- $\Sigma$ is the true population covariance.
- $\hat{\Sigma} = \frac{1}{n}\Phi^T\Phi$ is the empirical covariance.

### Key Takeaway: The "Cost of Learning"

The second term $\frac{\sigma^2}{n}(\dots)$ represents the **Variance of the Estimator**.

- It shows that our error on new data **decreases** as $n$ increases (roughly proportional to $1/n$).
- It shows that error **increases** if the data is noisy ($\sigma^2$ is large).

---

## 4. Summary: Empirical vs. Expected

|Feature|Empirical Risk $\hat{R}$|Expected Risk $R$|
|:--|:--|:--|
|**Perspective**|**The Past:** Performance on data we already have.|**The Future:** Performance on data we haven't seen yet.|
|**Calculation**|Easy: Simple arithmetic mean.|Impossible: Requires knowing the unknown distribution $D$ and $\theta^*$.|
|**Optimization**|We minimize this directly (OLS).|We hope to minimize this indirectly.|
|**Formula**|$\frac{1}{n} \|y - \Phi\theta\|

> **Critical Insight:** We minimize the Empirical Risk as a **proxy**. Because the OLS estimator is unbiased and consistent, minimizing the error on the training set (Empirical) typically drives down the error on the real world (Expected), provided we have enough data ($n$) to avoid Overfitting.

---