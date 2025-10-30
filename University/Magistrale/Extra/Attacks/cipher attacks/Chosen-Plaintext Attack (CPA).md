### **Chosen-Plaintext Attack (CPA)**

> Un attacco in cui l’avversario **può ottenere la cifratura di plaintext a sua scelta** (cioè ha accesso a un _encryption oracle_). Lo scopo è ricavare la chiave o ottenere informazioni che permettano di decrittare altri ciphertext.

---

### **Caratteristiche principali**

- **Accesso dell’attaccante:** può inviare plaintext (M_1, M_2, \dots) a un oracle che restituisce i rispettivi ciphertext (C_i = E_k(M_i)).
    
- **Obiettivo:** trovare vulnerabilità del cifrario o recuperare la chiave (k) o costruire una strategia per decrittare ciphertext non visti.
    
- **Potenza:** più forte del known-plaintext; meno potente del chosen-ciphertext (CCA).
    

---

### **Varianti**

- **Non-adaptive CPA:** l’attaccante sceglie tutti i plaintext in anticipo.
    
- **Adaptive CPA (più comune):** può scegliere plaintext **in base alle risposte precedenti** (interattivo).
    
- **IND-CPA (indistinguishability under CPA):** definizione formale di sicurezza — un cifrario è IND-CPA se un attaccante non riesce a distinguere la cifratura di due messaggi scelti con probabilità significativamente > 1/2, anche avendo accesso all’encryption oracle.
    

---

### **Esempi pratici**

- **RSA “textbook” (deterministico):** dato che è deterministico, inviando lo stesso (M) ottieni sempre lo stesso (C) → vulnerabile a CPA (e triviale a COA).
    
- **Reuse di IV/nonce in modalità CTR/stream cipher:** con un oracle che cifra chosen plaintext, un attaccante può ricavare il keystream e poi decrittare altri messaggi cifrati con lo stesso nonce.
    
- **ECB con oracle di cifratura:** permette di costruire tabelle di mapping blocco→ciphertext e ricostruire plaintext di messaggi strutturati.
    

---

### **Perché conta (ruolo teorico/pratico)**

- La **sicurezza moderna** delle primitive è spesso provata contro CPA (o meglio IND-CPA/IND-CCA).
    
- In contesti reali, se un protocollo espone un servizio che cifra dati scelti dall’attaccante (es. API di cifratura, servizi cloud mal progettati), CPA diventa concreto.
    

---

### **Contromisure e buone pratiche**

- **Cifratura probabilistica / padding randomizzato** (es. RSA-OAEP, randomized IV) per evitare determinismo.
    
- **Usare AEAD** (AES-GCM, ChaCha20-Poly1305): forniscono confidenzialità + integrità e sono progettati per resistere a molti modelli d’attacco.
    
- **Nonce/IV unico e non riutilizzato** per CTR/stream ciphers.
    
- **Non esporre un encryption oracle** a utenti non fidati (limitare API, autenticare richieste).
    
- **Key management** solido: rotazione, scopi separati per chiavi, limitare quantità di dati cifrati con la stessa chiave.
    
- **Prove formali**: scegliere schemi con sicurezza dimostrata (IND-CPA o IND-CCA a seconda del livello richiesto).
    

---

### **In breve**

> Un **CPA** dà all’attaccante il potere di cifrare messaggi scelti con l’obiettivo di rompere la cifratura o ottenere vantaggi per decrittare altri messaggi.  
> Le difese principali sono **cifratura non deterministica**, **nonce/IV corretti**, **AEAD**, e **non esporre oracle di cifratura**.