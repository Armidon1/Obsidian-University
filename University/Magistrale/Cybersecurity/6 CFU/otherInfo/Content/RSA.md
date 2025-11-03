# **RSA (Rivest–Shamir–Adleman)**

> È un **algoritmo di cifratura asimmetrica** ([[Asymmetric Encryption]]) molto diffuso, sviluppato nel 1977 da Rivest, Shamir e Adleman.  
> Serve sia per **[[Confidentiality]] dei dati** che per **firme digitali e [[Authenticity]]**.

---

## Panoramica dell'Algoritmo RSA e delle sue Applicazioni

L'algoritmo RSA è un sistema di crittografia asimmetrica che si basa sull'uso di una coppia di chiavi: una **chiave pubblica** (che può essere condivisa con tutti) e una **chiave privata** (che deve essere tenuta segreta dal proprietario).

A seconda di quale chiave viene utilizzata per l'operazione iniziale (che chiamiamo genericamente "cifratura"), RSA può essere utilizzato per due scopi principali e distinti:

1. **Cifratura con Chiave Pubblica**: Per garantire **Confidenzialità**.
    
2. **Cifratura con Chiave Privata**: Per garantire **Autenticità** e **[[Non-Repudiation]]** (la base per le firme digitali).
    

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

- **Performance**: La crittografia asimmetrica (RSA) è estremamente lenta (ordini di grandezza più lenta) rispetto alla crittografia simmetrica (come AES).
    
- **Limiti di Dimensione**: RSA opera su blocchi di numeri. Il messaggio (interpretato come un numero) deve essere più piccolo del modulo $N$ (la dimensione della chiave). Non è adatto per file di grandi dimensioni.
    
- **Sicurezza (Determinismo)**: L'RSA "textbook" (la pura formula matematica) è deterministico. Se non si usa un "padding" (uno schema di riempimento), cifrare lo stesso messaggio due volte produce lo stesso testo cifrato, il che è una vulnerabilità di sicurezza.
    
- **Consumo Energetico**: L'intensità computazionale lo rende problematico per dispositivi a bassa potenza (es. "battery draining").
    

### Soluzione: Cifratura Ibrida

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

Questo è l'uso di RSA per autenticazione e non-ripudio.

- **Scenario**: Alice (A) vuole inviare un messaggio (M) a Bob (B) in modo che Bob sia sicuro che provenga da Alice e non sia stato modificato.
    
- **Processo**:
    
    1. Alice "cifra" il messaggio M usando la sua **chiave privata** (solo lei può farlo).
        
    2. Bob (o chiunque altro) riceve il messaggio "cifrato" e usa la **chiave pubblica** di Alice per "decifrarlo".
        
- **Risultato**:
    
    - **Autenticità**: Se la decifratura con la chiave pubblica di Alice funziona e produce un messaggio sensato, Bob sa che deve essere stata Alice a crearlo (poiché solo lei ha la chiave privata).
        
    - **Integrità**: Se il messaggio fosse stato alterato, la decifratura fallirebbe.
        
    - **Nessuna Confidenzialità**: Chiunque può decifrare il messaggio usando la chiave pubblica di Alice.
        

Questo processo è la base del **non-ripudio**.

### Non-Ripudio

Il **non-ripudio** è la proprietà che impedisce al mittente di un messaggio di negare di averlo inviato. Fornisce una prova di origine e integrità che può essere verificata da terze parti (es. un giudice).

- **Differenza con [[HMAC]]**: Un HMAC (un MAC basato su chiave segreta) fornisce autenticazione e integrità, ma _non_ non-ripudio. In un HMAC, Alice e Bob condividono la stessa chiave segreta. Se Bob riceve un messaggio con un HMAC valido, sa che proviene da Alice. Tuttavia, Bob potrebbe aver creato lui stesso quel messaggio (dato che ha la chiave). Un giudice non può determinare chi dei due (che condividevano la chiave) abbia generato il messaggio. Con RSA, solo una persona (il proprietario della chiave privata) può "firmare".
    

### Problema: L'RSA "Textbook" non è ancora una Firma Sicura

Applicare l'RSA "puro" (chiamato "textbook RSA") per le firme ha una grave vulnerabilità chiamata **falsificazione esistenziale (Existential Forgery)**.

- **Notazione**: Sia $U$ la chiave pubblica di Alice e $V$ la sua chiave privata.
    
- **Processo di firma "ingenuo"**: Alice invia la coppia $(M, S)$, dove $S = E_V(M)$ (cifratura di M con chiave privata V).
    
- **Verifica "ingenua"**: Bob controlla se $E_U(S) = M$.
    

**L'attacco (Falsificazione Esistenziale):**

1. Un attaccante, Fran, non cerca di falsificare una firma per un messaggio $M$ specifico.
    
2. Fran sceglie un file binario _casuale_ $R$.
    
3. Fran usa la chiave **pubblica** $U$ di Alice (che tutti conoscono) e calcola $D = E_U(R)$. (Ricorda: in RSA, la cifratura e la decifratura sono la stessa operazione matematica, $x^k \bmod N$).
    
