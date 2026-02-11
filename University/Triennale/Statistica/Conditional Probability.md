# Probabilità Condizionata

**Tag:** #statistica #probabilità #machine_learning #bayes
**Fonte:** [[Sintesi statistica]]

## 📌 Definizione
La **Probabilità Condizionata** quantifica la probabilità che si verifichi un evento $E$ sapendo che un altro evento $F$ si è già verificato (ed è certo).

Si indica con $P(E|F)$ ("Probabilità di E dato F") ed è definita come:

$$ P(E|F) = \frac{P(E \cap F)}{P(F)} $$

*   **$P(E \cap F)$**: Probabilità che entrambi gli eventi accadano (Intersezione).
*   **$P(F)$**: Probabilità dell'evento condizionante (deve essere $>0$).

> [!ABSTRACT] Intuizione: Il "Mondo Ridotto"
> Condizionare significa **restringere lo spazio campionario**.
> Quando sappiamo che $F$ è accaduto, $F$ diventa il nostro nuovo "universo" di riferimento. Ignoriamo tutto ciò che è fuori da $F$. La probabilità di $E$ diventa quindi la frazione di $F$ occupata da $E$ (l'intersezione).

---

## 🛠️ Regole Fondamentali

### 1. Regola del Prodotto (Chain Rule)
Dalla definizione deriva la formula per calcolare la probabilità dell'intersezione (eventi congiunti):
$$ P(E \cap F) = P(E|F) \cdot P(F) $$

*Generalizzazione (Regola della Catena):*
$$ P(A_1 \cap A_2 \cap \dots \cap A_n) = P(A_1) P(A_2|A_1) P(A_3|A_1 \cap A_2) \dots $$

### 2. Teorema della Probabilità Totale (Fattorizzazione)
Se abbiamo una partizione dello spazio in eventi disgiunti $F_1, F_2, \dots, F_n$, possiamo calcolare la probabilità di un evento $E$ "sommando i pezzi":

$$ P(E) = \sum_{i} P(E|F_i)P(F_i) $$

*(Utile nel ML per calcolare il denominatore $P(X)$ in Bayes, sommando su tutte le classi $Y$).*

### 3. [[Teorema di Bayes]]
Il pilastro della classificazione probabilistica. Permette di "invertire" il condizionamento (da causa $\to$ effetto a effetto $\to$ causa):

$$ P(F|E) = \frac{P(E|F)P(F)}{P(E)} $$

Espanso con la Probabilità Totale:
$$ P(F_j|E) = \frac{P(E|F_j)P(F_j)}{\sum_{i} P(E|F_i)P(F_i)} $$

*   **$P(F|E)$:** Posteriori (ciò che vogliamo sapere dopo aver visto i dati).
*   **$P(E|F)$:** Verosimiglianza / Likelihood (modello generativo).
*   **$P(F)$:** Priori (conoscenza a priori).
*   **$P(E)$:** Evidenza (normalizzazione).

---

## 🎲 Variabili Aleatorie Condizionate
I concetti si estendono dalle variabili evento alle variabili aleatorie $X$ e $Y$.

### Funzione di Massa/Densità Condizionata
$$ p_{X|Y}(x|y) = P(X=x \mid Y=y) = \frac{p_{X,Y}(x,y)}{p_Y(y)} $$

### Valore Atteso Condizionato
La media della variabile $X$ calcolata solo nel "sotto-mondo" dove $Y=y$.
$$ \mathbb{E}[X \mid Y=y] = \sum_{x} x \cdot P(X=x \mid Y=y) $$

> [!TIP] Collegamento con Machine Learning
> Il **Bayes Optimal Predictor** per la *Squared Loss* è proprio il Valore Atteso Condizionato dell'etichetta $Y$ dato l'input $X=x$:
> $$ f^*(x) = \mathbb{E}[Y \mid X=x] $$

---

## ⚠️ Indipendenza
Due eventi (o variabili) sono **indipendenti** se l'accadere di uno non modifica la probabilità dell'altro.

$$ P(E|F) = P(E) $$

In questo caso, la probabilità congiunta diventa semplicemente il prodotto:
$$ P(E \cap F) = P(E) \cdot P(F) $$

*(Questa è l'assunzione chiave del classificatore **Naive Bayes**: assume che le feature $X_i$ siano indipendenti tra loro dato $Y$).*