# Autenticazione a Chiave Pubblica e Confronto con Kerberos

**Tags:** #ingegneria #security #autenticazione #crittografia #kerberos

## 1. Motivazione e Obiettivi

L'obiettivo fondamentale dell'autenticazione è verificare l'identità delle entità che comunicano su reti **non fidate**.

In un contesto di rete aperta, dobbiamo prevenire:

- **[[Impersonification]]:** Qualcuno finge di essere un altro.
    
- **[[Man-in-the-Middle (MITM)]]:** Un attaccante intercetta e manipola il traffico.
    

L'autenticazione permette di stabilire sessioni sicure e gestire le autorizzazioni. Esistono due approcci principali per farlo: l'approccio [[Symmetric Encryption#Autenticazione a Chiave Simmetrica|simmetrico]] (es. [[Kerberos]]) e quello a chiave pubblica.

---

## 2. Approccio Simmetrico e i suoi Limiti

Nel modello base simmetrico, l'autenticazione si basa sulla condivisione di un segreto (password o chiave) tra le parti.

### Vantaggi e Svantaggi

- **Pro:** È un metodo veloce e semplice, utilizza primitive crittografiche efficienti (MAC, cifrari). Funziona bene in sistemi piccoli e chiusi.
    
- **Contro (Senza [[KDC (Key Distribution Center)]]):** La distribuzione delle chiavi su larga scala è problematica. Se ogni utente deve parlare con ogni altro utente in modo sicuro, il numero di chiavi esplode.
    

### Analisi Matematica della Scalabilità

**The complexity of key management in a naive symmetric model is:**

$$\text{Chiavi totali} \approx O(n^2)$$

> [!abstract] Math Analysis
> 
> Con $n$ parti coinvolte, servirebbero coppie di segreti per ogni possibile connessione, rendendo la gestione impossibile su larga scala. Inoltre, se un verificatore viene compromesso, l'intero database utenti è a rischio.

---

## 3. Kerberos: La Soluzione Simmetrica Scalabile

Kerberos risolve il problema dell'esplosione delle chiavi $O(n^2)$ introducendo una **Terza Parte Fidata ([[Trusted Third Party (TTP)]])** chiamata **[[KDC (Key Distribution Center)]]**.

### Funzionamento Core

- Ogni entità (Principal) condivide **UNA sola chiave a lungo termine** con il KDC.
    
- Non c'è bisogno di segreti condivisi tra tutti gli utenti.
    
- Il KDC rilascia "ticket" con validità temporale limitata per accedere ai servizi (meccanismo SSO - Single Sign-On).
    

**The scalability improvement is defined as:**

$$\text{Gestione Chiavi Kerberos} = O(n)$$

> [!abstract] Math Analysis
> 
> Passiamo da una complessità quadratica a una lineare. Questo rende il sistema gestibile in ambienti Enterprise.

### Limiti Residui di Kerberos

Nonostante l'efficienza, Kerberos presenta dei vincoli strutturali:

1. **Single Point of Failure/Attack:** Il KDC è un bersaglio critico. Se compromesso, permette l'impersonificazione universale (Key Escrow).
    
2. **Requisiti Operativi:** Richiede che il KDC sia sempre raggiungibile (online) e necessita di sincronizzazione temporale precisa.
    
3. **Difficoltà Cross-Realm:** Gestire la fiducia tra organizzazioni diverse (es. Università A che parla con Azienda B) è amministrativamente complesso.
    
4. **Sicurezza Credenziali:** Spesso le chiavi derivano da password, vulnerabili ad attacchi di _offline guessing_.
    

---

## 4. Autenticazione a Chiave Pubblica

Questo approccio elimina la necessità di una terza parte online durante l'autenticazione, sfruttando la crittografia asimmetrica.

### Concetti Chiave

- **Key Pair:** Una chiave Privata (segreta) e una Pubblica (condivisa).
    
- **Firma Digitale:** Si verifica con la chiave pubblica; è matematicamente impossibile derivare la privata dalla pubblica.
    
- **Principio:** L'autenticazione consiste nel _provare il possesso_ della chiave privata senza mai rivelarla.
    

> [!abstract] Il Flusso Challenge-Response
> 
>  Ecco lo scambio tra Verifier e Prover:
> 
> 1. Il Verifier invia una **sfida casuale (nonce)**.
>     
> 2. Il Prover **firma** la sfida con la propria chiave privata.
>     
> 3. Il Verifier controlla la firma usando la chiave pubblica del Prover.
>     
>     Nota: Non c'è alcun segreto condiviso trasmesso sulla rete.
>     

### Vantaggi

- **Decentralizzazione:** Il verificatore può validare l'identità offline (se ha già la chiave pubblica).
    
- **Scala Internet:** Funziona naturalmente tra organizzazioni diverse (Open Internet) senza amministrazione complessa.
    
- **[[Non-Repudiation]]:** Non essendoci "Key Escrow" (nessun server ha la tua privata), la prova è molto più forte.
    

---

## 5. Il Problema della "Falsa Chiave Pubblica"

> [!failure] Common Pitfall
> 
> L'autenticazione a chiave pubblica è forte SOLO SE siamo certi che la chiave pubblica appartenga davvero a chi dice di essere.

### L'Attacco

Se un avversario riesce a sostituire la chiave pubblica della vittima con la propria:

1. L'avversario invia la **sua** chiave pubblica fingendo sia quella della vittima.
    
2. Il verificatore accetta questa chiave.
    
3. L'avversario firma i messaggi con la **sua** chiave privata.
    
4. Il verificatore controlla la firma con la chiave pubblica (falsa) che ha ricevuto: la matematica torna, la verifica ha successo.
    

**Risultato:** Autenticazione riuscita per l'attaccante. Crittografia corretta, ma **Identity Binding errato**.

### Soluzione: Certificati

Per garantire l'autenticità della chiave pubblica, si usano i **Certificati**.

- Sono dichiarazioni firmate digitalmente che legano un'identità a una chiave pubblica.
    
- Il verificatore controlla la firma di un'autorità fidata (CA) prima di fidarsi della chiave.
    

---

## 6. Confronto Finale: Kerberos vs Public Key

> [!tip] Exam Focus
> 
> Questa tabella riassuntiva è spesso oggetto di domande d'esame per capire quando usare una tecnologia rispetto all'altra.

|**Aspetto**|**Chiave Simmetrica (Kerberos)**|**Chiave Pubblica**|
|---|---|---|
|**Gestione Chiavi**|$O(n)$ con KDC (altrimenti $O(n^2)$)|Ogni utente ha 1 coppia di chiavi|
|**Modello di Fiducia**|Terza parte fidata online (KDC)|Autenticità via Certificati/Trust Anchors|
|**Scalabilità**|Ottima in domini chiusi (Enterprise)|Globale, naturale per reti aperte|
|**Rischi**|Compromissione KDC espone tutti|Falsa chiave pubblica rompe l'auth|
|**Performance**|Veloce, operazioni efficienti|Computazionalmente intensivo|

### Quando scegliere cosa?

- **Usa Kerberos se:** Sei in una rete aziendale (Enterprise/Realm), con utenti noti, amministrazione centralizzata e bisogno di alte performance.
    
- **Usa Chiave Pubblica se:** Sei su Internet, devi comunicare tra organizzazioni diverse, usi Smartcards/Token o non vuoi terze parti online.

---

# Protocolli di Autenticazione a Chiave Pubblica e Standard X.509

## 1. Introduzione e il Problema della Fiducia

L'autenticazione a chiave pubblica sembra semplice: invio un messaggio firmato o cifrato e, se la matematica funziona, l'autenticazione ha successo. Tuttavia, esiste un problema fondamentale.

Il problema di Trudy (Man-in-the-Middle):

Anche se la crittografia è solida, devo essere sicuro che la chiave pubblica che sto usando appartenga davvero alla persona con cui voglio parlare.

Se Trudy (l'attaccante) mi convince che la sua chiave pubblica appartiene ad Alice:

1. Io cifro i messaggi per Alice usando la chiave di Trudy.
    
2. Trudy li decifra, li legge, e li ricifra per Alice.
    
3. Io credo di parlare con Alice in modo sicuro, ma Trudy è nel mezzo.
    

> [!tip] Exam Focus
> 
> La soluzione strutturale a questo problema è la PKI (Public Key Infrastructure): un'autorità che garantisce la correttezza delle chiavi pubbliche tramite certificati.

---

## 2. Protocollo Needham-Schroeder (Public Key)

Questo è un protocollo classico per l'autenticazione mutua (Alice e Bob si autenticano a vicenda) utilizzando un server di fiducia (C).

### Funzionamento Logico

Alice (A) vuole parlare con Bob (B) ma non ha la sua chiave pubblica. Chiede aiuto al server (C).

**The protocol definition is:**

$$\begin{align} 1. & \ A \to C: \{A, B\} \\ 2. & \ C \to A: \{B, K_{PB}, Sig_C(K_{PB}, B)\} \\ 3. & \ A \to B: K_{PB}(N_A, A) \\ 4. & \ B \to C: \{B, A\} \\ 5. & \ C \to B: \{A, K_{PA}, Sig_C(K_{PA}, A)\} \\ 6. & \ B \to A: K_{PA}(N_A, N_B) \\ 7. & \ A \to B: K_{PB}(N_B) \end{align}$$

> [!abstract] Math Analysis
> 
> - **Passi 1-2:** A ottiene la chiave pubblica di B ($K_{PB}$) dal server, firmata per garantirne l'autenticità.
>     
> - **Passo 3:** A sfida B inviando un **nonce** ($N_A$) cifrato con la chiave di B.
>     
> - **Passi 4-5:** B fa lo stesso per ottenere la chiave di A.
>     
> - **Passo 6:** B dimostra di essere lui (decifrando $N_A$) e invia una sua sfida ($N_B$).
>     
> - **Passo 7:** A dimostra di essere lei rimandando indietro $N_B$.
>     

---

## 3. L'Attacco al Needham-Schroeder (MITM)

Il protocollo sopra descritto ha una vulnerabilità critica se un attaccante (T) è un utente legittimo del sistema.

### La Dinamica dell'Attacco

L'attaccante T si interpone. Quando A cerca di parlare con T (operazione legittima), T sfrutta questa sessione per aprire una sessione fraudolenta con B a nome di A.

**The attack flow focuses on steps 3, 6, and 7:**

$$\begin{align} 3. \ (R1) \ & A \to T: K_{PT}(N_A, A) \\ 3. \ (R2) \ & T(A) \to B: K_{PB}(N_A, A) \\ 6. \ (R2) \ & B \to T(A): K_{PA}(N_A, N_B) \\ 6. \ (R1) \ & T \to A: K_{PA}(N_A, N_B) \\ 7. \ (R1) \ & A \to T: K_{PT}(N_B) \\ 7. \ (R2) \ & T(A) \to B: K_{PB}(N_B) \end{align}$$

> [!failure] Common Pitfall
> 
> Cosa succede qui?
> 
> - A pensa di parlare con T (e invia $N_A$).
>     
> - T usa $N_A$ per ingannare B, fingendo di essere A.
>     
> - B risponde con la sfida $N_B$ cifrata per A ($K_{PA}$). T non può decifrarla!
>     
> - **Il trucco:** T inoltra il messaggio cifrato ad A (passo 6).
>     
> - A, credendo sia la risposta di T, lo decifra e rimanda indietro il nonce $N_B$ a T.
>     
> - Ora T ha il nonce $N_B$ in chiaro e può chiudere l'autenticazione con B.
>     

---

## 4. Il Fix del Needham-Schroeder

Per bloccare l'attacco, bisogna impedire che il messaggio del passo 6 possa essere riciclato in un contesto diverso.

**The corrected step 6 is:**

$$6. \ B \to A: K_{PA}(B, N_A, N_B)$$

> [!abstract] Math Analysis
> 
> B include la propria identità ($B$) nel messaggio cifrato.
> 
> Quando A decifra il messaggio, si aspetta di trovare l'identità di T (perché crede di parlare con T). Se trova "B", capisce che c'è un errore e interrompe la comunicazione.

---

## 5. Standard X.509

Lo standard X.509 definisce il formato dei certificati e i protocolli di autenticazione.

### Autenticazione One-Way (Singola)

Serve solo per autenticare A verso B (es. invio di una email certificata).

$$A \to B: Cert_A, D_A, Sig_A(D_A)$$

Dove $D_A$ contiene un timestamp ($t_A$), l'identità di B e una chiave di sessione cifrata.

### Autenticazione Two-Way (Mutua)

Entrambe le parti si autenticano. Introduce però una vulnerabilità simile a quella vista prima, perché la risposta di B non contiene esplicitamente l'identità di A nel corpo firmato.

### Autenticazione Three-Way

Risolve i problemi di sincronizzazione oraria (non usa timestamp ma solo nonce) e chiude le vulnerabilità di replay.

**The final step requires signing the nonces:**

$$3. \ A \to B: \{B, Sig_A(N_A, N_B, B)\}$$

> [!abstract] Visual Analysis
> 
> Il passo 3 è cruciale: legando insieme i due nonce ($N_A, N_B$) e l'identità del destinatario ($B$) tramite la firma digitale, si rende impossibile riutilizzare questo messaggio in un'altra sessione.

---

## 6. ISO/IEC 9798-3 e il "Canadian Attack"

Anche gli standard ISO hanno avuto versioni vulnerabili. Il protocollo 9798-3 (versione anni '90) soffriva di un difetto di design.

### Il Difetto (Bugged Version)

Nel passo 3, B inviava un nonce e la sua firma, ma **non legava** abbastanza fortemente le identità dei peer ai dati firmati.

**The "Canadian Attack" (Boyd & Mathuria, 2003):**

$$\begin{align} d) & \ B \to T(A): Cert_B, N_B, N_A, A, Sig_B(N_B, N_A, A) \\ e) & \ T(B) \to A: Cert_B, N_B, N_A, A, Sig_B(N_B, N_A, A) \end{align}$$

> [!failure] Common Pitfall
> 
> L'attaccante T inoltra semplicemente la firma valida di B ad A. A verifica la firma ed è corretta, ma non si rende conto che quella firma era destinata a una sessione in cui T stava impersonando A, non a una sessione diretta con B. Manca il "binding" delle identità.

---

## 7. Conclusioni e Trend Moderni

### Necessità della PKI

Senza una Public Key Infrastructure (PKI), non possiamo rispondere alla domanda: "Di chi è questa chiave?".

- **Certificati:** Uniscono Identità + Chiave Pubblica.
    
- **Trust Anchors:** Le Certification Authorities (CA) di cui ci fidiamo globalmente.
    

---

# Passkeys e Standard FIDO2: Il Nuovo Paradigma di Autenticazione

## 1. Oltre le Password: Il Concetto di Passkey

Le password tradizionali si basano su un **segreto condiviso**: l'utente e il server conoscono la stessa stringa. Questo modello è intrinsecamente vulnerabile a:

- Phishing.
    
- Credential Stuffing.
    
- Violazioni del database (se il server viene bucato, i segreti sono esposti).
    

Le **Passkeys** sostituiscono questo modello utilizzando la **Crittografia Asimmetrica** (Public Key Cryptography) unita allo sblocco biometrico locale.

- Basate sullo standard **FIDO2** (Fast IDentity Online).
    
- L'utente prova il possesso della chiave privata.
    
- La chiave privata **non viene mai trasmessa** al server.
    

---

## 2. Fondamenti Crittografici: ECDSA vs EdDSA

Le Passkeys utilizzano moderne curve ellittiche. È fondamentale distinguere i due algoritmi principali per la gestione della firma digitale.

### [[ECDSA]] (Elliptic Curve Digital Signature Algorithm)

#### Algoritmo di Firma (Signing)

Il processo di firma serve a generare una prova crittografica legata a un messaggio specifico e alla chiave privata dell'utente. A differenza di EdDSA, questo processo richiede una componente di casualità forte.

**The signing process is defined as:**

$$\begin{align} 1. & \ \text{Input: Private Key} \\ 2. & \ \text{Pick random nonce } k \\ 3. & \ \text{Compute Point } R \text{ (derived from } k) \\ 4. & \ \text{Compute challenge } h = H(m) \\ 5. & \ \text{Output Signature: } (r, s) \end{align}$$

> [!abstract] Math Analysis
> 
> - **Passo 1-2:** Il firmatario deve generare un numero casuale $k$ (nonce) per ogni singola firma.
>     
> - **Passo 3-5:** Utilizzando la chiave privata e il nonce, calcola un punto sulla curva e produce la coppia $(r, s)$. Ma che cosa sono $r$ ed $s$? ecco [[Cos'è (r,s) in ECDSA|qui]].
>     

---

#### Algoritmo di Verifica (Verification)

Il verificatore controlla la validità della firma utilizzando solo dati pubblici, senza mai conoscere la chiave privata.

**The verification logic is:**

$$\begin{align} \text{Input} &: \text{Public Key } Q, \text{Message } m, \text{Signature } (r, s) \\ \text{Step 1} &: \text{Recompute challenge } h = H(m) \\ \text{Step 2} &: \text{Perform curve operations using } Q, m, (r, s) \\ \text{Result} &: \text{Check if result matches } r \to \text{Accept/Reject} \end{align}$$

> [!abstract] Math Analysis
> 
> Il verificatore ricalcola l'hash del messaggio e combina la chiave pubblica con la firma. Se le operazioni sulla curva restituiscono il valore $r$ atteso, la firma è autentica.

---

#### La Vulnerabilità Critica: Il Random Nonce

La sicurezza di ECDSA dipende interamente dalla qualità del generatore di numeri casuali (RNG). Questo è il suo punto debole rispetto a EdDSA.

> [!failure] Common Pitfall: Randomness Failure
> 
> ECDSA si basa sul nonce casuale $k$.
> 
> - **Se l'RNG è debole:** Il nonce diventa prevedibile.
>     
> - **Se il nonce viene riutilizzato:** Se si firmano due messaggi diversi usando lo stesso $k$, un attaccante può calcolare matematicamente la **chiave privata** (Private Key Leakage).
>     
> 
> Questo rende ECDSA fragile in ambienti dove è difficile generare numeri veramente casuali (es. sistemi embedded poveri).

### EdDSA (Edwards-curve Digital Signature Algorithm)
[[EdDSA (Edwards-curve Digital Signature Algorithm)]]

È un algoritmo più moderno e sicuro, progettato per evitare i problemi dell'ECDSA.

**The signing algorithm is formally defined as:**

$$\begin{align} 1. \ \text{Nonce} &= \text{Deterministico (da Private Key)} \\ 2. \ R &= \text{Compute Point (dal Nonce)} \\ 3. \ h &= H(R, A, m) \\ 4. \ \text{Signature} &= (R, s) \end{align}$$

> [!abstract] Math Analysis
> 
> - $A$: è la chiave pubblica del firmatario.
>     
> - $m$: è il messaggio da firmare.
>     
> - $H$: è una funzione di hash crittografica.
>     
> - $R$: è un punto sulla curva ellittica calcolato dal nonce.
>     
> - La firma finale è la coppia $(R, s)$.
>     
_
> Perché è migliore? EdDSA calcola il nonce in modo deterministico (basandosi sul messaggio e sulla chiave) invece di usare un generatore casuale. Questo elimina il rischio di fallimenti del RNG e rende l'algoritmo più veloce e sicuro contro attacchi side-channel.


**The verification steps are:**

$$\begin{align} 1. \ \text{Input} &: \text{Chiave Pubblica } A, \text{Messaggio } m, \text{Firma } (R, s) \\ 2. \ h &= H(R, A, m) \quad (\text{Ricalcolo del challenge}) \\ 3. \ \text{Check} &: \text{Verifica equazione della curva} \end{align}$$

> [!abstract] Math Analysis
> 
> Il verificatore ricalcola l'hash $h$ usando i dati pubblici ($R, A, m$). Se l'equazione della curva ellittica è soddisfatta usando questo $h$, la firma è valida; altrimenti viene rifiutata.

---

## 3. Generazione e Custodia delle Chiavi

Dove risiedono fisicamente le Passkeys? Non sono file sparsi nel filesystem, ma sono protette dall'hardware.

Le chiavi vengono generate e custodite all'interno di un **Authenticator**:

- **TPM (Trusted Platform Module):** Chip dedicato sulla scheda madre.
    
- **Secure Enclave:** Area isolata all'interno della CPU (comune nei moderni smartphone e laptop).
    
- **HSM (Hardware Security Module):** Dispositivi esterni dedicati per alta sicurezza.
    

> [!tip] Exam Focus
> 
> La regola d'oro è: La chiave privata non lascia mai il dispositivo.

---

## 4. Flusso di Registrazione (Registration Flow)

Quando un utente crea una Passkey per un sito, avviene il seguente scambio:

1. L'utente richiede la registrazione.
    
2. Il server invia una sfida e il proprio ID (**RP ID** - Relying Party ID).
    
3. L'Authenticator genera la coppia di chiavi $(Pk, Sk)$.
    
4. L'Authenticator invia al server:
    
    - La **Chiave Pubblica**.
        
    - Il **Credential ID** (un puntatore per ritrovare la chiave in futuro).
        
    - L'**Attestation Signature** (prova che l'hardware è genuino).
        

---

## 5. Flusso di Autenticazione (Authentication Flow)

Quando l'utente vuole fare il login:

1. Il server genera un **Challenge** (nonce fresco) e lo invia insieme al Credential ID.
    
2. L'Authenticator sblocca la chiave privata (tramite biometria/PIN).
    
3. L'Authenticator firma un pacchetto dati contenente:
    
    - Il Challenge.
        
    - L'**RP ID** (il dominio del sito).
        
    - Metadati (es. contatori anti-replay).
        

**The verification logic is:**

$$\text{Verify}(Pk, \text{Signature}, \text{Challenge} + \text{RP ID}) \rightarrow \text{True/False}$$

> [!abstract] Visual Analysis
> 
> Il server verifica la firma usando la chiave pubblica memorizzata. Se la matematica torna, l'utente è autenticato.
> 
> Nota: Non c'è password hash da confrontare.

---

## 6. Sicurezza: Origin Binding e Anti-Phishing

Le Passkeys risolvono il problema del Phishing tramite un meccanismo chiamato **Origin Binding**.

### Come funziona

La credenziale è legata indissolubilmente al dominio web (**RP ID**) durante la creazione.

- Se creo una passkey per `bank.com`.
    
- Un attaccante crea `evil.com` (sito fake identico alla banca).
    
- Il browser/authenticator vede che l'RP ID richiesto è `evil.com` ma la chiave è legata a `bank.com`.
    
- **Risultato:** L'Authenticator **rifiuta** di firmare. L'attacco fallisce automaticamente.
    

> [!failure] Common Pitfall
> 
> Le Passkeys non proteggono dal DNS Poisoning avanzato se l'attaccante riesce a ottenere anche un certificato TLS valido per il dominio legittimo, ma proteggono efficacemente dal phishing "visivo" (URL simili).

---

## 7. Autenticazione Cross-Device

FIDO2 permette di usare le credenziali salvate sullo smartphone per fare login su un PC (es. un computer pubblico o di un amico).

**Il flusso operativo:**

1. Il sito sul PC mostra un **QR Code**.
    
2. Lo smartphone scansiona il QR Code.
    
3. Si stabilisce un canale sicuro effimero (via **Bluetooth** per prossimità e tunnel criptato).
    
4. L'utente si autentica sul telefono (biometria).
    
5. Il telefono invia la firma digitale al browser del PC.
    
6. Login effettuato.
    

> [!abstract] Visual Analysis
> 
> What to look at: La connessione tra telefono e laptop.
> 
> Meaning: Il Bluetooth serve per garantire la prossimità fisica (anti-relay attack remoto), mentre la crittografia protegge i dati.

---

## 8. Confronto Finale: Password vs Passkeys

|**Caratteristica**|**Password**|**Passkeys**|
|---|---|---|
|**Segreto**|Condiviso (Utente e Server sanno tutto)|Coppia di chiavi asimmetriche|
|**Storage Server**|Hash della password (vulnerabile)|Solo Chiave Pubblica (innocua)|
|**Phishing**|Alta suscettibilità|Impossibile (Origin Binding)|
|**Attacco Offline**|Cracking possibile sugli hash|Nessun segreto da crackare|
|**Riutilizzo**|Spesso riutilizzate (pericoloso)|Chiave unica per ogni dominio|

---

# Integrazione: Passkeys Gestite vs Hardware-Bound

**Tags:** #ingegneria #security #passkeys #bitwarden #fido2 #real_world_implementation

## 1. Il "Non Detto" delle Slide: Platform vs Roaming

Le slide del corso descrivono principalmente le Passkeys nel contesto dei **Platform Authenticators** (o _Single-Device Passkeys_).

- **Modello Slide:** La chiave è generata nel chip TPM o nella Secure Enclave del dispositivo (es. iPhone, PC Windows Hello).
    
- **Vincolo:** La chiave privata non lascia mai il dispositivo. Se perdi il telefono o il computer, perdi l'accesso a quella specifica credenziale.
    

La Realtà (Bitwarden, 1Password, Apple Keychain):

Questi servizi agiscono come Cross-Platform Authenticators. Implementano lo standard FIDO2 ma introducono la sincronizzazione delle chiavi private.

---

## 2. Come funziona tecnicamente con Bitwarden?

Quando usi un gestore di password come Bitwarden per una Passkey, il "Vault" cifrato sostituisce funzionalmente il TPM fisico descritto nella teoria classica.

### Differenze nel flusso operativo

1. **Generazione:** Invece di chiedere al chip TPM di creare la coppia $(Pk, Sk)$, è il software di Bitwarden a generarla localmente nella memoria sicura del dispositivo.
    
2. **Archiviazione:**
    
    - _Modello Hardware (Slide):_ La chiave privata $Sk$ resta isolata nel silicio del chip.
        
    - _Modello Bitwarden (Synced):_ La chiave privata $Sk$ viene cifrata con la chiave maestra dell'utente (es. AES-256) e salvata nel cloud.
        
3. **Sincronizzazione:** Questo "blob" cifrato viene scaricato sugli altri tuoi dispositivi, permettendoti di fare login da qualsiasi postazione.
    

> [!abstract] Visual Analysis
> 
> Il concetto di "Authenticator" nello standard WebAuthn è un'entità logica, non per forza fisica. Bitwarden agisce come un Software Authenticator che emula il comportamento sicuro richiesto dal protocollo, garantendo però la portabilità.

---

## 3. Analisi dei Trade-off: Sicurezza vs Comodità

> [!tip] Exam Focus
> 
> Se all'esame viene chiesto se le passkey sono sempre vincolate all'hardware, la risposta teorica basata sulle slide è "sì" (per garantire la non-esportabilità), ma la risposta ingegneristica completa è che esistono le Synced Passkeys (o Multi-Device Credentials).

|**Caratteristica**|**Hardware-Bound (Modello Slide)**|**Synced (Modello Bitwarden)**|
|---|---|---|
|**Dove vive la chiave**|Chip fisico (TPM/Enclave)|Vault cifrato (Cloud + Cache locale)|
|**Portabilità**|Nulla (Vincolata al singolo device)|Totale (Sync su tutti i device)|
|**Recovery**|Difficile (Se perdi il device, perdi la chiave)|Facile (Basta la Master Password)|
|**Vettore di Attacco**|Furto fisico del dispositivo + Biometria|Compromissione della Master Password|
|**Attinenza alle Slide**|Totale (descrizione fedele)|Parziale (estensione pratica dello standard)|

---

## 4. Perché le slide non ne parlano?

Le slide si concentrano sulle **garanzie crittografiche forti** che sono alla base della teoria:

- **Attestation:** Molti servizi ad alta sicurezza (es. banking o corporate access) richiedono l'**Attestazione**, ovvero la prova crittografica che la chiave risiede in un hardware sicuro e non modificabile. Le chiavi software come quelle di Bitwarden spesso non possono fornire questo livello di garanzia (o forniscono un'attestazione "software").
    
- **Non-Exportability:** Il focus didattico è sulla sicurezza assoluta: la chiave non deve mai poter essere copiata. I password manager, per definizione, devono esportare la chiave (in modo sicuro e cifrato) per poterla sincronizzare, violando il principio purista della "non-esportabilità" a favore dell'usabilità.
    

### Conclusione Tecnica

Bitwarden rispetta comunque i flussi matematici di **Registrazione** e **Autenticazione**:

1. Riceve il Challenge dal server.
    
2. Verifica l'utente (tramite PIN/Biometria dell'app o Master Password).
    
3. Firma il challenge con la chiave privata (che possiede decifrata temporaneamente in RAM).
    
4. Invia la firma al server.
    

La matematica sottostante è identica; cambia solo l'architettura di fiducia (fiducia nel chip fisico vs fiducia nella crittografia del vault software).