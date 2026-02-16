Note that this is a simplified version of the week 3: it doesn't contains proofs, so consider the case about seeing both materials 
# 3.1 & 3.2: From Linear to Polynomial Regression

### 1. Recap: The "Linear" Setup

Welcome to Week 3. Before we move forward, let's ground ourselves in what we established last week. We are solving a **Linear Regression** problem. We have a dataset of $n$ points, where each point has an input $x_i$ and a target label $y_i$.

Our goal is to find a function $f_\theta(x)$ that predicts $y$ as accurately as possible. To do this, we use **Feature Maps** ($\phi$).

- **The Model:** We define our prediction as a weighted sum of features: $$ f_\theta(x) = \sum_{j=1}^{d} \phi_j(x) \cdot \theta_j = \phi(x)^T \theta $$
- **Why is it "Linear"?** Even though $\phi(x)$ might transform the input $x$ into complex curves (like squares or sines), the math remains simple because the equation is **linear in the parameters $\theta$**. We are just summing up components.
- **The Solution:** Last week, we found the "Golden Rule" (the OLS estimator) that minimizes the squared error. If we collect all data into a matrix $\Phi$, the best parameter vector $\hat{\theta}$ is: $$ \hat{\theta} = (\Phi^T\Phi)^{-1}\Phi^T y $$

### 2. Introducing Polynomials

Now, let's make this concrete. A very powerful way to use feature maps is **Polynomial Regression**. Instead of using random features, we systematically use powers of $x$.

If we choose a degree $M$, our feature vector looks like this: $$ \phi(x) = [1, x, x^2, x^3, \dots, x^M] $$ This means our model tries to fit the data using a polynomial equation of degree $M$: $$ f_\theta(x) = \theta_0 + \theta_1 x + \theta_2 x^2 + \dots + \theta_M x^M $$

### 3. The "Perfect Fit" Trap

Here is a crucial observation from the text. Since we can choose the complexity $M$ (the degree), what happens if we pick a very high number?

- Imagine you have $n$ data points.
- If you set the degree **$M = n - 1$**, you have created a model with $n$ adjustable parameters (coefficients).
- Mathematically, a polynomial of degree $n-1$ can twist and turn enough to pass **exactly** through every single one of your $n$ points.

**The Result:** Your Training Error (Empirical Risk) becomes **Zero**. You have perfectly memorized the data. But... is this actually what we want?

---

# 3.2 Concept: Overfitting and Generalization

We just established that if we use a polynomial with a high enough degree ($M = n - 1$), we can hit every single data point perfectly. The training error becomes zero.

You might think: _"Great! Mission accomplished."_ But the sources tell us this is actually a failure. Here is why.

## 1. The Goal: Generalization

In Machine Learning, we do not care about the past; we care about the future.

- **Training Error:** How well we memorized the data we already have.
- **Generalization:** How well we make meaningful predictions on **future, unseen data points**.

If our model is too complex (like a polynomial with degree $M=9$ on just 10 data points), it doesn't just learn the trend; it learns the **noise**. It twists and turns wildly just to pass through every random fluctuation in the training set. This is called **Overfitting**: The predictor becomes "too tailored" to the specific training data and loses the ability to predict general trends.

## 2. The Complexity Trade-off

There is a fundamental relationship between the **Complexity of the Model** (e.g., degree $M$) and the **Error**:

1. **As Complexity Increases:** The **Training Error** always goes down (eventually hitting 0).
2. **As Complexity Increases:** The **Generalization Error** (Future Performance) initially goes down, finds a "sweet spot", and then shoots up again because of overfitting.

![[Pasted image 20260214201639.png]]
> **Visual Note:** In the provided Figure 1, the "sweet spot" for that specific dataset was around $M = 6$ or $7$. Anything higher, and the curve started oscillating wildly.

## 3. Solution A: Adding More Data

How do we stop this? The first solution is simple but expensive: **Get more data.** There is a "Rule of Thumb" in Machine Learning:

> _"More data points buy you the possibility of using more complex models."_

If you have a complex model (high $M$) but only a few points ($n=10$), you will overfit. But if you take that same complex model and give it massive amounts of data ($n=100$), the model is forced to smooth out. It can no longer "cheat" by wiggling through every point; it has to find the true underlying curve. So, increasing $n$ allows us to safely increase $M$ without losing generalization power.

