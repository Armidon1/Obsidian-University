# The Design Matrix ($\Phi$)

The **Design Matrix** (denoted as $\Phi$ or sometimes $X$) is the fundamental data structure in Linear Regression. It organizes all our observations and their corresponding features into a single grid, allowing us to use Linear Algebra to solve the optimization problem efficiently.

## 1. Definition and Structure

Given a dataset of $n$ samples and a feature map $\phi: \mathcal{X} \rightarrow \mathbb{R}^d$, the Design Matrix $\Phi$ is an **$n \times d$ matrix**.

It is constructed by stacking the transposed feature vectors of each data point on top of one another.

### General Structure

$$
\Phi = 
\begin{bmatrix} 
\phi_1(x_1) & \phi_2(x_1) & \dots & \phi_d(x_1) \\ 
\phi_1(x_2) & \phi_2(x_2) & \dots & \phi_d(x_2) \\ 
\vdots & \vdots & \ddots & \vdots \\ 
\phi_1(x_n) & \phi_2(x_n) & \dots & \phi_d(x_n) 
\end{bmatrix} 
= 
\begin{bmatrix} 
\text{---} & \phi(x_1)^T & \text{---} \\
\text{---} & \phi(x_2)^T & \text{---} \\
& \vdots & \\
\text{---} & \phi(x_n)^T & \text{---}
\end{bmatrix}
$$

- **Rows ($i=1 \dots n$):** Each row represents a single **data sample**.
- **Columns ($j=1 \dots d$):** Each column represents a specific **feature** across all samples.
- **Element $\Phi_{i,j}$:** The value of the $j$-th feature for the $i$-th sample.

---

## 2. Concrete Example: Polynomial Regression

Let's build a Design Matrix for a **Quadratic Regression** (fitting a parabola $y = \theta_0 + \theta_1 x + \theta_2 x^2$).

### The Setup

- **Dataset ($n=3$):** We have three data points: $x_1 = 2$, $x_2 = 5$, $x_3 = -1$.
- **Feature Map:** $\phi(x) = [1, x, x^2]^T$. (Note: We include $1$ for the intercept/bias).
- **Dimensions:** $n=3$ rows, $d=3$ columns.

### Building $\Phi$

We calculate the feature vector for each point:

1. **Point 1 ($x=2$):** $\phi(2) = [1, 2, 2^2] =$
2. **Point 2 ($x=5$):** $\phi(5) = [1, 5, 5^2] =$
3. **Point 3 ($x=-1$):** $\phi(-1) = [1, -1, (-1)^2] = [1, -1, 1]$

### The Resulting Matrix

$$ \Phi = \begin{bmatrix} 1 & 2 & 4 \ 1 & 5 & 25 \ 1 & -1 & 1 \end{bmatrix} $$

---

## 3. Why do we need it?

The Design Matrix allows us to rewrite the complex summation of errors into compact matrix operations.

1. **Compact Risk Formula:** Instead of $\sum (y_i - \phi(x_i)^T\theta)^2$, we write: $$ \hat{R}(\theta) = \frac{1}{n} |y - \Phi\theta|_2^2 $$
    
2. **The OLS Solution:** It is the key component of the closed-form solution for the optimal parameters $\hat{\theta}$: $$ \hat{theta} = (\Phi^T\Phi)^{-1}\Phi^T y $$
    
3. **Geometric Interpretation:** The columns of $\Phi$ span a subspace called $im(\Phi)$. The OLS estimator finds the orthogonal projection of the target vector $y$ onto this subspace.
    

---