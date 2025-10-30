# **Galois Authentication (Autenticazione Galois)**

> È il meccanismo di **autenticazione dei dati** utilizzato in **modalità [[AEAD]]** come **[[AES-GCM]]**, basato su operazioni matematiche nel **campo di Galois GF(2¹²⁸)**.  
> Serve a garantire **[[Integrity]] e [[Authenticity]]** dei messaggi cifrati e dei dati associati.

---

**Come funziona (in sintesi):**

1. I dati cifrati e i **dati associati non cifrati** (Associated Data) vengono trattati come **polinomi** nel campo di Galois GF(2¹²⁸).
    
2. Il risultato viene combinato con la **chiave di autenticazione derivata da AES**.
    
3. Il valore finale è il **tag di autenticazione** (authentication tag) che accompagna il messaggio.
    
4. Il destinatario ricalcola il tag e lo confronta con quello ricevuto:
    
    - Se coincidono → il messaggio è integro e autentico.
        
    - Se differiscono → il messaggio è stato alterato o non proviene dalla fonte legittima.
        

---

**Garantisce:**

- ✅ **Integrity** – rileva qualsiasi modifica al messaggio o ai dati associati.
    
- ✅ **Authenticity** – solo chi possiede la chiave può generare un tag valido.
    

**Non garantisce da solo:**

- ❌ **Confidentiality** – non cifra i dati; viene combinato con AES-CTR per protezione completa (come in AES-GCM).
    

---

**Vantaggi principali:**

- Altamente efficiente e parallelizzabile.
    
- Resistente a molti tipi di attacchi crittografici.
    
- Supporta **dati associati non cifrati** mantenendoli autenticati.
    

---

**Esempi d’uso:**

- **AES-GCM** in TLS 1.2/1.3
    
- VPN e protocolli IPsec
    
- Cloud storage sicuro e crittografia dei messaggi
    

---

**In breve:**

> **Galois Authentication** = autenticazione veloce e sicura tramite algebra di Galois,  
> fornendo **integrità e autenticità** nei sistemi AEAD come **AES-GCM**.