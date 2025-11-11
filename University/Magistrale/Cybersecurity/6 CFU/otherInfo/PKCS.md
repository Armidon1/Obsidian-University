# 📜 PKCS (Public-Key Cryptography Standards)

### Definizione

**PKCS** è l'acronimo di **Public-Key Cryptography Standards**, una suite di specifiche (standard) sviluppate e pubblicate da **RSA Laboratories** a partire dagli anni '90.

Il loro scopo è **promuovere l'interoperabilità** tra diversi sistemi crittografici. Non sono un algoritmo, ma un insieme di **"planimetrie" (blueprints)** che definiscono formati e protocolli comuni per l'implementazione della crittografia a chiave pubblica.

### Perché è Fondamentale per un Ingegnere

Senza PKCS, ogni fornitore (Microsoft, Apple, OpenSSL) implementerebbe la crittografia in modo proprietario e incompatibile. PKCS standardizza le risposte a domande ingegneristiche critiche come:

- "Come deve essere formattato un file di chiave privata per essere archiviato in modo sicuro?"
    
- "Qual è la struttura di un messaggio firmato digitalmente?"
    
- "Come si applica il padding a un messaggio prima di cifrarlo con RSA?"
    
- "Come si deriva una chiave crittografica da una password?"
    

Quando vedi un file `.p12`, `.pem` o hai a che fare con il padding `OAEP`, stai usando un'implementazione di uno standard PKCS.

### Standard PKCS Chiave (Esempi Pratici)

Sebbene esistano 15 standard, molti sono obsoleti. Questi sono quelli che un ingegnere incontra più di frequente:

|**Standard**|**Nome Comune**|**Scopo Principale (Cosa fa?)**|
|---|---|---|
|**PKCS #1**|**RSA Cryptography Standard**|**FONDAMENTALE.** Definisce le basi matematiche di RSA. Specifica come formattare le chiavi RSA e come implementare la cifratura e la firma, inclusi gli schemi di **padding** cruciali (es. `OAEP` per la cifratura, `PSS` per le firme).|
|**PKCS #5**|**Password-Based Cryptography Standard**|Definisce i metodi per **derivare chiavi crittografiche** da una password. La sua specifica più famosa è **PBKDF2** (Password-Based Key Derivation Function 2).|
|**PKCS #7**|**Cryptographic Message Syntax (CMS)**|Definisce un formato generico per dati crittografici, in particolare **messaggi firmati** e **certificati**. È la base per i file `.p7b` e `.p7c` e per le firme S/MIME.|
|**PKCS #8**|**Private-Key Information Syntax Standard**|**ESSENZIALE.** Specifica il formato standard per archiviare i file di **chiave privata** (cifrati o non cifrati). Quando vedi un file `-----BEGIN PRIVATE KEY-----`, stai guardando un PKCS #8 (spesso codificato in PEM).|
|**PKCS #10**|**Certification Request Syntax Standard**|Definisce il formato per una **CSR (Certificate Signing Request)**. È il file che generi e invii a una Certificate Authority (CA) per richiedere un certificato SSL/TLS.|
|**PKCS #12**|**Personal Information Exchange Syntax Standard**|**MOLTO COMUNE.** Definisce un formato di archivio (spesso protetto da password) per raggruppare una **chiave privata** con la sua corrispondente **catena di certificati pubblici**. È il formato dei file `.p12` e `.pfx`.|
A seguito verrà mostrata una panoramica di tutti i PKCS:
#### Panoramica degli Standard PKCS

Questi standard, sviluppati da RSA Laboratories, definiscono formati per la crittografia a chiave pubblica sicura.

|**Standard**|**Titolo**|**Funzione / Descrizione**|**Stato / Adozione**|
|---|---|---|---|
|**PKCS #1**|RSA Cryptography Standard|Cifratura RSA, firme e padding (come OAEP, PSS).|Ampiamente usato; parti adottate in **RFC 8017**.|
|**PKCS #3**|Diffie-Hellman Key Agreement|Formato per lo scambio di chiavi Diffie–Hellman.|Obsoleto; sostituito da standard IETF.|
|**PKCS #5**|Password-Based Cryptography|Definisce [[PBKDF1]], [[PBKDF2]] (derivazione della chiave).|Ampiamente usato; parte di **RFC 8018**.|
|**PKCS #6**|Extended Certificate Syntax|Definisce estensioni per i certificati.|Obsoleto; superato da **X.509v3**.|
|**PKCS #7**|Cryptographic Message Syntax|Formato per dati firmati/criptati ([[S-MIME\|S\MIME]]).|Superato da CMS (**RFC 5652**).|
|**PKCS #8**|Private Key Information Syntax|Standard per l'archiviazione di chiavi private (criptate o meno).|Ampiamente usato (OpenSSL, Java).|
|**PKCS #9**|Selected Attribute Types|Definisce attributi da usare in altri standard PKCS.|Ancora rilevante.|
|**PKCS #10**|Certificate Request Syntax|Formato per le Richieste di Firma di Certificato (CSR).|Ubiquo in TLS/PKI.|
|**PKCS #11**|Cryptographic Token Interface (Cryptoki)|API per interagire con hardware crittografico (HSM, smartcard).|Mantenuto attivamente da OASIS.|
|**PKCS #12**|Personal Information Exchange Syntax|Contenitore per certificati e chiavi private (file .p12, .pfx).|Ancora ampiamente usato (Windows, browser).|
|**PKCS #15**|Cryptographic Token Information Format|Formato per archiviare oggetti crittografici su token.|Usato nell'infrastruttura delle smartcard.|

