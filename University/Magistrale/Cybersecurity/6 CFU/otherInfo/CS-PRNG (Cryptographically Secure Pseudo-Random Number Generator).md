# CS-PRNG (Cryptographically Secure Pseudo-Random Number Generator)

## 1. Definizione

Un **CS-PRNG** è una sottocategoria speciale di [[PRNG (Pseudo-Random Number Generator)]] che soddisfa proprietà estremamente rigorose, rendendolo adatto all'uso in crittografia (es. generazione di chiavi [[AES]], nonce, [[Salt (Cryptographic)|Salt]]).

Mentre un normale PRNG (come `rand()` in C o `Random` in Java) si preoccupa solo della **distribuzione statistica** (i numeri devono _sembrare_ casuali), un CS-PRNG si preoccupa dell'**imprevedibilità**.

## 2. I Tre Requisiti di Sicurezza

Perché un PRNG possa fregiarsi del titolo "Cryptographically Secure", deve superare questi test:

### A. Il "Next-Bit Test" (Imprevedibilità)

Dato un numero qualsiasi di bit output già generati ($k$ bit), non deve esistere alcun algoritmo (polinomiale) in grado di prevedere il bit successivo ($k+1$) con una probabilità significativamente superiore al **50%**.

- In pratica: Anche se vedo un miliardo di numeri usciti, il prossimo è ancora un "lancio di moneta" per me.
    

### B. State Compromise Extension (Resistenza alla Compromissione)

Se un attaccante riesce a rubare lo **stato interno** del generatore in un certo momento $T$:

1. **Backward Secrecy (Segretezza in Indietro):** L'attaccante NON deve poter ricostruire i numeri generati _prima_ di $T$. (Protegge le vecchie chiavi).
    
2. **Forward Secrecy (Segretezza in Avanti):** Idealmente, se il generatore viene "rinfrescato" con nuova entropia, l'attaccante non dovrebbe poter prevedere i numeri futuri per sempre (anche se questo dipende dal reseeding).
    

## 3. Differenza Cruciale: PRNG vs CS-PRNG

|**Caratteristica**|**PRNG Standard (es. Mersenne Twister)**|**CS-PRNG (es. AES-CTR_DRBG)**|
|---|---|---|
|**Scopo**|Velocità, Simulazioni, Videogiochi.|**Sicurezza**, Chiavi, Token.|
|**Prevedibilità**|Alta. Basta osservare pochi output per clonare lo stato.|**Nulla.** Computazionalmente intrattabile.|
|**Performance**|Estremamente veloce.|Più lento (usa primitive crittografiche pesanti).|
|**Esempio Java**|`java.util.Random`|`java.security.SecureRandom`|

> [!failure] Common Pitfall
> 
> L'errore classico dello sviluppatore:
> 
> Usare un PRNG standard per generare un token di reset password.
> 
> Scenario: Un attaccante richiede 3 reset password per il proprio account, analizza i token, calcola lo stato del PRNG, e poi prevede esattamente quale sarà il token di reset per l'account dell'amministratore.

## 4. Architettura Interna

Un CS-PRNG non inventa la matematica da zero. Di solito è costruito usando una primitiva crittografica esistente in modalità "counter" o "feedback".

### Metodo 1: Basato su Hash (HMAC_DRBG)

Si usa una funzione hash sicura (es. [[SHA-256]]).

$$\text{Output}_i = \text{Hash}(\text{Counter}_i \ || \ \text{Seed})$$

Essendo l'hash irreversibile (One-Way), conoscere l'output non rivela il Seed.

### Metodo 2: Basato su Cifrario a Blocchi (CTR_DRBG)

È lo standard raccomandato dal NIST (SP 800-90A). Si usa [[AES]] in modalità Counter.

1. Il **Seed** diventa la Chiave AES.
    
2. Lo stato è un contatore incrementale.
    
3. L'output è il risultato della cifratura del contatore.
    

$$\text{Output}_i = \text{AES}_{Key}(\text{Counter}_i)$$

Poiché AES è sicuro, l'output è indistinguibile dal rumore casuale.

### Metodo 3: Basato sulla Teoria dei Numeri (Blum Blum Shub)

Basato sulla difficoltà di fattorizzare grandi numeri (come [[RSA]]).

- **Pro:** Sicurezza dimostrabile matematicamente.
    
- **Contro:** Molto lento rispetto ad AES.
    

## 5. Best Practices per l'Uso

1. **Non scriverlo tu:** Usa sempre le librerie del Sistema Operativo o del Linguaggio.
    
    - **Linux/Unix:** Leggi da `/dev/urandom`.
        
    - **Windows:** Usa `CryptGenRandom`.
        
    - **Python:** Usa il modulo `secrets` (non `random`).
        
2. **Seeding:** Assicurati che il CS-PRNG sia inizializzato con un seed proveniente da un vero [[TRNG]] (es. rumore hardware raccolto dal kernel).
    

---

**Vedi anche:**

- [[PRNG (Pseudo-Random Number Generator)]]
    
- [[TRNG (True Random Number Generator)]]
    
- [[AES (Advanced Encryption Standard)]]
    
- [[Hashing]]