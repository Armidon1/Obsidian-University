# **3DES (Triple Data Encryption Standard)**

> È un **algoritmo di cifratura simmetrica a blocchi** ([[Symmetric Encryption]] [[Block Cipher]]) che applica **tre volte l’algoritmo [[DES]]** per aumentare la sicurezza del vecchio standard originale.  
> È stato ampiamente usato prima dell’adozione di **[[AES]]**, ma oggi è considerato **obsoleto**.

---

**Come funziona:**

- 3DES esegue **tre operazioni DES** in sequenza, con una o più chiavi:   $$C = E_{k3}(D_{k2}(E_{k1}(P)))$$
    dove:
    - ( $E$ ) = cifratura DES,
        
    - ( $D$) = decifratura DES,
        
    - ( k1, k2, k3 ) = chiavi (da 56 bit ciascuna).
        

**Varianti principali:**

1. **3 chiavi (k1, k2, k3):** sicurezza piena (~112 bit effettivi).
    
2. **2 chiavi (k1, k2, k1):** sicurezza ridotta ma ancora migliore di DES singolo.
    
3. **1 chiave (k1 = k2 = k3):** equivalente a DES → insicuro.
    

---

**Caratteristiche:**

- **Dimensione blocco:** 64 bit
    
- **Dimensione chiave effettiva:** fino a 168 bit (3×56)
    
- **Tipo:** cifratura simmetrica a blocchi
    

---

**Garantisce:**

- ✅ **Confidentiality** (finché la chiave rimane segreta)
    
- ✅ **Compatibilità retroattiva** con DES
    

**Non garantisce:**

- ❌ **Integrità** o **Autenticità** (necessita [[MAC]] o [[HMAC]])
    
- ❌ **Efficienza:** è **lento**, triplica il costo computazionale del DES
    
- ❌ **Sicurezza a lungo termine:** vulnerabile a **attacchi meet-in-the-middle**
    

---

**Esempi d’uso:**

- Sistemi bancari legacy (es. EMV per carte di credito)
    
- VPN e protocolli IPsec in versioni più vecchie
    
- Standard FIPS 46-3 (ormai ritirato dal NIST)
    

---

**In breve:**

> **3DES** = “DES applicato tre volte” → più sicuro di [[DES]] ma **più lento e ormai deprecato**.  
> È stato **sostituito da [[AES]]**, che offre maggiore sicurezza ed efficienza con blocchi da 128 bit.