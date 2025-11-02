# **RSA (Rivest–Shamir–Adleman)**

> È un **algoritmo di cifratura asimmetrica** ([[Asymmetric Encryption]]) molto diffuso, sviluppato nel 1977 da Rivest, Shamir e Adleman.  
> Serve sia per **[[Confidentiality]] dei dati** che per **firme digitali e [[Authenticity]]**.

---

**Come funziona (in sintesi):**

1. Si genera una **coppia di chiavi:**
    
    - **Chiave pubblica (e, n)** → per cifrare messaggi
        
    - **Chiave privata (d, n)** → per decifrare messaggi
        
2. La sicurezza si basa sulla difficoltà di **fattorizzare numeri grandi** (prodotto di due primi grandi).
    
3. La cifratura (ecco qui se ti vuoi ricordare cosa fa il [[mod operator]]):  $$C = M^e\mod n$$
4. La decifratura:  $$M = C^d \mod n  $$
---

**Garantisce:**

- ✅ **[[Confidentiality]]** – solo chi possiede la chiave privata può decifrare il messaggio cifrato con la chiave pubblica.
    
- ✅ **[[Authenticity]] / [[Non-Repudiation]]** – firmando con la chiave privata, chi riceve può verificare con la chiave pubblica.
    

**Non garantisce da sola:**

- ❌ Efficienza per grandi quantità di dati → di solito si usa per cifrare **chiavi simmetriche** in sistemi ibridi.
    

---

**Esempi d’uso:**

- **[[TLS]] / HTTPS** – scambio sicuro di chiavi
    
- **Firme digitali** – autenticazione e integrità dei documenti
    
- **PGP / GPG** – cifratura e firma di email
    

---

**Vantaggi:**

- Sicuro se la chiave è sufficientemente lunga (2048–4096 bit oggi).
    
- Non richiede scambio segreto di chiavi tra mittente e destinatario.
    

**Svantaggi:**

- Più lento della cifratura simmetrica.
    
- Vulnerabile a chiavi corte o implementazioni scorrette.
    

---

**In breve:**

> **RSA** = algoritmo asimmetrico basato su numeri primi grandi,  
> garantisce **[[Confidentiality]], [[Authenticity]] e [[Non-Repudiation]]**,  
> ed è spesso combinato con cifratura simmetrica ([[Symmetric Encryption]]) per efficienza in sistemi reali.

vedi anche [[7 CS - Asymmetric encryption#RSA – the algorithm]]. 