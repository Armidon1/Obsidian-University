# **Symmetric Encryption (Cifratura Simmetrica)**

> È un **metodo di cifratura** in cui **la stessa chiave segreta** viene utilizzata sia per **cifrare** sia per **decifrare** i dati.

---

**Caratteristiche principali:**

1. **Chiave unica:** mittente e destinatario devono condividere la stessa chiave.
    
2. **Veloce:** adatto per cifrare grandi quantità di dati.
    
3. **Modalità operative:** può essere applicata a **blocchi** (block cipher) o a **flussi** (stream cipher).
    

---

**Garantisce:**

- ✅ **[[Confidentiality]]** – i dati sono illeggibili senza la chiave.
    

**Non garantisce da sola:**

- ❌ **[[Integrity]]** – non rileva modifiche al messaggio.
    
- ❌ **[[Authenticity]]** – chiunque con la chiave può cifrare o decifrare.
    

---

**Esempi:**

- **[[AES]] (Advanced Encryption Standard)** – block cipher
    
- **[[DES]] / [[3DES]]** – block cipher
    
- **[[ChaCha20]]** – stream cipher
    

---

**Vantaggi:**

- Alta velocità ed efficienza.
    
- Adatto per dati di grandi dimensioni.
    

**Svantaggi:**

- Distribuzione sicura della chiave tra mittente e destinatario può essere complessa (in questo viene usato l'[[Asymmetric Encryption]]).
    
- Se la chiave viene compromessa, l’intera comunicazione è a rischio.
    

---

**In breve:**

> **Symmetric encryption** = cifratura veloce e segreta con **una sola chiave condivisa**,  
> fornisce **[[Confidentiality]]**, ma necessita di ulteriori meccanismi per [[Authenticity]] e [[Integrity]].