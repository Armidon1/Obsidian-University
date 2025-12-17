# Autenticazione: Un'Introduzione

**Tags:** #engineering #cybersecurity #authentication #sicurezza_informatica #biometria

## 1. Definizione e Scenario Base

L'[[Authentication]] è un pilastro della sicurezza informatica. Lo scenario tipico per comprendere questo processo coinvolge tre attori astratti:

- **Alice:** Il soggetto che ha bisogno di provare la sua identità per accedere a un servizio, un'informazione o una risorsa.
    
- **Bob:** Il sistema o l'entità che deve essere certo dell'identità di Alice prima di concedere l'accesso.
    
- **Trudy:** L'intruso che tenta di impersonare Alice.
    

### Definizione Formale

L'autenticazione è il processo volto a stabilire e verificare che un soggetto che tenta di accedere a un sistema sia lo stesso soggetto che si è originariamente registrato.

Questo avviene validando uno o più fattori di autenticazione rispetto a dati di riferimento fidati acquisiti durante la fase di registrazione.

> [!tip] Exam Focus
> 
> È fondamentale distinguere tra identificazione legale e autenticazione informatica. L'autenticazione aumenta la "garanzia" (assurance) che l'identità dichiarata sia valida, ma non fornisce un'identificazione assoluta.
> 
> $$\text{Identificazione Assoluta} \neq \text{Autenticazione}$$

### Autenticazione nell'interazione umana

I concetti informatici derivano da metodi che usiamo quotidianamente:

- **Riconoscimento diretto:** Riconoscere qualcuno dall'aspetto o dalla voce (biometria naturale).
    
- **Confronto fisico:** Una guardia confronta il viso di una persona con la foto sul badge (verifica di un token).
    
- **Conoscenza condivisa:** Un'azienda accetta come prova dell'identità la conoscenza di un dato segreto, come la data di scadenza della carta di credito.
    

---

## 2. Il Ciclo di Vita dell'Autenticazione

L'autenticazione non è un evento isolato, ma un processo strutturato in 5 fasi fondamentali che si ripetono nel tempo:

1. **Registrazione (Enrollment):** Il soggetto crea le credenziali o registra le informazioni necessarie presso il sistema.
    
2. **Archiviazione Credenziali (Storage):** Il sistema salva i dati in modo sicuro (tramite hash, cifratura o hardware dedicato) per usarli come riferimento futuro.
    
3. **Tentativo di Autenticazione:** Il soggetto presenta le proprie credenziali al momento dell'accesso.
    
4. **Verifica:** Il sistema convalida le credenziali presentate confrontandole con i dati di riferimento archiviati.
    
5. **Gestione Accesso e Ciclo di Vita:** Include la concessione o il diniego dell'accesso, ma anche la gestione di rinnovi, revoche o cambi di credenziali.
    

---

## 3. Logica e Presupposti (World Assumptions)

Nella progettazione dei sistemi di sicurezza, si opera secondo logiche precise che definiscono come il sistema deve comportarsi di fronte all'incertezza.

Closed World Assumption (Ipotesi del Mondo Chiuso):

- Si presume che ciò che non è noto essere vero, sia falso.
- In sicurezza, questo principio si traduce nella "Negation as failure": se il sistema non può provare che un utente è autorizzato (predicato vero), deve assumere che non lo sia (falso).

$$\text{Unknown}(P) \implies \text{False}(P)$$

Ambiente Chiuso (Aziende/Casa):

- In ambienti controllati, spesso si utilizza una Terza Parte Fidata (chiamata convenzionalmente Carole) per distribuire le informazioni necessarie all'autenticazione tra le parti (Alice e Bob), garantendo che entrambi possano fidarsi l'uno dell'altro.

---

## 4. Umani vs Computer

Esiste una differenza sostanziale tra autenticare una macchina e una persona, dovuta alle diverse capacità di memoria e calcolo.

|**Soggetto**|**Capacità**|**Limitazioni**|
|---|---|---|
|**Computer**|Può memorizzare segreti di alta qualità (numeri casuali lunghi) ed eseguire operazioni crittografiche complesse.|Deve essere programmato e non ha iniziativa propria.|
|**Umano**|Memoria limitata (difficoltà con stringhe lunghe e casuali).|Deve ricordare solo una password (spesso breve).|

Interazione:

- Nei sistemi moderni, la workstation esegue le operazioni crittografiche complesse per conto dell'utente. La password umana serve solo per "sbloccare" l'accesso a una chiave crittografica di qualità superiore (ad esempio, decifrare una chiave privata RSA salvata sul disco).

