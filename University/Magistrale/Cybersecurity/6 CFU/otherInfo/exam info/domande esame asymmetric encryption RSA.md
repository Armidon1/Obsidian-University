guardare sempre prima [[CS 6cfu - Domande esame]]

Questa è davvero la parte più sostanziosa ("The meat") del corso. Basandomi sull'analisi di tutti gli esami passati (specialmente 2022-2025) e sulle tue note, ecco la "mappa" di ciò che devi sapere per l'esame su **Crittografia Asimmetrica, RSA, Firme Digitali e AEAD**.

---

### 1. RSA: Teoria e Vulnerabilità (Argomento Top)

Il prof non chiede quasi mai di cifrare un numero a mano (troppo lungo), ma chiede **concetti architetturali**.

- **Matematica di base:**
    
    - Relazione tra $e$ e $d$: Devi sapere che $e \cdot d \equiv 1 \pmod{\phi(n)}$.
        
    - Perché RSA funziona? Teorema di Eulero.
        
    - **Scambio chiavi:** "Cosa succede se scambio chiave pubblica e privata?"
        
        - Se cifri con la Pubblica $\to$ Confidenzialità.
            
        - Se cifri con la Privata $\to$ Firma/Autenticazione/Non-Ripudio.
            
- **Textbook RSA è INSICURO:**
    
    - Devi saper spiegare perché la versione base ($C = M^e \pmod n$) non si usa mai.
        
    - **Malleabilità (Homomorphic Property):** Se ho $C_1 = Enc(M_1)$ e $C_2 = Enc(M_2)$, allora $C_1 \cdot C_2 = Enc(M_1 \cdot M_2)$. Un attaccante può modificare il cifrato per creare un nuovo messaggio valido senza conoscere la chiave.
        
    - **Determinismo:** Senza padding, lo stesso messaggio produce sempre lo stesso cifrato (attacco dizionario possibile).
        
- OAEP (La Soluzione):
    
    *
    
    - Devi sapere che **OAEP** rende RSA probabilistico (grazie al random seed) e sicuro contro attacchi **Chosen-Ciphertext (IND-CCA2)**. Usa una struttura a rete di Feistel.
        

### 2. Diffie-Hellman & MITM (La Domanda da Disegno)

Spesso viene chiesto di disegnare lo schema o l'attacco.

- **Protocollo Base:** Sapere i passaggi: Alice manda $g^a$, Bob manda $g^b$, entrambi calcolano $g^{ab}$.
    
- Man-in-the-Middle (MITM):
    
    *
    
    - **Domanda:** "Descrivi come un attaccante può rompere DH se non c'è autenticazione."
        
    - **Risposta:** L'attaccante si mette in mezzo, concorda una chiave $K_{AT}$ con Alice e una $K_{BT}$ con Bob. Alice e Bob credono di parlare tra loro, ma parlano con l'attaccante.
        
    - **Soluzione:** Usare **Firme Digitali** o Certificati per autenticare i messaggi $g^a$ e $g^b$.
        
- **Forward Secrecy:** Differenza tra DH Statico (chiavi fisse, se rubate decifro tutto il passato) e **Ephemeral DH (DHE)** (chiavi cambiano ogni sessione, se rubate oggi non decifro ieri).
    

### 3. Firme Digitali & Non-Ripudio (Concetto Chiave)

Attenzione alla distinzione tra HMAC e Firma.

- **HMAC vs Firma (Domanda 2025):**
    
    - "Può un HMAC garantire il Non-Ripudio?"
        
    - **NO.** Perché la chiave è condivisa. Se Bob ha la chiave, può aver creato lui stesso il messaggio. Solo la Firma Digitale (chiave privata posseduta da UNO solo) garantisce Non-Ripudio.
        
- **Hash-then-Sign:**
    
    - Perché firmiamo l'hash e non il messaggio?
        
    - 1. Efficienza (RSA è lento su file grandi).
            
    - 2. Sicurezza (previene l'Existential Forgery su RSA puro).
            
- **PKCS#1 v1.5 vs PSS:**
    
    - **v1.5:** Deterministico (Stesso msg $\to$ Stessa firma). Vulnerabile.
        
    - **PSS (Probabilistic Signature Scheme):** Introduce un **Salt** casuale. Stesso msg $\to$ Firma Diversa ogni volta. È lo standard moderno.
        

### 4. AEAD: GCM e Poly1305 (Il Moderno)

Come detto nell'analisi precedente, questo è il trend "pratico".

- **Architettura:** Encrypt-then-MAC è l'unica sicura dimostrabilmente.
    
- **AES-GCM:**
    
    - Velocissimo su Hardware (AES-NI).
        
    - Usa CTR mode + GHASH.
        
    - **Pericolo:** Riuso del Nonce (IV) distrugge la sicurezza.
        
- **ChaCha20-Poly1305:**
    
    - Velocissimo su Software (Mobile/IoT).
        
    - Usa stream cipher + One-Time MAC.
        

### 5. Comandi OpenSSL (Analisi Pratica)

Negli esami 2023-2025 c'è quasi sempre una riga di comando da spiegare.

Esempi da sapere:

- `openssl rsa -in key.pem -pubout -out pub.pem` $\to$ Estrae la chiave pubblica dalla privata.
    
- `openssl enc -aes-256-cbc ...` $\to$ Cifratura simmetrica.
    
- `openssl dgst -sha256 -sign ...` $\to$ Crea una firma digitale dell'hash SHA256.
    

### Riassunto "Cheat Sheet" per l'Esame

|**Concetto**|**Cosa devi sapere/scrivere**|
|---|---|
|**RSA Textbook**|Insicuro. Malleabile ($Enc(A)\cdot Enc(B) = Enc(A \cdot B)$). Deterministico.|
|**RSA OAEP**|Standard sicuro. Probabilistico (Seed). IND-CCA2.|
|**DH Attack**|Man-in-the-Middle (perché manca autenticazione).|
|**Non-Ripudio**|Solo Chiave Privata (Firma). HMAC non basta.|
|**Firma PSS**|Probabilistica (Salt). Migliore della v1.5 (Deterministica).|
|**AEAD**|Encrypt-then-MAC. GCM o ChaCha20-Poly1305.|

Se ti capita la domanda **"Perché HMAC non fornisce non-ripudio?"**, è un rigore a porta vuota: rispondi "Perché la chiave è simmetrica e condivisa, quindi il ricevente potrebbe aver falsificato il messaggio".