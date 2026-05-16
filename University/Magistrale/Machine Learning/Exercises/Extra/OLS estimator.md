
# The Ordinary Least Squares (OLS) Estimator

**Tags:** #machine_learning #linear_regression #optimization #linear_algebra #statistics

## 1. Definizione e Obiettivo

L'**Ordinary Least Squares (OLS)** è lo stimatore "standard" per la Regressione Lineare. È una **soluzione in forma chiusa** (closed-form solution), il che significa che ci fornisce una formula matematica esatta per trovare i parametri ottimali $\hat{\theta}$ in un colpo solo, senza bisogno di iterazioni (a differenza del Gradient Descent).

L'obiettivo è minimizzare l'[[Empirical Risk]] (MSE):

$$\hat{\theta}_{OLS} = \underset{\theta}{\arg\min} \space \hat{R}(\theta) = \underset{\theta}{\arg\min} \frac{1}{n} \|y - \Phi\theta\|_2^2$$

---

## 2. The Theorem: The Closed-Form Solution

Se la matrice $\Phi^T\Phi$ è invertibile (ovvero se abbiamo almeno tanti dati quante feature, $n \ge d$, e le feature sono linearmente indipendenti), esiste una **soluzione unica** data dalla formula:

$$\boxed{\hat{\theta} = (\Phi^T\Phi)^{-1}\Phi^T y}$$

> [!abstract] Analisi Dimensionale
> 
> È fondamentale capire le dimensioni per non perdersi:
> 
> - $\Phi$: $n \times d$ (Design Matrix)
>     
> - $y$: $n \times 1$ (Target Vector)
>     
> - $\Phi^T\Phi$: $d \times d$ (Matrice quadrata simmetrica, "Gram Matrix")
>     
> - $(\Phi^T\Phi)^{-1}\Phi^T$: $d \times n$ (Pseudo-inversa di Moore-Penrose)
>     
> - $\hat{\theta}$: $d \times 1$ (Vettore dei pesi finale)
>     

---

## 3. Derivazione Algebrica (Optimization View)

Come arriviamo a questa formula? Trattiamo la Loss Function come una funzione da minimizzare usando il calcolo matriciale.

**1. Espansione della Loss Function**

Partiamo dall'errore quadratico in notazione matriciale:

$$\hat{R}(\theta) \propto (y - \Phi\theta)^T (y - \Phi\theta)$$

Espandendo i termini (simile a $(a-b)^2 = a^2 - 2ab + b^2$):

$$= y^Ty - (\Phi\theta)^T y - y^T(\Phi\theta) + (\Phi\theta)^T(\Phi\theta)$$

Poiché $(\Phi\theta)^T y$ è uno scalare, è uguale al suo trasposto. Possiamo accorpare i termini centrali:

$$= y^Ty - 2\theta^T\Phi^T y + \theta^T\Phi^T\Phi\theta$$

**2. Calcolo del Gradiente**

Calcoliamo la derivata rispetto a $\theta$ ($\nabla_\theta$):

- La derivata di $-2\theta^T A$ è $-2A$.
    
- La derivata di $\theta^T A \theta$ (quadratica) è $2A\theta$.
    

$$\nabla_\theta \hat{R}(\theta) = -2\Phi^T y + 2\Phi^T\Phi\theta$$

**3. Normal Equations**

Poniamo il gradiente a zero per trovare il minimo (essendo una funzione convessa, il punto stazionario è il minimo globale):

$$-2\Phi^T y + 2\Phi^T\Phi\theta = 0$$

$$\Phi^T\Phi\theta = \Phi^T y \quad (\text{Normal Equations})$$

Moltiplicando a sinistra per l'inversa $(\Phi^T\Phi)^{-1}$, otteniamo la soluzione finale:

$$\hat{\theta} = (\Phi^T\Phi)^{-1}\Phi^T y$$

---

## 4. Interpretazione Geometrica (Projection View)

Geometricamente, OLS è una **Proiezione Ortogonale**.

Il vettore target $y$ vive in $\mathbb{R}^n$, ma il nostro modello può solo generare predizioni che vivono nel sottospazio generato dalle colonne di $\Phi$ (un piano iperpiano "piatto").

- **Il Problema:** $y$ quasi mai giace sul piano di $\Phi$ (a causa del rumore).
    
- **La Soluzione:** Cerchiamo il punto sul piano ($\hat{y}$) che è più vicino a $y$. Questo punto è la proiezione ortogonale.
    
- **L'Ortogonalità:** L'errore $e = y - \hat{y}$ deve essere perpendicolare a ogni colonna di $\Phi$:
    
    $$\Phi^T (y - \Phi\hat{\theta}) = 0$$
    
    Questa equazione geometrica porta direttamente alle Normal Equations.
    

> [!tip] The "Hat Matrix"
> 
> La matrice $P = \Phi(\Phi^T\Phi)^{-1}\Phi^T$ è chiamata **Projection Matrix** o "Hat Matrix", perché "mette il cappello" alla y:
> 
> $$\hat{y} = P y$$
> 
> Trasforma i dati reali ($y$) nelle predizioni del modello ($\hat{y}$).

