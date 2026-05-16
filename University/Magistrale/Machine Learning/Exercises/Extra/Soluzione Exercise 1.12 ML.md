Questo è l'esercizio che formalizza il **Gaussian Naive Bayes**, uno dei classificatori più usati (ad esempio per filtrare lo spam).

È molto meno spaventoso di quanto sembri. La chiave è, ancora una volta, usare il trucco del "mondo congelato" (fissare $Y=j$) e sfruttare l'indipendenza.

### 1. L'Obiettivo

Come abbiamo visto per l'esercizio 1.10, con la **0-1 Loss** (classificazione), il predittore ottimo $f^*(x)$ è quello che sceglie la classe con la **probabilità a posteriori massima** (Maximum A Posteriori - MAP):

$$ f^*(x) = \operatorname*{argmax}_{j \in {1, \dots, k}} P(Y=j \mid X=x) $$

### 2. Teorema di Bayes

Non conosciamo $P(Y|X)$ direttamente, ma conosciamo le distribuzioni delle feature dato $Y$ (le Gaussiane). Usiamo Bayes:

$$ P(Y=j \mid X=x) = \frac{P(X=x \mid Y=j) \cdot P(Y=j)}{P(X=x)} $$

Poiché il denominatore $P(X=x)$ è uguale per tutte le classi $j$, possiamo ignorarlo nella massimizzazione. Ci concentriamo sul numeratore: $$ \text{argmax}_j ; [ P(X=x \mid Y=j) \cdot P(Y=j) ] $$

### 3. L'Assunzione "Naive" (Indipendenza)

Il testo dice che, dato $Y=j$, le componenti $X_1, \dots, X_d$ sono **indipendenti**. Questo significa che la probabilità congiunta è il **prodotto** delle probabilità singole:

$$ P(X=x \mid Y=j) = \prod_{i=1}^{d} P(X_i=x_i \mid Y=j) $$

### 4. Sostituzione delle Gaussiane

Il testo dice che ogni $X_i$ (dato $j$) è una Gaussiana $N(\mu_i^j, \sigma_i^j)$. La densità è: $$ P(X_i=x_i \mid Y=j) = \frac{1}{\sqrt{2\pi}\sigma_i^j} \exp\left( -\frac{(x_i - \mu_i^j)^2}{2(\sigma_i^j)^2} \right) $$

Sostituendo tutto nella formula del punto 2, otteniamo il predittore ottimo "grezzo":

$$ f^*(x) = \operatorname*{argmax}_{j} \left( P(Y=j) \cdot \prod_{i=1}^{d} \frac{1}{\sqrt{2\pi}\sigma_i^j} e^{-\frac{(x_i - \mu_i^j)^2}{2(\sigma_i^j)^2}} \right) $$

### 5. Il Risultato "Pulito" (Log-Trick)

In Machine Learning, per evitare di moltiplicare numeri piccolissimi (e far esplodere il computer), si applica il **Logaritmo**. Essendo una funzione crescente, non cambia il punto di massimo, ma trasforma i prodotti in somme.

$$ \ln(\text{Posterior}) = \ln(P(Y=j)) + \sum_{i=1}^d \ln\left( \frac{1}{\sqrt{2\pi}\sigma_i^j} \right) + \sum_{i=1}^d \left( -\frac{(x_i - \mu_i^j)^2}{2(\sigma_i^j)^2} \right) $$

Eliminando le costanti (come $\sqrt{2\pi}$) che non dipendono da $j$, otteniamo la forma finale usata negli algoritmi:

$$ f^*(x) = \operatorname*{argmax}_{j} \left[ \ln(P(Y=j)) - \underbrace{\sum_{i=1}^d \ln(\sigma_i^j)}_{\text{Penalità varianza}} - \underbrace{\sum_{i=1}^d \frac{(x_i - \mu_i^j)^2}{2(\sigma_i^j)^2}}_{\text{Distanza pesata}} \right] $$

### Interpretazione Intuitiva

Il predittore calcola un punteggio per ogni classe $j$ e sceglie la migliore. Il punteggio è composto da:

1. **Prior:** Quanto è probabile la classe $j$ a priori? (es. "è raro avere il cancro").
2. **Distanza:** Quanto il dato $x$ è vicino al centro $\mu^j$ della classe? (pesato dalla varianza: se la varianza è alta, essere lontani "costa meno").