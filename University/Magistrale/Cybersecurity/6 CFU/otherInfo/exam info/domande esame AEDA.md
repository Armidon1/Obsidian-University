guardare sempre prima [[CS 6cfu - Domande esame]]

Basandomi sulle note che hai incollato e incrociandole con lo stile degli esami analizzati (specialmente quelli recenti che chiedono differenze architetturali e comandi pratici), ecco cosa devi assolutamente sapere su **AEAD (Authenticated Encryption with Associated Data)** per l'esame.

Questo è un argomento "moderno" che il professore usa spesso per distinguere chi ha capito la teoria da chi la applica.

---

### 1. Le Architetture AE (Encrypt-then-MAC è il Re)

Devi saper distinguere i tre approcci e sapere quale è il migliore.

- **Encrypt-then-MAC (EtM):** È l'approccio **sicuro** raccomandato (usato in IPsec e nuovi standard).
    
    - _Funzionamento:_ Prima cifri il messaggio, poi calcoli il MAC sul **testo cifrato**.
        
    - _Perché è il migliore?_ Permette di verificare l'integrità _prima_ di decifrare. Se il MAC è sbagliato, scarti il pacchetto senza sprecare CPU per decifrarlo e senza esporti ad attacchi _Chosen-Ciphertext_.
        
    - _Diagramma mentale:_ Messaggio $\to$ Encrypt $\to$ Ciphertext $\to$ MAC(Ciphertext).
        
- **Encrypt-and-MAC (E&M):** Cifri il messaggio e calcoli il MAC sul _testo in chiaro_ in parallelo. È considerato **insicuro** in pratica (può rivelare informazioni sul plaintext tramite il MAC).
    
- **MAC-then-Encrypt (MtE):** Calcoli il MAC sul chiaro, poi cifri tutto (messaggio + MAC). Usato in vecchi SSL/TLS. Ha avuto problemi storici (es. attacchi Padding Oracle), quindi è meno robusto di EtM.
    

**Domanda d'esame probabile:** "Confronta EtM e MtE. Quale offre la migliore difesa contro attacchi Chosen-Ciphertext e perché?"

---

### 2. AES-GCM (Lo Standard)

Se all'esame leggi "AEAD", il 90% delle volte si parla di GCM.

- **Composizione:** Unisce **CTR Mode** (per la cifratura) + **GHASH** (per l'autenticazione).
    
    - _CTR:_ Permette la **parallelizzazione** (velocità).
        
    - _GHASH:_ È un MAC basato su polinomi nel campo di Galois $GF(2^{128})$.
        
- **Associated Data (AAD):** Devi sapere cosa sono. Sono dati che vengono **autenticati ma non cifrati** (es. l'header IP di un pacchetto). Se modifichi l'AAD, il tag finale cambia e la verifica fallisce.
    
- **Il Tallone d'Achille (IV Reuse):** Questa è la domanda da 30L.
    
    - _Cosa succede se riuso lo stesso IV (Nonce) con la stessa chiave in GCM?_
        
    - **Disastro Totale:** Poiché GCM usa la modalità CTR (che è uno stream cipher), riusare l'IV significa riusare il keystream.
        
    - **Conseguenza 1 (Confidenzialità):** $C_1 \oplus C_2 = P_1 \oplus P_2$ (come nell'OTP).
        
    - **Conseguenza 2 (Integrità):** In GCM, il riutilizzo dell'IV permette all'attaccante di recuperare la chiave di autenticazione interna ($H$) e forgiare tag validi per qualsiasi messaggio.
        

---

### 3. ChaCha20-Poly1305 (L'Alternativa Mobile)

Spesso chiesto come alternativa a AES-GCM.

- **Quando usarlo:** È preferito su dispositivi mobili o CPU senza istruzioni AES hardware (es. vecchi telefoni, IoT), perché è velocissimo via software.
    
- **Poly1305 (Il MAC):**
    
    - È un _One-Time MAC_.
        
    - Usa una chiave $(r, s)$ valida per un solo messaggio.
        
    - Matematica: Valuta un polinomio modulo il numero primo $2^{130}-5$. Ricorda questo numero primo, spesso esce nei quiz.
        
- **Differenza con GCM:** GCM usa aritmetica binaria ($GF(2^{128})$), Poly1305 usa aritmetica modulare su grandi numeri primi ($2^{130}-5$).
    

---

### 4. Checklist per l'Esame (Cosa memorizzare)

1. **Tabella comparativa:**
    
    - **GCM:** Hardware veloce (AES-NI), parallelizzabile, fragile se IV ripetuto.
        
    - **Poly1305:** Software veloce, sicuro, usa numeri primi.
        
2. **Definizione AAD:** Dati autenticati (in chiaro) + Dati cifrati (e autenticati).
    
3. **Matematica GCM:** Moltiplicazione in $GF(2^{128})$ (Carry-less multiplication).
    
4. **Matematica Poly1305:** Modulo $2^{130}-5$ (Numero primo di Mersenne).
    

**Esempio di domanda "Vero o Falso" (basata sui tuoi appunti):**

- "In GCM, l'autenticazione viene calcolata usando un semplice hash SHA-256." -> **FALSO** (Usa GHASH in $GF(2^{128})$).
    
- "L'approccio Encrypt-then-MAC calcola il tag di autenticazione sul testo in chiaro." -> **FALSO** (Sul testo cifrato).
    
- "ChaCha20-Poly1305 deriva una chiave one-time per il MAC a partire dal nonce." -> **VERO**.
    

Studiati bene il diagramma **EtM** (Encrypt-then-MAC) che hai nelle note: è quello che devi disegnare se ti chiedono "Progetta un sistema sicuro per confidenzialità e integrità".