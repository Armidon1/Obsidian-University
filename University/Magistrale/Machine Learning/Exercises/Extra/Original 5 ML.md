# 5 Week 5: Perceptron and SVM

## 5.1 The Perceptron Algorithm

We introduce one of the seminal machine learning algorithms: the Perceptron. It performs binary classification via separating hyperplanes, under the assumption that the underlying dataset is separable, i.e., there exists a hyperplane that perfectly separates the points corresponding to the two labels.

Formally, we are given $n$ points $(x_{1},y_{1}),(x_{2},y_{2}),...,(x_{n},y_{n})$, with $x_{i}\in\mathcal{X}=\mathbb{R}^{d}$ and $y_{i}\in\mathcal{Y}=\{-1,1\}$, and we want to find an hyperplane $H_{\theta}$ that separates them.

Recall, a generic hyperplane $H_{\theta}$ is given by all the points orthogonal to a non-zero vector $\theta$: $H_{\theta}=\{x\in\mathcal{X}|x^{T}\theta=0\}$.

Given a vector $\theta\in\mathbb{R}^{d}$ and a point $x\in\mathbb{R}^{d}$. The label $y$ predicted for $x$ by $\theta$ is then $\text{sign}(x^{T}\theta)$ (e.g., +1 if $x^{T}\theta\ge0$, and -1 if $x^{T}\theta<0$).

**Definition 1.1.** Given a vector $\theta$, and a point with label $y\in\{-1,1\}$, we say that $H_{\theta}$ makes a classification error on $x$ if $y\cdot x^{T}\theta\le0$. If we have that $y\cdot x^{T}\theta<1$, then we say that there is a margin error.

**Remark 1.2.** As we have already done for linear regression, we are considering homogeneous hyperplanes, i.e., those that contain the origin. This is, again, without loss of generality, as we can always add an extra dimension and set the corresponding coordinate to 1 for all the points in the dataset.

The Perceptron algorithm, described in the pseudocode, works as follows. It maintains a candidate hyperplane identified by vector $\theta_{t}$, then considers the points in the dataset one after the other (either cyclically, or uniformly at random as reported here). Every time that the current solution $\theta_{t}$ makes a margin error on the point $(x_{i_{t}},y_{i_{t}})$ considered, it modifies $\theta_{t}$ by adding $y_{i_{t}}x_{i_{t}}$.

Given a point $x$ and an hyperplane $H_{\theta}$, the distance of $x$ to the hyperplane is:

$$
\text{dist}(x,H_{\theta})=\min_{z\in H_{\theta}}||x-z||=\frac{|x^{T}\theta|}{||\theta||}
$$

**Definition 1.3.** Given $(x_{1},y_{1}),(x_{2},y_{2}),...,(x_{n},y_{n})$ and an hyperplane $H_{\theta}$ that correctly classifies all the points, the margin of $H_{\theta}$, denoted with $\gamma(\theta)$ is defined as the distance of $H_{\theta}$ from its closest point:

$$
\gamma(\theta)=\min_{i=1,...,n}\text{dist}(x_{i},H_{\theta}).
$$

The largest possible margin achievable by a hyperplane that classifies the points correctly is denoted with $\gamma^{*}$.

### Algorithm 1: The Perceptron Algorithm

**Require:** Training data $\{(x_{i},y_{i})\}_{i=1}^{n}$, where $x_{i}\in\mathbb{R}^{d}$, $y_{i}\in\{-1,+1\}$
**Require:** Maximum number of iterations $N$

1. Initialize $\theta_{0}\leftarrow 0\in\mathbb{R}^{d}$
2. **for** $t=1,2,..., N$ **do**
3.     Let $i_{t}$ be an index drawn uniformly at random in $1,...,n$
4.     **if** $y_{i_{t}}\cdot x_{i_{t}}^{T}\theta_{t}<1$ **then** $\quad \triangleright$ Margin Error
5.         $\theta_{t+1}\leftarrow\theta_{t}+y_{i_{t}}x_{i_{t}} \quad \triangleright$ $\theta_{t}$ is adjusted
6.     **else**
7.         $\theta_{t+1}\leftarrow\theta_{t} \quad \triangleright$ $\theta_{t}$ is not updated
8.     **end if**
9. **end for**
10. **return** $\theta_{N}$

---

