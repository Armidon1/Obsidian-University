# **Hybrid Encryption (Cifratura Ibrida)**

> **Hybrid Encryption** è un metodo di cifratura che **combina** la **[[Asymmetric Encryption]]** (a chiave pubblica) e la **[[Symmetric Encryption]]** (a chiave segreta) per sfruttare i vantaggi di entrambe.

---

### 🔹 **Idea principale:**

- La **crittografia asimmetrica** è **sicura ma lenta**.
    
- La **crittografia simmetrica** è **veloce ma richiede una chiave condivisa**.
    

💡 Quindi, l’idea è:

> Usare la **cifratura asimmetrica** solo per proteggere la chiave simmetrica,  
> e poi usare quella chiave per cifrare i dati veri e propri.

---

### 🔸 **Schema tipico:**

1. **Generazione chiave simmetrica:**  
    Il mittente genera una chiave simmetrica casuale ( K_s ).
    
2. **Cifratura del messaggio:**  
    Il messaggio ( M ) viene cifrato con un algoritmo simmetrico (es. AES):  
    [  
    C_M = \text{Enc}_{K_s}(M)  
    ]
    
3. **Cifratura della chiave simmetrica:**  
    ( K_s ) viene cifrata con la chiave pubblica del destinatario ( K_{pub} ):  
    [  
    C_K = \text{Enc}_{K_{pub}}(K_s)  
    ]
    
4. **Invio:**  
    Il mittente invia ( (C_K, C_M) ).
    
5. **Decifratura:**
    
    - Il destinatario usa la sua chiave privata ( K_{priv} ) per decifrare ( K_s ).
        
    - Poi usa ( K_s ) per decifrare il messaggio.
        

---

### 🔐 **Esempio pratico (semplificato):**

- Cifratura della chiave: RSA
    
- Cifratura del messaggio: AES
    

Questo è **esattamente** come funziona **TLS**, **PGP**, e molte altre tecnologie moderne.

---

### ✅ **Vantaggi:**

- Sicurezza elevata (grazie alla crittografia asimmetrica).
    
- Efficienza (dati cifrati con algoritmo simmetrico, molto più veloce).
    
- Scalabilità e facilità di distribuzione delle chiavi.
    

---

### ⚠️ **Svantaggi:**

- Implementazione più complessa.
    
- Se la chiave privata viene compromessa, anche la chiave simmetrica può essere decifrata.
    

---

### **In breve:**

> **Hybrid encryption** = usa **crittografia asimmetrica** per proteggere la **chiave simmetrica**,  
> e **crittografia simmetrica** per proteggere i **dati**.  
> 🔒 È la base della sicurezza di **TLS, HTTPS, PGP, Signal, ecc.**