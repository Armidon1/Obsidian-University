# ✍️ ECDSA (Elliptic Curve Digital Signature Algorithm)

### Definizione

**ECDSA** è la versione della **[[Elliptic Curve Cryptography - ECC]]** del **[[Digital Signature Algorithm (DSA)]]**. È un algoritmo a chiave pubblica ampiamente utilizzato il cui unico scopo è fornire **firme digitali**.

Come tutte le firme digitali, ECDSA garantisce:

- **[[Authentication]]:** Il ricevente può verificare che il messaggio provenga dal mittente (che possiede la chiave privata).
    
- **[[Integrity]]:** Il messaggio non è stato alterato dopo essere stato firmato.
    
- **[[Non-Repudiation]]:** Il mittente non può negare di aver firmato il messaggio.
    

La sua sicurezza si basa sulla difficoltà computazionale del **Problema del Logaritmo Discreto su Curve Ellittiche ([[ECDLP]])**.

Ecco la Nota Master per Obsidian dedicata all'algoritmo **ECDSA**, basata sulle slide del corso.

---
## 2. Algoritmo di Firma (Signing)

Il processo di firma serve a generare una prova crittografica legata a un messaggio specifico e alla chiave privata dell'utente. A differenza di EdDSA, questo processo richiede una componente di casualità forte.

**The signing process is defined as:**

$$\begin{align} 1. & \ \text{Input: Private Key} \\ 2. & \ \text{Pick random nonce } k \\ 3. & \ \text{Compute Point } R \text{ (derived from } k) \\ 4. & \ \text{Compute challenge } h = H(m) \\ 5. & \ \text{Output Signature: } (r, s) \end{align}$$

> [!abstract] Math Analysis
> 
> - **Passo 1-2:** Il firmatario deve generare un numero casuale $k$ (nonce) per ogni singola firma.
>     
> - **Passo 3-5:** Utilizzando la chiave privata e il nonce, calcola un punto sulla curva e produce la coppia $(r, s)$. Ma che cosa sono $r$ ed $s$? ecco [[Cos'è (r,s) in ECDSA|qui]].
>     

---

## 3. Algoritmo di Verifica (Verification)

Il verificatore controlla la validità della firma utilizzando solo dati pubblici, senza mai conoscere la chiave privata.

**The verification logic is:**

$$\begin{align} \text{Input} &: \text{Public Key } Q, \text{Message } m, \text{Signature } (r, s) \\ \text{Step 1} &: \text{Recompute challenge } h = H(m) \\ \text{Step 2} &: \text{Perform curve operations using } Q, m, (r, s) \\ \text{Result} &: \text{Check if result matches } r \to \text{Accept/Reject} \end{align}$$

> [!abstract] Math Analysis
> 
> Il verificatore ricalcola l'hash del messaggio e combina la chiave pubblica con la firma. Se le operazioni sulla curva restituiscono il valore $r$ atteso, la firma è autentica.

---

## 4. La Vulnerabilità Critica: Il Random Nonce

La sicurezza di ECDSA dipende interamente dalla qualità del generatore di numeri casuali (RNG). Questo è il suo punto debole rispetto a EdDSA.

> [!failure] Common Pitfall: Randomness Failure
> 
> ECDSA si basa sul nonce casuale $k$.
> 
> - **Se l'RNG è debole:** Il nonce diventa prevedibile.
>     
> - **Se il nonce viene riutilizzato:** Se si firmano due messaggi diversi usando lo stesso $k$, un attaccante può calcolare matematicamente la **chiave privata** (Private Key Leakage).
>     
> 
> Questo rende ECDSA fragile in ambienti dove è difficile generare numeri veramente casuali (es. sistemi embedded poveri).

### Dettagli Tecnici e Implicazioni per Ingegneri

|**Caratteristica**|**Descrizione Tecnica**|
|---|---|
|**Efficienza (Vantaggio su RSA)**|**Chiavi e Firme Piccole:** A parità di sicurezza (es. 256-bit ECC vs 3072-bit RSA), le chiavi e le firme ECDSA sono _molto più piccole_. Questo è un vantaggio enorme in termini di **larghezza di banda** (es. certificati TLS, transazioni blockchain).|
|**Velocità**|**Firma Veloce:** La firma ECDSA (che usa la chiave privata) è generalmente molto più veloce della firma RSA.<br><br>  <br><br>**Verifica Lenta:** La verifica ECDSA (che usa la chiave pubblica) è più lenta della verifica RSA (se RSA usa un esponente pubblico piccolo come 65537).|
|**Vulnerabilità CRITICA (Riuso del Nonce)**|L'intero algoritmo **fallisce catastroficamente** se il nonce $k$ (il numero casuale usato per firmare) viene **riutilizzato anche una sola volta** con la stessa chiave privata.<br><br>  <br><br>Se un attaccante vede due firme $(r, s_1)$ e $(r, s_2)$ sullo stesso $r$ (o due firme diverse con lo stesso $k$), può **calcolare algebricamente la chiave privata $d$**.|
|**Soluzione (RFC 6979)**|A causa del pericolo degli RNG (Random Number Generator) deboli, le implementazioni moderne usano **ECDSA Deterministico (RFC 6979)**. Questo standard genera il nonce $k$ in modo deterministico a partire da un hash della chiave privata e del messaggio ($k = \text{hash}(d + h)$), eliminando la dipendenza da un RNG e il rischio di riutilizzo.|

### Usi Pratici

- **Criptovalute:** ECDSA (specificamente la curva `secp256k1`) è l'algoritmo usato da **Bitcoin** ed **Ethereum** per autorizzare le transazioni (ogni transazione è una firma che dimostra la proprietà dei fondi).
    
- **TLS/SSL:** Usato per l'autenticazione del server. Il server firma l'handshake TLS con la sua chiave privata ECDSA per dimostrare al client che possiede il certificato.
    
- **Sistemi Operativi e Software:** Usato per firmare digitalmente aggiornamenti e applicazioni per garantirne l'autenticità e l'integrità.