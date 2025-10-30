# **CBC (Cipher Block Chaining Mode)**

> È una **modalità di funzionamento** per algoritmi di **cifratura a blocchi** (come [[AES]] o 3DES) che migliora la sicurezza rispetto a [[ECB]] introducendo **dipendenza tra i blocchi** tramite un **vettore di inizializzazione (IV)**.

---

**Come funziona:**
![[Pasted image 20251030104756.png]]

1. Il messaggio viene diviso in blocchi ($P_1, P_2, …, P_n$).
    
2. Ogni blocco in chiaro viene **XORato** con il blocco cifrato precedente prima di essere cifrato:  $$C_i = E_k(P_i \oplus C_{i-1})$$
3. Per il primo blocco si usa un **Initialization Vector (IV)** casuale:  $$C_1 = E_k(P_1 \oplus IV)  $$
4. In decifratura si inverte il processo:  ![[Pasted image 20251030104820.png]]$$P_i = D_k(C_i) \oplus C_{i-1}  $$
---

**Garantisce:**

- ✅ **[[Confidentiality]]:** blocchi identici producono cifrati diversi grazie all’IV.
    
- ✅ **Diffusione:** ogni blocco cifrato dipende dal precedente, rendendo più difficile l’analisi statistica.
    

**Non garantisce:**

- ❌ **[[Integrity]]** o **[[Authenticity]]** (un avversario può alterare i blocchi e causare errori prevedibili).
    
- ❌ **Parallelismo:** la cifratura non può essere parallelizzata facilmente (ogni blocco dipende dal precedente).
    

---

**Punti critici:**

- L’**IV deve essere unico e imprevedibile** per ogni sessione.
    
- Se l’IV è riutilizzato o prevedibile → la confidenzialità è compromessa.
    
- Un’alterazione in un blocco cifrato causa la **corruzione del blocco decifrato corrispondente e parziale del successivo** (effetto “error propagation”).
    

---

**Esempi d’uso:**

- Standard storici come SSL/[[TLS]] (nelle versioni precedenti a TLS 1.3).
    
- Cifratura di file o dischi (quando si usa un IV univoco per ogni file o settore).
    

---

**In breve:**

> **CBC** migliora la sicurezza rispetto a **[[ECB]]** introducendo dipendenza tra blocchi tramite un IV,  
> ma **non protegge l’integrità** e **non è adatto ai protocolli moderni** senza un [[MAC]] o un [[HMAC]] di supporto.