# ✍️ ECDSA (Elliptic Curve Digital Signature Algorithm)

### Definizione

**ECDSA** è la versione della **[[Elliptic Curve Cryptography - ECC]]** del **[[Digital Signature Algorithm (DSA)]]**. È un algoritmo a chiave pubblica ampiamente utilizzato il cui unico scopo è fornire **firme digitali**.

Come tutte le firme digitali, ECDSA garantisce:

- **[[Authentication]]:** Il ricevente può verificare che il messaggio provenga dal mittente (che possiede la chiave privata).
    
- **[[Integrity]]:** Il messaggio non è stato alterato dopo essere stato firmato.
    
- **[[Non-Repudiation]]:** Il mittente non può negare di aver firmato il messaggio.
    

La sua sicurezza si basa sulla difficoltà computazionale del **Problema del Logaritmo Discreto su Curve Ellittiche ([[ECDLP]])**.

### Come Funziona (Concettualmente)

L'algoritmo utilizza una chiave privata (un numero) e una chiave pubblica (un punto sulla curva) per creare e verificare una firma (una coppia di numeri).

#### 1. Generazione Chiavi

- **Chiave Privata ($d$):** Un numero intero segreto scelto casualmente.
    
- **Chiave Pubblica ($Q$):** Un punto sulla curva calcolato come $Q = d \times G$ (dove $G$ è il punto base pubblico della curva).
    

#### 2. Processo di Firma (Mittente)

Per firmare un messaggio $m$:

1. Calcola un **hash** del messaggio: $h = \text{hash}(m)$.
    
2. **CRITICO:** Genera un **nonce segreto e casuale $k$** (un numero usato una sola volta).
    
3. Calcola un punto sulla curva $P = k \times G$.
    
4. La firma è una coppia di numeri $(r, s)$:
    
    - $r$ = la coordinata x del punto $P$.
        
    - $s = k^{-1} \cdot (h + r \cdot d) \pmod n$ (dove $n$ è l'ordine della curva).
        
5. Il mittente invia il messaggio $m$ e la firma $(r, s)$.
    

#### 3. Processo di Verifica (Destinatario)

Per verificare la firma $(r, s)$ sul messaggio $m$:

1. Calcola l'hash $h = \text{hash}(m)$.
    
2. Calcola due valori $u_1$ e $u_2$ usando la firma.
    
3. Calcola un punto di verifica $P' = (u_1 \times G) + (u_2 \times Q)$.
    
4. **Verifica:** Se la coordinata x del punto $P'$ è uguale a $r$, la firma è **valida**. Altrimenti, è invalida.
    

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