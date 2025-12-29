# Autenticazione basata su Password

**Tags:** #engineering #cybersecurity #authentication #passwords #security_protocols

## 1. Fondamenti dell'Autenticazione

L'autenticazione basata su password è il metodo più diffuso e conosciuto. Si basa sul fattore di autenticazione **"What you know"** (Ciò che sai).

Affinché una password sia efficace, deve rispettare due requisiti fondamentali:

- Deve essere **segreta** (conosciuta solo dall'utente).
    
- Deve essere **digitabile** (l'utente deve poterla inserire tramite tastiera).
    

### Il fenomeno del Leet Speak

Gli utenti spesso cercano di rendere le password "complesse" ma facili da ricordare usando il **Leet Speak**.

> [!abstract] Definizione
> 
> Il Leet Speak è un "alfabeto alternativo" nato negli anni '80 sulle BBS, dove le lettere vengono sostituite con caratteri visivamente simili (es. numeri o simboli).

**Esempi di trasformazione Leet Speak:**

|**Testo Standard**|**Leet Speak**|
|---|---|
|hello|`h3110`|
|hacker|`$h4\times0r$`|
|elite|`311t3`|
|password|`p@55w0rd`|

> [!failure] Common Pitfall
> 
> Errore comune: Pensare che il Leet Speak renda una password sicura.
> 
> Realtà: Gli attaccanti conoscono queste sostituzioni. I software di cracking (come John the Ripper o Hashcat) provano automaticamente queste varianti durante gli attacchi a dizionario.

---

## 2. Il Modello dell'Attaccante (Attacker Model)

Per progettare un sistema sicuro, dobbiamo definire formalmente chi è il nostro "nemico". Il modello dell'attaccante analizza tre dimensioni principali:

1. **Conoscenza:** Cosa sa l'attaccante? (Policy delle password, dettagli del sistema, password trapelate).
    
2. **Accesso:** Come interagisce con il sistema?
    
3. **Risorse:** Che potenza di calcolo ha? (CPU, GPU cluster, dizionari).
    

### Tipologie di Attacco e Accesso

È cruciale distinguere tra due modalità di accesso, poiché richiedono difese diverse:

#### A. Attaccante Online

- **Modalità:** Tenta di indovinare la password usando l'interfaccia di login del sistema (es. pagina web).
    
- **Vincoli:** Il sistema può bloccarlo dopo $N$ tentativi errati.
    
- **Difesa:** Lockout (blocco account), CAPTCHA, Rate Limiting, MFA.
    

#### B. Attaccante Offline

- **Modalità:** Ha rubato il database delle password (spesso in forma di hash).
    
- **Vincoli:** Nessuno. Può fare infiniti tentativi sul proprio hardware.
    
- **Difesa:** Funzioni di hash lente (Argon2, bcrypt), password lunghe, Salt.
    

> [!tip] Exam Focus
> 
> Ricorda la differenza:
> 
> - **Online:** Limitato dalla velocità del server e dai controlli di sicurezza.
>     
> - **Offline:** Limitato solo dalla potenza hardware dell'attaccante (GPU).
>     

---

## 3. Classificazione degli Attacchi alle Password

I metodi per compromettere le credenziali si dividono in base all'obiettivo e alla tecnica:

- **Brute Force:** Provare sistematicamente _tutte_ le combinazioni possibili di caratteri.
    
- **Dictionary Attack:** Provare parole comuni prese da un elenco (dizionario), incluse le varianti Leet Speak.
    
- **Credential Stuffing:** Usare coppie `username:password` rubate da un sito (es. LinkedIn) per accedere a un altro sito (es. Amazon), sfruttando il riutilizzo delle password.
    
- **Social Engineering:** Manipolare l'utente per farsi rivelare la password.
    
- **Keylogging:** Malware che registra i tasti premuti.
    

---

## 4. Protocolli di Autenticazione e Sicurezza

Il server non deve mai salvare le password in chiaro (plaintext). Deve memorizzare un segreto derivato o una forma cifrata. Vediamo l'evoluzione dei protocolli per contrastare gli attacchi.

### Protocollo Base (Vulnerabile)

In questo scenario, il server $B$ memorizza l'hash della password dell'utente $A$.

**Definizione matematica del salvataggio su DB:**

$$\text{Server Store} = H(\text{password})$$

_Dove $H$ è una One-Way Function (funzione di hash)._

**Il protocollo di scambio:**

1. $$A \rightarrow B: A$$
    
    (L'utente si presenta)
    
2. $$B \rightarrow A: T$$
    
    (Il server invia $T = \text{timestamp} + \text{nonce}$)
    
3. $$A \rightarrow B: H(H(\text{password}) || T)$$
    

> [!abstract] Math Analysis
> 
> - **Nonce:** Un numero casuale usato una sola volta ("Number used ONCE").
>     
> - **Timestamp:** Impedisce che un vecchio messaggio venga riutilizzato in futuro.
>     
> - **Scopo:** Questo protocollo difende contro il **Replay Attack** (un attaccante non può rispedire il messaggio 3 intercettato perché $T$ cambia ogni volta), ma non protegge il database.
>     

### Il Problema delle Rainbow Tables

Se un attaccante ruba il database contenente solo $H(\text{password})$, può usare le **[[Rainbow Table]]**.

- **Cosa sono:** Tabelle pre-calcolate che associano `password` $\rightarrow$ `hash`.
    
- **Effetto:** L'attacco diventa una semplice ricerca (lookup) istantanea, annullando la proprietà "monodirezionale" dell'hash per password comuni.

>[!Failure] Vulnerabilità
>Se l'[[Adversary]] intercetta T e ruba il database, proverà l'**Attacco a Dizionario (Brute Force on-line)**. Prende una password "pippo", calcola $H(H("pippo")∣∣T_{intercettato}​)$ e vede se corrisponde.


---

## 5. La Soluzione: Il Salt

Per rendere inutili le Rainbow Tables, introduciamo il **[[Salt (Cryptographic)]]**.

> [!abstract] Definizione di Salt
> 
> Una sequenza di bit casuale generata per ogni utente e salvata in chiaro nel database accanto all'hash.

### Protocollo Robusto (con Salt)

**Definizione matematica del salvataggio su DB:**

$$\text{Server Store} = (\text{salt}, \; H(\text{password} \; || \; \text{salt}))$$

**Il protocollo di scambio rivisto:**

1. $$A \rightarrow B: A$$
    
2. $$B \rightarrow A: (\text{salt}, T)$$
    
    (Il server invia il salt specifico dell'utente e il nonce)
    
3. $$A \rightarrow B: H(H(\text{password} \; || \; \text{salt}) \; || \; T)$$
    

> [!abstract] Visual Analysis
> 
> What to look at: Nota come il salt viene inviato dal server al client al passaggio 2.
> 
> Meaning: Il salt non è segreto. Il suo scopo è rendere l'hash unico anche se due utenti hanno la stessa password.
> 
> Risultato: Le Rainbow Tables diventano inutili perché l'attaccante dovrebbe ricalcolarle per ogni possibile valore di Salt (computazionalmente impossibile).

---

## 6. Real World: Password Deboli e Password Manager

Nonostante la teoria, il fattore umano rimane l'anello debole.

### Have I Been Pwned (HIBP)

Siti come _Have I Been Pwned_ raccolgono miliardi di password compromesse da data breach reali.

- **Statistica:** Nel 2025, il database contiene circa **1.29 miliardi** di password uniche compromesse.
    

### Top Password Deboli (NordPass)

Le password più comuni sono incredibilmente prevedibili:

1. `123456`
    
2. `123456789`
    
3. `password`
    
4. `qwerty`
    

> [!example] Professor's Example
> 
> Una password come "dragon" o "monkey" (presenti nella top 20) viene indovinata da un attacco a dizionario in una frazione di secondo, indipendentemente dalla complessità dell'algoritmo di hash.

### Mitigazioni Finali

Per l'utente finale, l'unica difesa contro la propria memoria fallibile è la tecnologia:

- **[[MFA (Multi-Factor Authentication)]]:** Aggiunge un secondo livello di sicurezza (es. codice SMS, app, token hardware).
    
- **Password Manager:** Software che genera e ricorda password casuali lunghe e uniche per ogni sito. L'utente deve ricordare solo la _Master Password_.

---
# Protocolli Avanzati di Autenticazione e Hashing

## 1. Limiti dell'Autenticazione Tradizionale

Quando Alice vuole autenticarsi presso Bob (il server), i metodi base presentano vulnerabilità strutturali critiche:

- **Invio in chiaro (Plaintext):** Espone le credenziali all'intercettazione (_eavesdropping_).
    
- **Diffie-Hellman Semplice:** Se usato per stabilire una chiave con cui cifrare la password, un attaccante (Trudy) può interporsi (_Man-in-the-Middle_), impersonare Bob e decifrare la password.
    
- **Challenge/Response:** Sebbene protegga dal _Replay Attack_, è vulnerabile agli **attacchi a dizionario** se la password è debole (l'attaccante registra lo scambio e prova offline a trovare la password che lo genera).
    

### Obiettivo dei Protocolli Avanzati:

Garantire autenticazione crittografica forte permettendo all'utente di ricordare solo una password, senza dover memorizzare chiavi crittografiche o certificati sulla propria macchina (che potrebbe non essere sicura o configurata).

---

## 2. Lamport's Hash (One-Time Password)

Introdotto nel 1981, questo protocollo utilizza una **catena di hash** per generare password "usa e getta". È la base dei moderni sistemi OTP (S/Key).

### Logica Matematica

Il sistema si basa sull'applicazione ricorsiva di una funzione di hash $H$ per $n$ volte (dove $n$ è un numero grande, es. 1000).

Configurazione Server (Bob):

Bob non salva la password, ma l'hash $n$-esimo:

$$\text{Bob's DB} = \langle \text{username}, n, H^n(\text{password}) \rangle$$

**Procedura di Autenticazione:**

1. **Alice** invia il proprio username.
    
2. **Bob** risponde inviando il contatore attuale $n$.
    
3. **Alice** calcola il token "usa e getta" applicando l'hash $n-1$ volte:
    
    $$x = H^{n-1}(\text{password})$$
    
4. **Alice** invia $x$ a Bob.
    
5. **Bob** verifica la validità applicando l'hash _una sola volta_ al valore ricevuto:
    
    $$\text{Check: } H(x) \stackrel{?}{=} H^n(\text{password})$$
    
    _(Poiché $H(H^{n-1}) = H^n$)_
    
6. Se la verifica ha successo, Bob decrementa il contatore ($n-1$) e sostituisce il vecchio hash con $x$ nel database.
    

> [!abstract] Visual Analysis
> 
> Meaning: La sicurezza risiede nel fatto che la sequenza di trasmissione è inversa rispetto alla generazione ($n-1, n-2, \dots$). Poiché l'hash è una funzione unidirezionale (One-Way), un attaccante che intercetta il token $H^{n-1}$ non può calcolare il token futuro $H^{n-2}$ necessario per il prossimo login.

### Vulnerabilità e Difese Specifiche

- **Attacco a Dizionario:** Senza salt, un attaccante può pre-calcolare le catene di hash per password comuni.
    
    - **Soluzione:** Usare $H^{n-1}(\text{password} || \text{salt})$. Il salt permette anche di usare la stessa password su server diversi generando hash diversi.
        
- **Attacco "Small N":** Un finto server (Trudy) intercetta la richiesta di Alice e le invia un $n'$ molto basso (es. 50 invece di 1000). Alice calcola e invia $H^{50}$. Trudy ora possiede un token valido che può usare contro il vero server (che accetta qualsiasi $k < 1000$) fino a che il contatore non scende sotto 50.
    
    - **Difesa:** La workstation deve mostrare $n$ ad Alice per una verifica umana, oppure usare device personali fidati.
        

---

## 3. Protocollo EKE (Encrypted Key Exchange)

Il protocollo [[EKE (Encrypted Key Exchange)]] risolve un problema fondamentale: come usare uno scambio di chiavi sicuro (Diffie-Hellman) quando l'unico segreto condiviso è una password debole.

Concetto Chiave:

Si esegue uno scambio [[Diffie-Hellman Key Exchange]], ma i messaggi scambiati ($g^a$ e $g^b$) sono cifrati con la password dell'utente.

### Definizione Matematica dello Scambio

Sia $W$ il segreto debole ("weak secret") derivato dalla password: $W = f(\text{password})$, in particolare la $f$ potrebbe essere una qualsiasi funzione di Hashing. La weak secret $W$ è usata come chiave simmetrica. Ecco il protocollo:

1. **Alice $\rightarrow$ Bob:** Sceglie un numero casuale $a$ e invia:
    
    $$\text{Msg 1: } W \{ g^a \mod p \}$$
    
2. **Bob $\rightarrow$ Alice:** Sceglie un numero casuale $b$, genera un challenge $C_1$ e invia:
    
    $$\text{Msg 2: } W \{ g^b \mod p, C_1 \}$$
    
3. Calcolo della Chiave di Sessione $K$:
    
    Entrambi decifrano i messaggi usando $W$ e calcolano la chiave forte $K$:
    
    $$K = g^{ab} \mod p$$
    
4. **Verifica (Challenge/Response cifrato con $K$):**
    
    $$\text{Alice} \rightarrow \text{Bob}: K \{ C_1, C_2 \}$$
    
    $$\text{Bob} \rightarrow \text{Alice}: K \{ C_2 \}$$
    

> [!tip] Exam Focus: Perché EKE è sicuro?
Potresti chiederti: _"Se la password W è debole, un hacker non può intercettare il messaggio e provare tutte le password possibili finché non lo decifra?"_
>
La risposta è **NO**, ed è qui la genialità:
>
>1. L'hacker intercetta il blob cifrato.
  >  
>2. Prova a decifrarlo con la password "pippo". Ottiene un numero casuale X.
 >   
>3. Prova a decifrarlo con la password "password123". Ottiene un numero casuale Y.
  >  
>4. **Il problema per l'hacker:** Sia X che Y sembrano numeri casuali validi!
  >  
   > - Il contenuto cifrato (ga) è un numero casuale.
   >     
  >  - Se decifri con la password sbagliata, ottieni spazzatura (che sembra un numero >casuale).
       > 
    >- Se decifri con la password giusta, ottieni ga (che è un numero casuale).
      >  
>
>L'hacker non ha alcun modo di distinguere se ha trovato la password giusta o no, perché non c'è una struttura riconoscibile (come un'intestazione di file o un testo leggibile) dentro il pacchetto cifrato. È solo matematica randomica nascosta da altra matematica.
> 
> Supponendo anche che il pacchetto decifrato risulti effettivamente uguale a $g^a$, l'attaccante che intercetta i messaggi non ha modo di verificare se quel numero corrisponde davvero a $g^a$ senza risolvere il logaritmo discreto, che è matematicamente intrattabile. Guarda [[Sicurezza del protocollo EXE|qui]] per vedere i dettagli.

---

## 4. Tassonomia degli Attacchi: Online vs Offline

È cruciale distinguere lo scenario di attacco per applicare la difesa corretta.

### Attacchi Online (Guessing)

- **Definizione:** L'attaccante tenta di indovinare la password interagendo col sistema di login "vivo".
    
- **Velocità:** Molto bassa. Limitata dalla latenza di rete e dalle policy del server.
    
- **Rilevamento:** Facile (i log mostrano picchi di login falliti).
    
- **Miglior Difesa:** Account Lockout (blocco dopo 3-5 tentativi), CAPTCHA, Rate Limiting, MFA.
    

### Attacchi Offline (Cracking)

- **Definizione:** L'attaccante ha rubato il database (dump) degli hash e lavora sul proprio hardware.
    
- **Velocità:** Altissima. Limitata solo dalla potenza hardware (GPU/ASIC).
    
- **Rilevamento:** Molto difficile (avviene fuori dal sistema monitorato).
    
- **Miglior Difesa:** Strong Hashing (algoritmi lenti), Salting, Password lunghe.
    

---

## 5. Strong Hashing & KDF (Key Derivation Functions)

Per contrastare il cracking offline (specialmente via GPU), gli algoritmi di hashing devono essere **intenzionalmente lenti e costosi**.

### Proprietà Fondamentali

1. **Salted:** Obbligatorio per prevenire Rainbow Tables.
    
2. **Memory-Hard:** L'algoritmo deve richiedere molta RAM. Questo svantaggia le GPU e gli ASIC (che hanno poca memoria per core o memoria costosa) rispetto alla CPU.
    
3. **Costo Configurabile:** Deve essere possibile aumentare il "fattore di lavoro" (iterazioni/memoria) man mano che l'hardware migliora negli anni.
    

### Confronto Algoritmi di [[KDF (Key Derivation Function)]]

| **Algoritmo**  | **Tipo**          | **Resistenza GPU** | **Note**                                                                                                                                                         |
| -------------- | ----------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **PBKDF2**     | Iterativo (CPU)   | ❌ Bassa            | Standard diffuso ma obsoleto per password critiche. Facilmente parallelizzabile su GPU.                                                                          |
| **[[bcrypt]]** | CPU-bound         | ⚠️ Media           | Standard storico (>25 anni). Ha un fattore di costo regolabile.                                                                                                  |
| **scrypt**     | Memory-hard       | ✅ Alta             | Primo algoritmo progettato per richiedere memoria significativa.                                                                                                 |
| **[[Argon2]]** | **Memory & Time** | ✅✅ Altissima       | **Vincitore della Password Hashing Competition (PHC).** Permette di configurare separatamente memoria, tempo e parallelismo. È lo standard moderno raccomandato. |

> [!failure] Common Pitfall
> 
> Errore: Usare SHA-256 o MD5 per le password.
> 
> Perché: Sono algoritmi progettati per essere veloci. Una GPU moderna può calcolare miliardi di hash SHA-256 al secondo, rendendo banale il brute-force di password complesse.
> 
> Correzione: Usare sempre una KDF (Argon2id o bcrypt).

---
# Protocolli EKE Avanzati e Proprietà di "Augmentation"

## 1. Varianti di EKE (SPEKE e PDM)

Prima di introdurre i protocolli avanzati, analizziamo due varianti storiche del protocollo base EKE (Encrypted Key Exchange).

### SPEKE (Simple Password Exponential Key Exchange)

Invece di usare un generatore $g$ fisso, SPEKE utilizza il segreto derivato dalla password ($W$) come base per lo scambio Diffie-Hellman.

**Logica Matematica:**

$$\text{Scambio: } W^a \pmod p \quad \text{e} \quad W^b \pmod p$$

$$\text{Chiave Sessione: } K = W^{ab} \pmod p$$



### PDM (Password Derived Moduli)

In questa variante, è il modulo $p$ (il numero primo) a dipendere dalla password, mentre il generatore è fisso ($g=2$).

---

## 2. Il Problema di EKE: Perché serve l'Augmentation?

Il protocollo EKE standard ha una vulnerabilità architetturale. Il server (Bob) memorizza un segreto $W$ derivato dalla password dell'utente.

**Le vulnerabilità:**

- Se un attaccante (Trudy) compromette il server e ruba $W$, può impersonare Alice.
    
- Se Trudy ruba il file delle password, può eseguire un attacco a dizionario offline.
    

> [!failure] Common Pitfall
> 
> In EKE base, il server è un "Single Point of Failure". Chi controlla il server (o il suo database) può impersonare qualsiasi utente senza dover craccare la password, perché possiede già il segreto $W$ necessario per lo scambio.

### La Soluzione: Augmentation Property

Per risolvere questo problema, si introduce la proprietà di **Augmentation**.

Definizione:

Un protocollo è "Augmented" se il server non memorizza la password (o un suo equivalente diretto), ma solo un Verifier derivato.

> [!tip] Exam Focus
> 
> Vantaggio Cruciale: Se il database del server viene rubato, l'attaccante NON può impersonare l'utente immediatamente. Deve prima eseguire con successo un attacco a dizionario offline contro il Verifier per trovare la password originale.

---

## 3. Protocollo Augmented EKE

In questo schema, il server memorizza un valore $v$ che serve a verificare la password, ma non a generare la prova di identità dell'utente.

### Setup Matematico

Il server (Bob) memorizza per ogni utente:

1. Username e Salt pubblico $u$.
    
2. Il Verifier $v$, calcolato come:
    

$$W = H(u \parallel \text{"Alice"} \parallel \text{password})$$

$$v = g^W \pmod p$$

### Passaggi del Protocollo

Alice vuole autenticarsi. Lei conosce la password (e quindi può calcolare $W$), Bob conosce solo $v$.

1. **Alice $\rightarrow$ Bob:** Invia la sua parte pubblica Diffie-Hellman.
    
    $$A = g^a \pmod p$$
    
2. **Bob $\rightarrow$ Alice:** Bob deve "mascherare" il suo contributo $g^b$ usando il verifier $v$.
    
    $$B = (v^u \cdot g^b) \pmod p, \; u, \; C_B$$
    
    _(Bob invia anche il salt $u$ e un challenge $C_B$)_. Il **B** calcolato servirà per calcolarsi la chiave segreta **K**.
    
3. **Alice $\rightarrow$ Bob** :  Alice invia a Bob la challenge $C_B$ criptata con la chiave K (per autenticarsi) e manda la challenge $C_A$ per autenticare Bob: $$E_K(C_B),\  C_A$$
4. **Bob $\rightarrow$ Alice** :  Bob invia ad Alice la challenge $C_A$ criptata con la chiave K (per autenticarsi ad Alice) : $$E_K(C_B),\  C_A$$
### **Calcolo della Chiave $K$:**

Qui avviene la magia matematica che permette ad Alice di rimuovere il mascheramento.
- **Calcolo di Alice:**   $$S = \left( \frac{B}{v^u} \right)^a \pmod p = (g^b)^a \pmod p$$
  _(Alice usa $W$ per calcolare $v$ e "pulire" il messaggio di Bob)_10.
   
- **Calcolo di Bob:**$$S = A^b \pmod p = (g^a)^b \pmod p$$
> [!abstract] Visual Analysis (Augmented PDM)
>
![[Pasted image 20251228223733.png]]
> 
> What to look at: Lo schema mostra lo scambio per la variante PDM Augmentata.
> 
> Meaning: Nota come Bob memorizza $2^W$ (il verifier). Alice invia $2^a$. Bob risponde con $2^b$ e un hash di verifica. In questo caso specifico, l'augmentation è gestita tramite hash, ma il principio rimane: Bob non ha $W$, ha solo $2^W$.

---

## 4. SRP (Secure Remote Password)

SRP è un miglioramento di Augmented EKE ed è ampiamente utilizzato (standard industriale). Introduce un moltiplicatore $k$ per rendere ancora più sicura la verifica.

### Setup SRP

- **Globals:** Primo $p$, generatore $g$, moltiplicatore $k = H(p \parallel g)$.
    
- **Server Store:**
    
    $$ v = g^W \pmod p$$
    

### Workflow SRP

1. **Alice $\rightarrow$ Bob:**
    
    $$A = g^a \pmod p$$
    
2. Bob $\rightarrow$ Alice:
    
    Bob calcola il messaggio $B$ sommando il verifier moltiplicato per $k$:
    
    $$B = (k \cdot v + g^b) \pmod p$$
    
    .
    
3. Calcolo della Chiave $K$:
    
    Viene introdotto un valore di "scrambling" $r = H(A \parallel B)$ per legare la sessione.
    
    **Alice calcola:**
    
    $$S = (B - k \cdot v)^{a + rW} \pmod p$$
    
    _(Alice sottrae la componente del verifier per ottenere $g^b$)_.
    
    **Bob calcola:**
    
    $$S = (A \cdot v^r)^b \pmod p$$
    
    .
    

> [!abstract] Math Analysis
> 
> L'equazione di Bob funziona perché:
> 
> $$A \cdot v^r = g^a \cdot g^{Wr} = g^{a+Wr}$$
> 
> Elevando tutto alla $b$ (il segreto di Bob), ottiene lo stesso valore che Alice ha calcolato usando il suo segreto effimero $a$ e la password $W$.

---

## 5. Augmentation ad Alte Prestazioni (RSA)

Le esponenziazioni Diffie-Hellman sono computazionalmente costose. Per migliorare le performance lato server, si può usare RSA.

Idea di base:

Il server esegue una verifica di firma RSA (molto veloce) invece di un'esponenziazione completa DH.

### Implementazione

1. **Server Store:** Bob memorizza la chiave privata RSA di Alice **cifrata** con la password di Alice ($Y$), e la corrispondente chiave pubblica in chiaro.
    
    $$Y = E_{\text{pwd}}(\text{Alice Private Key})$$
    
2. **Il Flusso:**
    
    - Alice inizia lo scambio EKE.
        
    - Bob invia $Y$ ad Alice (oltre ai parametri DH), ed una challenge $c$.
        
    - Alice decifra $Y$ usando la sua password per ottenere la sua **Chiave Privata**.
        
    - Alice **firma** un hash della chiave di sessione con la challenge $c$ e lo invia a Bob.
        
    - Bob verifica la firma usando la chiave pubblica di Alice che ha in memoria.
    
![[Pasted image 20251229113628.png]]
> [!example] Professor's Logic
> 
> Bob agisce come una "cassaforte digitale". Custodisce la chiave privata di Alice, ma non può usarla perché è cifrata con la password di Alice (che Bob non conosce). Solo Alice può sbloccarla e usarla per firmare, provando così la sua identità.

---

# Gestione Sicura delle Password (Modern Rules)

## 1. Il Contesto: Perché è importante?

Le violazioni delle password rimangono il punto di ingresso n. 1 per gli attaccanti.

L'obiettivo della progettazione moderna non è solo "prevenire" l'attacco, ma rendere le credenziali rubate inutili.

### Il Ciclo di Vita della Password

Ogni password attraversa 6 fasi critiche che devono essere gestite:

1. **Creazione:** Generazione sicura.
    
2. **Archiviazione (Storage):** Salvataggio protetto (Mai in chiaro!).
    
3. **Utilizzo:** Login e autocompletamento.
    
4. **Manutenzione:** Aggiornamento dei parametri di sicurezza.
    
5. **Recovery/Reset:** Procedure di recupero credenziali.
    
6. **Ritiro (Retirement):** Eliminazione sicura.
    

---

## 2. Modelli di Attacco e Difesa

Per difenderci, dobbiamo capire come operano i tre tipi principali di attaccante.

### Tassonomia degli Attaccanti

- **Attaccante Offline:** Ha rubato il database (DB breach). Usa GPU potenti per crackare gli hash.
    
- **Attaccante Online:**
    
    - _Credential Stuffing:_ Usa password rubate altrove (sfrutta il riutilizzo).
        
    - _Password Spraying:_ Prova password comuni (es. "Winter2025") su molti account.
        
- **Phishing:** Crea siti falsi (domain spoofing) per ingannare l'utente.
    

### Strategia di Riduzione del Rischio

L'obiettivo difensivo è duplice:

1. **Aumentare il costo per tentativo:** Rendere lento e costoso indovinare una password (tramite KDF lenti).
    
2. **Ridurre la superficie di attacco:** Eliminare password brevi, riutilizzo e vulnerabilità al phishing.
    

---

## 3. Regole di Archiviazione: Salt vs Pepper

Non salvare mai le password in chiaro o con crittografia reversibile. Usa sempre funzioni di hash (KDF).

### Salt (Sale)

- **Caratteristiche:** Stringa casuale, univoca per ogni utente, lunga almeno 16 byte.
    
- **Posizione:** Salvato nel database _insieme_ all'hash.
    
- **Scopo:** Difende contro le **Rainbow Tables** (attacchi pre-calcolati).
    

### Pepper (Pepe)

- **Caratteristiche:** Unico segreto condiviso per tutto il sistema (o per gruppo).
    
- **Posizione:** Salvato **FUORI** dal database (es. in un file di config sicuro o HSM - Hardware Security Module).
    
- **Scopo:** Aggiunge un livello di sicurezza. Se il DB viene rubato ma il Pepper è al sicuro, il database è inutile.
    

### Logica Matematica di Archiviazione

La costruzione corretta per l'hashing sicuro combina entrambi:

$$\text{Hash} = \text{KDF}(\text{Password} \parallel \text{Pepper} \parallel \text{Salt})$$

> [!abstract] Math Analysis
> 
> - **$\parallel$**: Simbolo di concatenazione.
>     
> - **KDF**: Key Derivation Function (funzione lenta come Argon2 o bcrypt).
>     
> - **Risultato:** Nel database salvi la coppia `(Hash, Salt)`. Il `Pepper` rimane segreto altrove.
>     

![[Pasted image 20251229114624.png]]

> [!tip] Exam Focus
> 
> Differenza Chiave:
> 
> - Il **Salt** è pubblico (nel DB) e serve per l'unicità.
>     
> - Il **Pepper** è segreto (fuori dal DB) e serve per la difesa in profondità.
>     

---

## 4. Manutenzione: Freshness dei Parametri

L'hardware degli attaccanti migliora ogni anno (Legge di Moore). I parametri di sicurezza devono evolversi.

- **Revisione Annuale:** Controlla i costi delle KDF.
    
- **Argon2:** Aumenta memoria/tempo se la verifica richiede < 100 ms.
    
- **Bcrypt:** Aumenta il _cost factor_ man mano che le CPU diventano più veloci.
    
- **Azione:** Se i parametri sono obsoleti, forza il **re-hashing** al prossimo login dell'utente.
    

---

## 5. Password Policy (Lato Utente)

Le vecchie regole (es. "Cambia password ogni 90 giorni", "Obbligo caratteri speciali") sono obsolete e dannose.

### Le Nuove Regole (NIST/OWASP)

- **Lunghezza:** Minimo 12 caratteri (16 per admin). La lunghezza batte la complessità.
    
- **Complessità Arbitraria:** **NO**. Non forzare simboli speciali (portano a password come `P@ssword1!`).
    
- **Spazi:** Permetti l'uso di spazi per favorire le **Passphrases**.
    
- **Blocklist:** Blocca le password notoriamente compromesse (usa API come _Have I Been Pwned_) e pattern banali (nome azienda, stagione+anno).
    

> [!example] Professor's Example
> 
> Bad: P@ssword! (Complessa ma prevedibile).
> 
> Good: fluffy-hamster-telescope-42 (Passphrase: alta entropia, facile da ricordare).

---

## 6. Password Manager

L'unica password sicura è quella che non devi ricordare.

- **Funzionamento:** L'utente ricorda solo la _Master Password_. Tutto il resto è in un vault cifrato.
    
- **Vantaggi:**
    
    - Genera password casuali di 20+ caratteri.
        
    - Previene il riutilizzo.
        
    - Protegge dal Phishing (l'autofill non funziona su domini falsi).
        

**Esempi Citati:**

- **Bitwarden:** Open-source, cloud sync.
    
- **1Password:** Commerciale, ottime feature business.
    
- **KeePassXC:** Offline, locale (massima privacy, niente cloud).
    

### Design Compatibile

I form di login devono supportare i manager:

- **Abilitare il PASTE:** Mai bloccare l'incolla della password.
    
- **Lunghezza:** Supportare almeno 64 caratteri (meglio nessun limite).
    
- **Caratteri:** Non bloccare simboli "strani" o emoji.
    

---

## 7. Reset Sicuro e "Security Questions"

### Kill the Security Questions

Le domande di sicurezza ("Nome del tuo cane", "Cognome da nubile di tua madre") sono **insicure**.

- Le risposte sono spesso pubbliche (OSINT su social media) o facili da indovinare.
    
- **Regola:** Non usarle mai come unico metodo di recupero.
    

### Best Practice per il Reset

1. **Out-of-Band (OOB):** Invia un link/codice via Email, SMS o Push Notification.
    
2. **Lock:** Blocca l'account dopo il reset fino al prossimo login corretto.
    
3. **Notifica:** Avvisa sempre l'utente (su un canale separato) che è avvenuto un reset.
    

---

## 8. Checklist Finale (Riepilogo)

> [!failure] Common Mistakes
> 
> - Bloccare il copia-incolla nei form.
>     
> - Imporre limiti di lunghezza arbitrari (es. max 16 chars).
>     
> - Salvare il Pepper nello stesso DB degli hash.
>     
> - Non aggiornare mai i parametri KDF.
>     

**La Checklist Minimale:**

- [ ] Password uniche e casuali.
    
- [ ] Lunghezza minima adeguata e controllo contro i leak (HIBP).
    
- [ ] KDF moderno con Salt (per utente) + Pepper.
    
- [ ] Reset sicuro tramite canale OOB (no domande segrete).
    
- [ ] Interfaccia amichevole per i Password Manager.


---

# Autenticazione: Con o Senza Chiavi di Sessione

## 1. I Due Paradigmi dell'Autenticazione

Quando progettiamo un protocollo di autenticazione, ci troviamo di fronte a un bivio fondamentale. L'esito del processo può essere di due tipi:

1. **Autenticazione + Chiave di Sessione (Session Key):**
    
    - L'identità viene verificata.
        
    - Viene generata una chiave crittografica fresca ed effimera per proteggere le comunicazioni successive.
        
2. **Solo Autenticazione (Authentication Only):**
    
    - L'identità viene verificata.
        
    - **Non** viene generata alcuna nuova chiave. Il processo finisce lì.
        

---

## 2. Definizioni Chiave

### Cos'è una Session Key?

Una chiave di sessione è una chiave crittografica con proprietà specifiche:

- **Short-lived:** Ha vita breve (dura quanto la sessione).
    
- **High-Entropy:** È generata casualmente (imprevedibile).
    
- **Ephemeral:** Viene distrutta al termine della sessione.
    

### Cos'è l'Autenticazione (Pura)?

È il processo di provare l'identità a un peer (controparte).

- Si basa su tecnologie diverse (password, biometria).
    
- **Non implica** necessariamente la crittografia dei dati successivi.
    

---

## 3. Scenari d'Uso: Il Confronto

Dobbiamo saper distinguere dove si applicano questi due approcci nel mondo reale.

### Caso A: Solo Autenticazione (No Keys)

Si usa quando l'obiettivo è verificare l'accesso puntuale o quando il canale è già sicuro.

- **Login Locale:** Inserimento password per sbloccare il PC (non serve cifrare il bus dati della tastiera).
    
- **Controllo Accessi Fisico:** Badge per aprire una porta.
    
- **Canale già sicuro:** Comunicazione su un cavo dedicato o VPN pre-esistente.
    
- **Vincoli di Risorse:** Dispositivi IoT a batteria che non possono sprecare CPU per generare chiavi effimere (es. Diffie-Hellman).
    

> [!example] Professor's Example
> 
> Pensate al tornello della metropolitana. Passate il biglietto (autenticazione), il tornello si apre. Non viene creato un "canale segreto" tra voi e il tornello per il resto del viaggio. È un evento "one-shot".

### Caso B: Autenticazione + Chiave (With Keys)

Si usa quando dobbiamo proteggere il traffico dati che segue l'autenticazione.

- **TLS/SSL:** Handshake del server + creazione chiavi per HTTPS.
    
- **SSH:** Scambio chiavi prima dell'autenticazione utente.
    
- **Protocolli PAKE:** (Password-Authenticated Key Exchange) come SRP o EKE.
    

---

## 4. Rischi e Benefici (Trade-offs)

### Rischi dell'approccio "Solo Autenticazione"

Se non generiamo una chiave di sessione, ci esponiamo a:

1. **Nessuna Forward Secrecy:** Se la chiave a lungo termine (password o chiave master) viene rubata, tutte le sessioni passate possono essere decifrate.
    
2. **Rischio Replay:** Un attaccante può registrare il messaggio di "OK" e riprodurlo per entrare (a meno che non si usino timestamp o nonce).
    
3. **Mancanza di Isolamento:** La stessa chiave autentica tutto, indefinitamente.
    

### Benefici dell'approccio "Con Chiave di Sessione"

L'uso di chiavi effimere garantisce proprietà di sicurezza superiori:

- **Forward Secrecy (Segretezza in Avanti):**
    
    - Ogni sessione ha una chiave indipendente.
        
    - La compromissione di una chiave non impatta le altre (passate o future).
        
- **Key Confirmation:**
    
    - Entrambe le parti provano di possedere la stessa chiave, confermando che il canale è stabilito correttamente.
        
- **Cryptographic Binding:**
    
    - La prova di autenticazione è legata matematicamente a quella specifica sessione.
        

> [!tip] Exam Focus
> 
> Domanda tipica: "Perché preferire le Session Keys anche se sono computazionalmente costose?"
> 
> Risposta: Principalmente per la Forward Secrecy e il Damage Limitation. Se rubano la chiave di sessione n. 5, le sessioni n. 4 e n. 6 rimangono sicure.

---

## 5. Linee Guida di Progettazione (Design Guidance)

Come decidere quale approccio usare nel vostro progetto?

### Usa "Solo Autenticazione" se:

- Il traffico successivo è minimo o pubblico.
    
- La sessione è già protetta da un altro layer (es. Tunnel IPSec).
    
- Hai vincoli hardware estremi (CPU/Batteria).
    
- _Nota:_ Devi comunque aggiungere **Nonce** o **Timestamp** per evitare attacchi di replay.
    

### Usa "Autenticazione + Chiave" se:

- Hai bisogno di **Forward Secrecy** (Cruciale per privacy).
    
- Vuoi isolare le sessioni l'una dall'altra.
    
- Serve un binding crittografico forte tra identità e canale dati.
    

### Checklist per Protocolli con Chiavi di Sessione

Se decidi di generare chiavi, segui queste regole d'oro:

1. **Meccanismi di Hashing Sicuri:** Usa KDF robuste.
    
2. **Context Binding:** Includi identità, ruoli e transcript del protocollo nella derivazione della chiave.
    
3. **Conferma Esplicita:** Usa un MAC sui messaggi di handshake per confermare che entrambi hanno la stessa chiave.
    
4. **Effimere:** Usa chiavi _ephemeral_ e scartale (cancellale dalla memoria) subito dopo la fine della sessione.
    
5. **Separazione:** Deriva chiavi diverse per scopi diversi (una chiave per cifrare, una diversa per l'integrità/MAC).
    

> [!failure] Common Pitfall
> 
> Errore grave: Usare la stessa chiave sia per cifrare i dati (Confidentiality) sia per calcolare il MAC (Integrity).
> 
> Soluzione: Dalla chiave di sessione "master", deriva due sotto-chiavi indipendenti: $K_{enc}$ e $K_{mac}$.