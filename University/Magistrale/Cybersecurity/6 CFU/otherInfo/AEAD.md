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

Guarda anche [[6 CS - Authenticated Encryption#AEAD GCM]]
