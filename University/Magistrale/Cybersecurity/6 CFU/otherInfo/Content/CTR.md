# **CTR (Counter Mode)**

> È una **modalità di cifratura a blocchi** ([[Block Cipher]]) che trasforma un algoritmo a blocchi (come [[AES]]) in un **[[Stream Cipher]]**, garantendo **[[Confidentiality]]** dei dati.

---

**Come funziona (in sintesi):**
![[Pasted image 20251030133804.png]]

1. Si genera un **contatore (nonce + counter)** unico per ogni blocco.
    
2. Il contatore viene cifrato con l’algoritmo a blocchi:  $$
    \text{Keystream}_i = E_k(\text{Counter}_i)  $$
3. Il blocco di testo in chiaro viene XORato con il keystream:  $$ C_i = P_i \oplus \text{Keystream}_i  $$
4. La decifratura è identica: XOR tra ciphertext e keystream produce il plaintext.


---

**Garantisce:**

- ✅ **[[Confidentiality]]** – i dati diventano illeggibili senza la chiave.
    
- ✅ **Parallelizzazione** – cifratura e decifratura possono essere eseguite in parallelo sui blocchi.
    

**Non garantisce:**

- ❌ **[[Integrity]] o **[[Authenticity]]** – il messaggio può essere modificato senza essere rilevato.
    

---

**Vantaggi principali:**

- Velocità e parallelismo su CPU moderne.
    
- Trasforma un algoritmo a blocchi in un **cifrario a flusso**.
    
- Adatto per messaggi di lunghezza variabile e streaming.
    

---

**Esempi d’uso:**

- AES-CTR in [[TLS]] e IPsec
    
- Cifratura di dati in sistemi cloud o storage
    
- Base di modalità [[AEAD]] come AES-GCM
    

---

**In breve:**

> **CTR** = trasforma un algoritmo [[Block Cipher]] in uno **[[Stream Cipher]]**,  
> garantisce **[[Confidentiality]]** ma richiede [[MAC]]/[[HMAC]] o [[AEAD]] per [[Integrity]] e [[Authenticity]].