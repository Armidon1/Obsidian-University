# Teorema di Bayes

**Tag:** #statistica #probabilità #bayes #machine_learning #inference
**Fonte:** [[Sintesi statistica]] (pagine 3, 9)

## 📌 Definizione
Il **Teorema di Bayes** è una formula matematica che descrive come aggiornare la probabilità di un'ipotesi (o evento) alla luce di nuove prove (o dati).

Permette di "invertire" le probabilità condizionate: se conosciamo la probabilità dell'effetto data la causa ($P(\text{Effetto}|\text{Causa})$), possiamo calcolare la probabilità della causa dato l'effetto osservato.

### La Formula
Siano $F_j$ una serie di ipotesi (cause) ed $E$ un evento osservato (evidenza/effetto). La formula è:

$$ P(F_j | E) = \frac{P(E | F_j) \cdot P(F_j)}{P(E)} $$

Dove il denominatore $P(E)$ si calcola spesso usando la **Formula di Fattorizzazione** (Probabilità Totale):
$$ P(E) = \sum_{i} P(E | F_i) \cdot P(F_i) $$

## 🧠 I 4 Componenti Chiave
Nel contesto del Machine Learning (dove $F_j = Y$ classe, $E = X$ dati), i termini hanno nomi specifici:

1.  **Posteriori** $P(F_j | E)$:
    *   La probabilità dell'ipotesi *dopo* aver visto i dati. È ciò che vogliamo calcolare (es. Probabilità che il paziente sia malato dato il test positivo).
2.  **Verosimiglianza (Likelihood)** $P(E | F_j)$:
    *   Quanto è probabile osservare questi dati se l'ipotesi fosse vera. (es. Probabilità che il test sia positivo se il paziente è davvero malato).
3.  **Priori** $P(F_j)$:
    *   La nostra conoscenza iniziale sull'ipotesi prima di vedere i dati. (es. Quanto è diffusa la malattia nella popolazione generale?).
4.  **Evidenza (Marginale)** $P(E)$:
    *   La probabilità totale di osservare i dati sotto tutte le possibili ipotesi. Serve come costante di normalizzazione per far sì che la somma delle probabilità faccia 1.

> [!TIP] Interpretazione Intuitiva
> $$ \text{Posteriori} \propto \text{Verosimiglianza} \times \text{Priori} $$
> La tua credenza aggiornata è un compromesso tra ciò che ti dicono i dati attuali (Likelihood) e ciò che sapevi già prima (Prior).

---

## 🚀 Applicazioni nel Machine Learning

### 1. Classificazione (Bayes Optimal Predictor)
L'obiettivo è trovare la classe $y$ che massimizza la probabilità a posteriori:
$$ f^*(x) = \operatorname*{argmax}_{y} P(Y=y | X=x) $$
Usando Bayes, questo equivale a massimizzare:
$$ \operatorname*{argmax}_{y} P(X=x | Y=y) \cdot P(Y=y) $$
*(Il denominatore $P(X=x)$ si ignora perché è costante per tutte le classi).*

### 2. Likelihood Ratio Test (Classificazione Binaria)
Quando confrontiamo due classi ($Y=1$ vs $Y=0$), il teorema ci permette di passare dal confronto delle posteriori al confronto delle likelihood pesate dai priori (come visto nella Proposizione 2.1):

$$ \frac{P(Y=1|X)}{P(Y=0|X)} = \frac{P(X|Y=1)}{P(X|Y=0)} \cdot \frac{P(Y=1)}{P(Y=0)} $$

### 3. Naive Bayes
Un classificatore che applica il Teorema di Bayes assumendo che le feature $X_i$ siano **indipendenti** tra loro data la classe $Y$.
$$ P(X|Y) \approx \prod P(X_i|Y) $$

---

## ⚠️ Esempio Classico (Falsi Positivi)
Un test medico ha una precisione del 99% ($P(+|\text{Malato})=0.99$, $P(-|\text{Sano})=0.99$). La malattia colpisce 1 persona su 1000 ($P(\text{Malato})=0.001$).
Se sei positivo al test, sei malato?

La risposta intuitiva è "sì, al 99%", ma Bayes corregge l'errore:
$$ P(\text{Malato}|+) = \frac{0.99 \cdot 0.001}{(0.99 \cdot 0.001) + (0.01 \cdot 0.999)} \approx 9\% $$
Il **Priori** molto basso (malattia rara) "schiaccia" la **Verosimiglianza** del test.