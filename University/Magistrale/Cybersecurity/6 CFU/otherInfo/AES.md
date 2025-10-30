# **AES (Advanced Encryption Standard)**

> È un **algoritmo di cifratura simmetrica a blocchi** usato per garantire la **[[Confidentiality]] dei dati**, standardizzato dal NIST nel 2001 come successore del [[DES]].

**Caratteristiche principali:**

- Usa la **stessa chiave** per cifrare e decifrare (cifratura simmetrica).
    
- Opera su **blocchi di 128 bit**.
    
- Supporta chiavi di **128, 192 o 256 bit**, determinando il livello di sicurezza.
    
- Basato su una struttura matematica detta **rete di sostituzione–permutazione** (Substitution–Permutation Network).
    

**Modalità d’uso comuni (block modes):**

- **[[ECB]] (Electronic Codebook):** insicura, non protegge contro pattern ripetuti.
    
- **[[CBC]] (Cipher Block Chaining):** aggiunge casualità ma non autenticazione.
    
- **GCM (Galois/Counter Mode):** fornisce **confidenzialità + integrità** (autenticazione integrata).
    

**Garantisce:**

- ✅ **[[Confidentiality]]** — i dati sono cifrati e illeggibili senza la chiave corretta.
    

**Non garantisce da solo:**

- ❌ **[[Integrity]]**
    
- ❌ **[[Authenticity]]**
    

**Esempi d’uso:**

- Cifratura di file e dischi (BitLocker, VeraCrypt)
    
- Comunicazioni sicure ([[TLS]], IPsec, Wi-Fi WPA2/WPA3)
    
- Applicazioni e protocolli crittografici moderni
    

**In breve:**

> **AES** è il principale standard di cifratura simmetrica moderno: **veloce, sicuro e ampiamente adottato** per proteggere la **riservatezza dei dati**.