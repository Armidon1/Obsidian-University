# CS-PRNG based by RSA

## 1. Definizione

Il **Generatore Basato su RSA** è un [[CS-PRNG]] (Generatore Pseudo-Casuale Crittograficamente Sicuro) che basa la sua sicurezza sulla difficoltà computazionale del problema RSA (invertire la funzione $x^e \pmod n$).

A differenza dei generatori basati su cifrari a blocchi (come il [[Generatore "Cipher of a Counter"|CTR_DRBG]]), che si basano sull'euristica ("AES sembra sicuro"), il generatore RSA gode di una **sicurezza dimostrabile**: se un attaccante riuscisse a prevedere i numeri generati, allora avrebbe trovato un metodo efficiente per rompere la crittografia [[RSA]].

## 2. L'Algoritmo

Il funzionamento è simile al processo di cifratura RSA ripetuto in un loop.

### Setup

1. Si generano due grandi numeri primi $p$ e $q$.
    
2. Si calcola il modulo $n = p \cdot q$.
    
3. Si sceglie un esponente pubblico $e$ coprimo con $\phi(n)$.
    
4. Si sceglie un **[[Seed]]** casuale $z_0$ (compreso tra $1$ e $n-1$).
    

### Generazione (Iterazione)

Per generare una sequenza di bit casuali $b_i$:

1. Aggiornamento di Stato: Si eleva il valore corrente alla potenza $e$ modulo $n$.
    
    $$z_{i+1} = (z_i)^e \pmod n$$
    
2. Estrazione Output: Si prende il bit meno significativo (LSB) del nuovo stato.
    
    $$b_{i+1} = z_{i+1} \pmod 2$$
    
3. Si ripete il ciclo.
    

> [!abstract] Visualizzazione Logica
> 
> - **Input:** Seed $z_0$
>     
> - **Passo 1:** $z_1 = z_0^e \pmod n \to$ Output: ultimo bit di $z_1$.
>     
> - **Passo 2:** $z_2 = z_1^e \pmod n \to$ Output: ultimo bit di $z_2$.
>     
> - ...e così via.
>     

## 3. Implementazione (Pseudocodice)

Ecco la struttura logica esatta (basata sui tuoi appunti):

C

```
/* Parametri RSA standard */
prime numbers p, q
n = p * q
integer e s.t. GCD(e, (p-1)*(q-1)) = 1

/* Inizializzazione */
z = seed  // Seed segreto iniziale

loop:
    /* Calcolo prossimo stato (Cifratura RSA) */
    z_next = (z ^ e) mod n
    
    /* Aggiornamento */
    z = z_next
    
    /* Output: Bit meno significativo */
    output_bit = z mod 2
```

## 4. Analisi della Sicurezza

La forza di questo generatore risiede in un teorema fondamentale:

"Il bit meno significativo di una cifratura RSA è sicuro quanto l'intera cifratura RSA." (Hard-Core Predicate).

- Se un attaccante, osservando la sequenza di bit $b_1, b_2, \dots$, riuscisse a prevedere il prossimo bit con probabilità $> 50\% + \epsilon$, allora esisterebbe un algoritmo polinomiale per invertire RSA (trovare $z$ dato $z^e$).
    
- Poiché assumiamo che invertire RSA sia difficile (Intrattabile), allora il generatore è sicuro.
    

## 5. Pro e Contro (RSA vs AES)

|**Caratteristica**|**Generatore RSA**|**Generatore AES (CTR_DRBG)**|
|---|---|---|
|**Sicurezza**|**Provabile** (legata alla fattorizzazione).|Euristica (legata alla robustezza di AES).|
|**Velocità**|**Molto Lento.** Richiede calcoli su grandi numeri interi (es. 2048 bit) per ogni singolo bit di output.|**Velocissimo.** Operazioni su bit e blocchi piccoli, spesso accelerati dall'hardware.|
|**Utilizzo**|Accademico, o dove la sicurezza provabile è più importante della velocità.|Standard industriale per sistemi operativi e protocolli (TLS).|

> [!failure] Nota Bene
> 
> Nonostante la sicurezza teorica, non si usa quasi mai per generare flussi di dati ad alta velocità (come cifrare un video) perché l'operazione modulo $n$ è troppo pesante computazionalmente rispetto a uno XOR o a un AES.

---

**Vedi anche:**

- [[RSA]]
    
- [[CS-PRNG]]
    
- [[Blum Blum Shub]] (Un altro generatore basato sulla teoria dei numeri)
    
- [[Generatore "Cipher of a Counter"]] (L'alternativa veloce)