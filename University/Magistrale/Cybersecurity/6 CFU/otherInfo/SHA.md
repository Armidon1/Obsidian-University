# **SHA (Secure Hash Algorithm)**

> È una **famiglia di funzioni di hash crittografiche** progettata per garantire **[[Integrity]] e [[Authenticity]] indiretta dei dati**, sviluppata dalla NSA e standardizzata dal NIST.

---

**Caratteristiche principali:**

1. **Deterministica:** lo stesso input produce sempre lo stesso hash.
    
2. **Irreversibile:** non è possibile ricostruire l’input dall’hash.
    
3. **Collision-resistant:** difficile trovare due input diversi con lo stesso hash.
    
4. **Avalanche effect:** anche un singolo bit modificato produce un hash completamente diverso.
    

---

**Varianti comuni:**

- **SHA-1:** 160-bit, ormai considerato insicuro per collisioni.
    
- **SHA-2:** include SHA-224, SHA-256, SHA-384, SHA-512, molto sicuro e ampiamente usato.
    
- **SHA-3:** versione più recente, basata su Keccak, resistente a collisioni e attacchi differenziali.
    

---

**Garantisce:**

- ✅ **[[Integrity]]** – verifica che i dati non siano stati modificati.
    
- ✅ **[[Authenticity]]** se combinato con chiavi segrete (es. [[HMAC]]-SHA).
    

**Non garantisce da solo:**

- ❌ **[[Confidentiality]]** – il contenuto originale rimane pubblico.
    
- ❌ **Protezione contro la modifica attiva** senza chiave segreta.
    

---

**Esempi d’uso:**

- **Verifica integrità dei file e firmware** (SHA-256 checksum).
    
- **Password hashing** combinato con salt (es. [[HMAC]], PBKDF2).
    
- **Firme digitali e certificati X.509** (SHA-256 con RSA o ECDSA).
    
- **Blockchain** (collegamento sicuro dei blocchi tramite hash SHA-256).
    

---

**In breve:**

> **SHA** = funzione di hash sicura e standardizzata,  
> fondamentale per **integrità dei dati, autenticazione e firme digitali**,  
> ma **non protegge la confidenzialità** da sola.

Vedi anche [[4 CS  Lower Level - Data Integrity - MAC, attacks and SHA-1#SHA-1 basics]]