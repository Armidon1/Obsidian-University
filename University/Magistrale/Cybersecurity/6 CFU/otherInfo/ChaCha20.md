# **ChaCha20**

> È un **algoritmo di cifratura simmetrica a flusso ([[stream cipher]])** progettato da Daniel J. Bernstein, come alternativa veloce e sicura ad [[AES]] in modalità CTR.  
> Serve a garantire **[[Confidentiality]]** dei dati, soprattutto in ambienti con **hardware limitato** o su dispositivi mobili.

---

**Come funziona (in sintesi):**

1. Usa una **chiave simmetrica** (256 bit) e un **nonce** (numero unico per ogni messaggio).
    
2. Genera un **keystream pseudo-casuale** tramite operazioni su 512-bit state matrix.
    
3. Applica un **XOR bit-a-bit** tra il keystream e il testo in chiaro per produrre il testo cifrato:  $$C = P \oplus \text{Keystream}  $$
4. La decifratura è simmetrica: lo stesso keystream XORato con il ciphertext restituisce il plaintext.
    

---

**Garantisce:**

- ✅ **Confidentiality** – i dati cifrati sono illeggibili senza la chiave.
    
- ✅ **Resistenza a molti attacchi pratici** su flussi di dati e chiavi ripetute, se usato correttamente.
    

**Non garantisce da solo:**

- ❌ **[[Integrity]]** o **[[Authenticity]]** (per questo si combina spesso con **[[Poly1305]]**, formando **ChaCha20-Poly1305**, AEAD).
    

---

**Vantaggi principali:**

- Molto veloce su CPU senza istruzioni AES dedicate.
    
- Sicuro contro attacchi side-channel comuni su AES.
    
- Ideale per IoT, VPN, TLS su dispositivi mobili.
    

---

**Esempi d’uso:**

- TLS 1.3 (ChaCha20-Poly1305)
    
- OpenSSH
    
- WireGuard VPN
    
- Protocolli IoT sicuri e applicazioni mobile
    

---

**In breve:**

> **ChaCha20** = cifratura **simmetrica a flusso** moderna, veloce e sicura.  
> Garantisce **confidenzialità** e viene spesso combinata con **[[Poly1305]]** per autenticazione e integrità.

Vedi anche [[2 CS - Stream Ciphers#ChaCha20]]
