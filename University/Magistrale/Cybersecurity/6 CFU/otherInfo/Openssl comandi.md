Ecco dei **"Pattern Mentali"** da memorizzare.

L'idea è imparare lo scheletro fisso del comando e sapere dove inserire le "variabili" (i nomi dei file che il prof ti darà nel testo dell'esercizio).

Usa questa legenda per i segnaposto:

- `[ALGO]` = Algoritmo (es. `aes-256-cbc`, `sha256`)
    
- `[PRIV]` = File Chiave Privata
    
- `[PUB]` = File Chiave Pubblica
    
- `[IN]` = File di Input
    
- `[OUT]` = File di Output
    

---

### 1. Pattern Gestione Chiavi (Comando `rsa`)

Questo comando serve per **creare**, **proteggere** o **estrarre** parti di chiavi.

Scheletro:

openssl rsa -in [INPUT_KEY] [AZIONE] -out [OUTPUT_KEY]

- **Se devi estrarre la pubblica:**
    
    - Azione: `-pubout`
        
    - _Esempio:_ `openssl rsa -in priv.pem -pubout -out pub.pem`
        
- **Se devi cifrare la privata (mettere password):**
    
    - Azione: `-[ALGO]` (es. `-aes256`)
        
    - _Esempio:_ `openssl rsa -in priv.pem -aes256 -out priv_secure.pem`
        
