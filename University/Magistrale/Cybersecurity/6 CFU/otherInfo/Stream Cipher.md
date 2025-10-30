# **Stream Cipher (Cifrario a flusso)**

> È un **algoritmo di cifratura simmetrica** che cifra i dati **bit o byte per bit/byte**, generando un **keystream pseudo-casuale** da combinare con il testo in chiaro tramite un’operazione XOR.

---

**Come funziona (in sintesi):**

1. Il cifrario riceve:
    
    - Una **chiave segreta**
        
    - (Opzionalmente) un **nonce o vettore di inizializzazione**
        
2. Genera un **keystream** lungo quanto il messaggio da cifrare.
    
3. Cifra il messaggio:  $$C = P \oplus \text{Keystream}  $$
4. La decifratura usa lo stesso keystream e XOR:  $$P = C \oplus \text{Keystream}  $$

---

**Garantisce:**

- ✅ **[[Confidentiality]]** – i dati diventano illeggibili senza la chiave corretta.
    

**Non garantisce da solo:**

- ❌ **[[Integrity]]** – non rileva modifiche al messaggio.
    
- ❌ **[[Authenticity]]** – chiunque con un keystream valido può cifrare/decifrare.
    

---

**Vantaggi principali:**

- Molto veloce, adatto per flussi di dati continui.
    
- Richiede poca memoria, ideale per hardware limitato o sistemi embedded.
    
- Buono per cifrare dati di lunghezza variabile in tempo reale.
    

**Svantaggi:**

- Il keystream **non deve mai essere riutilizzato** con la stessa chiave → altrimenti il cifrario è compromesso.
    
- Necessita di sistemi AEAD (es. ChaCha20-Poly1305) per autenticazione e integrità.
    

---

**Esempi di stream cipher:**

- **RC4** (storico, oggi considerato insicuro)
    
- **[[ChaCha20]]** (moderno e sicuro)
    
- **Salsa20** (precursore di ChaCha20)
    

---

**In breve:**

> **Stream cipher** = cifratura **bit/byte per bit/byte**, molto veloce e leggera,  
> garantisce **confidenzialità**, ma per sicurezza completa va combinata con **[[MAC]] o AEAD**.