We are ready to provide an upper bound on the number of margin mistakes that the Perceptron Algorithm makes. We say that the algorithm converges if it finds a hyperplane that correctly classifies all the points and makes no margin error. Finally, we denote with $D$ the diameter of the problem, i.e. $D=\max_{i}||x_{i}||$ and $\gamma^{*}$ the largest possible margin.

**Theorem 1.4. (Novikoff)** The Perceptron Algorithm makes at most $M=\frac{2+D^{2}}{(\gamma^{*})^{2}}$ margin mistakes, if the points are linearly separable with margin $\gamma^{*}$.

**Proof.** Consider a generic time step $t$ where $\theta_{t}$ makes a margin error on $(x_{i_{t}},y_{i_{t}})$, we have:

$$
||\theta_{t+1}||^{2}=||\theta_{t}+y_{i_{t}}x_{i_{t}}||^{2}=||\theta_{t}||^{2}+2y_{i_{t}}x_{i_{t}}^{T}\theta_{t}+||x_{i_{t}}||^{2}\le||\theta_{t}||^{2}+2+D^{2}
$$

Denote with $m_{t}$ the number of margin errors made up to time $t$ included. If we repeatedly apply the above inequality, we get:

$$
||\theta_{t+1}||^{2}\le m_{t}(2+D^{2})+||\theta_{0}||^{2}=m_{t}(2+D^{2}).
$$

Denote now with $\theta^{*}$ a unit norm vector that identifies the hyperplane with the largest margin, so that $\gamma^{*}=\min_{i}y_{i}x_{i}^{T}\theta^{*}$.

$$
(\theta^{*})^{T}\theta_{t+1}=\sum_{k=1}^{m_{t}}(\theta^{*})^{T}(y_{i_{k}}x_{i_{k}})=\sum_{k=1}^{m_{t}}y_{i_{k}}(\theta^{*})^{T}x_{i_{k}}\ge\sum_{k=1}^{m_{t}}\gamma^{*}=m_{t}\gamma^{*}
$$

Now, by Cauchy-Schwarz: $(\theta^{*})^{T}\theta_{t+1}\le||\theta^{*}||\cdot||\theta_{t+1}||=||\theta_{t+1}||$ (since $||\theta^{*}||=1$). So, $m_{t}\gamma^{*}\le||\theta_{t+1}||$. Squaring both sides: $(m_{t}\gamma^{*})^{2}\le||\theta_{t+1}||^{2}$. Combining with the upper bound:

$$
(m_{t}\gamma^{*})^{2}\le||\theta_{t+1}||^{2}\le m_{t}(2+D^{2})
$$

$$
m_{t}^{2}(\gamma^{*})^{2}\le m_{t}(2+D^{2})\Rightarrow m_{t}\le\frac{2+D^{2}}{(\gamma^{*})^{2}}
$$

This concludes the proof.

## 5.2 Support Vector Machine

For the perceptron algorithm to work, we need to assume separability. Another way of looking at this classification task is to solve the following hard-margin problem:

$$
\min_{\theta}\frac{1}{2}||\theta||^{2}
$$

$$
\text{subject to } y_{i}(x_{i}^{T}\theta)\ge1, \forall i
$$

There are two reasons to minimize $||\theta||$. First, it is always good to choose the "simplest" solution. Second, there is a strong relation between $||\theta||$ and the margin $\gamma(\theta)$.

**Proposition 2.1.** Consider any $\hat{\theta}$ that solves the hard-margin problem, then the margin of $H_{\hat{\theta}}$ is optimal, $\gamma(\hat{\theta})=\gamma^{*}$ and $\gamma^{*}=1/||\hat{\theta}||$.

**Proof.** Consider any $\theta$ that satisfies the constraints $y_{i}x_{i}^{T}\theta\ge1$. The margin is:

$$
\gamma(\theta)=\min_{i}\frac{|x_{i}^{T}\theta|}{||\theta||}=\min_{i}\frac{y_{i}x_{i}^{T}\theta}{||\theta||}\ge\frac{1}{||\theta||}
$$

Let $\theta^{*}$ be the optimal vector. We can scale it so that $\min_{i}y_{i}x_{i}^{T}\theta^{*}=1$. For this $\theta^{*}$ we have $\gamma(\theta^{*})=\min_{i}\frac{y_{i}x_{i}^{T}\theta^{*}}{||\theta^{*}||}=\frac{1}{||\theta^{*}||}$. Since $\hat{\theta}$ is the solution that minimizes $||\theta||$ while satisfying the constraints, we have $||\hat{\theta}||\le||\theta^{*}||$. Thus, $\gamma(\hat{\theta})\ge\frac{1}{||\hat{\theta}||}\ge\frac{1}{||\theta^{*}||}=\gamma(\theta^{*})=\gamma^{*}$. Since $\gamma^{*}$ is the largest possible margin, we must have $\gamma(\theta)=\gamma^{*}$. $\Pi$

