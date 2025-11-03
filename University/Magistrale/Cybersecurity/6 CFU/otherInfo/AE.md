# **Authenticated Encryption (AE)**

> **Authenticated Encryption (AE)** è un approccio crittografico che **combina cifratura e autenticazione** in un unico meccanismo, garantendo **[[Confidentiality]]**, **[[Integrity]]** e **[[Authenticity]]** del messaggio.

---

### 🧩 **Obiettivo**

Tradizionalmente, cifratura (es. [[AES]]) protegge solo la **[[Confidentiality]]**, mentre un [[MAC]] (es. [[HMAC]], [[Poly1305]]) protegge **[[Integrity]]** e **[[Authenticity]]**.  
Con **AE**, entrambe le protezioni vengono **integrate in un unico algoritmo**, evitando errori d’uso e vulnerabilità di combinazione (come [[EtM]], [[MtE]], [[EaM]]).

---

### ⚙️ **Funzionamento generale**

Un algoritmo AE prende in input:

- una **chiave segreta** ( K ),
    
- un **nonce/IV** (numero univoco per messaggio),
    
- un **plaintext** ( P ),
    
- opzionalmente **Associated Data (AD)** (dati non cifrati ma autenticati, come header o metadata).
    

E produce:  
[  
C, T = \text{Encrypt}(K, \text{nonce}, P, AD)  
]  
dove

- ( C ) = ciphertext
    
- ( T ) = tag di autenticazione
    

Durante la decifratura, il tag ( T ) viene verificato: se non corrisponde, il messaggio è **rifiutato**.

---

### 🔒 **Proprietà**

- 🔐 **Confidenzialità:** il contenuto è cifrato.
    
- ✅ **Integrità:** eventuali modifiche vengono rilevate.
    
- 🧭 **Autenticità:** il destinatario sa che il messaggio proviene dal mittente legittimo.
    
- 🚫 **Fail-safe:** la decifratura fallisce automaticamente se il tag non è valido.
    

---

### 🧠 **Esempi di algoritmi AE**

- **AES-GCM** (Galois/Counter Mode)
    
- **ChaCha20-Poly1305**
    
- **AES-CCM**
    
- **OCB mode**
    
- **SIV (Synthetic IV) mode** – resistente ai nonce ripetuti
    

---

### 📘 **In breve**

> **Authenticated Encryption (AE)** = cifratura + autenticazione in un unico schema.  
> Garantisce che il messaggio sia **riservato, integro e autentico** — è lo **standard moderno** nei protocolli sicuri come **TLS 1.3, SSH, IPsec, WireGuard**.

un estensione naturale di AE è [[AEAD]]