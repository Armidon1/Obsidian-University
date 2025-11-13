# ⚡ Esponenziazione Modulare (Modular Exponentiation)

### Definizione

L'**Esponenziazione Modulare** è un'operazione matematica che calcola il resto della divisione di un numero elevato a una grande potenza per un altro numero (il modulo). È l'operazione fondamentale alla base di quasi tutta la crittografia a chiave pubblica moderna.

L'operazione è della forma:

$$c \equiv b^e \pmod m$$

Dove:

- $b$ = base
    
- $e$ = esponente
    
- $m$ = modulo
    
- $c$ = risultato (il resto)
    

Poiché è un concetto elementare ma molto controinuitivo, guarda [[Modular Exponentiation Details|questa analisi nel dettaglio]] 
### Il Problema (Perché è un'operazione speciale?)

Per un ingegnere informatico, l'approccio "ingenuo" per calcolare $b^e \pmod m$ sarebbe:

1. Calcolare il valore $b^e$.
    
2. Prendere il risultato e calcolare il resto (modulo $m$).
    

Questo approccio **fallisce catastroficamente** nella pratica.

**Esempio:** In [[RSA]], i numeri sono enormi. Anche con numeri "piccoli" come $50^{123} \pmod{100}$, il numero intermedio ($50^{123}$) ha più di 200 cifre. Supera la capacità di qualsiasi tipo di dato standard (come un `int64`) ed è computazionalmente ingestibile da memorizzare.

### La Soluzione: "Exponentiation by Squaring"

La soluzione è un algoritmo efficiente (spesso chiamato **Square-and-Multiply**) che non calcola mai il numero intermedio. Si basa sulla proprietà dell'aritmetica modulare:

$$(x \cdot y) \pmod m \equiv \left[ (x \pmod m) \cdot (y \pmod m) \right] \pmod m$$

Questo significa che possiamo applicare l'operazione di modulo **ad ogni passo** della moltiplicazione, mantenendo i numeri intermedi sempre piccoli (mai più grandi di $m^2$).

L'algoritmo scompone l'esponente $e$ nella sua rappresentazione binaria ed esegue una serie di moltiplicazioni e quadrati, applicando il modulo a ogni passaggio.

**Efficienza:**

- **Approccio Ingenuo:** Richiede $O(e)$ moltiplicazioni.
    
- **Square-and-Multiply:** Richiede solo $O(\log e)$ moltiplicazioni.
    

Per un esponente a 2048 bit, questo è la differenza tra $2^{2048}$ operazioni (impossibile) e circa 2048 operazioni (istantaneo).

Un ottimizzazione potrebbe essere [[Euler's Theorem]].

### Applicazioni Crittografiche (Perché è importante)

L'esponenziazione modulare è il cavallo di battaglia della crittografia asimmetrica:

1. **Crittosistema [[RSA]]:**
    
    - **Cifratura:** $C = M^e \pmod n$
        
    - **Decifratura:** $M = C^d \pmod n$
        
2. **Diffie-Hellman Key Exchange:**
    
    - **Calcolo Chiavi Pubbliche:** $A = g^a \pmod p$
        
    - **Calcolo Segreto Condiviso:** $S = B^a \pmod p$
        
3. **Protocollo ElGamal:**
    
    - Utilizza l'esponenziazione modulare per la cifratura e la firma.
        

È una **funzione unidirezionale ([[OWF]])**: è computazionalmente facile da eseguire (grazie allo _Square-and-Multiply_), ma estremamente difficile da invertire (questo è il **[[Discrete Logarithm (DL) Problem]]**).

#### Fast Modular Exponentiation (Algorithm)

We don't compute $g^x$ and _then_ take the modulus. We use **exponentiation by squaring** (or the binary method), applying the modulus at every partial step.

```C
/*
 * Computes (base^exp) % mod efficiently.
 */
long fastModExp(unsigned int base, unsigned int exp, long mod) {
    long result = 1;
    long b = base % mod; // Apply mod to base first

    while (exp > 0) {
        // If the last bit of exp is 1 (i.e., exp is odd)
        if (exp & 1)
            result = (result * b) % mod;
        
        // Square the base (and apply mod)
        b = (b * b) % mod;
        
        // Right-shift the exponent (divide by 2)
        exp >>= 1;
    }
    return result;
}
```

- **Efficiency:** This algorithm runs in $O(\log(x))$ multiplications. Since $x < p$, the overall complexity is $O(\log^3(p))$.
    
