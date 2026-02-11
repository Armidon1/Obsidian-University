# Covarianza (Covariance)

**Tag:** #statistica #probabilità #machine_learning #definizioni
**Fonte:** [[Sintesi statistica]]

## 📌 Definizione
La **Covarianza**, indicata come $\text{Cov}(X, Y)$ o $\sigma_{XY}$, misura la relazione lineare tra due variabili casuali $X$ e $Y$. Indica se e quanto le due variabili tendono a variare insieme.

Matematicamente, è il valore atteso del prodotto degli scarti dalle rispettive medie:

$$ \text{Cov}(X, Y) = \mathbb{E}[(X - \mu_X)(Y - \mu_Y)] $$

Dove $\mu_X = \mathbb{E}[X]$ e $\mu_Y = \mathbb{E}[Y]$.

---

## 🧮 Formula Operativa
Per i calcoli manuali si usa la formula derivata dalla linearità del valore atteso (Formula di König):

$$ \text{Cov}(X, Y) = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y] $$

> [!TIP] Interpretazione del Segno
> *   **$\text{Cov} > 0$:** Le variabili sono **concordi**. Quando $X$ assume valori grandi, anche $Y$ tende ad assumere valori grandi (e viceversa).
> *   **$\text{Cov} < 0$:** Le variabili sono **discordi**. Quando $X$ cresce, $Y$ tende a diminuire.
> *   **$\text{Cov} = 0$:** Le variabili sono **incorrelate**. Non c'è relazione lineare (ma potrebbe esserci una relazione non lineare).

---

## ⚙️ Proprietà Fondamentali
Le dispense elencano diverse proprietà algebriche utili per semplificare i calcoli (pag. 9):

1.  **Relazione con la Varianza:**
    La covarianza di una variabile con se stessa è la sua varianza.
    $$ \text{Cov}(X, X) = \text{Var}(X) $$

2.  **Simmetria:**
    $$ \text{Cov}(X, Y) = \text{Cov}(Y, X) $$

3.  **Bilinearità (Linearità su entrambi gli argomenti):**
    *   **Costanti moltiplicative:** $\text{Cov}(aX, Y) = a \cdot \text{Cov}(X, Y)$
    *   **Somma:** $\text{Cov}(X + Z, Y) = \text{Cov}(X, Y) + \text{Cov}(Z, Y)$

    *Formula generale:*
    $$ \text{Cov}\left(\sum_i a_i X_i, \sum_j b_j Y_j\right) = \sum_i \sum_j a_i b_j \text{Cov}(X_i, Y_j) $$

4.  **Invarianza per traslazione:**
    Aggiungere costanti non cambia la covarianza (sposta le medie ma non la relazione tra gli scarti).
    $$ \text{Cov}(X+a, Y+b) = \text{Cov}(X, Y) $$

---

## ⚠️ Indipendenza vs Incorrelazione
Una distinzione fondamentale marcata nelle dispense (pag. 4 e 9):

*   **Indipendenza $\implies$ Incorrelazione:**
    Se $X$ e $Y$ sono indipendenti, allora $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$, quindi $\text{Cov}(X, Y) = 0$.

*   **Incorrelazione $\not\implies$ Indipendenza:**
    Se $\text{Cov}(X, Y) = 0$, le variabili sono incorrelate, ma **NON** necessariamente indipendenti. Potrebbe esistere una relazione non lineare (es. $Y = X^2$ con $X$ simmetrica rispetto a 0).

---

## 📉 Coefficiente di Correlazione Lineare ($\rho$)
La covarianza dipende dall'unità di misura (es. metri vs centimetri). Per avere una misura standardizzata tra $[-1, 1]$, si usa il coefficiente di correlazione:

$$ \rho_{XY} = \frac{\text{Cov}(X, Y)}{\sqrt{\text{Var}(X)\text{Var}(Y)}} = \frac{\sigma_{XY}}{\sigma_X \sigma_Y} $$

*   $\rho = 1$: Perfetta correlazione lineare positiva.
*   $\rho = -1$: Perfetta correlazione lineare negativa.
*   $\rho = 0$: Assenza di correlazione lineare.

---

## 🧠 Collegamento con Machine Learning
*   **Varianza della somma:** Fondamentale per capire l'errore di un modello ensemble o la somma di feature.
    $$ \text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X,Y) $$
*   **Gaussiane Multivariate:** Nel ML (es. Gaussian Mixture Models o LDA), la "forma" della distribuzione dei dati è descritta dalla **Matrice di Covarianza** $\Sigma$, che contiene le varianze sulla diagonale e le covarianze fuori diagonale.