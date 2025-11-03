# **EtM (Encrypt-then-MAC)**

> **Encrypt-then-MAC** è uno **schema di composizione sicuro** usato in crittografia simmetrica per garantire **[[Confidentiality]] + [[Integrity]] + [[Authenticity]]** dei messaggi.

Sebbene sia la pratica più sicura considerando i restanti due ([[MtE]] e [[EaM]]), le migliori strategie sono gli algoritmi [[AEAD]] (come [[AES-GCM]], se si ha il supporto hardware per AES) oppure [[ChaCha20-Poly1305]] (ancora meglio se non si ha il supporto hardware per [[AES]]).

---

### 🔐 **Come funziona (passaggi):**

1. **Cifratura (Encrypt):**
    ![[Pasted image 20251022133248.png]]
    - Si cifra il messaggio con una chiave simmetrica ( $k_E$ ):  $$C = E_{k_E}(M)  $$
2. **Autenticazione (then-MAC):**
    - Si calcola un **MAC (Message Authentication Code)** sul ciphertext usando un’altra chiave ( k_M ):  $$T = MAC_{k_M}(C)$$
3. **Invio:**
    - Si inviano entrambi: ( $(C, T)$ )
        
4. **Verifica alla ricezione:**
    - Il destinatario verifica prima il $MAC ( T )$.
        
    - Solo se il MAC è valido, procede a **decifrare** ($C$).
        

---

### ✅ **Garantisce:**

- **[[Confidentiality]]** → grazie alla cifratura.
    
- **[[Integrity]] & [[Authenticity]]** → grazie al [[MAC]].
    
- **Sicurezza dimostrabile:** protegge da attacchi come _padding oracle_ o _chosen ciphertext attack (CCA)_.
    

---

### ⚠️ **Altri schemi (meno sicuri):**

- **MAC-then-Encrypt ([[MtE]]):** autenticazione prima della cifratura → vulnerabile.
    
- **Encrypt-and-MAC ([[EaM]]):** cifratura e MAC separati → sicurezza dipende dal protocollo.
    

---

### **Esempi reali:**

- Alcune versioni di **IPsec** usano EtM.
    
- Schemi **[[AEAD]]** moderni (come **[[AES-GCM]]**, **[[ChaCha20]]-[[Poly1305]]**) implementano l’equivalente logico di _Encrypt-then-MAC_.
    

---

**In breve:**

> **EtM (Encrypt-then-MAC)** = prima cifro, poi autentico.  
> È lo **schema raccomandato** per garantire **confidenzialità, integrità e autenticità** in modo sicuro.