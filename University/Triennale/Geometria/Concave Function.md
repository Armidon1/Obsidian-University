# Concave Function (Funzione Concava)

## 1. Intuitive Definition
Visually, a concave function looks like a **hill** or an **inverted bowl**.
If you pour water onto the function, it will **spill off**. It "curves downwards."
![[Pasted image 20260212193540.png]]
> [!TIP] Mnemonic
> ![[Pasted image 20260212193523.png]]
> **Concave** has a "cave" like a... **cave** (the entrance of a cave curves inward/downward).
> Alternatively: It looks like a "frown" $\frown$.

## 2. Mathematical Definition
A function $f(x)$ is concave if, for any two points $x_1$ and $x_2$ in its domain, the line segment connecting $(x_1, f(x_1))$ and $(x_2, f(x_2))$ lies **below or on** the graph of the function.

Mathematically:
$$f(tx_1 + (1-t)x_2) \geq t f(x_1) + (1-t) f(x_2)$$
for all $t \in [0, 1]$.

> [!NOTE] Relation to Convexity
> A function $f(x)$ is concave if and only if $-f(x)$ is [[Convex Function|convex]].
> *(This is useful: minimizing a convex function is the same as maximizing a concave function).*

## 3. Key Properties

### A. The Maximum Guarantee
* **Property:** If a strictly concave function has a Local Maximum, that point is also the **Global Maximum**.
* **Implication:** In optimization problems where we want to **maximize** something (like utility or profit), concavity guarantees a unique best solution.

### B. Second Derivative Condition
* **Single Variable:** If the function is twice differentiable, it is concave if and only if the second derivative is non-positive everywhere:
    $$f''(x) \leq 0$$
    *(Think: Negative implies a "frown" shape $\frown$)*.
* **Multivariate:** The **Hessian Matrix** must be **Negative Semi-Definite (NSD)**.

## 4. Examples
1.  $f(x) = -x^2$ (Inverted parabola).
2.  $f(x) = \log(x)$ (Logarithmic function - grows slower and slower).
3.  $f(x) = \sqrt{x}$ (Square root for $x \ge 0$).

---

## 🇬🇧 English for Math (Language Notes)

> [!NOTE] Grammar & Terminology
>
> 1.  **"Lies below"**:
>     * *Italian:* "Sta sotto" / "Giace sotto".
>     * *English:* Again, use **lies below**. "Is under" is acceptable in casual speech, but "lies below" is precise in geometry.
>
> 2.  **"Spill off"**:
>     * While convex functions "hold" water (come una ciotola), concave functions make water **spill off** (versarsi/cadere via).
>
> 3.  **"Upper Bound"**:
>     * The line segment acts as a *lower bound* for a convex function, but an **upper bound** is not the right term here. Instead, we say the chord is **below** the curve.
>
> 4.  **"Bounded above"**:
>     * A concave function like $-x^2$ is **bounded above** (ha un limite superiore, il picco), whereas a convex function is **bounded below** (ha un limite inferiore, la valle).