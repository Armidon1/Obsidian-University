Ecco la soluzione dell'**Esercizio 2.3**, che è un caso particolare e molto semplice del _Likelihood Ratio Test_.

### 1. Dati del problema

- **Loss Function:** 0-1 Loss ($l(a,b) = \mathbb{I}{a \neq b}$).
    - Costo errori ($l(1,0)$ e $l(0,1)$) = **1**.
    - Costo risposte corrette ($l(0,0)$ e $l(1,1)$) = **0**.
- **Priori:** Le classi sono equiprobabili.
    - $P(Y=1) = P(Y=0) = 0.5$.

### 2. La Formula Generale

Come abbiamo visto nella discussione precedente, il predittore ottimo è: $$ f^*(x) = \mathbb{I} \left{ \frac{P(X=x|Y=1)}{P(X=x|Y=0)} \ge \eta \right} $$

Dove la soglia $\eta$ è definita come: $$ \eta = \frac{[l(1,0)-l(0,0)] \cdot P(Y=0)}{[l(0,1)-l(1,1)] \cdot P(Y=1)} $$

### 3. Calcolo della Soglia ($\eta$)

Sostituiamo i numeri:

1. **Parte dei Costi:**
    - Numeratore: $1 - 0 = 1$
    - Denominatore: $1 - 0 = 1$
    - Rapporto Costi: $1/1 = 1$.
2. **Parte dei Priori:**
    - $P(Y=0) / P(Y=1) = 0.5 / 0.5 = 1$.

Quindi: $$ \eta = 1 \cdot 1 = 1 $$

### 4. Risultato Finale

Il predittore ottimo diventa semplicemente:

$$ f^*(x) = \mathbb{I} \left{ \frac{P(X=x|Y=1)}{P(X=x|Y=0)} \ge 1 \right} $$

Ovvero, prediciamo **1** se: $$ P(X=x|Y=1) \ge P(X=x|Y=0) $$

### Interpretazione

Questo risultato ci dice una cosa molto intuitiva: Quando **non hai preferenze a priori** (le classi sono ugualmente probabili) e **i costi sono simmetrici** (sbagliare da una parte o dall'altra fa male uguale), il predittore ottimo si affida ciecamente ai dati. Scegli semplicemente la classe che rende i dati osservati più probabili (**Maximum Likelihood**).