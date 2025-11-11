# ✍️ DSA (Digital Signature Algorithm)

### Definizione

Il **Digital Signature Algorithm (DSA)** è un **algoritmo a chiave pubblica** standardizzato (Federal Information Processing Standard - FIPS) il cui unico scopo è la creazione e la verifica di **firme digitali**.

Come tutte le firme digitali, DSA garantisce:

- **[[Authentication]]:** Il ricevente può verificare che il messaggio provenga dal mittente.
    
- **[[Integrity]]:** Il messaggio non è stato alterato dopo essere stato firmato.
    
- **[[Non-Repudiation]]:** Il mittente non può negare di aver firmato il messaggio.
    

**Importante:** DSA **non può essere usato per la cifratura** ([[Confidentiality]]). È un algoritmo _esclusivamente_ per firme.

### Come Funziona (Concettualmente)

La sicurezza di DSA si basa sulla difficoltà computazionale del **[[The Discrete Logarithm (DL) Problem|Problema del Logaritmo Discreto (DLP)]]** all'interno di un gruppo moltiplicativo (simile a [[ElGamal]]).

#### 1. Parametri Comuni (Setup)

Prima di tutto, il sistema si accorda su parametri pubblici $(p, q, g)$:

- $p$: Un numero primo molto grande.
    
- $q$: Un numero primo più piccolo che divide $p-1$.
    
- $g$: Un generatore (base) calcolato da $p$ e $q$.
    

#### 2. Generazione Chiavi

- **Chiave Privata ($x$):** Un numero intero segreto scelto casualmente.
    
- **Chiave Pubblica ($y$):** Calcolata come $y = g^x \pmod p$.
    

#### 3. Processo di Firma (Mittente)

Per firmare un messaggio $m$:

1. Calcola un **hash** del messaggio: $h = \text{hash}(m)$.
    
2. **CRITICO:** Genera un **nonce segreto e casuale $k$** (un numero usato una sola volta).
    
3. La firma è una coppia di numeri $(r, s)$:
    
    - $r = (g^k \pmod p) \pmod q$
        
    - $s = k^{-1} \cdot (h + x \cdot r) \pmod q$
        
4. Il mittente invia il messaggio $m$ e la firma $(r, s)$.
    

#### 4. Processo di Verifica (Destinatario)

Per verificare la firma $(r, s)$ sul messaggio $m$:

1. Calcola l'hash $h = \text{hash}(m)$.
    
2. Calcola $w = s^{-1} \pmod q$.
    
3. Calcola $u_1 = h \cdot w \pmod q$ e $u_2 = r \cdot w \pmod q$.
    
4. Calcola $v = (g^{u_1} \cdot y^{u_2} \pmod p) \pmod q$.
    
5. **Verifica:** Se $v$ è uguale a $r$, la firma è **valida**. Altrimenti, è invalida.
    

### Dettagli Tecnici e Implicazioni per Ingegneri

|**Caratteristica**|**Descrizione Tecnica**|
|---|---|
|**Efficienza**|La firma DSA (che usa la chiave privata) è **veloce**. La verifica (che usa la chiave pubblica) è **lenta** a causa delle due esponenziazioni modulari.|
|**Dimensione Firma**|Le firme DSA sono relativamente compatte (es. 64 byte per una chiave a 1024 bit).|
|**Vulnerabilità CRITICA (Riuso del Nonce)**|Identica a ECDSA. L'intero algoritmo **fallisce catastroficamente** se il nonce $k$ (il numero casuale usato per firmare) viene **riutilizzato anche una sola volta** con la stessa chiave privata.<br><br>  <br><br>Il riutilizzo di $k$ permette a un attaccante di **calcolare algebricamente la chiave privata $x$** del firmatario.|
|**Soluzione (RFC 6979)**|Come per ECDSA, le implementazioni moderne usano **DSA Deterministico (RFC 6979)**, che genera il nonce $k$ in modo deterministico a partire dalla chiave privata e dall'hash del messaggio, eliminando il rischio.|
|**Stato Attuale**|DSA è considerato **legacy (obsoleto)**. È stato quasi interamente sostituito da **RSA** (per la sua flessibilità) e **ECDSA** (per la sua efficienza e le chiavi più corte a parità di sicurezza). Le librerie crittografiche moderne ne sconsigliano l'uso per nuove applicazioni.|