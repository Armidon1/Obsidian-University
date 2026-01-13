guardare sempre prima [[CS 6cfu - Domande esame]]
# OTP

Basandomi sugli esami che hai caricato (in particolare 2016, 2022 e 2024) e sulle dispense, ecco la spiegazione di **One-Time Pad (OTP)** strutturata esattamente come serve per superare l'esame.

Il Professore si concentra su 3 aspetti: la definizione matematica di "Cifrario Perfetto", le condizioni per cui OTP lo è, e la dimostrazione matematica del perché il riutilizzo della chiave è catastrofico.

---

### 1. Definizione e Funzionamento

L'OTP è un cifrario a flusso (**Stream Cipher**) di tipo **sincrono**.

- **Funzionamento:** Si esegue lo XOR bit a bit tra il messaggio ($M$) e la chiave ($K$).
    
    - Cifratura: $C = M \oplus K$
        
    - Decifratura: $M = C \oplus K$
        
- **Vernam Cipher:** Negli esami viene spesso chiamato "Vernam Cipher".
    

### 2. OTP come "Cifrario Perfetto" (Shannon)

Questa è una domanda teorica frequente (es. Q1.1 del 2016 e Q4.1 del 2022).

Un cifrario si dice perfetto (Perfect Secrecy) se il testo cifrato non rivela alcuna informazione sul testo in chiaro.

Definizione Matematica (da scrivere all'esame):

La probabilità che il messaggio sia $m$, dato che abbiamo osservato il cifrato $c$, è uguale alla probabilità a priori che il messaggio sia $m$:

$$P(M=m | C=c) = P(M=m)$$

In parole povere: intercettare il messaggio cifrato non mi dà nessun vantaggio statistico per indovinare il messaggio originale.

### 3. Le 3 Regole d'Oro (Condizioni di Validità)

Affinché l'OTP sia matematicamente perfetto, devono valere **tutte e tre** queste condizioni (spesso chiedono "Sotto quali condizioni OTP è perfetto?"):

1. **Randomness:** La chiave $K$ deve essere generata in modo **veramente casuale** (True Random). Un PRNG (Pseudo-Random Number Generator) _non_ basta.
    
2. **Lunghezza:** La lunghezza della chiave deve essere maggiore o uguale a quella del messaggio ($|K| \ge |M|$).
    
3. **One-Time:** La chiave deve essere usata **una sola volta** e poi distrutta.
    

### 4. L'Attacco al "Key Reuse" (Domanda Killer)

Questa è la domanda più ricorrente in assoluto (presente nel 2024, 2022 e nelle dispense).

Domanda: "Perché è pericoloso riutilizzare lo stesso keystream in OTP?" o "Mostra l'attacco".

Risposta da 30 e lode:

Se Alice cifra due messaggi diversi ($M_1$ e $M_2$) usando la stessa chiave $K$, l'attaccante intercetta i due cifrati $C_1$ e $C_2$.

1. $C_1 = M_1 \oplus K$
    
2. $C_2 = M_2 \oplus K$
    

L'attaccante esegue lo XOR tra i due testi cifrati:

$$C_1 \oplus C_2 = (M_1 \oplus K) \oplus (M_2 \oplus K)$$

Per le proprietà commutativa e associativa dello XOR (e poiché $K \oplus K = 0$):

$$C_1 \oplus C_2 = M_1 \oplus M_2 \oplus (K \oplus K) = M_1 \oplus M_2$$

**Conclusione:** La chiave si elide ("cancella"). L'attaccante ottiene lo XOR dei due testi in chiaro ($M_1 \oplus M_2$). Questo rompe la segretezza perfetta perché, tramite analisi statistica e _crib dragging_ (indovinare parole probabili), è banale separare $M_1$ da $M_2$.

### 5. Trappole Vero/Falso (Dagli esami 2017-2018)

Fai attenzione a queste affermazioni nelle tabelle Vero/Falso:

- _"Per qualsiasi keystream possibile, OTP è un cifrario perfetto"_ -> **FALSO**. (Solo se il keystream è _truly random_).
    
- _"OTP è un cifrario a flusso asincrono"_ -> **FALSO**. (È sincrono, il keystream non dipende dal testo cifrato precedente).
    
- _"Un cifrario non può essere perfetto se lo spazio delle chiavi è minore dello spazio dei messaggi"_ -> **VERO**. (È una conseguenza del teorema di Shannon: servono tante chiavi quanti messaggi).
    

### Sintesi per il ripasso

Se ti chiede OTP, scrivi subito: **$C = M \oplus K$**, cita **Shannon** (Perfect Secrecy), elenca le **3 condizioni** (Random, Lunghezza, Uso singolo) e, se richiesto, fai vedere che **$C_1 \oplus C_2 = M_1 \oplus M_2$** se si riusa la chiave.

# RC4

Certamente. Basandomi sulla "Domanda Killer" del **Giugno 2023** e sulle note della tua ultima lezione, ecco la spiegazione di **RC4** strutturata per l'esame.

Il Professore richiede spesso di descrivere **entrambe** le fasi (Inizializzazione e Generazione) e di classificarlo correttamente.

---

### 1. Carta d'Identità (Definizioni da sapere)

- **Tipo:** Cifrario a Flusso (**Stream Cipher**) Sincrono.
    
- **Autore:** Ron Rivest (la "R" di RSA).
    
- **Caratteristica:** Basato su una permutazione casuale di 256 byte. È veloce e semplice da implementare via software.
    
- **Stato:** Deprecato (insicuro), ma studiato per scopi didattici (era usato in WEP e vecchi TLS).
    

---

### 2. L'Algoritmo (La parte da memorizzare)

L'RC4 ha uno "stato interno" composto da un vettore $S$ di 256 byte (una permutazione dei numeri da 0 a 255) e due indici $i$ e $j$.

Il funzionamento si divide in due fasi. Se all'esame ti chiedono "Descrivi RC4", devi scrivere questi due blocchi di pseudocodice.

#### Fase A: KSA (Key Scheduling Algorithm) - Inizializzazione

Qui si mescola il vettore $S$ usando la chiave segreta $K$.

1. **Riempimento:** Inizializza $S$ con l'identità ($S[0]=0, S[1]=1, \dots, S[255]=255$).
    
2. **Mescolamento:**
    
    Plaintext
    
    ```
    j = 0
    per i da 0 a 255:
        j = (j + S[i] + K[i % lunghezza_chiave]) mod 256
        SCAMBIA(S[i], S[j])
    ```
    
    _Nota:_ Il modulo `lunghezza_chiave` serve a ripetere la chiave se è più corta di 256 byte.
    

#### Fase B: PRGA (Pseudo-Random Generation Algorithm) - Generazione

Qui si genera il keystream (un byte alla volta) e lo si cifra con lo XOR. Questo ciclo gira all'infinito (o finché c'è messaggio).

