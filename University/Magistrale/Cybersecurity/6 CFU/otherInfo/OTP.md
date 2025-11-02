# **One-Time Pad (OTP)**

> L’**OTP** è uno schema di cifratura **simmetrico bit-wise** ([[Symmetric Encryption]]) in cui il plaintext viene XORato con una chiave **random** lunga quanto il messaggio **e usata una sola volta**.  $$C = P \oplus K \qquad\text{e}\qquad P = C \oplus K$$  

---

### **Proprietà chiave**

- **Perfect secrecy (segretezza perfetta):** dimostrata da Shannon — se la chiave è _veramente casuale_, **lunghezza ≥ messaggio**, usata una sola volta e mantenuta segreta, l’OTP garantisce che il ciphertext non dia alcuna informazione sul plaintext.
    
- **Semplicità:** operazione elementare (XOR).
    
- **Decriptazione triviale** se si possiede la chiave.
    

---

### **Requisiti obbligatori**

1. **Chiave veramente casuale** (non pseudo-random).
    
2. **Lunghezza della chiave ≥ lunghezza del plaintext**.
    
3. **Chiave usata una sola volta** (one-time).
    
4. **Chiave mantenuta perfettamente segreta** e mai riutilizzata né esposta.
    

---

### **Vantaggi**

- Fornisce **segretezza matematica perfetta** se i requisiti sono rispettati.
    
- Impossibile rompere il ciphertext con capacità computazionale illimitata (se i requisiti sono rispettati).
    

---

### **Svantaggi pratici**

- **Distribuzione/gestione della chiave**: generare, trasportare e conservare chiavi lungohe quanto i messaggi è estremamente costoso e poco pratico a scala.
    
- **Necessità di vera casualità:** generatori PRNG non adeguati comprometterebbero la sicurezza.
    
- **Nessuna autenticazione integrata:** l’OTP non fornisce [[Integrity]]/[[Authenticity]]; serve un [[MAC]] o firma separata.
    
- **Catastrofico se riutilizzata (two-time pad):** riuso della stessa chiave su due plaintext ($P_1,P_2)$ dà ($C_1 \oplus C_2 = P_1 \oplus P_2$), da cui si possono ricavare facilmente informazioni — storia ha mostrato rotture semplici con riuso di pad.
    

---

### **Esempio pratico (sintetico)**

- Plaintext (bit): 101100
    
- Key (bit): 011011
    
- Ciphertext = XOR: 110111
    
- Decifrando: 110111 XOR 011011 = 101100 (plaintext)
    

---

### **Uso reale e raccomandazioni**

- Usato storicamente (Vernam cipher, messaggi diplomatici segreti) e in scenari estremi dove la gestione chiavi è possibile (es. comunicazioni diplomatiche point-to-point con scambio fisico di chiavi).
    
- **Nella maggior parte dei casi moderni, OTP è impraticabile**: si preferiscono cipher e protocolli pratici ([[AES-GCM]], [[ChaCha20-Poly1305]]) che offrono eccellente sicurezza e integrità con gestione chiavi molto più efficiente.
    
- Se si necessita di segretezza a lungo termine e si può garantire la gestione delle chiavi, l’OTP rimane l’unico schema con segretezza perfetta formale.
    

---

### **In breve**

> **OTP = XOR tra plaintext e chiave casuale lunga quanto il messaggio, usata una sola volta.**  
> Offre **segretezza perfetta** ma è **praticamente costoso e rischioso** per l’uso generale (soprattutto per la distribuzione/riuso delle chiavi).