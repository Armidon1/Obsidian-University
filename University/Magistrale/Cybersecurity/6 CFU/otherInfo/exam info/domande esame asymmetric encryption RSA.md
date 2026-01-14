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
	- guarda [[[domande esame asymmetric encryption RSA#approfondimento vulnerabilità|qui]] per saperne di più
		
        
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

# approfondimento vulnerabilità

Questa è un'ottima domanda strategica. Hai in mano degli appunti molto dettagliati e completi, ma per l'esame non tutto ha lo stesso "peso".

In base all'analisi degli esami passati (2012-2025), ecco la **gerarchia di importanza** di ciò che devi studiare. Non devi imparare a memoria ogni singola dimostrazione matematica complessa (come Coppersmith), ma ci sono concetti che devi saper spiegare **e dimostrare** sul foglio.

Ecco cosa è **Obbligatorio** (Must Know) e cosa è **Opzionale** (Nice to Know).

---

### 🚨 1. I "Must Know" (Da sapere a memoria)

Questi concetti escono spessissimo. Se non li sai, perdi punti pesanti.

#### **A. La Malleabilità (Proprietà Moltiplicativa)**

Devi saper **scrivere la formula** che dimostra perché RSA è malleabile. È la prova regina del perché serve il padding.

- **Concetto:** "Se moltiplico i cifrati, ottengo il cifrato del prodotto dei messaggi."
    
- Cosa scrivere all'esame:
    
    $$C_{new} = C_1 \cdot C_2 = (M_1^e) \cdot (M_2^e) = (M_1 \cdot M_2)^e \pmod N$$
    
    Implicazione: Un attaccante può modificare il messaggio cifrato senza decifrarlo.
    

#### **B. Attacco a Testo Cifrato Scelto (CCA - Chosen Ciphertext)**

Questo è l'esempio pratico della malleabilità. Negli appunti hai l'esempio del "$2M$". **Imparalo.**

- **Lo scenario:** L'attaccante vuole decifrare $C$. Crea $C' = C \cdot 2^e$. Fa decifrare $C'$ alla vittima (che ottiene $2M$). L'attaccante divide per 2 e ottiene $M$.
    
- **Perché è importante:** Dimostra che senza padding, RSA è totalmente insicuro contro un attaccante attivo.
    

#### **C. Determinismo**

- **Concetto:** RSA puro non usa numeri casuali. $Enc(M)$ è sempre uguale.
    
- **L'Attacco:** Se indovino che il messaggio è "Sì" o "No", cifro "Sì" e "No" con la pubblica e confronto il risultato con quello intercettato.
    
- **Soluzione Universale:** **OAEP** (Padding). Aggiunge casualità, rendendo il cifrato sempre diverso.
    

---

### 🟠 2. I "Should Know" (Concettuali)

Qui devi capire il _perché_, ma raramente ti chiederanno di scrivere le formule complesse.

#### **A. Low Exponent Attack ($e=3$) - Broadcast**

- **Concetto:** Se mando lo stesso messaggio a 3 persone diverse usando $e=3$, un attaccante usa il **Teorema Cinese del Resto (CRT)** per recuperare il messaggio.
    
- **Livello di dettaglio:** Non devi risolvere il sistema CRT all'esame. Devi solo dire: _"Con $e=3$ e 3 destinatari, si applica CRT per ottenere $M^3$ reale (senza modulo) e si fa la radice cubica."_
    

#### **B. Fattorizzazione**

- **Concetto:** La sicurezza dipende dalla difficoltà di fattorizzare $N$.
    
- **Dettaglio:** Sapere che se $p$ e $q$ sono troppo vicini o troppo piccoli, $N$ si fattorizza facilmente. Non ti chiederanno di fattorizzare numeri a mano.
    

#### **C. Side-Channel Attacks (Timing)**

- **Concetto:** Misurando il tempo di decifratura, capisco se i bit della chiave privata sono 0 o 1.
    
- **Soluzione:** **Blinding**. (Moltiplicare per un numero casuale prima di decifrare, per mascherare il tempo reale).
    

---

### 🟢 3. I "Nice to Know" (Meno probabili)

Questi sono argomenti di nicchia o troppo complessi per un esercizio scritto standard.

- **Coppersmith Attack:** È matematica avanzata sui reticoli. Ti basta sapere che _"Messaggi piccoli con esponente piccolo sono vulnerabili"_. Non imparare la dimostrazione.
    
- **Common Modulus Attack:** È uno scenario di configurazione errata (stesso $N$ per tutti). È utile saperlo come esempio di "cosa non fare", ma è meno critico della Malleabilità.
    

---

### Sintesi Strategica

Se hai poco tempo, concentrati su questo schema **Problema $\to$ Dimostrazione $\to$ Soluzione**:

|**Vulnerabilità**|**Dimostrazione (Da sapere)**|**Soluzione (La Parola Magica)**|
|---|---|---|
|**Malleabilità**|$C_1 \cdot C_2 = (M_1 M_2)^e$|**Padding (OAEP)**|
|**Determinismo**|Guessing Attack (Dizionario)|**Padding (OAEP)**|
|**Low Exponent ($e=3$)**|Broadcast Attack con CRT|Usare $e=65537$ + Padding|
|**Timing Attack**|Analisi tempi esecuzione|**Blinding**|

**Vuoi che proviamo a simulare una domanda d'esame sulla Malleabilità per vedere se riesci a scriverla correttamente?**