---

# 3.2 (Continued) Concept: Regularization

We just learned that "Getting More Data" is the best cure for overfitting. But in the real world, data is expensive or simply unavailable. So, what if we are stuck with a small dataset ($n=10$) and a complex model ($M=9$)?

We use a technique called **Regularization**.

## 1. The Core Idea: Penalize Complexity

If "Overfitting" means the model is trying too hard to fit the noise by creating wild, large parameters (coefficients), then "Regularization" means punishing the model for doing exactly that.

We change the rules of the game. Instead of just minimizing the error, the model must minimize a combination of **Error + Complexity**.

### The New Optimization Goal

We introduce a modified risk function $\hat{R}_{reg}(\theta)$:

$$ \hat{R}_{reg}(\theta) = \underbrace{\frac{1}{2n} |y - \Phi\theta|_2^2}_{\text{Fit the Data}} + \underbrace{\lambda \Psi(\theta)}_{\text{Keep weights small}} $$

- **First Term:** The standard Empirical Risk (MSE). It pushes the model to fit the data perfectly.
- **Second Term ($\Psi(\theta)$):** A penalty term based on the size of the parameters $\theta$.
- **$\lambda$ (Lambda):** The "control knob." It decides how much we care about simplicity versus accuracy.

## 2. The Three Types of Regularizers

The source outlines three specific ways to define the penalty $\Psi(\theta)$:

### A. Ridge Regression ($L_2$ Regularization)

- **Formula:** $\Psi(\theta) = |\theta|_2^2 = \sum \theta_j^2$
- **What it does:** It shrinks all coefficients $\theta$ towards zero, but rarely makes them exactly zero.
- **Why use it?** It is mathematically friendly (**Convex** and **Differentiable**), meaning we can still find a unique, easy solution.

### B. Lasso Regression ($L_1$ Regularization)

- **Formula:** $\Psi(\theta) = |\theta|_1 = \sum |\theta_j|$
- **What it does:** It is very aggressive. It forces many coefficients to become **exactly zero**.
- **Why use it?** It performs automatic **Feature Selection**. If you have 100 features but only 5 matter, Lasso will kill the other 95 (set their weights to 0).

### C. Elastic Net

- **Formula:** A mix of both Ridge and Lasso.
- **Why use it?** It tries to get the best of both worlds (feature selection of Lasso + stability of Ridge).

## 3. The Hyperparameter $\lambda$

Setting the right $\lambda$ is crucial.

- **If $\lambda$ is too high:** You punish the model too much. It becomes scared to learn anything (Underfitting).
- **If $\lambda$ is too low:** You barely punish the model. It goes back to Overfitting.

---

# 3.3 The Price of Perfection: Computational Complexity

We have our "Golden Formula" for the optimal parameters $\hat{\theta}$: $$ \hat{\theta} = (\Phi^T\Phi)^{-1}\Phi^T y $$

This formula is perfect. It gives the exact solution. But as computer scientists, we need to ask: **Is it expensive to run?** To find out, we have to count the number of operations (additions and multiplications) the computer performs. We use **Big-O notation**, where $n$ is the number of data points and $d$ is the number of features.

## 1. Breaking Down the Costs

Let's dismantle the formula piece by piece:

1. **Building the Matrix ($\Phi^T\Phi$):** We need to multiply the Design Matrix by its transpose. The resulting matrix is size $d \times d$. To calculate just _one_ number in this grid, we have to sum up products over all $n$ data points.
    
    - **Cost:** $O(nd^2)$
    - _Translation:_ This is the most expensive part if you have a lot of data ($n$).
2. **Inverting the Matrix ($(\dots)^{-1}$):** Matrix inversion is computationally heavy (usually done via Gaussian Elimination).
    
    - **Cost:** $O(d^3)$
    - _Translation:_ This is the bottleneck if you have a lot of features ($d$). If $d=10,000$, $d^3$ is a trillion operations!
3. **The Rest ($\Phi^T y$ and final multiplication):** Calculating $\Phi^T y$ takes $O(nd)$, and the final multiplication takes $O(d^2)$.
    
    - _Translation:_ These are negligible compared to the first two steps.

## 2. The Final Bill (Proposition 3.1)

When we add it all up, the total complexity is: $$ \text{Total Time} = O(nd^2 + d^3) $$

