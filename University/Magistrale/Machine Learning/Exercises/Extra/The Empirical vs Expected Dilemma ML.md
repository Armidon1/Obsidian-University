Questa è una domanda eccellente che tocca il cuore del Machine Learning teorico.

La risposta breve è: **Usiamo il Rischio Empirico perché non possiamo calcolare il Rischio Atteso.**

Il Rischio Atteso è ciò che _vogliamo_ minimizzare (la generalizzazione), ma il Rischio Empirico è l'unica cosa che _possiamo_ minimizzare (i dati che abbiamo).

Ecco una nota per **Obsidian** che spiega questo dilemma fondamentale, basandosi specificamente sulle fonti e.

---

# 2.1.3 Concept: The Empirical vs. Expected Dilemma

You asked: _Why do we minimize Empirical Risk instead of Expected Risk?_

The answer lies in the distinction between "The Map" (our data) and "The Territory" (reality).

## 1. The Problem: The Unknowable Distribution

To calculate the **Expected Risk** $R(\theta)$, we would need to calculate the weighted average of errors over **all possible data points** that exist in the universe, weighted by their true probability.

$$ R(\theta) = \mathbb{E}[(Y - \phi(X)^T \theta)^2] $$

To solve this, we would need access to the true data distribution $D$.

- **Source:** _"Since we do not have access to the distribution D, we are using the n samples as a proxy for it!"_
- **Source:** _"Important: The last Proposition tells us that in order to minimize the expected risk under the linear assumption it is enough to know the vector $\theta^*$. Clearly, such vector is unknown, so we need to estimate it from data."*

In simple terms: We cannot do the math for Expected Risk because we are "blind" to the true mechanics of the world ($\theta^*$ and distribution $D$).

## 2. The Solution: The Empirical Proxy

Since we cannot see the whole universe, we look at the snapshot we have: our training dataset of $n$ samples. We calculate the **Empirical Risk** (the simple average error on our $n$ points) and minimize that instead.

$$ \hat{R}(\theta) = \frac{1}{n} \sum_{i=1}^{n} (y_i - \phi(x_i)^T \theta)^2 $$

We treat the Empirical Risk as a **proxy** (a substitute) for the Expected Risk.

- **Assumption:** If our sample size $n$ is large enough (Law of Large Numbers), the "simple mean" of our data (Empirical) will be very close to the "weighted mean" of reality (Expected).

## 3. Does it work? (The Guarantee)

By minimizing the Empirical Risk, we find the estimator $\hat{\theta}$. Does this actually help us find the true optimal parameters $\theta^*$?

Yes, under the Linear Assumption, we have statistical guarantees (Source):

1. **Unbiased:** On average, minimizing Empirical Risk leads us exactly to $\theta^*$ ($\mathbb{E}[\hat{\theta}] = \theta^*$).
2. **Convergence:** As $n \to \infty$, our empirical estimate becomes more and more precise (Variance decreases).

## Summary

- **Goal:** Minimize Expected Risk (Perform well on new data).
- **Obstacle:** We don't know the future data or the true distribution.
- **Strategy:** Minimize Empirical Risk (Perform well on past data) and rely on statistics to guarantee that this generalizes to the future.

---

Tutto chiaro? Se vuoi, possiamo passare ad analizzare come questa strategia possa fallire se ci fidiamo _troppo_ dei dati empirici (introducendo il concetto di **Overfitting**, che vedremo nella Week 3).