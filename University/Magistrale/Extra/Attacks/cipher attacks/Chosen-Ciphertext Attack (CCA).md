### **Chosen-Ciphertext Attack (CCA)**

> Un attacco in cui l’avversario può ottenere **decifrature (o altre risposte) di ciphertext a sua scelta** da un _decryption oracle_; usa queste risposte per ricavare informazioni sulla chiave o per decrittare altri ciphertext.  
> È il **modello d’attacco più potente** tra i classici (più potente di COA, KPA, CPA).

---

### **Varianti principali**

- **Non-adaptive CCA (CCA1)**: l’attaccante può richiedere decifrature di ciphertext scelti _prima_ di ricevere l’obiettivo da rompere.
    
- **Adaptive CCA (CCA2)**: l’attaccante può continuare a richiedere decifrature anche _dopo_ aver visto il ciphertext bersaglio, eccetto che per il ciphertext esatto bersaglio. CCA2 è la definizione standard e la più potente (indistinguibilità sotto CCA, IND-CCA).
    

---

### **Perché è pericoloso (esempi pratici)**

- **Bleichenbacher attack** su RSA PKCS#1 v1.5: un oracle che segnala formati di padding corretti ha permesso di recuperare plaintext RSA.
    
- **Padding oracle attacks (Vaudenay):** errori/messe a confronto delle risposte di decifratura rivelano informazioni utili per ricostruire il plaintext.
    
- **Applicazioni reali:** se un servizio restituisce messaggi d’errore diversi quando la decifratura fallisce, un attaccante può sfruttarli come oracle.
    

---

### **Relazione con altre nozioni**

- Un sistema **IND-CCA** (indistinguibilità sotto chosen-ciphertext) è sicuro contro CCA e quindi anche contro CPA, KPA e COA.
    
- Molti schemi “semplici” (es. RSA plain) **non** sono IND-CCA sicuri; richiedono trasformazioni o protocolli aggiuntivi.
    

---

### **Contromisure e buone pratiche**

- **Usare schemi CCA-secure** o costruzioni che danno sicurezza contro CCA (es. RSA-OAEP sotto opportune ipotesi, KEM-DEM con KEM CCA-secure).
    
- **AEAD / Encrypt-then-MAC (EtM):** usare cifratura autenticata (AES-GCM, ChaCha20-Poly1305) evita la necessità di un decryption oracle separato perché la verifica del MAC/tag viene fatta _prima_ della decifratura.
    
- **Non esporre un decryption oracle:** autenticare e autorizzare richieste, non fornire API che decifrano ciphertext arbitrari per utenti non fidati.
    
- **Messaggi d’errore uniformi e constant-time:** non rivelare via timing o contenuto perché risposte diverse possono funzionare da oracle.
    
- **Validazione lato client/server:** verificare tag/MAC prima di qualsiasi elaborazione del plaintext.
    
- **Prove formali / usare primitive standardizzate:** scegliere primitive con prove IND-CCA o usare trasformazioni note (KEM/DEM, Fujisaki-Okamoto, ecc.).
    
- **Patch note e test:** test contro padding-oracle e fuzzing sulle routine di decrittazione.
    

---

### **In breve**

> Un **CCA** offre all’attaccante un _decryption oracle_ e può essere devastante se il protocollo/implementazione fornisce risposte utili.  
> Difesa: **AEAD / EtM**, non esporre oracle, error handling uniforme, e usare schemi con sicurezza provata IND-CCA.