1. Inizializza $i = 0, j = 0$.
    
2. **Ciclo di generazione:**
    
    Plaintext
    
    ```
    i = (i + 1) mod 256
    j = (j + S[i]) mod 256
    SCAMBIA(S[i], S[j])
    
    t = (S[i] + S[j]) mod 256
    k = S[t]   <-- Questo è il byte del Keystream!
    
    Cifrato = Messaggio XOR k
    ```
    

---

### 3. Debolezze (Perché è rotto?)

Spesso chiedono perché non si usa più o quali sono i suoi problemi (citato nelle slide "Biased output").

1. **Bias nei primi byte:** I primi byte del keystream non sono veramente casuali, ma hanno una correlazione statistica con la chiave.
    
    - _Soluzione (non sufficiente):_ Scartare i primi 1024 o 3072 byte del keystream.
        
2. **Disastro WEP:** Il protocollo WEP (WiFi) usava RC4 concatenando un _IV_ (Initialization Vector) pubblico alla chiave segreta ($IV || K$). Poiché l'IV era corto (24 bit), si ripeteva spesso.
    
    - _Conseguenza:_ Riutilizzo del keystream $\rightarrow$ rottura della cifratura (come in OTP).
        

---

### 4. Trappole Vero/Falso (Dagli esami 2017)

Attento a non cadere in questi tranelli trovati nei vecchi compiti:

- _"RC-4 è una modalità operativa (operation mode)"_ -> **FALSO**. (È un algoritmo di cifratura a sé stante, non una modalità come CBC o CTR).
    
- _"RC-4 è un cifrario a blocchi"_ -> **FALSO**. (È uno stream cipher).
    