What can we say when the underlying dataset is not linearly separable? We introduce some slackness. For any point $i$, we associate a slackness variable $\xi_{i}\ge0$ and we relax the margin error: $y_{i}x_{i}^{T}\theta\ge1-\xi_{i}$. Problem (3) then becomes (Soft-Margin SVM):

$$
\min_{\theta,\xi}\frac{1}{2}||\theta||^{2}+C\sum_{i=1}^{n}\xi_{i}
$$

$$
\text{subject to } y_{i}(x_{i}^{T}\theta)\ge1-\xi_{i} \quad \forall i
$$
$$
\xi_{i}\ge0 \quad \forall i
$$

Note, $C$ is a hyperparameter that tunes the relative importance of the norm term and of the margin error.

We can further simplify the optimization problem, by noting that, for any fixed vector $\theta$, the best choice of $\xi_{i}$ is $\xi_{i}=\max\{0,1-y_{i}\theta^{T}x_{i}\}=(1-y_{i}\theta^{T}x_{i})_{+}$, where $(\cdot)_+$ denotes the positive part. Therefore, we can rewrite the equivalent (unconstrained) optimization problem:

$$
\min_{\theta}\frac{1}{2}||\theta||^{2}+C\sum_{i=1}^{n}(1-y_{i}\theta^{T}x_{i})_{+}
$$

The function $h(z)=(1-z)_{+}$ is called the hinge function, and is convex. Therefore, the objective function is convex (sum of two convex functions), and we can safely use gradient or stochastic gradient descent. There is a small caveat: there are some points where the gradient may not be well defined (at $z=1$). In those points, we use a sub-gradient.

**Definition 2.2.** Let $F:\mathbb{R}^{d}\rightarrow\mathbb{R}$ be a convex function, and $x\in\mathbb{R}^{d}$. We say that a vector $g\in\mathbb{R}^{d}$ is a sub-gradient in $x$, if the following inequality holds for any $y\in\mathbb{R}^{d}$:

$$
F(y)\ge F(x)+g^{T}(y-x)
$$

Let $L(\theta)$ be our objective function. $L(\theta)=\frac{1}{2}||\theta||^{2}+C\sum_{i}L_{i}(\theta)$ where $L_{i}(\theta)=(1-y_{i}\theta^{T}x_{i})_{+}$. The sub-gradient of $L_{i}(\theta)$ is:

$$
\partial L_{i}(\theta)=\begin{cases}\{-Cy_{i}x_{i}\} & \text{if } y_{i}\theta^{T}x_{i}<1\\ \{0\} & \text{if } y_{i}\theta^{T}x_{i}>1\\ \{\alpha(-Cy_{i}x_{i})|\alpha\in[0,1]\} & \text{if } y_{i}\theta^{T}x_{i}=1\end{cases}
$$

A valid sub-gradient $g(\theta)$ for $L(\theta)$ can be constructed by taking one sub-gradient for each term. A common choice is:

$$
g(\theta)=\theta+\sum_{i}g_{i}
$$

where $g_{i}\in\partial(C\cdot L_{i}(\theta))$.

$$
g(\theta)=\theta-C\sum_{i}y_{i}x_{i}\mathbb{1}_{\{y_{i}\theta^{T}x_{i}\le1\}}
$$

At this point, it is instructive to look at the pseudocode for the stochastic (sub-)gradient version. A natural choice for the learning rate is $\eta_{t}=\frac{1}{Ct}$. The stochastic sub-gradient descent algorithm for SVM is extremely similar to the Perceptron Algorithm, even though they are designed for slightly different problems. Moreover, this model is called Support Vector Machine (SVM), because the decision boundary only depends on the points considered, where margin errors have been made (the "support vectors").

### Algorithm 2: Stochastic Gradient Descent for SVM

**Require:** Training data $\{(x_{i},y_{i})\}_{i=1}^{n}$, $x_{i}\in\mathbb{R}^{d}$, $y_{i}\in\{-1,+1\}$
**Require:** Maximum iterations $N$, learning rates $\eta_{t}$, regularizer $C$

