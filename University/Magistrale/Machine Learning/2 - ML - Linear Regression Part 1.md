# Week 2: Linear Regression

This week focuses on the fundamental "Hello World" algorithm of Machine Learning: **Linear Regression**. While the concept of fitting a line to data might seem simple, the mathematical framework we build here—involving loss functions, optimization, and statistical guarantees—forms the foundation for almost all advanced learning models.

## The Core Problem

We are placed in a **Supervised Learning** setting. We are given a dataset containing $n$ pairs of inputs and outputs: $$ S = {(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)} $$

- **$x_i$ (Input):** The features or data points (e.g., square footage of a house).
- **$y_i$ (Target):** The real-valued label we want to predict (e.g., the price of the house).

## The Goal

Our objective is to find a function $f_\theta(x)$ that best explains the relationship between inputs and outputs. specifically, we look for a linear relationship (or a relationship linear in parameters) that minimizes the discrepancy between our predictions and reality.

## The Roadmap

To fully understand Linear Regression, we will attack the problem from three different angles:

1. **Optimization View:** We define a cost function (Mean Squared Error) and use calculus to find the parameters that minimize it.
2. **Geometric View:** We visualize the data as vectors in space and understand regression as finding the "shadow" (projection) of the target vector onto the feature space.
3. **Statistical View:** We assume a probabilistic model (the "Linear Assumption") to calculate how well our model generalizes to new, unseen data (Risk, Bias, and Variance).

---

Puoi inserire questo blocco all'inizio della tua nota su Obsidian, subito prima della sezione **2.1 Warm-Up**.

## 2.1 Warm-Up: Linear Regression in 1-Dimension

To understand linear regression, we start with the simplest possible scenario: working with data in a single dimension. Imagine you are given a dataset containing $n$ pairs of numbers: $$ (x_1, y_1), (x_2, y_2), \dots, (x_n, y_n) $$Remember: this is our Set of data, but we do not have full control of the Distribution **D**, that's why we won't work with the [[Expected Risk|Expected Risk]] but with the [[Empirical Risk]].
Your goal is to find a relationship between the inputs ($x$) and the outputs ($y$). specifically, we want to find the best straight line defined by the equation $y = mx + q$ that fits this data.

### Defining "Best Fit": The Empirical Mean Square Error

How do we mathematically define what the "best" line is? We define it as the line that minimizes the error between what the line predicts and the actual data points. We use the **[[Empirical Mean]] Square Error (MSE)**, which measures the average of the squared differences between the true value $y_i$ and the predicted value $(mx_i + q)$.

The cost function (or risk function) $\hat{R}$ depends on our two parameters, the slope $m$ and the intercept $q$: $$ \hat{R}(m, q) = \frac{1}{n} \sum_{i=1}^{n} (mx_i + q - y_i)^2 $$
Note that, in compare to the Expected Risk, it is a a simply mean of the loss function, which in this scenario is a quadratic loss, while the Expected Risk is a weighted mean. 

But why aren't we using the Expected Risk and we had to define the Empirical Risk? See [[The Empirical vs Expected Dilemma ML|here]], but in general because we do not have actually a complete control over the distribution $D$ but we have only a Set of labelled $x_i$ of n-elements.

This function is a polynomial in terms of $m$ and $q$. Crucially, it is a convex function (imagine a 3D bowl shape), and as $m$ and $q$ grow very large, the error grows to infinity. This guarantees that the minimum error exists and can be found exactly where the gradient (the slope of the error bowl) is zero. 

>[!Abstract] Visual Analysis
>![[Pasted image 20260213124625.png]]
>
>**NOTE.** that's an example of bowl shape

**Basically:** It is possible to calculate the gradient, so calculate the partials derivates to slope and interception, and equal them to 0 to find the critical point, which, because of the fact that the Empirical Risk is a convex function, for sure is the minimum point. See [[Convexity and Optimization ML|here]] why
### Step 1: Finding the Intercept ($q$)

To find the minimum, we take the partial derivatives of the cost function and set them to zero. Let's start with the intercept $q$.

$$ \frac{\partial \hat{R}}{\partial q} = \frac{2}{n} \sum_{i=1}^{n} (mx_i + q - y_i) = 0 $$

We can simplify this equation to solve for $q$.

1. **Partiamo dalla derivata posta a zero:** $$ \frac{2}{n} \sum_{i=1}^{n} (mx_i + q - y_i) = 0 $$
    
2. **Eliminiamo la costante:** Possiamo dividere tutto per $\frac{2}{n}$ (che è diverso da zero), quindi ci rimane solo la sommatoria: $$ \sum_{i=1}^{n} (mx_i + q - y_i) = 0 $$
    
3. **Spezziamo la sommatoria:** Per la proprietà lineare delle sommatorie, possiamo trattare i termini separatamente: $$ \sum_{i=1}^{n} mx_i + \sum_{i=1}^{n} q - \sum_{i=1}^{n} y_i = 0 $$
    
