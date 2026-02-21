# Week 6: Statistical Learning and Tree Predictors

**Instructor:** Dr. Federico Fusco **Date:** November 4, 2025 - version 1

## 1 Generalization Bounds

Our goal is to provide a mathematical framework for the overfitting phenomenon. From previous weeks, we have the high-level intuition that "more complex" models require more data to achieve the same performance on the test data. This perspective is provided by the so-called **Generalization Bounds**, which quantify the number of samples required to ensure that the expected risk of all the classifiers is well estimated by the corresponding empirical risk. In these notes, we focus on binary classification, i.e., the label set $\mathcal{Y}$ is only composed of two labels (${0, 1}$ or ${-1, 1}$, depending on the context), but similar results can also be achieved for multi-class classification and regression.

Assume that we have access to $n$ i.i.d. samples from a distribution $\mathcal{D}$ over $\mathcal{X} \times \mathcal{Y}$, and we are focusing on a specific family $\mathcal{H}$ of classifiers. For each $h \in \mathcal{H}$, we use the empirical risk $\hat{R}$ to estimate the expected risk $R$. Stated differently, we are using the training set (i.e., the $n$ i.i.d. samples) to make predictions on unseen samples (i.e., the test set).

$$ R(h) = \mathbb{E}_{(X,Y)\sim\mathcal{D}} [\ell(h(X), Y)], \quad \hat{R}(h) = \frac{1}{n} \sum_{i=1}^n \ell(h(x_i), y_i). $$

We would like to argue that for all classifiers $h \in \mathcal{H}$, it holds that $\hat{R}(h) \approx R(h)$.

### 1.1 Mathematical Preliminaries

We start by recalling some fundamental results from probability theory: union bound and Chernoff inequality.

**Theorem 1.1 (Union Bound).** Given events $A_1, \dots, A_k$, then $$ \mathbb{P}(A_1 \cup \dots \cup A_k) \le \sum_i \mathbb{P}(A_i). $$

**Theorem 1.2 (Chernoff Bound).** Let $Z_1, \dots, Z_n$ be $n$ independent and identically distributed Bernoulli random variables, with probability of success $\mu$. Denote with $\hat{Z}$ the average of the $n$ random variables, and denote with $\epsilon$ a precision parameter. We have the following: $$ \mathbb{P}(|\hat{Z} - \mu| > \epsilon) \le 2e^{-2\epsilon^2 n} $$

### 1.2 Finite Families of Classifiers

When the family of classifiers we are considering is finite, then we have the following simple result.

**Theorem 1.3.** Let $\epsilon \in (0, 1)$ be a fixed precision parameter. Consider a finite family of classifiers $\mathcal{H}$, if we have $n$ i.i.d. samples, we get the following: $$ \mathbb{P}\left( \sup_{h \in \mathcal{H}} |R(h) - \hat{R}(h)| > \epsilon \right) \le 2|\mathcal{H}|e^{-2\epsilon^2 n} $$

**Proof.** Denote with $E_h$ the clean event for the generic classifier $h \in \mathcal{H}$ as follows: $$ E_h = { |R(h) - \hat{R}(h)| \le \epsilon }. $$ The event that we are trying to control, namely that for any $h \in \mathcal{H}$ the risk is well approximated, corresponds to the intersection over all $h$ of the clean events. Namely, we have the following:

$$ \mathbb{P}\left( \sup_{h \in \mathcal{H}} |R(h) - \hat{R}(h)| > \epsilon \right) = \mathbb{P}\left( \bigcup_{h \in \mathcal{H}} E_h^c \right) $$ $$ \le \sum_{h \in \mathcal{H}} \mathbb{P}(E_h^c) \quad \text{(By Union Bound, see Theorem 1.1)} $$ $$ \le 2|\mathcal{H}|e^{-2\epsilon^2 n} \quad \text{(By Chernoff Bound, see Theorem 1.2)} $$

The above inequality relates the precision parameter $\epsilon$ and the number of samples $n$ with the failure probability. In particular, if we fix the precision $\epsilon$ and the tolerated probability of failure $\delta \in (0, 1)$, we get the following, more explicit result.

**Corollary 1.4.** If $$ n \ge \frac{1}{2\epsilon^2} \ln \left( \frac{2|\mathcal{H}|}{\delta} \right), $$ then the probability of error is at most $\delta$.

> **Important** It is crucial to understand the randomness involved in the statement of the theorem: we consider the $n$ i.i.d. samples, and we argue that, with probability at least $1 - \delta$ with respect to these samples, the expected performance on a _new_ sample is $\epsilon$-approximated by the empirical performance on the $n$ initial samples.

### 1.3 Infinite Families of Classifiers: The VC Dimension

