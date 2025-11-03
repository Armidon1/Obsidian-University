# **DES (Data Encryption Standard)**

> È un **algoritmo di cifratura simmetrica a blocchi**, sviluppato negli anni ’70 e standardizzato dal **NIST nel 1977**, per garantire la **[[Confidentiality]] dei dati elettronici**.  
> È stato per decenni lo **standard di riferimento**, ma oggi è considerato **insicuro** a causa della sua chiave troppo corta.

---

**Come funziona:**
![[Pasted image 20251030105644.png]]

- Opera su **blocchi di 64 bit** di testo in chiaro.
    
- Utilizza una **chiave simmetrica di 56 bit** (più 8 bit di parità).
    
- Applica **16 round** di una struttura chiamata **Feistel network**, che combina:
    
    - Sostituzioni (S-boxes)
        
    - Permutazioni
        
    - Operazioni XOR con sottochiavi derivate dalla chiave principale.
        

**Cifratura e decifratura:**

- Entrambe usano lo stesso algoritmo, con le **sottochiavi applicate in ordine inverso** per la decifratura.
    

---

**Garantisce:**

- ✅ **[[Confidentiality]]** (fino a quando la chiave non è compromessa).
    

**Non garantisce:**

- ❌ **[[Integrity]]** o **[[Authenticity]]**.
    
- ❌ **[[Security]] a lungo termine:** la chiave da 56 bit è troppo corta → vulnerabile a **brute force**.
    
- ❌ **efficiency moderna:** hardware specializzato può romperlo in poche ore o minuti.
    

---

**Attacchi noti:**

- **Brute-force:** provando tutte le 2⁵⁶ chiavi possibili.
    
- **Differential e Linear Cryptanalysis:** analisi statistica per dedurre la chiave.
    

---

**Esempi d’uso (storici):**

- Sistemi bancari e finanziari negli anni ’80–’90.
    
- Standard originali di cifratura dati (FIPS 46).
    
- Base del successivo **[[3DES]]**, che applica DES tre volte per aumentare la sicurezza.
    

---

**In breve:**

> **DES** è stato il **primo standard di cifratura elettronica** diffuso globalmente,  
> ma oggi è **deprecato e insicuro** per via della chiave da 56 bit.  
> È stato **sostituito da [[AES]]** come standard moderno per la cifratura simmetrica.