4. **Il trucco della costante (Qui è la chiave!):** Il termine $q$ è una **costante** (non dipende dall'indice $i$). Sommare una costante $q$ per $n$ volte (da $i=1$ a $n$) equivale semplicemente a moltiplicare $q$ per $n$: $$ \sum_{i=1}^{n} q = n \cdot q $$
    
5. **Riscriviamo l'equazione:** $$ m \sum_{i=1}^{n} x_i + n \cdot q - \sum_{i=1}^{n} y_i = 0 $$
    
6. **Isoliamo la q:** Portiamo $n \cdot q$ da una parte e tutto il resto dall'altra: $$ n \cdot q = \sum_{i=1}^{n} y_i - m \sum_{i=1}^{n} x_i $$
    
7. **Dividiamo per n:** Adesso dividiamo tutto per $n$ per ottenere $q$ pulita: $$ q = \frac{1}{n} \sum_{i=1}^{n} y_i - m \frac{1}{n} \sum_{i=1}^{n} x_i $$
    
8. **Risultato finale:** Dato che $\frac{1}{n} \sum y_i$ è la media $\bar{y}$ e $\frac{1}{n} \sum x_i$ è la media $\bar{x}$, otteniamo: $$ q = \bar{y} - m\bar{x} $$
    

This equation tells us that the optimal line **must pass through the center of mass** of the data points $(\bar{x}, \bar{y})$.

### Step 2: Finding the Slope ($m$)

Now that we have an expression for $q$, we turn our attention to the slope $m$. We calculate the derivative of the cost function with respect to $m$ and set it to zero:

$$ \frac{\partial \hat{R}}{\partial m} = \frac{2}{n} \sum_{i=1}^{n} x_i(mx_i + q - y_i) = 0 $$

#### Step-by-Step Derivation: Isolating $m$

1. **Partiamo dalla derivata posta a zero:** Abbiamo calcolato la derivata rispetto a $m$ e rimosso la costante $\frac{2}{n}$. $$ \sum_{i=1}^{n} x_i(mx_i + q - y_i) = 0 $$
    
2. **Sostituzione di $q$:** Sappiamo dal passaggio precedente che $q = \bar{y} - m\bar{x}$. Sostituiamo questa espressione al posto di $q$ nell'equazione: $$ \sum_{i=1}^{n} x_i(mx_i + (\bar{y} - m\bar{x}) - y_i) = 0 $$
    
3. **Raggruppamento dei termini:** All'interno della parentesi, raggruppiamo i termini che contengono $m$ e quelli che non lo contengono.
    
    - Termini con $m$: $mx_i - m\bar{x} = m(x_i - \bar{x})$
    - Termini senza $m$: $\bar{y} - y_i = -(y_i - \bar{y})$
    
    Riscriviamo la sommatoria con questi raggruppamenti: $$ \sum_{i=1}^{n} x_i [ m(x_i - \bar{x}) - (y_i - \bar{y}) ] = 0 $$
    
4. **Distribuzione della sommatoria:** Ora moltiplichiamo $x_i$ per i termini dentro la parentesi quadra e spezziamo la sommatoria in due parti (proprietà lineare): $$ \sum_{i=1}^{n} m x_i(x_i - \bar{x}) - \sum_{i=1}^{n} x_i(y_i - \bar{y}) = 0 $$
    
5. **Isolamento di $m$:** Portiamo la sommatoria che **non** contiene $m$ (quella con le $y$) dall'altra parte dell'uguale: $$ m \sum_{i=1}^{n} x_i(x_i - \bar{x}) = \sum_{i=1}^{n} x_i(y_i - \bar{y}) $$
    
6. **Risultato finale:** Per trovare $m$, dividiamo tutto per il termine che moltiplica $m$ (la sommatoria delle $x$): $$ m = \frac{\sum_{i=1}^{n} x_i(y_i - \bar{y})}{\sum_{i=1}^{n} x_i(x_i - \bar{x})} $$
    

While this formula is mathematically correct, it is not the standard form you usually see. We can "massage" the numerator and denominator to make them cleaner and more interpretable (relating them to covariance and variance).

### Step 3: Deriving the Classical Formula (Detailed)

We currently have this expression for the slope $m$: $$ m = \frac{\sum_{i=1}^{n} x_i(y_i - \bar{y})}{\sum_{i=1}^{n} x_i(x_i - \bar{x})} $$

To get to the standard statistical form (Covariance over Variance), we need to transform both the numerator and the denominator. We use a fundamental property of the mean ("medio" in italiano): **The sum of deviations from the mean is always zero.** $$ \sum_{i=1}^{n} (x_i - \bar{x}) = 0 \quad \text{and} \quad \sum_{i=1}^{n} (y_i - \bar{y}) = 0 $$

#### 1. Massaging the Numerator

We want to transform $\sum x_i(y_i - \bar{y})$ into $\sum (x_i - \bar{x})(y_i - \bar{y})$.

**The Trick:** Since $\sum (y_i - \bar{y}) = 0$, we can multiply this sum by _any_ constant and it will still be zero. Let's multiply it by the constant $\bar{x}$. $$ \text{Zero Term} = \bar{x} \sum_{i=1}^{n} (y_i - \bar{y}) = 0 $$

Now, we calculate the numerator by **subtracting this Zero Term** from our original expression (subtracting zero doesn't change the value):

$$ \text{Numerator} = \sum_{i=1}^{n} x_i(y_i - \bar{y}) - \underbrace{\bar{x} \sum_{i=1}^{n} (y_i - \bar{y})}_{\text{This is 0}} $$

Now we can merge the two summations into one: $$ = \sum_{i=1}^{n} [ x_i(y_i - \bar{y}) - \bar{x}(y_i - \bar{y}) ] $$

Notice that $(y_i - \bar{y})$ is a common factor. We can factor it out: $$ = \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) $$

#### 2. Massaging the Denominator

We apply the exact same logic to the denominator $\sum x_i(x_i - \bar{x})$.

**The Trick:** We know that $\sum (x_i - \bar{x}) = 0$. Let's multiply this by the constant $\bar{x}$. $$ \text{Zero Term} = \bar{x} \sum_{i=1}^{n} (x_i - \bar{x}) = 0 $$

We subtract this Zero Term from the original denominator: $$ \text{Denominator} = \sum_{i=1}^{n} x_i(x_i - \bar{x}) - \underbrace{\bar{x} \sum_{i=1}^{n} (x_i - \bar{x})}_{\text{This is 0}} $$

Merge the summations: $$ = \sum_{i=1}^{n} [ x_i(x_i - \bar{x}) - \bar{x}(x_i - \bar{x}) ] $$

Factor out the common term $(x_i - \bar{x})$: $$ = \sum_{i=1}^{n} (x_i - \bar{x})(x_i - \bar{x}) = \sum_{i=1}^{n} (x_i - \bar{x})^2 $$

#### 3. The Final Result

By substituting these new forms back into our fraction, we get the classical OLS estimator formula:

$$ \hat{m} = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2} $$

