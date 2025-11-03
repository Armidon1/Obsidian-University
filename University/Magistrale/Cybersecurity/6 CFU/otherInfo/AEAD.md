# **AEAD (Authenticated Encryption with Associated Data)**

> È un **meccanismo crittografico** che fornisce **[[Confidentiality]], [[Integrity]] e [[Authenticity]]** dei dati **in un’unica operazione**.

**Caratteristiche principali:**

- Cifra il messaggio (confidenzialità).
    
- Genera un **tag di autenticazione** ([[MAC]]) per verificare che il messaggio e i dati associati non siano stati alterati (integrità e autenticità).
    
- Permette di includere **dati non cifrati ma autenticati** (Associated Data), come intestazioni di protocollo.
    

**Esempi:**

- **[[AES-GCM]] ([[AES]] in modalità Galois/Counter [[GCM]])
    
- **[[ChaCha20-Poly1305]]**
    

**In breve:**

> AEAD = cifratura + autenticazione in un unico schema sicuro,  
> garantisce **confidenzialità, integrità e autenticità** dei messaggi.

## Come AEAD estende [[AE]] 
**AEAD è un’estensione (e miglioramento pratico) di AE**. Ti spiego chiaramente la differenza 👇

---

### 🔐 **AE (Authenticated Encryption)**

> È il concetto generale di **cifratura autenticata**: un sistema che fornisce **confidenzialità + integrità + autenticità** del messaggio.

➡️ L’AE protegge **solo il messaggio cifrato (plaintext → ciphertext)**.  
Non prevede esplicitamente dati “extra” da autenticare.

---

### 🔑 **AEAD (Authenticated Encryption with Associated Data)**

> È una **forma estesa e standardizzata di AE** che, oltre a cifrare e autenticare il messaggio, permette anche di **autenticare dati aggiuntivi non cifrati** (_Associated Data_, AD).

---

### ⚙️ **Funzionamento AEAD**

Input:

- Chiave segreta ( K )
    
- Nonce (valore unico per messaggio)
    
- Plaintext ( P )
    
- **Associated Data (AD)** → non cifrati ma autenticati (es. header, indirizzi, ID di sessione)
    

Output:    
$$C, T = \text{AEAD-Encrypt}(K, \text{nonce}, P, AD)$$
Durante la decifratura:  $$  P = \text{AEAD-Decrypt}(K, \text{nonce}, C, AD, T)  
$$
→ Se il **tag T** non è valido, il messaggio è rifiutato.

---

### 🧩 **Differenza chiave**

|Caratteristica|AE|AEAD|
|---|---|---|
|Protegge confidenzialità|✅|✅|
|Protegge integrità/autenticità|✅|✅|
|Autentica dati non cifrati (AD)|❌|✅|
|Standard moderno (TLS 1.3, SSH, QUIC)|⚠️|✅|

---

### 💡 **Esempi di AEAD**

- **AES-GCM**
    
- **ChaCha20-Poly1305**
    
- **AES-CCM**
    

---

### 📘 **In breve**

> ✅ **AEAD** = _Authenticated Encryption + Associated Data_  
> È un **AE “potenziato”** che protegge sia il messaggio cifrato **sia i metadati** (non cifrati ma autenticati).  
> È lo **standard moderno** nei protocolli di sicurezza come **TLS 1.3, WireGuard, QUIC, SSH**.


Guarda anche [[6 CS - Authenticated Encryption#AEAD GCM]]
