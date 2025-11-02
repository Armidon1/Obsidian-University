# **KDF — Key Derivation Function**

> Una **KDF (Key Derivation Function)** è una **funzione crittografica** che serve a **derivare una o più chiavi segrete** a partire da un input iniziale segreto (detto _master key_, _shared secret_ o _password_).

---

### 🧩 **Scopo principale**

Convertire un materiale segreto di base — come una password, una chiave condivisa dopo un handshake o un segreto casuale — in **chiavi derivate** sicure, **indipendenti e imprevedibili** da usare in:

- cifratura ([[AES]], [[ChaCha20]]…)
    
- autenticazione ([[HMAC]], [[AEAD]]…)
    
- sessioni diverse o protocolli multipli.
    

---

### ⚙️ **Funzionamento generale**

Una KDF prende in input:

- un **valore segreto** (es. password o chiave principale),
    
- un **salt** (valore casuale non segreto che evita collisioni e attacchi precomputati),
    
- opzionalmente un **context/info** (identificatore di uso),  
    e produce:   $$\text{DerivedKey} = \text{KDF}(\text{Secret}, \text{Salt}, \text{Info})$$  
    

---

### 🔒 **Proprietà desiderate**

- **Deterministica:** stesso input → stessa chiave.
    
- **Resistente alla preimmagine e collisione:** non si può risalire all’input.
    
- **Output indistinguibile da casuale.**
    
- **Isolamento:** chiavi derivate per scopi diversi non interferiscono tra loro.
    

---

### 💡 **Tipi principali di KDF**

1. **Password-Based KDF (PBKDF):**
    
    - Usa una password come input.
        
    - Aggiunge _salt_ e _iterazioni_ per rallentare brute-force.
        
    - Esempi:
        
        - **PBKDF2** (RFC 8018)
            
        - **bcrypt**
            
        - **scrypt**
            
        - **Argon2** (moderno, resistente a GPU/ASIC).
            
2. **Key-Based KDF:**
    
    - Usa una chiave o segreto condiviso (es. dopo un _Diffie–Hellman_).
        
    - Esempi:
        
        - **HKDF** (HMAC-based KDF, RFC 5869) → standard in TLS 1.3.
            
        - **TLS PRF** (usata nelle vecchie versioni di TLS).
            

---

### 📘 **In breve**

> **KDF = funzione che trasforma un segreto iniziale in una o più chiavi forti, indipendenti e sicure.**  
> Fondamentale per proteggere password, gestire chiavi di sessione e separare usi diversi in protocolli crittografici.