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

---

Dal libro [[0 CS Lower Level - BOOK - Network Security Private Communication in a Public World.pdf]]
## 3.6 3DES (Multiple Encryption DES)

To fix the 56-bit key problem, the most accepted method was **Triple DES (3DES)**, also known as TDEA (Triple Data Encryption Algorithm). This approach applies the DES cipher three times.

The standard form is **EDE (Encrypt-Decrypt-Encrypt)**:

- **Encryption**: $C = E_{K3}(D_{K2}(E_{K1}(P)))$
    
- **Decryption**: $P = D_{K1}(E_{K2}(D_{K3}(C)))$
    

This uses three independent keys ($K_1, K_2, K_3$), for a total key length of $3 \times 56 = \mathbf{168}$ bits.

---

### 3.6.1 Why Three Encryptions?

- **Encrypting Twice (Same Key)**: $E_K(E_K(P))$. This is **not** more secure. A brute-force attack still only requires $2^{56}$ guesses. It just doubles the work for both the attacker and the user.
    
- **Encrypting Twice (Two Keys - "[[2DES]]", entra nel link per saperne di più)**: $E_{K2}(E_{K1}(P))$. This seems like it should have 112-bit security. However, it is vulnerable to a **Meet-in-the-Middle (MITM) attack**.
    
    - **MITM Attack**: An attacker with a known plaintext-ciphertext pair ($m_1, c_1$) can:
        
        1. Encrypt $m_1$ with all $2^{56}$ possible $K_1$ values and store the results in a giant table: $\langle K_1, \text{result} \rangle$.
            
        2. Decrypt $c_1$ with all $2^{56}$ possible $K_2$ values and look for a match in the first table's results.
            
        3. A match $E_{K1}(m_1) = D_{K2}(c_1)$ reveals a candidate $\langle K_1, K_2 \rangle$ pair.
            
    - **Complexity**: This attack's time complexity is roughly $O(2^{57})$, which is vastly better than the $O(2^{112})$ of a true 112-bit cipher.
        
    - **Limitation**: The attack's main barrier is **memory**. It requires storing $2^{56}$ intermediate values, which is physically impractical (zettabytes of storage).
        
    - Because of this theoretical weakness, 2DES is not considered secure, leading to 3DES.
        

### Effective Security of 3DES

- **3-Key 3DES ($K_1, K_2, K_3$)**: The 168-bit key length is misleading. A similar (but more complex) Meet-in-the-Middle attack can break 3-Key 3DES in $O(2^{112})$ time and $O(2^{56})$ space. Therefore, 3-Key 3DES is only considered to have **112 bits of effective security**.
    
- **2-Key 3DES ($K_1, K_2, K_1$)**: A popular variation used only two keys ($K_1$ and $K_2$), setting $K_3=K_1$. This has a 112-bit key length. However, more advanced cryptanalysis has shown its effective security is only about **80 bits**. For this reason, 3-Key 3DES became the preferred standard.
    

---

### 3.6.2 Why EDE Rather Than EEE?

Why was the middle step a Decryption (D) instead of Encrypt-Encrypt-Encrypt (EEE)?

The reason was backward compatibility with single DES.

If you use an EDE implementation but set all three keys to be the same ($K_1 = K_2 = K_3 = K$):

$C = E_K(D_K(E_K(P)))$

Since $D_K$ is the inverse of $E_K$, the first two operations cancel each other out, leaving:

$C = E_K(P)$

This clever choice allowed hardware and software built for 3DES to also perform standard single DES encryption by simply loading the same key into all three key slots.

---

## 3.7 The Move to AES

By the 1990s, the world needed a new standard.

1. **DES** had an insecure **56-bit key**.
    
2. **3DES** was a secure replacement (at 112-bit strength) but was **very slow** (3x the work).
    
3. Both DES and 3DES suffered from a **small 64-bit block size**. This becomes a security risk (due to the "birthday bound") when encrypting large amounts of data (gigabytes) with the same key, as it can lead to "collisions" that leak information.
    

Because of this, NIST held a public, international competition to find a successor. The winning algorithm, a cipher named **Rijndael**, was standardized as the **Advanced Encryption Standard (AES)**. It features a 128-bit block size and supports 128, 192, and 256-bit keys.