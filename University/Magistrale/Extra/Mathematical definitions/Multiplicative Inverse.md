# ✖️ Inverso Moltiplicativo

### Definizione (Aritmetica Standard)

Nell'aritmetica di base, l'inverso moltiplicativo di un numero $a$ è quel numero (spesso scritto $a^{-1}$ o $\frac{1}{a}$) che, moltiplicato per $a$, dà come risultato l'identità moltiplicativa, **1**.

- **Esempio:** L'inverso moltiplicativo di $5$ è $\frac{1}{5}$, perché $5 \times \frac{1}{5} = 1$.
    

### Definizione (Aritmetica Modulare - Crittografia)

Questo è il concetto cruciale per l'ingegneria informatica e la crittografia.

L'inverso moltiplicativo di un numero intero $a$ **modulo $m$** è un numero intero $x$ (spesso scritto come $a^{-1}$) tale che il prodotto $a \cdot x$ è congruente a 1, modulo $m$.

$$a \cdot x \equiv 1 \pmod m$$

Questo $x$ è il numero che, nel sistema modulare, "annulla" l'effetto della moltiplicazione per $a$.

### Condizione di Esistenza

Un inverso moltiplicativo $a^{-1} \pmod m$ **esiste se e solo se** $a$ e $m$ sono **coprimi** (o _relativamente primi_), il che significa che il loro massimo comun divisore è 1.

$$\gcd(a, m) = 1$$

- **Esempio 1 (Esiste):** Trovare l'inverso di $3 \pmod{10}$.
    
    - $\gcd(3, 10) = 1$. L'inverso esiste.
        
    - Cerchiamo $x$ tale che $3 \cdot x \equiv 1 \pmod{10}$.
        
    - L'inverso è $7$, perché $3 \times 7 = 21 \equiv 1 \pmod{10}$.
        
    - Quindi, $3^{-1} \equiv 7 \pmod{10}$.
        
- **Esempio 2 (Non Esiste):** Trovare l'inverso di $2 \pmod{10}$.
    
    - $\gcd(2, 10) = 2$. L'inverso **non esiste**.
        
    - Non c'è nessun numero intero $x$ che, moltiplicato per 2, dia un resto di 1 se diviso per 10 (il risultato sarà sempre un numero pari).
        

### Come Trovarlo (Collegamento Ingegneristico)

L'inverso modulare viene calcolato computazionalmente utilizzando l'**[[Extended Euclidean Algorithm (EEA)|Algoritmo di Euclide Esteso (EEA)]]**.

Dati $a$ e $m$, l'EEA trova i coefficienti $x$ e $y$ tali che:

$$ax + my = \gcd(a, m)$$

Se $a$ e $m$ sono coprimi ($\gcd(a, m) = 1$), l'equazione diventa:

$$ax + my = 1$$

Se prendiamo questa equazione modulo $m$, il termine $my$ scompare (diventa 0), lasciandoci con:

$$ax \equiv 1 \pmod m$$

Il coefficiente $x$ (se necessario, aggiustato per essere positivo) calcolato dall'EEA è precisamente l'inverso moltiplicativo di $a$ modulo $m$.

### Applicazioni Crittografiche

L'inverso modulare è un'operazione fondamentale in crittografia:

- **[[RSA]]:** È usato per calcolare la chiave privata $d$ a partire dall'esponente pubblico $e$ e dal totiente $\phi(n)$. Si risolve $e \cdot d \equiv 1 \pmod{\phi(n)}$, dove $d$ è l'inverso di $e$.
    
- **[[Elliptic Curve Cryptography - ECC|Crittografia Ellittica (ECC)]]:** È essenziale per l'operazione di "divisione" dei punti (che è implementata come moltiplicazione per l'inverso).