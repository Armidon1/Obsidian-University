# **Block Cipher (Cifrario a blocchi)**

> È un **algoritmo di cifratura simmetrica** ([[Symmetric Encryption]]) che cifra i dati **a blocchi di dimensione fissa** (es. 64 o 128 bit) invece di singoli bit o byte, trasformando ogni blocco di testo in chiaro in un blocco di testo cifrato della stessa dimensione.

---

**Come funziona (in sintesi):**

1. Il messaggio viene diviso in **blocchi di dimensione fissa**.
    
2. Ogni blocco ( $P_i$ ) viene cifrato usando una **chiave segreta** ( $k$ ) tramite la funzione di cifratura:  $$C_i = E_k(P_i)$$
3. La decifratura utilizza la funzione inversa con la stessa chiave:  $$P_i = D_k(C_i)$$  

---

**Caratteristiche principali:**

- **Simmetrico:** stessa chiave per cifratura e decifratura.
    
- **Dimensione fissa:** tipicamente 64 o 128 bit per blocco.
    
- **Modalità operative:** può essere combinato con modalità come **[[ECB]], [[CBC]], [[CTR]], [[GCM]]** per migliorare sicurezza ed efficienza.
    

---

**Vantaggi:**

- Sicuro se combinato con modalità corrette.
    
- Adatto per cifrare grandi quantità di dati.
    

**Svantaggi:**

- Blocchi identici cifrati in **[[ECB]]** possono rivelare pattern.
    
- Non garantisce [[Integrity]] o [[Authenticity]] senza un [[MAC]]/[[HMAC]] o [[AEAD]].
    

---

**Esempi:**

- **[[AES]]** (Advanced Encryption Standard) – blocchi da 128 bit
    
- **[[DES]] / [[3DES]]** – blocchi da 64 bit
    
- **Blowfish / Twofish**
    

---

**In breve:**

> **Block cipher** = cifratura simmetrica su **blocchi di dati**.  
> Fornisce **[[Confidentiality]]**, ma per [[Integrity]] e [[Authenticity]] va combinata con modalità sicure o [[MAC]]/[[AEAD]].