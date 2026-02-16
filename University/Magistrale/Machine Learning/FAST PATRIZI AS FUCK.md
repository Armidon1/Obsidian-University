Capisco la tua preoccupazione. Basarsi solo su due sessioni d'esame è tecnicamente un rischio, ma data la tempistica (48 ore), è **l'unica strategia sensata**. Patrizi e Fusco tendono a essere metodici: se una tipologia di esercizio compare in entrambi gli esami (come il disegno della rete o il calcolo CNN), è quasi certo che ci sarà.

Ecco la **Lista di Sopravvivenza** per la parte di Patrizi. Ho diviso tra "Sicuro al 99%" (visto negli esami) e "Paracadute" (presente nel Teaching Log ma non ancora uscito, da leggere velocemente).

---

### 1. Neural Networks (Feedforward) - **PRIORITÀ MASSIMA**

È l'esercizio "creativo" da 6 punti. Devi saper passare dal testo al disegno/matrice.

- **Disegno & Matrici (Esercizio pratico):**
    - Se hai un layer con $N$ input e uno con $M$ neuroni, la **matrice dei pesi $W$** ha dimensione **$M \times N$** (righe $\times$ colonne).
    - Il **vettore Bias $b$** ha dimensione **$M$** (tanti quanti i neuroni di arrivo).
    - _Esempio:_ Input $\mathbb{R}^6 \to$ Hidden 6 unità. Matrice $W$: $6 \times 6$. Bias: $6$.
- **Funzioni di Attivazione (Crocette):**
    - **Hidden Layers:** Usa quasi sempre **ReLU**.
    - **Output Layer (Regressione):** Usa **Linear** (nessuna attivazione).
    - **Output Layer (Classificazione Binaria):** Usa **Sigmoid**.
    - **Output Layer (Classificazione Multiclasse):** Usa **Softmax**.
