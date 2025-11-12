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
        
    - L'inverso è $7$ (come se lo è trovato 7? guarda [[Multiplicative Inverse#Spiegazione mentalità per lo svolgimento dell'esempio|qui]]), perché $3 \times 7 = 21 \equiv 1 \pmod{10}$.
        
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

---
# Spiegazione mentalità per lo svolgimento dell'esempio
### L'idea dell'Inverso

Pensa all'inverso come a un "pulsante Annulla" per la moltiplicazione.

Nel mondo normale (numeri reali):

Se hai il numero 4, qual è il suo inverso moltiplicativo? È $1/4$ (o 0.25).

Perché? Perché se moltiplichi 4 per $1/4$, ottieni 1.

$$4 \times (1/4) = 1$$

Il numero 1 è l'elemento "neutro": moltiplicare per 1 non cambia nulla. L'inverso è ciò che ti riporta all'elemento neutro.

---

### Nel mondo dell'Aritmetica Modulare (l'"orologio")

In $\pmod{10}$, il concetto è identico, ma le regole sono diverse.

- Il nostro "mondo" non è la linea infinita dei numeri, ma un cerchio, un **orologio con 10 ore** (da 0 a 9).
    
- L'elemento "neutro" è sempre **1**.
    
- L'obiettivo è trovare un numero che, moltiplicato per il nostro numero di partenza, ci faccia "atterrare" sull'**1** dopo aver fatto tutti i giri necessari.
    

**Il nostro caso: trovare l'inverso di $3 \pmod{10}$**

Stiamo cercando un numero $x$ tale che:

$$3 \times x \equiv 1 \pmod{10}$$

Questo significa: "Se faccio $x$ salti da 3 ore sul mio orologio da 10 ore, dove atterro?". Vogliamo atterrare sull'**1**.

Proviamo:

- **$x=1$**: $3 \times 1 = 3$. Atterro sul 3. (No)
    
- **$x=2$**: $3 \times 2 = 6$. Atterro sul 6. (No)
    
- **$x=3$**: $3 \times 3 = 9$. Atterro sul 9. (No)
    
- **$x=4$**: $3 \times 4 = 12$. Faccio un giro completo (10 ore) e avanzo di 2. Atterro sul **2**. (No)
    
- **$x=5$**: $3 \times 5 = 15$. Faccio un giro (10 ore) e avanzo di 5. Atterro sul **5**. (No)
    
- **$x=6$**: $3 \times 6 = 18$. Faccio un giro (10 ore) e avanzo di 8. Atterro sul **8**. (No)
    
- **$x=7$**: $3 \times 7 = 21$. Faccio due giri completi (20 ore) e avanzo di 1. **Atterro sull'1**.
    

**Ci siamo!**

Abbiamo trovato che $x=7$ è il numero che, moltiplicato per 3, ci fa "atterrare" sull'1 nel mondo $\pmod{10}$.

Per questo $7$ è l'inverso moltiplicativo di $3 \pmod{10}$.

In breve: l'inverso moltiplicativo $a^{-1}$ è quel numero che, moltiplicato per $a$, dà come **resto 1** quando diviso per $m$.