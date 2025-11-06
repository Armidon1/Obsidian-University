### **Known-Plaintext Attack (KPA)**

> Un attacco in cui l’avversario **possiede alcune coppie plaintext–ciphertext** ((M, C)) e le usa per cercare di **recuperare la chiave** o decrittare altri ciphertext sconosciuti.

---

### **Caratteristiche principali**

- **Informazione disponibile all’attaccante:** alcune coppie ((M_i, C_i = E_k(M_i))).
    
- **Obiettivo:** scoprire (k) o ottenere una tecnica/offset che permetta di decrittare altri ciphertext cifrati con la stessa chiave.
    
- **Potenza:** più potente del ciphertext-only attack (COA), meno potente del chosen-plaintext attack (CPA) dove l’attaccante può scegliere i plaintext.
    

---

### **Metodi e scenari tipici**

- **Analisi delle relazioni algebraiche** tra (M) e (C) per debolezze del cifrario.
    
- **Exploits pratici:** recupero di chiavi in cifrari storici (es. crittoanalisi dell’Enigma) o attacchi su cifrari con strutture prevedibili.
    
- **Two-time pad / reuse di keystream in stream ciphers:** se lo stesso keystream è riutilizzato su (M_1) e (M_2), conoscendo (M_1) si ricava il keystream e quindi si può decrittare (M_2).
    
- **Attacchi su protocolli:** header noti, formati fissi o messaggi ripetitivi forniscono plaintext noti/utili per l’analisi.
    

---

### **Esempi storici e moderni**

- **Enigma (WWII):** cattura di messaggi noti e uso di crib (sequenze note) per ridurre lo spazio delle chiavi.
    
- **Two-time pad:** se la stessa pad è riutilizzata, conoscere un plaintext permette di svelare gli altri.
    
- **Attacchi pratici:** sfruttamento di plaintext predicibili (es. intestazioni, formati) per attaccare cifrature mal implementate.
    

---

### **Relazione con altri modelli**

- **COA (ciphertext-only):** attaccante ha meno informazioni — KPA è più forte.
    
- **CPA (chosen-plaintext):** attaccante può scegliere plaintext da cifrare — più potente di KPA.
    
- **CCA (chosen-ciphertext):** ancora più potente (può ottenere decifrature su ciphertext scelti).
    
- Un sistema sicuro contro CPA/CCA è automaticamente sicuro contro KPA/COA.
    

---

### **Contromisure pratiche**

- Usare **algoritmi moderni e standardizzati** (AES, ChaCha20) e **modalità AEAD** (AES-GCM, ChaCha20-Poly1305).
    
- **Non riusare nonce/IV/keystream**; garantire nonce unico e, quando richiesto, imprevedibile.
    
- Evitare plaintext prevedibili: **padding casuale**, dissociazione di header sensibili o autenticazione dei metadati.
    
- **Key management** solido: rotazione delle chiavi, limitare la quantità di dati cifrati con la stessa chiave.
    
- Implementare **rate limiting e logging** per ridurre esposizione di coppie ((M,C)).
    

---

### **In breve**

> In un **KPA** l’attaccante conosce alcuni plaintext e i corrispondenti ciphertext e sfrutta queste coppie per dedurre la chiave o decrittare altri messaggi. È efficace contro cifrari deboli o implementazioni errate (es. reuse di keystream), ma i moderni schemi ben progettati la rendono impraticabile.