c'è anche PKCS#13 che tratta della Crittografia Ellittica, che permette di ottenere la stessa sicurezza di una chiave da 1 milione di bit con semplicemente un migliaio di bit e questo aiuta molto con le [[Performance]].

---

## Una Panoramica di PKCS (Parte 2)

I **Public-Key Cryptography Standards (PKCS)** erano una serie di standard sviluppati da RSA Laboratories per garantire l'**interoperabilità** tra diversi venditori per le operazioni crittografiche. Sebbene molti siano stati superati o integrati negli RFC (Request for Comments) dell'IETF, hanno costituito la base fondamentale per molti protocolli di sicurezza oggi in uso.

Ecco una panoramica di diversi standard chiave della collezione.

---

## PKCS #3 — Accordo sulla Chiave Diffie-Hellman

- **Scopo:** Standardizzare lo **scambio di chiavi Diffie-Hellman (DH)**.
    
- **Meccanismo:** Definiva i parametri e la codifica per il protocollo DH, dove due parti generano ciascuna una coppia di chiavi pubblica/privata e le usano per calcolare un segreto condiviso ($g^{ab} \pmod p$). Questo segreto condiviso viene poi usato per derivare le chiavi di sessione simmetriche.
    
- **Stato e Contesto:**
    
    - **Obsoleto.** Questo standard è storicamente importante come il primo a standardizzare DH, ma è stato superato da standard IETF più robusti come **RFC 2631** (che fa riferimento a ANSI X9.42).
        
    - Le definizioni moderne dei parametri DH (ad esempio, gruppi di primi specifici) sono definite in standard come **RFC 3526**.
        
