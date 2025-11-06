### **Ciphertext-only attack (COA)**

> Un **attacco in cui l’avversario ha accesso solo ai ciphertext** (i messaggi cifrati), senza poter ottenere plaintext corrispondenti né poter inviare plaintext scelti al sistema.  
> L’obiettivo è **recuperare il plaintext** o, meglio, **ricavare la chiave** usata per cifrare, usando soltanto l’analisi dei ciphertext disponibili.

---

### **Caratteristiche principali**

- **Informazione disponibile all’attaccante:** solo ( C = E_k(M) ) (uno o più ciphertext).
    
- **Nessun accesso** a oracle di cifratura/decifratura: né chosen-plaintext né chosen-ciphertext.
    
- **Difficoltà:** è il modello d’attacco **più debole** (meno privilegiato) per l’attaccante; se una cifra è sicura contro COA è già abbastanza resistente nella maggior parte dei casi.
    

---

### **Metodi classici ed esempi**

- **Analisi delle frequenze:** per cifrari sostituzione semplici (es. cifrario di Cesare, sostituzione monoalfabetica).
    
- **Pattern analysis / lunghezza dei messaggi / metadati:** utile su formati prevedibili.
    
- **Criptoanalisi statistica:** attacchi su cifrari storici (Vigenère, Hill) sfruttano ridondanza linguistica.
    
- **Attacchi pratici moderni:** raramente efficaci su algoritmi moderni (AES, ChaCha20) se implementati correttamente; però possono sfruttare **errori di protocollo** (es. riuso di nonce/IV in stream/CTR), compressione + cifratura, o informazioni laterali esposte.
    

---

### **Quando è praticamente efficace**

- Cifrari **deboli** o implementazioni con **errori** (reuse di nonce/IV, chiavi brevi, output prevedibile).
    
- Messaggi con **alta ridondanza** o formati noti (es. header fissi).
    
- Sistemi dove l’attaccante raccoglie un grande corpus di ciphertext per analisi statistica.
    

---

### **Confronto con altri modelli d’attacco**

- **Known-plaintext (KPA):** attaccante conosce alcune coppie ( (M,C) ). Più potente di COA.
    
- **Chosen-plaintext (CPA) / adaptive CPA:** attaccante può far cifrare plaintext scelti — ancora più potente.
    
- **Chosen-ciphertext (CCA):** attaccante può ottenere decifrature di ciphertext scelti — il più potente dei modelli classici.
    

Se un sistema è sicuro contro CCA, è sicuro contro tutti i modelli più deboli (CPA, KPA, COA).

---

### **Contromisure pratiche**

- Usare **algoritmi moderni e standardizzati** (AES-GCM, ChaCha20-Poly1305).
    
- Evitare **reuse di nonce/IV** (critico per CTR/stream ciphers).
    
- Usare **AEAD** o EtM per garantire integrità oltre alla confidenzialità.
    
- Usare **chiavi sufficientemente lunghe** e sicure, con buona gestione e rotazione.
    
- Ridurre ridondanza nei plaintext (padding casuale, salting), evitare formati prevedibili senza protezione.
    
- Monitorare e limitare l’esposizione di ciphertext (logging, mitigazione di esfiltrazione).
    

---

### **In breve**

> Un **ciphertext-only attack** tenta di rompere la cifratura avendo **solo i messaggi cifrati**. È il modello d’attacco più limitato: efficace contro cifrari deboli o implementazioni errate, ma generalmente **inefficace contro algoritmi moderni e protocolli ben progettati**.