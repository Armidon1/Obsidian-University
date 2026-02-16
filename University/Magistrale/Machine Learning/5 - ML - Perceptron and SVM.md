For the original source (important for the prof's theorem's proofs, see [[Original 5 ML|here]])

![[5_-_ML_-_Dal_Perceptron_alle_SVM.mp4]]
---
## Part 1: The Setup and the Hyperplane

![[Pasted image 20260216174530.png]]

In this section, we set the stage for the **Perceptron**. Instead of jumping straight into the algorithm, we first need to understand the geometry of the problem we are trying to solve.

#### The Goal: Binary Classification

Imagine you have a dataset of points plotted on a graph. Some points belong to one category (let's label them **+1**) and others belong to a different category (labeled **-1**). The fundamental goal of the Perceptron is to draw a straight line (or a flat sheet, depending on the dimensions) that perfectly separates these two groups.

In mathematical terms, we assume the dataset is **linearly separable**. This means there exists at least one "wall" that can divide the positive points from the negative points without making any mistakes.

#### Defining the Data and the Model

Let's formalize the inputs:

- We have $n$ data points: $(x_1, y_1), (x_2, y_2), \dots, (x_n, y_n)$.
- $x_i$ is a vector in $\mathbb{R}^d$ (the features of your data).
- $y_i$ is the label, which can only be **-1** or **1**.

Our objective is to find a **hyperplane**, denoted as $H_\theta$. You can think of a hyperplane as the decision boundary (una superficie o una linea che suddivide lo spazio delle caratteristiche (features) in regioni distinte dove ogni regione corrisponde a una specifica etichetta di classe (nel tuo caso, **-1** o **1**)). If a point falls on one side, we classify it as positive; if it falls on the other, it is negative.

#### How the Hyperplane Works

![[Pasted image 20260216181238.png]]

A generic hyperplane is defined by a vector $\theta$ (theta). This vector $\theta$ is important because it is **orthogonal** (perpendicular) to the hyperplane itself. It points in the direction of the "positive" side.

Mathematically, the hyperplane $H_\theta$ is the set of all points $x$ where the dot product with $\theta$ is zero: $$H_\theta = {x \in \mathcal{X} \mid x^T \theta = 0}$$
[[5 ML more about the hyperplane|see here more about the hyperplane]]

To classify a new point $x$, we simply check the angle between the point $x$ and our vector $\theta$ by calculating $x^T \theta$:

1. If $x^T \theta \geq 0$, the angle is less than 90 degrees, so the point is on the "positive" side. We predict **+1**.
2. If $x^T \theta < 0$, the point is on the "opposite" side. We predict **-1**. The prediction formula is simply: $\text{sign}(x^T \theta)$.

![[Pasted image 20260216184129.png]]

#### A Note on Simplified Geometry (Homogeneous Coordinates)

![[Pasted image 20260216184712.png]]

You might wonder: "Don't lines usually have an intercept (or bias), like $y = mx + q$?" Yes, usually a hyperplane needs a bias term to move away from the origin. However, to make our math cleaner, we use a trick called **homogeneous coordinates**. We assume our hyperplane passes through the origin. If our data requires a bias, we simply add an extra dimension (an extra coordinate set to 1) to all our data points. This allows us to treat everything as a simple dot product without worrying about a separate bias term.

#### Types of Errors

Before looking at how the algorithm learns, we must define what constitutes a mistake:

![[Pasted image 20260216184650.png]]

- **Classification Error:** This happens when our prediction disagrees with the true label $y$. Since $y$ is either 1 or -1, if the product $y \cdot x^T \theta$ is negative, it means the signs disagreed. This is an error.
- **Margin Error:** This is a stricter condition. Even if we classify the point correctly, we might barely scrape by. We say there is a "margin error" if $y \cdot x^T \theta < 1$. This means the point is too close to the boundary for comfort, or it is on the wrong side.

	but what it is actually the differences between the [[Perceptron]] and the [[Logistic Regression]]? see [[Perceptron vs Logistic Regression|here]]

---

## Part 2: The Perceptron Algorithm and Novikoff's Theorem

Now that we have defined our geometry, we can look at the **Perceptron Algorithm** itself. It is surprisingly simple for such a powerful tool. It is an iterative algorithm, meaning it looks at the data points one by one and updates its strategy on the fly.

#### The Algorithm Loop

The process works as follows:

1. **Initialization:** We start with a weight vector $\theta$ set to zero (a vector of all zeros). This means initially, we have no idea where the separating line is.
2. **Selection:** We loop through our data for a fixed number of iterations ($N$). In each step, we pick a random data point $(x_{i_t}, y_{i_t})$ from our dataset.
3. **The Check:** We check if our current hyperplane $\theta_t$ makes a **margin error** on this point. Recall from the previous section that a margin error occurs if $y_{i_t} \cdot x_{i_t}^T \theta_t < 1$.
    - In simple terms: "Is this point on the wrong side, or is it correctly classified but dangerously close to the boundary?"

#### The Update Rule

![[Pasted image 20260216180251.png]]

- If there is no error, we do nothing. We keep $\theta_t$ exactly as it is. 
- if there **is** a margin error, we must update our vector. The update rule is elegant: $$ \theta_{t+1} \leftarrow \theta_t + y_{i_t} x_{i_t} $$

**Why does this work?** Think about the geometry. If the point was positive ($y=1$) but we predicted negative (or had a low score), adding $x$ to $\theta$ makes the new $\theta$ point more in the direction of $x$. This increases the dot product $x^T\theta$, fixing the error. Conversely, if $y=-1$, we subtract $x$, making $\theta$ point away from $x$, lowering the score.

Do you remember about $\theta$? see [[5 ML theta cazzè|here]]

#### Will it ever stop? (Novikoff’s Theorem)

A major question in machine learning is "Convergence." If we let this run, will it eventually find the perfect separator, or will it loop forever making mistakes?

**Theorem 1.4 (Novikoff)** gives us a guarantee. It states that if the dataset is linearly separable, the Perceptron will make a finite number of mistakes and then stop. Specifically, the number of mistakes $M$ is bounded by: $$ M \leq \frac{2 + D^2}{(\gamma^*)^2} $$

Here is how to interpret the components of this formula:

- $D$ is the **diameter** of the data (the length of the longest vector $x$). If your data points are spread very far out, it might take longer to converge.
- $\gamma^*$ is the **optimal margin**. This represents how "easy" the problem is. If the gap between positive and negative points is wide (large $\gamma^*$), the algorithm converges quickly. If the gap is tiny, the algorithm struggles to squeeze the line in between.

#### More about the optimal margin

![[Pasted image 20260216191253.png]]

Sì, **esattamente**. Hai colto il concetto fondamentale, ma per essere rigorosi dobbiamo distinguere tra il margine di un iperpiano qualsiasi e il "margine ottimo".

Ecco la distinzione precisa basata sulle tue fonti:

##### 1. Il Margine di un Iperpiano ($\gamma(\theta)$)

Hai ragione: dato un iperpiano $H_\theta$ che separa correttamente i dati, il suo margine è definito come la **distanza tra l'iperpiano stesso e il punto del dataset più vicino** a esso.

- Formula: $\gamma(\theta) = \min_{i} \text{dist}(x_i, H_\theta)$.
- Visivamente: È lo spazio libero tra il "muro" e il giocatore più vicino al muro.

##### 2. L'Optimal Margin ($\gamma^\star$)

L'**Optimal Margin** è il **massimo possibile** di questa distanza minima. Tra tutti gli infiniti muri (iperpiani) che potresti costruire per separare i dati, l'_optimal margin_ appartiene a quello specifico muro che riesce a stare più lontano possibile dai punti di entrambe le classi.

##### In sintesi

- **Distanza:** Quanto è lontano un punto dal muro.
- **Margine:** Quanto è lontano il punto _più vicino_ (il caso peggiore) dal muro.
- **Optimal Margin:** La "strada" più larga che puoi costruire massimizzando quella distanza minima.

> **Nota tecnica:** I punti che si trovano esattamente a questa distanza minima (sul bordo della strada) sono chiamati **Support Vectors**, perché sono quelli che "reggono" il margine.

#### Intuition behind the Proof

The proof of this theorem relies on two competing forces:

1. **The Growth of Alignment:** Every time we update $\theta$, it gets "closer" to the perfect solution $\theta^*$. We can prove mathematically that the dot product between our current $\theta$ and the perfect $\theta^*$ grows steadily.
2. **The Growth of Length:** However, we also check how fast the _length_ (norm) of our vector $\theta$ grows. It turns out the length grows quite slowly (at a rate related to the diameter $D$).

By comparing these two rates using the **Cauchy-Schwarz inequality** (which basically says the overlap between two vectors can't exceed their lengths multiplied), we reach a contradiction if the number of mistakes gets too high. Therefore, the mistakes _must_ stop growing eventually.

---

Ecco la terza parte. Qui facciamo il salto concettuale dal Perceptron (che trova una linea _qualsiasi_ che funziona) alle Support Vector Machines (che cercano la linea _migliore_ possibile) e vediamo come gestire i dati che non possono essere separati perfettamente.

---

## Part 3: Support Vector Machines (Hard and Soft Margins)

![[Pasted image 20260216175249.png]]

While the Perceptron is a fantastic starting point, it has a significant flaw. It stops as soon as it finds _any_ hyperplane that separates the data. But not all separating lines are created equal. Imagine a line that barely scrapes past your data points versus a line that sits perfectly in the middle of the gap. We clearly prefer the latter. This preference leads us to the **[[Support Vector Machine (SVM)]]**.

#### The Hard-Margin SVM (The Search for the "Best" Line)

![[Pasted image 20260216200253.png]]

If our data is perfectly separable, we don't just want a solution; we want the solution with the **largest margin** ($\gamma^*$). The margin is the distance between the hyperplane and the closest data point. A larger margin implies our model is more robust and "safer" against noise.

Mathematically, maximizing the margin turns out to be equivalent to minimizing the length (norm) of our vector $\theta$. Why is this?

- Recall that the margin $\gamma(\theta)$ is proportional to $1/|\theta|$.
- Therefore, to **maximize** the margin, we must **minimize** $|\theta|$.

This gives us the **Hard-Margin optimization problem**: $$ \min_\theta \frac{1}{2} |\theta|^2 \quad \text{subject to} \quad y_i(x_i^T \theta) \geq 1 \text{ for all } i $$ In plain English: "Find the smallest possible vector $\theta$ (simplest solution) such that every single data point is correctly classified with a safety score of at least 1". **Proposition 2.1** confirms that if you solve this problem, you invariably find the optimal margin $\gamma^*$.

#### The Reality Check: Non-Separable Data (Soft-Margin SVM)

In the real world, data is rarely perfect. There might be noise or outliers that make perfect separation impossible. If we insist on a "Hard Margin," our algorithm will fail to find a solution.

To fix this, we introduce **slack variables**, denoted by the Greek letter $\xi_i$ (xi). We allow the model to make mistakes, but we penalize it for them. For each data point, $\xi_i$ measures how much the point violates the safety margin:

- If $\xi_i = 0$, the point is correctly classified and safe.
- If $\xi_i > 0$, the point is either too close to the boundary or on the wrong side entirely.

Our new goal is a trade-off. We want to keep the vector $\theta$ small (for a good margin) _AND_ we want to keep the total errors ($\sum \xi_i$) small. This is the **Soft-Margin SVM**: $$ \min_{\theta, \xi} \frac{1}{2} |\theta|^2 + C \sum_{i=1}^n \xi_i $$ Here, **$C$ is a crucial hyperparameter**. It acts like a volume knob:

- **High $C$:** We care a lot about errors. The model will try very hard not to miss any points (risking overfitting).
- **Low $C$:** We care more about having a simple, wide margin. We tolerate more mistakes to get a "smoother" boundary.

#### Simplifying with Hinge Loss

Managing these constraints (the "subject to" parts) can be mathematically annoying. We can simplify the problem by combining the constraints directly into the minimization formula.

We use the **Hinge Loss function**: $h(z) = (1 - z)_+$. This function looks at our prediction score ($y_i \theta^T x_i$). If the score is greater than 1 (safe), the cost is 0. If the score is less than 1, the cost increases linearly.

This leads to the modern, unconstrained formulation of SVM: $$ \min_\theta \frac{1}{2} |\theta|^2 + C \sum_{i=1}^n (1 - y_i \theta^T x_i)_+ $$ This equation is beautiful because it is **convex**. In mathematics, convex functions are bowl-shaped, meaning they have a single global minimum. We can easily slide down to the bottom of this bowl using gradient descent to find the best solution.

---

**Tutto chiaro su come siamo passati dal "cercare una linea" al "cercare la linea ottima col compromesso degli errori"?** Il prossimo paragrafo riguarderà come risolvere praticamente questa equazione usando lo **Stochastic Gradient Descent (SGD)** e il concetto di **Sub-gradiente** (necessario perché la funzione Hinge ha uno spigolo e non è differenziabile ovunque). Procedo?

Ecco la quarta parte. Qui entriamo nel "motore" che fa funzionare le SVM: come calcolare concretamente la soluzione usando la discesa del gradiente, e come gestire il fatto che la nostra funzione di costo ha uno "spigolo" (non è differenziabile ovunque).

---

## Part 4: Solving SVM with Stochastic Gradient Descent (SGD)

We have established that finding the best SVM model means minimizing a specific cost function. This function combines two goals: keeping the vector $\theta$ small (regularization) and keeping the errors low (Hinge loss). The formula is: $$ L(\theta) = \frac{1}{2} |\theta|^2 + C \sum_{i=1}^n (1 - y_i \theta^T x_i)_+ $$

To minimize this, we typically use **Stochastic Gradient Descent (SGD)**. However, there is a mathematical hurdle: the Hinge loss function $(1 - z)_+$ is not a smooth curve; it has a sharp corner (a "kink") at $z=1$. In calculus, you cannot take the derivative of a sharp corner.

#### The Solution: Sub-Gradients

To get around this, we use a **sub-gradient**. Think of a derivative as the tangent line touching a curve. At a sharp corner, you can't draw a _single_ unique tangent line, but you can draw _many_ lines that stay "under" the function. Any of these valid lines gives us a "sub-gradient."

- If the point is clearly on the wrong side ($y_i \theta^T x_i < 1$), the slope is clear: $-y_i x_i$.
- If the point is clearly safe ($y_i \theta^T x_i > 1$), the slope is 0.
- If the point is exactly on the boundary ($y_i \theta^T x_i = 1$), we can pick a value in between. Usually, we just pick one for simplicity.

#### The SGD Algorithm for SVM

When we apply this logic to our update rule, we get **Algorithm 2**, which looks remarkably similar to the Perceptron but with a crucial "shrinkage" step. We iterate through the data using a learning rate $\eta_t$ (often set to $1/Ct$). For each random point $(x_{i_t}, y_{i_t})$:

1. **Check for Error:** Is $y_{i_t} x_{i_t}^T \theta_t < 1$?
2. **Case A (Error):** If there is a margin violation, we update $\theta$ in two ways:
    - We move it toward the correct direction (like Perceptron): $+ \eta_t C y_{i_t} x_{i_t}$.
    - We _shrink_ the current vector slightly to minimize the norm: $- \eta_t \theta_t$.
    - **Combined Update:** $\theta_{t+1} \leftarrow (1 - \eta_t)\theta_t + \eta_t C y_{i_t} x_{i_t}$.
3. **Case B (No Error):** Even if the point is correct, we still apply the regularization! We shrink the vector slightly to ensure we are constantly trying to maximize the margin.
    - **Update:** $\theta_{t+1} \leftarrow (1 - \eta_t)\theta_t$.

This distinction is vital: **Perceptron only learns from mistakes. SVM learns from everything**, constantly refining the margin even on correct predictions.

---

**Tutto chiaro sulla differenza tra l'update del Perceptron e quello dell'SVM?** Ora passiamo all'ultimo concetto fondamentale: il **Kernel Trick**. Questo è il trucco magico che permette a un classificatore lineare di risolvere problemi _non lineari_ (come cerchi o spirali) senza esplodere nei calcoli. Procedo?

Ecco l'ultima parte fondamentale: il **Kernel Trick**. Questo è il concetto che trasforma un classificatore "stupido" (che sa disegnare solo linee rette) in uno strumento potentissimo capace di disegnare curve complesse e forme multidimensionali, senza far esplodere i calcoli.

---

## Part 5: The Kernel Trick (Going Beyond Linearity)

Up to this point, we have assumed that our decision boundary is a straight line (or a flat hyperplane). But real-world data is often complex; imagine data points arranged in a circle or a spiral. A straight line simply cannot separate them.

![[Pasted image 20260216175904.png]]

#### The Intuition: Mapping to Higher Dimensions

To solve this, we use a **Feature Map**, denoted by $\psi$ (psi). The idea is to "lift" our data from the original space (where it is not separable) into a much higher-dimensional space (where it might be). For example, if you have 1D data points scattered on a line, you can map them to a parabola in 2D ($x \to (x, x^2)$). Suddenly, a straight line in 2D can slice through the parabola, effectively creating a non-linear boundary in the original 1D space.

However, there is a catch: the dimension of this new space ($d'$) could be massive, or even **infinite**. Calculating coordinates and dot products in an infinite-dimensional space is computationally impossible. This is where the **Kernel Trick** saves us.

#### The Mathematical Foundation: The Representer Theorem

First, we need to realize something crucial about our weight vector $\theta$. Whether we use the Perceptron or SVM, the vector $\theta$ is built by adding and subtracting our training data points $x_i$ (remember the update rule $\theta \leftarrow \theta + y_i x_i$). This leads to the **Representer Theorem**: The optimal vector $\theta$ is always a linear combination of the transformed data points: $$ \theta = \sum_{i=1}^n \alpha_i \psi(x_i) $$ Here, $\alpha_i$ are simply weights telling us how much each specific data point contributes to the final model.

#### The "Trick": Calculating without Moving

Because $\theta$ is just a sum of points, when we want to make a prediction for a new point $x_j$, we compute the dot product: $$ \langle \psi(x_j), \theta \rangle = \left\langle \psi(x_j), \sum_{i=1}^n \alpha_i \psi(x_i) \right\rangle $$ Using linearity, we can pull the sum out: $$ = \sum_{i=1}^n \alpha_i \langle \psi(x_j), \psi(x_i) \rangle $$ Do you see the magic here? We **never** need to know the vector $\theta$ explicitly, nor do we need to know the coordinates of $\psi(x)$. We only need to know the result of the dot product between two points in that high-dimensional space.

We define this dot product as the **Kernel Function**: $$ K(x_i, x_j) = \langle \psi(x_i), \psi(x_j) \rangle $$ This allows us to work in infinite dimensions while doing simple calculations in our original space.

#### Common Kernels

The text gives two powerful examples of Kernels:

1. **Polynomial Kernel:** $$ K(x, z) = (x^T z + c)^D $$ This implicitly maps your data into a space containing all possible interactions of features up to degree $D$. If you tried to write out all those coordinates manually, it would take forever, but the Kernel computes it in one simple step.
2. **Gaussian (RBF) Kernel:** $$ K(x, z) = e^{-\frac{|x-z|^2}{2\sigma^2}} $$ This is the most famous kernel. It corresponds to a feature map into an **infinite-dimensional** Hilbert space. Conceptually, it measures "similarity": if $x$ and $z$ are close, the value is near 1; if they are far, it drops to 0. It allows the SVM to draw very smooth, flexible boundaries around your data.

---

Questo conclude la **Week 5**. Abbiamo coperto:

1. La geometria dell'iperpiano.
2. L'algoritmo Perceptron e la sua convergenza.
3. Le SVM (Hard e Soft margin).
4. L'ottimizzazione tramite SGD e Sub-gradienti.
5. Il Kernel Trick per la non-linearità.

Sei soddisfatto di questa struttura per le tue note su Obsidian o vuoi che approfondiamo qualche passaggio matematico specifico?