- _"RC-4 genera una permutazione apparentemente casuale"_ -> **VERO**. (Il cuore dell'algoritmo è proprio mescolare il vettore $S$).
    

### Sintesi per il ripasso

Se esce la domanda aperta su RC4:

1. Scrivi: **Stream Cipher Sincrono**.
    
2. Scrivi lo pseudocodice **KSA** (mescola $S$ con la chiave).
    
3. Scrivi lo pseudocodice **PRGA** (genera il byte $k$ e fai $M \oplus k$).
    
4. Ricorda sempre di scrivere **`mod 256`** e **`SCAMBIA S[i], S[j]`**. Sono i marchi di fabbrica di RC4.

# chacha20 

Certamente. Dato che **ChaCha20** è presente nelle slide del corso e rappresenta lo "standard moderno" (l'erede sicuro di RC4), è molto probabile che possa uscire come domanda di confronto o come alternativa "moderna".

Ecco la scheda di **ChaCha20** strutturata per l'esame, basata sulle note della lezione che hai condiviso.

---

### 1. Carta d'Identità (Definizioni da sapere)

- **Tipo:** Cifrario a Flusso (**Stream Cipher**) Sincrono.
    
- **Autore:** Daniel J. Bernstein (DJB), 2008. È un'evoluzione di _Salsa20_.
    
- **Status:** Standard attuale (RFC 8439). Usato in **TLS 1.3**, WireGuard (VPN), e Android (perché è velocissimo anche senza chip dedicati, a differenza di AES).
    
- **Filosofia:** Sicurezza tramite operazioni semplici (ARX: Add, Rotate, XOR) e diffusione rapida.
    

---

### 2. Lo Stato Interno (La Matrice 4x4)

A differenza di RC4 (che usa un vettore di permutazione $S$), ChaCha20 lavora su una **matrice 4x4** di parole a 32 bit (totale 512 bit).

Se ti chiedono "Come è composto lo stato?", disegna o descrivi questa matrice:

|**Costanti ("expand 32-byte k")**|**Costanti**|**Costanti**|**Costanti**|
|---|---|---|---|
|**Chiave** (256 bit)|**Chiave**|**Chiave**|**Chiave**|
|**Chiave**|**Chiave**|**Chiave**|**Chiave**|
|**Contatore** (32 bit)|**Nonce** (96 bit)|**Nonce**|**Nonce**|

**Elementi chiave:**

1. **Costanti:** Servono per evitare stati "tutti zero".
    
2. **Chiave:** 256 bit (8 parole).
    
3. **Contatore:** Permette di cifrare blocchi diversi senza dipendere da quelli precedenti (accesso casuale/parallelo).
    
4. **Nonce:** Numero usato una sola volta per garantire che messaggi diversi con la stessa chiave abbiano keystream diversi.
    

---

### 3. L'Algoritmo (Quarter-Round e Double-Round)

Il funzionamento si basa sul mescolamento di questa matrice.

#### A. Operazione Base: Quarter-Round (ARX)

Lavora su 4 parole della matrice alla volta. Esegue solo 3 operazioni (molto veloci per la CPU):

1. **A**ddition (Somma modulo $2^{32}$)
    
2. **R**otation (Rotazione bit)
    
3. XOR
    
    Nota esame: Ricorda l'acronimo ARX. Non serve scrivere le equazioni esatte, ma sapere che usa queste tre operazioni per creare confusione e diffusione.
    

#### B. Il Ciclo (20 Round)

L'algoritmo esegue **10 "Double-Rounds"** (totale 20 round, da cui il nome ChaCha**20**).

1. **Column-Round:** Applica il Quarter-Round alle 4 colonne.
    
2. Diagonal-Round: Applica il Quarter-Round alle 4 diagonali.
    
    Obiettivo: Dopo 20 round, ogni bit dello stato iniziale ha influenzato ogni bit dello stato finale (diffusione completa).
    

#### C. Generazione del Keystream (Importante!)

Alla fine dei 20 round, c'è un passaggio cruciale per la sicurezza (che impedisce di risalire alla chiave partendo dal keystream):

1. Prendi lo **Stato Iniziale** (prima del mescolamento).
    
2. Sommalo allo **Stato Finale** (dopo i 20 round).
    
3. Il risultato viene serializzato: ecco il tuo blocco di **Keystream** (64 byte).
    

Cifratura:

$$C = M \oplus \text{Keystream}$$

---

### 4. Confronto per l'Esame: ChaCha20 vs RC4

Questa è una potenziale domanda da 30L per mostrare che hai capito l'evoluzione.

|**Caratteristica**|**RC4 (Vecchio)**|**ChaCha20 (Nuovo)**|
|---|---|---|
|**Struttura**|Permutazione interna ($S$) evolutiva|Matrice 4x4 + Funzione Hash (non invertibile)|
|**Generazione**|Sequenziale (devi calcolare byte $i$ per avere $i+1$)|**Accesso Casuale** (grazie al Contatore, puoi generare subito il blocco 50 senza calcolare i precedenti)|
|**Nonce**|Non gestito nativamente (si usava concatenazione insicura in WEP)|**Nativo** (parte integrante della matrice)|
|**Sicurezza**|Rotto (Bias statistici)|Sicuro (Nessun attacco pratico noto)|
|**Performance**|Veloce sw, lento hw|Veloce ovunque (ARX friendly)|

### Sintesi per il ripasso

Se ti chiedono ChaCha20:

1. Scrivi: **Stream Cipher basato su matrice 4x4**.
    
2. Cita gli ingredienti: **Chiave, Nonce, Contatore**.
    
3. Spiega il core: **ARX** (Add-Rotate-XOR) ripetuto per **20 round**.
    
4. Passaggio chiave: **Somma finale** stato iniziale + stato finale (irreversibilità).
    
5. Uso: È il sostituto di RC4 in TLS 1.3 perché sicuro e parallelizzabile (grazie al contatore).