# **MtE (MAC-then-Encrypt)**

> **MAC-then-Encrypt** è uno schema di composizione crittografica in cui si **calcola prima il [[MAC]]** del messaggio in chiaro e **poi si cifra** sia il messaggio sia il suo MAC.

---

### 🔐 **Come funziona (passaggi):**
![[Pasted image 20251022133430.png]]
1. **Autenticazione (MAC):**
    - Si calcola il **MAC** sul messaggio in chiaro ( M ):  $$T = MAC_{k_M}(M)  $$        
2. **Cifratura (Encrypt):**
    - Si cifra l’unione del messaggio e del tag:  $$C = E_{k_E}(M ,|, T)  $$
3. **Invio:**
    - Si invia il ciphertext ( C ).

4. **Alla ricezione:**
    - Il destinatario **decifra** ( $C$ ) → ottiene ( $M$ ) e ( $T$ ).
    - Ricalcola ( $MAC_{k_M}(M)$ ) e verifica se coincide con ( T ).
        

---

### ✅ **Vantaggi:**

- Facile da implementare.
    
- Storicamente usato in protocolli come **SSL 3.0** e **[[TLS]] 1.0/1.1**.
    

---

### ⚠️ **Svantaggi e rischi:**

- ❌ Vulnerabile a **padding oracle attacks** e **chosen ciphertext attacks (CCA)**.
    
- ❌ Un errore nella fase di decifratura può rivelare informazioni sul plaintext.
    
- ❌ Non garantisce la separazione tra confidenzialità e autenticità.
    

---

**In breve:**

> **MAC-then-Encrypt (MtE)** = prima autentico, poi cifro.  
> È **meno sicuro** di _Encrypt-then-MAC_, perché può esporre il sistema a **attacchi di [[Integrity]] e [[Confidentiality]]** se non implementato correttamente.