# Convex Function (Funzione Convessa)

## 1. Intuitive Definition
Visually, a convex function looks like a **bowl** or a **valley**.
If you pour water into the function, it will collect at a single point (the bottom).
![[Pasted image 20260212193534.png]]

> [!TIP] Mnemonic
> ![[Pasted image 20260212193512.png]]
> **Convex** has a "V" like a **V**alley.
> **[[Concave Function|Concave]]** has a "cave" like a... **cave** (curves downwards).

## 2. Mathematical Definition
A function $f(x)$ is convex if, for any two points $x_1$ and $x_2$ in its domain, the line segment connecting $(x_1, f(x_1))$ and $(x_2, f(x_2))$ lies **above or on** the graph of the function.

Mathematically:
$$f(tx_1 + (1-t)x_2) \leq t f(x_1) + (1-t) f(x_2)$$
for all $t \in [0, 1]$.

## 3. Key Properties

### A. The Minimum Guarantee (Crucial for Optimization)
This is the most important property for Gradient Descent and Machine Learning.
* **Property:** If a strictly convex function has a Local Minimum, that point is also the **Global Minimum**.
* **Implication:** We do not need to worry about getting stuck in a "false valley" (local minimum). If the derivative is zero ($\nabla f(x) = 0$), we have found the best possible solution.

### B. Second Derivative Condition
* **Single Variable:** If the function is twice differentiable, it is convex if and only if the second derivative is non-negative everywhere:
    $$f''(x) \geq 0$$
    *(Think: Positive implies a "smile" shape $\smile$)*.
* **Multivariate:** The **Hessian Matrix** (matrix of second derivatives) must be **Positive Semi-Definite (PSD)**.

## 4. Examples
1.  $f(x) = x^2$ (The standard parabola).
2.  $f(x) = e^x$ (Exponential function).
3.  $f(x) = |x|$ (Absolute value - convex but not differentiable at 0).
4.  **Cross-Entropy Loss** and **Mean Squared Error (MSE)** (Common cost functions in ML).

---

## 🇬🇧 English for Math (Language Notes)

> [!NOTE] Grammar & Terminology
>
> 1.  **"Lies above"**:
>     * *Italian:* "Sta sopra".
>     * *English:* We say the line segment **lies above** the graph. Avoid saying "stays over".
>
> 2.  **"Strictly Convex" vs "Convex"**:
>     * If the curve is flat at the bottom (like a bathtub), it is *convex* but not *strictly convex*.
>     * If it curves up everywhere (like a perfect bowl), it is **strictly convex**.
>
> 3.  **Zero Conditional (Review)**:
>     * Notice the definitions use the Present Simple for facts:
>     * *"If the second derivative **is** positive, the function **curves** upward."* (Non usare "will curve").
>
> 4.  **False Friends**:
>     * *Argument:* In math, strictly refers to the input of the function ($x$), not a "litigio" (quarrel).
>     * *Stationary Point:* A point where derivative is zero (Punto stazionario).