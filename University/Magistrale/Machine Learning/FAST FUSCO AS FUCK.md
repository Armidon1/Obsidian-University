Ecco il piano d'attacco per le **Week 5** e **Week 6**, basato rigorosamente su ciò che ho trovato negli esami passati e nei tuoi appunti ("Teaching Log" e PDF).

Andiamo dritti al punto per massimizzare il punteggio con il minimo sforzo mnemonico.

---

### WEEK 5: Perceptron & SVM (L'essenziale)

L'obiettivo qui non è più calcolare una probabilità, ma tracciare una linea di confine netta tra due classi (es. -1 e +1). In questo contesto specifico (Week 5: Perceptron e SVM), le due classi sono indicate matematicamente con le etichette **${+1, -1}$**.

È una differenza importante rispetto alla Regressione Logistica della settimana scorsa (dove usavamo 0 e 1):

- **Perché usiamo +1 e -1?** Perché semplifica enormemente i calcoli basandosi sul **segno**.
- **Come funziona:** Per sapere se hai classificato bene un punto, ti basta moltiplicare l'etichetta vera ($y$) per il punteggio predetto dal modello ($x^T\theta$).
    - Se il risultato è **positivo** ($>0$), i segni sono uguali (es. $+ \times +$ oppure $- \times -$), quindi hai indovinato.
    - Se il risultato è **negativo** ($<0$), i segni sono opposti, quindi hai sbagliato.

Quindi, "classe +1" potrebbe essere "Sì/Spam" e "classe -1" "No/Non-Spam".

#### 1. Il Perceptron (Da sapere per le crocette)

È l'algoritmo base.

- **Concetto:** Se classifica bene un punto, non fa nulla. Se sbaglia, sposta la linea un po' verso quel punto per correggerlo.
- **Teorema fondamentale:** Se i dati sono separabili linearmente (c'è spazio per una retta in mezzo), il Perceptron troverà **sicuramente** una soluzione in un numero finito di passi. Non va in loop infinito.

#### 2. SVM (Support Vector Machines) - Concetto Chiave

Il Perceptron trova _una_ linea a caso. L'SVM cerca la linea **migliore**.

- **Cos'è "Migliore"?** Quella che ha il **Margine** più ampio possibile (la strada più larga che passa tra i punti delle due classi).
- **Support Vectors:** Sono i punti più vicini alla linea di confine. Solo loro contano per definire la retta; gli altri punti lontani sono irrilevanti.
- **Hinge Loss:** È la funzione di costo dell'SVM (apparsa nelle formule dei tuoi appunti): $$ L(y, f(x)) = \max(0, 1 - y \cdot f(x)) $$
    - _Significato:_ Se il punto è classificato bene e lontano dalla linea, il costo è 0. Se è classificato male o troppo vicino alla linea, il costo cresce.

#### 3. Il "Kernel Trick" (DOMANDA D'ESAME CLASSICA)

Negli esami c'è quasi sempre una domanda (es. Domanda 2 dell'Erasmus Session).

- **Il Problema:** Se i dati non sono separabili da una retta (es. un cerchio di punti rossi dentro un anello di punti blu), l'SVM fallisce.
- **La Soluzione:** Proiettiamo i dati in uno spazio a più dimensioni dove diventano separabili da un piano.
- **Il "Trick" (Trucco):** Non calcoliamo davvero le coordinate nel nuovo spazio (sarebbe lentissimo). Ci basta calcolare il **prodotto scalare** usando una funzione chiamata **Kernel** ($K(x, z)$).
- **Risposta da memorizzare:** Il Kernel Trick permette di operare in uno spazio ad alta dimensione senza calcolare esplicitamente le coordinate.

---

### WEEK 6: VC Dimension (Esercizio da 6 Punti)

Questo è l'argomento teorico più importante. Negli esami (es. Esercizio 11 Erasmus Session, Esercizio 5 First Session) chiedono spesso di calcolare la "VC dimension".

