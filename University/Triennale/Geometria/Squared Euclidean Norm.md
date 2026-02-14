# Squared Euclidean Norm ($L_2^2$)

**Tags:** #math #linear_algebra #machine_learning #optimization

## 1. Definition

The **Squared Euclidean Norm** is a scalar value that represents the square of the standard Euclidean distance (length) of a vector from the origin.

In Machine Learning, it is the fundamental building block for **Least Squares**, **Ridge Regression**, and many Loss Functions.

### Mathematical Formulation

Given a vector $x \in \mathbb{R}^n$:

$$x = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}$$

The Squared Norm is defined as the inner product of the vector with itself:

$$\|x\|_2^2 = x^T x = \sum_{i=1}^{n} x_i^2$$

> [!abstract] Notation Breakdown
> 
> - **$\|\cdot\|_2$**: The standard Euclidean Norm (Length).
>     
> - **$\|\cdot\|_2^2$**: The **Squared** Length (removes the square root).
>     
> - **$x^T x$**: Matrix notation (Row vector $\times$ Column vector).
>     

---

## 2. Geometric Interpretation

While the standard norm $\|x\|_2$ represents the "physical" length of the arrow from the origin to the point $x$, the **Squared Norm** represents the **area of the square** that has that vector as its side.

- **Standard Norm:** $\|x\|_2 = \sqrt{x_1^2 + x_2^2}$ (Pythagoras)
    
- **Squared Norm:** $\|x\|_2^2 = x_1^2 + x_2^2$ (Pythagoras without the root)
    

---

## 3. Why is it used in Machine Learning?

We almost always use the squared norm $\|e\|_2^2$ instead of the standard norm $\|e\|_2$ for loss functions.

### Reason A: Convexity & Derivative Simplicity

The standard norm $\|x\|_2$ contains a square root function: $\sqrt{\sum x_i^2}$.

- **Problem:** The derivative of $\sqrt{z}$ is $\frac{1}{2\sqrt{z}}$. This becomes undefined (or unstable) when $z \approx 0$ (at the minimum).
    
- **Solution:** The squared norm removes the root. The function becomes a simple **Paraboloid** (Quadratic).
    
    - It is **strictly convex** (bowl shape).
        
    - Its derivative is linear and easy to compute.
        

### Reason B: Penalizing Large Errors

Squaring the error term $(y - \hat{y})^2$ disproportionately punishes **large outliers**.

- Error = 2 $\rightarrow$ Penalty = 4
    
- Error = 10 $\rightarrow$ Penalty = 100
    
    This forces the model to focus on fixing the "worst" predictions.
    

---

## 4. The Gradient (Crucial for Optimization)

In Gradient Descent, we need the derivative of the norm with respect to the vector $x$.

### The Identity

$$\nabla_x \|x\|_2^2 = \nabla_x (x^T x) = 2x$$

> [!tip] Exam/Derivation Focus
> 
> This specific derivative is why the gradient of the Mean Squared Error (MSE) is so clean.
> 
> If $f(\theta) = \|y - \Phi\theta\|_2^2$:
> 
> $$\nabla_\theta f(\theta) = -2\Phi^T(y - \Phi\theta)$$

---
