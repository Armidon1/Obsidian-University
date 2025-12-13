# RSAES-OAEP (RSA Encryption Scheme - Optimal Asymmetric Encryption Padding)

**Tag:** #crittografia #RSA #standard #PKCS1 #sicurezza #implementazione

## 1. Definizione

[[RSAES]]-[[OAEP]] è lo schema di cifratura completo definito nello standard PKCS#1 v2.2 (RFC 8017).

Combina le primitive crittografiche RSA con lo schema di padding OAEP per fornire un sistema di cifratura a chiave pubblica sicuro contro attacchi a testo cifrato scelto ([[IND-CCA2]]).

## 2. Componenti dello Schema

Per funzionare, RSAES-OAEP assembla diverse primitive:

1. **Schema di Padding:** [[RSA-OAEP]] (per la sicurezza semantica e robustezza).
    
2. **Primitive RSA:** [[RSAEP]] (Cifratura) e [[RSADP]] (Decifratura).
    
3. **Conversioni:** [[OS2IP]] (Byte $\to$ Intero) e [[I2OSP]] (Intero $\to$ Byte).
    
4. **Funzioni Hash:** Una funzione hash $Hash$ (es. [[SHA-256]]) e una Mask Generation Function $MGF$ (es. [[Mask Generation Function (MGF)|MGF1]]).
    

## 3. Parametri del Protocollo

Prima di iniziare, mittente e destinatario devono concordare su:

- $Hash$:- La funzione hash da usare.
    
- $MGF$: La funzione di generazione della maschera ([[MGF]]).
    
- $L$: Una etichetta (label) opzionale associata al messaggio (di default è una stringa vuota).
    

## 4. Processo di Cifratura

Dato un messaggio $M$ e la chiave pubblica $(n, e)$:

1. **Controllo Lunghezza:** Se il messaggio $M$ è troppo lungo per il modulo (cioè $|M| > k - 2 \cdot hLen - 2$), l'operazione fallisce.
    
2. **Encoding (EME-OAEP):**
    
    - Si genera il blocco con padding OAEP usando un seed casuale.
        
    - Risultato: $EM$ (Encoded Message).
        
3. **Conversione in Intero:**
    
    - $m = \text{OS2IP}(EM)$.
        
4. **Cifratura RSA:**
    
    - $c = \text{RSAEP}((n, e), m) = m^e \pmod n$.
        
5. **Output:**
    
    - $C = \text{I2OSP}(c, k)$.
        

## 5. Processo di Decifratura

Dato un testo cifrato $C$ e la chiave privata $K$:

1. **Controllo Lunghezza:** Se la lunghezza di $C$ non è $k$ (lunghezza del modulo), errore.
    
2. **Conversione in Intero:**
    
    - $c = \text{OS2IP}(C)$.
        
3. **Decifratura RSA:**
    
    - $m = \text{RSADP}(K, c) = c^d \pmod n$.
        
    - Se RSADP fallisce, restituire "errore di decifratura".
        
4. **Conversione in Stringa:**
    
    - $EM = \text{I2OSP}(m, k)$.
        
5. **Decoding (EME-OAEP):**
    
    - Si separa $EM$ in seed mascherato e dati mascherati.
        
    - Si recupera il messaggio originale $M$ verificando il padding e l'hash dell'etichetta $L$.
        
    - **Nota di Sicurezza:** Se un qualsiasi controllo fallisce (es. byte di padding errato, hash mismatch), l'algoritmo deve restituire un errore generico ("decryption error") senza specificare _cosa_ è fallito, per prevenire attacchi oracolo.
        

## 6. Perché usare RSAES-OAEP?

- **Standard Moderno:** È l'unico schema di cifratura RSA raccomandato per nuove applicazioni.
    
- **Sicurezza:** Offre garanzie di sicurezza formale che mancano al vecchio RSAES-PKCS1-v1_5.
    
- **Interoperabilità:** Essendo definito in PKCS#1, è supportato da quasi tutte le librerie crittografiche (OpenSSL, Bouncy Castle, Java Crypto, ecc.).
    

---

**Vedi anche:**

- [[OAEP]] (Dettagli sul padding)
    
- [[RSAES]] (Concetto generale di schema RSA)
    
- [[PKCS#1]]