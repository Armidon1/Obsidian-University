# EdDSA (Edwards-curve Digital Signature Algorithm)

**Tags:** #ingegneria #security #eddsa #firma_digitale #ecc #crittografia

## 1. Definizione e Contesto

EdDSA è un moderno algoritmo di firma digitale a chiave pubblica. Rappresenta l'evoluzione rispetto ai classici algoritmi basati su curve ellittiche (come ECDSA), progettato per essere più sicuro e performante.

Si basa sulle Curve di Edwards (una variante specifica delle curve ellittiche) che offrono vantaggi computazionali significativi.

---

## 2. La Grande Differenza: Il Nonce Deterministico

La caratteristica rivoluzionaria di EdDSA rispetto a ECDSA è il modo in cui gestisce il numero casuale (nonce) necessario per la firma.

> [!failure] Common Pitfall: Il problema di ECDSA
> 
> In ECDSA, il firmatario deve generare un nonce $k$ usando un generatore di numeri casuali (RNG).
> 
> - Se l'RNG è debole o difettoso, $k$ non è davvero casuale.
>     
> - Se $k$ viene riutilizzato per messaggi diversi, un attaccante può calcolare matematicamente la **chiave privata**.
>     

La Soluzione EdDSA:

EdDSA elimina il rischio rendendo la generazione del nonce deterministica. Non si affida al caso, ma deriva il nonce direttamente dalla chiave privata e dal messaggio stesso.

---

## 3. Algoritmo di Firma (Signing)

Il processo di firma garantisce che, per lo stesso messaggio e la stessa chiave, la firma sia sempre identica (determinismo).

**The signing algorithm is formally defined as:**

$$\begin{align} 1. \ \text{Nonce} &= \text{Deterministico (da Private Key)} \\ 2. \ R &= \text{Compute Point (dal Nonce)} \\ 3. \ h &= H(R, A, m) \\ 4. \ \text{Signature} &= (R, s) \end{align}$$

> [!abstract] Math Analysis
> 
> - $A$: è la chiave pubblica del firmatario.
>     
> - $m$: è il messaggio da firmare.
>     
> - $H$: è una funzione di hash crittografica.
>     
> - $R$: è un punto sulla curva ellittica calcolato dal nonce.
>     
> - La firma finale è la coppia $(R, s)$.
>     

---

## 4. Algoritmo di Verifica (Verification)

Il verificatore utilizza la chiave pubblica per controllare la validità della firma.

**The verification steps are:**

$$\begin{align} 1. \ \text{Input} &: \text{Chiave Pubblica } A, \text{Messaggio } m, \text{Firma } (R, s) \\ 2. \ h &= H(R, A, m) \quad (\text{Ricalcolo del challenge}) \\ 3. \ \text{Check} &: \text{Verifica equazione della curva} \end{align}$$

> [!abstract] Math Analysis
> 
> Il verificatore ricalcola l'hash $h$ usando i dati pubblici ($R, A, m$). Se l'equazione della curva ellittica è soddisfatta usando questo $h$, la firma è valida; altrimenti viene rifiutata.

---

## 5. Vantaggi Principali

> [!tip] Exam Focus
> 
> Ricorda perché EdDSA è preferito nelle moderne implementazioni (es. Passkeys, SSH, TLS 1.3):

- **Sicurezza Robusta:** Essendo deterministico, non soffre di fallimenti del generatore di numeri casuali (RNG failures).
    
- **Performance:** È molto veloce nelle implementazioni software, non richiedendo hardware dedicato per essere efficiente.
    
- **Semplicità:** È più difficile da implementare in modo errato rispetto a ECDSA.