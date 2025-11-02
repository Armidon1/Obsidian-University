# **ChaCha20-Poly1305**

> **ChaCha20-Poly1305** è un moderno **schema [[AEAD]] (Authenticated Encryption with Associated Data)** che combina l’algoritmo di cifratura **[[ChaCha20]]** ([[Stream Cipher]]) con il meccanismo di autenticazione **[[Poly1305]]** ([[MAC]]).
> 
> Fornisce **[[Confidentiality]], [[Integrity]] e [[Authenticity]]** in un’unica operazione efficiente e sicura.

---

### 🧩 **Componenti principali**

1. **[[ChaCha20]]** → cifra i dati (encryption)
    
    - Stream cipher basato su addizioni, XOR e rotazioni di bit.
        
    - Usa una chiave di **256 bit**, un **nonce di 96 bit**, e un **contatore a 32 bit**.
        
    - Progettato per essere **sicuro e veloce** anche su CPU senza accelerazione hardware AES.
        
2. **[[Poly1305]]** → calcola il **Message Authentication Code (MAC)**
    
    - Usa un algoritmo matematico su modulo ( 2^{130} - 5 ).
        
    - Garantisce l’**integrità** e l’**autenticità** del messaggio cifrato e dei dati associati (AAD).
        

---

### ⚙️ **Funzionamento semplificato**

1. ChaCha20 genera un **keystream** pseudo-casuale.
    
2. Il plaintext viene **XORato** con il keystream → si ottiene il **ciphertext**.
    
3. Poly1305 calcola un **tag di autenticazione** sul ciphertext + AAD.
    
4. Durante la decifratura, il tag viene verificato:
    
    - se è valido → il messaggio è autentico e integro;
        
    - se non lo è → il messaggio è rifiutato.
        

---

### 🧠 **Proprietà**

- 🔐 **[[Confidentiality]]:** fornita da ChaCha20.
    
- ✅ **[[Integrity]] e [[Authenticity]]:** garantite da Poly1305.
    
- ⚡ **Prestazioni:** molto veloce anche su dispositivi mobili e embedded.
    
- 🧩 **[[Nonce]]:** ogni messaggio deve avere un **nonce univoco**, per evitare vulnerabilità.
    

---

### 📦 **Utilizzo pratico**

- Standardizzato in **RFC 8439**.
    
- Usato in:
    
    - **[[TLS]] 1.3**
        
    - **SSH**
        
    - **WireGuard**
        
    - **Google QUIC / HTTP/3**
        
    - **OpenVPN**
        

---

### 📘 **In breve**

> **ChaCha20-Poly1305 = AEAD moderno → cifratura + autenticazione.**  
> Sicuro, efficiente e adatto a tutte le piattaforme, anche dove AES è lento.