---

## 5. Fattori di Autenticazione

Per autenticare le persone si utilizzano diverse categorie di "prove", comunemente chiamate fattori di autenticazione.

1. **What you know (Cosa sai):** Password, PIN, risposte a domande segrete.
    
2. **What you have (Cosa hai):** Smart card, token hardware, smartphone.
    
3. **Who you are (Chi sei):** Caratteristiche biometriche.
    
4. **Where you are (Dove sei):** Indirizzo di rete o posizione GPS.
    

> [!failure] Common Pitfall
> 
> Basarsi esclusivamente sul fattore "Where you are" (es. indirizzo IP) è considerato debole a causa della facilità con cui è possibile falsificare l'origine del traffico (IP Spoofing).

### Focus: Password e Minacce

- **Per gli umani:** Le password sono chiavi brevi ("low-quality secrets"), spesso facili da indovinare.
    
- **Per i computer:** Gestiscono chiavi lunghe ("high-quality secrets"), che non vengono mai salvate in chiaro ma sempre cifrate o hashate.
    
- **Minaccia Principale:** Il **[[Login Trojan Horse]]**. Questa tecnica prevede che un attaccante simuli fedelmente la finestra di login del sistema operativo o di un servizio per indurre l'utente a digitare le proprie credenziali, che vengono poi catturate e inviate all'attaccante.
    

---

## 6. Biometria (Who you are)

La biometria utilizza caratteristiche fisiche o comportamentali uniche per l'autenticazione.

A differenza delle password, l'accuratezza biometrica non è assoluta (binaria), ma probabilistica. L'efficacia di un sistema biometrico si misura tramite i tassi di errore:

- **False Positive:** Il sistema accetta erroneamente un impostore.
    
- **False Negative:** Il sistema rifiuta erroneamente un utente legittimo.
    

### Esempi e Criticità

- **Impronte Digitali (Fingerprinting):**
    
    - _Rischi:_ Possibilità di utilizzare impronte sintetiche o, in scenari estremi, dita di persone decedute.
        
    - _Instabilità:_ Le impronte possono degradarsi o cambiare nel tempo (es. bambini in crescita, lavori manuali usuranti).
        
