# 🧮 Algoritmo di Euclide Esteso (Extended Euclidean Algorithm - EEA)

### Definizione e Scopo

L'**Algoritmo di Euclide Esteso (EEA)** è un'evoluzione fondamentale del classico Algoritmo di Euclide. Mentre l'algoritmo standard ha il solo scopo di trovare il Massimo Comun Divisore (MCD) di due interi $a$ e $b$, ovvero $\gcd(a, b)$, l'algoritmo _esteso_ fa un passo cruciale in più:

Oltre a calcolare il $\gcd(a, b)$, determina anche due numeri interi $x$ e $y$ (chiamati **coefficienti di Bézout**) che soddisfano l'**[[Bézout's identity]]**:

$$ax + by = \gcd(a, b)$$

In termini ingegneristici, questo algoritmo permette di esprimere il MCD di due numeri come una **combinazione lineare** dei numeri stessi.

### Applicazione Critica: Inverso Moltiplicativo Modulare

Per un ingegnere informatico, l'utilità principale dell'EEA non è il MCD, ma la sua capacità di **trovare l'inverso moltiplicativo modulare**. Questo è il processo per trovare un numero $x$ tale che:

$$a \cdot x \equiv 1 \pmod m$$

Questo numero $x$ è l'inverso di $a$ modulo $m$, indicato come $a^{-1}$.

#### Come funziona

1. Per trovare l'inverso di $a$ modulo $m$, usiamo l'EEA con gli input $a$ e $m$.
    
2. L'identità di Bézout che l'algoritmo risolve è: $ax + my = \gcd(a, m)$.
    
3. Affinché un inverso modulare esista, $a$ e $m$ devono essere **[[Coprime]]**, il che significa che il loro unico divisore comune è 1, quindi $\gcd(a, m) = 1$.
    
4. Sotto questa condizione, l'equazione dell'identità diventa:
    
    $$ax + my = 1$$
    
5. Ora, se applichiamo l'operazione di modulo $m$ a entrambi i lati dell'equazione:
    
    $$(ax + my) \equiv 1 \pmod m$$
    
6. Dato che $my$ è per definizione un multiplo di $m$, il termine $my \equiv 0 \pmod m$. L'equazione si semplifica drasticamente in:
    
    $$ax \equiv 1 \pmod m$$
    
7. Questo significa che il coefficiente $x$ calcolato dall'EEA è esattamente l'**[[Multiplicative Inverse]]** di $a$ modulo $m$.
    

### Uso in Crittografia (RSA)

Questa capacità è la pietra angolare di molti sistemi crittografici a chiave pubblica.

- **Generazione Chiavi [[RSA]]:** L'EEA è **essenziale** per la generazione delle chiavi RSA. Viene utilizzato per calcolare l'esponente privato $d$ partendo dall'esponente pubblico $e$ e dal [[Euler's totient function]] $\phi(n)$.
    
    - Si deve risolvere l'equazione: $e \cdot d \equiv 1 \pmod{\phi(n)}$.
        
    - Questa è una classica ricerca di inverso modulare. Si usa l'EEA per trovare l'inverso di $e$ modulo $\phi(n)$. Il coefficiente $x$ restituito dall'algoritmo è l'esponente privato $d$.
        
- **[[Elliptic Curve Cryptography - ECC]]:** L'algoritmo è utilizzato anche in varie operazioni sui campi finiti necessarie per l'aritmetica della curva.
    

### L'Algoritmo EEA (Pseudocodice)

Questo pseudocodice implementa l'algoritmo per trovare i coefficienti $x_0$ e $y_0$ dall'identità di Bézout.

```C
/*
 * Restituisce (x0, y0) tali che a*x0 + b*y0 = gcd(a, b)
 * (Assumendo gcd(a, b) = 1 per l'inverso)
 * Stiamo tipicamente cercando x0, che è l'inverso di a mod b.
 */
function extendedEuclid(a, b)
    // Inizializza i valori per le identità
    x0 ← 1, y0 ← 0
    x1 ← 0, y1 ← 1

    // Il loop continua finché b (il resto) non è 0
    while b ≠ 0
        // Calcola il quoziente
        q ← a div b
        
        // Aggiorna a e b (come nell'algoritmo di Euclide standard)
        (a, b) ← (b, a mod b)
        
        // Aggiorna i coefficienti di Bézout
        (x0, x1) ← (x1, x0 - q * x1)
        (y0, y1) ← (y1, y0 - q * y1)

    // Quando b = 0, a = gcd(a, b)
    // e x0, y0 sono i coefficienti di Bézout
    return (x0, y0) 
}
```


---
