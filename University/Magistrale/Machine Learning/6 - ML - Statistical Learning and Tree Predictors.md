For the original source (important for the prof's theorem's proofs, see [[Original 6 ML|here]])

![[6_-_ML_-_Il_Paradosso_dell_Overfitting.mp4]]

---

# Week 6: Statistical Learning and Tree Predictors

## Part 1: Introduction to Generalization Bounds

The primary objective of this week's material is to establish a rigorous mathematical framework to explain the phenomenon of **overfitting**. From previous studies, you likely already possess the high-level intuition that models with greater complexity require a larger volume of data to achieve consistent performance on new, unseen test data. **Generalization bounds** provide the theoretical perspective necessary to formalize this intuition. Specifically, these bounds allow us to quantify the exact number of samples required to ensure that the error rate we observe on our training data (the empirical risk) is a reliable estimate of the model's true error rate on the general population (the expected risk). Although this text focuses on **binary classification**—where the labels $\mathcal{Y}$ are limited to ${0, 1}$ or ${-1, 1}$—it is important to note that these results can be extended to apply to multi-class classification and regression tasks as well.

![[Pasted image 20260220133936.png]]

To model this mathematically, we assume we have access to a dataset consisting of $n$ independent and identically distributed (i.i.d.) samples drawn from a data distribution $\mathcal{D}$ over the space $\mathcal{X} \times \mathcal{Y}$. We consider a specific hypothesis class (or family) of classifiers, denoted as $\mathcal{H}$. For any given classifier $h$ within this family ($h \in \mathcal{H}$), we utilize the **empirical risk**, denoted as $\hat{R}(h)$, as an estimator for the **expected risk**, $R(h)$. The expected risk represents the true average loss over the entire distribution, while the empirical risk is the average loss calculated strictly on our training samples: $$ \hat{R}(h) = \frac{1}{n} \sum_{i=1}^n l(h(x_i), y_i) $$ Our fundamental goal in this analysis is to demonstrate that for _all_ classifiers in our hypothesis class $\mathcal{H}$, the empirical risk is a close approximation of the true risk, such that $\hat{R}(h) \approx R(h)$.

---

## Part 2: Mathematical Preliminaries

Before we can prove that a model learns effectively, we need to recall two fundamental results from probability theory. These tools allow us to quantify how likely it is that our empirical observations (training error) deviate from the theoretical truth (test error).

### The Union Bound

![[Pasted image 20260221170728.png]]

