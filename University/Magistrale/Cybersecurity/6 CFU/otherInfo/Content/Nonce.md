# **Nonce**

> In crittografia, un **nonce** è un **numero o valore usato una sola volta**, spesso generato casualmente o sequenzialmente, che serve a **rendere univoco un’operazione crittografica**.

---

**Caratteristiche principali:**

1. **Unicità:** deve essere **diverso per ogni sessione o messaggio**.
    
2. **Non segreto:** di solito è trasmesso in chiaro, ma deve essere **non ripetuto**.
    
3. **Scopo principale:**
    
    - Prevenire **riutilizzo del keystream** nei cifrari a flusso (come AES-CTR, ChaCha20).
        
    - Proteggere contro **replay attack** (riuso di messaggi intercettati).
        

---

**Esempi d’uso:**

- AES-CTR / AES-GCM → il nonce combinato con la chiave genera un **keystream unico** per ogni messaggio.
    
- ChaCha20 → il nonce + chiave produce un keystream diverso ogni volta.
    
- Protocollo di autenticazione → nonce nei challenge-response per evitare replay.
    

---

**In breve:**

> Il **nonce** è un “numero usa e getta” che garantisce **unicità e sicurezza** nelle operazioni crittografiche,  
> senza bisogno di mantenerlo segreto.

Se vuoi, posso fare **uno schema visivo semplice** che mostra come AES-GCM o ChaCha20 usano il nonce per generare un keystream unico. Vuoi che lo faccia?