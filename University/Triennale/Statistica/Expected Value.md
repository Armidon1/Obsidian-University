# Valore Atteso (Expected Value)

**Tag:** #statistica #probabilità #machine_learning #definizioni
**Fonte:** [[Sintesi statistica]]

## 📌 Definizione
Il **Valore Atteso** (o media, speranza matematica), indicato solitamente con $\mathbb{E}[X]$ o $\mu$, rappresenta il "baricentro" della distribuzione di probabilità di una variabile casuale. È la somma pesata dei possibili valori che la variabile può assumere.

### Formula (Caso Discreto)
Per una variabile casuale discreta $X$ che assume valori $x_1, x_2, \dots, x_n$ con probabilità $P(X=x_i)$:

$$ \mathbb{E}[X] = \sum_{i} x_i \cdot P(X=x_i) $$

> [!NOTE] Interpretazione
> Non è necessariamente un valore che la variabile assumerà davvero (es. la media di un dado è 3.5), ma è il valore verso cui tende la media campionaria per un numero elevato di prove (Legge dei Grandi Numeri).

---

## ⚙️ Proprietà Fondamentali
Le seguenti proprietà sono essenziali per semplificare i calcoli, specialmente nel Machine Learning.

### 1. Linearità (Fondamentale)
L'operatore di valore atteso è **lineare**.
*   **Costanti:** $\mathbb{E}[c] = c$
*   **Scalare e somma:** $\mathbb{E}[aX + b] = a\mathbb{E}[X] + b$
*   **Somma di V.A.:** $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$
    *   *Nota:* Questa vale **sempre**, sia che $X$ e $Y$ siano indipendenti o dipendenti.

### 2. Prodotto di V.A.
$$ \mathbb{E}[XY] = \mathbb{E}[X] \cdot \mathbb{E}[Y] $$
> [!WARNING] Attenzione
> Questa uguaglianza vale **SOLO se X e Y sono INDIPENDENTI**. In caso contrario, $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y] + \text{Cov}(X,Y)$.

---

## 🧠 Legge dello Statistico Inconsapevole (LOTUS)
Per calcolare il valore atteso di una **funzione** di una variabile casuale $g(X)$ (ad esempio, la *Loss Function* $l(f(X), Y)$ nel ML), non serve conoscere la distribuzione di $g(X)$, basta usare quella di $X$:

$$ \mathbb{E}[g(X)] = \sum_{x} g(x) \cdot P(X=x) $$

Nel caso di due variabili (es. dati ed etichette):
$$ \mathbb{E}[g(X, Y)] = \sum_{x} \sum_{y} g(x, y) \cdot P(X=x, Y=y) $$

---

## 🔄 Valore Atteso Condizionato
Definito come la media di $X$ dato che si è verificato l'evento $Y=y$:

$$ \mathbb{E}[X \mid Y=y] = \sum_{x} x \cdot P(X=x \mid Y=y) $$

### Teorema delle Aspettative Iterate (Tower Property)
Il valore atteso globale è la media dei valori attesi condizionati:
$$ \mathbb{E}[X] = \mathbb{E}_Y [ \mathbb{E}[X \mid Y] ] $$
*Utilità:* Usato per derivare il **Bayes Optimal Predictor**.

---

## 📊 Tabella Valori Attesi Notevoli
Riepilogo dalle dispense:

| Distribuzione | Simbolo | Valore Atteso $\mathbb{E}[X]$ | Note |
| :--- | :--- | :--- | :--- |
| **Bernoulli** | $B(p)$ | $p$ | Esito binario (0/1) |
| **Binomiale** | $Bin(n, p)$ | $np$ | Somma di $n$ Bernoulli indip. |
| **Geometrica** | $Geom(p)$ | $\frac{1}{p}$ | Prove fino al primo successo |
| **Poisson** | $Poi(\lambda)$ | $\lambda$ | Eventi rari in intervallo |
| **Uniforme** | $U(1, n)$ | $\frac{n+1}{2}$ | Probabilità costante |
| **Normale** | $N(\mu, \sigma^2)$ | $\mu$ | Gaussiana |