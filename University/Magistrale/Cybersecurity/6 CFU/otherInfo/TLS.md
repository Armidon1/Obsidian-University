# **TLS (Transport Layer Security)**

> È un **protocollo crittografico** che fornisce **sicurezza nelle comunicazioni su rete**, garantendo **[[Confidentiality]]**, **[[Integrity]]** e **[[Authenticity]]** dei dati scambiati tra due entità (es. client e server).

**Come funziona (in sintesi):**

1. **Handshake:**
    
    - Il client e il server negoziano le versioni del protocollo, gli algoritmi di cifratura e si scambiano certificati digitali.
        
    - Viene stabilita una **chiave di sessione segreta** tramite meccanismi come Diffie–Hellman.
        
2. **Sessione sicura:**
    
    - Tutti i dati successivi vengono **cifrati** con chiavi simmetriche derivate dal handshake.
        
    - Ogni messaggio è accompagnato da un **[[MAC]] o [[HMAC]]** per garantire l’integrità.
        

**Garantisce:**

- ✅ **[[Confidentiality]]:** tramite cifratura dei dati ([[AES]], [[ChaCha20]], ecc.)
    
- ✅ **[[Integrity]]:** tramite [[MAC]]/[[HMAC]] o [[AEAD]] (Authenticated Encryption)
    
- ✅ **[[Authenticity]]:** tramite certificati digitali e firme del server (e, opzionalmente, del client)
    

**Non garantisce:**

- ❌ **[[Availability]]** (non previene [[DoS]])
    

**Esempi d’uso:** [[HTTPS]], email sicura (SMTPS, IMAPS), VPN, VoIP.

**In breve:**

> TLS = canale di comunicazione **autenticato e cifrato** tra due parti su Internet.