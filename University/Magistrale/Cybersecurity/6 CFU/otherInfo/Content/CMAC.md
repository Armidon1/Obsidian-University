# **CMAC (Cipher-based Message Authentication Code)**

> È una **versione migliorata e standardizzata** del **[[CBC-MAC]]**, progettata per fornire **autenticazione dei messaggi** (integrità e autenticità) in modo **sicuro anche per messaggi di lunghezza variabile**.  
> È definito dallo standard **NIST SP 800-38B**.

---

**Come funziona (in sintesi):**

1. Usa un **algoritmo di cifratura a blocchi** (come AES o 3DES).
    
2. Genera due **sottochiavi derivate** dalla chiave principale (K1 e K2) per gestire correttamente i messaggi di lunghezza diversa.
    
3. Il messaggio viene diviso in blocchi:
    
    - Se l’ultimo blocco è completo → viene combinato con K1.
        
    - Se è incompleto → viene riempito (padding) e combinato con K2.
        
4. I blocchi vengono poi processati come in CBC (con XOR e cifratura a blocchi).
    
5. L’**ultimo blocco cifrato** diventa il **tag MAC** finale.
    

---

**Garantisce:**

- ✅ **[[Integrity]]** – rileva qualsiasi modifica al messaggio.
    
- ✅ **[[Authenticity]]** – solo chi possiede la chiave può calcolare un [[MAC]] valido.
    
- ✅ **Sicurezza per messaggi di lunghezza variabile**, a differenza di CBC-MAC.
    

**Non garantisce:**

- ❌ **[[Confidentiality]]** – non cifra i dati, serve solo per autenticazione.
    

---

**Vantaggi rispetto a CBC-MAC:**

- Sicuro per messaggi di qualunque lunghezza.
    
- Evita vulnerabilità dovute al riutilizzo dell’IV o alla manipolazione dei blocchi.
    
- È semplice da implementare usando [[AES]] come base.
    

---

**Esempi d’uso:**

- Autenticazione nei protocolli **AES-CMAC** (IEEE 802.11i / WPA2).
    
- **IPsec** e **Bluetooth Security Architecture**.
    
- Messaggi autenticati in sistemi embedded e IoT.
    

---

**In breve:**

> **CMAC** è la versione moderna e sicura di **CBC-MAC**,  
> usata per garantire **integrità e autenticità** dei dati,  
> spesso implementata come **AES-CMAC** nei protocolli di sicurezza contemporanei.