4. Fran invia a Bob la coppia $(D, R)$, sostenendo che sia un messaggio $(M, S)$ firmato da Alice.
    
5. Bob riceve $(D, R)$ ed esegue la verifica: controlla se $E_U(R) = D$.
    
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
    
- **Sicurezza (vs Forgery)**: L'attacco di Fran fallisce. Fran può ancora scegliere $R$ e calcolare $D = E_U(R)$, ma non può trovare un messaggio $M$ tale che $H(M) = D$, perché $H$ è una funzione _one-way_ (non invertibile).
    
- **Efficienza**: Firmare un hash (es. 256 bit) è molto più veloce che firmare un file di gigabyte.
    

_(Nota: L'uso di hash introduce il rischio teorico di collisioni (legato al "birthday bound"), ma l'uso di digest sufficientemente grandi come SHA-256 rende questo attacco impraticabile)._

---

## 3. Debolezze e Attacchi all'RSA "Textbook"

La sicurezza di RSA dipende da implementazioni attente. L'RSA "textbook" (la formula matematica di base) è vulnerabile.

### Attacco 1: Fattorizzare $N$

La sicurezza di RSA si basa sull'ipotesi che sia computazionalmente difficile fattorizzare il modulo $N$ nei suoi due fattori primi, $p$ e $q$.

- Se un attaccante riesce a fattorizzare $N$, può calcolare $\phi(N) = (p-1)(q-1)$ e da lì calcolare facilmente la chiave privata $d$.
    
- **Contromisure**:
    
    - Usare chiavi grandi: $p$ e $q$ devono essere molto grandi (oggi si raccomandano chiavi $N$ di almeno 2048 bit, quindi $p$ e $q$ di ~1024 bit).
        
    - $p$ e $q$ non devono essere troppo vicini tra loro.
        
    - $p-1$ e $q-1$ devono avere fattori primi grandi (per sconfiggere algoritmi di fattorizzazione specializzati come l'algoritmo $p-1$ di Pollard).
        
- **Stato dell'arte**: I "Factoring Challenges" di RSA hanno mostrato che chiavi un tempo considerate sicure (es. 640 bit) sono state fattorizzate (nel 2005).
    
- **Problema Aperto**: Se so fattorizzare $N$, rompo RSA. Ma l'inverso è vero? Se riesco a "rompere" RSA (cioè a calcolare $d$ senza fattorizzare), posso fattorizzare $N$? Questo rimane un problema teorico aperto.
    
- **Caso di Studio (Gpcode Ransomware, 2008)**: Una variante di questo ransomware usava RSA-1024. Kaspersky Labs stimò (teoricamente) che per fattorizzare una singola chiave a 1024 bit sarebbero serviti 15 milioni di computer per un anno. La chiave non fu rotta, dimostrando la forza pratica di RSA-1024 all'epoca.
    

### Attacco 2: Messaggi Facili da Decifrare (Senza Padding)

Se si usa l'RSA "textbook", alcuni messaggi sono problematici:

- **Messaggi $m = 0, 1, N-1$**: Cifrare questi valori spesso restituisce il valore stesso. Ad esempio, $1^e \bmod N = 1$. E $(N-1)^e \bmod N \equiv (-1)^e \bmod N$. Poiché $e$ è quasi sempre dispari, questo risulta $N-1$.
    
- **Messaggi Piccoli e Esponente Piccolo**: Se sia il messaggio $m$ che l'esponente pubblico $e$ sono piccoli (es. $e=3$), è possibile che $m^e < N$.
    
    - In questo caso, l'operazione $c = m^e \bmod N$ si riduce a $c = m^e$.
        
    - L'attaccante può semplicemente calcolare la radice $e$-esima aritmetica di $c$ (un'operazione facile) per trovare $m$.
        

### Attacco 3: Esponente Pubblico Piccolo (es. $e=3$)

Un esponente pubblico piccolo come $e=3$ è molto efficiente per la cifratura/verifica, ma può essere pericoloso.

- Se un avversario intercetta due cifrature di messaggi correlati, ad esempio $c_1 = m^3 \bmod n$ e $c_2 = (m+1)^3 \bmod n$, esistono tecniche algebriche per ricavare $m$ direttamente da $c_1$ e $c_2$ senza dover fattorizzare $N$.
    

### Soluzione a tutti questi Attacchi: il Padding

Tutte le debolezze menzionate (determinismo, messaggi piccoli, attacchi con $e=3$) sono risolte non usando l'RSA "textbook", ma implementando **schemi di padding** (riempimento) standardizzati.

Questi schemi (come **OAEP** per la cifratura e **PSS** per la firma) aggiungono dati casuali e strutturati al messaggio _prima_ che venga applicata l'operazione RSA. Questo assicura che:

1. Il messaggio non sia mai "piccolo".
    
2. La cifratura non sia deterministica (cifrare lo stesso messaggio due volte produce risultati diversi).
    
3. Le relazioni algebriche tra messaggi correlati vengano distrutte.
vedi anche [[7 CS - Asymmetric encryption#RSA – the algorithm]]. 