1. Initialize $\theta_{0}\leftarrow 0\in\mathbb{R}^{d}$
2. **for** $t=1,2,..., N$ **do**
3.     Let $i_{t}$ be an index drawn uniformly at random in $1,...,n$
4.     **if** $y_{i_{t}}\cdot x_{i_{t}}^{T}\theta_{t}<1$ **then** $\quad \triangleright$ Margin Error
5.         $\theta_{t+1}\leftarrow\theta_{t}-\eta_{t}(\theta_{t}-Cy_{i_{t}}x_{i_{t}}) \quad \triangleright$ Update with margin-violating point
6.     **else**
7.         $\theta_{t+1}\leftarrow\theta_{t}(1-\eta_{t}) \quad \triangleright$ Update with only regularization term
8.     **end if**
9. **end for**
10. **return** $\theta_{N}$

## 5.3 Kernel Trick

Now, imagine that we want to go beyond linear separators. A possibility may be to map the points to a feature space via a feature map $\psi:\mathbb{R}^{d}\rightarrow\mathbb{R}^{d^{\prime}}$. We do not want to find an algorithm that depends on the feature dimension $d'$, which may be infinite or very large.

Since we want a definition that also covers infinitely dimensional vector space, we state the formal definition of scalar products (or inner products).

**Definition 2.3.** Given a vector space $V$, a scalar product $\langle\cdot,\cdot\rangle:V^{2}\rightarrow\mathbb{R}$ satisfies the following properties:

* **Linearity:** for any vectors $v,w,z\in V$ and scalar $\alpha\in\mathbb{R}$ it holds $\langle\alpha v,z\rangle=\alpha\langle v,z\rangle$ and $\langle v+w,z\rangle=\langle v,z\rangle+\langle w,z\rangle$.
* **Symmetry:** for any vectors $v,w\in V$ it holds $\langle v,w\rangle=\langle w,v\rangle$.
* **Positivity:** for any vector $v\in V$, $\langle v,v\rangle\ge0$, and the equality is only reached for $v=0$.

The last ingredient we need is the notion of Hilbert space: essentially, an Hilbert Space is a vector space equipped with a scalar product. There are two crucial observations underlying the so-called Kernel Trick:

* The vector $\theta_{t}$ maintained by SVM (and Perceptron) is always a linear combination of vectors of the form $\psi(x_{1}),...,\psi(x_{n})$. (This is known as the **Representer Theorem**). Therefore all the optimization procedure lives in this $n$-dimensional subspace. We only need to maintain the $n$ coordinates $\alpha_{1}^{t},...,\alpha_{n}^{t}$ in memory, that identify $\theta_{t}=\sum_{i=1}^{n}\alpha_{i}^{t}\psi(x_{i})$.
* We actually do not need to know exactly $\theta_{t}$, but only to be able to compute scalar products of the type $\langle\psi(x_{j}),\theta_{t}\rangle$ (for prediction) and update the $\alpha_{i}$.

$$
\langle\psi(x_{j}),\theta_{t}\rangle=\left\langle\psi(x_{j}),\sum_{i=1}^{n}\alpha_{i}^{t}\psi(x_{i})\right\rangle=\sum_{i=1}^{n}\alpha_{i}^{t}\langle\psi(x_{j}),\psi(x_{i})\rangle.
$$

Therefore, at the end of the day, we only need to maintain in memory the $n$ coordinates of $\theta_{t}$ (the $\alpha_{i}$'s), and be able to compute the so-called kernel matrix $K$ whose generic element is $K(x_{i},x_{j})=\langle\psi(x_{i}),\psi(x_{j})\rangle$. This $K(x_{i},x_{j})$ is the "kernel function".

**Example 2.4 (Polynomial Kernel).** Imagine $d=1$, and we consider the feature maps $\psi(x)=(1,x,x^{2},...,x^{D})$. The target space is $\mathbb{R}^{D+1}$ and the scalar product becomes $\langle \psi(x), \psi(z) \rangle$. A more general polynomial kernel is $K(x,z)=(x^{T}z+c)^{D}$.

**Example 2.5 (Gaussian Kernel).** The dimension of the input space is $d$, we can map the points to an infinite dimensional vector space whose scalar product is computed as follows:

$$
K(x,z) = \langle \psi(x), \psi(z)\rangle=e^{-||x-z||^{2}/(2\sigma^{2})}
$$

This type of Kernel is called Gaussian or Radial Basis Function (RBF) Kernel.