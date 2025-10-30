# **AES-CTR (Advanced Encryption Standard – Counter Mode)**

> È una **modalità di cifratura a blocchi** ([[Block Cipher]]) che trasforma **[[AES]]** in un **cifrario a flusso** ([[Stream Cipher]]), garantendo **[[Confidentiality]]** dei dati.

---

**Come funziona (in sintesi):**
![[Pasted image 20251030133804.png]] *Nota*: nell'immagine il block cipher encryption sarebbe proprio [[AES]].

1. Si genera un **contatore unico ([[Nonce]] + counter)** per ogni blocco.
    
2. Il contatore viene cifrato con [[AES]], dove $k$ è la chiave e $i$ è il blocco i-esimo:    $$\text{Keystream}_i = AES_k(\text{Counter}_i)  $$
3. Il blocco di testo in chiaro viene XORato con il keystream:  $$C_i = P_i \oplus \text{Keystream}_i  $$
4. La decifratura è identica: XOR tra ciphertext e keystream produce il plaintext.
    

---

**Garantisce:**

- ✅ **[[Confidentiality]]** – i dati diventano illeggibili senza la chiave.
    
- ✅ **Parallelizzazione** – cifratura e decifratura possono essere eseguite in parallelo sui blocchi.
    

**Non garantisce:**

- ❌ **[[Integrity]]** o **[[Authenticity]]** – non rileva modifiche al messaggio.
    

---

**Vantaggi principali:**

- Velocità e parallelismo su CPU moderne.
    
- Adatto per messaggi di lunghezza variabile e streaming.
    
- Trasforma [[AES]] in un **cifrario a flusso**.
    

---

**Esempi d’uso:**

- AES-CTR in [[TLS]] e IPsec
    
- Cifratura dati in sistemi cloud o storage
    
- Base per modalità [[AEAD]] come **[[AES-GCM]]**
    

---

**In breve:**

> **AES-CTR** = [[AES]] + [[CTR]] → cifratura **veloce e flessibile** che garantisce **[[Confidentiality]]**,  
> ma per [[Integrity]] e [[Authenticity]] va combinata con **[[HMAC]] o [[AEAD]]**.