Although direct, the result for finite families is fairly unsatisfactory, as meaningful families of classifiers are typically infinite (e.g., linear classifiers). Luckily, there is a simple combinatorial notion that characterizes the families for which something similar to Theorem 1.3 can be obtained.

**Definition 1.5 (Shattering).** Given a set $S$ of points ${x_1, \dots, x_{|S|}}$, we say that family $\mathcal{H}$ shatters $S$, if $\mathcal{H}$ can realize any labeling of $S$: for any set of labels ${y_1, \dots, y_{|S|}} \in {0, 1}^{|S|}$, there exists $h \in \mathcal{H}$ such that $h(x_i) = y_i$ for all $x_i \in S$.

**Definition 1.6 (VC Dimension).** Given a hypothesis class $\mathcal{H}$, we define its Vapnik-Chervonenkis (VC) dimension as the size of the largest set that is shattered by $\mathcal{H}$. If $\mathcal{H}$ can shatter arbitrarily large sets, then the VC dimension is set to infinity.

We then have the following result, which is arguably the most important theorem in learning theory. The proof is omitted, but can be found in Chapter 14.5 of Mitzenmacher and Upfal or Chapter 6 of Shalev-Shwartz and Ben-David .

**Theorem 1.7.** Let $\epsilon \in (0, 1)$ be a fixed precision parameter, and $\delta \in (0, 1)$ be the tolerated probability of error. Consider a family of classifiers $\mathcal{H}$ with VC dimension $d$, if we have $n$ i.i.d. samples, with $$ n \in \Omega \left( \frac{d \log(1/\epsilon) + \log(1/\delta)}{\epsilon^2} \right) $$ we get the following: $$ \mathbb{P}\left( \sup_{h \in \mathcal{H}} |R(h) - \hat{R}(h)| > \epsilon \right) \le \delta. $$

> **Note** The way of looking at the Theorem is as follows: given a precision $\epsilon$ and a tolerated probability of error $\delta$, it tells how many samples are needed to $\epsilon$-approximate the risk of all classifiers in $\mathcal{H}$. In particular, this number scales linearly with the VC dimension.

**Example 1.8.** The VC dimension of intervals is 2. **Example 1.9.** The VC dimension of axis-aligned rectangles in $\mathbb{R}^2$ is 4. **Example 1.10.** The VC dimension of triangles in $\mathbb{R}^2$ is 7. **Example 1.11.** The VC dimension of a finite family of classifiers is $\log |\mathcal{H}|$. We therefore have that Theorem 1.3 is a special case of Theorem 1.7.

> **Important** It is surprising that a combinatorial quantity such as the VC dimension characterizes a probabilistic property. Note, the VC dimension does characterize learnability; indeed, for any family with unbounded VC dimension, we cannot guarantee the same bounds as in Theorem 1.3 or Theorem 1.7: there will always be some classifiers whose risk is not well estimated!

### 1.4 Risk Decomposition

We can now provide a mathematically satisfactory exposition of overfitting, at least for the special case of binary classification. Let $h^*$ denote the Bayes optimal classifier, and let $\mathcal{H}$ be any fixed family of classifiers. We can decompose the expected risk of a generic classifier $h \in \mathcal{H}$ as follows:

$$ R(h) = \underbrace{R(h^*)}_{\text{Bayes Error}} + \underbrace{\left( \inf_{h \in \mathcal{H}} R(h) - R(h^*) \right)}_{\text{Bias given by class } \mathcal{H}} + \underbrace{\left( R(h) - \inf_{h \in \mathcal{H}} R(h) \right)}_{\text{Estimation Error}}. $$

We analyze separately the three terms:

- The first term of this decomposition is the **Bayes Error**, i.e., the risk of the best classifier. This error is a priori non-zero, and there is nothing we can do to reduce it.
- The second term is the "discretization" error that we incur by restricting our attention to the family $\mathcal{H}$. It only depends on the choice of the family $\mathcal{H}$, and is not affected directly by the number of samples, nor by how we pick the classifier $h$.
- The third error is the risk of $h$ with respect to the best classifier in $\mathcal{H}$. We know that for all classifiers in $\mathcal{H}$, the empirical risk $\hat{R}$ is a good estimate of $R$, up to an error that is quantified in Theorem 1.7. Denote with $h^*_{\mathcal{H}}$ the best classifier in $\mathcal{H}$, we get $$ R(h) - R(h^*_{\mathcal{H}}) \le \hat{R}(h) - \hat{R}(h^*_{\mathcal{H}}) + O\left( \sqrt{\frac{d \log n/d + \log 1/\delta}{n}} \right) $$ In particular, if we let $h$ to be the best classifiers on the samples (or nearly the best), then the above term is essentially $\sqrt{\frac{d \log n/d + \log 1/\delta}{n}}$, which only depends on the VC dimension $d$, the number of samples $n$, and the tolerated probability of error $\delta$.

