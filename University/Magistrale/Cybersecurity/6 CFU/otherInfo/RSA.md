# **RSA (Rivest–Shamir–Adleman)**

> È un **algoritmo di cifratura asimmetrica** ([[Asymmetric Encryption]]) molto diffuso, sviluppato nel 1977 da Rivest, Shamir e Adleman.  
> Serve sia per **[[Confidentiality]] dei dati** che per **firme digitali e [[Authenticity]]**.

---

## Panoramica dell'Algoritmo RSA e delle sue Applicazioni

L'algoritmo RSA è un sistema di crittografia asimmetrica che si basa sull'uso di una coppia di chiavi: una **chiave pubblica** (che può essere condivisa con tutti) e una **chiave privata** (che deve essere tenuta segreta dal proprietario).

A seconda di quale chiave viene utilizzata per l'operazione iniziale (che chiamiamo genericamente "cifratura"), RSA può essere utilizzato per due scopi principali e distinti:

1. **Cifratura con Chiave Pubblica**: Per garantire **[[Confidentiality]]**.
    
2. **Cifratura con Chiave Privata**: Per garantire **[[Authenticity]]** e **[[Non-Repudiation]]** (la base per le firme digitali).
    

Analizziamo entrambi i casi.

---

## 1. Cifratura con Chiave Pubblica (Obiettivo: Confidenzialità)

Questo è l'uso più intuitivo di RSA.

- **Scenario**: Alice (A) vuole inviare un messaggio segreto (M) a Bob (B).
    
- **Processo**:
    
    1. Alice ottiene la **chiave pubblica** di Bob (che Bob ha reso disponibile a tutti).
        
    2. Alice "cifra" il messaggio M utilizzando la chiave pubblica di Bob.
        
    3. Solo Bob, che possiede la **chiave privata** corrispondente, può "decifrare" il messaggio e leggerlo.
        
- **Risultato**: Si ottiene la **Confidenzialità**. Chiunque può inviare un messaggio segreto a Bob, ma solo Bob può leggerlo.
    

### Problemi di questo approccio

Sebbene efficace per la confidenzialità, questo metodo non è quasi mai usato per cifrare messaggi lunghi per diversi motivi:

- **Performance**: La crittografia asimmetrica (RSA) è estremamente lenta (ordini di grandezza più lenta) rispetto alla [[Symmetric Encryption]] (come [[AES]]).
    
- **Limiti di Dimensione**: RSA opera su blocchi di numeri. Il messaggio (interpretato come un numero) deve essere più piccolo del modulo $N$ (la dimensione della chiave). Non è adatto per file di grandi dimensioni.
    
- **Sicurezza (Determinismo)**: L'RSA "textbook" (la pura formula matematica) è deterministico. Se non si usa un "padding" (uno schema di riempimento), cifrare lo stesso messaggio due volte produce lo stesso testo cifrato, il che è una vulnerabilità di sicurezza.
    
- **Consumo Energetico**: L'intensità computazionale lo rende problematico per dispositivi a bassa potenza (es. "battery draining").
    

### Soluzione: Cifratura Ibrida ([[Hybrid Encryption]])

Per questi motivi, RSA viene quasi sempre usato per la **confidenzialità** in un sistema ibrido, tipicamente per lo **scambio di chiavi**:

1. Alice vuole inviare un file lungo a Bob.
    
2. Alice genera una chiave simmetrica _nuova e casuale_ (es. una chiave AES a 256 bit).
    
3. Alice cifra il file lungo usando AES e questa chiave simmetrica (molto veloce).
    
4. Alice cifra la (piccola) chiave simmetrica usando la **chiave pubblica** di Bob (lento, ma applicato solo a pochi bit).
    
5. Alice invia a Bob il `file cifrato con AES`  + `la chiave AES cifrata con RSA`.
    
6. Bob usa la sua **chiave privata** per decifrare la chiave AES, e poi usa quest'ultima per decifrare il file.
    

**Rischio (Man-in-the-Middle)**: Una nota importante. Se un attaccante (Fran) inganna Alice e le fornisce una _falsa chiave pubblica_ sostenendo che sia di Bob, Alice cifrerà il messaggio (o la chiave simmetrica) con la chiave di Fran. Fran potrà decifrarlo, mentre Bob riceverà solo dati incomprensibili. Questo sottolinea la necessità di _autenticare_ le chiavi pubbliche (es. tramite certificati).

---