### Why does this matter?

- **If $n$ is huge:** The $nd^2$ term kills us.
- **If $d$ is huge:** The $d^3$ term kills us.

## 3. The Hidden Danger (Remark 3.2)

There is another problem besides time. Inverting a matrix is not just slow; it can be **unstable**. If the matrix $\Phi^T\Phi$ is "ill-conditioned" (meaning some columns are very similar to others), the computer might make rounding errors that explode, giving us a completely wrong result.

**Conclusion:** The closed-form solution is great for small datasets. But for "Big Data" (massive $n$ or massive $d$), we need a cheaper, safer alternative.

---

# 3.4 Concept: Gradient Descent (The General Algorithm)
[[3.4 ML Details|Important Details]]

The "Closed Form" solution we studied before is like teleportation: you instantly calculate the coordinates of the peak of the mountain. **Gradient Descent** is like hiking: you start at a random spot, look at the slope under your feet, and take a step downhill. You repeat this until you reach the bottom.

## 1. The Algorithm

We want to minimize a function $F(\theta)$ (in our case, the Risk). The algorithm is surprisingly simple:

1. **Start:** Pick a random starting point $\theta_0$ (it doesn't matter where).
2. **Iterate:** For every time step $t = 1, 2, \dots$:
    - Calculate the **Gradient** $\nabla F(\theta_{t-1})$ at your current position. (This tells you the direction of the steepest ascent).
    - Take a step in the **opposite** direction.

### The Update Formula

$$ \theta_t = \theta_{t-1} - \gamma \nabla F(\theta_{t-1}) $$

- $\theta_{t-1}$: Where you are now.
- $\nabla F$: The direction of the "uphill" slope.
- $-$: We subtract because we want to go "downhill."
- **$\gamma$ (Gamma): The Learning Rate.** This is the size of your step.
    - If $\gamma$ is too small: You take tiny baby steps. It takes forever to reach the bottom.
    - If $\gamma$ is too big: You might overshoot the valley and bounce up the other side.

## 2. The Danger: Local Minima

Imagine a mountain range with many small valleys (local minima) and one huge, deep canyon (global minimum). If you are blindfolded and just walk downhill, you might get stuck in a small valley and think you are done, while the real bottom is miles away. Gradient Descent **cannot** distinguish between a local puddle and the ocean.

## 3. The Safety Net: Convexity

How do we ensure we don't get trapped? We make sure our function is **Convex**.

- **Definition:** A function is convex if it is shaped like a perfect bowl. If you draw a line between any two points on the curve, the curve always lies _below_ that line.
- **The Guarantee:** In a convex landscape, **every Local Minimum is also the Global Minimum.** If the slope is flat, you are definitely at the true bottom.

### How to check for Convexity? (The Hessian)

To know if a multidimensional function is a "bowl," we look at its **Hessian Matrix** $H$ (the matrix of second derivatives).

- If the Hessian is **Positive Semi-Definite** (meaning $v^T H v \geq 0$ for all vectors $v$), the function is convex.
- Intuitively, this means the function curves "upward" in every possible direction.

---

# 3.5 Gradient Descent for Linear Regression (The Setup)
[[3.5 ML Details|Important Details]]


We previously defined the general algorithm. Now, let's plug in our specific equations. Recall that our goal is to minimize the Empirical Risk (Mean Squared Error): $$ \hat{R}(\theta) = \frac{1}{2n} |y - \Phi\theta|_2^2 $$

## 1. The Gradient and The Hessian

To use Gradient Descent, we need to know the slope (Gradient) and the shape of the valley (Hessian). The sources give us the exact formulas:

- **The Gradient ($\nabla \hat{R}$):** $$ \nabla \hat{R}(\theta) = \frac{1}{n} (\Phi^T\Phi\theta - \Phi^T y) $$
    
    - _Note:_ This is simply the derivative of the squared error.
- **The Hessian ($H$):** $$ H = \nabla^2 \hat{R}(\theta) = \frac{1}{n} \Phi^T\Phi $$
    
    - _Note:_ This matrix represents the curvature of our error surface.

## 2. The Guarantee: Why it works (Proposition 4.4)

Before we start the algorithm, we need to be sure we won't get stuck in a fake local minimum. We need to prove our function is **Convex**. To do this, we look at the Hessian $H = \frac{1}{n} \Phi^T\Phi$.

**The Proof (Simplified):** A matrix is "Positive Semi-Definite" (which implies convexity) if, for any vector $v$, the quantity $v^T H v$ is never negative. Let's check our Hessian: $$ v^T H v = v^T (\frac{1}{n} \Phi^T\Phi) v = \frac{1}{n} (v^T \Phi^T) (\Phi v) = \frac{1}{n} |\Phi v|_2^2 $$ Since a squared norm ($|\dots|^2$) is **always positive or zero**, our Hessian is positive semi-definite.

**Conclusion:** The Error Surface of Linear Regression is a perfect bowl. Gradient Descent is mathematically guaranteed to find the Global Minimum (provided the step size is correct).

## 3. The Specific Algorithm

Now we can update our general loop. Instead of a generic $\nabla F$, we plug in our linear regression gradient:

1. **Start:** Pick any $\theta_0$.
2. **Update Rule:** $$ \theta_t = \theta_{t-1} - \gamma \frac{1}{n} (\Phi^T\Phi\theta_{t-1} - \Phi^T y) $$

This formula allows us to iteratively improve our weights $\theta$ without ever needing to invert a massive matrix!

---
# 3.5 (Continued) Convergence Analysis: The Speed Limit

We established that Gradient Descent _will_ eventually reach the bottom of the valley (the optimal $\hat{\theta}$). But how fast? It turns out the speed depends entirely on the **shape of the valley**.

## 1. The Condition Number ($\kappa$)

We define a special number called the **Condition Number** $\kappa$ (Kappa). $$ \kappa = \frac{L}{\mu} \geq 1 $$

- **$L$ (Lipschitz Constant):** The largest eigenvalue of the Hessian. This represents the "steepest" direction of the valley.
- **$\mu$ (Strong Convexity):** The smallest eigenvalue. This represents the "flattest" direction.

**The Physical Meaning:**

- If $\kappa$ is close to 1 ($L \approx \mu$), the valley is a perfect bowl (circular). You can walk straight to the center. **Convergence is fast.**
- If $\kappa$ is huge ($L \gg \mu$), the valley is a long, narrow ravine. You will bounce back and forth against the steep walls while slowly making progress along the flat bottom. **Convergence is slow.**

## 2. The Convergence Theorem (Theorem 4.5)

The source gives us precise bounds on how the error shrinks at every step $t$, assuming we use the optimal learning rate $\gamma = 1/L$.

**A. Getting closer to the true parameters:** $$ |\theta_t - \hat{\theta}|_2^2 \leq \left(1 - \frac{1}{\kappa}\right)^{2t} |\theta_0 - \hat{\theta}|_2^2 $$

- _Interpretation:_ At every step, we multiply our distance from the goal by a factor slightly less than 1. This is **Exponential Convergence** (or "Linear Convergence" in optimization terms). The larger $\kappa$ is, the closer this factor is to 1, and the slower we go.

**B. Reducing the Error (Risk):** $$ \hat{R}(\theta_t) - \hat{R}(\hat{\theta}) \leq \left(1 - \frac{1}{\kappa}\right)^{2t} (\hat{R}(\theta_0) - \hat{R}(\hat{\theta})) $$

- _Interpretation:_ The value of the loss function drops at the same rate.

## 3. How many steps do we need? (Corollary 4.6)

If we want our error to be smaller than a tiny number $\epsilon$ (epsilon), how many iterations $N$ must we run? The math says we need roughly: $$ N \approx \frac{\kappa}{2} \log\left(\frac{1}{\epsilon}\right) $$

- **Key Takeaway:** The time needed is proportional to the Condition Number $\kappa$. If your data is messy (bad $\kappa$), you pay the price in waiting time.

---

Here is the conclusion of Section 3.5.

We now have the final piece of the puzzle. We know the Closed Form solution costs $O(nd^2 + d^3)$, and we know Gradient Descent takes $N \approx \kappa \log(1/\epsilon)$ steps. Now, let's calculate the total cost of Gradient Descent and see when it is better than the Closed Form.

---

# 3.5 (Conclusion) Gradient Descent vs. Closed Form: The Final Verdict

How much time does Gradient Descent _actually_ take? It depends on how we implement the math inside the loop. According to the sources, we have two strategies:

### Strategy A: Pre-computing the Hessian

We calculate the matrix $\Phi^T\Phi$ once at the beginning (Cost: $O(nd^2)$). Then, every step of the loop is cheap ($O(d^2)$).

- **Total Time:** $O(nd^2 + d^2 \cdot \kappa \log(1/\epsilon))$
- **Verdict:** This is still expensive if the number of features $d$ is large, because of that initial $nd^2$ cost.

### Strategy B: Computing "From Scratch"

We do **not** pre-calculate the matrix. Instead, in every step, we compute the gradient directly from the raw data.
	
- **Cost per step:** $O(nd)$ (Scanning the data once).
- **Total Time:** $O(nd \cdot \kappa \log(1/\epsilon))$
- **Verdict:** This is the winner for high-dimensional data!
    - The Closed Form had a $d^3$ term (disaster for big $d$).
    - This approach uses $nd$, which is linear.

### Summary: When to use what?

1. **Use Closed Form (OLS):** If you have small data (small $n$, small $d$). It gives the exact answer instantly.
2. **Use Gradient Descent:** If you have **massive features** ($d$ is huge). It avoids the $d^3$ matrix inversion bottleneck.

**However, there is still a problem. Even Strategy B requires looking at all $n$ data points for every single step. If $n = 1,000,000,000$ (like Google or Facebook data), this is too slow. This leads us to the final topic of Week 3: Stochastic Gradient Descent (Section 3.6). 

---

# 3.6 Stochastic Gradient Descent (SGD)

## 1. The Bottleneck: "The Summation Problem"

Let's look closely at the cost function we are trying to minimize. It is almost always a sum of errors over individual data points: $$ L(\theta) = \sum_{i=1}^n l_i(\theta) $$ _(Where $l_i$ is the squared error for just the $i$-th person in our dataset)._

To take **one single step** in standard Gradient Descent, we have to calculate the derivative for **every single one** of these $n$ terms and sum them up.

- **Imagine:** You have a dataset of 1 billion images ($n=10^9$).
- **The Cost:** To move your parameters just one inch, you have to process 1 billion images. This is incredibly inefficient.

## 2. The Solution: The "Random Proxy"

Instead of calculating the exact gradient (the average opinion of 1 billion data points), we settle for a **random estimate**.

**The Algorithm (SGD):**

1. At every time step $t$, pick **one random index** $i_t$ from your dataset (uniformly at random).
2. Pretend that this one data point represents the entire dataset.
3. Calculate the gradient based **only** on this single point: $$ g(\theta_t) = \nabla l_{i_t}(\theta_t) $$
4. Update your weights: $$ \theta_t = \theta_{t-1} - \gamma \cdot g(\theta_t) $$

**The Cost:**

- **Standard GD:** $O(nd)$ per step.
- **SGD:** $O(d)$ per step. (It is $n$ times faster!)

## 3. Why does this work? (Unbiased Estimator)

You might think: _"If I just look at one random point, won't I move in the wrong direction?"_ Yes, sometimes you will. The path of SGD is noisy and "drunk-like." It zig-zags wildly.

However, the source gives us the mathematical guarantee: $$ \mathbb{E}[g(\theta_t)] = \nabla L(\theta) $$

- **Translation:** On average (in Expectation), the random gradient equals the true gradient.
- **Intuition:** Even if individual steps are wrong, the **average direction** over many steps leads you correctly to the bottom of the valley.

## 4. The Middle Ground: Minibatch SGD

- **Pure SGD (1 point):** Very fast, but very noisy (high variance). It might zig-zag too much.
- **Full GD (All points):** Very smooth path, but too slow.

The industry standard is **Minibatch SGD**: Instead of picking 1 point or all points, we pick a small "batch" (e.g., 32 or 64 points).

- **Benefit:** It reduces the variance (the estimate is more robust/stable than using just 1 point).
- **Benefit:** It is still much faster than using the full dataset.

---

**Conclusion of Week 3** We have successfully covered:

1. **Polynomial Regression:** How to fit curves using linear models.
2. **Overfitting:** Why models fail when they get too complex.
3. **Regularization:** How to fix overfitting (Ridge, Lasso).
4. **Gradient Descent:** How to find the solution without inverting massive matrices.
5. **SGD:** How to make it work on massive datasets.