The first tool is the **Union Bound** (also known as Boole's inequality). This theorem allows us to bound the probability that _at least one_ of a set of events occurs. Suppose we have a collection of events $A_1, A_2, \dots, A_k$. We want to know the probability of the union of these events, denoted as $P(A_1 \cup \dots \cup A_k)$. The Union Bound states that this probability is less than or equal to the sum of the probabilities of the individual events: $$ P\left(\bigcup_{i=1}^k A_i\right) \le \sum_{i=1}^k P(A_i) $$ In the context of machine learning, this is crucial when dealing with a finite hypothesis class. If "event $A_i$" represents a specific classifier $h_i$ failing to generalize well, the Union Bound helps us calculate the worst-case probability that _any_ classifier in our set fails.

### The Hoeffding / Chernoff Bound

![[Pasted image 20260221170833.png]]

The second, and perhaps more powerful tool for our purposes, is the **Hoeffding (or Chernoff) inequality**. This theorem addresses the law of large numbers: it tells us how quickly the empirical average of random variables converges to their true expected value.

Let $Z_1, \dots, Z_n$ be independent and identically distributed (i.i.d.) Bernoulli random variables (variables that take values 0 or 1), each with a true expected value (probability of success) $E[Z_i] = \mu$. Let $\hat{Z}$ be the empirical average of these variables calculated over $n$ samples: $$ \hat{Z} = \frac{1}{n} \sum_{i=1}^n Z_i $$ The theorem states that for any precision parameter $\epsilon > 0$, the probability that the empirical average $\hat{Z}$ deviates from the true mean $\mu$ by more than $\epsilon$ drops exponentially as the number of samples $n$ increases: $$ P(|\hat{Z} - \mu| > \epsilon) \le 2e^{-2\epsilon^2 n} $$ This result is incredibly important because it provides a tight bound on estimation error. In our learning framework, we will treat the loss of a classifier on a specific data point as a random variable $Z$. Consequently, this inequality guarantees that with enough data ($n$), the empirical risk $\hat{R}(h)$ will be very close to the true risk $R(h)$ with high probability.

---

## Part 3: Finite Families of Classifiers

Now that we have established the mathematical groundwork with the Union Bound and Hoeffding's inequality, we can address the core problem: guaranteeing the performance of a learned model. Specifically, we begin by considering the simplest case where our hypothesis class $\mathcal{H}$ is **finite**. This means there is a fixed, countable number of possible classifiers we can choose from, denoted as $|\mathcal{H}|$.

### The Problem of Selection

![[Pasted image 20260221171715.png]]
	
When we train a model, we typically select the classifier $\hat{h}$ that minimizes the empirical risk (training error) $\hat{R}(h)$. However, there is a danger here. Even if a classifier is terrible on the true distribution (high $R(h)$), it might—by pure chance—perform well on the specific random sample of data we collected. To trust our chosen model, we need to ensure that the training error is a good proxy for the test error for _all_ classifiers in our set simultaneously. If the empirical risk is close to the true risk for every $h \in \mathcal{H}$, then the classifier that minimizes the training error is guaranteed to be nearly optimal for the true distribution as well. This concept is known as **uniform convergence**.

In the language of a normal human being: **If every classifier has the empirical risk near to its own expected risk**, we are choosing the classifier that has the minimum empirical risk. If there is even **one** classifier in your hypothesis class H where the expected risk is distant from the empirical risk (specifically, if the empirical risk is low but the true risk is high), you run the risk of **overfitting**. In this scenario, we have to restrict the complexity of our classifier and accept a possible bias of the predictor.
### Applying the Bounds

![[Pasted image 20260221171738.png]]

To quantify this, we look for the probability that _at least one_ classifier in our set has a deceptive training error (deviating from its true error by more than $\epsilon$). Using the Union Bound, we can sum the probabilities of this bad event happening for each individual classifier. Since Hoeffding's inequality tells us the probability for a single classifier is at most $2e^{-2n\epsilon^2}$, the probability for _any_ of the $|\mathcal{H}|$ classifiers failing is bounded by: $$ P\left(\max_{h \in \mathcal{H}} |\hat{R}(h) - R(h)| > \epsilon\right) \le \sum_{h \in \mathcal{H}} 2e^{-2n\epsilon^2} = 2|\mathcal{H}|e^{-2n\epsilon^2} $$ This is a powerful result. It tells us that as long as the number of samples $n$ is large enough, the probability of _any_ model fooling us drops exponentially.

[[spiegazione ML 6.3.1|spiegotto]]

### Sample Complexity

![[Pasted image 20260221171907.png]]

We can invert this relationship to answer a practical question: **How much data do we need?** If we want to be confident (with probability $1-\delta$) that our training error is within $\epsilon$ of the true error, we can solve the inequality for $n$. By setting the right-hand side equal to $\delta$ and rearranging the terms, we derive the sample complexity bound: $$ n \ge \frac{1}{2\epsilon^2} \left( \ln |\mathcal{H}| + \ln \frac{2}{\delta} \right) $$ This equation reveals two critical insights about learning:

1. **Complexity cost:** The number of samples needed grows logarithmically with the size of the hypothesis class ($\ln |\mathcal{H}|$). This implies that adding more complexity to our model (increasing $|\mathcal{H}|$) requires more data, but the cost grows slowly.
2. **Precision cost:** The number of samples grows quadratically with the inverse of the precision ($1/\epsilon^2$). This means that if you want to halve your margin of error, you need four times as much data.

[[spiegazione H che cos'è ML 6.3.2|spiegazione che cos'è H]]


---

## Part 4: Infinite Families and the VC Dimension

The results we derived for finite hypothesis classes are mathematically sound but practically limited. In the real world, most hypothesis classes $\mathcal{H}$ are **infinite**. For example, consider a simple linear classifier in a continuous space: there are infinitely many possible lines (or hyperplanes) one could draw to separate data points. Since $|\mathcal{H}|$ is infinite, the term $\ln |\mathcal{H}|$ in our previous bound would be infinite, rendering the bound useless. To resolve this, we need a more sophisticated way to measure the "richness" or "complexity" of a model class that doesn't rely on simply counting the number of classifiers. This measure is the **Vapnik-Chervonenkis (VC) dimension**.

### The Concept of Shattering

![[Pasted image 20260223165639.png]]

To understand VC dimension, we first need to define the concept of **shattering**. Imagine a set of data points $S = {x_1, \dots, x_m}$. We say that a hypothesis class $\mathcal{H}$ **shatters** this set $S$ if $\mathcal{H}$ is capable of realizing _every possible_ labeling of these points. Since each of the $m$ points can be labeled either $0$ or $1$, there are $2^m$ possible combinations of labels. If, for every one of these $2^m$ combinations, you can find a classifier $h \in \mathcal{H}$ that assigns exactly those labels to the points in $S$, then $S$ is shattered by $\mathcal{H}$. Essentially, shattering means the model is powerful enough to "memorize" any pattern on that specific set of points.


>[!Abstract] Definizione Shattering
Dato un insieme finito di punti $S = {x_1, \dots, x_m}$ appartenenti allo spazio degli input $\mathcal{X}$, si dice che una famiglia di classificatori (o classe di ipotesi) $\mathcal{H}$ **shatter** (frantuma) l'insieme $S$ se $\mathcal{H}$ è in grado di realizzare **qualsiasi possibile etichettatura** di $S$.
>
In termini matematici, ciò significa che per ogni possibile sequenza di etichette binarie $(y_1, \dots, y_m) \in {0, 1}^m$ (ci sono $2^m$ combinazioni possibili), esiste almeno un classificatore $h$ all'interno della famiglia $\mathcal{H}$ tale che: $$ h(x_i) = y_i \quad \text{per tutti i punti } i = 1, \dots, m $$

#### Perché è importante?

Il concetto di shattering è il blocco costruttivo per definire la **Dimensione VC** (Vapnik-Chervonenkis), che è una misura della complessità (o capacità) di un modello:

- La **Dimensione VC** di $\mathcal{H}$ è definita come la dimensione del **più grande** insieme finito $S$ che $\mathcal{H}$ riesce a frantumare.
- Se una famiglia $\mathcal{H}$ può fare shattering di insiemi arbitrariamente grandi, allora la sua dimensione VC è infinita.

**Esempio pratico citato nelle fonti:** La famiglia di tutti gli **alberi decisionali** (senza restrizioni di profondità) ha una dimensione VC infinita. Questo perché, dato un qualsiasi insieme di punti distinti, è sempre possibile costruire un albero abbastanza profondo da isolare ogni singolo punto in una propria foglia, assegnandogli l'etichetta desiderata. Di conseguenza, questa famiglia può fare _shattering_ di qualsiasi dataset.

### Defining VC Dimension

![[Pasted image 20260223165703.png]]

The **VC dimension** of a hypothesis class, denoted as $\text{VC}(\mathcal{H})$, is defined as the **size of the largest finite set $S$ that $\mathcal{H}$ can shatter**.

- If $\mathcal{H}$ can shatter a set of size $d$, but cannot shatter _any_ set of size $d+1$, then $\text{VC}(\mathcal{H}) = d$.
- If $\mathcal{H}$ can shatter arbitrarily large sets, then $\text{VC}(\mathcal{H}) = \infty$.

It is crucial to note the precise logic here: to have a VC dimension of $d$, you only need to find _one_ specific configuration of $d$ points that can be shattered. You do not need to prove that _all_ sets of size $d$ are shatterable. Conversely, to show the dimension is _not_ $d+1$, you must prove that _no_ set of size $d+1$ exists that can be shattered.

Capisco perfettamente la tua difficoltà. Le definizioni formali di VC Dimension e "shattering" (frantumazione) sono spesso molto astratte.

Per chiarire i concetti, dimentichiamo per un attimo la matematica complessa e proviamo a **visualizzare concretamente** chi sono i protagonisti di questa storia: $\mathcal{H}$ e $S$.

#### 1. Chi è $S$? (I Punti sul Foglio)

Immagina $S$ non come un insieme astratto, ma come **un gruppo di punti disegnati su un foglio di carta**.

- Se $S$ ha dimensione 3 ($|S|=3$), hai disegnato **3 puntini** sul foglio in posizioni fisse.
- Questi punti non hanno ancora un colore (un'etichetta). Sono solo lì, fermi.

#### 2. Chi è $\mathcal{H}$? (Il Tuo Strumento di Disegno)

Immagina $\mathcal{H}$ come lo **strumento** o la **regola** che ti è permesso usare per separare questi punti.

- **Esempio 1: Linee Rette.** Se $\mathcal{H}$ è l'insieme dei classificatori lineari, il tuo strumento è un righello. Puoi tracciare una linea retta ovunque sul foglio. Tutto ciò che sta da una parte della linea diventa "Blu" (classe 1), tutto ciò che sta dall'altra diventa "Rosso" (classe 0).
- **Esempio 2: Rettangoli.** Se $\mathcal{H}$ è l'insieme dei rettangoli allineati agli assi, il tuo strumento è una cornice rettangolare. Ciò che è dentro è "Blu", ciò che è fuori è "Rosso".

#### 3. Cosa significa "Shattering" (Frantumare)?

Ora arriva il gioco. Hai i tuoi 3 punti fissi sul foglio ($S$). Io (il "diavolo" o l'avversario) decido come colorarli. Posso scegliere qualsiasi combinazione:

- Tutti rossi.
- Tutti blu.
- Il primo rosso, gli altri due blu.
- Eccetera. (Con 3 punti ci sono $2^3 = 8$ combinazioni possibili).

Dire che il tuo strumento $\mathcal{H}$ **"shattera"** (frantuma) questi 3 punti significa: **"Non importa come io colori questi 3 punti, tu riesci SEMPRE a trovare un modo per separarli correttamente usando il tuo strumento."**

- Se coloro il punto in alto Rosso e quello in basso Blu, riesci a mettere il righello in mezzo? Sì.
- Se li coloro tutti Blu, riesci a mettere il righello in modo che siano tutti dalla stessa parte? Sì.

Se riesci a farlo per **tutte** le 8 combinazioni possibili, allora hai "shatterato" quel set di 3 punti.

#### 4. La Dimensione VC (Il Punteggio Massimo)

La Dimensione VC è semplicemente il **record massimo** di punti che il tuo strumento riesce a gestire in questo modo.

- **Il caso delle Linee Rette (in 2D):**
    - Riesci a shatterare **3 punti**? Sì (purché non siano allineati, ma a noi basta trovarne _un_ gruppo posizionato bene).
    - Riesci a shatterare **4 punti**? Proviamo. Mettiamo 4 punti a forma di quadrato. Se io coloro quelli sulla diagonale (es. in alto a destra e in basso a sinistra) di Blu, e gli altri due di Rosso... **puoi separarli con UNA sola linea retta?**
    - **No.** È impossibile.
    - Risultato: Il tuo strumento "Linea Retta" vince con 3 punti, ma perde con 4. Quindi la sua **Dimensione VC è 3**.

#### Riepilogo Visuale

- **$S$**: I punti che mettiamo sul tavolo per sfidare il modello.
- **$\mathcal{H}$**: Le forme geometriche (linee, cerchi, rettangoli) che possiamo usare per dividere i punti.
- **Shattering**: La capacità di adattare la forma geometrica a _qualsiasi_ colorazione arbitraria dei punti.
- **VC Dimension**: Il numero massimo di punti per cui questo gioco riesce sempre. Se il gioco riesce con infiniti punti (come per gli alberi decisionali molto profondi), la dimensione è infinita e il modello rischia di imparare a memoria (overfitting) qualsiasi rumore.

### The Fundamental Theorem of Learning

![[Pasted image 20260223171921.png]]

This combinatorial measure connects directly to learnability. A famous theorem in statistical learning states that if a hypothesis class has a finite VC dimension $d$, it is learnable. The sample complexity—the number of samples $n$ required to guarantee that the empirical risk is within $\epsilon$ of the true risk with high probability ($1-\delta$)—scales linearly with $d$. Specifically, the bound is roughly: $$ n \ge C \frac{d \log(1/\epsilon) + \log(1/\delta)}{\epsilon^2} $$ where $C$ is a constant. This is the "infinite" analog to our previous finite bound. It tells us that the difficulty of learning a model depends not on the number of parameters or the number of classifiers, but on its "effective" complexity as measured by the VC dimension.

### Examples of VC Dimension

![[Pasted image 20260223165723.png]]

To make this concrete, consider these standard geometric examples:

- **Intervals on a line:** $\text{VC} = 2$. You can shatter 2 points with an interval, but you cannot shatter 3 (e.g., you cannot label the outer two points as "positive" and the middle one as "negative" with a single interval).
- **Axis-aligned rectangles in $\mathbb{R}^2$:** $\text{VC} = 4$. You can arrange 4 points in a diamond shape and label them any way you want with a rectangle, but no set of 5 points can be shattered.
- **Triangles in $\mathbb{R}^2$:** $\text{VC} = 7$.

---

## Part 5: Risk Decomposition and the Bias-Variance Tradeoff

With the concept of VC dimension established, we can now mathematically formalize the phenomenon of overfitting through **Risk Decomposition**. This framework allows us to break down the error of any classifier $h$ into three distinct components, helping us understand why simply choosing the most complex model is not always the best strategy.

### The Three Components of Error

Let $h^*$ denote the **Bayes optimal classifier**. This is the theoretical "perfect" classifier that knows the true probability distribution of the data. No model can ever perform better than $h^*$. Let $h^*_{\mathcal{H}}$ denote the best possible classifier within our specific hypothesis class $\mathcal{H}$ (the one we would choose if we had infinite data). Finally, let $h$ be the classifier we actually learned using our finite training set. We can decompose the excess risk as follows: $$ R(h) = \underbrace{R(h^*)}_{\text{Bayes Error}} + \underbrace{(R(h^*_{\mathcal{H}}) - R(h^*))}_{\text{Approximation Error (Bias)}} + \underbrace{(R(h) - R(h^*_{\mathcal{H}}))}_{\text{Estimation Error (Variance)}} $$

1. **Bayes Error (Irreducible):** This is the inherent noise in the problem. Even the perfect model makes mistakes if the data is ambiguous (e.g., two identical patients where one has a disease and the other doesn't). We cannot reduce this.
2. **Approximation Error (Bias):** This measures how limited our chosen family $\mathcal{H}$ is. If the true relationship is quadratic but we only use linear classifiers (low complexity), this error will be high. This is the "discretization" error caused by restricting ourselves to a specific family of models.
3. **Estimation Error (Variance):** This measures how far our learned model $h$ is from the best possible model in the class $h^*_{\mathcal{H}}$. This error arises because we have finite data and might be "fooled" by the training sample.

### The Tradeoff

This decomposition reveals the fundamental **Bias-Variance Tradeoff**, which is controlled by the complexity of $\mathcal{H}$ (its VC dimension $d$):

- **If we increase complexity (high $d$):** The Approximation Error decreases (we can fit more complex functions), but the Estimation Error increases (we need much more data to find the right model, scaling with $\sqrt{d/n}$).
- **If we decrease complexity (low $d$):** The Estimation Error decreases (it's easy to find the best simple model), but the Approximation Error increases (the model is too rigid to capture the truth).

Our goal is to choose a family $\mathcal{H}$ that balances these two competing errors for our specific sample size $n$.

---

## Part 6: Tree Predictors: Structure and Overfitting

![[Pasted image 20260224165115.png]]

We now shift our focus from abstract generalization bounds to a concrete algorithm: **Tree Predictors**. You can visualize a decision tree not just as a data structure, but as a method for recursively partitioning the input space $\mathcal{X}$ into smaller rectangular regions. Mathematically, we assume the input space decomposes into dimensions, such as $\mathcal{X} = \mathcal{X}_1 \times \dots \times \mathcal{X}_d$. A tree predictor is represented by a **rooted binary tree** where:

- **Internal nodes** represent logical **tests** on a specific coordinate of the input data (e.g., "Is $x^{(1)} \ge 0.5$?").
- **Leaves** contain the final **prediction** (the label $y$).

To classify a new data point $x$, you simply start at the root and follow the path determined by the test outcomes until you reach a leaf. The label assigned to that leaf is the model's prediction.

### The Infinite Power of Trees

A fundamental property of decision trees is their extreme flexibility. A key theorem states that for **any** training set with distinct inputs, there exists a tree predictor that can classify every single point correctly (achieving **zero training error**). The proof is intuitive: imagine growing a tree so deep that every single training point ends up in its own unique leaf. If you label that leaf with the true label of that point, you have perfectly memorized the dataset. While this sounds appealing, it is a textbook example of **overfitting**. A tree that isolates every training point has effectively "memorized" the noise in the data rather than learning the underlying structure. This implies that the class of _all_ possible trees has an infinite VC dimension, making it impossible to guarantee generalization without restrictions. To make trees useful, we must limit their complexity, typically by fixing a maximum number of nodes $N$.

---

## Part 7: Greedy Training and Impurity Measures

![[Alberi__Paradosso_Overfitting.mp4]]

![[Pasted image 20260224182739.png]]

Since finding the globally optimal decision tree of a fixed size $N$ is a computationally difficult problem, we rely on a **Greedy Algorithm** to approximate the best solution. The approach is "greedy" because at every step, it makes the locally optimal decision to reduce error without worrying about future consequences. The standard algorithm (similar to CART) operates as follows:

1. **Initialization:** Start with a trivial tree consisting of a single leaf that contains the entire training dataset.
2. **Iteration:** While the tree has fewer than $N$ nodes:
    - Select a leaf $\ell$ that currently contains misclassified points.
    - Replace this leaf with a new internal test node and two new children leaves, $\ell_L$ and $\ell_R$.
    - Distribute the data points from the original leaf into the two new leaves based on the outcome of the test (e.g., "Is $x^{(1)} \ge 0.5$?").
3. **Termination:** Stop when the node budget $N$ is reached.

### The Splitting Criterion

The core decision in this algorithm is choosing _which_ leaf to split and _what_ test to apply. We make this choice by minimizing a cost function. If we let $N_\ell$ be the total number of points in a leaf and $N_\ell^+$ be the count of positive samples (the label of that specific $x$ feature vector is $+1$), the empirical error of that leaf is $N_\ell \cdot \psi(N_\ell^+ / N_\ell)$, where $\psi(z) = \min(z, 1-z)$. When we split a leaf $\ell$ into left ($\ell_L$) and right ($\ell_R$) children, the total error will effectively decrease (or stay the same) if the impurity function $\psi$ is **concave**. Mathematically, this guarantees that: $$ N_\ell \psi\left(\frac{N_\ell^+}{N_\ell}\right) \ge N_{\ell_L} \psi\left(\frac{N_{\ell_L}^+}{N_{\ell_L}}\right) + N_{\ell_R} \psi\left(\frac{N_{\ell_R}^+}{N_{\ell_R}}\right) $$

### Surrogate Impurity Functions

While the standard misclassification error ($\min(z, 1-z)$) seems intuitive, it is often problematic for optimization because it is not strictly concave (it is "pointy"). This means a split might separate data but not strictly reduce the immediate classification error, causing the algorithm to get stuck. To fix this, we typically use smoother **surrogate** impurity functions that are strictly concave and encourage purer splits:

- **Gini Index:** $\psi_G(z) = 2z(1-z)$. This is the default in many libraries (like CART) and measures how often a randomly chosen element from the set would be incorrectly labeled.
- **Scaled Entropy:** $\psi_e(z) = -z \log_2 z - (1-z) \log_2 (1-z)$. This is based on information theory and measures the disorder in the leaf.

---

## Part 8: VC Dimension of Trees and Random Forests

We conclude our analysis by applying the VC dimension framework directly to decision trees. This allows us to understand theoretically why "pruning" (potatura) or limiting the size of a tree is necessary for generalization, and leads us to one of the most popular machine learning algorithms: Random Forests.

### The Complexity of Unrestricted Trees

As hinted earlier, the class of **all** possible binary decision trees (with unrestricted depth) has an **infinite VC dimension**. This is because, given any finite set of $m$ points with distinct feature values, we can always construct a tree that is deep enough to assign each point to its own unique leaf. Once isolated, we can label each leaf to match the specific labels of the points exactly. Since this can be done for _any_ possible labeling of the points, the class shatters datasets of arbitrary size. Consequently, without restrictions, we cannot derive a meaningful generalization bound using the standard VC theorems; the model is simply too powerful and prone to massive overfitting.

### Bounded Trees and Sample Complexity

To ensure learnability, we must restrict the hypothesis class. We typically do this by fixing a hyperparameter $N$, which represents the **maximum number of nodes** allowed in the tree. Let $\mathcal{T}_N$ denote the family of all binary tree predictors with at most $N$ nodes operating on a $d$-dimensional input space. Unlike the unrestricted case, $\mathcal{T}_N$ is a **finite** set. We can mathematically bound its size (cardinality) by counting the number of possible tree structures (topology), the number of possible tests at internal nodes, and the possible labels at the leaves. A useful proposition states that the size of this class is bounded roughly by: $$ |\mathcal{T}_N| \le (C \cdot d)^N $$ where $C$ is a constant (e.g., $8$ or $2e$). Using our previous results for finite hypothesis classes, this implies that the **sample complexity** (the number of training examples $n$ needed) scales **linearly with the number of nodes $N$** and only **logarithmically with the input dimension $d$**. This confirms that simpler trees (smaller $N$) generalize better with less data, while complex trees require significantly more data to avoid overfitting.

### Random Forests: Reducing Variance

While single decision trees are easy to interpret, they suffer from **high variance**: small changes in the training data can result in a completely different tree structure. To mitigate this, we use **Random Forests**. A Random Forest is an **ensemble** method that trains multiple "short" or simple trees, rather than a single complex one. The key idea involves two levels of randomness:

1. **Bagging (Bootstrap Aggregation):** Each tree is trained on a different random subset of the data (sampled with replacement).
2. **Feature Randomness:** (Often used) At each split, the algorithm only considers a random subset of features rather than all $d$ dimensions.

Once trained, the forest makes a prediction by taking a **majority vote** (or weighted average) of the predictions from all individual trees. By averaging many independent (or loosely correlated) models, the forest significantly **reduces the estimation error (variance)** without substantially increasing the bias, leading to robust generalization performance that often surpasses that of any single tree.

---