guarda la [[OLS estimator#Spiegazione dettagliata sull'interpretazione geometrica|spiegazione dettagliata qui]]

---

## 5. Proprietà Statistiche (Bias & Variance)

Se assumiamo che i dati siano generati da un processo lineare reale $Y = \Phi\theta^* + \epsilon$ (Linear Assumption), l'OLS gode di proprietà eccellenti.

### A. Unbiasedness (Correttezza)

Lo stimatore è corretto "in media". Se ripetessimo l'esperimento infinite volte, la media delle stime coinciderebbe con la verità.

$$\mathbb{E}[\hat{\theta}] = \theta^*$$

_Dimostrazione:_ $\mathbb{E}[\hat{\theta}] = \theta^* + \mathbb{E}[(\Phi^T\Phi)^{-1}\Phi^T \epsilon]$. Poiché il rumore $\epsilon$ ha media 0, il secondo termine sparisce.

### B. Variance (Precisione)

La varianza dello stimatore dipende dal rumore intrinseco ($\sigma^2$) e dalla "forma" dei dati ($\Phi^T\Phi$).

$$\mathbb{V}[\hat{\theta}] = \sigma^2 (\Phi^T\Phi)^{-1}$$

- **Più rumore ($\sigma^2 \uparrow$)** $\to$ Stima più instabile.
    
- **Più dati ($n \uparrow$)** $\to$ Gli elementi di $\Phi^T\Phi$ crescono $\to$ L'inversa diventa più piccola $\to$ Varianza minore (la stima converge).
    

---

## 6. Limiti Computazionali

Nonostante la bellezza matematica, l'OLS ha due grossi difetti pratici:

1. **Costo Computazionale:** Invertire la matrice $\Phi^T\Phi$ (che è $d \times d$) ha una complessità di **$O(d^3)$**.
    
    - Se $d = 10.000$ feature, l'operazione è lentissima.
        
    - _Soluzione:_ Gradient Descent (Week 3).
        
2. **Invertibilità:** Se $n < d$ (meno dati che feature) o se le feature sono collineari (ridondanti), la matrice $\Phi^T\Phi$ è singolare (determinante 0) e non può essere invertita.
    
    - _Soluzione:_ Regolarizzazione (Ridge/Lasso).


# Spiegazione dettagliata sull'interpretazione geometrica

In parole povere, questo paragrafo trasforma un problema di **algebra** (trovare dei numeri) in un problema di **geometria** (trovare la strada più breve).

Ecco la spiegazione dettagliata del concetto geometrico per la tua nota Obsidian:

---

## La Geometria dell'Errore: Proiezione Ortogonale

Per capire cosa fa davvero l'algoritmo OLS (Ordinary Least Squares), dobbiamo smettere di guardare le singole equazioni e immaginare uno spazio geometrico.

### 1. Il "Pavimento" e il "Soffitto"

- **Lo spazio $\mathbb{R}^n$**: Immagina una stanza 3D. Il vettore $y$ (i tuoi dati reali) è come una mosca che vola a metà altezza nella stanza.
    
- **L'immagine di $\Phi$ ($im(\Phi)$)**: Rappresenta il **pavimento** della stanza. Le colonne della tua matrice $\Phi$ definiscono questo piano.
    
- **Il Vincolo**: Poiché il nostro modello è lineare ($\hat{y} = \Phi\theta$), le nostre previsioni ($\hat{y}$) possono esistere **solo sul pavimento**. Non possono mai "volare" e raggiungere la mosca nel punto esatto in cui si trova.
    

### 2. La Ricerca del Punto più Vicino

Dato che non possiamo raggiungere la mosca ($y$), qual è il punto del pavimento più vicino a lei?

- La geometria ci insegna che la distanza minima tra un punto e un piano è la **linea retta perpendicolare** (ortogonale).
    
- La nostra previsione ottimale $\hat{y}$ è quindi l'**ombra** della mosca proiettata verticalmente sul pavimento.
    

### 3. La Matrice di Proiezione ($P$)

Il paragrafo introduce la matrice $P = \Phi(\Phi^T\Phi)^{-1}\Phi^T$. In geometria, questa matrice non è solo un ammasso di simboli, ma è un **operatore di proiezione**.

Immagina $P$ come una pressa idraulica:

1. **Schiaccia** tutto ciò che non è coerente con il nostro modello.
    
2. Se un vettore è già sul pavimento, $P$ lo lascia stare ($Pv = v$).
    
3. Se un vettore è puramente verticale (perpendicolare al pavimento, ovvero puro rumore), $P$ lo annulla portandolo a zero ($Pv = 0$).
    

> [!abstract] Visual Analysis 
> Il vettore di errore $e = y - \hat{y}$ è la linea verticale che unisce la mosca ($y$) alla sua ombra ($\hat{y}$). Questa linea è **perpendicolare** (a 90 gradi) rispetto a ogni direzione possibile sul pavimento.

### 4. Il Processo in Due Fasi

L'algoritmo OLS lavora così:

1. **Fase Geometrica (Proietta)**: Trova l'ombra $\hat{y}$ sul pavimento che minimizza la lunghezza dell'errore.
    
2. **Fase Algebrica (Coordina)**: Una volta trovata l'ombra, calcola i pesi $\hat{\theta}$ (le "istruzioni") necessari per muoversi sulle piastrelle del pavimento (le colonne di $\Phi$) e arrivare esattamente in quel punto.
    

---

**Ti è più chiaro ora perché l'errore deve essere perpendicolare? Se vuoi, possiamo approfondire la dimostrazione del perché $Pv=v$ per i vettori sul piano.**