- **Numerator:** This is proportional to the **Covariance** between $x$ and $y$.
- **Denominator:** This is proportional to the **Variance** of $x$.

In plain English: the optimal slope $\hat{m}$ is the ratio of the [[Covariance]] between $x$ and $y$ to the [[Variance]] of $x$.

---

## 2.2 The Linear Regression Framework

In the previous section, we looked at the 1-dimensional case, finding the best line to fit a set of points. While useful, real-world problems are rarely that simple. We need to generalize this approach in two key directions:

1. **Higher Dimensions:** Handling inputs that are vectors, not just single numbers (e.g., predicting house prices based on size, location, and age, not just size).
2. **Complex Functions:** Fitting curves that are not straight lines (like polynomials or waves), while keeping the mathematics simple.

We assume we have $n$ data points $(x_1, y_1), \dots, (x_n, y_n)$. Here, the input $x_i$ belongs to some abstract space $\mathcal{X}$, while the output $y_i$ is a real number.

### Feature Maps and the Prediction Function

To bridge the gap between complex inputs and linear models, we introduce the concept of **[[Feature Maps]]**. We define $d$ different functions $\phi_j : \mathcal{X} \rightarrow \mathbb{R}$. These maps transform our raw input $x$ into a vector of features.

Our prediction function $f_\theta(x)$ is defined as a weighted sum of these features: $$ f_\theta(x) = \sum_{j=1}^{d} \phi_j(x) \cdot \theta_j = \phi(x)^T \theta $$ Here, $\theta$ is a vector of parameters (weights) that we want to learn. $\phi(x)$ is a vector where the $j$-th entry is the result of the feature map $\phi_j(x)$. 

#### But what actually is the $\phi(x)$? 

The function $\phi$ (Phi) acts as a **translator** or an **expander**. Its job is to take your raw input $x$ (which might be simple) and transform it into a richer set of features that the Linear Regression algorithm can actually use to model complex curves.
Linear Regression, by itself, is "stupid": it can only draw straight lines. It cannot draw curves. The $\phi$ function solves this by pre-calculating the curves for the model.

- **Imagine this:** You have data that looks like a parabola (a U-shape). You want to fit it, but your model only knows how to do $y = \theta \cdot x$.
- **What $\phi$ does:** You define $\phi(x) = [x, x^2]$.
- **The Result:** If your input is $x=3$:
    1. $\phi$ calculates $3^2 = 9$.
    2. It creates a vector $\phi=[3,9]$.
    3. The model now sees two simple numbers: 3 and 9. It finds a weight ($\theta_1$) for the 3 and a weight ($\theta_2$) for the 9.
    4. Mathematically, it thinks it's doing a linear sum: $\theta_1(3) + \theta_2(9)$.
    5. Visually, it creates a curve: $\theta_1 x + \theta_2 x^2$.

so basically It changes the "Space"

- **In the $x$ space:** The relationship is a curve.
- **In the $\phi(x)$ space:** The relationship is a flat plane (subspace).

$\phi$ maps the data from a space where it is hard to model (curved) to a higher-dimensional space where it is easy to model (linear/flat).

##### 3. Concrete Examples (from Source)

The sources give specific examples of what $\phi$ calculates depending on what you need:

- **Polynomial Regression:** If you think the data curves like a polynomial, $\phi$ calculates powers: $$ \phi(x) = [1, x, x^2, x^3, \dots] $$
- **Fourier Regression:** If you think the data repeats (like a wave or seasonal sales), $\phi$ calculates sines and cosines: $$ \phi(x) = [\sin(x), \cos(x)] $$

##### Summary

The $\phi$ function allows you to say: _"I know the relationship isn't a straight line. I will manually calculate the squared terms (or sines, or logs) myself using $\phi$, so the Linear Regression algorithm can just find the weights for them."_

It keeps the math **linear in the parameters** ($\theta$), even though the result is **non-linear in the input** ($x$).

**Crucial Concept:** Why is this still called _Linear_ Regression? You might notice that the feature maps $\phi(x)$ can be non-linear (like $x^2$ or $\sin(x)$). However, the function $f_\theta(x)$ is **linear in the parameters $\theta$**. This linearity in $\theta$ is what allows us to use linear algebra to solve the problem efficiently, regardless of how complex the features are.

### The Optimization Problem (Matrix Notation)

