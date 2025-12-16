# "Cipher of a Counter" Generator

## 1. Definizione

Il generatore **Cipher of a Counter** è un algoritmo per costruire un [[CS-PRNG]] (Generatore Pseudo-Casuale Crittograficamente Sicuro) utilizzando un **Cifrario a Blocchi** (come [[DES]] o [[AES]]) in modo ciclico.

È stato formalizzato da Meyer e Matyas nel 1982.

L'idea centrale è controintuitiva: invece di cifrare un messaggio segreto, cifriamo una sequenza nota e prevedibile (un contatore: 1, 2, 3...) usando una chiave segreta. Poiché un buon cifrario produce output che sembrano casuali (indistinguibili dal rumore), la sequenza risultante è un ottimo flusso di numeri casuali.

## 2. L'Algoritmo
![[Pasted image 20251216122600.png]]

Il sistema si basa su una Chiave Maestra segreta ($K_m$) e un contatore interno ($C$).

**Parametri:**

- **$E$:** Un algoritmo di cifratura a blocchi (es. AES).
    
- **$K_m$:** La Master Key (che funge da **[[Seed]]** del generatore).
    
- **$N$:** La dimensione del blocco del cifrario (es. 128 bit per AES).
    
- **$C$:** Un contatore intero.
    

Procedura di Generazione:

Per generare l'i-esimo numero casuale $X_i$:

1. Si incrementa il contatore (modulo $N$, per renderlo ciclico).
    
    $$C_{i} = (C_{i-1} + 1) \pmod N$$
    
2. Si cifra il valore del contatore usando la Chiave Maestra.
    
    $$X_i = E(K_m, \ C_i)$$
    
3. $X_i$ è il blocco di bit casuali in output.
    

> [!abstract] Visualizzazione
> 
> - **Input:** `0001` $\xrightarrow{Key}$ **AES** $\to$ `9aF2...` (Random 1)
>     
> - **Input:** `0002` $\xrightarrow{Key}$ **AES** $\to$ `b7C1...` (Random 2)
>     
> - **Input:** `0003` $\xrightarrow{Key}$ **AES** $\to$ `1d04...` (Random 3)
>     
> 
> Anche se l'input cambia di un solo bit (1 $\to$ 2), l'effetto valanga del cifrario rende gli output completamente diversi e non correlati.

## 3. Proprietà di Sicurezza

La sicurezza di questo generatore si riduce direttamente alla sicurezza del cifrario a blocchi sottostante.

1. **Imprevedibilità (K3/K4):** Se l'attaccante vede la sequenza $X_i$, non può prevedere $X_{i+1}$ a meno che non riesca a invertire il cifrario $E$ e scoprire la chiave $K_m$. Se il cifrario è sicuro (es. AES), questo è computazionalmente impossibile.
    
2. **Periodicità:** Il generatore è ciclico. Dopo $2^N$ generazioni (dove $N$ sono i bit del blocco), il contatore torna a zero e la sequenza si ripete.
    
    - _Nota:_ Con AES (128 bit), il periodo è $2^{128}$, un numero talmente grande da non essere un problema pratico.
        

## 4. Evoluzione Moderna: CTR_DRBG

Il concetto di "Cipher of a Counter" è il nonno dello standard attuale NIST: **CTR_DRBG** (Counter Mode Deterministic Random Bit Generator).

Le differenze nello standard moderno (NIST SP 800-90A) sono:

- Meccanismi formali di **Reseeding** (per garantire la _Forward Secrecy_).
    
- Uso esclusivo di **[[AES]]** come primitiva.
    
- Aggiornamento periodico della chiave $K_m$ stessa, non solo del contatore, per evitare attacchi crittanalitici su lunghe sequenze.
    

---

**Vedi anche:**

- [[CS-PRNG]]
    
- [[AES (Advanced Encryption Standard)]]
    
- [[Cifratura a Blocchi]]
    
- [[Generazione di Numeri Casuali (RNG)]]