- **Voce:**
    
    - _Rischi:_ Vulnerabile ai **[[Replay attack]]** (uso di registrazioni della voce dell'utente).
        
    - _Instabilità:_ La voce può essere alterata da malattie (raffreddore), rumore di fondo o scarsa qualità del microfono/telefono.
        
- **Dinamica della digitazione (Keystroke timing):**
    
    - Si basa sul ritmo di digitazione unico di ogni persona.
        
    - È considerato sicuro perché è fisiologicamente impossibile per un attaccante digitare stabilmente a una velocità superiore al proprio limite naturale per imitare qualcun altro.
        
- **Firma Autografa (Handwritten signature):**
    
    - L'analisi puramente visiva è debole.
        
    - I sistemi moderni (es. in banca) utilizzano tablet che registrano non solo il tratto, ma anche la **pressione** e la **velocità** di scrittura, rendendo la firma molto difficile da falsificare.

---
# Autenticazione: Modelli di Attaccante

**Tags:** #engineering #cybersecurity #authentication #threat_modeling #attacker_model

## 1. Perché modellare l'Attaccante?

Nel design di un sistema sicuro, non è sufficiente implementare tecnologie difensive in modo generico. È necessario definire chiaramente chi è il nemico attraverso la modellazione dell'attaccante. Questo processo serve a:

- **Chiarire l'ambito della protezione:** Definire esplicitamente contro chi il sistema si sta difendendo.
    
- **Migliorare il design del protocollo:** Selezionare metodi di autenticazione che rispondano ai rischi reali, evitando complessità inutili per scenari a basso rischio.
    
- **Guidare la strategia di mitigazione:** Prioritizzare i controlli di sicurezza per gli attacchi più probabili e dannosi.
    

> [!tip] Exam Focus
> 
> Concentrare le risorse su minacce realistiche è più efficace che cercare di coprire ogni singolo "edge case" teorico.

---

## 2. Profilazione: Le Dimensioni dell'Attaccante

Un attaccante non è un'entità astratta, ma viene classificato in base a cinque dimensioni principali:

1. **Motivazione:**
    
    - Guadagno finanziario (frode, furto).
        
    - Spionaggio (aziendale o politico).
        
    - Sabotaggio o interruzione dei servizi.
        
    - Vendetta personale o ideologica.
        
2. **Risorse:**
    
    - Potenza computazionale (cluster CPU/GPU per brute force, botnet).
        
    - Tempo e pazienza per campagne a lungo termine.
        
    - Budget per acquistare exploit o dati rubati.
        
3. **Competenze (Skills):**
    
    - **Script Kiddies:** Bassa competenza, utilizzano tool pre-fatti.
        
    - **Professionisti / APT (Advanced Persistent Threats):** Alta competenza, capacità di sviluppare attacchi su misura.
        
4. **Livello di Accesso:**
    
    - Fisico (accesso diretto al dispositivo o alla rete).
        
    - Rete Locale (LAN).
        
    - Remoto (accesso basato su Internet).
        
5. **Persistenza:**
    
    - Attacco opportunistico "una tantum".
        
    - Intrusione continua e mirata.
        

---

## 3. Livelli di Capacità (Cosa possono fare?)

Oltre al profilo, è fondamentale capire come l'avversario interagisce con il sistema:

- **Avversario Passivo:**
    
    - Osserva il traffico di rete senza alterarlo.
        
    - Colleziona metadati (timestamp, indirizzi IP) per inferire comportamenti.
        
- **Avversario Attivo:**
    
    - Inietta, modifica o cancella messaggi di autenticazione.
        
    - Esegue il replay di credenziali valide precedentemente catturate.
        
- **Insider Threat (Minaccia Interna):**
    
    - Possiede credenziali legittime o accessi privilegiati.
        
    - Può aggirare molte difese perimetrali esterne.
        
    - Potrebbe collaborare con attaccanti esterni (collusione).
        

---

## 4. Vettori di Attacco Principali

Queste sono le tecniche concrete utilizzate per violare i sistemi di autenticazione:

### Attacchi Generici

- **Furto di Credenziali:**
    
    - Phishing diretto agli utenti.
        
    - Malware o keylogger che registrano la digitazione.
        
    - Furto di credenziali salvate da dispositivi compromessi.
        
    - Riutilizzo di coppie username/password provenienti da vecchi data breach (Credential Stuffing).
        
- **Brute Force e Guessing:**
    
    - Tentativi online (spesso limitati da rate limits).
        
    - Cracking offline di database di password hashate rubati.
        
- **Replay Attacks:**
    
    - Cattura di dati di autenticazione validi e reinvio successivo.
        
    - Sfrutta la mancanza di controlli sulla freschezza della sessione.
        
- **Man-in-the-Middle (MITM):**
    
    - Intercettazione e modifica di sessioni di autenticazione in tempo reale.
        
    - Utilizzo di certificati falsi o router compromessi.
        

### Minacce Specializzate

- **Biometric Spoofing:** Creazione di impronte artificiali, modelli facciali 3D o uso di foto/video.
    
- **Token Cloning:** Duplicazione fisica di smartcard o copiatura dei "seed" (semi) per gli OTP. Sfrutta protezioni hardware deboli.
    
- **Session Hijacking:** Furto di cookie di sessione o token tramite malware o XSS per bypassare la ri-autenticazione.
    
- **Social Engineering:** Impersonare utenti legittimi chiamando il supporto IT o ingannare l'utente per farsi rivelare le credenziali.
    

---

## 5. Scenari Realistici ed Esempi

Esempi concreti di applicazione dei modelli di attacco:

1. **Wi-Fi Hotspot non sicuro:**
    
    - Un attaccante passivo cattura traffico non cifrato.
        
    - Un attaccante attivo inietta pagine di login false.
        
2. **Abuso di Insider Aziendale:**
    
    - Un amministratore accede ad aree riservate senza controlli di autorizzazione adeguati.
        
    - Manipola i log di audit per nascondere le proprie tracce.
        
3. **Dispositivo Mobile Compromesso:**
    
    - Il malware bypassa l'autenticazione biometrica facendo il replay di dati salvati.
        
    - L'utente non è consapevole che il dispositivo agisce da proxy per l'attaccante.
        

---

## 6. Mappatura: Minacce vs Difese

Questa sezione è cruciale per la progettazione: ad ogni attacco corrisponde una specifica contromisura tecnica.

La relazione tra attacco e difesa può essere schematizzata così:

**1. Contro [[Man-in-the-Middle (MITM)]]:**

- Utilizzo di **Autenticazione Mutua** (Client e Server si autenticano a vicenda).
    
- Protocollo **[[TLS]]** con _certificate pinning_.
    

**2. Contro [[Replay Attack]]:**

- Uso di **[[Nonce]]** (numeri usati una volta sola) e **Timestamp** nei messaggi.
    
- **OTP** (One-Time Passwords) e token a vita breve.
    

**3. Contro Furto di Credenziali:**

- Implementazione della **[[MFA (Multi-Factor Authentication)]]**.
    
- Uso di token hardware o app mobili sicure.
    

**4. Contro Brute Force:**

- **Rate limiting** (limitazione tentativi) e blocco account (account lockouts).
    
- Hashing delle password con **[[Salt (Cryptographic)]]** e iterazioni multiple (es. bcrypt, Argon2).
    

**5. Contro Biometric Spoofing:**

- **Liveness detection** (rilevamento della "vivezza") e challenge-response biometrici.
    

---

## 7. Presupposti di Sicurezza e Design

Quando si progetta un sistema, bisogna partire da assunzioni realistiche e spesso pessimistiche.

> [!failure] Common Pitfall
> 
> Mai assumere che la rete sia sicura o che l'utente si comporti perfettamente.

- **Le reti non sono fidate:** Assumere sempre che il traffico possa essere monitorato da parti non autorizzate.
    
- **Gli endpoint possono essere compromessi:** [[Malware-Based Attacks|Malware]], [[Rootkits]] o configurazioni errate dei dispositivi sono rischi reali.
    
- **Gli utenti sono fallibili:** Sono suscettibili a [[Phishing]] e ingegneria sociale.
    
- **Le implementazioni sono imperfette:** Bug software, generatori di numeri casuali deboli e configurazioni errate sono la norma.
    

### Conclusione sul Design

Non esiste una soluzione unica ("One size does not fit all"). Bisogna definire "chi, cosa, come" prima di progettare le difese e aggiornare regolarmente i modelli di minaccia, poiché il panorama degli attacchi evolve nel tempo.

La sicurezza dell'autenticazione è la somma di: solidità del protocollo + sicurezza dell'endpoint + resilienza del fattore umano.

---

# Autenticazione: Scenari e Tecniche

**Tags:** #engineering #cybersecurity #authentication #crittografia #protocolli #timestamp #nonce

## 1. Scenari di Autenticazione

Quando parliamo di autenticazione basata sulla conoscenza di chiavi crittografiche, identifichiamo tre scenari architetturali principali:

1. **Segreto Condiviso (Simmetrico, cioè [[Symmetric Encryption]]):** Alice e Bob condividono una chiave segreta ($K_{AB}$). È il modello più semplice ma difficile da scalare.
    
2. **[[Trusted Third Party (TTP)]]:** Alice e Bob non condividono nulla direttamente, ma entrambi condividono una chiave con un'autorità centrale, **Carole** (Authentication Server). Carole agisce da ponte.
    
3. **Chiave Pubblica (Asimmetrico, cioè [[Public-Key Encryption]]):** Gli utenti possiedono una coppia di chiavi (Pubblica/Privata). L'autenticazione avviene dimostrando il possesso della chiave privata senza rivelarla.
    

---

## 2. La Gestione delle Chiavi

La sicurezza dei protocolli dipende intrinsecamente dalla qualità e dalla gestione delle chiavi utilizzate.

### Classificazione Temporale

- **Master Keys (Statiche):** Chiavi a lungo termine. Se compromesse, il danno è grave e persistente.
    
- **Ephemeral Keys (Dinamiche):** Chiavi di sessione, usate per breve tempo. La loro compromissione limita i danni alla singola sessione.
    

### Qualità della Chiave

Una chiave sicura deve essere indistinguibile da una sequenza casuale di bit.

- **Lunghezza:** Più è lunga, maggiore è lo sforzo computazionale richiesto per un attacco forza bruta.
    
- **Generazione:** Devono essere create tramite **[[KDF (Key Derivation Function)]]** o scambiate in modo sicuro (es. protocolli tipo [[Diffie-Hellman Key Exchange]]).
    

> [!tip] Exam Focus
> 
> Ricorda: Le chiavi pubbliche sono le uniche che non richiedono segretezza, ma richiedono autenticità (devo essere sicuro che la chiave pubblica di Alice sia davvero di Alice).

---

## 3. Tecniche Fondamentali (Anti-Replay)

Per garantire che un messaggio di autenticazione sia "fresco" (freshness) e non una riproduzione di un vecchio messaggio intercettato da un attaccante ([[Replay attack]]), si usano tre tecniche principali.

### A. Timestamp (Marche Temporali)

Si include nel messaggio una stringa che indica l'ora corrente (fino ai millisecondi).

- **Funzionamento:** Chi riceve il messaggio controlla se il Timestamp rientra in un **intervallo di validità** accettabile (finestra temporale).
    
- **Debolezza 1:** Richiede che gli orologi di Mittente e Destinatario siano perfettamente **sincronizzati**.
    
- **Debolezza 2:** Un attaccante veloce può effettuare un replay del messaggio se riesce a farlo entro l'intervallo di validità.
    

> [!abstract] TSA (Timestamping Authorities)
> 
> Per dare valore legale o forte ai timestamp, si usano le TSA. Queste autorità producono un timestamp fidato e lo firmano digitalmente insieme all'hash del documento.
> 
> $$\text{Token} = \text{Sign}_{TSA}(\text{Hash}(Data) \ || \ \text{Time})$$

### B. Nonce (Number used Once)

È un numero casuale generato da chi vuole verificare l'identità (il Verificatore) e inviato a chi deve autenticarsi.

- **Scopo:** Creare una "sfida" (Challenge) sempre nuova.
    
- **Requisito:** Serve un generatore di numeri casuali crittograficamente sicuro (**[[CS-PRNG (Cryptographically Secure PRNG)|CS-PRNG]]**).
    
- **Vantaggio:** Garantisce freschezza assoluta.
    
- **Utilizzo Misto:** Spesso i Nonce vengono accoppiati ai Timestamp per evitare di dover memorizzare storici infiniti di numeri usati: il nonce serve per l'unicità, il timestamp limita la durata della memorizzazione del nonce.
    

### C. Sequence Numbers (Numeri di Sequenza)

Ispirati al protocollo [[TCP]].

- Si numerano i messaggi in ordine progressivo.
    
- È difficile per un attaccante inserire un messaggio falso nella sequenza corretta senza essere rilevato.
    
- Quando il numero raggiunge il massimo valore, i parametri di sicurezza vengono spesso rinegoziati.
    

---

## 4. Cifratura vs Autenticazione

Un errore concettuale comune è pensare che cifrare un messaggio garantisca automaticamente la sua autenticità.

> [!failure] Common Pitfall
> 
> La Cifratura NON garantisce l'Autenticità.

- **Scenario di Attacco:** Trudy può intercettare un messaggio cifrato scambiato tra Alice e Bob in passato e reinviarlo oggi. Bob riuscirà a decifrarlo (perché la chiave è valida), credendo che sia un nuovo comando inviato da Alice.
    
- **Soluzione:** È necessario implementare meccanismi specifici di [[Integrity]] e [[Authentication]] (come [[HMAC]] o [[Digital Signature]]) oltre alla cifratura.

---

# Autenticazione a Chiave Simmetrica

**Tags:** #engineering #cybersecurity #authentication #symmetric_key #protocols #challenge_response

## 1. Concetti Fondamentali

In questo scenario, l'autenticazione si basa su un segreto condiviso.

- **Presupposto:** Alice e Bob condividono una chiave segreta simmetrica, denotata come $K_{Alice-Bob}$.
    
- **Meccanismo:** Per autenticarsi, una parte deve dimostrare di conoscere la chiave $K$ senza inviarla mai in chiaro sulla rete.
    

### Tipologie di Direzionalità

1. **One-way (Unilaterale):** Una parte (Alice) prova la sua identità all'altra (Bob). Bob rimane anonimo/non verificato.
    
2. **Two-way (Mutual Authentication):** Entrambe le parti si autenticano a vicenda. Alice prova di essere Alice, e Bob prova di essere Bob.
    
    - _Nota:_ L'autenticazione mutua è più robusta se avviene **quasi simultaneamente** piuttosto che come due autenticazioni unilaterali separate.
        

---

## 2. Protocollo Challenge-Response (Sfida-Risposta)

È il metodo standard per l'autenticazione basata su Nonce (numeri casuali usati una volta sola).

Il flusso logico (Unilaterale: Alice si autentica a Bob) è il seguente:

1. **Alice** dichiara di essere Alice.
    
2. **Bob** invia una sfida (Nonce $R$) ad Alice.
    
3. **Alice** cifra la sfida con la chiave condivisa e la rispedisce.
    

$$\begin{align} 1. \ A &\rightarrow B : \text{"I am Alice"} \\ 2. \ B &\rightarrow A : R \\ 3. \ A &\rightarrow B : K_{Alice-Bob}\{R\} \end{align}$$

> [!abstract] Math Analysis
> 
> Bob decifra il messaggio ricevuto. Se il risultato corrisponde a $R$, allora chi ha inviato il messaggio possiede necessariamente la chiave $K_{Alice-Bob}$.
> 
> Questo protocollo può essere implementato anche usando [[HMAC]] al posto della cifratura reversibile.

### Vulnerabilità: Password Guessing

Se la chiave $K_{Alice-Bob}$ è derivata da una password umana (quindi debole/breve), questo protocollo è vulnerabile.

- Un attaccante che ascolta (Eavesdropper) cattura la coppia $(R, K\{R\})$.
    
- Può tentare un attacco di forza bruta offline ([[Dictionary Attack]]) provando a cifrare $R$ con tutte le password possibili finché non ottiene l'output catturato. Questo è un attacco di tipo **[[Known-Plaintext Attack (KPA)]]**.
    

---

## 3. Autenticazione Basata su Timestamp

Per ridurre il numero di messaggi (da 3 a 1), si può usare il tempo al posto di una sfida interattiva.

Alice invia direttamente il Timestamp cifrato:

$$A \rightarrow B : \text{"I am Alice"}, \ K_{Alice-Bob}\{\text{Timestamp}\}$$

> [!tip] Vantaggi e Svantaggi
> 
> - **Pro:** Molto efficiente (nessuno stato intermedio, meno messaggi).
>     
> - **Contro:** Richiede che gli orologi di Alice e Bob siano **sincronizzati**. Bob deve accettare il messaggio solo se il timestamp rientra in una piccola "finestra temporale" (Clock Skew) per evitare i Replay Attack.
>     

---

## 4. Attacchi Avanzati e Difese

### A. [[Replay attack]] (Attacco a Ponte)

Un attaccante $T$ (Trudy) si posiziona tra Alice e Bob. $T$ non conosce la chiave, ma fa da "ponte" trasparente.

1. $T$ finge di essere Alice con Bob.
    
2. Quando Bob invia la sfida $R$, $T$ la gira ad Alice (fingendo di essere Bob o un server legittimo).
    
3. Alice risolve la sfida (cifra $R$) e la rispedisce a $T$.
    
4. $T$ gira la soluzione a Bob.
    
5. **Risultato:** Bob accetta $T$ come se fosse Alice.
    

> [!failure] Defense Strategy
> 
> Per prevenire il Relay Attack serve la Distance Bounding o il Channel Binding:
> 
> - Verifica della prossimità fisica.
>     
> - Legare la risposta a caratteristiche del canale che $T$ non può inoltrare.
>     
> - Autenticazione Mutua (Alice deve verificare che sta parlando con il vero Bob prima di rispondere alla sfida).
>     

### B. Reflection Attack (Attacco di Riflessione)

Questo attacco sfrutta i protocolli di Autenticazione Mutua Ottimizzata dove si cerca di risparmiare messaggi.

Se Alice e Bob usano lo stesso protocollo simmetrico, Trudy può ingannare Bob facendogli risolvere la sua stessa sfida.

**Scenario:** Trudy vuole impersonare Alice verso Bob.

1. Trudy inizia la **Sessione 1** con Bob: "Sono Alice".
    
2. Bob invia la sfida $R_1$.
    
3. Trudy (che non ha la chiave) apre una **Sessione 2** simultanea con Bob, fingendo di essere Alice o riflettendo il segnale.
    
4. Trudy invia $R_1$ a Bob (nella Sessione 2) come se fosse la _sua_ sfida.
    
5. Bob risolve $R_1$ (perché deve autenticarsi nella Sessione 2) e invia la soluzione $K\{R_1\}$ a Trudy.
    
6. Trudy prende $K\{R_1\}$ e la usa per chiudere la **Sessione 1**.
    

> [!abstract] Come prevenirlo?
> 
> L'attacco funziona perché la sfida da A$\to$B è identica alla sfida da B$\to$A. Bisogna rompere questa simmetria:
> 
> 1. **Chiavi diverse:** Usare $K_{AB}$ per una direzione e una chiave diversa (es. $-K_{AB}$ o $K_{AB}+1$) per l'altra.
>     
> 2. **Formato diverso:** Il "Challenger" usa numeri pari, il "Responder" usa numeri dispari. In questo modo Bob non accetterà mai di risolvere una sfida "pari" se lui stesso ne ha inviata una "pari".
>     

---

## 5. Autenticazione Mutua Ottimizzata

Per evitare di scambiare troppi messaggi (un approccio ingenuo ne richiederebbe 5), si possono accorpare i dati.

### Protocollo a 3 Messaggi

1. **Alice $\to$ Bob:** "Sono Alice", invia la sua sfida $R_A$.
    
2. **Bob $\to$ Alice:** Invia la sua sfida $R_B$ **E** la soluzione alla sfida di Alice $K\{R_A\}$.
    
3. **Alice $\to$ Bob:** Invia la soluzione alla sfida di Bob $K\{R_B\}$.
    

In questo modo, in soli 3 passaggi, entrambe le parti sono autenticate. Tuttavia, questo design deve essere attentamente analizzato per evitare le vulnerabilità di riflessione descritte sopra.

---

# Autenticazione con Terza Parte Fidata (TTP)

**Tags:** #engineering #cybersecurity #authentication #TTP #Needham-Schroeder #Kerberos #KDC

## 1. Il Concetto di Terza Parte Fidata

Quando il numero di utenti in una rete cresce, l'autenticazione a coppie (Alice-Bob) basata su chiavi simmetriche diventa ingestibile.

- **Problema della Scalabilità:** Se ogni utente dovesse condividere una chiave segreta con tutti gli altri, servirebbero $\frac{N(N-1)}{2}$ chiavi (complessità quadratica).
    
- **Soluzione:** Introdurre una **Trusted Third Party (TTP)**, spesso chiamata **KDC (Key Distribution Center)** o Server di Autenticazione (Carole).
    

### Architettura a Stella

- Ogni utente condivide una chiave segreta **solo** con il server TTP ($K_{AC}$ per Alice, $K_{BC}$ per Bob).
    
- **Vantaggio:** Gestione della fiducia semplificata.
    
- **Rischio:** La TTP è un **Single Point of Failure**. Se compromessa o irraggiungibile, tutto il sistema si ferma.
    

---

## 2. Obiettivi e Modello dell'Attaccante

L'obiettivo del protocollo è permettere ad Alice e Bob di autenticarsi a vicenda e stabilire una **Session Key ($K$)** sicura per comunicare.

### Requisiti di Sicurezza

1. Solo Alice, Bob e la TTP devono conoscere $K$.
    
2. $K$ deve essere una chiave fresca (random, non riutilizzata).
    
3. Alice e Bob devono essere certi dell'identità l'uno dell'altro.
    

### Modello di Attaccante (Trudy)

Trudy è potente ma ha dei limiti:

- **Poteri:** Può sniffare, fare spoofing, essere un utente legittimo del sistema (quindi può parlare con la TTP), può avviare sessioni multiple concorrenti.
    
- **Limiti:** Non può indovinare numeri random (Nonce) generati da Alice o Bob. **Non conosce le chiavi a lungo termine** ($K_{AC}, K_{BC}$) degli altri utenti. Non può decifrare messaggi senza chiave in tempo utile.
    

---

## 3. Evoluzione del Protocollo (Tentativi e Fallimenti)

Per arrivare a un protocollo sicuro, si passa attraverso versioni vulnerabili.

### Tentativo 1: Protocollo Base

Alice chiede alla TTP una chiave per parlare con Bob.

1. $A \rightarrow TTP: (A, B)$
    
2. $TTP \rightarrow A: K_{AC}(K), \ K_{BC}(K)$
    
3. Alice decifra la sua parte, ottiene $K$, e gira a Bob la parte cifrata per lui.
    

> [!failure] Vulnerabilità (MITM & Identity Misbinding)
> 
> Trudy può intercettare la richiesta. Se Trudy è un utente legittimo, può farsi passare per Bob o Alice in vari passaggi, poiché i messaggi cifrati non contengono l'identità del destinatario esplicita all'interno della cifratura.

### Tentativo 2: Protocollo Modificato (Identity Inclusion)

Per mitigare il problema precedente, la TTP include l'identità nel messaggio cifrato.

$$TTP \rightarrow A: K_{AC}(K, B), \ K_{BC}(K, A)$$

Tuttavia, questo è ancora vulnerabile ai Replay Attack. Trudy può registrare un vecchio messaggio valido e reinviarlo in seguito per costringere Alice o Bob a usare una vecchia chiave compromessa.

---

## 4. Protocollo Needham-Schroeder (NS)

Questo è il protocollo fondamentale che risolve i problemi precedenti introducendo i **Nonce** (numeri casuali usati una volta sola) per garantire la freschezza della sessione.

I Passaggi del Protocollo 1

1. Richiesta: Alice invia alla TTP la richiesta per Bob e un Nonce ($N_A$).
    
    $$A \rightarrow C: A, B, N_A$$
    
2. Generazione Chiavi e Ticket: La TTP (Carole/C) genera la session key $K$. Invia ad Alice un messaggio cifrato contenente $K$, il nonce originale (per provare che la risposta è fresca) e un "Ticket" cifrato per Bob.
    
    $$C \rightarrow A: K_{AC}(N_A, B, K, \underbrace{K_{BC}(K, A)}_{\text{Ticket per Bob}})$$
    
3. Inoltro del Ticket: Alice decifra il messaggio, verifica $N_A$, estrae $K$ e invia il Ticket a Bob.
    
    $$A \rightarrow B: K_{BC}(K, A)$$
    
4. Sfida di Bob: Bob decifra il Ticket, ottiene $K$ e conosce l'identità di Alice. Per verificare che Alice sia viva ora (e non sia un replay), Bob genera un nuovo Nonce $N_B$ cifrato con $K$.
    
    $$B \rightarrow A: K(N_B)$$
    
5. Risposta di Alice: Alice decifra $N_B$, lo decrementa (o modifica in modo predicibile) e lo rimanda cifrato.
    
    $$A \rightarrow B: K(N_B - 1)$$
    

> [!abstract] Concetto Chiave
> 
> Il Passaggio 5 prova a Bob che Alice possiede la chiave di sessione $K$ adesso. Nessun attaccante potrebbe generare $K(N_B-1)$ senza conoscere $K$.

---

## 5. L'Attacco a Needham-Schroeder (Attacco Denning-Sacco)

Nonostante l'uso dei Nonce, il protocollo originale ha una vulnerabilità critica scoperta nel 1981, legata alla compromissione di una vecchia chiave di sessione.

Scenario dell'Attacco 2

Supponiamo che Trudy abbia registrato una vecchia sessione tra Alice e Bob e che, in qualche modo, sia riuscita a scoprire la vecchia chiave di sessione $K'$ (compromessa).

1. Replay del Ticket: Trudy attende che Alice non sia connessa e invia a Bob il vecchio Ticket registrato (Passaggio 3 del protocollo originale).
    
    $$T(A) \rightarrow B: K_{BC}(K', A)$$
    
2. **Inganno di Bob:** Bob decifra il ticket. Essendo cifrato con la sua chiave segreta $K_{BC}$ (che non è cambiata), lo ritiene valido. Pensa che Alice voglia parlargli usando la chiave $K'$.
    
3. Sfida: Bob invia la sfida con un nuovo Nonce $N'$, cifrata con $K'$ (che Trudy conosce!).
    
    $$B \rightarrow T: K'(N')$$
    
4. Risposta: Trudy può facilmente decifrare $N'$, calcolare $N'-1$ e ricifrarlo con $K'$.
    
    $$T \rightarrow B: K'(N'-1)$$
    

