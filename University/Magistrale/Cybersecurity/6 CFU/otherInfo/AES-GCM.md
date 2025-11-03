# **AES-GCM (Advanced Encryption Standard – Galois/Counter Mode)**

> È una **modalità [[AEAD]] (Authenticated Encryption with Associated Data)** basata su **[[AES]] in modalità [[CTR]]** combinata con **[[Galois Authentication]]** , che fornisce **[[Confidentiality]], [[Integrity]] e [[Authenticity]]** in un’unica operazione.

---

**Come funziona (in sintesi):**

1. **Cifratura ([[CTR]]):**
    
    - [[AES]] cifra il messaggio usando un **keystream generato da un contatore unico (nonce + counter)**.
        
2. **Autenticazione (Galois):**
    
    - Viene calcolato un **tag di autenticazione** tramite operazioni su [[Galois Field]] (GF(2¹²⁸)) sui dati cifrati e sui **dati associati non cifrati** (Associated Data).
        
3. **Verifica:**
    
    - Il destinatario ricalcola il tag e lo confronta con quello ricevuto per confermare **[[Integrity]] e [[Authenticity]]**.
        

---

**Garantisce:**

- ✅ **[[Confidentiality]]** – i dati sono cifrati.
    
- ✅ **[[Integrity]]** – rileva qualsiasi modifica ai dati cifrati o associati.
    
- ✅ **[[Authenticity]]** – assicura che il messaggio provenga dalla fonte legittima.
    

**Non garantisce:**

- ❌ **[[Availability]]** – non protegge da interruzioni o [[DoS]].
    

---

**Vantaggi principali:**

- Molto veloce e parallelizzabile.
    
- [[AEAD]] integrato: non serve aggiungere [[HMAC]] separato.
    
- Standard moderno per protocolli di sicurezza come [[TLS]] 1.2/1.3 e IPsec.
    

---

**Esempi d’uso:**

- **HTTPS/[[TLS]]**
    
- VPN (IPsec, WireGuard con AES-GCM)
    
- Cloud storage sicuro
    

---

**In breve:**

> **AES-GCM** = [[AES]] + [[CTR]] + [[Galois Authentication]] → cifratura **sicura e autenticata**.  
> Fornisce **[[Confidentiality]], [[Integrity]] e [[Authenticity]]** in un unico schema [[AEAD]].