> **Important** The trade-off when choosing the "right" family $\mathcal{H}$ of classifiers is clear: the more complex the class, i.e., the larger the VC dimension, the smaller the second term becomes, at the cost of a worse bound on the third term. Similarly, choosing a simple family $\mathcal{H}$ makes it easier to control the third term, while incurring a large discretization error.

## 2 Tree Predictors

Assume that the input space $\mathcal{X}$ is given by the product of $\mathcal{X}_1 \times \dots \times \mathcal{X}_d$, we consider the family of classifiers that can be represented by trees. A tree predictor is associated with a rooted tree whose internal nodes correspond to tests, while the leaves correspond to labels. To compute the label of $x \in \mathcal{X}$, we need to follow a root-to-leaves path, starting from the root, and following the outcomes of the tests. Typically, the tests only entail checking one dimension of $x$ at a time.

**Example 2.1.** Consider $\mathcal{X} =^2$ and the predictor tree that works as follows: if $x^{(1)} \ge 1/2$, then move left, otherwise go right. If right, then output label 1 if $x^{(2)} \ge 1/3$, and -1 otherwise. If left then output label 1 if $x^{(2)} \le 2/3$, and -1 otherwise.

In these notes, we focus on binary classification (the label set $\mathcal{Y}$ is ${-1, 1}$), and binary input $\mathcal{X} = {0, 1}^d$, and the 0-1 loss. The argument can be easily extended beyond the binary case and to more general losses. We also restrict our attention to binary tests (i.e., each internal node in the tree has exactly two children, depending on the binary outcome of the test).

### 2.1 Training a Tree Predictor

Consider a generic tree predictor $h_T$, we want to evaluate its performance on the training set ${(x_1, y_1), \dots (x_n, y_n)}$. Following the structure of the tree predictor $h_T$, we can associate each one of the training points to a leaf $\ell$. Since our goal is to minimize the number of points that are misclassified, it makes sense to label a leaf with the label that is more frequent there. Denote with $N_\ell^+$, respectively $N_\ell^-$, the number of points in the training set that gets mapped to leaf $\ell$ and have label +1, respectively -1, then we label $\ell$ with +1 if $N_\ell^+ \ge N_\ell^-$, and with -1 otherwise. In particular, the number of errors in a given leaf is equal to the cardinality of the smallest class: $\min{N_\ell^+, N_\ell^-}$. All in all, the error of a tree predictor $h_T$ can be written as:

$$ \hat{R}(h_T) = \frac{1}{n} \sum_{\ell \text{ leaf}} \min\left{ \frac{N_\ell^+}{N_\ell}, \frac{N_\ell^-}{N_\ell} \right} N_\ell = \frac{1}{n} \sum_{\ell \text{ leaf}} \psi\left( \frac{N_\ell^+}{N_\ell} \right) N_\ell, $$

where $N_\ell$ denotes the number of points in leaf $\ell$, and the function $\psi(z)$ is simply $\min{z, 1-z}$. Tree predictors exhibit a crucial difference with respect to all the other machine learning models that we have studied: if we let the tree to grow arbitrarily deep, then we can typically set the error to 0!

**Theorem 2.2.** For any training set with distinct inputs, i.e., $x_i \ne x_j$ for any $i \ne j$, there exists a tree predictor that perfectly classifies all the points.

**Proof Sketch.** We can achieve this result by simply constructing a tree where each input point is contained in exactly one leaf, and then correctly labeling that leaf. This can be achieved in many ways; for instance, it is possible to "split" the dataset one coordinate at a time.

As you can imagine, such an approach wildly overfits on the training set, so we need an alternative perspective. The idea is to consider a good tree predictor that has at most $N$ nodes, where $N$ is the hyper-parameter that captures the complexity of the tree. Once we fix $N$, the goal becomes finding the best tree classifier with at most $N$ nodes on the given training set. While this problem can be solved optimally, we present here a well-known greedy algorithm that exhibits nice empirical performance. It works as follows: starting from a trivial tree with only one leaf, it recursively chooses a leaf, replaces it with a test node, and connects the two corresponding leaves. Terminating as soon as the tree has $N$ nodes. The algorithm works as follows:

**Training a Decision Tree**

- **Input:** Training data ${(x_i, y_i)}_{i=1}^n$, where $x_i \in \mathbb{R}^d, y_i \in {-1, +1}$
- **Hyperparameter:** Maximum number of nodes $N$
- Start with a single leaf that contains all the points
- **while** The decision tree has less than $N$ nodes **do**
    - Select a leaf $\ell$ that contains some misclassified points
    - Replace it with a test node, and two leaves $\ell_L$ and $\ell_R$
    - Move the points in $\ell$ to the two children, according to the outcome of the test

