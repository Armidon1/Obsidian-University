
#### PBKDF2 (Standard Attuale)

- **Definizione:** Il successore e attuale standard industriale [[PBKDF]] (definito in RFC 2898 / PKCS #5 v2.0).
    
- **Funzionamento:** Sostituisce la semplice funzione di hash con una **PRF (Pseudorandom Function)**, quasi sempre implementata come **[[HMAC]]** (es. HMAC-SHA256).
    
- **Vantaggi Chiave:**
    
    1. **Lunghezza di Output Flessibile:** È stato progettato specificamente per generare chiavi di **qualsiasi lunghezza desiderata**. Lo fa concatenando i risultati di più blocchi di calcolo iterativo.
        
    2. **Flessibilità Algoritmica:** Può utilizzare diverse funzioni di hash (SHA-1, SHA-256, SHA-512) come base per l'HMAC, permettendo al sistema di adattarsi a standard di sicurezza più recenti.
        
    3. **Sicurezza (HMAC):** L'uso di HMAC fornisce proprietà crittografiche più forti rispetto al semplice hashing iterativo usato in PBKDF1.
        

**In sintesi:** [[PBKDF1]] è obsoleto perché non poteva produrre chiavi sufficientemente lunghe. **PBKDF2** è lo standard moderno che risolve questo problema, consentendo un output di lunghezza arbitraria e utilizzando la costruzione HMAC, più sicura.