## 2. Cifratura con Chiave Privata (Obiettivo: Firma Digitale)

Questo è l'uso di RSA per [[Authentication]] e [[Non-Repudiation]].

- **Scenario**: Alice (A) vuole inviare un messaggio (M) a Bob (B) in modo che Bob sia sicuro che provenga da Alice e non sia stato modificato.
    
- **Processo**:
    
    1. Alice "cifra" il messaggio M usando la sua **chiave privata** (solo lei può farlo).
        
    2. Bob (o chiunque altro) riceve il messaggio "cifrato" e usa la **chiave pubblica** di Alice per "decifrarlo".
        
- **Risultato**:
    
    - **[[Authenticity]]**: Se la decifratura con la chiave pubblica di Alice funziona e produce un messaggio sensato, Bob sa che deve essere stata Alice a crearlo (poiché solo lei ha la chiave privata).
        
    - **[[Integrity]]**: Se il messaggio fosse stato alterato, la decifratura fallirebbe.
        
    - **Nessuna [[Confidentiality]]**: Chiunque può decifrare il messaggio usando la chiave pubblica di Alice.
        

Questo processo è la base del **[[Non-Repudiation]]**.

### Non-Ripudio

Il **non-ripudio** è la proprietà che impedisce al mittente di un messaggio di negare di averlo inviato. Fornisce una prova di origine e integrità che può essere verificata da terze parti (es. un giudice).

- **Differenza con [[HMAC]]**: Un HMAC (un MAC basato su chiave segreta) fornisce autenticazione e integrità, ma _non_ non-ripudio. In un HMAC, Alice e Bob condividono la stessa chiave segreta. Se Bob riceve un messaggio con un HMAC valido, sa che proviene da Alice. Tuttavia, Bob potrebbe aver creato lui stesso quel messaggio (dato che ha la chiave). Un giudice non può determinare chi dei due (che condividevano la chiave) abbia generato il messaggio. Con RSA, solo una persona (il proprietario della chiave privata) può "firmare".
    

### Problema: L'RSA "Textbook" non è ancora una Firma Sicura

Applicare l'RSA "puro" (chiamato "textbook RSA") per le firme ha una grave vulnerabilità chiamata **falsificazione esistenziale ([[Existential Forgery (E)]])**.

- **Notazione**: Sia $U$ la chiave pubblica di Alice e $V$ la sua chiave privata.
    
- **Processo di firma "ingenuo"**: Alice invia la coppia $(M, S)$, dove $S = E_V(M)$ (cifratura di M con chiave privata V).
    
- **Verifica "ingenua"**: Bob controlla se $E_U(S) = M$.
    

**L'attacco (Falsificazione Esistenziale):**

1. Un attaccante, Fran, non cerca di falsificare una firma per un messaggio $M$ specifico.
    
2. Fran sceglie un file binario _casuale_ $R$, sostenendolo come firma digitale di Alice.
    
3. Fran usa la chiave **pubblica** $U$ di Alice (che tutti conoscono) e calcola $D = E_U(R)$. (Ricorda: in RSA, la cifratura e la decifratura sono la stessa operazione matematica, $x^k \bmod N$, in questo caso $D=R^e \pmod N$ dove $(e,N)$ formano la chiave pubblica di Alice).
    
4. Fran invia a Bob la coppia $(D, R)$, sostenendo che sia un messaggio $(M, S)$ firmato da Alice.
    
5. Bob riceve $(D, R)$ ed esegue la verifica: controlla se $E_U(R) = D$. Cioè fa la stessa identica operazione che ha fatto Fran per generare D. 
    
6. L'uguaglianza è vera per costruzione! Bob accetta $(D, R)$ come un messaggio $D$ validamente firmato da Alice con la firma $R$.
    
7. Anche se $D$ è un file senza senso (spazzatura), Fran ha creato con successo una coppia (messaggio, firma) valida che Alice non ha mai generato.
    

### Soluzione: La Vera Firma Digitale RSA

Per risolvere questo problema (e per efficienza), **non si firma mai l'intero messaggio**. Si firma un suo **digest** (hash).

- **Processo di Firma (Alice)**:
    
    1. Alice calcola un hash crittografico del messaggio: $h = H(M)$. (Dove $H$ è una funzione come SHA-256, che è una _One-Way Function_ o OWF).
        
    2. Alice "cifra" (firma) solo l'hash con la sua chiave privata: $S = E_V(h) = E_V(H(M))$.
        
    3. Alice invia a Bob la coppia $(M, S)$.
        
