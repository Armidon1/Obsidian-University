# **Asymmetric Encryption (Cifratura Asimmetrica)**

> È un **metodo di cifratura** in cui vengono utilizzate **due chiavi differenti ma matematicamente correlate**:
> 
> - **Chiave pubblica (public key):** per cifrare i dati
>     
> - **Chiave privata (private key):** per decifrare i dati
>     

---

**Caratteristiche principali:**

1. **Chiavi distinte:** la chiave privata **non deve essere condivisa**, mentre la chiave pubblica può essere distribuita liberamente.
    
2. **Sicurezza basata sulla difficoltà di problemi matematici complessi**, come:
    
    - Fattorizzazione di grandi numeri primi ([[RSA]])
        
    - Problema del logaritmo discreto (DSA, ElGamal)
        
    - Curve ellittiche (ECC)
        
3. **Supporta anche firme digitali**, garantendo autenticità e non-repudiation.
    

---

**Garantisce:**

- ✅ **[[Confidentiality]]** – solo chi possiede la chiave privata può decifrare il messaggio cifrato con la chiave pubblica.
    
- ✅ **[[Authenticity]] / [[Non-Repudiation]]** – chi cifra o firma con la propria chiave privata può essere autenticato.
    

**Non garantisce da sola:**

- ❌ Efficienza per grandi quantità di dati – di solito viene usata **per cifrare chiavi simmetriche** in sistemi ibridi.
    

---

**Esempi:**

- **[[RSA]]** – cifratura e firme digitali
    
- **ElGamal / DSA** – cifratura e firma digitale
    
- **ECC (Elliptic Curve Cryptography)** – chiavi più corte, maggiore efficienza
    

---

**Vantaggi:**

- Non richiede condivisione segreta della chiave.
    
- Permette **scambio sicuro di chiavi simmetriche** in sistemi ibridi.
    
- Supporta firme digitali e autenticazione.
    

**Svantaggi:**

- Più lenta della cifratura simmetrica.
    
- Computazionalmente più pesante su grandi quantità di dati.
    

---

**In breve:**

> **Asymmetric encryption** = cifratura con **coppia di chiavi pubblica/privata**,  
> permette **[[Confidentiality]], [[Authenticity]] e [[Non-Repudiation]]**,  
> ed è spesso combinata con cifratura simmetrica per efficienza.