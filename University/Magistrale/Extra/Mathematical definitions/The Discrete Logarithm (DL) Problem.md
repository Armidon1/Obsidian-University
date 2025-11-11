# 🔒 Problema del Logaritmo Discreto (DLP)

### Definizione

Il **Problema del Logaritmo Discreto (DLP)** è un problema matematico **computazionalmente difficile** che costituisce la base della sicurezza per molti sistemi crittografici a chiave pubblica, tra cui **[[Diffie-Hellman Key Exchange|Dieffie-Hellman]]** ed **[[ElGamal]]**.

In termini semplici, il DLP è il **problema inverso** dell'**esponenziazione modulare**.

L'esponenziazione modulare è _facile_ da calcolare. Dati:

- Una base $g$
    
- Un esponente $x$
    
- Un modulo $p$
    

È computazionalmente veloce calcolare il risultato $y$:

$$y = g^x \pmod p$$

Il **Problema del Logaritmo Discreto** è: dati $g$, $p$ e il risultato $y$, è computazionalmente **infattibile** (estremamente difficile) trovare l'esponente $x$.

$$x = \log_g(y) \pmod p \quad (\text{Trovare } x)$$

### Analogia: La "Funzione Unidirezionale"

Per un ingegnere informatico, il DLP è l'esempio perfetto di una **funzione unidirezionale ([[OWF]])**:

- **Andare avanti (Esponenziazione):** Facile. È come mescolare due colori di vernice per ottenerne un terzo. Se ti do il blu e il giallo, ottieni facilmente il verde.
    
- **Tornare indietro (Logaritmo Discreto):** Difficile. È come se ti dessi il secchio di vernice verde e ti chiedessi: "Esattamente quali tonalità di blu e giallo ho usato, e in quali proporzioni?". È un problema quasi impossibile.
    

### Implicazioni in Crittografia

|**Concetto**|**Descrizione Tecnica**|
|---|---|
|**Fondamento di Sicurezza**|L'intera sicurezza di protocolli come Diffie-Hellman si basa sul fatto che l'avversario non può risolvere il DLP in un tempo ragionevole.|
|**Chiave Privata e Pubblica**|Nel protocollo Diffie-Hellman:<br><br>  <br><br>• **$x$** (l'esponente) è la **chiave privata** (il segreto).<br><br>  <br><br>• **$y$** (il risultato) è la **chiave pubblica** (il valore condiviso).<br><br>  <br><br>È facile per te generare la tua chiave pubblica $y$ dal tuo segreto $x$. È impossibile per chiunque altro scoprire il tuo segreto $x$ guardando la tua chiave pubblica $y$.|
|**Evoluzione (ECC)**|Il DLP esiste anche in altri contesti, come le **curve ellittiche**. Il **Problema del Logaritmo Discreto su Curve Ellittiche (ECDLP)** è una versione ancora più difficile dello stesso problema, ed è il motivo per cui la crittografia a curva ellittica (ECC) è così sicura ed efficiente.|
## In particolare
This problem is the basis for the **[[Diffie-Hellman Key Exchange]]** and the **[[ElGamal]]** encryption system.

- **Definition:** Let $G$ be a finite cyclic group with _n_ elements and $g$ be a generator of $G$.
    
- **Easy Problem:** Given $g$ and an integer $x$, it is easy (efficient) to compute $y = g^x$. This is **[[Modular Exponentiation]]**.
    
- **Hard Problem:** Given $y$ and $g$, it is computationally infeasible to find the integer $x$ that satisfies the equation $y = g^x$.
    
- **Terminology:** This $x$ is called the **discrete logarithm of $y$ to the base $g$**. Ma perché diciamo logaritmo discreto? Questa è un'ottima domanda di approfondimento che va al cuore della differenza tra la matematica "classica" e quella usata in crittografia.
	- La parola **"discreto"** viene usata per sottolineare che stiamo lavorando all'interno di un **insieme finito e specifico di numeri interi**, (come gli interi modulo p), e non sull'insieme **continuo** dei numeri reali. vedi qui un [[Logaritmo Discreto vs Logaritmo Standard#🧩 Logaritmo Discreto|Esempio di Logaritmo Discreto]]
    
- **Example (a common group):** The multiplicative group of integers modulo a prime $p$, $\mathbb{Z}^*_p$. The problem is:
    
    - Find $x$ given $y$, $g$, and $p$ in the equation: $y \equiv g^x \pmod p$
        
- **DL in $\mathbb{Z}^*_p$ as an [[OWF]]:**
    
    - The function $x \rightarrow g^x \pmod p$ is **easy** to compute.
        
    - The inverse function $y \rightarrow x$ is **believed to be hard**.
        
    - This provides a **computation-based** notion of security.