- **Processo di Verifica (Bob)**:
    
    1. Bob riceve $(M, S)$.
        
    2. Bob calcola l'hash del messaggio $M$ ricevuto: $h_1 = H(M)$.
        
    3. Bob "decifra" la firma $S$ usando la chiave pubblica $U$ di Alice: $h_2 = E_U(S)$.
        
    4. Bob confronta i due hash:
        
        - Se $h_1 = h_2$, la firma è **accettata**.
            
        - Se $h_1 \neq h_2$, la firma è **rifiutata**.
            

**Perché funziona:**

- **Integrità**: L'hash $H(M)$ garantisce che il messaggio $M$ non sia stato alterato dopo la firma (se lo fosse, $h_1$ sarebbe diverso).
    
- **Autenticità**: La firma $S$ (cifrata con $V$) garantisce che provenga da Alice (altrimenti $h_2$ non corrisponderebbe).
    
- **Non-Ripudio**: Si ottiene solo se la verifica ha successo.
    
- **Sicurezza (vs Forgery)**: L'attacco di Fran fallisce. Fran può ancora scegliere $R$ e calcolare $D = E_U(R)$, ma non può trovare un messaggio $M$ tale che $H(M) = D$, perché $H$ è una funzione _one-way_ (non invertibile). Proprio perché introduco un qualcosa che non è invertibile, per funzionare è strettamente necessario avere $M$ per produrre il digest $h_1$ che verrà poi criptato con la chiave pubblica.
    
- **Efficienza**: Firmare un hash (es. 256 bit) è molto più veloce che firmare un file di gigabyte.
    

_(Nota: L'uso di hash introduce il rischio teorico di collisioni (legato al "birthday bound"), ma l'uso di digest sufficientemente grandi come SHA-256 rende questo attacco impraticabile)._

---

## 3. Debolezze e Attacchi all'RSA "Textbook"

La sicurezza di RSA dipende da implementazioni attente. L'RSA "textbook" (la formula matematica di base) è vulnerabile.

### 1. Fattorizzazione di $N$

- **Attacco:** Se un attaccante può fattorizzare $N$ in $p$ e $q$, può calcolare $\varphi(N)$ e poi usare $e$ per trovare la chiave privata $d$. Fattorizzare $N$ rompe RSA.
    
- **Problema Aperto:** Sappiamo che (Fattorizzare $N$) $\implies$ (Rompere RSA). È vero il contrario? (Rompere RSA) $\implies$ (Fattorizzare $N$)? Non è noto.
    