Our goal remains the same: find the parameter vector $\theta \in \mathbb{R}^d$ that minimizes the Mean Squared Error (MSE). $$ \hat{R}(\theta) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \phi(x_i)^T \theta)^2 $$

To make the math cleaner and easier to implement, we switch to **Matrix Notation**.

1. Let $y$ be the column vector containing all target values $y_1, \dots, y_n$.
2. Let $\Phi$ be the $n \times d$ matrix (often called the [[Design Matrix]], note the n possible elements of the data set and the d dimensions of the feature vector.). We create this by stacking the feature vectors of all our data points. The element at row $i$ and column $j$ is simply the $j$-th feature of the $i$-th data point: $\Phi_{i,j} = \phi_j(x_i)$.

Using this notation, the sum of squared errors becomes the [[Squared Euclidean Norm]] of a vector difference: $$ \hat{R}(\theta) = \frac{1}{n} |y - \Phi\theta|_2^2 $$ This compact formula says: "Calculate the vector of predictions $\Phi\theta$, subtract it from the true vector $y$, find the length (norm) of the resulting error vector, and square it."

### Examples of Flexibility

The power of this framework lies in how we define $\phi(x)$:

- **1-D Linear Regression:** If we set $\phi_1(x) = 1$ and $\phi_2(x) = x$, we recover the simple line equation $y = \theta_1 + \theta_2 x$ (where $\theta_1$ is the intercept $q$ and $\theta_2$ is the slope $m$).
- **Polynomial Regression:** If we want to fit a curve, we can use powers of $x$ as features: $1, x, x^2, \dots, x^l$. The model learns the best polynomial, but the math remains linear in $\theta$.
- **Fourier Regression:** If the data looks periodic (like sound waves or seasonal trends), we can use sines and cosines as features: $\sin(2\pi x)$ and $\cos(2\pi x)$.

---

## 2.3 The Ordinary Least Squares (OLS) Estimator

We have defined our goal: to minimize the Mean Squared Error $\hat{R}(\theta)$. Now, we arrive at the most significant result of this week: the explicit formula that gives us the optimal parameters. This solution is known as the **Ordinary Least Squares (OLS) Estimator**.

### Theorem 2.4: The Formula

If we have a dataset of $n$ points and $d$ features, and assuming the matrix $\Phi^T\Phi$ is invertible, there is a unique solution that minimizes the error. It is given by this famous equation:

$$ \hat{\theta} = (\Phi^T\Phi)^{-1}\Phi^T y $$

At first glance, this might look intimidating. But let's break down what it represents. It tells us that to find the best weights $\hat{\theta}$, we take our feature matrix $\Phi$, multiply it by its transpose, invert the result, and then multiply by the transpose of the features and the target values $y$.

### The Proof: Minimizing the Cost Function

How do we prove this is the solution? We treat the cost function $\hat{R}(\theta)$ exactly like a function in calculus. Since it is a convex function (shaped like a bowl) and "coercive" (it goes to infinity as the parameters grow), we know it has a global minimum. To find it, we simply need to find the point where the gradient (the slope) is zero.

**Step 1: Expanding the Squared Norm** First, we rewrite the cost function using linear algebra properties. Remember that the squared norm of a vector $|v|^2$ is the same as the dot product with itself $v^T v$. $$ \hat{R}(\theta) = \frac{1}{n} (y - \Phi\theta)^T (y - \Phi\theta) $$

We expand this multiplication term by term, similar to how you expand $(a-b)^2 = a^2 - 2ab + b^2$, but with matrices: $$ \hat{R}(\theta) = \frac{1}{n} (y^Ty - (\Phi\theta)^T y - y^T\Phi\theta + (\Phi\theta)^T \Phi\theta) $$

**Step 2: The "Scalar Trick"** Here is a subtle but important simplification. Look at the term $(\Phi\theta)^T y$. The result of this multiplication is a single number (a scalar). In linear algebra, the transpose of a scalar is the scalar itself ($k^T = k$). Therefore, we can transpose this term: $$ ((\Phi\theta)^T y)^T = y^T (\Phi\theta) $$ This shows that the two middle terms in our expansion are actually identical. We can combine them: $$ \hat{R}(\theta) = \frac{1}{n} (|y|^2 - 2\theta^T \Phi^T y + \theta^T \Phi^T \Phi \theta) $$

**Step 3: Computing the Gradient** Now we take the derivative (gradient) with respect to $\theta$. We apply rules of matrix calculus:

1. The term $|y|^2$ is constant with respect to $\theta$, so its derivative is 0.
2. The term $-2\theta^T \Phi^T y$ is linear in $\theta$. Its derivative is the coefficient vector: $-2\Phi^T y$.
3. The term $\theta^T (\Phi^T \Phi) \theta$ is quadratic (like $ax^2$). Its derivative is $2(\Phi^T \Phi)\theta$.

Putting it all together, the gradient is: $$ \nabla \hat{R}(\theta) = \frac{2}{n} (\Phi^T\Phi\theta - \Phi^T y) $$

**Step 4: The Normal Equation** To find the minimum, we set the gradient to zero: $$ \frac{2}{n} (\Phi^T\Phi\theta - \Phi^T y) = 0 $$ We can ignore the constant $\frac{2}{n}$ and move the negative term to the other side. This leaves us with the **Normal Equation**: $$ \Phi^T\Phi\theta = \Phi^T y $$

Finally, to isolate $\theta$, we multiply both sides by the inverse of the matrix $(\Phi^T\Phi)^{-1}$. This yields our theorem's formula: $$ \hat{\theta} = (\Phi^T\Phi)^{-1}\Phi^T y $$

