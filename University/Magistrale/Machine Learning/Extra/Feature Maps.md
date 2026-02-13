# 2.2.1 Concept: Feature Maps ($\phi$)

**Feature Maps** are the bridge between raw, complex data and linear mathematical models. They allow us to apply Linear Regression to problems that are not linear in reality (like curved trajectories or periodic waves).

## 1. Definition

Given an input space $\mathcal{X}$ (which could be anything: numbers, vectors, images), we define $d$ functions called **Feature Maps**: $$ \phi_j : \mathcal{X} \rightarrow \mathbb{R} \quad \text{for } j=1, \dots, d $$

These maps transform a raw input $x$ into a vector of real numbers $\phi(x) \in \mathbb{R}^d$: $$ \phi(x) = \begin{bmatrix} \phi_1(x) \ \vdots \ \phi_d(x) \end{bmatrix} $$

## 2. The Prediction Function

We construct our model predictions as a **weighted sum** of these features. $$ f_\theta(x) = \sum_{j=1}^{d} \phi_j(x) \cdot \theta_j = \phi(x)^T \theta $$

### The "Linearity" Trick

This is the most important concept to grasp.

- The function $f_\theta(x)$ can be **non-linear** with respect to the input $x$ (e.g., if $\phi(x) = x^2$, the curve is a parabola).
- However, the function remains **linear** with respect to the parameters $\theta$.

> **Source Quote:** _"Note, this problem is still called linear regression because function $f_\theta(x)$ is not linear in $x$, but is linear in $\theta$!"_

This linearity in $\theta$ allows us to use Linear Algebra (matrix inversion) to solve the problem, regardless of how complex the features are.

#### So we introduced $\theta$ in a way to create another linear function in respect to $\theta$

You correctly identified that raw data is rarely linear. The power of Linear Regression lies in a specific definition: the model doesn't need to be a straight line in the real world ($x$), it only needs to be a "straight line" in the mathematical parameter space ($\theta$).

##### 1. The Problem: $x$ is not linear

In the real world, data is complex.

- **Example:** If you throw a ball, its height $y$ over time $x$ follows a parabola ($y = ax^2 + bx + c$).
- If you try to fit a straight line $y = mx + q$ directly to raw $x$, you will get a terrible error. The "Linear Assumption" on raw $x$ fails.

##### 2. The Solution: Feature Maps ($\phi$)

Instead of abandoning Linear Regression, we transform the input. We define a **Feature Map** $\phi(x)$. For the ball example (Polynomial Regression), we map the time $x$ to a vector: $$ \phi(x) = [1, x, x^2]^T $$

Now, our prediction function looks like this: $$ f_\theta(x) = \theta_0 \cdot 1 + \theta_1 \cdot x + \theta_2 \cdot x^2 $$

##### 3. The Crucial Distinction: Linear in $\theta$

Here is the core concept found in the sources:

> _"Note, this problem is still called linear regression because function $f_\theta(x)$ is not linear in $x$, but is linear in $\theta$!"_

- **Non-Linear in $x$:** If you plot $f(x)$ against $x$, you see a curve (a parabola).
- **Linear in $\theta$:** If you fix $x$, the equation is just a simple weighted sum: $\text{Value} = \theta_0 + \theta_1(\text{number}) + \theta_2(\text{number})$.

This allows us to keep using the **OLS Formula** $\hat{\theta} = (\Phi^T\Phi)^{-1}\Phi^T y$. The math "thinks" it is solving a linear problem, even if the result is a curve.

##### 4. Geometric View

- **In Input Space ($\mathcal{X}$):** The points lie on a curved manifold.
- **In Feature Space ($im(\Phi)$):** The points lie on a flat hyperplane (a subspace). We are finding the best projection onto this flat plane.

##### Summary

The "idea" is:

1. We acknowledge $x$ is complex.
2. We "hard-code" the complexity into $\phi(x)$ (e.g., we manually calculate squares or sines).
3. We use standard Linear Regression to find the best weights $\theta$ for these features.

---

## 3. The Design Matrix ($\Phi$)

When we have a dataset of $n$ points, we apply the feature maps to every single input $x_i$. We stack these vectors to create the **Design Matrix** $\Phi$ ($n \times d$).

$$ \Phi = \begin{bmatrix} — \phi(x_1)^T — \ \vdots \ — \phi(x_n)^T — \end{bmatrix} $$

- The element $\Phi_{i,j}$ corresponds to the $j$-th feature of the $i$-th data point.
- This matrix is the core component of the OLS formula: $\hat{\theta} = (\Phi^T\Phi)^{-1}\Phi^T y$.

---

## 4. Common Examples

We can choose different maps depending on the shape of the data:

|Type|Formula|Features $\phi(x)$|Use Case|
|:--|:--|:--|:--|
|**Standard 1-D**|$y = q + mx$|$[1, x]$|Simple straight trends.|
|**Polynomial**|$y = \theta_0 + \theta_1 x + \theta_2 x^2 \dots$|$[1, x, x^2, \dots, x^l]$|Curved data. ($l$-degree poly requires $l+1$ dims).|
|**Fourier**|$y = \theta_1 \sin(x) + \theta_2 \cos(x)$|$[\sin(2\pi x), \cos(2\pi x)]$|Periodic data (waves, seasons).|

## 5. Geometric Interpretation

Under the **Linear Assumption** ($Y = \phi(X)^T \theta^* + \epsilon$), the "true" relationship is a curve in the original space $\mathcal{X}$. However, if we visualize the data in the **Feature Space** (the $d$-dimensional space defined by $\phi$), the points lie on a flat hyperplane (linear subspace).

- **Input Space:** Data might look like a parabola.
- **Feature Space:** Data looks like a flat plane.

---