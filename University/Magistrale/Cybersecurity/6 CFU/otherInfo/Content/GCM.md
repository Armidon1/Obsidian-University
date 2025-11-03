# **GCM (Galois/Counter Mode)**

> È una **modalità di cifratura a blocchi** che fornisce **[[AEAD]] (Authenticated Encryption with Associated Data)**, cioè **[[Confidentiality]], [[Integrity]] e [[Authenticity]]** in un’unica operazione.

---

**Come funziona (in sintesi):**
![[Pasted image 20251103095538.png]]
1. **Cifratura:**
    
    - Usa un algoritmo a blocchi (es. AES) in **modalità counter (CTR)** per cifrare il messaggio, generando confidenzialità.
        
2. **Autenticazione:**
    
    - Calcola un **tag di autenticazione** usando operazioni di **Galois Field multiplication** sui dati cifrati e sugli eventuali dati associati non cifrati (Associated Data).
        
3. **Tag finale:**
    
    - Il destinatario verifica il tag per confermare che **nessuna modifica** sia stata fatta al messaggio o ai dati associati.
        

---

**Garantisce:**

- ✅ **[[Confidentiality]]** – i dati sono cifrati.
    
- ✅ **[[Integrity]]** – rileva modifiche ai dati cifrati o associati.
    
- ✅ **[[Authenticity]]** – assicura che il messaggio provenga dalla fonte legittima.
    

**Non garantisce:**

- ❌ **Disponibilità** – non protegge da interruzioni del servizio.
    

---

**Esempi d’uso:**

- [[TLS]] 1.2 e 1.3 (AES-GCM per HTTPS)
    
- VPN e protocolli IPsec
    
- Protezione dei dati su cloud storage
    

---

**In breve:**

> **GCM** = modalità [[AES]] che combina **cifratura in CTR** e **autenticazione Galois**,  
> fornendo **[[AEAD]]**: [[Confidentiality]] + [[Integrity]] + [[Authenticity]] in un unico schema sicuro.

vedi anche [[6 CS - Authenticated Encryption#What is GCM?]]