### A Note on Invertibility

For this solution to exist, the matrix $\Phi^T\Phi$ must be [[Invertible Matrix]]. A necessary condition for this is that $d \le n$. In simple terms, we must have **at least as many data points as we have features**. If we have more features than data points ($d > n$), the system is underdetermined, and there isn't a single unique solution.


---

## 2.4 A Geometric Interpretation

The algebraic formula for the [[OLS estimator]], $\hat{\theta} = (\Phi^T\Phi)^{-1}\Phi^T y$, is correct, but it doesn't give us much intuition about _what_ is actually happening. To understand the mechanism deeply, we turn to geometry.

### The Setup: Subspaces and Projections

Imagine the space $\mathbb{R}^n$ where our target vector $y$ lives. Our feature matrix $\Phi$ has columns that represent our input variables. These columns span a specific "flat" region inside the larger space $\mathbb{R}^n$. We call this region the **image of $\Phi$**, denoted as $im(\Phi)$.

- **Key Insight:** Any prediction our model makes ($\hat{y} = \Phi\theta$) _must_ lie somewhere on this specific plane (subspace).

However, the real target vector $y$ (the actual data) almost never lies perfectly on this plane because of noise and errors. It "floats" somewhere above or below it. Our goal is to find the point on the plane that is **closest** to $y$. Geometrically, the shortest distance from a point to a plane is the straight line perpendicular (orthogonal) to that plane.

### Proposition 2.5: OLS as Orthogonal Projection

The math confirms our geometric intuition. The OLS estimator creates a **Projection Matrix** $P$: $$ P = \Phi(\Phi^T\Phi)^{-1}\Phi^T $$ This matrix $P$ acts like a light source that casts the shadow of $y$ directly onto the feature plane.

**Proof (How the matrix works):** We verify this by checking how $P$ treats different types of vectors:

