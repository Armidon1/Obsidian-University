	Ecco la definizione di PBKDF e la spiegazione di PBKDF1 e 2.

### 🔑 PBKDF (Password-Based Key Derivation Function)

Una **PBKDF (Password-Based Key Derivation Function)** è una **funzione crittografica** (specificamente una KDF) progettata per un unico scopo: prendere una password a bassa entropia (come `password123`) e trasformarla in una **chiave crittografica forte e sicura** di lunghezza desiderata (es. 256 bit).

Il suo obiettivo principale è rendere gli attacchi a dizionario e _brute-force_ sulla password originale computazionalmente **costosi e lenti**.

Per un ingegnere, i suoi componenti chiave sono:

1. **Salt:** Un valore casuale unico generato per ogni utente. Il _salt_ viene combinato con la password prima dell'elaborazione. Questo neutralizza gli attacchi basati su _rainbow table_ (tabelle pre-calcolate di hash), poiché la stessa password produrrà un hash completamente diverso per ogni _salt_ diverso.
    
2. **Key Stretching (Stiramento):** La funzione esegue un processo iterativo ad alto costo computazionale (es. applicando un HMAC migliaia o milioni di volte). Questo rallenta deliberatamente il processo di hashing, rendendo estremamente lento per un attaccante testare miliardi di password al secondo, anche con hardware specializzato (GPU/ASIC).
    

---

### [[PBKDF1]] vs. [[PBKDF2]]

Entrambe sono standard specificati nel **PKCS #5**, ma PBKDF2 è il successore che risolve una limitazione critica di PBKDF1.

#### PBKDF1 (Obsoleto)

- **Definizione:** La prima versione dello standard. Utilizzava una funzione di hash (come SHA-1) in modo iterativo.
    
- **Funzionamento:** Applicava ripetutamente l'hash alla concatenazione della password e del _salt_.
    
- **Limitazione Fatale:** La sua **lunghezza massima dell'output (chiave derivata) era limitata alla dimensione dell'output della funzione di hash sottostante**. Ad esempio, se usava SHA-1, non poteva produrre una chiave più lunga di 160 bit. Questo lo rende inadatto per molti algoritmi crittografici moderni che richiedono chiavi più lunghe (es. AES-256).
    

#### PBKDF2 (Standard Attuale)

- **Definizione:** Il successore e attuale standard industriale (definito in RFC 2898 / PKCS #5 v2.0).
    
- **Funzionamento:** Sostituisce la semplice funzione di hash con una **PRF (Pseudorandom Function)**, quasi sempre implementata come **HMAC** (es. HMAC-SHA256).
    
- **Vantaggi Chiave:**
    
    1. **Lunghezza di Output Flessibile:** È stato progettato specificamente per generare chiavi di **qualsiasi lunghezza desiderata**. Lo fa concatenando i risultati di più blocchi di calcolo iterativo.
        
    2. **Flessibilità Algoritmica:** Può utilizzare diverse funzioni di hash (SHA-1, SHA-256, SHA-512) come base per l'HMAC, permettendo al sistema di adattarsi a standard di sicurezza più recenti.
        
    3. **Sicurezza (HMAC):** L'uso di HMAC fornisce proprietà crittografiche più forti rispetto al semplice hashing iterativo usato in PBKDF1.
        

**In sintesi:** PBKDF1 è obsoleto perché non poteva produrre chiavi sufficientemente lunghe. **PBKDF2** è lo standard moderno che risolve questo problema, consentendo un output di lunghezza arbitraria e utilizzando la costruzione HMAC, più sicura.

---