# **Hashing (Funzione di hash)**

> È un **processo crittografico o matematico** che trasforma **un input di qualsiasi lunghezza** (messaggio, file, password) in un **valore di lunghezza fissa**, chiamato **hash** o **digest**, in modo **irreversibile**.

---

**Caratteristiche principali di una funzione di hash crittografica:**

1. **Deterministica:** lo stesso input produce sempre lo stesso hash.
    
2. **Irreversibile:** non è possibile ricavare l’input dall’hash.
    
3. **Collision-resistant:** difficile trovare due input diversi con lo stesso hash.
    
4. **Avalanche effect:** piccole modifiche all’input cambiano drasticamente l’hash.
    

---

**Garantisce:**

- ✅ **[[Integrity]]** – se l’hash calcolato al destinatario coincide con quello del mittente, il messaggio non è stato modificato.
    
- ✅ **Verifica rapida dei dati** – utile per checksum e deduplicazione.
    

**Non garantisce da solo:**

- ❌ **[[Confidentiality]]** – l’hash non nasconde il contenuto.
    
- ❌ **[[Authenticity]]** – chiunque può calcolare l’hash del messaggio se conosce il contenuto.
    

---

**Esempi d’uso:**

- **Verifica integrità dei file:** SHA-256 su download o backup.
    
- **Autenticazione di password:** archiviazione sicura con salt + hash (bcrypt, Argon2).
    
- **Creazione di [[MAC]] o [[HMAC]]:** combinazione di chiave segreta + hash per autenticazione dei messaggi.
    
- **Blockchain:** collegamento sicuro dei blocchi tramite hash.
    

---

**In breve:**

> **Hashing** = trasformare dati in un **digest unico e di lunghezza fissa**,  
> utile per **verifica integrità, firme digitali e autenticazione**,  
> ma non fornisce **confidenzialità** o **autenticazione** da solo.

Vedi anche [[4 CS - Data Integrity - MAC, attacks and SHA-1#HASHING FOR INTEGRITY|HASHING FOR INTEGRITY]]