1. **Vectors already on the plane:** If a vector $v$ is already in the feature space (meaning $v = \Phi\lambda$), multiplying it by $P$ leaves it unchanged ($Pv = v$). The matrix knows it's already "perfect."
2. **Vectors perpendicular to the plane:** If a vector $v$ is orthogonal to the features (it represents pure noise or error that our model can't capture), multiplying it by $P$ destroys it ($Pv = 0$).
3. **General Case:** Any vector $y$ can be split into a relevant part ($y_{\parallel}$) and a noise part ($y_{\perp}$). The matrix $P$ keeps the relevant part and discards the noise: $$ Py = P(y_{\parallel} + y_{\perp}) = y_{\parallel} + 0 = \hat{y} $$

### The Two-Step Process

So, what is the OLS algorithm actually doing? It performs two distinct geometric steps:

1. **Project:** It first projects the target $y$ onto the feature subspace to find the "perfect prediction" vector $\hat{y}$. $$ \hat{y} = Py = \Phi(\Phi^T\Phi)^{-1}\Phi^T y $$ Geometrically, the error vector ($y - \hat{y}$) is now perpendicular to the feature space. This guarantees that the squared error length is minimized.
2. **Coordinate:** Once we have this ideal prediction $\hat{y}$, we find the **coordinates** $\hat{\theta}$ needed to reconstruct it using our features (the columns of $\Phi$). $$ \Phi\hat{\theta} = \hat{y} $$ Solving this gives us the familiar formula $\hat{\theta} = (\Phi^T\Phi)^{-1}\Phi^T y$.

---

## 2.5 The Linear Assumption and Linear Regression

Up to this point, we have treated linear regression as a geometric problem: simply fitting a curve to data points to minimize error. Now, we shift to a **statistical perspective**. We introduce a formal model to describe how the data is generated in the real world. This allows us to use Decision Theory (from Week 1) to assess how good our predictor really is.

### Definition 3.1: The Linear Assumption

We assume that there is a "Ground Truth" behind our data. specifically, we say that a data distribution respects the **Linear Assumption** if the output $Y$ is generated by a specific formula involving the input $X$ and some random noise. We assume there exists a **true, unknown parameter vector** $\theta^*$ such that:

$$ Y = \phi(X)^T \theta^* + \epsilon $$

Here is what this equation tells us about the world:

1. **Deterministic Part ($\phi(X)^T \theta^*$):** The output is largely determined by the features of the input combined with the "true" weights $\theta^*$.
2. **Random Part ($\epsilon$):** There is always some noise $\epsilon$ (epsilon) that we cannot predict. This noise is **independent** of the input $X$.
    - It is **unbiased**: $\mathbb{E}[\epsilon] = 0$ (on average, the noise is zero, it doesn't systematically skew results).
    - It has a fixed **variance**: $\mathbb{E}[\epsilon^2] = \sigma^2$ (this represents the "loudness" or scale of the noise).

**Geometric Implication:** If the variance $\sigma^2$ were zero, every single data point would lie perfectly on the curve defined by $\theta^*$. Because $\sigma^2 > 0$, the points are scattered around this "true" curve.

### Proposition 3.2: The Optimal Predictor

Now that we have a model of reality, we can ask: "What is the mathematically best predictor $f^*(x)$?" From Week 1, we know that to minimize the squared error, the best predictor is always the **conditional expectation** $\mathbb{E}[Y | X=x]$.

Under our new Linear Assumption, this optimal predictor takes a very specific form: $$ f^*(x) = \phi(x)^T \theta^* $$

**Proof (Why is this true?):** Let's calculate the conditional expectation explicitly. We want to know the expected value of $Y$ given a specific input $x$. Since we assume $Y = \phi(x)^T \theta^* + \epsilon$, we substitute this into the expectation:

$$ \mathbb{E}[Y | X=x] = \mathbb{E}[\phi(x)^T \theta^* + \epsilon | X=x] $$

We can split this into two parts:

1. The term $\phi(x)^T \theta^*$ is constant (deterministic) for a fixed $x$, so it comes out of the expectation unchanged.
2. The term $\mathbb{E}[\epsilon | X=x]$ becomes simply $\mathbb{E}[\epsilon]$ because the noise is independent of $X$. Since we defined the noise as having a mean of zero, this term vanishes.

$$ = \phi(x)^T \theta^* + 0 = \phi(x)^T \theta^* $$

**The Takeaway:** This proposition tells us something crucial: If we lived in a perfect world and knew the true parameters $\theta^*$, we would have the optimal model. However, **we do not know $\theta^*$**. Therefore, our goal in Machine Learning is to use our data to find an estimate $\hat{\theta}$ that is as close as possible to the true $\theta^*$.

---

## 2.6 Estimating $\theta^*$ (Bias and Variance)

Now that we have assumed a "true" model exists ($Y = \Phi\theta^* + \epsilon$), we need to evaluate how well our OLS estimator $\hat{\theta}$ performs in recovering this truth. We assess this using two key statistical properties: **Bias** (are we right on average?) and **Variance** (how much does our estimate jump around?).

### 1. Unbiasedness: Are we accurate on average?

The first question is: If we could repeat this experiment infinite times—collecting new data with new random noise each time—would the _average_ of our estimated $\hat{\theta}$ values match the true $\theta^*$?

**Theorem 3.3:** The OLS estimator is **unbiased**. Mathematically, this means: $$ \mathbb{E}[\hat{\theta}] = \theta^* $$

**Proof (The Logic):** Let's substitute our definition of the true process ($Y = \Phi\theta^* + \epsilon$) into our formula for the estimator: $$ \hat{\theta} = (\Phi^T\Phi)^{-1}\Phi^T Y $$ $$ \hat{\theta} = (\Phi^T\Phi)^{-1}\Phi^T (\Phi\theta^* + \epsilon) $$

We distribute the terms. Notice what happens to the first part: $(\Phi^T\Phi)^{-1}\Phi^T \Phi$ cancels out to become the Identity matrix $I$. $$ \hat{\theta} = I\theta^* + (\Phi^T\Phi)^{-1}\Phi^T \epsilon $$ $$ \hat{\theta} = \theta^* + (\Phi^T\Phi)^{-1}\Phi^T \epsilon $$

This equation is profound (profondo). It says our estimate $\hat{\theta}$ is equal to the **truth** $\theta^*$ plus some **linear transformation of the noise** $\epsilon$. When we take the expectation (average) of both sides, the deterministic part $\theta^*$ stays the same. The noise part depends on $\mathbb{E}[\epsilon]$. Since we assumed the noise has a mean of zero, that entire second term vanishes. $$ \mathbb{E}[\hat{\theta}] = \theta^* + 0 = \theta^* $$

### 2. Covariance: How precise is our estimate?

Even if we are right "on average," any single experiment might be far off due to bad luck with the noise. We measure this uncertainty with the **Covariance Matrix**.

**Theorem 3.4:** The covariance of the estimator is determined by the noise level and the geometry of the data. $$ \mathbb{V}[\hat{\theta}] = \sigma^2 (\Phi^T\Phi)^{-1} $$

**Proof (The Logic):** We start from the equation we derived above: $\hat{\theta} = \theta^* + (\Phi^T\Phi)^{-1}\Phi^T \epsilon$. The variance of a constant ($\theta^*$) is zero, so the variance of our estimator comes entirely from the noise term: $$ \mathbb{V}[\hat{\theta}] = \mathbb{V}[ (\Phi^T\Phi)^{-1}\Phi^T \epsilon ] $$

In matrix algebra, when you pull a matrix $A$ out of a variance operator, it comes out as $A \mathbb{V} A^T$. Here, let $A = (\Phi^T\Phi)^{-1}\Phi^T$. $$ \mathbb{V}[\hat{\theta}] = A \mathbb{V}[\epsilon] A^T $$

We know $\mathbb{V}[\epsilon] = \sigma^2 I$ (from our assumptions). So: $$ \mathbb{V}[\hat{\theta}] = \sigma^2 A A^T $$ $$ = \sigma^2 [(\Phi^T\Phi)^{-1}\Phi^T] [(\Phi^T\Phi)^{-1}\Phi^T]^T $$ $$ = \sigma^2 (\Phi^T\Phi)^{-1}\Phi^T \Phi (\Phi^T\Phi)^{-1} $$ Notice that $\Phi^T \Phi$ in the middle cancels with one of the inverses. We are left with exactly: $$ \sigma^2 (\Phi^T\Phi)^{-1} $$

### Interpretation: How to reduce error?

This formula gives us the recipe for a better model. To reduce the variance (uncertainty) of our estimate, we have two levers:

1. **Reduce Noise ($\sigma^2$):** Often impossible, as this is inherent to the problem.
2. **Increase Data Strength ($\Phi^T\Phi$):** This matrix represents the "spread" or amount of our data. As $n$ (sample size) increases, the entries in $\Phi^T\Phi$ grow larger. Since we are taking the _inverse_, the variance gets **smaller**.
    - Roughly speaking, the variance shrinks at a rate of $1/n$. More data equals more precision.

---

## 2.7 The Risk of the OLS Estimator

We have established that our estimator $\hat{\theta}$ is unbiased and we know its variance. But in Machine Learning, our ultimate metric is **Generalization**: How well will our model perform on a _new_, unseen data point? This is measured by the **Expected Risk**.

### Step 1: Risk of a Fixed Parameter (Proposition 3.5)

Before we analyze our calculated estimator $\hat{\theta}$ (which is random because it depends on the data), let's first calculate the risk for any _fixed_, non-random set of weights $\theta$.

We want to calculate the expected squared error on a new point $(X, Y)$: $$ R(\theta) = \mathbb{E}[(Y - \phi(X)^T \theta)^2] $$

By substituting the Linear Assumption ($Y = \phi(X)^T \theta^* + \epsilon$), expanding the square, and using the fact that noise $\epsilon$ is independent of $X$ (and thus cross-terms average out to zero), we arrive at a crucial decomposition:

$$ R(\theta) = (\theta^* - \theta)^T \Sigma (\theta^* - \theta) + R(\theta^*) $$

Here:

- **$\Sigma$** is the covariance matrix of the features: $\mathbb{E}[\phi(X)\phi(X)^T]$. It describes the shape of the data distribution.
- $R(\theta^*) = \sigma^2$ is the **Irreducible Error**. Even if we knew the perfect weights $\theta^*$, we would still have an error of $\sigma^2$ because of the random noise $\epsilon$.

### Step 2: Risk of the Estimator (Proposition 3.6)

Now we substitute our estimator $\hat{\theta}$ into the equation. Since $\hat{\theta}$ is a random variable (it changes depending on which $n$ samples we trained on), we must take the expectation over the training data as well.

The formula for the expected risk of the OLS estimator is: $$ \mathbb{E}[R(\hat{\theta})] = R(\theta^*) + \frac{\sigma^2}{n} \mathbb{E}[\text{Tr}(\Sigma \hat{\Sigma}^{-1})] $$

**How do we derive this? (The "Trace Trick")** The derivation involves a clever trick using the **Trace** of a matrix (the sum of diagonal elements).

1. From Step 1, the "excess risk" is the term $\mathbb{E}[(\theta^* - \hat{\theta})^T \Sigma (\theta^* - \hat{\theta})]$.
2. This term is a **scalar** (a single number). In linear algebra, the trace of a scalar is the scalar itself. This allows us to use the cyclic property of the trace ($\text{Tr}(ABC) = \text{Tr}(CAB)$) to rearrange terms.
3. We cycle the vector $(\theta^* - \hat{\theta})$ to the end. This creates the term $(\theta^* - \hat{\theta})(\theta^* - \hat{\theta})^T$, which is exactly the definition of **Variance** we found in Section 2.6!
4. Substituting the variance formula ($\sigma^2 \mathbb{E}[(\Phi^T\Phi)^{-1}]$), we arrive at the final result.

### Interpretation: The Two Sources of Error

This final formula tells us that our total error comes from two sources:

1. **The Noise Floor ($R(\theta^*) = \sigma^2$):** We can never beat this. It is the noise inherent in the universe (or the data).
2. **The Estimation Cost ($\frac{\sigma^2}{n} \dots$):** This is the extra error we pay because we don't know the true $\theta^*$.
    - It increases with noise $\sigma^2$.
    - It **decreases** as $n$ (sample size) gets larger.
    - It depends on the ratio between the true data distribution $\Sigma$ and our empirical sample distribution $\hat{\Sigma}$.


---

# Summary & Key Takeaways: The Dual Nature of OLS

To conclude our deep dive into Linear Regression, it is crucial to recognize that we have solved the problem from two completely different angles that surprisingly lead to the same result. This duality is what makes the Ordinary Least Squares (OLS) estimator so powerful.

## 1. The Geometric Perspective (The "How")

From a purely mathematical and geometric standpoint, we defined the "best" model as the one that minimizes the squared Euclidean distance between our predictions and the reality. We discovered that the OLS estimator $\hat{\theta} = (\Phi^T\Phi)^{-1}\Phi^T y$ is nothing more than an **orthogonal projection**.

- We cannot reach the true target $y$ because it lives outside our feature space (due to noise).
- Therefore, we project $y$ onto the subspace spanned by our features ($im(\Phi)$). The resulting vector $\hat{y}$ is the closest possible point to the truth that our model is capable of representing.

## 2. The Statistical Perspective (The "Why")

When we added the **Linear Assumption** (assuming data is generated by $Y = \phi(X)^T \theta^* + \epsilon$), we gained the ability to evaluate the quality of our model on _unseen_ data. We proved two vital properties of the OLS estimator:

- **Unbiased:** On average, our method finds the true parameters ($\mathbb{E}[\hat{\theta}] = \theta^*$). We are not systematically wrong.
- **Variance:** However, we pay a price. Because we have finite data ($n$), our estimate fluctuates. The variance is $\frac{\sigma^2}{n}$. This means our precision improves linearly as we collect more data.

## 3. The Final Verdict: The Risk Decomposition

The ultimate conclusion of this week is the formula for the **Expected Risk** on new data. It decomposes the error into two fundamental components that cannot be avoided:

$$ \mathbb{E}[R(\hat{\theta})] = \underbrace{\sigma^2}_{\text{Irreducible Noise}} + \underbrace{\frac{\sigma^2}{n} \mathbb{E}[\text{Tr}(\Sigma \hat{\Sigma}^{-1})]}_{\text{Estimation Variance}} $$

This equation tells us the limit of machine learning:

1. **Noise Floor:** We can never predict better than the intrinsic noise of the system ($\sigma^2$).
2. **Cost of Ignorance:** The second term is the penalty we pay for not knowing the true $\theta^*$. This penalty is proportional to the noise ($\sigma^2$), the complexity of our features ($d$), and inversely proportional to the amount of data ($n$).

### Looking Ahead: The Computational Bottleneck

While we have a beautiful closed-form solution $\hat{\theta} = (\Phi^T\Phi)^{-1}\Phi^T y$, there is a practical problem lurking in the shadows. Calculating the inverse of the matrix $\Phi^T\Phi$ is computationally expensive.

- The complexity is roughly $O(nd^2 + d^3)$.
- If we have millions of features ($d$) or huge datasets ($n$), calculating this exact formula becomes too slow or numerically unstable.

This limitation sets the stage for **Week 3**, where we will explore methods to approximate this solution more efficiently (like Gradient Descent) and deal with situations where our model becomes "too complex" (Overfitting).

# Spiegami in modo semplice cosa abbiamo fatto dal 2.2 fino al 2.7

Certamente. Immagina i capitoli dal 2.2 al 2.7 come un viaggio che parte dal "Come si fa?" e arriva al "Perché funziona?".

Ecco il senso logico di ogni passaggio, spiegato in modo semplice:

### 1. Potenziamo il Modello (2.2: Feature Maps & Generalizzazione)

Nel "Warm-Up" (2.1) abbiamo tracciato una retta semplice. Ma il mondo reale è fatto di curve, onde e relazioni complesse.

- **Il problema:** Una retta non basta per descrivere dati complessi.
- **La soluzione:** Non cambiamo l'algoritmo, cambiamo i **dati**. Usiamo le **Feature Maps** ($\phi$) per trasformare i dati (es. elevando al quadrato $x \to x^2$).
- **Il senso:** Rendiamo il modello capace di disegnare curve complesse pur continuando a usare la matematica semplice delle linee rette (Linearità nei parametri $\theta$).

### 2. Troviamo la Soluzione (2.3: OLS Estimator)

Ora che abbiamo il modello potente, come troviamo i pesi migliori ($\theta$)?

- **Il senso:** Non andiamo per tentativi. La matematica ci regala una formula "magica" (chiusa ed esatta), chiamata **OLS Estimator**: $\hat{\theta} = (\Phi^T\Phi)^{-1}\Phi^T y$. Questa formula ci dà immediatamente la soluzione che minimizza l'errore sui dati che abbiamo.

### 3. Visualizziamo cosa accade (2.4: Interpretazione Geometrica)

Cosa sta facendo quella formula nello spazio?

- **Il senso:** Immagina che il tuo obiettivo (il vettore $y$) sia un punto irraggiungibile che fluttua nello spazio (perché contiene rumore che il tuo modello non può prevedere). L'OLS trova la **proiezione ortogonale** (l'ombra) di quel punto sul piano del tuo modello. È il punto più vicino possibile alla verità che il tuo modello può toccare.

### 4. Definiamo le Regole del Gioco (2.5: Linear Assumption)

Qui passiamo dalla geometria alla statistica.

- **Il senso:** Per capire se il nostro metodo è valido, dobbiamo fare un'ipotesi su come funziona il mondo. Assumiamo che esista una "verità nascosta" ($\theta^*$) che genera i dati, sporcata solo da un po' di rumore casuale ($\epsilon$). Senza questa assunzione, non potremmo valutare quanto siamo bravi.

### 5. La Garanzia di Qualità (2.6: Estimating $\theta^*$)

Ora ci chiediamo: la nostra formula OLS riesce a scoprire quella verità nascosta ($\theta^*$)?

- **Il senso:** Sì, abbiamo due garanzie statistiche:
    1. **Non siamo prevenuti (Unbiased):** In media, colpiamo il centro del bersaglio ($\mathbb{E}[\hat{\theta}] = \theta^*$).
    2. **Miglioriamo con l'esperienza (Variance):** Più dati raccogliamo ($n$), più la nostra mira diventa stabile e precisa (la varianza scende come $1/n$).

### 6. Il Conto Finale (2.7: Risk of OLS)

Alla fine, quanto errore faremo su dati nuovi (futuri) che non abbiamo mai visto?

- **Il senso:** L'errore totale è la somma di due cose:
    1. **Rumore Irriducibile ($\sigma^2$):** L'imprevedibilità del mondo. Nessuno può eliminarlo.
    2. **Costo dell'Apprendimento:** Un errore extra dovuto al fatto che abbiamo usato un numero limitato di dati per imparare. Questo capitolo ci dice che l'errore cala man mano che $n$ aumenta, ma non scenderà mai sotto la soglia del rumore intrinseco.

**In sintesi estrema:**

1. Prepariamo i dati per gestire le curve (2.2).
2. Calcoliamo la soluzione perfetta sui dati che abbiamo (2.3).
3. Capiamo che è una proiezione geometrica (2.4).
4. Assumiamo che ci sia una verità da scoprire (2.5).
5. Dimostriamo che il nostro metodo scopre la verità in media (2.6).
6. Calcoliamo quanto errore ci costerà l'incertezza sui nuovi dati (2.7).