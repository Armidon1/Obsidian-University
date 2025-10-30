# **Campo di Galois (Galois Field, $GF$)**

> È una **struttura algebrica finita** con un **numero limitato di elementi** in cui è possibile definire **operazioni di somma e moltiplicazione** che soddisfano le proprietà dei campi (associativa, commutativa, esistenza dell’inverso, ecc.).  
> È molto usato in **crittografia**, **codici correttivi** e **teoria dei numeri**.

---

**Caratteristiche principali:**

1. **Numero finito di elementi:** un campo di Galois $GF(pⁿ)$ contiene esattamente ( $p^n$ ) elementi, dove:
    
    - ( $p$ ) è un numero primo (base del campo)
        
    - ( $n$ ) è un intero positivo (estensione del campo)
        
2. **Operazioni chiuse:**
    
    - Somma e moltiplicazione tra elementi del campo producono sempre elementi del campo.
        
3. **Inverso esistente:**
    
    - Ogni elemento diverso da zero ha un **inverso moltiplicativo**.
        
4. **Uso in crittografia:**
    
    - In [[AES-GCM]] e [[Poly1305]], le operazioni su $GF(2¹²⁸)$ permettono di calcolare **tag di autenticazione** in modo efficiente e sicuro.
        

---

**Esempio pratico:**

- $GF(2)$ → campo con 2 elementi {0,1}, con XOR come somma e AND come moltiplicazione.
    
- $GF(2^{128})$ → campo usato in [[AES-GCM]], con 2¹²⁸ elementi, permette di rappresentare blocchi di 128 bit come polinomi.
    

---

**In breve:**

> Un **campo di Galois** è un campo finito in cui si possono fare operazioni matematiche sicure e prevedibili,  
> fondamentale per **autenticazione e cifratura moderna** come [[AES-GCM]] e [[Poly1305]].
