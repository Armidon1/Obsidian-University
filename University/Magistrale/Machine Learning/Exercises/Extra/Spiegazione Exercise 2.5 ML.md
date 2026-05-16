Ecco la soluzione dell'**Esercizio 2.5** passo dopo passo.

Questo è uno degli esercizi più interessanti perché mostra come, quando le varianze sono diverse, il confine di decisione non è più una linea retta (come nell'Ex 2.4), ma diventa una forma geometrica chiusa (un cerchio/iper-sfera).

### 1. Impostazione dei Dati

- **Problema:** Classificazione binaria con 0-1 Loss.
- **Priori:** Equiprobabili $P(Y=1) = P(Y=0) = 0.5$.
- **Distribuzioni ($X \in \mathbb{R}^2$):**
    - **Classe 0:** $X|0 \sim \mathcal{N}(\mu_0, \Sigma_0)$ con $\mu_0 = \vec{0}$ e $\Sigma_0 = I$ (Identità).
    - **Classe 1:** $X|1 \sim \mathcal{N}(\mu_1, \Sigma_1)$ con $\mu_1 = \begin{pmatrix} 1 \ 1 \end{pmatrix}$ e $\Sigma_1 = \frac{1}{2}I$.

**Nota importante sulla Soglia ($\eta$):** Poiché i costi sono simmetrici (0-1 Loss) e i priori sono uguali, la soglia è semplicemente $\eta = 1$. Dobbiamo predire la Classe 1 quando: $$ P(X=x|1) \ge P(X=x|0) $$

### 2. Scrittura delle Densità

Ricordiamo la formula della Gaussiana multivariata in $d=2$ dimensioni: $$ p(x) = \frac{1}{2\pi \sqrt{|\Sigma|}} \exp\left( -\frac{1}{2} (x-\mu)^T \Sigma^{-1} (x-\mu) \right) $$

- **Per la Classe 0 ($\Sigma=I$, $|\Sigma|=1$):** $$ p(x|0) = \frac{1}{2\pi} e^{-\frac{1}{2} |x|^2} $$
    
- **Per la Classe 1 ($\Sigma=\frac{1}{2}I$, $|\Sigma|=0.25$, $\Sigma^{-1}=2I$):** Attenzione qui: il determinante è $(1/2) \cdot (1/2) = 1/4$. La radice è $1/2$. Il termine $2\pi \cdot (1/2)$ diventa $\pi$. Nell'esponente, $\Sigma^{-1}$ moltiplica per 2. $$ p(x|1) = \frac{1}{\pi} e^{-|x - \vec{1}|^2} $$ _(Nota come l'esponente non ha il $1/2$ davanti perché è stato cancellato dal 2 della matrice inversa)._
    

### 3. Impostazione della Disuguaglianza (Log-Trick)

Impostiamo $p(x|1) \ge p(x|0)$: $$ \frac{1}{\pi} e^{-|x - \vec{1}|^2} \ge \frac{1}{2\pi} e^{-\frac{1}{2} |x|^2} $$

Cancelliamo $\pi$ e passiamo ai logaritmi naturali ($\ln$) per eliminare gli esponenziali: $$ \ln(1) - |x - \vec{1}|^2 \ge \ln(1/2) - \frac{1}{2} |x|^2 $$

Sapendo che $\ln(1)=0$ e $\ln(1/2) = -\ln(2)$: $$ - |x - \vec{1}|^2 \ge -\ln(2) - \frac{1}{2} |x|^2 $$

Moltiplichiamo tutto per $-1$ (invertendo il verso della disuguaglianza) per lavorare con numeri positivi: $$ |x - \vec{1}|^2 \le \ln(2) + \frac{1}{2} |x|^2 $$

### 4. Sviluppo Algebrico (Trovare la Geometria)

Siano $x_1, x_2$ le componenti di $x$. Sviluppiamo il quadrato della norma a sinistra $|x - \vec{1}|^2$: $$ (x_1-1)^2 + (x_2-1)^2 = |x|^2 - 2(x_1+x_2) + 2 $$

Sostituiamo nella disuguaglianza: $$ |x|^2 - 2(x_1+x_2) + 2 \le \ln(2) + \frac{1}{2} |x|^2 $$

Portiamo tutti i termini $|x|^2$ a sinistra: $$ \frac{1}{2} |x|^2 - 2(x_1+x_2) \le \ln(2) - 2 $$

Moltiplichiamo tutto per 2 per pulire la frazione: $$ |x|^2 - 4(x_1+x_2) \le 2\ln(2) - 4 $$

### 5. Risultato Finale: Il Cerchio

Questa equazione ($x_1^2 + x_2^2 - 4x_1 - 4x_2 \dots$) rappresenta un **Cerchio**. Per vederlo chiaramente, usiamo il metodo del "completamento del quadrato":

$$ (x_1^2 - 4x_1 + 4) + (x_2^2 - 4x_2 + 4) - 8 \le 2\ln(2) - 4 $$ $$ (x_1 - 2)^2 + (x_2 - 2)^2 \le 4 + 2\ln(2) $$

**Il Predittore Ottimo è:** Predici **Classe 1** se il punto $x$ cade **dentro** il cerchio definito da:

- **Centro:** $C = (2, 2)$
- **Raggio al quadrato:** $R^2 = 4 + 2\ln(2) \approx 5.38$
- **Raggio:** $R \approx 2.32$

Altrimenti predici **Classe 0**.

### 6. Interpretazione Intuitiva

Perché un cerchio spostato a $(2,2)$?

- La Classe 1 è molto più "concentrata" ($\sigma^2=0.5$) rispetto alla Classe 0 ($\sigma^2=1$).
- Quando ti allontani molto dal centro, la probabilità della Classe 1 (che è "stretta") crolla a zero molto più velocemente della Classe 0 (che è "larga").
- Quindi la Classe 1 può vincere solo in una regione limitata ("un'isola") attorno al suo centro. Fuori da quell'isola, vince sempre la Classe 0 perché ha "code più lunghe".