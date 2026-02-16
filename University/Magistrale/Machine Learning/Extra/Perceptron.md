# Algoritmo Perceptron

**Tag:** #machine_learning #classificazione #algoritmo #geometria #supervisionato

---
![[Pasted image 20260216174530.png]]
## 1. Cos'è? (Concetto Visivo)

Il **Perceptron** è uno degli algoritmi fondamentali del Machine Learning. È un classificatore binario che ragiona in termini di **Geometria** e non di Probabilità.

- **Obiettivo:** Trovare un **Iperpiano separatore** ($H_\theta$) (una linea retta in 2D, un piano in 3D) che divida perfettamente i punti dati in due classi.
- **Immagine mentale:** Immagina di dover costruire un muro dritto in un campo per separare le pecore (classe +1) dai lupi (classe -1).
- **Input:** Vettori $x$ (le caratteristiche).
- **Label (Etichette):** $y \in {-1, +1}$ (usiamo questi numeri invece di 0/1 per facilitare i calcoli geometrici).

---

## 2. La Matematica (Semplificata)

Tutto si basa sul **Prodotto Scalare** (l'angolo tra i vettori).

Per classificare un nuovo punto $x$, calcoliamo il punteggio: $$f(x) = x^T \theta$$

Dove $\theta$ è il vettore che definisce l'orientamento del nostro "muro" (iperpiano).

### La Regola della Decisione

Guardiamo il **segno** del risultato:

1. **Segno Positivo ($>0$):** L'angolo tra $x$ e $\theta$ è $< 90^\circ$ (puntano nella stessa direzione). $\rightarrow$ **Previsione: +1**.
2. **Segno Negativo ($<0$):** L'angolo è $> 90^\circ$ (puntano in direzioni opposte). $\rightarrow$ **Previsione: -1**.
3. **Zero:** Il punto è esattamente sul muro ($90^\circ$).

> [!NOTE] Interpretazione Geometrica Il prodotto scalare $x^T \theta$ è legato al coseno dell'angolo.
> 
> - Coseno positivo = Stesso lato del muro.
> - Coseno negativo = Lato opposto.

---

## 3. L'Algoritmo (Come impara)

Il Perceptron è un "Lazy Learner" (impara solo quando sbaglia).

**Procedimento:**

1. Iniziamo con un vettore vuoto ($\theta = 0$).
2. Prendiamo un punto a caso $(x_i, y_i)$.
3. Controlliamo se c'è un errore.

### Tipi di Errore

Ci sono due modi di sbagliare:

- **Errore di Classificazione:** Ho predetto -1 ma era +1 (o viceversa). Matematicamente: $y_i(x_i^T \theta) \le 0$.
- **Errore di Margine (Margin Error):** Ho indovinato, ma sono **troppo vicino** al muro (non sono sicuro). Matematicamente: $y_i(x_i^T \theta) < 1$.

### L'Aggiornamento (Update Rule)

Se c'è un **Margin Error** (cioè $y_i x_i^T \theta < 1$), spostiamo il muro leggermente:

$$\theta_{nuovo} \leftarrow \theta_{vecchio} + y_i x_i$$

- Se era un esempio positivo ($y=1$), **aggiungiamo** il vettore (tiriamo $\theta$ verso $x$).
- Se era negativo ($y=-1$), **sottraiamo** il vettore (spingiamo $\theta$ via da $x$).

> [!ABSTRACT] In sintesi Se il punto è classificato bene e con un buon margine di sicurezza: **Non fare nulla**. Se il punto è classificato male o è troppo vicino al confine: **Correggi $\theta$**.

---

## 4. Teorema di Novikoff (Funzionerà?)

Questo teorema ci assicura che l'algoritmo non girerà all'infinito, _a patto che i dati siano separabili linearmente_.

Il numero massimo di errori ($M$) che il Perceptron farà è limitato da: $$M \le \frac{2 + D^2}{(\gamma^*)^2}$$ (approssimativamente $\frac{R^2}{\gamma^2}$)

Dove:

- **$D$ (o $R$):** Il raggio/diametro dei dati (quanto sono sparsi i punti).
- **$\gamma^*$ (Gamma):** Il **Margine Ottimo**. È la larghezza del corridoio più ampio che può separare le due classi.

> [!TIP] Intuizione
> 
> - Se il **Margine è grande** (i dati sono ben separati), $\gamma$ è grande $\rightarrow$ Faccio **pochi errori**.
> - Se il **Margine è minuscolo** (i dati sono appiccicati), $\gamma$ è piccolo $\rightarrow$ Faccio **molti errori** prima di trovare la soluzione.

---

## Collegamenti

- [[Support Vector Machines (SVM)]] - L'evoluzione del Perceptron che cerca attivamente il margine migliore.
- [[Logistic Regression]] - L'approccio probabilistico (vs geometrico).
- [[Kernel Trick]] - Per usare il Perceptron quando i dati non sono separabili da una linea retta.