Risultato: Bob è convinto di parlare con Alice su un canale sicuro, ma sta parlando con Trudy.

Causa: Bob non ha modo di verificare la freschezza del Ticket generato dalla TTP. Non sa se il ticket è stato creato 1 secondo fa o 1 anno fa.

---

## 6. Needham-Schroeder Espanso (o Variante)

Per risolvere l'attacco di replay, bisogna garantire la freschezza anche verso Bob. Ci sono due approcci principali che hanno portato allo sviluppo di protocolli moderni come **Kerberos**.

Variante con Timestamp 3

Si introducono timestamp ($t$) nei messaggi cifrati dalla TTP.

$$C \rightarrow A: K_{AC}(..., t, ...), \ K_{BC}(..., t, ...)$$

Bob accetta il ticket solo se il timestamp è recente (richiede orologi sincronizzati).

Variante con Handshake Espanso 4

Bob deve contattare la TTP o inviare un nonce alla TTP prima di accettare la chiave.

1. Alice dice "Voglio parlarti".
    
2. Bob invia un Nonce $N_B$ ad Alice e alla TTP.
    
3. La TTP include $N_B$ nel ticket per Bob.
    
4. Quando Bob riceve il ticket e trova il suo $N_B$ all'interno, ha la prova matematica che il ticket è stato generato _dopo_ che lui ha inviato la richiesta.
    

> [!tip] Exam Focus
> 
> Il protocollo Needham-Schroeder è la base teorica di Kerberos, il sistema di autenticazione standard in Windows e Active Directory. Kerberos usa pesantemente i Timestamp per evitare i problemi di replay senza dover fare troppi scambi di messaggi (handshake).