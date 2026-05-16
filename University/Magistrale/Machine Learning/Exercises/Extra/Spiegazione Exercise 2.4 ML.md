Ecco la soluzione dell'**Esercizio 2.4** passo dopo passo.

Questo è un classico esercizio di **Likelihood Ratio Test** con Gaussiane, molto simile a quelli d'esame. Ci insegna come i costi ($l$) e le probabilità a priori ($P(Y)$) influenzino la nostra decisione.

### 1. Impostiamo i dati

Abbiamo due classi:

- **Classe 0 ($Y=0$):** Molto comune ($P \approx 1$) e standard ($X \sim \mathcal{N}(0, 1)$).
- **Classe 1 ($Y=1$):** Evento rarissimo ($P = 10^{-6}$) ma con distribuzione spostata ($X \sim \mathcal{N}(s, 1)$).

**Loss Matrix (Costi e Guadagni):** Qui c'è una particolarità: $l(1,1) = -10^6$. Un valore negativo di loss significa un **guadagno**.

- Se indovini l'evento raro (1,1), guadagni un milione.
- Se fai un Falso Positivo (1,0), paghi solo 100.
- Se sbagli l'evento raro (0,1), non paghi nulla (0).

### 2. Calcolo della Soglia ($\eta$)

Come visto per l'esercizio precedente, il predittore ottimo è: $$ \text{Likelihood Ratio } \mathcal{L}(x) \ge \eta $$

Calcoliamo prima la parte destra ($\eta$), che contiene costi e priori: $$ \eta = \frac{[l(1,0) - l(0,0)] \cdot P(Y=0)}{[l(0,1) - l(1,1)] \cdot P(Y=1)} $$

Sostituiamo i numeri:

- **Numeratore (Costo Falso Positivo pesato):** $(100 - 0) \cdot (1 - 10^{-6}) \approx 100 \cdot 1 = \mathbf{100}$.
- **Denominatore (Guadagno Vero Positivo pesato):** $(0 - (-10^6)) \cdot 10^{-6} = 10^6 \cdot 10^{-6} = \mathbf{1}$.

Quindi la nostra soglia è: $$ \eta = \frac{100}{1} = 100 $$

_Nota intuitiva:_ Anche se l'evento è rarissimo ($10^{-6}$), il guadagno nel trovarlo è talmente alto ($10^6$) che i due fattori si cancellano al denominatore. La soglia rimane alta (100) solo perché il Falso Positivo costa 100.

### 3. Impostazione del Rapporto (Likelihood Ratio)

Ora dobbiamo soddisfare la condizione: $$ \frac{P(X=x|Y=1)}{P(X=x|Y=0)} \ge 100 $$

Sostituendo le formule delle Gaussiane (con varianza 1 e medie $s$ e $0$): $$ \frac{\frac{1}{\sqrt{2\pi}} e^{-\frac{(x-s)^2}{2}}}{\frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}} \ge 100 $$

### 4. Risoluzione (Log-Trick)

Semplifichiamo le costanti e applichiamo il logaritmo naturale ($\ln$) a entrambi i lati per eliminare gli esponenziali:

1. **Semplificazione esponenti:** $$ e^{-\frac{(x-s)^2}{2} + \frac{x^2}{2}} \ge 100 $$
    
2. **Logaritmo:** $$ -\frac{(x-s)^2}{2} + \frac{x^2}{2} \ge \ln(100) $$
    
3. **Sviluppo del quadrato:** $$ -\frac{1}{2}(x^2 - 2xs + s^2) + \frac{x^2}{2} \ge \ln(100) $$ $$ -\frac{x^2}{2} + xs - \frac{s^2}{2} + \frac{x^2}{2} \ge \ln(100) $$
    
    I termini quadratici ($x^2$) si cancellano (successo!), resta: $$ xs - \frac{s^2}{2} \ge \ln(100) $$
    

### 5. Risultato Finale

Dobbiamo isolare $x$. _Assumendo che lo spostamento $s$ sia positivo ($s > 0$)_, dividiamo tutto per $s$:

$$ x \ge \frac{s}{2} + \frac{\ln(100)}{s} $$

Il predittore ottimo è: $$ f^*(x) = \begin{cases} 1 & \text{se } x \ge \frac{s}{2} + \frac{4.6}{s} \ 0 & \text{altrimenti} \end{cases} $$

### Interpretazione Fisica

Normalmente, per distinguere due Gaussiane, taglieremmo esattamente a metà strada ($s/2$). Qui però aggiungiamo un termine positivo ($\frac{\ln(100)}{s}$). Significa che spostiamo l'asticella **più a destra**. Perché? Perché $\eta=100$ favorisce la classe 0. Nonostante il premio milionario, il costo del falso positivo (100) combinato con l'estrema rarità dell'evento ci rende comunque "prudenti": prediciamo l'evento raro solo se il segnale $x$ è molto forte.