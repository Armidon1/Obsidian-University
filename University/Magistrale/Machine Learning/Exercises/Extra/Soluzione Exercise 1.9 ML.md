Ecco la soluzione dell'**Esercizio 1.9** passo dopo passo.

Mentre nell'esercizio precedente (Loss Quadratica) il risultato era la _Media Condizionata_, qui vedremo che per la **Loss Assoluta** ($l(a, b) = |a-b|$) il predittore ottimo è la **Mediana Condizionata**.

### 1. Impostazione del problema

Secondo il **Teorema 1.6**, dobbiamo trovare per ogni $x$ il valore $z$ che minimizza il rischio atteso condizionato:

$$f^*(x) = \text{argmin}_{z \in \mathbb{R}} \mathbb{E}[|z - Y| \mid X=x]$$

Come suggerito dall'hint dell'esercizio, assumiamo che la distribuzione di $Y$ (dato $X=x$) abbia una funzione di densità di probabilità, che chiameremo $p(y)$ per brevità.

### 2. Svolgimento Matematico

Dobbiamo minimizzare la funzione di costo $J(z)$: $$J(z) = \int_{-\infty}^{+\infty} |z - y| p(y) dy$$

Poiché c'è un valore assoluto, non possiamo derivare direttamente. Dobbiamo spezzare l'integrale in due parti: una dove $y < z$ (quindi $|z-y| = z-y$) e una dove $y > z$ (quindi $|z-y| = y-z$).

$$J(z) = \int_{-\infty}^{z} (z - y)p(y) dy + \int_{z}^{+\infty} (y - z)p(y) dy$$

Ora calcoliamo la **derivata** rispetto a $z$ usando la regola di Leibniz per gli integrali:

1. **Primo integrale** ($\int_{-\infty}^{z} (z - y)p(y) dy$): La derivata di $(z-y)$ rispetto a $z$ è $1$. $$\frac{d}{dz} \dots = \int_{-\infty}^{z} 1 \cdot p(y) dy = P(Y \le z)$$
    
2. **Secondo integrale** ($\int_{z}^{+\infty} (y - z)p(y) dy$): La derivata di $(y-z)$ rispetto a $z$ è $-1$. $$\frac{d}{dz} \dots = \int_{z}^{+\infty} -1 \cdot p(y) dy = -P(Y \ge z)$$
    

Quindi la derivata totale è: $$J'(z) = P(Y \le z) - P(Y \ge z)$$

### 3. Ottimizzazione

Poniamo la derivata uguale a zero per trovare il minimo:

$$P(Y \le z) - P(Y \ge z) = 0$$ $$P(Y \le z) = P(Y \ge z)$$

Sapendo che la somma delle probabilità è 1 ($P(Y \ge z) = 1 - P(Y \le z)$), otteniamo:

$$P(Y \le z) = 1 - P(Y \le z)$$ $$2 \cdot P(Y \le z) = 1$$ $$P(Y \le z) = \frac{1}{2}$$

### 4. Risultato Finale

Il valore $z$ che soddisfa questa equazione (ovvero il valore che lascia il 50% di probabilità a sinistra e il 50% a destra) è per definizione la **Mediana**.

Quindi, il predittore ottimo per la loss assoluta è la **Mediana Condizionata**:

$$f^*(x) = \text{Median}[Y \mid X=x]$$

### Nota concettuale: Media vs Mediana

