# PRNG (Pseudo-Random Number Generator)

## 1. Definizione

Un **PRNG** (Pseudo-Random Number Generator) è un algoritmo deterministico che produce una sequenza di numeri le cui proprietà statistiche approssimano quelle di una sequenza di numeri casuali veri.

La parola chiave è **Pseudo**: la casualità è apparente. Dato che l'algoritmo è deterministico, se si conosce lo stato iniziale, l'intera sequenza è perfettamente prevedibile.

## 2. Architettura Logica

Un PRNG è essenzialmente una macchina a stati finiti definita da:

1. **Seed (Seme):** L'input iniziale (che deve essere segreto e casuale, idealmente da un [[TRNG (True Random Number Generator)]]).
    
2. **Stato Interno:** Una variabile che tiene traccia della posizione nella sequenza.
    
3. **Funzione di Transizione:** Calcola il prossimo stato e il prossimo output.
    

$$\begin{align} S_{i+1} &= f(S_i) \quad (\text{Aggiornamento Stato}) \\ R_i &= g(S_i) \quad (\text{Output Numero}) \end{align}$$

> [!abstract] Visual Metaphor
> 
> Immagina un libro contenente milioni di cifre di $\pi$.
> 
> - Il **PRNG** è il libro.
>     
> - Il **Seed** è il numero di pagina da cui inizi a leggere.
>     
> - Se dici a qualcuno "leggi a pagina 42", leggerà gli stessi numeri che leggi tu.
>     

## 3. PRNG Statistici vs CSPRNG

Questa è la distinzione più importante per un ingegnere.

### A. PRNG Statistici (InSicuri)

- **Obiettivo:** Velocità e buona distribuzione statistica (devono sembrare casuali in grafici e simulazioni).
    
- **Esempi:** `rand()` in C, Mersenne Twister (MT19937), LCG.
    
- **Difetto:** Sono reversibili. Osservando abbastanza output, si può calcolare lo stato interno e prevedere tutti i numeri futuri.
    
- **Uso:** Monte Carlo simulations, Video Games, Procedural Generation.
    
- **NON USARE PER:** Chiavi crittografiche, Token di sessione.
    

### B. CSPRNG (Cryptographically Secure)

- **Obiettivo:** Imprevedibilità (Next-Bit Test).
    
- **Esempi:** `/dev/urandom`, AES-CTR_DRBG, [[Blum Blum Shub]].
    
- **Proprietà:** Anche se un attaccante vede $N$ numeri, non può calcolare l'$N+1$-esimo in tempo polinomiale.
    
- **Uso:** Generazione chiavi RSA/AES, Salt, Nonce.
    

## 4. Algoritmi Celebri

### Linear Congruential Generator (LCG)

Il più antico e semplice (usato nelle vecchie librerie C).

$$X_{n+1} = (a \cdot X_n + c) \pmod m$$

- Molto veloce ma **crittograficamente rotto**. Se plottato in 3D, i numeri si allineano su piani paralleli (Marsaglia Effect).
    

### Mersenne Twister

Lo standard industriale per le simulazioni (Python, Ruby, Excel, MATLAB lo usano di default).

- Periodo lunghissimo ($2^{19937}-1$).
    
- **NON sicuro:** Basta osservare 624 numeri per clonare l'intero stato interno.
    

## 5. Vulnerabilità Storiche

Quando si usa un PRNG debole o un Seed prevedibile in contesti di sicurezza:

1. **Netscape Navigator (1996):**
    
    - Il Seed era basato su `tempo corrente` + `PID`.
        
    - Un attaccante poteva indovinare il seed provando poche combinazioni e decifrare il traffico SSL.
        
2. **Debian OpenSSL (2008):**
    
    - Uno sviluppatore rimosse la riga di codice che aggiungeva entropia al seed (per zittire un warning di Valgrind).
        
    - Risultato: Esistevano solo 32.767 chiavi possibili. Chiunque poteva entrare nei server SSH.
        

> [!failure] Common Pitfall
> 
> Errore da evitare: Usare System.currentTimeMillis() come seed per generare password o token. È un valore pubblico e prevedibile!

---

**Vedi anche:**

- [[TRNG (True Random Number Generator)]]
    
- [[RNG (Random Number Generator)]]
    
- [[Generazione di Numeri Casuali (RNG)]] (La tua nota generale)