#### 1. Cos'è la VC Dimension?

Misura la "potenza" del tuo modello.

- **Shattering (Frantumazione):** Un modello "shatters" un set di punti se riesce a classificarli correttamente in **tutti** i modi possibili (tutte le combinazioni di 0 e 1).
- **Regola:** La VC Dimension è il numero massimo di punti che il modello riesce a "shatterare".

#### 2. L'Esercizio Tipo: "Intervalli" (Intervals)

Spesso l'esame chiede la VC dimension di "intervalli" o "half-intervals" sulla retta reale.

- **Caso: Intervalli chiusi $[a, b]$** (es. "Sei positivo se stai tra $a$ e $b$").
    
    - Prendiamo 2 punti: Possiamo classificarli come vogliamo? Sì.
    - Prendiamo 3 punti: Possiamo classificarli come vogliamo? No.
        - _Controesempio:_ Se hai 3 punti allineati ($x_1, x_2, x_3$) e vuoi classificare il primo e il terzo come positivi (1) e quello in mezzo come negativo (0), non puoi farlo con un unico intervallo continuo senza includere anche quello in mezzo.
    - **Risposta:** La VC Dimension degli intervalli è **2**.
- **Caso: Half-intervals $[a, + \infty)$** (es. "Sei positivo se sei maggiore di $a$").
    
    - Con 1 punto fai quello che vuoi.
    - Con 2 punti ($x_1, x_2$): Se vuoi che il primo sia 1 (positivo) e il secondo 0 (negativo), ma $x_1 < x_2$, è impossibile con una retta che dice "tutti quelli a destra sono positivi".
    - **Risposta:** La VC Dimension è **1**.

---

### EXTRA: Parte Secondaria (Reti Neurali & CNN)

Visto che hai citato la parte secondaria, ecco le 2 cose pratiche da sapere per gli esercizi "disegnati" o di calcolo che valgono punti facili.

#### 1. Formula Output CNN (Convolutional Neural Networks)

C'è spesso un esercizio (es. Esercizio 14 Erasmus Session) che ti dà Input, Kernel, Stride e Padding e chiede la dimensione dell'output. Impara questa formula a memoria:

$$ \text{Output} = \frac{(\text{Input} - \text{Kernel} + 2 \cdot \text{Padding})}{\text{Stride}} + 1 $$

- _Esempio:_ Input $10 \times 10$, Kernel $3 \times 3$, Padding $0$, Stride $2$. $$ \text{Calcolo} = \frac{(10 - 3 + 0)}{2} + 1 = \frac{7}{2} + 1 = 3.5 + 1 = 4.5 $$ (Di solito si arrotonda per difetto o i numeri sono fatti apposta per dare un intero, nell'esercizio d'esame specifico chiedeva la "shape", quindi applica la formula per altezza e larghezza).

#### 2. Disegnare una Rete Neurale (Esercizio 13)

Se ti chiedono di disegnare una rete o definire le matrici:

