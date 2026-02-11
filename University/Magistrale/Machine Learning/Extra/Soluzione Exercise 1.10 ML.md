Ecco la soluzione dell'**Esercizio 1.10**, spiegata in modo semplice usando solo le regole di base della probabilità (somma e prodotto).

Questo esercizio è perfetto per riprendere confidenza perché non richiede derivate o integrali, ma solo logica.

### 1. Traduciamo il problema

- **Situazione:** Abbiamo $k$ classi possibili (es. 1, 2, ..., $k$).
- **Loss Function:** È la "0-1 Loss". Significa che "paghi" 1 se sbagli, 0 se indovini.
- **Il Predittore ($f$):** È un generatore casuale. Non guarda i dati ($x$), ma tira semplicemente un dado a $k$ facce e spara una risposta a caso.
    - Probabilità di predire una classe qualsiasi ($z$): $P(z) = 1/k$.
    - Questa scelta è **indipendente** dalla vera etichetta $Y$.

### 2. Cosa dobbiamo calcolare?

Il **Rischio Atteso** ($R$) con la 0-1 Loss è semplicemente la **Probabilità di Sbagliare** (Probability of Error).

$$ R(f) = P(\text{Predizione} \neq \text{Realtà}) $$

Invece di calcolare la probabilità di sbagliare (che può avvenire in $k-1$ modi), è molto più facile calcolare la probabilità di **indovinare** e sottrarla a 1.

$$ R(f) = 1 - P(\text{Predizione} = \text{Realtà}) $$

### 3. Il Calcolo (Passo dopo passo)

Quando indoviniamo? Quando il nostro dado casuale ($Z$) esce esattamente sullo stesso valore della vera etichetta ($Y$).

Usiamo la **Legge della Probabilità Totale** (sommiamo su tutte le possibili classi reali $y$):

$$ P(\text{Indovinare}) = \sum_{i=1}^{k} P(\text{Predico } i \textbf{ E } \text{Realtà è } i) $$

Poiché il nostro predittore tira a caso ed è **indipendente** dalla realtà, la probabilità congiunta ("E") è il prodotto delle probabilità:

$$ P(\text{Predico } i \textbf{ E } \text{Realtà è } i) = \underbrace{P(\text{Predico } i)}_{1/k} \cdot \underbrace{P(\text{Realtà è } i)}_{P(Y=i)} $$

Sostituiamo nella somma: $$ P(\text{Indovinare}) = \sum_{i=1}^{k} \frac{1}{k} \cdot P(Y=i) $$

Portiamo fuori la costante $1/k$: $$ P(\text{Indovinare}) = \frac{1}{k} \underbrace{\sum_{i=1}^{k} P(Y=i)}_{\text{Somma di tutte le probabilità = 1}} $$

Quindi: $$ P(\text{Indovinare}) = \frac{1}{k} \cdot 1 = \frac{1}{k} $$

### 4. Risultato Finale

Il rischio (la probabilità di errore) è:

$$ \text{Risk} = 1 - \frac{1}{k} = \frac{k-1}{k} $$

### Sanity Check (Prova del 9)

- **Se $k=2$ (Testa o Croce):** Il rischio è $(2-1)/2 = 1/2$. Ha senso: se tiri a caso, sbagli il 50% delle volte.
- **Se $k \to \infty$:** Il rischio tende a 1. Ha senso: se devi indovinare un numero tra 1 e un milione a caso, sbaglierai quasi sicuramente.