> **Note** The greedy algorithm that we have described is _not_ optimal, but performs reasonably well in practice.

Our goal is to find, given the training set, a tree predictor with "small" error. To this end, we make the following observation: if we start from a leaf and replace it with a test, then the training error cannot increase. Formally, if we split a leaf $\ell$ in two leaves $\ell_L$ and $\ell_R$, we get:

$$ \underbrace{\psi\left( \frac{N_\ell^+}{N_\ell} \right) N_\ell}_{\text{contribution of } \ell} = \psi\left( \frac{N_{\ell_L}^+ + N_{\ell_R}^+}{N_\ell} \right) N_\ell \ge \underbrace{\psi\left( \frac{N_{\ell_L}^+}{N_{\ell_L}} \right) N_{\ell_L}}_{\text{contribution of } \ell_L} + \underbrace{\psi\left( \frac{N_{\ell_R}^+}{N_{\ell_R}} \right) N_{\ell_R}}_{\text{contribution of } \ell_R} $$

where in the inequality, we use that the function $\psi$ is concave.

**Remark 2.3.** The function $\psi(z) = \min{z, 1-z}$ may be problematic, as it could result in a non-decrease in the loss. Consider the instance where $N_\ell^+ / N_\ell = 0.8$, $N_{\ell_L}^+ / N_{\ell_L} = 0.6$, $N_{\ell_R}^+ / N_{\ell_R} = 1$, and $N_{\ell_L} / N_\ell = 2$ (sic).

Therefore, there are other choices of function $\psi$ as "surrogate" of $\min{z, 1-z}$, and are used to choose which leaf to split and how to perform the split:

- **Gini index:** $\psi_G(z) = 2z(1-z)$
- **Scaled Entropy:** $\psi_e(z) = -z \log_2 z - (1-z) \log_2 (1-z)$

> **Important** A fantastic feature of trees is that they are easy to interpret.

### 2.2 The VC dimension of tree predictors

We can use the notion of VC dimension to formalize our intuition about the complexity of tree predictors. In particular, let $\mathcal{T}$ be the family of all tree predictors; it is a simple exercise to argue that it has infinite VC dimension. Indeed, given any disjoint $n$ points, we can always find a tree deep enough that maps each point to a leaf, and thus can shatter the $n$ points. On the other hand, the tree classifiers on $N$ nodes $\mathcal{T}_N$ are finitely many, so it is possible to learn all such classifiers with enough samples (by Theorem 1.3).

**Proposition 2.4.** Consider the family $\mathcal{T}_N$ of all the tree predictors on trees of $N$ nodes, then $|\mathcal{T}_N| \le (2de)^N$.

**Proof.** The cardinality of $\mathcal{T}_N$ is smaller than the product of: the number of binary trees with $N$ nodes (this specifies the topology of the underlying tree), the number of ways of assigning binary tests to the internal nodes, and the number of ways of assigning binary labels to the leaves. If the tree has $M$ internal nodes, then there are $d^M$ ways of assigning tests to internal nodes (there are $d$ dimensions), and $2^{N-M}$ ways of assigning the labels to the leaves. All in all, each tree of $N$ nodes can implement up to $2^{N-M} d^M \le d^N$ classifiers. Finally, the number of complete binary trees is given by the following formula: $$ \frac{2^N}{N+1} \binom{N-1}{\frac{N-1}{2}} \le 2^N \left( \frac{2e}{N-1} \right)^{\frac{N-1}{2}}, $$ where in the second inequality we use the Stirling approximation, which implies that $\binom{n}{k} \le (ne/k)^k$. All in all, we get: $|\mathcal{T}_N| \le (2ed)^N$.

The Proposition tells us that the number of samples needed to get good estimates scales linearly in $N$, and only logarithmically in the dimension of the input space $d$.

### 2.3 Random Forests

There is a powerful way of combining tree predictors into a unique better predictor, called Random Forests. Such an approach consists in instantiating multiple short tree predictors, trained on different subsets of the same training set. Each tree is associated with a weight, and the final prediction is determined by the weighted majority of the predictions from the individual trees.

## 3 Pointers

The main reference for generalization bounds and VC dimension is Shalev-Shwartz and Ben-David . We also refer to Mitzenmacher and Upfal for a more probabilistic approach, and to Ng for a more practical one. Regarding Tree Predictors and Random Forests, we refer to Chapter 6 of Géron for a more practical approach, and to Chapter 18 of Shalev-Shwartz and Ben-David and to the notes by Cesa-Bianchi for a more theoretical perspective.