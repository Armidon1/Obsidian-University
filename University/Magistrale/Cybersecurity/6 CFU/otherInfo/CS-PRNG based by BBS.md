# Blum Blum Shub (BBS)

## 1. Definizione

Il **Blum Blum Shub (BBS)** è un algoritmo **[[CS-PRNG]]** (Generatore Pseudo-Casuale Crittograficamente Sicuro) proposto nel 1986 da Lenore Blum, Manuel Blum e Michael Shub.

È celebre per essere uno dei generatori con la **sicurezza più forte dimostrabile**: la sua imprevedibilità è matematicamente equivalente alla difficoltà di fattorizzare grandi numeri interi (lo stesso problema su cui si basa [[RSA]]).

## 2. Requisiti Matematici (Blum Primes)

Il sistema si basa sull'aritmetica modulare. Per funzionare correttamente e mantenere le proprietà di sicurezza, i parametri devono essere scelti con cura:

1. Numeri Primi di Blum: Si scelgono due grandi numeri primi $p$ e $q$ tali che siano congruenti a 3 modulo 4.
    
    $$p \equiv 3 \pmod 4 \quad \text{e} \quad q \equiv 3 \pmod 4$$
    
2. **Modulo di Blum:** Si calcola $n = p \cdot q$.
    

> [!abstract] Perché $3 \pmod 4$?
> 
> Questa proprietà specifica garantisce che ogni residuo quadratico abbia esattamente una radice quadrata che è anch'essa un residuo quadratico. Questo rende la sequenza generata una permutazione ciclica robusta.

## 3. L'Algoritmo

Il processo di generazione è molto semplice: elevare al quadrato e prendere il modulo.

### Setup (Inizializzazione)

1. Si sceglie un **[[Seed]]** casuale $s$ tale che sia coprimo con $n$ (ovvero $MCD(s, n) = 1$).
    
2. Si calcola lo stato iniziale $x_0$:
    
    $$x_0 = s^2 \pmod n$$
    

### Ciclo di Generazione

Per ogni bit $b_i$ che vogliamo generare:

1. Calcolo nuovo stato:
    
    $$x_{i+1} = x_i^2 \pmod n$$
    
2. Estrazione Output: Si prende il bit di parità (o il bit meno significativo) del nuovo stato.
    
    $$b_i = x_{i+1} \pmod 2$$
    

### Implementazione (Pseudocodice)

Ecco la logica tratta dagli appunti universitari:

C

```
/* Setup */
choose p, q big prime s.t. p ≡ q ≡ 3 (mod 4)
n = p * q
randomly choose s s.t. GCD(s, n) = 1

/* Calcolo stato iniziale */
X[0] = (s^2) mod n

/* Loop infinito */
for i = 1 to ∞:
    /* Elevamento al quadrato */
    X[i] = (X[i-1]^2) mod n
    
    /* Estrazione bit (Parità) */
    Bit_Output = X[i] mod 2
    
    return Bit_Output
```

## 4. Sicurezza (Hardness Assumption)

La sicurezza del BBS si basa sul **Problema della Residuosità Quadratica**.

Il teorema di sicurezza afferma che:

> "Se un attaccante può predire il prossimo bit della sequenza con una probabilità significativamente superiore al 50%, allora esiste un algoritmo efficiente per fattorizzare $n$ (cioè scoprire $p$ e $q$)."

Poiché la fattorizzazione di grandi interi è un problema intrattabile (almeno per i computer classici), il generatore è considerato sicuro.

## 5. Efficienza e Utilizzo Pratico

Nonostante la sicurezza teorica perfetta, BBS ha un grande difetto: la **velocità**.

|**Caratteristica**|**BBS (Teoria dei Numeri)**|**CTR_DRBG (Basato su AES)**|
|---|---|---|
|**Operazione Base**|Moltiplicazione modulare su grandi numeri (es. 2048 bit). Molto pesante.|XOR e sostituzioni su blocchi piccoli (128 bit). Molto veloce.|
|**Output per ciclo**|Di solito **1 bit** alla volta (o pochi bit sicuri).|**128 bit** alla volta.|
|**Utilizzo Reale**|Generazione di chiavi master di alto valore, contesti accademici/militari dove la velocità non conta.|Cifratura web (HTTPS), Hard disk encryption, VPN.|

> [!tip] Possiamo estrarre più bit?
> 
> Sì, è possibile estrarre fino a $O(\log \log n)$ bit meno significativi per ogni iterazione mantenendo la sicurezza provabile, ma anche con questa ottimizzazione rimane molto più lento di AES.

---

**Vedi anche:**

- [[CS-PRNG (Cryptographically Secure Pseudo-Random Number Generator)]]
    
- [[CS-PRNG based by RSA]]
    
- [[Entropy]]