guardare sempre prima [[CS 6cfu - Domande esame]]

La verità è che non ci sono domande di analisi del codice (tipo Netscape o Debian) negli esami scritti. Non perdere tempo a memorizzare quei codici C.

Ecco l'unica tipologia di esercizio "puro" sui PRNG uscita (precisamente nell'esame del **29 Settembre 2017**) e le domande "applicate" che escono sempre.

---

### 1. L'Esercizio "Matematico" (Visto nel 2017)

Questa è l'unica domanda teorica "tosta" sui PRNG trovata nei file.

**Domanda:** Discuti la sicurezza dei seguenti PRNG, considerando sia il caso in cui il seme iniziale $n_0$ è pubblico, sia il caso in cui è segreto. ($H$ è una funzione hash sicura, $X$ è una chiave segreta).

1. $n_{i+1} = H(n_i)$
    
2. $n_{i+1} = H(H(n_i))$
    
3. $n_{i+1} = X \{ n_i \}$ (Cifratura del precedente con chiave $X$)
    
4. $n_{i+1} = H^{(i+1)}(n_0) \{ X \}$
    

Come rispondere per prendere il massimo:

Il trucco è analizzare la prevedibilità (Next-bit test) e la reversibilità (Backward secrecy).

- **Caso A: $n_0$ Pubblico**
    
    - **Risposta:** **INSICURO SEMPRE**. Se il seme è pubblico e l'algoritmo è deterministico (come sono hash e cifrari), chiunque può calcolare l'intera sequenza $n_1, n_2, \dots$. Non c'è nessuna sicurezza.
        
- **Caso B: $n_0$ Segreto (Il vero succo della domanda)**
    
    - **Schema 1: $n_{i+1} = H(n_i)$**
        
        - _Forward Secrecy (Futuro):_ Se scopro $n_i$, posso calcolare facilmente $n_{i+1}$ (basta fare l'hash). Quindi se l'attaccante intercetta un numero, predice tutti i futuri. **Debole**.
            
        - _Backward Secrecy (Passato):_ Se scopro $n_i$, posso trovare $n_{i-1}$? No, perché $H$ è One-Way (non invertibile). Quindi il passato è **Sicuro**.
            
    - **Schema 3: $n_{i+1} = Enc_X(n_i)$ (Cifratura simmetrica)**
        
        - Se scopro $n_i$ e non ho la chiave $X$, non posso calcolare né il futuro (mi serve $X$ per cifrare) né il passato (mi serve $X$ per decifrare).
            
        - È **Molto Sicuro** (purché la chiave $X$ resti segreta). È simile allo standard ANSI X9.17 o CTR_DRBG.
            

---

### 2. Le Domande "Nascoste" sulla Casualità (Molto Frequenti)

Nella maggior parte degli esami recenti (2022-2025), la casualità non è una domanda a sé, ma è la risposta corretta ad altre domande.

Ecco cosa devi scrivere:

#### A. Perché l'IV (Nonce) deve essere casuale/unico?

Domanda presente ovunque (es. Gennaio 2024, Febbraio 2023).

- **Contesto:** Modalità operative stream (CTR, OFB) o GCM.
    
- **Domanda:** "Cosa succede se riuso lo stesso keystream/IV?" o "OFB necessita di un IV random?"
    
- **Risposta da Esame:** L'IV deve essere **unico** (e preferibilmente casuale) per garantire che cifrando due volte lo stesso messaggio con la stessa chiave si ottengano cifrati diversi.
    
    - _Se non è random/unico:_ In OFB/CTR/GCM, riusare l'IV significa riusare il keystream. L'attaccante può fare lo XOR dei cifrati e ottenere lo XOR dei messaggi in chiaro, rompendo la confidenzialità.
        

#### B. A cosa servono i "Salt"?

Trovata in Gennaio 2025.

- **Domanda:** "What is salting? Why use it?"
    
- **Risposta:** Il _Salting_ è l'aggiunta di dati casuali (randomness) a un input.
    
    - _Nelle Password:_ Serve a rendere unico l'hash di password uguali e a sconfiggere le **Rainbow Tables** (tabelle precalcolate).
        
    - _Nelle Firme (PSS):_ Serve a rendere la firma probabilistica. Senza Salt (random), la firma RSA è deterministica e vulnerabile.
        

#### C. Comandi OpenSSL

Se ti chiede di analizzare un comando, spesso c'è l'opzione `-salt` o la generazione di chiavi.

- Sapere che `openssl rand -hex 16` genera 16 byte casuali usando il generatore sicuro del sistema (CSPRNG, solitamente `/dev/urandom`).
    

---

### In sintesi: Cosa studiare per l'esame vero

Non studiare i codici C difettosi. Concentrati solo su:

1. **Analisi logica:** Se il seme è pubblico, il generatore è rotto.
    
2. **Hash chain:** $n_{i+1} = H(n_i)$ protegge il passato (non invertibile) ma espone il futuro se trapela un numero.
    
3. **Applicazione:** La casualità serve per IV, Salt e Chiavi effimere (DHE). Se fallisce la casualità lì, fallisce tutto il protocollo.