- **Applicazioni:** Era un componente fondamentale per protocolli come il TLS legacy (ora deprecato) e IPsec (che usa ancora i "gruppi" DH per l'accordo sulla chiave).
    

---

## PKCS #5 — Cifratura Basata su Password (PBE)

- **Scopo (Motivazione):** Risolve un problema umano fondamentale: gli utenti ricordano **password** (che hanno bassa entropia e sono spesso deboli), non lunghe chiavi crittografiche (che hanno alta entropia). PKCS #5 fornisce un metodo sicuro per **derivare una chiave forte da una password debole**.
    
- **Meccanismo (Derivazione della Chiave):**
    
    - Specifica le **Password-Based Key Derivation Functions (PBKDFs)**.
        
    - [[PBKDF1]] (legacy) e [[PBKDF2]] (lo standard moderno) sono i più famosi.
        
    - [[PBKDF2]] "stira" (key stretching) una password mescolandola con un **Salt** (un valore casuale unico) ed eseguendola attraverso una funzione pseudo-casuale (come HMAC-SHA256) migliaia di volte (il **conteggio delle iterazioni**).
        
    - **Funzione:** `Chiave Derivata = PBKDF2(password, salt, iterazioni, lunghezza_chiave_output)`
        
    - Questo processo è _deliberatamente lento_ per rendere gli attacchi a forza bruta contro la password computazionalmente impraticabili. Le KDF moderne come `bcrypt`, `scrypt` e `Argon2` si basano su questo stesso concetto.
        
- **Applicazioni:**
    
    - **Sicurezza Wi-Fi:** WPA/WPA2 usano PBKDF2 per derivare la chiave di cifratura di rete dalla password Wi-Fi.
        
    - **Gestori di Password:** Usato per criptare la tua cassaforte di password (es. KeePass, 1Password).
        
    - **Cifratura del Disco:** Usato per derivare la chiave che sblocca un disco rigido cifrato.
        
    - **PKCS #12:** Usato per proteggere con password i file delle chiavi private.
        

---

## PKCS #8 — Sintassi per le Informazioni sulla Chiave Privata

- **Scopo:** Una sintassi standard (che usa ASN.1) per **archiviare le informazioni sulla chiave privata**. Fornisce un formato comune che diversi sistemi e software (come OpenSSL, Java, .NET) possono tutti comprendere.
    
- **Struttura:** Definisce due strutture principali:
    
    1. **`PrivateKeyInfo`:** Un contenitore non criptato che contiene il tipo di chiave (RSA, EC, ecc.) e i dati della chiave stessa (l'`OCTET STRING`).
        
    2. **`EncryptedPrivateKeyInfo`:** Un contenitore per una chiave privata _criptata_. Specifica l'algoritmo di cifratura (tipicamente un PBE da **PKCS #5**) e i dati della chiave criptata.
        
- **Applicazioni:**
    
    - Questo è il formato che si vede nei **file PEM** usati per TLS/HTTPS:
        
        - `-----BEGIN PRIVATE KEY-----` (PKCS #8 non criptato)
            
        - `-----BEGIN ENCRYPTED PRIVATE KEY-----` (PKCS #8 criptato, protetto da password)
            
    - Essenziale per l'archiviazione sicura delle chiavi e l'interoperabilità in tutti i moderni sistemi PKI.
        

---

## PKCS #9 — Tipi di Attributi Selezionati

- **Scopo:** Fornisce **estensibilità** per altri standard PKCS. Non è un protocollo in sé, ma una _libreria di definizioni_ per "attributi" che possono essere allegati a oggetti come certificati o chiavi private. Gli attributi sono come informazioni aggiuntive.
    
- **Esempi di Attributi:**
    
    - `emailAddress`
        
    - `unstructuredName`
        
    - `challengePassword` (una password usata in un PKCS #10 Certificate Signing Request (CSR) per autenticare una richiesta di rinnovo o revoca).
        
    - Permette anche attributi personalizzati tramite **Object Identifiers (OID)**.
        
- **Applicazioni:** Usato per fornire informazioni di identità più ricche all'interno dei certificati X.509 e dei CSR PKCS #10.
    

---

## PKCS #11 — Interfaccia per Token Crittografici (Cryptoki)

- **Scopo:** Questo è uno standard **API (Application Programming Interface) in linguaggio C**, non un formato di file. Fornisce un modo indipendente dal venditore per il software di _parlare con_ dispositivi crittografici hardware.
    
- **Concetti Chiave (Architettura):**
    
    - **HSM (Hardware Security Module):** Il dispositivo fisico o cloud che protegge le chiavi.
        
    - **Cryptoki (Crypto Key API):** Il "driver" o software di interfaccia.
        
    - **Slot:** Un'interfaccia o lettore (es. un lettore di smart card, una porta USB).
        
    - **Token:** Il dispositivo crittografico stesso (es. una smart card, un token USB).
        
    - **Sessione:** Una connessione attiva tra l'applicazione e il token.
        
    - **Oggetti:** Le chiavi, i certificati o i dati memorizzati sul token. Le chiavi sono spesso contrassegnate come "non esportabili", il che significa che possono essere _usate_ ma mai _estratte_.
        
- **Applicazioni:**
    
    - PKI aziendale (usando HSM per proteggere le CA root).
        
    - Login con smart card per sistemi operativi.
        
    - Esecuzione sicura di firme digitali o terminazione TLS (il server web parla all'HSM tramite PKCS #11 per firmare i dati).
        
    - HSM Cloud (ad es. in AWS, Azure) presentano un'interfaccia PKCS #11.
        

---

## PKCS #12 — Sintassi per lo Scambio di Informazioni Personali

- **Scopo:** Definisce un **formato contenitore** (un singolo file) per raggruppare informazioni crittografiche correlate. È comunemente noto con le sue estensioni di file: **.pfx** o **.p12**.
    
- **Struttura:** Un file PKCS #12 è una "valigia digitale" che tipicamente contiene:
    
    1. Una **Chiave Privata** (che è essa stessa solitamente criptata usando PBE PKCS #5).
        
    2. Il corrispondente **Certificato di Chiave Pubblica** (X.509).
        
    3. La "catena di fiducia": eventuali certificati intermedi e root.
        
- **Utilizzo:**
    
    - **Backup e Trasporto:** Questo è il modo più comune per **esportare** un certificato e la sua chiave privata da un server e **importarlo** su un altro (ad esempio, quando si sposta un sito web su un nuovo server).
        
    - Usato da browser, sistemi operativi e client VPN/Email per importare credenziali utente e Windows.
        

---

## PKCS #15 — Formato delle Informazioni sul Token Crittografico

- **Scopo:** Questo standard definisce il **formato del file system** _sul_ token crittografico. Assicura che un token (come una carta d'identità elettronica nazionale) di un venditore possa essere compreso e utilizzato da software di un altro venditore.
    
- **PKCS #11 vs. PKCS #15 (La Distinzione Chiave):**
    
    - **PKCS #15 (Archiviazione):** Questo è _come i dati sono strutturati_ sul token (ad esempio, la struttura delle directory, i nomi dei file e le regole di controllo degli accessi).
        
    - **PKCS #11 (Accesso):** Questa è l'_API usata da un'applicazione_ per leggere, scrivere e usare gli oggetti memorizzati nel formato PKCS #15.
        
- **Applicazioni:**
    
    - Carte d'identità elettroniche nazionali.
        
    - Passaporti digitali.
        
    - Tessere sanitarie.
        
    - Carte di accesso aziendali.