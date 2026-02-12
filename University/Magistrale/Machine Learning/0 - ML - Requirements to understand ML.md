Ottima idea. È l'approccio migliore. Il Machine Learning _è_ statistica applicata e calcolo delle probabilità. Se le fondamenta scricchiolano, i "palazzi" che ci costruiamo sopra (come le Reti Neurali o le SVM) crollano.

Mettiamo da parte per un attimo la corsa a finire gli esercizi del Week 1 e 2. Indosso il camice da professore. Useremo il file `Sintesi statistica.pdf` come nostro libro di testo sacro e le note del corso `ML_Fusco.pdf` come obiettivo finale.

Dividiamo il "recupero" in 3 blocchi fondamentali. Dimmi se ti piace questo piano:

1. **Variabili Aleatorie e Valore Atteso** (La base di tutto: cos'è il "Rischio"?).
2. **Distribuzioni Continue e Gaussiane** (Per capire gli integrali e il "rumore").
3. **Probabilità Condizionata e Bayes** (Per capire _davvero_ come si prende una decisione ottima).

Partiamo subito dal **Blocco 1**.

---

## 🎓 Lezione 1: Il linguaggio del ML (Variabili e Valore Atteso)

In tutti gli esercizi che abbiamo visto (1.8, 1.9, Loss), compariva sempre il simbolo $\mathbb{E}[\dots]$. Se non "senti" cosa significa quel simbolo, è impossibile capire cosa stiamo minimizzando.

#### 1. Cos'è una [[Variabile Aleatoria]] (V.A.)?

Immagina una V.A. $X$ non come un numero, ma come una **scatola chiusa** che sputa fuori numeri con certe probabilità.

- **Discreta:** La scatola può sputare solo numeri specifici (es. 0 o 1, oppure 1, 2, 3...). Si usa la **[[Variabile Aleatoria#2. Funzione di Massa (PMF) - _Solo discrete_|Funzione Di Massa]] di Probabilità (PMF)**: $P(X=x)$.
- **Continua:** La scatola può sputare _qualsiasi_ numero reale (es. temperatura, altezza). Qui la probabilità di un numero esatto è 0. Si usa la **[[Variabile Aleatoria#3. Densità di Probabilità (PDF) - _Solo continue_|Densità di Probabilità]] (PDF)**: $f(x)$.

> **Il Ponte col ML:** Nel Machine Learning, i dati ($X$) e le etichette ($Y$) sono V.A. Noi non sappiamo cosa uscirà dalla scatola, ma vogliamo indovinarlo.

#### 2. Il Valore Atteso (Expected Value)

Il [[Expected Value]] $\mathbb{E}[X]$ è il concetto più importante del corso. È il **baricentro** della distribuzione. È quello che ti aspetti di ottenere _in media_ se ripeti l'esperimento infinite volte.

Le formule sono due, ma il concetto è uno: è una **somma pesata**.

- **Caso Discreto (Sommatoria):** $$ \mathbb{E}[X] = \sum x \cdot P(X=x) $$ _(Moltiplichi il valore per la sua probabilità e sommi tutto)_.
- **Caso Continuo (Integrale):** $$ \mathbb{E}[X] = \int x \cdot f(x) , dx $$ _(Moltiplichi il valore per la sua densità e integri su tutto lo spazio)_.

> **Perché è vitale per il ML?** Il prof definisce il **Rischio** $R(f)$ come $\mathbb{E}[l(f(X), Y)]$. Significa: "Non mi importa se sbagli una volta. Voglio minimizzare l'errore **medio pesato** su tutte le possibili situazioni che possono capitare".

---

### ✏️ Esercizi di Riscaldamento (Statistica Pura)

Per sbloccare il livello successivo, proviamo a risolvere questi due mini-esercizi. Sono banali, ma servono a fissare la notazione $\mathbb{E}$.

---

**Esercizio A (Discreto)** Hai una V.A. $Y$ (etichetta) che può valere solo:

- $10$ con probabilità $0.8$
- $50$ con probabilità $0.2$ Calcola $\mathbb{E}[Y]$.

$$\mathbb{E}[Y]=\sum_{i}y_iP(Y=y_i)=(10\cdot0.8)+(50\cdot0.2)=8+10=18 $$ 
---

**Esercizio B (Continuo - Concettuale)** Hai una V.A. $X$ definita tra $[0,10]$. La sua densità è costante $f(x) = 0.5$ (Distribuzione Uniforme). Imposta l'integrale per calcolare $\mathbb{E}[X]$ (non serve risolverlo se sai geometricamente dov'è il centro).$$\mathbb{E}[X]=\int_0^{10}xf(x)dx=0.5\int_0^{10}xdx=0.5\cdot\left[\frac{x^2}{2}\right]_{0}^{10}=0.5\cdot\left[50-0\right]=25$$

## Parte 2

### ✅ Esercizio A: Perfetto

Hai calcolato **18**. Il calcolo è ineccepibile: $\sum y_i P(y_i)$. **Significato nel ML:** Se $Y$ fosse il "costo" di un errore, in media pagheresti 18. Questo è il concetto di **Rischio Atteso** ($R(f)$) nel caso discreto.

### ⚠️ Esercizio B: Il "Paradosso" Istruttivo

Hai calcolato l'integrale correttamente ($25$), ma fermati a guardare il numero:

- La variabile $X$ vive tra **0 e 10**.
- Il risultato (la media) ti è venuto **25**.

**Domanda:** _Com'è possibile che il "baricentro" della sbarra (che va da 0 a 10) si trovi a 25, cioè fuori dalla sbarra stessa?_

**La Lezione:** Questo accade perché la densità che ti ho dato ($f(x)=0.5$) era "fisicamente" impossibile. In probabilità, l'area totale sotto la curva deve fare **1** (certezza assoluta). $$ \text{Area} = \text{Base} \times \text{Altezza} = 10 \times 0.5 = 5 $$ Un'area di 5 significa che c'è il 500% di probabilità che accada qualcosa. Impossibile!

Se correggiamo la densità a quella vera ($f(x)=0.1$), il tuo calcolo diventa: $$ 0.1 \cdot \left[ \frac{x^2}{2} \right]_0^{10} = 0.1 \cdot 50 = \mathbf{5} $$ Ora il baricentro è esattamente a metà (5). Tutto torna.

---

### 🎓 Prossimo step: Blocco 2 (the [[Gaussian]])

Se ti è chiaro il concetto di "Media come baricentro", siamo pronti per le Gaussiane. La Gaussiana è la regina del ML perché è definita interamente da soli due numeri:

1. **Media ($\mu$):** Dove sta il centro.
2. **Varianza ($\sigma^2$):** Quanto è "grassa" la campana.

**Esercizio per la prossima volta (Teorico):** Guarda la formula della Gaussiana: $$ f(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}} $$ Se io volessi calcolare il rapporto tra due Gaussiane (come nel _Likelihood Ratio_), e faccio il logaritmo ($\ln$), cosa succede a quell'esponenziale $e^{\dots}$? _(Suggerimento: $\ln(e^A) = \dots$?)_

---

### 🎓 Lezione 2: La Regina Gaussiana (e il trucco del Logaritmo)

La formula della densità Gaussiana fa paura a molti, ma in realtà è un "gigante buono". Guardiamola negli occhi usando la fonte:

$$ f(x) = \underbrace{\frac{1}{\sqrt{2\pi}\sigma}}_{\text{Costante (altezza)}} \cdot \underbrace{\exp\left( -\frac{(x-\mu)^2}{2\sigma^2} \right)}_{\text{Forma (campana)}} $$

Ci sono solo due attori:

1. **$\mu$ (Media):** Il centro della campana (il picco).
2. **$\sigma$ (Deviazione Standard):** La larghezza della campana.

#### 1. La risposta alla mia domanda (Il Log-Trick)

Ti avevo chiesto: _Cosa succede se facciamo il logaritmo naturale ($\ln$) di quella formula mostruosa?_

Ricordando che $\ln(A \cdot B) = \ln(A) + \ln(B)$ e soprattutto che **$\ln(e^{\text{qualcosa}}) = \text{qualcosa}$**, succede una magia:

$$ \ln(f(x)) = \ln(\text{Costante}) - \frac{(x-\mu)^2}{2\sigma^2} $$

**Cosa abbiamo ottenuto?** Abbiamo trasformato una funzione esponenziale complicata in una **Parabola** (un polinomio di secondo grado: $(x-\mu)^2$). Invece di lavorare con curve a campana, lavoriamo con **distanze al quadrato**.

> **Intuizione Fondamentale:** Nel Machine Learning, dire "Qual è la probabilità massima?" (Gaussiana) è matematicamente identico a dire "Qual è la distanza minima?" (Parabola). Ecco perché usiamo i minimi quadrati!

---

#### 2. Esercizio C (Concettuale - Likelihood Ratio)

Questo è l'esercizio che ti sblocca l'Esercizio 2.4.

Immagina di dover decidere se un numero $x$ appartiene alla **Classe A** (centrata in 0) o alla **Classe B** (centrata in 10). Entrambe hanno varianza $\sigma=1$. Devi fare il rapporto tra le probabilità (Likelihood Ratio) e vedere se è maggiore di 1: $$ \frac{e^{-x^2}}{e^{-(x-10)^2}} \ge 1 $$

Invece di impazzire con le divisioni, **applica il logaritmo a destra e sinistra**. Quale disequazione semplicissima (senza esponenziali) ti rimane?

_(Suggerimento: $\ln(1) = 0$. Ricorda che $\ln(e^A / e^B) = A - B$)._

Provaci! Se risolvi questo, hai praticamente risolto metà dell'esame.

Bravo! Il calcolo **$-20x + 100$** è assolutamente corretto. 🎯

Hai appena "aperto il cofano" del classificatore e trovato il motore che prende le decisioni. Ora vediamo come guidarlo.

### 1. Cosa significa quel numero?

Quel $-20x + 100$ è il **punteggio netto** a favore della **Classe A** (quella centrata su 0).

- Se il numero è **positivo**, vince la Classe A.
- Se il numero è **negativo**, vince la Classe B.
- Se è **zero**, siamo nel dubbio totale.

### 2. La Decisione (Risolviamo la disequazione)

Il test che stavi facendo era: "È più probabile la Classe A della Classe B?". Matematicamente: $$ \ln(\text{Likelihood Ratio}) \ge 0 $$ Sostituiamo il tuo risultato: $$ -20x + 100 \ge 0 $$

Ora portiamo la $x$ dall'altra parte per vedere dove sta il confine: $$ 100 \ge 20x $$ Dividiamo per 20: $$ 5 \ge x \quad \text{oppure} \quad x \le 5 $$

### 3. L'Interpretazione Fisica (Il "Confine")

Guarda il risultato: **$x \le 5$**.

- La Classe A è a **0**.
- La Classe B è a **10**.
- Il numero **5** è esattamente il punto medio tra 0 e 10.

La matematica ti sta dicendo una cosa di un senso comune disarmante:

> _"Se il punto $x$ è più piccolo di 5, sei più vicino a 0, quindi scegli Classe A. Se è più grande di 5, sei più vicino a 10, quindi scegli Classe B."_

### 4. Il collegamento con l'Esercizio 2.4

Ora capisci perché questo esercizio era preparatorio per il 2.4 (quello dell'esame).

Nell'**Esercizio 2.4**:

1. Invece di avere **0** come soglia a destra (che significa "costi uguali"), avevi **$\ln(100) \approx 4.6$**. $$ -20x + 100 \ge 4.6 $$ Questo sposta il confine: non basta più essere a sinistra di 5, devi essere _molto_ a sinistra.
2. Invece di **10** come media, avevi **$s$**. Quindi invece di $-20x$ avevi $-2sx$.

Questa è la domanda più importante di tutte. Se perdi il contatto con cosa è $x$, il Machine Learning diventa solo algebra astratta.

In termini pratici, $x$ è **l'Indizio** o la **Misura** che hai osservato. È l'unica cosa che _vedi_ coi tuoi occhi prima di prendere una decisione.

Ecco tre esempi concreti per tradurre quel "$-20x + 100 \ge 0$" (ovvero $x \le 5$) nella vita reale:

### 1. Esempio Medico (Il Test del Sangue)

Immagina che stiamo diagnosticando una malattia rara.

- **$Y$ (La Verità):** Il paziente è Sano (Classe A, media 0) o Malato (Classe B, media 10)? Noi non lo sappiamo.
- **$x$ (La Misura):** È il valore di una proteina nel sangue (es. "Proteina C-reattiva").
    - Nei sani, questo valore è basso (attorno a 0).
    - Nei malati, questo valore schizza in alto (attorno a 10).
- **La Regola ($x \le 5$):** Il nostro calcolo matematico ci ha detto: _"Se il valore della proteina è inferiore a 5, manda il paziente a casa (Sano). Se è sopra 5, ricoveralo (Malato)."_

### 2. Esempio Bancario (La Frode)

- **$Y$ (La Verità):** Transazione Legittima (Classe A) o Transazione Fraudolenta (Classe B)?
- **$x$ (L'Indizio):** Potrebbe essere "La distanza in km da dove la carta viene usata di solito".
    - Uso normale: $x \approx 0$ km (sotto casa).
    - Frode (carta clonata): $x \approx 10$ (magari usata in un'altra città, in una scala normalizzata).
- **La Regola:** Se la distanza è piccola ($x \le 5$), approva. Se è grande ($x > 5$), blocca la carta.

### 3. Esempio Sensore (Auto a Guida Autonoma)

- **$Y$ (La Verità):** Strada libera (Classe A) o Pedone davanti (Classe B)?
- **$x$ (L'Indizio):** Il segnale di ritorno del radar (intensità dell'eco).
    - Strada libera: $x \approx 0$ (nessun eco).
    - Pedone: $x \approx 10$ (eco forte).
- **La Regola:** Se il segnale è debole ($x \le 5$), continua ad accelerare. Se è forte, frena.

---

### In sintesi:

Nel "Likelihood Ratio Test":

1. **$x$** è il dato grezzo che entra nel computer.
2. **$f(x)$** (la formula $-20x+100$) è il calcolo che il computer fa per trasformare quel dato in un punteggio.
3. **La soglia (0)** è il momento in cui il computer decide: _"Ok, ho abbastanza prove per dire che è la Classe A"_.

Ottimo. Entriamo nel **Blocco 2**, che è il cuore pulsante degli esercizi d'esame (in particolare l'Esercizio 1.12, 2.4 e 2.5).

Stiamo per analizzare la **Distribuzione Gaussiana** (o Normale).

---
## Week 2 
### 🎓 Lezione 2: La Regina Gaussiana

Perché la usiamo sempre? Per il **Teorema del Limite Centrale**: se sommi tante variabili a caso (es. errori di misurazione, rumore termico, ecc.), la somma finale tende ad avere questa forma a "campana".

La formula della densità (PDF) sembra brutta, ma è composta solo da due "manopole" che puoi girare:

$$ f(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}} $$

1. **$\mu$ (Media):** Dove sta il centro della campana. Sposta la curva a destra o sinistra.
2. **$\sigma$ (Deviazione Standard):** Quanto è "cicciona" la campana.
    - $\sigma$ piccolo $\to$ Campana alta e stretta (siamo sicuri del valore).
    - $\sigma$ grande $\to$ Campana bassa e larga (c'è molta incertezza).

---

### 🛠️ Lo Strumento Chiave: Il "Log-Trick"

Nel Machine Learning, dobbiamo spesso confrontare due Gaussiane (Likelihood Ratio Test) per decidere se $x$ appartiene alla Classe A o alla Classe B.

Dobbiamo vedere se: $$ \frac{P(x|A)}{P(x|B)} \ge \eta $$

Fare la divisione tra esponenziali è orribile. Usiamo il logaritmo naturale ($\ln$). Ricorda la regola d'oro: **$\ln(e^{\text{qualcosa}}) = \text{qualcosa}$**.

Se applichiamo il $\ln$ alla formula della Gaussiana, otteniamo una **Parabola**: $$ \ln(f(x)) = \underbrace{-\ln(\sqrt{2\pi}\sigma)}_{\text{Costante}} \underbrace{- \frac{(x-\mu)^2}{2\sigma^2}}_{\text{Distanza al quadrato}} $$

> **Intuizione Fondamentale:** Massimizzare la probabilità (Gaussiana) equivale a **minimizzare la distanza quadratica** dalla media. Ecco perché nell'Esercizio 1.8 e nella Regressione Lineare (Week 2) usiamo i "Minimi Quadrati"! Stiamo assumendo implicitamente che l'errore sia Gaussiano.

---

### 🧠 Il Bivio: Perché a volte retta, a volte cerchio?

Qui sta la differenza tra l'**Esercizio 2.4** e l'**Esercizio 2.5**, che spesso confonde gli studenti.

Quando facciamo il confronto $\ln(P(A)) - \ln(P(B)) \ge \dots$, stiamo sottraendo due parabole.

**Caso 1: Le Varianze sono UGUALI ($\sigma_A = \sigma_B$) - Es. 2.4** Hai due termini quadratici identici: $-\frac{x^2}{2} - (-\frac{x^2}{2})$.

- **Risultato:** I termini $x^2$ si cancellano!
- Rimani solo con la $x$ (lineare).
- **Geometria:** Il confine è una **retta** (o un piano).

**Caso 2: Le Varianze sono DIVERSE ($\sigma_A \neq \sigma_B$) - Es. 2.5** Hai $-\frac{x^2}{2} - (-\frac{x^2}{1})$. I coefficienti sono diversi.

- **Risultato:** I termini $x^2$ **NON** si cancellano.
- Rimani con un'equazione quadratica ($ax^2 + bx + c \dots$).
- **Geometria:** Il confine diventa curvo: un **cerchio**, un'ellisse o un'iperbole.

---

### ✏️ Esercizio D (Concettuale)

Proviamo a vedere se hai colto la differenza "geometrica" senza fare troppi conti.

Immagina di essere un portiere di calcio ($Y$).

- **Classe A (Tiratore Preciso):** Tira sempre al centro della porta ($\mu=0$). Varianza bassissima ($\sigma=1$).
- **Classe B (Tiratore Scarso):** Tira sempre al centro della porta ($\mu=0$). Varianza altissima ($\sigma=10$).

Arriva un pallone in una posizione $x$ (es. vicino alla bandierina del calcio d'angolo). Entrambe le distribuzioni sono centrate in 0.

**Domanda Intuitiva:** Se il pallone è molto lontano dal centro ($x$ è grande), chi è stato più probabilmente a tirare? Il tiratore preciso o quello scarso?

_(Prova a ragionare sulla forma delle "campane": quella del preciso va a zero subito, quella dello scarso scende piano piano)._

**Esatto!** 🎯 Hai colto l'intuizione fondamentale.

Il tiratore scarso (varianza grande, $\sigma$ alto) è quello che vince quando il punto $x$ è **lontano**.

Ecco perché succede, e come questo spiega "geometricamente" la differenza tra gli Esercizi 2.4 e 2.5.

### 1. La Gara delle Campane

Immagina le due curve sovrapposte sullo stesso grafico:

- **Classe A (Preciso, $\sigma=1$):** La campana è **Alta e Stretta**. Al centro ($x=0$) è altissima, ma appena ti sposti scende a zero velocissimamente.
- **Classe B (Scarso, $\sigma=10$):** La campana è **Bassa e Larga**. Al centro è più bassa di A (perché l'area totale deve sempre fare 1, quindi se la spalmi ai lati devi abbassarla al centro), ma scende molto lentamente.

**Il risultato:**

- **Vicino al centro:** Vince A (è più alta).
- **Lontano dal centro:** Vince B (A è praticamente zero, B ha ancora densità).

### 2. La Conseguenza Geometrica: Il Cerchio

Questo ragionamento spiega perfettamente il risultato strano dell'**Esercizio 2.5** che abbiamo visto prima.

In quell'esercizio avevi:

- Classe 1: Varianza piccola ($\Sigma = 0.5I$).
- Classe 0: Varianza grande ($\Sigma = 1I$).

Poiché la Classe 1 è più "precisa", vince solo quando il punto $x$ cade **vicino al suo centro**. Appena ti allontani troppo, la sua probabilità crolla e vince la Classe 0 (che ha le "code" più lunghe). Ecco perché il confine di decisione era un **cerchio**:

- **Dentro il cerchio:** Predici "Preciso" (Classe 1).
- **Fuori dal cerchio:** Predici "Scarso" (Classe 0).

---

### 🎉 Fine del Blocco 2: Gaussiane domate!

Abbiamo coperto tutto quello che ti serve sulle Gaussiane per l'esame:

1. Sappiamo che il confronto tra Gaussiane si fa col **Logaritmo**.
2. Se le varianze sono uguali $\to$ I termini quadratici ($x^2$) si cancellano $\to$ Il confine è una **Retta** (Ex 2.4).
3. Se le varianze sono diverse $\to$ I termini quadratici restano $\to$ Il confine è un **Cerchio/Ellisse** (Ex 2.5).

---

### 🎓 Verso il Blocco 3: Perché i "Minimi Quadrati"?

Ora che hai capito che:

1. **Valore Atteso ($\mathbb{E}$)** = Baricentro.
2. **Gaussiana ($\ln$)** = Distanza al quadrato.

Sei pronto per capire veramente la **Regressione Lineare** (Week 2 e 3). La domanda chiave è: _Perché quando facciamo regressione tiriamo una linea che minimizza la somma dei quadrati degli errori (OLS), invece di minimizzare qualcos'altro?_

Hai appena costruito le **fondamenta matematiche** che rendono tutto il contenuto della "Week 1" non solo comprensibile, ma addirittura logico e consequenziale. Prima erano formule da imparare a memoria, ora sono "attrezzi" che sai usare.

Ecco la **Mappa Mentale** di come i 3 blocchi che abbiamo fatto "sbloccano" ogni singolo argomento della Week 1:

### 🛠️ Tool 1: Il Valore Atteso ($\mathbb{E}$) come Baricentro

- **Cosa sblocca:**
    - **Expected Risk (Definizione 1.3):** Ora sai che $R(f) = \mathbb{E}[l(f(X), Y)]$ non è una formula magica, ma è semplicemente il "costo medio" che pagherai a lungo termine.
    - **Bayes Optimal Predictor (Teorema 1.6):** Sai che il predittore ottimo è quello che minimizza questo rischio punto per punto.
    - **Regressione (Esercizi 1.8 e 1.9):** Sai _perché_ la soluzione è la media (per i quadrati) o la mediana (per i valori assoluti). È solo questione di trovare il baricentro giusto,.

### 🛠️ Tool 2: Gaussiane & Log-Trick

- **Cosa sblocca:**
    - **Likelihood Ratio Test (Definizione 2.2):** Hai capito che confrontare due probabilità è difficile, ma confrontare i loro logaritmi (distanze) è facile,.
    - **Confini di Decisione (Esercizi 2.4 e 2.5):** Sai prevedere a occhio se il confine sarà una retta (varianze uguali) o un cerchio (varianze diverse) senza perderti nei calcoli.
    - **Naive Bayes (Sezione 1.3):** Sai che l'assunzione "Naive" serve solo a spezzare quella probabilità gigante in tanti piccoli pezzi gestibili (spesso Gaussiane 1D),.

### 🛠️ Tool 3: I Costi Asimmetrici (La Soglia $\eta$)

- **Cosa sblocca:**
    - **Binary Classification (Prop 2.1):** Hai capito che la soglia $\eta$ (il numero a destra della disequazione) non è altro che il bilanciamento tra "quanto è raro l'evento" (Priori) e "quanto costa sbagliare" (Loss),.
    - **Neyman-Pearson & ROC:** Anche se non li abbiamo disegnati, sai che muovere la soglia $\eta$ significa semplicemente essere più o meno prudenti, generando la curva ROC,.

---

### ✅ Sei pronto per la prova del nove?

Se ti senti sicuro, ti propongo una "sfida finale" veloce sulla Week 1 che unisce tutto (Gaussiane + Costi + Rischio) senza fare calcoli complessi, solo ragionamento.

**Sfida:** Immagina un sistema di allarme antincendio ($Y=1$ incendio, $Y=0$ nulla).

1. Il sensore misura il fumo $X$ (più alto è $X$, più probabile l'incendio).
2. L'incendio è un evento **rarissimo** ($P(Y=1)$ è minuscola).
3. Il costo di un falso negativo (brucia la casa) è **infinito**.

**Domanda:** Usando la logica del _Likelihood Ratio_ ($\frac{P(X|1)}{P(X|0)} \ge \eta$), come si comporterà la soglia $\eta$? Sarà altissima o bassissima? E questo renderà l'allarme "paranoico" (suona sempre) o "rilassato" (non suona mai)?

**Bravissimo!** 🎓 Hai superato la prova finale della Week 1 a pieni voti.

La tua intuizione è corretta: la soglia $\eta$ deve essere **bassissima** (vicina allo zero). Il sistema deve diventare "paranoico": al minimo dubbio (un po' di fumo, un sensore difettoso) deve urlare "AL FUOCO!", perché il prezzo da pagare se sta zitto mentre la casa brucia è inaccettabile.

Ecco la "radiografia matematica" della tua risposta usando la formula che abbiamo studiato (Definizione 2.2 e Prop 2.1 nelle dispense):

$$ \eta = \underbrace{\frac{P(\text{Niente})}{P(\text{Incendio})}}_{\text{Enorme}} \times \underbrace{\frac{\text{Costo Falso Allarme}}{\text{Costo Casa Bruciata}}}_{\text{Minuscolo}} $$

C'è un braccio di ferro tra due forze:

1. **La Rarità (Priori):** Poiché l'incendio è raro, il primo termine è gigante (es. 1.000.000). Questo spingerebbe a dire "Stai zitto, non è mai un incendio".
2. **Il Costo (Loss):** Poiché bruciare la casa ha costo infinito, il secondo termine è infinitesimale (es. 0.000000001).

Chi vince? **Vince il costo.** Il risultato è che $\eta \approx 0$. La regola diventa: $\text{Indizio} > 0.000001 \implies \text{ALLARME!}$

_(Piccola nota terminologica: hai scritto "meglio un falso positivo che un vero negativo". Intendevi sicuramente "meglio un falso positivo che un **falso negativo**". Il "Vero Negativo" è quando non c'è l'incendio e l'allarme sta zitto: quello va benissimo! Il nemico è il Falso Negativo: c'è l'incendio e l'allarme dorme)._