- **Se devi togliere la password:**
    
    - Azione: (nessuna flag particolare, basta non mettere l'algo)
        
    - _Esempio:_ `openssl rsa -in priv_secure.pem -out priv_plain.pem`
        

> **Regola d'oro:** Se leggi "estrai pubblica", scrivi subito **`-pubout`**.

---

### 2. Pattern Crittografia Asimmetrica (Comando `pkeyutl`)

Usa questo per cifrare/decifrare file piccoli o chiavi AES usando RSA.

Scheletro:

openssl pkeyutl -[OPERAZIONE] -inkey [CHIAVE] [OPZIONI_CHIAVE] -in [IN] -out [OUT]

- **Se Cifri (Confidenzialità):**
    
    - Operazione: `-encrypt`
        
    - Chiave: `[PUB]`
        
    - Opzione Chiave: `-pubin` (Obbligatorio!)
        
- **Se Decifri:**
    
    - Operazione: `-decrypt`
        
    - Chiave: `[PRIV]`
        
    - Opzione Chiave: (Nessuna, la privata è default)
        

> Regola d'oro:
> 
> Cifrare = Pubblica in input (-pubin).
> 
> Decifrare = Privata in input.

---

### 3. Pattern Firma Digitale (Comando `dgst`)

Usa questo per firmare documenti e verificare firme.

Scheletro:

openssl dgst -[HASH] -[AZIONE] [CHIAVE] [OPZIONI_EXTRA] [FILE_ORIGINALE]

- **Se Firmi (Crei la firma):**
    
    - Azione: `-sign`
        
    - Chiave: `[PRIV]`
        
    - Opzioni Extra: `-out [FILE_FIRMA]`
        
    - _Comando:_ `openssl dgst -sha256 -sign priv.pem -out firma.bin doc.pdf`
        
- **Se Verifichi (Controlli la firma):**
    
    - Azione: `-verify`
        
    - Chiave: `[PUB]`
        
    - Opzioni Extra: `-signature [FILE_FIRMA]`
        
    - _Comando:_ `openssl dgst -sha256 -verify pub.pem -signature firma.bin doc.pdf`
        

> Regola d'oro:
> 
> L'ordine nella verifica è sacro: Chiave -> Firma -> File Originale.

---

### 4. Pattern Cifratura Simmetrica (Comando `enc`)

Usa questo per cifrare file grossi con password.

Scheletro:

openssl enc -[ALGO] -[AZIONE] -in [IN] -out [OUT]

- **Se Cifri:**
    
    - Azione: `-e` (spesso opzionale perché è default, ma meglio metterlo)
        
    - Consiglio: Aggiungi `-p` per vedere sale/chiave/IV a video.
        
- **Se Decifri:**
    
    - Azione: `-d` (Obbligatorio!)
        

> **Regola d'oro:** Se devi decifrare e dimentichi **`-d`**, stai cifrando il file cifrato una seconda volta!

---

### 5. Pattern Ispezione (Comandi `x509` o `rsa`)

Usa questo per "leggere" il contenuto di file codificati in base64.

Scheletro:

openssl [TIPO] -in [FILE] -text -noout

- **Se è un Certificato:** TIPO = `x509`
    
- **Se è una Chiave:** TIPO = `rsa` (o `pkey`)
    
- **Se è una richiesta (CSR):** TIPO = `req`
    

> **Regola d'oro:** La coppia **`-text -noout`** va sempre insieme. `-text` traduce, `-noout` pulisce la spazzatura.

---

#### Tabella Riassuntiva "Salva-Esame"

Impara a memoria solo le associazioni di questa tabella:

|**Obiettivo**|**Comando**|**Chiave da usare**|**Flag Critica da non scordare**|
|---|---|---|---|
|**Estrarre Pubblica**|`rsa`|Privata|`-pubout`|
|**Cifrare (RSA)**|`pkeyutl`|Pubblica|`-encrypt -pubin`|
|**Decifrare (RSA)**|`pkeyutl`|Privata|`-decrypt`|
|**Firmare**|`dgst`|Privata|`-sign`|
|**Verificare**|`dgst`|Pubblica|`-verify ... -signature`|
|**Decifrare (AES)**|`enc`|(Password)|`-d`|
|**Leggere Cert.**|`x509`|-|`-text -noout`|


---

### 6. Pattern Generazione Casualità (Comando `rand`)

Il professore potrebbe chiederti: _"Genera un IV casuale di 16 byte"_ oppure _"Genera una chiave di sessione casuale per AES-256"_.

Scheletro:

openssl rand -[FORMATO] [NUMERO_BYTE] > [FILE_OUTPUT]

- **Esempio:** Genera 16 byte casuali in esadecimale (utile per IV).
    
    - _Comando:_ `openssl rand -hex 16`
        
- **Esempio:** Genera 32 byte casuali (256 bit) e salvali in un file binario (utile per chiave AES).
    
    - _Comando:_ `openssl rand -out session_key.bin 32`
        

> Regola d'oro:
> 
> Se l'output deve essere leggibile/copiabile, usa -hex.
> 
> Se deve essere un file chiave, usa -out (binario).

---

### 7. Pattern Hashing Semplice (Comando `dgst` senza sign)

A volte la domanda è solo sull'**integrità** (senza autenticazione/firma): _"Calcola l'impronta SHA-256 del file data.txt"_.

Scheletro:

openssl dgst -[HASH] [FILE]

- **Esempio:** `openssl dgst -sha256 data.txt`
    

> Regola d'oro:
> 
> È uguale al comando di firma, ma senza -sign [KEY] e senza -out. Stampa solo l'hash a video.

---

### 8. Pattern PKI: Richiesta di Certificato (Comando `req`)

Questo capita nelle domande sulla PKI (Certificate Authority).

Scenario: "Sei un amministratore web. Hai creato la chiave privata. Ora crea la CSR (Certificate Signing Request) da inviare alla CA per ottenere il certificato."

Scheletro:

openssl req -new -key [PRIV] -out [OUTPUT.csr]

- **Esempio:** `openssl req -new -key my_priv.pem -out richiesta.csr`
    
    - _Nota:_ A questo punto OpenSSL ti farà una serie di domande interattive (Country, Organization, Common Name, ecc.).
        

> Regola d'oro:
> 
> CSR = comando req.
> 
> Input = Chiave Privata (-key).
> 
> Output = File CSR (-out).

---

### 9. Pattern Parametri Diffie-Hellman (Comando `dhparam`)

Raro, ma presente in qualche vecchio esame sulla teoria dei numeri.

Scenario: "Genera i parametri Diffie-Hellman (i numeri primi p e g) a 2048 bit".

Scheletro:

openssl dhparam -out [OUTPUT_FILE] [BIT]

- **Esempio:** `openssl dhparam -out dh_params.pem 2048`
    

---

### Riepilogo Totale (Cheat Sheet Definitivo)

Ecco la "Mappa Completa" di tutto ciò che può succedere all'esame OpenSSL. Se sai questi, sai tutto.

|**Categoria**|**Comando Chiave**|**Cosa fa**|**Esempio Flash**|
|---|---|---|---|
|**Chiavi**|`genpkey` / `genrsa`|Crea chiavi|`genrsa -out k.pem 2048`|
|**Chiavi**|`rsa`|Estrae Pubblica|`rsa -in k.pem -pubout`|
|**Crypto**|`pkeyutl`|Cifra (con Pub)|`pkeyutl -encrypt -pubin`|
|**Crypto**|`pkeyutl`|Decifra (con Priv)|`pkeyutl -decrypt`|
|**Crypto**|`enc`|Cifra Simmetrica|`enc -aes256 -e`|
|**Firma**|`dgst`|Firma (con Priv)|`dgst -sign k.pem`|
|**Firma**|`dgst`|Verifica (con Pub)|`dgst -verify p.pem`|
|**Hash**|`dgst`|Solo Hash|`dgst -sha256`|
|**PKI**|`req`|Crea CSR|`req -new -key k.pem`|
|**PKI**|`x509`|Legge Cert|`x509 -in c.pem -text`|
|**Random**|`rand`|Crea IV/Key|`rand -hex 16`|

Ti senti coperto ora? Vuoi provare a combinare qualcuno di questi (es. generare una chiave random e poi cifrarla con RSA)?