- **Definizione Backpropagation (Crocetta):**
    - Serve a calcolare il **gradiente** della funzione di costo rispetto ai parametri. (Non serve ad aggiornare i pesi, quello lo fa l'SGD; la backprop calcola solo la direzione).

### 2. CNN (Convolutional Neural Networks) - **PRIORITÀ MASSIMA**

È l'esercizio di calcolo da 5 punti + teoria.

- **Calcolo Output (Formula da sapere a memoria):** $$ O = \frac{I - K + 2P}{S} + 1 $$ ($I$=Input, $K$=Kernel, $P$=Padding, $S$=Stride).
    - _Attenzione:_ Se l'esercizio chiede la "shape" (forma), devi dare (Altezza, Larghezza, Canali). Il numero di canali di uscita è uguale al numero di filtri (kernels) usati.
- **Max Pooling (Crocetta):**
    - È un'operazione di **downsampling** (riduce la dimensione spaziale). Serve a ridurre i calcoli e dare invarianza alle piccole traslazioni.
- **Perché le CNN sono meglio delle reti dense per le immagini?**
    - _Parameter Sharing:_ Usano gli stessi pesi (kernel) su tutta l'immagine.
    - _Local Connectivity:_ Guardano solo i pixel vicini.

### 3. Clustering (K-Means) - **ALTA PRIORITÀ**

Visto sia come esercizio grafico che come crocetta.

- **Esecuzione K-Means (Esercizio grafico):**
    - Step 1 (**Assignment**): Assegna ogni punto al centroide più vicino (colora i punti). _Trucco:_ Traccia la linea a metà tra i due centroidi; chi sta di qua è A, chi sta di là è B.
    - Step 2 (**Update**): Sposta il centroide nel "centro esatto" (media) dei punti appena colorati.
- **Obiettivo K-Means (Crocetta):**
    - Minimizza la **somma delle distanze quadratiche** tra i punti e i loro centroidi assegnati.
- **Dendrogramma (Crocetta):**
    - È un "albero dei cluster". È l'output del **Clustering Gerarchico**, _NON_ del K-Means.

### 4. Regularization & Boosting - **ALTA PRIORITÀ**

Solo crocette, ma escono sempre.

- **Regularization (Definizione):**
    - Serve a prevenire l'**Overfitting**.
- **Dropout:**
    - È una tecnica di regolarizzazione per Reti Neurali (spegne neuroni a caso durante il training).
- **AdaBoost:**
    - Un algoritmo che combina "weak learners" (modelli deboli, poco meglio del caso) per crearne uno forte. Lavora sequenzialmente (corregge gli errori del precedente).

---

### 5. Il "Paracadute" (Cose nel programma ma non negli esami)

Dato che temi la sorpresa, ecco 3 definizioni flash da leggere _solo se ti avanza tempo_, basate sul Teaching Log:

1. **Autoencoders:** Sono reti che copiano l'input nell'output ($x \to x$) passando per un "collo di bottiglia" compresso. Servono per la riduzione della dimensionalità (come la PCA ma non lineare).
2. **PCA (Principal Component Analysis):** Riduzione dimensionale non supervisionata. Cerca le direzioni di massima varianza. È una trasformazione lineare.
3. **KNN (K-Nearest Neighbors):**
    - È un algoritmo "Pigro" (Lazy): non impara un modello, memorizza solo i dati.
    - Per classificare un nuovo punto, guarda i $K$ vicini e fa la maggioranza.
    - Soffre la "Maledizione della dimensionalità" (funziona male se hai troppe feature).

### Sintesi della Strategia

1. Impara a memoria la **formula CNN**: $\frac{I-K+2P}{S}+1$. (5 punti sicuri).
2. Impara a disegnare la rete neurale e scrivere le dimensioni matrici **$M \times N$**. (6 punti sicuri).
3. Ricorda le definizioni per le crocette: **Backprop = Gradiente**; **Max Pooling = Downsampling**; **Regularization = No Overfitting**; **Dendrogram = Albero**.

Se sai fare queste 3 cose, hai già in tasca circa 15-16 punti solo sulla parte di Patrizi. Uniscili ai 12-14 punti "facili" di Fusco (VC dimension intervalli + Derivata OLS/Loss) e l'esame è passato.

Capisco che vedere richieste di "disegnare" senza riferimenti chiari metta ansia. Stai tranquillo: si tratta semplicemente di rappresentare graficamente l'architettura della rete (cerchi e frecce).

Le "cose da disegnare" si riferiscono alle **Feedforward Neural Networks** (Reti Neurali).

Ecco esattamente **dove guardare** nelle fonti che mi hai mandato e **come svolgere l'esercizio** per prendere i punti pieni.

### 1. Dove guardare (La "Bibbia" visiva)

Apri il file **`neural_networks.pdf`**. Le figure chiave sono queste:

- **Pagina 29, Figura 3.4:** Ti mostra il concetto base. Input a sinistra, Output a destra, frecce in mezzo.
- **Pagina 36, Figura 3.12 (IMPORTANTE):** Questa è la rappresentazione standard che devi imparare.
    - **Input Layer ($x$):** I cerchi a sinistra.
    - **Hidden Layer ($h$):** I cerchi al centro.
    - **Output Layer ($y$):** I cerchi a destra.
    - **Weights (Pesi):** Le frecce che collegano _ogni_ cerchio di uno strato a _tutti_ i cerchi dello strato successivo.
- **Pagina 48, Figura 4.6:** Questa ti serve per capire la **Notazione Matriciale** (che negli esami chiedono sempre insieme al disegno).

### 2. Come si risolve l'Esercizio (Passo dopo Passo)

Prendiamo l'**Esercizio 13 dell'Erasmus Session** come esempio pratico. _Testo:_ "Design a Feedforward Neural Network... Input $\mathbb{R}^6$, First hidden layer 6 units, Second hidden layer 4 units. Classification binary."

Ecco cosa devi fare sul foglio:

#### A. Il Disegno (Graphical Representation)

1. **Disegna la colonna Input:** Disegna una colonna verticale di **6 cerchi** (perché l'input è $\mathbb{R}^6$). Etichettali $x_1...x_6$.
2. **Disegna il 1° Hidden Layer:** A destra, disegna una colonna di **6 cerchi**. Etichettali $h^{(1)}$.
3. **Disegna il 2° Hidden Layer:** A destra, disegna una colonna di **4 cerchi**. Etichettali $h^{(2)}$.
4. **Disegna l'Output Layer:** Poiché è "binary classification", ti basta **1 cerchio** finale (o 2 se usi la Softmax, ma per binaria basta 1 con sigmoide). Etichettalo $y$.
5. **Collega tutto:** Traccia frecce che vanno da _ogni_ cerchio dell'input a _ogni_ cerchio del primo hidden, poi dal primo al secondo, e infine all'output.

#### B. La Notazione Matriciale (Matrix Notation) - Punti Facili

L'esame chiede "size of parameter matrix" e "size of bias vector". Usa questa regola d'oro presente nel file `neural_networks.pdf`:

Se uno strato ha **$N$ neuroni in entrata** e va verso uno strato con **$M$ neuroni in uscita**:

- La Matrice dei Pesi $W$ (o $\Omega$) è grande **$M \times N$** (Righe $\times$ Colonne).
- Il Vettore Bias $b$ (o $\beta$) è grande **$M$** (vettore colonna).

**Applicazione all'esercizio Erasmus:**

1. **Da Input (6) a Hidden 1 (6):**
    - Matrice $W_1$: dimensione **$6 \times 6$**.
    - Bias $b_1$: dimensione **$6$**.
    - Attivazione: **ReLU** (standard per gli hidden layer).
2. **Da Hidden 1 (6) a Hidden 2 (4):**
    - Matrice $W_2$: dimensione **$4 \times 6$** (4 destinazioni, 6 partenze).
    - Bias $b_2$: dimensione **$4$**.
    - Attivazione: **ReLU**.
3. **Da Hidden 2 (4) a Output (1):**
    - Matrice $W_3$: dimensione **$1 \times 4$**.
    - Bias $b_3$: dimensione **$1$**.
    - Attivazione: **Sigmoid** (perché è classificazione binaria).

### Sintesi estrema per domani

Se ti chiedono di "disegnare l'architettura":

1. Fai i pallini in colonna (Input $\to$ Hidden $\to$ Output).
2. Metti le frecce "tutti con tutti".
3. Scrivi le dimensioni delle matrici come **(Neuroni Arrivo $\times$ Neuroni Partenza)**.

Vai a guardare la **Figura 3.12** nel PDF ora, ti chiarirà tutto in un secondo.