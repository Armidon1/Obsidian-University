# **EaM (Encrypt-and-MAC)**

> **Encrypt-and-MAC** è uno schema di composizione crittografica in cui si **cifra il messaggio** e **si calcola il [[MAC]] separatamente** sul messaggio in chiaro o sul ciphertext.  
> Entrambi — il **ciphertext** e il **tag MAC** — vengono poi inviati insieme.

---

### 🔐 **Come funziona (schema tipico):**
![[Pasted image 20251022133408.png]]
1. **Cifratura (Encrypt):**  $$C = E_{k_E}(M)  $$    
2. **Autenticazione (MAC):**  $$T = MAC_{k_M}(M)  $$  
    oppure, in alcune varianti:    $$T = MAC_{k_M}(C)  $$
3. **Invio:**
    
    - Il mittente invia ( (C, T) ).
        
4. **Alla ricezione:**
    
    - Il destinatario verifica il MAC (ricalcolando ( T )).
        
    - Se è valido, procede a **decifrare** ( C ).
        

---

### ✅ **Vantaggi:**

- Semplice da implementare.
    
- Separazione logica tra **cifratura** e **autenticazione**.
    

---

### ⚠️ **Svantaggi:**

- ❌ La sicurezza **dipende da cosa viene autenticato**:
    
    - Se si fa il MAC sul **messaggio in chiaro**, si perde confidenzialità del tag.
        
    - Se si fa il MAC sul **ciphertext**, è simile a _Encrypt-then-MAC_, ma non sempre ben definito.
        
- ❌ Potenzialmente vulnerabile a **chosen ciphertext attacks** se non gestito correttamente.
	    
---

**In breve:**

> **EaM (Encrypt-and-MAC)** = cifratura e autenticazione eseguite separatamente e poi combinate.  
> È **meno rigoroso** di _Encrypt-then-MAC_ e può essere sicuro **solo se implementato con attenzione**, scegliendo correttamente cosa autenticare (tipicamente il ciphertext).