- **Regola Matrici:** Se un layer ha $N$ input e va verso $M$ neuroni, la matrice dei pesi $W$ sarà $M \times N$ (o $N \times M$ a seconda della convenzione, ma l'importante è che colleghi tutti con tutti).
- **Bias:** Il vettore bias ha sempre dimensione $M$ (pari al numero di neuroni del layer di arrivo).

---

### Riassunto tattico per domani:

1. **SVM:** Cerca il margine massimo. **Kernel Trick** = calcoli impliciti in alta dimensione.
2. **VC Dimension:** Impara a memoria che per gli intervalli chiusi è **2** e per le semirette è **1**.
3. **CNN:** Impara la formula $\frac{(I - K + 2P)}{S} + 1$.

Vuoi provare a risolvere insieme uno degli esercizi degli esami passati (tipo quello sulla VC dimension o sulla CNN) per essere sicuro di aver capito il meccanismo?

# week 6 2
Ho analizzato i file ufficiali che mi hai inviato ("Week 6 - ML_Fusco.pdf" e la versione estesa).

**Buone notizie:** I documenti ufficiali **confermano esattamente** i numeri e i concetti che ti avevo anticipato, ma ora abbiamo la certezza delle definizioni "alla Fusco".

Ecco il **Riassunto Ufficiale Blindato** per la Week 6. Se sai questo schema, copri sia le domande a crocette che l'eventuale esercizio teorico.

---

### 1. I "Numeri Sacri" della VC Dimension (DA MEMORIZZARE)

I PDF ufficiali elencano esplicitamente questi casi. È molto probabile che una domanda chieda uno di questi valori:

- **Intervalli (1D):** VC-dim = **2**.
- **Rettangoli allineati agli assi (2D):** VC-dim = **4**.
- **Triangoli (2D):** VC-dim = **7**.
- **Famiglia finita di classificatori ($H$):** VC-dim $\le \log_2 |H|$.

**Concetto chiave per le crocette:**

- **Shattering:** Una famiglia di modelli "frantuma" (shatters) un set di punti se riesce a classificarli in **tutti** i modi possibili (tutte le combinazioni di etichette 0/1).
- **VC Dimension:** È la dimensione del set **più grande** che il modello riesce a "shatterare".
- **Relazione coi Dati:** Il numero di dati necessari ($n$) cresce **linearmente** con la VC dimension $d$. (Più il modello è complesso/potente, più dati servono).

---

### 2. Risk Decomposition (I 3 Errori)

Secondo il PDF, l'errore totale di un modello si scompone in tre parti. Nelle crocette chiedono spesso le definizioni:

1. **Bayes Error:** L'errore minimo inevitabile (rumore intrinseco nei dati). Non possiamo ridurlo.
2. **Approximation Error (Bias):** L'errore dovuto al fatto che il nostro modello è "troppo semplice" per capire la realtà (es. usare una retta per dati curvi). Si riduce usando modelli più complessi ($H$ più grande).
3. **Estimation Error (Variance):** L'errore dovuto al fatto che abbiamo dati finiti e potremmo non trovare il miglior modello possibile. Si riduce avendo **più dati** o usando modelli **meno complessi**.

**Il Trade-off:**

- Modello Complesso (Alta VC-dim) $\rightarrow$ Basso Bias, Alta Varianza.
- Modello Semplice (Bassa VC-dim) $\rightarrow$ Alto Bias, Bassa Varianza.

---

### 3. Decision Trees (Alberi)

Ecco i punti tecnici estratti dai PDF per le domande specifiche:

- **Overfitting:** Un albero senza limiti di profondità può classificare perfettamente qualsiasi training set (Errore = 0) isolando ogni punto in una foglia, ma così facendo **overfitta** terribilmente.
- **Impurity (Funzioni di Costo):** Per decidere come dividere i nodi, usiamo funzioni che devono essere **concave**. Le due citate da Fusco sono:
    1. **Gini Index:** $\psi_G(z) = 2z(1-z)$.
    2. **(Scaled) Entropy:** Basata sui logaritmi.
- **Algoritmo Greedy:** L'algoritmo standard non trova l'albero ottimo (che sarebbe troppo difficile), ma ne trova uno "abbastanza buono" dividendo i nodi passo dopo passo.
- **Random Forests:** Uniscono tanti alberi allenati su sottoinsiemi di dati per ridurre la **varianza** e migliorare la generalizzazione.

---

### Sintesi Operativa per domani

Se ti chiedono:

- VC dei triangoli? Rispondi **7**.
- VC degli intervalli? Rispondi **2**.
- Perché limitiamo la profondità degli alberi? Per evitare l'**overfitting** (o Estimation Error alto).
- Come scala la complessità dei campioni? Linearmente con la **VC-dimension**.

Questo è tutto ciò che c'è nei file ufficiali che valga la pena memorizzare ora. Vai tranquillo!