# Support Vector Machines (SVM)

**Tag:** #machine_learning #classificazione #algoritmo #geometria #ottimizzazione

---

## 1. Il Concetto (L'evoluzione del Perceptron)

Se il [[Perceptron]] si accontenta di trovare un muro _qualsiasi_ che separi i dati, l'**SVM** (Macchina a Vettori di Supporto) è un perfezionista: vuole trovare il muro **migliore possibile**.

### L'Immagine Mentale: La Strada

- Immagina di nuovo i punti rossi e blu sul foglio.
- Invece di disegnare una linea sottile, immagina di dover disegnare una **strada asfaltata** (un corridoio) che separi i due gruppi.
- L'obiettivo dell'SVM è fare questa strada **il più larga possibile** (Massimizzare il Margine).
- La linea di mezzo della strada è la tua _Decision Boundary_.

> [!NOTE] Chi sono i "Support Vectors"? Sono i punti dati che toccano i bordi della strada (i più vicini al confine). Sono gli unici punti che contano: l'intera strada è "sorretta" da loro. Se muovi gli altri punti lontani, la strada non cambia.

---

## 2. Hard Margin (Il Mondo Ideale)

Se i dati sono perfettamente separabili (non ci sono eccezioni), usiamo l'SVM "Hard Margin".

**Obiettivo Matematico:** Vogliamo massimizzare la larghezza della strada ($\gamma$). Nelle dispense si dimostra che massimizzare il margine equivale a **minimizzare la norma** del vettore $\theta$.

$$ \min \frac{1}{2} |\theta|^2 \quad \text{soggetto a} \quad y_i (x_i^T \theta) \ge 1 $$

- **Minimizzare $|\theta|$** = Rendere la soluzione "semplice" e la strada larga.
- **Vincolo ($y \cdot x^T\theta \ge 1$)** = Nessuno deve calpestare l'asfalto.

---

## 3. Soft Margin (Il Mondo Reale)

Nella realtà, i dati sono spesso mischiati ("rumorosi") e una separazione perfetta è impossibile. Se insistiamo a separare tutto, la strada diventerebbe minuscola o inesistente.

**Soluzione:** Introduciamo le **Slack Variables** ($\xi_i$). Immagina di permettere qualche "intruso" sulla strada o addirittura nel campo sbagliato, ma fagli pagare una **multa**.

### La Nuova Formula

$$ \min \frac{1}{2} |\theta|^2 + C \sum_{i=1}^n \xi_i $$

Ci sono due forze in gioco:

1. **$|\theta|^2$**: Voglio la strada larga.
2. **$\sum \xi_i$**: Voglio pagare poche multe (pochi errori).
3. **$C$ (Iperparametro):** È la severità del vigile urbano.

> [!TIP] Come funziona C?
> 
> - **C Alto:** Vigile severissimo. Tolleranza zero agli errori. La strada sarà stretta pur di non sbagliare. (Rischio: [[Overfitting]]).
> - **C Basso:** Vigile rilassato. Accetta più errori pur di avere una strada più larga e generale. (Meglio per generalizzare).

---

## 4. Come impara (Hinge Loss)

Per addestrare l'SVM, usiamo una funzione di costo chiamata **Hinge Loss** (funzione a cerniera):

$$ L(y, f(x)) = \max(0, 1 - y \cdot f(x)) $$

- Se il punto è dal lato giusto e lontano dalla strada ($>1$): **Costo 0** (Nessun problema).
- Se il punto è sulla strada o dal lato sbagliato ($<1$): **Il costo cresce linearmente**.

**Aggiornamento (Stochastic Gradient Descent):** L'algoritmo guarda un punto alla volta.

- **Se è corretto e sicuro:** Riduciamo solo leggermente $\theta$ (per tenerlo piccolo/semplice).
- **Se c'è errore:** Spostiamo il muro usando sia la regolarizzazione che l'errore commesso.

---

## 5. Il Kernel Trick (La Magia 3D)

Cosa succede se i dati sono disposti a cerchio (i rossi al centro, i blu intorno)? Una linea dritta non potrà mai separarli.

L'SVM usa il **Kernel Trick** per proiettare i dati in uno spazio con più dimensioni dove diventano separabili linearmente.

- **Immagine Mentale:** Immagina i punti disegnati su un foglio di gomma. Se sollevi il centro del foglio verso l'alto (aggiungi una dimensione), i punti rossi al centro salgono, quelli blu restano giù. Ora puoi passare un "foglio" piatto (iperpiano) tra i due gruppi.

**Il trucco matematico:** Non dobbiamo calcolare davvero le coordinate nel nuovo spazio (che potrebbero essere infinite!). Ci basta calcolare il **prodotto scalare** (la somiglianza) tra i punti trasformati. Questa funzione di somiglianza si chiama **Kernel** $K(x, z)$.

- **Kernel Polinomiale:** Curve e forme complesse.
- **Kernel RBF (Gaussiano):** Crea "isole" di decisioni attorno ai punti.

---

## Collegamenti

- [[Algoritmo Perceptron]] - Il predecessore (senza margine).
- [[Overfitting]] - Il rischio se C è troppo alto.
- [[Gradient Descent]] - Il metodo usato per minimizzare la Hinge Loss.