- **Squared Loss (Esercizio 1.8) $\to$ Media:** La media è sensibile agli **outlier**. Se hai un valore $Y$ molto lontano, l'errore al quadrato diventa enorme, quindi la media si "sposta" verso quell'outlier per ridurre il danno.
- **Absolute Loss (Esercizio 1.9) $\to$ Mediana:** La mediana è **robusta**. Se sposti un punto estremo ancora più lontano, la mediana non cambia (perché conta solo l'ordine dei dati, non il loro valore numerico preciso). Ecco perché la loss assoluta è preferita quando ci sono dati "sporchi" o rumore impulsivo.

# Spiegazione come sono stati fatti gli integrali dal professore

Certamente. Analizziamo **solo** il Termine A al microscopio.

Stiamo calcolando la derivata rispetto a $z$ di questo prodotto:

$$\frac{d}{dz} \left[ \underbrace{z}_{f(z)} \cdot \underbrace{\int_{-\infty}^{z} p(y) \, dy}_{g(z)} \right]$$

Per farlo, usiamo la **Regola del Prodotto** (o di Leibniz):

$$(f \cdot g)' = f' \cdot g + f \cdot g'$$

Dobbiamo trovare quattro pezzi: $f$, $g$, $f'$ e $g'$.

---

### Passo 1: Identifichiamo le due parti ($f$ e $g$)

1. **La prima funzione ($f$) è:**
    
    $$f(z) = z$$
    
    Questa è semplice, è solo la variabile.
    
2. **La seconda funzione ($g$) è l'integrale:**
    
    $$g(z) = \int_{-\infty}^{z} p(y) \, dy$$
    
    Questa è una funzione di $z$ perché $z$ è l'estremo superiore dell'integrale (il limite fino a cui calcoliamo l'area).
    

---

### Passo 2: Calcoliamo le derivate ($f'$ e $g'$)

1. **Derivata della prima ($f'$):**
    
    $$f'(z) = \frac{d}{dz}(z) = 1$$
    
    _(La derivata di una variabile rispetto a se stessa è 1)._
    
2. **Derivata della seconda ($g'$):**
    
    Qui entra in gioco il **Teorema Fondamentale del Calcolo Integrale**.
    
    $$g'(z) = \frac{d}{dz} \left( \int_{-\infty}^{z} p(y) \, dy \right)$$
    
    La regola dice: _la derivata di un integrale rispetto al suo estremo superiore è semplicemente la funzione che c'è dentro (l'integranda), valutata in quel punto._
    
    Quindi:
    
    $$g'(z) = p(z)$$
    

---

### Passo 3: Mettiamo tutto insieme nella formula

Ora sostituiamo i quattro pezzi nella formula del prodotto: $(f' \cdot g) + (f \cdot g')$.

1. **Primo pezzo ($f' \cdot g$):**
    
    $$1 \cdot \left( \int_{-\infty}^{z} p(y) \, dy \right) = \int_{-\infty}^{z} p(y) \, dy$$
    
2. **Secondo pezzo ($f \cdot g'$):**
    
    $$z \cdot p(z)$$
    

### Risultato Finale per il Termine A

Sommando i due pezzi otteniamo esattamente quello che avevamo visto:

$$\frac{d}{dz} \left[ z \int_{-\infty}^{z} p(y)dy \right] = \underbrace{\int_{-\infty}^{z} p(y)dy}_{\text{Integrale rimasto}} + \underbrace{z \cdot p(z)}_{\text{Termine che si cancellerà}}$$

È più chiaro ora come siamo arrivati a quei due addendi specifici?

---

Certamente. Analizziamo il **Termine B** con la stessa precisione.

Il termine B nell'equazione è questo:

$$B(z) = - \int_{-\infty}^{z} y \cdot p(y) \, dy$$

### La differenza rispetto al Termine A

Nel Termine A avevamo una $z$ _fuori_ dall'integrale che moltiplicava l'integrale stesso (quindi serviva la regola del prodotto).

Qui, invece, la $z$ compare **solo** come estremo superiore dell'integrale. Non c'è nessuna $z$ che moltiplica davanti.

Questo rende il calcolo più diretto perché dobbiamo usare **solo** il Teorema Fondamentale del Calcolo Integrale.

---

### Passo 1: Identifichiamo la "funzione interna" (l'integranda)

Guardiamo cosa c'è dentro l'integrale. Chiamiamo questa funzione $h(y)$:

$$h(y) = y \cdot p(y)$$

Quindi il nostro Termine B si può riscrivere come:

$$B(z) = - \int_{-\infty}^{z} h(y) \, dy$$

---

### Passo 2: Applichiamo la regola di derivazione

La regola d'oro (Teorema Fondamentale) dice:

> _Se derivi un integrale rispetto al suo estremo superiore, il risultato è semplicemente la funzione che c'era dentro, valutata in quel punto._

In formule:

$$\frac{d}{dz} \left( \int_{a}^{z} h(y) \, dy \right) = h(z)$$

Cosa significa in pratica? Significa che **prendi tutto quello che c'è dentro l'integrale e sostituisci tutte le $y$ con delle $z$**.

---

### Passo 3: Eseguiamo la sostituzione

1. La nostra funzione interna era: $h(y) = y \cdot p(y)$
    
2. Sostituiamo $y$ con $z$:
    
    $$h(z) = z \cdot p(z)$$
    

---

### Passo 4: Non dimentichiamo il segno meno

Il Termine B aveva un segno meno davanti all'integrale. La derivata è lineare, quindi il segno meno rimane lì dov'è.

$$\frac{d}{dz} \left[ - \int_{-\infty}^{z} y \cdot p(y) \, dy \right] = - \left[ z \cdot p(z) \right]$$

### Risultato Finale per il Termine B

La derivata è:

$$- z \cdot p(z)$$

Ecco perché nell'immagine vedi quel termine barrato: questo $- z p(z)$ è esattamente l'opposto del $+ z p(z)$ che era spuntato fuori derivando il Termine A. Si annullano perfettamente.

i termini C e D sono speculari.

# Perché l'integrale diventa una probabilità?

Questa è un'ottima domanda. Qui non stiamo più facendo calcoli (derivare o integrare), ma stiamo applicando una **definizione**.

Il passaggio da $\int p(y)dy$ a $P(Y \leq z)$ è letteralmente il modo in cui si **legge** la probabilità nelle variabili continue.

Ecco il concetto chiave:

### 1. L'Area è la Probabilità

In statistica, $p(y)$ è la **funzione di densità**. Di per sé, il valore di $p(y)$ in un punto non è una probabilità.

Per ottenere una probabilità, devi calcolare l'**area sotto la curva** di $p(y)$ in un certo intervallo.

Quindi, matematicamente, scrivere questo integrale:

$$\int_{A}^{B} p(y) dy$$

...è **esattamente la stessa cosa** che dire a parole:

_"La probabilità che la variabile $Y$ cada tra $A$ e $B$"._

### 2. Guardiamo il lato sinistro

L'equazione che abbiamo trovato (dopo le cancellazioni) aveva questo termine a sinistra:

$$\int_{-\infty}^{z} p(y) dy$$

Traducilo in italiano:

- "L'area sotto la curva..."
    
- "...partendo da meno infinito ($-\infty$)..."
    
- "...e arrivando fino a $z$".
    

Questo copre tutti i casi in cui $Y$ è più piccolo o uguale a $z$.

Quindi:

$$P(Y \leq z)$$

### 3. Guardiamo il lato destro

Ora, guardiamo l'integrale a destra dell'uguale:

$$\int_{z}^{+\infty} p(y) dy$$

Traducilo in italiano:

- "L'area sotto la curva..."
    
- "...partendo da $z$..."
    
- "...e arrivando fino a più infinito ($+\infty$)".
    

Questo copre tutti i casi in cui $Y$ è più grande o uguale a $z$.

Quindi:

$$P(Y \geq z)$$

---

### E la condizione $| X=x$?

Nell'immagine, la funzione di partenza era definita "conditioned on $X=x$" (vedi la prima riga scritta a mano: $E[|z-y| | X=x]$).

La $p(y)$ usata negli integrali era in realtà una scorciatoia per dire $p(y|x)$.

Quindi, non è semplicemente "La probabilità che $Y$ sia minore di $z$".

È "La probabilità che $Y$ sia minore di $z$, **dato che** $X$ vale $x$".

Ecco perché alla fine vedi scritto:

$$P(Y \leq z | X=x)$$

---

### In sintesi

Non è un calcolo matematico complicato, è solo una **definizione**:

1. $\int_{-\infty}^{z} p(y) dy$ **è la definizione matematica di** $P(Y \leq z)$.
    
2. $\int_{z}^{+\infty} p(y) dy$ **è la definizione matematica di** $P(Y \geq z)$.
    

Il passaggio finale ("è uguale a 1/2") deriva dal fatto che la somma di queste due probabilità deve essere il 100% (o 1), e visto che sono uguali, ognuna deve valere il 50%.