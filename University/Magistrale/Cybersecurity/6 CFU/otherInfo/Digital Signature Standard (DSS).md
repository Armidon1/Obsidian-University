# Digital Signature Standard (DSS)

## 1. Definizione e Contesto

Il **Digital Signature Standard (DSS)** è lo standard del governo degli Stati Uniti per le firme digitali, definito dal **[[NIST]]** nella pubblicazione **FIPS 186**.

È importante distinguere tra lo Standard (il documento legale/tecnico) e gli Algoritmi che esso approva.

Attualmente (FIPS 186-4/5), il DSS specifica tre algoritmi approvati per generare firme digitali:

1. **[[Digital Signature Algorithm (DSA)]]:** L'algoritmo originale creato appositamente per questo standard (una variante di [[ElGamal]]).
    
2. **[[RSA]]:** L'algoritmo classico (usato sia per cifratura che per firma).
    
3. **[[ECDSA]] (Elliptic Curve DSA):** La variante di DSA basata su curve ellittiche (oggi la più usata, es. Bitcoin, [[HTTPS]]).
    

## 2. DSA (Digital Signature Algorithm)

Spesso quando si dice "DSS" si intende impropriamente "[[Digital Signature Algorithm (DSA)]]".

Il DSA è stato proposto dal NIST nel 1991 come alternativa a RSA (che all'epoca era brevettato).

### Caratteristiche Chiave

- **Solo Firma:** A differenza di RSA, il DSA **non può essere usato per la cifratura** ([[Confidentiality]]). Serve solo per firmare e verificare.
    
- **Origine:** È una variante ottimizzata del **[[ElGamal]]**.
    
- **Sicurezza:** Basata sul **[[Discrete Logarithm (DL) Problem]]**  ($g^x \pmod p$).
    

### La Struttura della Firma $(r, s)$

Una firma DSA non è un singolo blocco di dati (come in RSA), ma una **coppia di grandi numeri interi** $(r, s)$.

1. **$r$:** Dipende dal parametro casuale $k$ e dalla chiave pubblica, ma _non_ dal messaggio.
    
2. **$s$:** Dipende dal messaggio (Hash), dalla chiave privata e da $r$.
    

## 3. L'Algoritmo DSA (Semplificato)

### Parametri Pubblici

- $p$: Un numero primo grande (es. 2048 bit).
    
- $q$: Un numero primo più piccolo (es. 256 bit) che divide $(p-1)$.
    
- $g$: Un [[Generatore g (radice primitiva)]] di un sottogruppo di ordine $q$.
    

### Generazione Firma (Signing)

Per firmare l'hash del messaggio $H(M)$ con la chiave privata $x$:

1. Si genera un numero segreto casuale **$k$** (il _nonce_ o _per-message secret_) tale che $0 < k < q$.
    
2. Si calcola $r$:
    
    $$r = (g^k \pmod p) \pmod q$$
    
3. Si calcola $s$:
    
    $$s = k^{-1} (H(M) + x \cdot r) \pmod q$$
    
4. La firma è la coppia $(r, s)$.
    

### Verifica

Il destinatario, conoscendo la chiave pubblica $y$:

1. Calcola $w = s^{-1} \pmod q$.
    
2. Calcola due componenti $u_1$ e $u_2$ basati sull'hash e sulla firma.
    
3. Calcola il valore di verifica $v$:
    
    $$v = (g^{u_1} y^{u_2} \pmod p) \pmod q$$
    
4. Accetta se $v == r$.
    

> [!abstract] Differenza Concettuale con RSA
> 
> - **RSA:** "Decifro l'hash con la chiave privata". (Deterministico senza padding).
>     
> - **DSA:** "Creo una prova matematica $(r, s)$ che lega l'hash alla chiave pubblica tramite un numero casuale". (Intrinsecamente probabilistico).
>     

## 4. Il Tallone d'Achille: Il parametro $k$

La sicurezza di DSA (e ECDSA) è **estremamente fragile** rispetto alla generazione del numero casuale $k$.

> [!failure] Vulnerabilità Critica (Catastrofe del Nonce)
> 
> Se per due messaggi diversi firmati con la stessa chiave privata viene usato lo stesso $k$:
> 
> 1. Il valore $r$ sarà identico.
>     
> 2. Un attaccante può usare l'algebra elementare per sottrarre le due equazioni delle firme e cancellare l'incognita $k$.
>     
> 3. **La chiave privata $x$ viene esposta immediatamente.**
>     
> 
> _Caso Reale:_ La PlayStation 3 (Sony) usava ECDSA con un $k$ statico. Gli hacker calcolarono la Master Key privata di Sony e poterono firmare qualsiasi software come "ufficiale".

Per evitare questo, oggi si usa il **Deterministic DSA (RFC 6979)**, che invece di scegliere $k$ a caso, lo genera come hash del messaggio e della chiave privata (rendendolo unico ma deterministico, simulando un [[PRF]]).

## 5. DSA vs RSA

|**Caratteristica**|**RSA**|**DSA / DSS**|
|---|---|---|
|**Funzione**|Cifratura + Firma|Solo Firma|
|**Performance Firma**|Più lenta|Più veloce (alcuni valori possono essere precalcolati)|
|**Performance Verifica**|**Molto veloce** (se $e$ è piccolo)|Molto lenta (operazioni esponenziali pesanti)|
|**Dimensione Chiavi**|Grandi (es. 2048/4096 bit)|Più compatte (specialmente ECDSA)|
|**Dominio**|Standard de facto per certificati web storici|Standard governativo USA, base per le crypto moderne (Bitcoin usa ECDSA)|

---

**Vedi anche:**

- [[ElGamal]] (Il padre del DSA)
    
- [[NIST]]
    
- [[RSA]]
    
- [[Generatore g (radice primitiva)]]
    
- [[RNG (Random Number Generator)]] (Cruciale per $k$)