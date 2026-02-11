# Varianza (Variance)

**Tag:** #statistica #probabilità #machine_learning #definizioni
**Fonte:** [[Sintesi statistica]]

## 📌 Definizione
La **Varianza**, indicata solitamente con $\text{Var}(X)$, $\sigma^2_X$ o $V(X)$, è una misura di dispersione che quantifica quanto i valori di una variabile casuale si discostano mediamente dalla loro media ($\mu$).

Matematicamente, è definita come il **valore atteso degli scarti quadratici dalla media**:

$$ \text{Var}(X) = \mathbb{E}[(X - \mathbb{E}[X])^2] $$

O più semplicemente, indicando $\mu = \mathbb{E}[X]$:
$$ \text{Var}(X) = \mathbb{E}[(X - \mu)^2] $$

> [!NOTE] Deviazione Standard
> La varianza è un valore al quadrato (quindi non ha la stessa unità di misura dei dati). Per riportarla alla scala originale, si usa la **Deviazione Standard** (o Scarto Quadratico Medio):
> $$ \sigma_X = \sqrt{\text{Var}(X)} $$

---

## 🧮 Formule di Calcolo
Per i calcoli manuali, raramente si usa la definizione pura. Si utilizza invece la **Formula Operativa** (derivata dalla linearità del valore atteso):

$$ \text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 $$

*"La media dei quadrati meno il quadrato della media."*

---

## ⚙️ Proprietà Fondamentali
Le dispense evidenziano proprietà cruciali per la manipolazione algebrica delle varianze.

### 1. Invarianza per traslazione
Sommare una costante $b$ a una variabile casuale **non cambia** la sua varianza (la distribuzione si sposta ma non si allarga).
$$ \text{Var}(X + b) = \text{Var}(X) $$

### 2. Omogeneità di secondo grado
Moltiplicare la variabile per una costante $a$ scala la varianza del quadrato della costante.
$$ \text{Var}(aX) = a^2 \text{Var}(X) $$

**Combinando le due:**
$$ \text{Var}(aX + b) = a^2 \text{Var}(X) $$

### 3. Varianza della Somma
Qui la regola cambia a seconda della dipendenza tra le variabili.

*   **Caso Generale (Variabili Dipendenti):**
    $$ \text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X, Y) $$
    *(Dove $\text{Cov}(X, Y) = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]$ è la covarianza)*

*   **Caso Variabili INDIPENDENTI:**
    Se $X$ e $Y$ sono indipendenti (o anche solo incorrelate), la covarianza è zero.
    $$ \text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) $$

---

## 📊 Tabella Varianze Notevoli
Riepilogo dalle dispense (pagine sulle distribuzioni):

| Distribuzione | Parametri | Varianza $\text{Var}(X)$ | Note |
| :--- | :--- | :--- | :--- |
| **Bernoulli** | $p$ | $p(1-p)$ | Massima per $p=0.5$ |
| **Binomiale** | $n, p$ | $np(1-p)$ | Somma di $n$ Bernoulli indip. |
| **Geometrica** | $p$ | $\frac{1-p}{p^2}$ | |
| **Poisson** | $\lambda$ | $\lambda$ | Coincide con la media |
| **Uniforme Discreta** | $n$ (casi) | $\frac{n^2-1}{12}$ | |
| **Normale** | $\mu, \sigma^2$ | $\sigma^2$ | Parametro esplicito della pdf |

---

## 🧠 Collegamento con Machine Learning
*   **Bias-Variance Tradeoff:** In ML, la varianza dell'errore misura quanto il modello è sensibile alle fluttuazioni del set di training (Overfitting = Alta Varianza).
*   **MSE (Mean Squared Error):** La funzione di perdita quadratica può essere decomposta in $Bias^2 + Variance + Noise$.