- **Soluzione:** Usare una corretta generazione della chiave:
    
    - $p$ e $q$ devono essere **sufficientemente grandi** (ad es., $N$ dovrebbe essere di 2048 o 4096 bit).
        
    - $p$ e $q$ **non devono essere troppo vicini** tra loro.
        
    - $(p-1)$ e $(q-1)$ devono avere fattori primi grandi (per sventare l'algoritmo p-1 di Pollard).
        
- **Contesto Storico:** Le sfide di fattorizzazione hanno mostrato la difficoltà. RSA-640 (bit) è stato fattorizzato nel 2005. Nel 2008, il ransomware Gpcode utilizzava una chiave a 1024 bit e Kaspersky Labs stimò che sarebbero stati necessari 15 milioni di computer moderni per 1 anno per romperla. La chiave non è mai stata rotta, dimostrando la forza pratica delle chiavi a 1024 bit all'epoca.
    

---

### 2. Attacchi a Messaggi Semplici o Piccoli

- **Problema 1:** Se $m = 0$, $1$, o $N-1$, allora $RSA(m) = m$. Il testo cifrato è identico al testo in chiaro.
    
    - **Soluzione:** Usare un "salt" o padding (riempimento).
        
- **Problema 2:** Se sia $m$ che $e$ sono piccoli (ad es., $e = 3$) e $m$ è piccolo, potremmo avere $m^e < N$.
    
    - In questo caso, $C = m^e \pmod N = m^e$.
        
    - L'attaccante non ha bisogno di fare aritmetica modulare; calcola semplicemente la radice $e$-esima di $C$ per trovare $m$.
        
    - **Soluzione:** Aggiungere un padding (riempimento) non nullo a _tutti_ i messaggi per assicurarsi che $m$ non sia mai piccolo.
        

---

### 3. Attacchi con Esponente Basso ($e=3$)

- **Problema 1 (Messaggi Correlati):** Se un attaccante intercetta due messaggi correlati da una trasformazione nota, ad es., $c_1 = m^3 \pmod n$ e $c_2 = (m+1)^3 \pmod n$, può usare questa relazione algebrica (l'attacco di Coppersmith) per ricavare $m$.
    
    - **Soluzione:** Scegliere un $e$ grande (come 65537) o usare il padding.
        
- **Problema 2 (Attacco del Teorema Cinese del Resto):** Se lo _stesso messaggio_ $m$ viene inviato a 3 utenti diversi (con $e=3$ e moduli diversi $n_1, n_2, n_3$), un attaccante intercetta:
    
    1. $c_1 = m^3 \pmod{n_1}$
        
    2. $c_2 = m^3 \pmod{n_2}$
        
    3. $c_3 = m^3 \pmod{n_3}$
        
    
    - Usando il Teorema Cinese del Resto (CRT), l'attaccante può combinare questi valori per trovare $m^3 \pmod{n_1n_2n_3}$.
        
    - Dato che $m < n_i$ per ogni $i$, $m^3$ sarà più piccolo del prodotto $n_1n_2n_3$. Il risultato è semplicemente $m^3$.
        
    - L'attaccante calcola la semplice radice cubica e trova $m$.
        
    - **Soluzione:** Aggiungere un padding casuale a ogni messaggio. Questo assicura che lo _stesso_ messaggio non venga mai inviato due volte.
        

---

### 4. Attacco alla Cifratura Deterministica

- **Problema:** L'RSA "da manuale" (textbook) è deterministico. Se un attaccante sa che il messaggio è $m_1$ ("SÌ") o $m_2$ ("NO"), può cifrare sia $m_1$ che $m_2$ con la chiave pubblica. Confronta i risultati con il testo cifrato intercettato per scoprire il messaggio.
    
- **Soluzione:** Aggiungere una stringa casuale (padding) al messaggio.
    

---

### 5. Attacco del Modulo Comune

- **Problema:** Se due utenti sono configurati con lo _stesso modulo $n$_ (ma $e$ e $d$ diversi), è catastrofico.
    
- L'Utente 1 (con $e_1, d_1, n$) potrebbe usare le proprie chiavi per ricavare $p$ e $q$ (è complicato ma possibile).
    
- Una volta ottenuti $p$ e $q$, può calcolare $\varphi(N)$ e usarlo per trovare la chiave privata $d_2$ dell'Utente 2 dalla sua chiave pubblica $e_2$.
    
- **Soluzione:** Ogni persona deve generare il proprio $N$ univoco.

## Altri Attacchi a RSA

Oltre all'attacco base di fattorizzazione, ci sono molti altri modi per attaccare un'implementazione di RSA, specialmente se segue la definizione "da manuale" (textbook) senza un adeguato padding (riempimento).

- **Attacchi di Fattorizzazione:** L'attacco matematico più diretto. Se un attaccante può fattorizzare il modulo $N$ nelle sue componenti prime $p$ e $q$, può calcolare la chiave privata $d$.
    
- **Attacchi con Esponente Basso:** Usare un esponente pubblico piccolo (come $e=3$) può rendere RSA vulnerabile se lo stesso messaggio viene inviato a più destinatari (es. l'attacco broadcast di Håstad) o se il messaggio è piccolo.
    
- **Attacco del Modulo Comune:** Se lo stesso modulo $N$ è usato da utenti diversi (con coppie $(e,d)$ diverse), un utente può potenzialmente usare le proprie conoscenze per fattorizzare $N$ o decifrare messaggi inviati ad altri.
    
- **Attacco del Primo Piccolo:** Se uno dei primi ($p$ o $q$) è troppo piccolo, può essere facilmente trovato per divisione di prova (trial division) o altri metodi di fattorizzazione.
    
- **Attacchi a Canale Laterale (Side-Channel):** Questi attacchi non rompono la matematica ma sfruttano l'implementazione fisica.
    
    - **Attacchi a Tempo (Timing):** Misurando precisamente quanto tempo impiega la decifratura, un attaccante potrebbe essere in grado di dedurre i bit della chiave privata $d$.
        
    - **Attacchi sull'Energia/Potenza:** Misurare il consumo energetico di un dispositivo (come una smart card) durante la decifratura può far trapelare informazioni sulla chiave privata.
        
- **Attacchi a Iniezione di Errore (Fault-Injection):** Causare deliberatamente errori durante il calcolo crittografico (ad es. fluttuando tensione o temperatura) può a volte portare il dispositivo a produrre dati corrotti che rivelano informazioni segrete.
    

---

### Proprietà Moltiplicativa e Malleabilità

In crittografia, si dice che una funzione $f$ ha un omomorfismo moltiplicativo (o è semplicemente moltiplicativa) se:

$$f(m_1 \cdot m_2) \equiv f(m_1) \cdot f(m_2) \pmod n$$

Questo è vero per la cifratura RSA "da manuale":

$$RSA(m_1 \cdot m_2) = (m_1 \cdot m_2)^e \pmod N = (m_1^e \cdot m_2^e) \pmod N = RSA(m_1) \cdot RSA(m_2) \pmod N$$

- Questa proprietà rende RSA **malleabile**. La malleabilità significa che un attaccante può modificare un testo cifrato in un altro testo cifrato valido per un testo in chiaro correlato, senza conoscere nessuno dei due testi in chiaro.
    
- Ad esempio, se un attaccante ha il testo cifrato $C = M^e \pmod N$, può facilmente creare un testo cifrato per $2M$ calcolando $C' = C \cdot 2^e \pmod N$. Il destinatario decifrerà $C'$ come $2M$, potendo essere ingannato nell'accettare un messaggio modificato.
    

---

### Attacchi a RSA: Sfruttare la Malleabilità

La proprietà moltiplicativa può essere generalizzata:

Se $M = M_1 \cdot M_2 \cdot \dots \cdot M_k$, allora:

$$RSA(M) = RSA(M_1) \cdot RSA(M_2) \cdot \dots \cdot RSA(M_k) \pmod N$$

Questo permette a un avversario di costruire testi cifrati per messaggi compositi se conosce i testi cifrati delle loro componenti.

**Soluzione:** Usare sempre uno schema di **padding** sicuro (come OAEP) prima di cifrare. Il padding distrugge questa struttura moltiplicativa, rendendo la cifratura non malleabile.

---

### Esempio di Attacco con Testo Cifrato Scelto (Chosen Ciphertext Attack - CCA)

Un avversario vuole decifrare un testo cifrato target $C = M^e \pmod N$.

1. L'avversario calcola un nuovo testo cifrato $X$ moltiplicando $C$ per la cifratura di un numero scelto (ad es., $2$):
    
    $$X = (C \cdot 2^e) \pmod N$$
    
2. L'avversario invia $X$ alla vittima (o a un oracolo di decifratura) e gli chiede di decifrarlo. La vittima potrebbe essere indotta a farlo se $X$ sembra un messaggio valido diverso.
    
3. La vittima decifra $X$ e restituisce il risultato $Y$:
    
    $$Y = X^d \pmod N = (C \cdot 2^e)^d \pmod N = (C^d \cdot (2^e)^d) \pmod N$$
    
    Dato che $C^d = M$ e $(2^e)^d = 2^{ed} \equiv 2^1 \pmod N$, otteniamo:
    
    $$Y = M \cdot 2 \pmod N$$
    
4. L'avversario ora ha $Y = 2M$. Può facilmente recuperare il messaggio originale $M$ calcolando:
    
    $$M = Y \cdot 2^{-1} \pmod N$$
    
    (dove $2^{-1}$ è l'inverso moltiplicativo modulare di 2 modulo $N$).
    

---

### Attacco con Testo Cifrato Scelto (Generale)

Questa è una versione più generale dell'attacco precedente.

Assumiamo che un attaccante $T$ conosca un testo cifrato target $c = M^e \pmod N$.

1. $T$ sceglie casualmente un valore $X$.
    
2. $T$ calcola un nuovo testo cifrato $c' = c \cdot X^e \pmod N$.
    
3. $T$ chiede all'oracolo di decifratura di decifrare $c'$.
    
4. L'oracolo restituisce il testo in chiaro $M' = (c')^d \pmod N$.
    
5. $T$ può ora calcolare il messaggio originale $M$:
    
    $$M' = (c')^d = (c \cdot X^e)^d = c^d \cdot (X^e)^d = M \cdot X \pmod N$$
    
    Quindi, $M = M' \cdot X^{-1} \pmod N$.
    

**Soluzione:** Il processo di decifratura deve **verificare rigorosamente la struttura** del messaggio decifrato prima di restituirlo. Se viene utilizzato uno schema di padding sicuro (come OAEP), il messaggio decifrato $M'$ avrà molto probabilmente un padding non valido e l'oracolo restituirà un errore invece del testo in chiaro grezzo, sventando l'attacco.

---

### Attacchi all'Implementazione (Side-Channel)

Questi attacchi non rompono la matematica di RSA ma sfruttano le debolezze nel modo in cui è implementato sull'hardware reale.

- **Attacchi a Tempo (Timing):** Il tempo necessario per eseguire l'esponenziazione modulare $C^d \pmod N$ può dipendere dai bit specifici della chiave privata $d$ (ad es., un bit '1' potrebbe richiedere più tempo per essere processato rispetto a un bit '0' a causa di un passo di moltiplicazione extra). Misurando queste minuscole differenze su molte decifrature, un attaccante può recuperare $d$.
    
- **Analisi dell'Energia/Potenza:** Similmente al tempo, la quantità di energia consumata da un processore (come in una smart card) può variare a seconda dell'operazione eseguita. L'Analisi Differenziale della Potenza (DPA) può essere usata per estrarre la chiave.
    
- **Soluzione:** Usare **implementazioni a tempo costante** in cui ogni decifratura richiede la stessa quantità di tempo indipendentemente dalla chiave o dall'input. Un'altra tecnica è il **blinding** (mascheramento), in cui valori casuali vengono introdotti nel calcolo per mascherare gli input effettivi, per poi essere rimossi alla fine.
    

---

## RSA - Conclusione sugli Attacchi

- **L'implementazione "da manuale" di RSA NON è sicura.** Non soddisfa i criteri di sicurezza moderni (come l'indistinguibilità sotto attacco con testo cifrato scelto, IND-CCA).
    
- È vulnerabile a molti attacchi matematici e implementativi a causa della sua natura deterministica e della sua malleabilità.
    
- **Versione Standard:** In pratica, RSA è sempre usato con uno schema di padding. Il messaggio $M$ viene pre-elaborato in un messaggio con padding $M'$ prima della cifratura.
    
    - $C = (M')^e \pmod N$
        
    - Poiché $M'$ contiene dati casuali (dallo schema di padding), la cifratura diventa probabilistica e non malleabile.

Il padding è definito dai PKCS che sono standard da seguire.

### PKCS: Lo Standard per il Padding

**[[PKCS]]** sta per **Public-Key Cryptography Standards** (Standard per la Crittografia a Chiave Pubblica). Si tratta di un insieme di standard sviluppati da RSA Laboratories per garantire l'implementazione sicura e l'interoperabilità della crittografia a chiave pubblica.

|**Standard**|**Titolo**|**Funzione / Descrizione**|
|---|---|---|
|**PKCS #1**|**RSA Cryptography Standard**|Definisce i formati corretti per la **cifratura RSA** e le **firme**, inclusi gli schemi di **padding** cruciali (come OAEP e PSS) necessari per fermare gli attacchi descritti sopra.|
|**PKCS #3**|Diffie-Hellman Key Agreement|Definisce il formato di scambio chiavi DH. (Ora ampiamente obsoleto e sostituito da standard IETF).|
|**PKCS #5**|Password-Based Cryptography|Definisce le funzioni di derivazione della chiave (PBKDF1, PBKDF2) per trasformare le password in chiavi crittografiche.|
|**PKCS #6**|Extended Certificate Syntax|Definisce le estensioni dei certificati. (Obsoleto, sostituito da X.509v3).|

---

### Parte 5: La Soluzione - PKCS (Public-Key Cryptography Standards)

**Conclusione: L'RSA "da manuale" (Textbook) NON è sicuro.**

Per essere sicuro, RSA deve essere usato con uno **schema di padding**. Gli standard per questo sono definiti da **PKCS**.

#### PKCS #1 (Vecchia Versione)

Questo standard definiva uno schema di padding per la cifratura:

`m = 0x00 || 0x02 || [almeno 8 byte casuali non zero] || 0x00 || M`

- **0x00** (primo byte): Assicura che il numero risultante sia $< N$.
    
- **0x02**: Indica la cifratura (0x01 era usato per le firme).
    
- **Byte casuali**: Questo è il padding che risolve la maggior parte delle debolezze di RSA. Rende la cifratura non deterministica e previene attacchi a messaggi piccoli o correlati.

vedi anche [[PKCS]]
vedi anche [[7 CS  Lower Level - Asymmetric encryption#RSA – the algorithm]]. 

