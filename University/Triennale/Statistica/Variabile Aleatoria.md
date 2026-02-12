# Random Variable

> [!abstract] Definizione 
> Una **Variabile Aleatoria (V.A.)** $X$ è una funzione che associa un numero reale a ogni esito di uno spazio campionario $S$ di un esperimento casuale.
> 
> $$X: S \to \mathbb{R}$$

## Classificazione

- **Discrete:** Assumono un insieme numerabile di valori (es. numero di teste in n lanci).
    
- **Continue:** Assumono valori in un intervallo continuo di $\mathbb{R}$.
    

---

## Funzioni Caratteristiche

### 1. Funzione di Ripartizione (CDF)

Definisce la probabilità che la variabile assuma un valore minore o uguale a $x$:

$$F(x) = P(X \le x)$$

### 2. Funzione di Massa (PMF) - _Solo discrete_

Definisce la probabilità che la variabile assuma esattamente il valore $a$:

$$p(a) = P(X = a)$$

### 3. Densità di Probabilità (PDF) - _Solo continue_

Per le variabili continue, la probabilità di un singolo punto è 0. Si calcola la probabilità in un intervallo tramite integrale.

$$P(a \le X \le b) = \int_{a}^{b} f(x) dx$$

---

## Valori Sintetici

I parametri principali per descrivere una V.A. sono:

|**Parametro**|**Simbolo**|**Formula (Discreta)**|**Proprietà notevole**|
|---|---|---|---|
|**Valore Atteso** (Media)|$E[X]$ o $\mu$|$\sum x \cdot P(X=x)$|Lineare: $E[aX+b] = aE[X]+b$|
|**Varianza**|$Var(X)$ o $\sigma^2$|$E[(X-\mu)^2] = E[X^2] - (E[X])^2$|$Var(aX+b) = a^2 Var(X)$|

---

## Distribuzioni Notevoli (Cheat Sheet)

Discrete

|**Distribuzione**|**Notazione**|**PMF P(X=k)**|**Media E[X]**|**Varianza Var(X)**|**Descrizione**|
|---|---|---|---|---|---|
|**Bernoulli**|$B(p)$|$p^k(1-p)^{1-k}$|$p$|$pq$|Singola prova (successo/fallimento).|
|**Binomiale**|$Bin(n,p)$|$\binom{n}{k}p^k q^{n-k}$|$np$|$npq$|Somma di $n$ prove Bernoulli indipendenti.|
|**Poisson**|$Poi(\lambda)$|$\frac{e^{-\lambda}\lambda^k}{k!}$|$\lambda$|$\lambda$|Eventi rari in un intervallo di tempo/spazio.|
|**Geometrica**|$Geom(p)$|$p(1-p)^{k-1}$|$\frac{1}{p}$|$\frac{1-p}{p^2}$|Prove necessarie per il primo successo.|
|**Ipergeometrica**|$H(N,m,n)$|(vedi pag 8)|$\frac{nm}{N}$|(complessa)|Estrazione _senza_ reinserimento.|

> [!tip] Relazione Poisson-Binomiale 
> Se $n$ è molto grande e $p$ molto piccolo, la Binomiale può essere approssimata da una Poisson con $\lambda = np$.
> 


Continue

**[[Gaussian]] $N(\mu, \sigma^2)$**

La distribuzione più importante, a forma di campana simmetrica rispetto alla media $\mu$.

- **PDF:** $f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$
    
- **Normale Standard ($Z$):** È una normale con $\mu=0$ e $\sigma^2=1$. Si ottiene standardizzando:
    
    $$Z = \frac{X - \mu}{\sigma}$$
    
    I valori si calcolano usando le tavole della funzione $\Phi(z)$.
    

---

## Teoremi Fondamentali

### Disuguaglianze

Servono a limitare le probabilità quando non si conosce la distribuzione esatta.

- **Markov:** Per V.A. non negative, $P(X \ge a) \le \frac{E[X]}{a}$.
    
- **Chebyshev:** $P(|X - \mu| \ge r) \le \frac{\sigma^2}{r^2}$.
    

### Teoremi Limite

1. **Legge Debole dei Grandi Numeri:** La media campionaria di una successione di V.A. i.i.d. tende alla media vera $\mu$ al crescere di $n$.
    
2. **Teorema del Limite Centrale (TLC):** La somma di un numero elevato di V.A. indipendenti e identicamente distribuite tende ad avere una distribuzione **Normale** $N(n\mu, n\sigma^2)$, indipendentemente dalla distribuzione originale.
    

---

## Variabili Aleatorie Congiunte

Considerando due variabili $X$ e $Y$:

- **Indipendenza:** $P(X \cap Y) = P(X)P(Y)$.
    
- **Covarianza:** Misura la tendenza di due variabili a variare insieme.
    
    $$Cov(X,Y) = E[XY] - E[X]E[Y]$$
    
- **Correlazione ($\rho$):** Versione normalizzata della covarianza, valori tra $[-1, 1]$.
    
    $$Corr(X,Y) = \frac{Cov(X,Y)}{\sigma_X \sigma_Y}$$
    

---
