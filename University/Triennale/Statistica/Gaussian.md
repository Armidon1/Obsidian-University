# Distribuzione Normale (Gaussiana)

> [!abstract] Definizione 
> La **Distribuzione Normale** (o Gaussiana) è la distribuzione continua più importante in statistica. È caratterizzata da una curva a forma di campana, simmetrica rispetto al suo valore atteso.
> 
Si indica con $X \sim N(\mu, \sigma^2)$.

## Funzione di Densità di Probabilità (PDF)

La formula analitica della densità è:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

_dove:_

- $\mu = E[X]$ è il **Valore Atteso** (centro della simmetria).
    
    
- $\sigma^2 = Var(X)$ è la **Varianza** (indica la dispersione dei dati).
    

---

## Proprietà Fondamentali

1. **Simmetria:** La curva è perfettamente simmetrica rispetto a $x = \mu$. In questo punto la funzione raggiunge il suo massimo.
    
2. **Forma:**
    
    - Al variare di $\mu$, la curva trasla lungo l'asse x.
        
    - Al variare di $\sigma$, la curva cambia forma: più $\sigma$ è piccolo, più la campana è stretta e alta; più è grande, più è piatta e larga.
        
3. **Linearità:** Se $X$ è gaussiana, ogni sua trasformazione lineare $Y = aX + b$ è ancora una gaussiana con $E[Y] = a\mu + b$ e $Var(Y) = a^2\sigma^2$.
    
4. **Riproducibilità:** La somma di variabili normali indipendenti è ancora una variabile normale.
    

---

## Normale Standard ($Z$)

Poiché l'integrale della normale non è risolvibile analiticamente, si usa una variabile standardizzata per consultare le tavole.

> [!info] Standardizzazione
> 
> $$Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$$
> 
> Dove $\mu=0$ e $\sigma^2=1$.
> 


### Calcolo delle Probabilità

La Funzione di Ripartizione della normale standard è indicata con $\Phi(z)$.

$$P(X \le b) = \Phi\left(\frac{b-\mu}{\sigma}\right)$$

Per calcolare la probabilità in un intervallo $(a, b)$:

$$P(a < X < b) = \Phi\left(\frac{b-\mu}{\sigma}\right) - \Phi\left(\frac{a-\mu}{\sigma}\right) = \Phi(z_b) - \Phi(z_a)$$


> [!tip] Uso delle Tavole (Simmetria)
> 
> Le tavole spesso riportano solo valori positivi di $z$. Per valori negativi si usa la proprietà di simmetria:
> 
> $$\Phi(-z) = 1 - \Phi(z)$$
> 
>

---

## Teorema del Limite Centrale (TLC)

La somma (o la media) di un numero elevato di variabili aleatorie indipendenti e identicamente distribuite tende a distribuirsi come una Normale, indipendentemente dalla distribuzione di partenza.


### Approssimazioni Notevoli

Grazie al TLC, la Normale può approssimare altre distribuzioni quando $n$ è grande:

- **Binomiale $\to$ Normale:** Se $npq \ge 10$, allora $Bin(n,p) \approx N(np, npq)$.
    
- **Poisson $\to$ Normale:** Se $\lambda \ge 10$, allora $Poi(\lambda) \approx N(\lambda, \lambda)$.


![[Pasted image 20260212122619.png]]