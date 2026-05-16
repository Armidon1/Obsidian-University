Ecco la soluzione dell'**Esercizio 1.11**, basata sulla logica della classificazione binaria e della 0-1 Loss.

### 1. Impostazione del problema

- **Etichette possibili:** $Y \in {-1, 1}$.
- **Funzione di Loss:** 0-1 Loss. Significa che il rischio $R(f)$ è semplicemente la **probabilità di errore**: $$R(f) = P(f(X) \neq Y)$$
- **Predittori:**
    - $f(x)$: il predittore originale.
    - $-f(x)$: il predittore "opposto" (se $f$ dice $1$, lui dice $-1$ e viceversa).

### 2. Ragionamento Logico

Dobbiamo confrontare quando sbaglia $f$ con quando sbaglia $-f$. Poiché le classi sono solo due ($-1$ e $1$) e opposte tra loro, vale questa regola ferrea:

- **Caso A:** Se $f(x)$ indovina ($f(x) = Y$): Allora il suo opposto $-f(x)$ darà necessariamente il risultato sbagliato ($-Y \neq Y$).
    
- **Caso B:** Se $f(x)$ sbaglia ($f(x) \neq Y$): In un mondo binario ${-1, 1}$, se non è zuppa è pan bagnato. Se $f$ ha scelto l'etichetta sbagliata, allora l'altra etichetta (quella scelta da $-f$) deve per forza essere quella giusta.
    
    _Dimostrazione rapida:_ Se $Y=1$ e $f(x)=-1$ (errore), allora $-f(x)= -(-1) = 1 = Y$ (corretto).
    

### 3. Conclusione Matematica

Da quanto sopra, capiamo che l'evento "$-f$ sbaglia" è esattamente l'evento "$f$ indovina".

$$ P(-f(X) \neq Y) = P(f(X) = Y) $$

Sapendo che la somma della probabilità di sbagliare e quella di indovinare è sempre 1 ($P(\text{Errore}) + P(\text{Corretto}) = 1$):

$$ R(-f) = 1 - R(f) $$

### Interpretazione

Questo risultato ci dice che se hai un classificatore che è **terribile** (es. $R(f) = 0.99$, sbaglia il 99% delle volte), ti basta invertire le sue risposte per ottenere un classificatore **eccellente** ($R(-f) = 0.01$, sbaglia solo l'1% delle volte).

Il vero problema nel Machine Learning non è avere un predittore che sbaglia sempre (basta invertirlo), ma averne uno che sbaglia il 50% delle volte ($R(f)=0.5$), perché in quel caso anche il suo opposto sbaglierà il 50% delle volte. È l'incertezza massima.