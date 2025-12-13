# PKCS#1 (Public-Key Cryptography Standards #1)

**Tag:** #crittografia #RSA #standard #IETF #RFC #sicurezza

## 1. Definizione

PKCS#1 è il primo della famiglia dei Public-Key Cryptography Standards (PKCS), pubblicati originariamente da RSA Laboratories (ora parte di EMC/Dell).

Definisce le raccomandazioni fondamentali per l'implementazione dell'algoritmo [[RSA]], specificando come cifrare, firmare e formattare i dati e le chiavi.

L'ultima versione è standardizzata nella **RFC 8017** (v2.2).

## 2. Architettura dello Standard

Lo standard distingue nettamente tra **Primitive** e **Schemi**:

### A. Primitive (Mathematical Core)

Sono le operazioni matematiche di base, non sicure se usate da sole.

- **[[RSAEP]] / [[RSADP]]:** Cifratura e Decifratura grezza ($c = m^e \pmod n$).
    
- **RSASP1 / RSAVP1:** Generazione e Verifica della firma grezza ($s = m^d \pmod n$).
    
- **[[OS2IP]] / [[I2OSP]]:** Conversioni tra Interi e Stringhe di Ottetti (Byte).
    

### B. Schemi (Secure Protocols)

Combinano le primitive con tecniche di **padding** e hashing per fornire garanzie di sicurezza complete.

- **[[RSAES]] (Encryption Schemes):** Per la cifratura dei dati.
    
- **RSASSA (Signature Schemes with Appendix):** Per la firma digitale.
    

## 3. Evoluzione e Versioni

Lo standard si è evoluto per rispondere a vulnerabilità critiche.

### PKCS#1 v1.5 (Legacy)

- **Status:** Deprecato per la cifratura; ancora supportato per firme (ma sconsigliato).
    
- **Cifratura (RSAES-PKCS1-v1_5):** Usa un padding semplice con byte casuali non-zero.
    
    - _Problema:_ Vulnerabile ad attacchi **Chosen-Ciphertext** (es. Attacco di Bleichenbacher / Padding Oracle).
        
- **Firma (RSASSA-PKCS1-v1_5):** Deterministica. Ancora diffusa nei certificati X.509 e in TLS < 1.3.
    

### PKCS#1 v2.x (Moderno)

Introduce schemi basati su **OAEP** e **PSS** per garantire sicurezza provabile.

- **Cifratura ([[RSAES-OAEP]]):**
    
    - Usa **[[RSA-OAEP]]** (Optimal Asymmetric Encryption Padding).
        
    - Integra funzioni hash (es. [[SHA-256]]) e [[Mask Generation Function (MGF)]].
        
    - Sicuro contro attacchi CCA2.
        
- **Firma ([[RSA-PSS|RSASSA-PSS]]):**
    
    - Usa **[[RSA-PSS]]** (Probabilistic Signature Scheme).
        
    - Probabilistico: la stessa firma generata due volte è diversa (grazie al salt).
        
    - Sicurezza dimostrabile nel modello Random Oracle.
        

## 4. Riepilogo Schemi

|**Funzione**|**Schema Legacy (v1.5)**|**Schema Moderno (v2.x)**|
|---|---|---|
|**Cifratura**|`RSAES-PKCS1-v1_5` (INSICURO)|**`RSAES-OAEP`** (RACCOMANDATO)|
|**Firma**|`RSASSA-PKCS1-v1_5` (ACCETTABILE)|**`RSASSA-PSS`** (RACCOMANDATO)|

## 5. Formato delle Chiavi

PKCS#1 definisce anche la sintassi ASN.1 per salvare le chiavi RSA:

- **Chiave Pubblica (`RSAPublicKey`):** Contiene $n, e$.
    
- **Chiave Privata (`RSAPrivateKey`):** Contiene $n, e, d, p, q$ e i coefficienti per il calcolo CRT ($dP, dQ, qInv$).
    

---

**Vedi anche:**

- [[RSA]]
    
- [[RSAES-OAEP]]
    
- [[RSA-PSS]]
    
- [[IETF]] (Internet Engineering Task Force)