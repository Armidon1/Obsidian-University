# **CBC-MAC (Cipher Block Chaining – Message Authentication Code)**

> È un **meccanismo di autenticazione dei messaggi ([[MAC]])** basato sulla **modalità [[CBC]]** di un algoritmo di cifratura a blocchi (come [[AES]] o [[3DES]]).  
> Serve a garantire **l’[[Integrity]]** e **l’[[Authenticity]]** dei dati, ma **non la [[Confidentiality]]**.

---

**Come funziona (in sintesi):**

1. Il messaggio è diviso in blocchi ( $P_1, P_2, …, P_n$ ).
    
2. Ogni blocco viene elaborato come in **[[CBC]] encryption**, ma **solo l’ultimo blocco cifrato** viene usato come **[[MAC]]**:  $$C_i = E_k(P_i \oplus C_{i-1})  $$
    con ( $C_0 = IV$ ) (di solito impostato a zero).
    
3. Il **MAC finale** = ( $C_n$ ).
    
4. Il destinatario ricalcola il CBC-MAC sul messaggio ricevuto e confronta il risultato.
    

---

**Garantisce:**

- ✅ **Integrity** – rileva modifiche non autorizzate al messaggio.
    
- ✅ **Authenticity** – solo chi conosce la chiave segreta può produrre un MAC valido.
    

**Non garantisce:**

- ❌ **[[Confidentiality]]** – i dati non sono cifrati.
    
- ❌ **Sicurezza per messaggi di lunghezza variabile**, se non correttamente implementato (può essere manipolato).
    

---

**Varianti più sicure:**

- **[[CMAC]] (Cipher-based MAC):** versione migliorata e standardizzata di CBC-MAC (NIST SP 800-38B).
    
- **XCBC-MAC:** altra estensione sicura per messaggi di lunghezza variabile.
    

---

**Esempi d’uso:**

- Autenticazione in protocolli crittografici simmetrici.
    
- Validazione di dati cifrati o trasmessi in ambienti controllati.
    

---

**In breve:**

> **CBC-MAC** usa la struttura di **CBC** per creare un codice di autenticazione dei messaggi.  
> Garantisce **integrità e autenticità**, ma **non confidenzialità**,  
> e deve essere usato con attenzione — preferibilmente sostituito da **CMAC** o **[[HMAC]]** nelle implementazioni moderne.
> 

Vedi anche [[4 - Data Integrity - MAC, attacks and SHA-1#CBC Mode MACs]]