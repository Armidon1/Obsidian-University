# Infrastruttura a Chiave Pubblica (PKI)

**Tags:** #ingegneria #security #pki #crittografia #trust_models

## 1. Motivazione e Problema Fondamentale

La crittografia moderna (RSA, ECC, EdDSA) è matematicamente solida. Gli attacchi odierni raramente rompono la matematica sottostante.

Il vero problema è la distribuzione delle chiavi.

Se Alice vuole parlare con Bob usando la crittografia a chiave pubblica, deve ottenere la chiave pubblica di Bob.

- **Il rischio:** Se l'attaccante sostituisce la chiave di Bob con la propria, può intercettare tutto (Man-in-the-Middle).
    
- **La soluzione:** Serve un sistema per garantire che una certa chiave pubblica appartenga davvero a una specifica identità.
    

> [!failure] Common Pitfall
> 
> La crittografia protegge il canale, ma la PKI protegge l'identità. Senza PKI, potresti avere una connessione cifrata perfetta, ma con la persona sbagliata.

---

## 2. Modelli di Fiducia a Confronto

Esistono diversi modi per stabilire se fidarsi di una chiave pubblica.

### A. Web of Trust (WoT)

Nato con PGP. È un modello **decentralizzato**.

- **Funzionamento:** Gli utenti firmano le chiavi degli altri utenti.
    
- **Logica:** "Se mi fido di Alice, e Alice si fida di Bob, allora io mi fido di Bob".
    
- **Pro:** Nessun punto singolo di fallimento.
    
- **Contro:** Complesso, soggettivo e non scala a livello globale.
    

### B. TOFU (Trust On First Use)

Usato da SSH.

- **Funzionamento:** La prima volta che ti colleghi, accetti la chiave presentata. Il sistema la memorizza.
    
- **Logica:** Se la chiave cambia in futuro, ricevi un avviso.
    
- **Contro:** Sei vulnerabile al primo collegamento (First-contact MITM).
    

### C. PKI (X.509)

Il modello standard per il web (HTTPS). È un modello **gerarchico centralizzato**.

- **Funzionamento:** Ci sono autorità centrali (CA) che garantiscono per gli altri.
    
- **Pro:** Scalabile globalmente, validazione automatica.
    
- **Contro:** Se la CA centrale viene compromessa, il danno è enorme (Single Point of Failure).
    

---

## 3. Architettura e Componenti della PKI

La PKI è un sistema composto da hardware, software, policy e procedure. Ecco i tre pilastri fondamentali:

![[SCREEN_SLIDE_16_COMPONENTS]]

> [!abstract] Visual Analysis
> 
> What to look at: Lo schema mostra il flusso di fiducia che parte dalla Root CA, passa per la Intermediate CA e arriva all'End-Entity.
> 
> Meaning:
> 
> 1. **Certification Authority (CA):** È la terza parte fidata. Emette e gestisce i certificati.
>     
> 2. **Registration Authority (RA):** È l'ente che verifica l'identità (il "buttafuori"). Controlla i documenti prima di dire alla CA di emettere il certificato.
>     
> 3. **Repository:** Dove vengono pubblicati i certificati e le liste di revoca (es. directory pubbliche).
>     

### Technical Logic: The Trust Chain

**La catena di validazione segue questa logica gerarchica:**

$$\text{Trust Anchor (Root)} \rightarrow \text{Intermediate CA} \rightarrow \text{End-Entity (User/Server)}$$

> [!abstract] Math Analysis
> 
> Ogni entità firma digitalmente il certificato del livello inferiore. Il client verifica la catena risalendo dal basso fino alla Root CA, di cui si fida a priori.

---

## 4. La Gerarchia delle CA

Per sicurezza e scalabilità, le CA non usano la loro chiave principale per tutto.

### Root CA (Trust Anchor)

- È il vertice della piramide.
    
- Il suo certificato è **Self-Signed** (firmato da se stessa).
    
- La chiave privata è tenuta **Offline** in moduli hardware sicuri (HSM) per evitare furti.
    
- È pre-installata nei browser e nei sistemi operativi (Trust Store).
    

### Intermediate CA

- Delegata dalla Root CA.
    
- Emette i certificati finali o delega ad altre subordinate.
    
- **Scopo:** Se una Intermediate viene compromessa, la Root può revocarla senza dover sostituire la Root stessa su milioni di dispositivi.
    

---

## 5. Validazione e Revoca

Un certificato può diventare non valido prima della scadenza (es. furto della chiave privata). Esistono due metodi per controllare lo stato:

### CRL (Certificate Revocation List)

- Una "lista nera" di certificati revocati, firmata dalla CA.
    
- **Problema:** Le liste diventano enormi e non sono aggiornate in tempo reale (ritardo di propagazione).
    

### OCSP (Online Certificate Status Protocol)

- Verifica in tempo reale.
    
- Il client interroga un server (OCSP Responder): "Questo certificato è valido?".
    
- Risposta: **Sì / No**.
    
- Più efficiente della CRL.
    

---

## 6. Trust Store e Rischi

Il **Trust Store** è il database delle Root CA fidate, mantenuto dai vendor (Apple, Microsoft, Google, Mozilla).

> [!tip] Exam Focus
> 
> Un dispositivo si fida di molte Root CA simultaneamente (100-200+). Basta che UNA sola di queste venga compromessa per poter generare certificati falsi per qualsiasi sito web.

### Case Study: DigiNotar (2011)

Un esempio reale di disastro PKI.

- Una CA olandese (DigiNotar) fu compromessa.
    
- Gli attaccanti emisero certificati falsi per `*.google.com`.
    
- **Impatto:** MitM su larga scala contro utenti Gmail in Iran.
    
- **Conseguenza:** I browser rimuoverono DigiNotar dai Trust Store, portando l'azienda al fallimento.
    

> [!failure] Common Pitfall
> 
> Malware e Trust Store: Alcuni malware installano una Root CA malevola nel Trust Store del PC vittima. Questo permette al malware di intercettare tutto il traffico HTTPS (anche bancario) senza che il browser mostri alcun errore di sicurezza.

---

# Struttura dei Certificati X.509 e Encoding (ASN.1, DER, PEM)

**Tags:** #ingegneria #security #pki #x509 #asn1 #encoding

## 1. Perché l'Encoding è Fondamentale?

I certificati digitali sono contenitori di identità digitale. Affinché la sicurezza funzioni globalmente, dobbiamo garantire che un certificato creato su un server Linux venga letto identicamente da un client Windows o da uno smartphone Android.

L'**encoding rigoroso** serve a garantire:

- **Compatibilità:** Funzionamento su piattaforme diverse (Little Endian vs Big Endian).
    
- **Interpretazione Univoca:** Non ci devono essere dubbi su dove finisce un campo e inizia l'altro.
    
- **Verifica della Firma:** Se cambia anche solo un bit nella rappresentazione binaria del certificato, la verifica della firma crittografica fallisce.
    

---

## 2. ASN.1 (Abstract Syntax Notation One)

Prima di parlare di bit e byte, dobbiamo definire la **struttura logica** dei dati. Per questo si usa **ASN.1**.

### Cos'è ASN.1?

È un linguaggio formale (standard ISO/ITU-T) nato negli anni '80 per definire strutture dati in modo indipendente dall'hardware e dal linguaggio di programmazione.

> [!tip] Exam Focus
> 
> ASN.1 è solo la sintassi astratta. Definisce cosa c'è nel certificato (es: "qui c'è un numero intero", "qui c'è una data"), ma non come scrivere questi dati in binario sul disco.

**I vantaggi chiave sono:**

- **Platform-neutral:** Ignora se la CPU è a 32 o 64 bit.
    
- **Language-independent:** Funziona con C, Java, Python, Go.
    
- **Flessibile:** Supporta versioning e retro-compatibilità.
    

---

## 3. La Struttura X.509 in ASN.1

Lo standard X.509 definisce il certificato come una sequenza ordinata di tre macro-campi.

**Here is the exact ASN.1 definition shown in the slides:**

Plaintext

```
Certificate ::= SEQUENCE {
    tbsCertificate      TBSCertificate,
    signatureAlgorithm  AlgorithmIdentifier,
    signatureValue      BIT STRING
}
```

> [!abstract] Code Analysis
> 
> - **tbsCertificate (To Be Signed):** Contiene tutte le informazioni (Chi è il soggetto, chi è l'emittente, la chiave pubblica, la scadenza). È la parte che verrà hashata.
>     
> - **signatureAlgorithm:** Dice quale algoritmo usare (es. SHA256 con RSA).
>     
> - **signatureValue:** È la firma digitale vera e propria (una stringa di bit).
>     

---

## 4. Il Modello a Tre Livelli

Per capire come funziona un certificato, immagina una struttura a cipolla o a livelli gerarchici.

![[SCREEN_SLIDE_37_LAYERS]]

> [!abstract] Visual Analysis
> 
> What to look at: La distinzione tra Concetto, Sintassi e Rappresentazione.
> 
> Meaning:
> 
> 1. **X.509 (Concettuale):** Definisce l'oggetto "Certificato" e le sue regole di business.
>     
> 2. **ASN.1 (Sintassi):** Definisce la struttura astratta dei dati (Tipi, Campi).
>     
> 3. **DER/PEM (Encoding):** Definisce la rappresentazione concreta (i bit reali sul filo).
>     

---

## 5. Regole di Encoding: BER vs DER

Una volta definita la struttura con ASN.1, dobbiamo trasformarla in bit. Esistono le "Basic Encoding Rules" (BER), ma per la crittografia non bastano.

### Il problema del BER (Basic Encoding Rules)

Il BER è flessibile: permette di codificare lo stesso dato in modi diversi.

- _Esempio:_ Un booleano `TRUE` potrebbe essere codificato come `0x01` o `0xFF`.
    
- **Problema:** Se la rappresentazione non è unica, l'hash del file cambia. Se l'hash cambia, la firma digitale si rompe.
    

### La soluzione: DER (Distinguished Encoding Rules)

Il **DER** è un sottoinsieme "stretto" del BER.

- **Regola d'oro:** Esiste **UNA sola** codifica valida per ogni struttura ASN.1.
    
- **Determinismo:** Garantisce che chiunque codifichi quel certificato otterrà esattamente la stessa sequenza di byte.
    

> [!failure] Common Pitfall
> 
> Non usare mai BER o codifiche non canoniche per firmare dati. La verifica della firma fallirà perché il verificatore potrebbe ricostruire i byte in modo leggermente diverso, ottenendo un hash diverso.

---

## 6. Formati dei File: DER vs PEM

Nella pratica operativa (configurando server web o firewall), incontrerai due tipi di file per i certificati. Sono la stessa cosa, cambia solo il "contenitore".

### Formato DER (.cer, .crt, .der)

- **Natura:** Binario puro.
    
- **Vantaggi:** Compatto, efficiente, pronto per la verifica della firma.
    
- **Codice macchina:** `30 82 03 9F ...` (Illeggibile per l'umano).
    

### Formato PEM (.pem, .crt, .key)

È lo standard di fatto per il web (Apache, Nginx) e per l'invio via email.

- **Natura:** Testo ASCII.
    
- **Struttura:** È il file DER codificato in **Base64** con header e footer.
    

**Here is the exact implementation structure shown in the slides:**

Plaintext

```
-----BEGIN CERTIFICATE-----
MIIDdzCCAI+gAwIBAgIEb1Cb...
(Base64 content)
-----END CERTIFICATE-----
```

> [!abstract] Code Analysis
> 
> Questo formato aumenta la dimensione del file di circa il 33%, ma permette il copia-incolla sicuro nei file di configurazione o nelle email senza corrompere i bit.

### Tabella Comparativa Rapida

|**Caratteristica**|**DER**|**PEM**|
|---|---|---|
|**Encoding**|Binario|ASCII (Base64 del DER)|
|**Uso Principale**|Java, Windows, Trust Stores interni|Linux, Web Server, Email|
|**Leggibilità**|Macchina|Umano (parzialmente)|
|**Sicurezza**|Pronto per l'uso|Deve essere decodificato in DER prima dell'uso|

---

# Struttura dei Certificati X.509: Campi Fondamentali

**Tags:** #ingegneria #security #pki #x509 #rfc5280 #certificati

## 1. Panoramica: La Struttura TBSCertificate

Il cuore di un certificato digitale è la struttura dati chiamata **TBSCertificate** (To Be Signed Certificate). Questa è la parte che contiene tutte le informazioni critiche e che viene firmata digitalmente dalla Certification Authority (CA).

È definita nello standard **RFC 5280**. Questi campi catturano tre aspetti essenziali:

1. **Identità** (Chi è il soggetto).
    
2. **Materiale della Chiave** (La chiave pubblica).
    
3. **Validità** (Per quanto tempo ci fidiamo).
    

![[SCREEN_SLIDE_43_CORE_FIELDS]]

> [!abstract] Visual Analysis
> 
> What to look at: L'immagine mostra i 6 campi "Core" che circondano il certificato.
> 
> Meaning: Questi sono i pilastri della fiducia digitale: Versione, Serial Number, Issuer (Emittente), Validità, Subject (Soggetto), Public Key.

---

## 2. Analisi Dettagliata dei Campi

### A. Version (Versione)

Indica quale versione dello standard X.509 stiamo usando.

- **v1:** Formato originale (pochi campi, niente estensioni).
    
- **v2:** Ha aggiunto identificatori unici (usato raramente).
    
- **v3:** Lo standard dominante oggi. Supporta le **Estensioni** (fondamentali per la sicurezza moderna).
    

**Codifica interna:**

$$\text{Encoded as INTEGER: } \{0 = v1, \ 1 = v2, \ 2 = v3\}$$

### B. Serial Number (Numero Seriale)

È un identificativo **UNICO** assegnato dalla CA a ogni certificato che emette.

- Deve essere un intero positivo molto grande (generato casualmente).
    
- **Scopo:** È fondamentale per la revoca. Le CRL (Certificate Revocation List) elencano i certificati revocati usando proprio questo numero.
    

> [!failure] Common Pitfall
> 
> Riutilizzo del Seriale: Se una CA assegna lo stesso numero seriale a due certificati diversi (anche per errore), il meccanismo di revoca si rompe e la validazione fallisce.

### C. Signature Algorithm

Dichiara quale algoritmo crittografico è stato usato per firmare il certificato.

Questo campo appare due volte (dentro il TBSCertificate e fuori) e devono combaciare.

**Esempi tipici:**

Plaintext

```
sha256WithRSAEncryption
ecdsaWithSHA384
```

### D. Validity (Periodo di Validità)

Definisce la finestra temporale in cui il certificato è considerato affidabile. Se siamo fuori da questo intervallo, il certificato viene **respinto**.

**The time format definition is:**

$$\text{Generalized Time format: YYYYMMDDHHMMSSZ} \quad (\text{Z} = \text{UTC})$$

Composto da due sottocampi:

- **notBefore:** Data di inizio validità.
    
- **notAfter:** Data di scadenza.
    

> [!tip] Exam Focus
> 
> Sicurezza e Durata:
> 
> - **Root CA:** Durano 15-25 anni.
>     
> - **Certificati TLS Server:** Oggi durano massimo **398 giorni** (circa 1 anno).
>     
> - **Principio:** Una validità più breve migliora la sicurezza (riduce l'esposizione al rischio e forza la rotazione delle chiavi).
>     

---

## 3. Identità: Issuer e Subject

Questi campi usano una struttura gerarchica derivata dallo standard X.500, chiamata **Distinguished Name (DN)**.

### Struttura del DN

Un DN è una sequenza di attributi chiamati **RDN** (Relative Distinguished Names).

**Common Attributes:**

- **C** = Country (Paese, es. IT, US)
    
- **O** = Organization (Azienda)
    
- **OU** = Organizational Unit (Dipartimento, opzionale)
    
- **CN** = Common Name (Nome comune)
    
- **L** = Locality (Città)
    
- **ST** = State/Province
    

### Issuer (Emittente)

Identifica l'entità che ha **firmato** il certificato (solitamente la CA).

- In un certificato **Root CA**, il campo _Issuer_ è identico al campo _Subject_ (perché è auto-firmato, "Self-Signed").
    

### Subject (Soggetto)

Identifica l'entità a cui appartiene la chiave pubblica (es. il sito web o l'utente).

> [!example] Professor's Note on TLS
> 
> Nel web moderno, il campo CN (Common Name) è deprecato per la validazione degli hostname. I browser oggi controllano rigorosamente il campo SAN (Subject Alternative Name), che è un'estensione, non il CN.

---

## 4. Subject Public Key Info

Questo è il "carico utile" del certificato. Contiene due elementi inscindibili:

1. **L'Algoritmo:** I parametri della chiave (es. "Questa è una chiave RSA a 2048 bit" o "Questa è una chiave Ellittica sulla curva P-256").
    
2. **La Chiave Pubblica:** La sequenza di bit vera e propria.
    

**Structure defined via OID (Object Identifier):**

Plaintext

```
AlgorithmIdentifier ::= SEQUENCE {
    algorithm   OBJECT IDENTIFIER,
    parameters  ANY DEFINED BY algorithm OPTIONAL
}
SubjectPublicKey ::= BIT STRING
```

---

## 5. Sintesi delle Relazioni

Per capire come tutto si lega insieme:

1. L'**Issuer** firma digitalmente l'intera struttura TBSCertificate.
    
2. Il **Serial Number** identifica univocamente quel certificato nello scope dell'Issuer.
    
3. La **Validity** crea il vincolo temporale.
    
4. Il **Subject** lega la chiave pubblica a un'identità reale.
    

**Equazione Logica del Certificato:**

$$\text{Certificato} = \text{Identità} + \text{Chiave Pubblica} + \text{Tempo} + \text{Firma dell'Issuer}$$

---

# Estensioni dei Certificati X.509 (Versione 3)

**Tags:** #ingegneria #security #pki #x509 #rfc5280 #estensioni

## 1. Perché servono le Estensioni?

I campi base del certificato (Subject, Issuer, Validità) non bastano per le esigenze della PKI moderna.

Introdotte con X.509 v3, le estensioni servono a:

- Supportare **multi-domini** (es. un certificato valido per `www.google.com` e `mail.google.com`).
    
- Definire **restrizioni d'uso** (es. "questa chiave serve solo per firmare email, non per cifrare").
    
- Controllare la **catena di fiducia** (deleghe e path validation).
    

### Struttura di un'Estensione

Ogni estensione segue un modello standard definito nella RFC 5280 composto da tre elementi:

**Here is the exact structure logic:**

Plaintext

```
Extension ::= SEQUENCE {
    extnID      OBJECT IDENTIFIER, -- OID univoco (es. KeyUsage)
    critical    BOOLEAN DEFAULT FALSE,
    extnValue   OCTET STRING -- Il contenuto codificato in ASN.1
}
```

> [!abstract] Code Analysis
> 
> - **extnID:** È l'etichetta che dice "che tipo" di estensione è.
>     
> - **critical:** Un flag booleano (Vero/Falso) fondamentale per la sicurezza.
>     
> - **extnValue:** I dati veri e propri dell'estensione.
>     

---

## 2. Il Flag "Critical": Regola d'Oro

Ogni estensione deve essere marcata esplicitamente come **Critica** o **Non Critica**. Questo determina come il client (browser o OS) deve comportarsi se **non riconosce** l'estensione.

- **Critical = TRUE:**
    
    - Se il sistema non capisce l'estensione, **DEVE rifiutare** l'intero certificato.
        
    - Si usa per vincoli di sicurezza (es. "Questo certificato non è una CA").
        
- **Critical = FALSE:**
    
    - Se il sistema non capisce l'estensione, può **ignorarla** e procedere.
        
    - Si usa per informazioni informative (es. "Dove scaricare la CRL").
        

> [!failure] Common Pitfall
> 
> Marcare erroneamente un'estensione critica come non critica crea buchi di sicurezza. Marcarne una informativa come critica crea problemi di interoperabilità (il certificato viene rifiutato senza motivo valido).

---

## 3. Identificatori della Chiave (Chain Building)

Come fa il browser a sapere quale CA ha firmato il certificato, specialmente se ci sono più CA con nomi simili? Usa gli identificatori univoci delle chiavi.

### Subject Key Identifier (SKI)

- Identifica la chiave pubblica contenuta **dentro** il certificato stesso.
    
- Solitamente è l'hash SHA-1 della chiave pubblica.
    

### Authority Key Identifier (AKI)

- Identifica la chiave pubblica dell'**emittente** (Issuer) che ha firmato il certificato.
    
- Serve per risalire al "genitore" nella catena di fiducia.
    

**The validation logic matches keys as follows:**

$$\text{Validation Link: } AKI_{\text{child}} \equiv SKI_{\text{parent}}$$

> [!abstract] Math Analysis
> 
> Per costruire la catena, il software cerca un certificato "genitore" il cui SKI corrisponda esattamente all'AKI del certificato "figlio" che sta analizzando. Questo metodo è molto più robusto del semplice confronto dei nomi.

---

## 4. Restrizioni d'Uso: Key Usage & EKU

Non tutte le chiavi devono poter fare tutto. Limitare l'uso riduce il rischio in caso di compromissione.

### Key Usage (KU)

Definisce le operazioni crittografiche di basso livello permesse.

- **digitalSignature:** Per handshake TLS o firma codice.
    
- **keyEncipherment:** Per scambiare chiavi di sessione (RSA).
    
- **crlSign / keyCertSign:** Permessi speciali **solo per le CA** (firmare CRL o altri certificati).
    

### Extended Key Usage (EKU)

Raffina il KU definendo lo scopo applicativo specifico (tramite OID).

- **Server Auth:** Autenticazione Server Web (HTTPS).
    
- **Client Auth:** Autenticazione Client (es. Smart Card).
    
- **Code Signing:** Firma di software.
    
- **Email Protection:** S/MIME.
    

> [!tip] Exam Focus
> 
> Se un certificato ha KeyUsage = digitalSignature ma viene usato per cifrare dati, la validazione fallisce. Le librerie TLS controllano rigorosamente questi campi.

---

## 5. Subject Alternative Name (SAN)

> [!tip] Exam Focus
> 
> CN vs SAN: Nel web moderno, il campo Common Name (CN) è deprecato per la validazione degli hostname. I browser guardano esclusivamente il SAN.

Il SAN permette di legare l'identità a più valori e tipi diversi:

- **DNS:** `www.example.com`, `example.net` (Multi-dominio).
    
- **Wildcard:** `*.example.com` (Tutti i sottodomini).
    
- **IP:** Indirizzi IP statici (es. per dispositivi IoT).
    
- **Email:** Indirizzi email per S/MIME.
    

---

## 6. Basic Constraints (Chi comanda?)

Questa estensione è cruciale per distinguere un "Capo" (CA) da un "Impiegato" (End-Entity).

### I Campi

1. **CA Boolean:** `TRUE` se il certificato appartiene a una CA, `FALSE` se è un utente/server.
    
2. **PathLenConstraint:** Numero massimo di CA subordinate che possono esistere sotto questa CA.
    

Risk Scenario:

Se un certificato utente non ha Basic Constraints o li ha settati male (es. manca il blocco CA=FALSE), un attaccante potrebbe usare quel certificato per firmare altri certificati falsi (diventando una CA canaglia).

> [!example] Professor's Example
> 
> Incidente Microsoft 2001: Un certificato intermedio fu emesso senza Basic Constraints corretti. L'attaccante lo usò come una CA "rogue" per generare certificati validi per qualsiasi dominio, compromettendo l'intera fiducia.

---

## 7. Altre Estensioni Importanti

Servono per gestire il ciclo di vita e le policy.

- **CRL Distribution Points (CRL DP):** Indica l'URL dove scaricare la lista dei certificati revocati.
    
- **Authority Information Access (AIA):**
    
    - Indica l'URL del server OCSP (validazione real-time).
        
    - Indica l'URL dove scaricare il certificato dell'Issuer (aiuta a ricostruire la catena se manca un pezzo).
        
- **Name Constraints:** Permette a una CA Enterprise di emettere certificati **solo** per un certo dominio (es. solo `*.unina.it`), limitando i danni in caso di compromissione.

---

# Gerarchie di Fiducia PKI e Catene di Certificati

**Tags:** #ingegneria #security #pki #trust_hierarchy #certificate_chain #root_ca

## 1. Root CA: L'Ancora di Fiducia (Trust Anchor)

Al vertice di ogni gerarchia PKI c'è la **Root CA**. Questa entità gode di una posizione unica perché non ha autorità superiori.

### Caratteristiche Fondamentali

- **Certificato Self-Signed:** Essendo l'autorità suprema, la Root CA firma il proprio certificato.
    
- **Punto di Partenza:** È l'origine assoluta della validazione. Se non ti fidi della Root, non ti fidi di nulla nella catena.
    
- **Trust Store:** I certificati Root non si scaricano "al volo" dalla rete; sono **pre-installati** e hardcoded nei Sistemi Operativi (Windows, macOS, Linux) e nei Browser (Firefox, Chrome).
    

**The logic of a self-signed certificate is:**

$$\text{Verify}(Pk_{Root}, \text{Signature}_{Root}, \text{Data}_{Root}) \rightarrow \text{True}$$

> [!abstract] Math Analysis
> 
> La firma sul certificato è generata usando la chiave privata corrispondente alla chiave pubblica contenuta nel certificato stesso. È una tautologia crittografica accettata per assioma (Trust Anchor).

---

## 2. Sicurezza e Distribuzione delle Root CA

Dato che una Root CA è il fondamento di tutto, la sua sicurezza è paranoica.

### Protezione delle Chiavi Root

- **Offline / Air-gapped:** Le chiavi private delle Root CA non sono mai connesse a Internet. Vivono in computer spenti o scollegati fisicamente dalla rete.
    
- **HSM (Hardware Security Modules):** Le chiavi sono custodite in hardware anti-manomissione.
    
- **Signing Ceremonies:** L'attivazione della chiave per firmare (ad esempio per creare una nuova Intermediate CA) è un evento fisico formale, registrato e controllato da più persone.
    

> [!failure] Common Pitfall
> 
> Impatto della Compromissione: Se la chiave privata di una Root CA viene rubata, l'intera gerarchia di fiducia crolla. Qualsiasi certificato emesso (passato, presente e futuro) diventa inaffidabile. L'unica soluzione è rimuovere la Root dai Trust Store globali, causando disservizi enormi.

---

## 3. Intermediate CAs: I Delegati Operativi

Per motivi di sicurezza e scalabilità, la Root CA non emette direttamente i certificati per i siti web o gli utenti finali. Delega questo compito alle **Intermediate CA**.

### Perché usare livelli intermedi?

1. **Risk Reduction:** Se un'Intermediate CA viene compromessa, basta revocare quel singolo ramo. La Root rimane sicura e offline.
    
2. **Scalabilità:** Permette di gestire ecosistemi enormi distribuendo il carico di emissione.
    
3. **Flessibilità Operativa:** Si possono creare Intermediate specializzate per scopi diversi (Policy Separation).
    

![[SCREEN_SLIDE_74_HIERARCHY]]

> [!abstract] Visual Analysis
> 
> What to look at: L'immagine mostra la struttura ad albero: una singola Root si dirama in molteplici Intermediate.
> 
> Meaning: La Root è il "tronco" statico e sicuro, le Intermediate sono i "rami" operativi che crescono e gestiscono le foglie (End-Entities).

### Intermediate Specializzate

Spesso le CA creano intermediari dedicati a funzioni specifiche per limitare i danni in caso di problemi:

- **TLS Intermediates:** Emettono solo certificati SSL/TLS per server HTTPS.
    
- **Code Signing Intermediates:** Emettono solo certificati per firmare software.
    
- **Document Signing Intermediates:** Per la firma legale o eID.
    

---

## 4. Tipi di Certificati nella Gerarchia

Possiamo classificare i certificati in base al loro ruolo nella catena:

|**Tipo Certificato**|**Emesso da**|**Ruolo**|
|---|---|---|
|**Root CA**|Se stesso (Self-signed)|Trust Anchor. Pre-installato.|
|**Intermediate CA**|Root CA o altra Intermediate|Costruisce la catena di fiducia.|
|**End-Entity**|Intermediate CA|Usato da Server, Client, App. È la "foglia" dell'albero.|

---

## 5. Validazione della Catena (Certificate Chain)

Quando un browser si collega a un sito (es. `google.com`), non riceve solo il certificato del sito, ma una **lista** di certificati.

### Il Processo di Validazione

Il client deve ricostruire il percorso di fiducia dal certificato del server fino a una Root che possiede nel suo Trust Store locale.

**The chain validation logic is recursive:**

$$\begin{align} 1. & \ \text{Check: } \text{EndEntity} \xrightarrow{\text{signed by}} \text{Intermediate}_1 \\ 2. & \ \text{Check: } \text{Intermediate}_1 \xrightarrow{\text{signed by}} \text{Intermediate}_2 \\ 3. & \ \dots \\ 4. & \ \text{Check: } \text{Intermediate}_N \xrightarrow{\text{signed by}} \text{Root}_{Trusted} \end{align}$$

> [!tip] Exam Focus
> 
> L'anello mancante: Il server deve inviare al client il certificato End-Entity E tutti i certificati Intermediate necessari. Non invia la Root (perché il client ce l'ha già). Se il server dimentica di inviare un Intermediate ("Intermediate missing"), il browser non riesce a collegare la foglia alla radice e mostra un errore di sicurezza.


---

# Catena di Fiducia e Gerarchie PKI

**Tags:** #ingegneria #security #pki #chain_of_trust #certificati #x509

## 1. Il Concetto di "Chain of Trust"

La **Chain of Trust** (Catena di Fiducia) è la sequenza verificabile di certificati che collega un'entità finale (es. un sito web) a una radice fidata (Root CA).

L'obiettivo è garantire l'autenticità tramite la validazione delle firme digitali a cascata. Se un solo anello della catena è rotto o non fidato, l'intera validazione fallisce.

### I Tre Attori della Catena

1. **End-Entity (Foglia):** Il certificato dell'utente finale (Server, Client, Code Signer). Non può emettere altri certificati.
    
2. **Intermediate CA (Ramo):** Autorità delegate che estendono la fiducia.
    
3. **Root CA (Radice):** L'ancora di fiducia (Trust Anchor), auto-firmata e pre-installata nel sistema.
    

---

## 2. Analisi dei Componenti della Gerarchia

### End-Entity Certificates

Sono le "foglie" dell'albero PKI.

- **Destinatari:** Server Web (HTTPS), Utenti (S/MIME), Sviluppatori (Code Signing).
    
- **Restrizioni:** Non hanno il potere di firmare altri certificati.
    
- **Estensioni Chiave:** Usano `Key Usage` e `Extended Key Usage` per definire cosa possono fare (es. "Solo autenticazione server").
    

### Intermediate Certificates

Sono i "delegati" della Root CA.

- **Scopo:** Migliorare la scalabilità e proteggere la Root (che rimane offline).
    
- **Caratteristica Tecnica:** Devono avere l'estensione `Basic Constraints` impostata su `CA=true`.
    
- **Path Length:** Possono avere vincoli sulla profondità della catena (quanti sotto-livelli possono creare).
    

### Root Certificates

Sono le "ancore" della sicurezza.

- **Auto-firmati:** L'emittente (Issuer) e il soggetto (Subject) coincidono.
    
- **Offline:** Le chiavi private sono custodite in HSM (Hardware Security Modules) isolati per sicurezza.
    
- **Rimozione:** Se una Root viene rimossa dal Trust Store, tutti i certificati che discendono da essa diventano immediatamente invalidi.
    

---

## 3. Visualizzazione e Validazione della Catena

La validazione non è magica, è un processo algoritmico preciso che collega i certificati padre-figlio.

![[SCREEN_SLIDE_88_CHAIN]]

> [!abstract] Visual Analysis
> 
> What to look at: Il diagramma a flusso verticale.
> 
> Meaning:
> 
> 1. Il browser vede `www.example.com` (End-Entity).
>     
> 2. Verifica che sia firmato da `Intermediate CA #1`.
>     
> 3. Verifica che `Intermediate CA #1` sia firmata da `Intermediate CA #2`.
>     
> 4. Verifica che `Intermediate CA #2` sia firmata da `Root CA`.
>     
> 5. Trova la `Root CA` nel suo archivio locale fidato (Trust Store). **Catena valida.**
>     

### Il Meccanismo Tecnico di Matching (SKI & AKI)

Per costruire la catena senza ambiguità (specialmente quando ci sono CA con nomi simili), si usano gli identificatori delle chiavi.

**The cryptographic link logic is:**

$$\text{AKI}_{\text{child}} \equiv \text{SKI}_{\text{parent}}$$

> [!abstract] Math Analysis
> 
> - **SKI (Subject Key Identifier):** L'impronta digitale univoca della chiave pubblica nel certificato.
>     
> - **AKI (Authority Key Identifier):** L'impronta della chiave pubblica dell'emittente (Issuer).
>     
> - **Regola:** Il software cerca un certificato padre il cui SKI corrisponda esattamente all'AKI del figlio.
>     

### Matching dei Nomi (Issuer/Subject)

Oltre alle chiavi, deve esserci coerenza nei nomi.

**Name Chaining Rule:**

$$\text{Issuer}_{\text{child}} \equiv \text{Subject}_{\text{parent}}$$

> [!tip] Exam Focus
> 
> La combinazione di Nome (DN) e Chiave (SKI/AKI) garantisce la consistenza strutturale e crittografica della catena.

---

## 4. Gestione della Lunghezza e Vincoli

Le catene possono essere lunghe, ma la complessità introduce rischi.

### Basic Constraints & Path Length

Per evitare che una CA intermedia deleghi potere all'infinito (o che un'entità finale si finga CA), si usano vincoli stretti.

**Logic for Basic Constraints:**

Plaintext

```
BasicConstraints ::= SEQUENCE {
    cA                      BOOLEAN DEFAULT FALSE,
    pathLenConstraint       INTEGER OPTIONAL
}
```

> [!abstract] Code Analysis
> 
> - **CA=true:** Abilita il certificato a firmarne altri.
>     
> - **pathLenConstraint:** Specifica il numero massimo di CA intermedie permesse sotto questo certificato. Se è 0, la CA può firmare solo End-Entities, non altre CA.
>     

---

## 5. Rischi e Best Practices

### Perché non fidarsi direttamente delle Intermedie?

> [!failure] Common Pitfall
> 
> Errore: Un amministratore installa manualmente una Intermediate CA nel Trust Store locale per "far funzionare le cose".
> 
> Rischio:
> 
> 1. Si bypassano le policy del fornitore (es. Microsoft/Apple/Mozilla).
>     
> 2. Se la Root revoca l'Intermediate, il sistema continua a fidarsi erroneamente dell'Intermediate perché è stata forzata come "Ancora".
>     
>     Regola: Fidati solo delle Root. Le Intermedie devono derivare la loro autorità, non possederla intrinsecamente.
>     

### Il Principio dell'Anello Debole (Weakest Link)

Una catena è forte quanto il suo anello più debole.

- Se una singola Intermediate CA viene compromessa, **tutta la sottostruttura** che dipende da essa è compromessa (potenziale MITM su vasta scala).
    
- Catene più lunghe = Superficie di attacco più ampia.
    

### Costruzione della Catena (Chain Building)

Se il server non invia tutti i certificati intermedi necessari durante l'handshake TLS, il client deve cercarli.

- Usa l'estensione **AIA (Authority Information Access)** che contiene l'URL dove scaricare il certificato dell'Issuer mancante.

---

# Ciclo di Vita del Certificato: La Revoca

**Tags:** #ingegneria #security #pki #revocation #crl #ocsp

## 1. Definizione e Scopo

La revoca è il processo formale di invalidazione di un certificato digitale prima della sua naturale data di scadenza.

È un meccanismo di sicurezza fondamentale: se una chiave viene compromessa oggi ma il certificato scade tra due anni, non possiamo aspettare. Dobbiamo "uccidere" quel certificato immediatamente.

### Motivi per la Revoca

- **Compromissione della Chiave Privata:** Il motivo più critico (es. furto, hack).
    
- **Cambiamento di Identità:** Il soggetto cambia nome, affiliazione aziendale o dominio.
    
- **Errore di Emissione:** La CA ha inserito dati errati nel certificato.
    
- **Cessazione:** L'organizzazione o il servizio non esistono più.
    

> [!failure] Common Pitfall
> 
> La revoca non è automatica. Lo stato di "revocato" deve essere esplicitamente pubblicato dalla CA e attivamente controllato dai client (browser, OS). Se il client non controlla, continuerà a fidarsi di un certificato compromesso.

---

## 2. Certificate Revocation Lists (CRL)

La CRL è il metodo tradizionale. È una "Lista Nera" contenente i certificati invalidati, firmata digitalmente dalla CA.

### Struttura della CRL

Definita in **ASN.1**, una CRL contiene metadati e l'elenco delle revoche.

**The structure includes specific time windows:**

$$\begin{align} \text{CRL} &= \{ \\ & \quad \text{Version, Issuer, Signature}, \\ & \quad \text{thisUpdate} \ (\text{Data emissione corrente}), \\ & \quad \text{nextUpdate} \ (\text{Data scadenza lista}), \\ & \quad \text{RevokedCertificates}: [ \\ & \qquad \{ \text{Serial Number}, \ \text{Revocation Date}, \ \text{Reason (opt)} \} \\ & \quad ] \\ \} \end{align}$$

> [!abstract] Math Analysis
> 
> - **nextUpdate:** È il campo vitale. Dice al client: _"Questa lista è valida fino a questa data"_. Se la data attuale supera `nextUpdate`, il client è obbligato a scaricare una nuova CRL fresca.
>     
> - **Serial Number:** La revoca si basa esclusivamente sul confronto dei numeri seriali.
>     

### Funzionamento Operativo

1. Il client legge l'estensione **CDP (CRL Distribution Point)** nel certificato.
    
2. Scarica la CRL (spesso via HTTP).
    
3. Verifica la firma della CA sulla lista.
    
4. Controlla se il seriale del certificato è presente nella lista.
    
    - **Presente** $\rightarrow$ Certificato non valido.
        
    - **Assente** $\rightarrow$ Certificato valido (o almeno non revocato).
        

### Limiti e Svantaggi

- **Dimensione (Size):** Le CRL possono pesare diversi Megabyte. Scaricarle rallenta notevolmente la prima connessione.
    
- **Latenza (Latency):** Tra l'emissione di una revoca e il `nextUpdate`, c'è una finestra temporale in cui i client potrebbero usare una lista vecchia (rischio di sicurezza).
    
- **Scalabilità:** Non adatto a sistemi real-time o dispositivi IoT.
    

---

## 3. Ottimizzazione: Delta CRL

Per ridurre il peso del download, si usano le **Delta CRL**.

- Invece di scaricare tutta la lista, si scarica solo un "patch" che contiene le modifiche (nuove revoche) rispetto all'ultima CRL completa.
    
- **Requisito:** Il client deve essere abbastanza intelligente da gestire e fondere insieme la CRL Base e la Delta CRL.
    

---

## 4. OCSP (Online Certificate Status Protocol)

Definito nella **RFC 6960**, OCSP supera i limiti delle liste statiche offrendo una verifica in tempo reale.

### Modello Request/Response

Invece di scaricare "tutta la lista dei cattivi", il client chiede lo stato di **uno specifico** certificato.

**The query logic is:**

$$\text{Client} \xrightarrow{\text{Serial Number}} \text{OCSP Responder (CA)} \xrightarrow{\text{Status Signed}} \text{Client}$$

**Le Risposte Possibili:**

1. **Good:** Il certificato è valido.
    
2. **Revoked:** Il certificato è revocato (non fidarti!).
    
3. **Unknown:** La CA non ha record di questo certificato (spesso trattato come errore).
    

![[SCREEN_SLIDE_105_OCSP_STRUCTURE]]

> [!abstract] Visual Analysis
> 
> What to look at: La struttura della risposta.
> 
> Meaning: La risposta OCSP è piccola, veloce e firmata digitalmente dal Responder per garantirne l'autenticità.

---

## 5. OCSP Stapling (La Soluzione Moderna)

L'OCSP standard ha due problemi: Privacy (la CA sa chi stai visitando) e Performance (il client deve fare una connessione extra alla CA).

L'OCSP Stapling risolve entrambi.

### Come funziona

1. È il **Server Web** (es. `google.com`) a contattare periodicamente la CA per chiedere il proprio stato.
    
2. La CA risponde al Server con un messaggio firmato ("Sei valido").
    
3. Il Server "spilla" (staple) questa risposta firmata direttamente dentro l'handshake TLS inviato al Client.
    

**Vantaggi:**

- **Zero Latenza Client:** Il client riceve certificato + prova di validità in un colpo solo.
    
- **Privacy Totale:** La CA vede solo le richieste del Server, non gli IP degli utenti.
    
- **Robustezza:** Se il server OCSP della CA va offline, il Server Web può continuare a servire l'ultima risposta firmata (finché è valida), evitando disservizi.


---

# Tipologie di Certificati Digitali X.509

**Tags:** #ingegneria #security #pki #certificati #tls #smime #iot

## 1. Panoramica Generale

Non esiste un solo tipo di certificato. Sebbene la struttura tecnica (X.509) sia comune, i certificati differiscono profondamente per **scopo d'uso** e **livello di validazione**.

Le tre garanzie fondamentali fornite sono:

- **Autenticazione:** Prova l'identità del soggetto.
    
- **Confidenzialità:** Permette la cifratura dei dati.
    
- **Integrità:** Previene la manomissione.
    

![[SCREEN_SLIDE_107_TYPES]]

> [!abstract] Visual Analysis
> 
> What to look at: L'immagine mostra l'ecosistema dei certificati come una raggiera.
> 
> Meaning: Al centro c'è la tecnologia PKI, da cui si diramano usi diversi: Server (SSL/TLS), Client, Email (S/MIME), Code Signing, ecc.

---

## 2. Certificati SSL/TLS (HTTPS)

Sono i certificati più comuni, fondamentali per la sicurezza del web (e-commerce, banking).

Si classificano in base a due criteri: Livello di Validazione e Copertura del Dominio.

### Classificazione per Validazione (Validation Level)

Quanto è profondo il controllo fatto dalla CA prima di emettere il certificato?

1. **Domain Validation (DV):**
    
    - **Verifica:** Conferma solo che chi richiede il certificato controlla il dominio (es. via email o record DNS).
        
    - **Caratteristiche:** Automatizzato, veloce, economico.
        
    - **Livello di Fiducia:** Basso (garantisce la cifratura, ma non sai chi c'è dietro il sito).
        
2. **Organization Validation (OV):**
    
    - **Verifica:** Controlla il dominio E l'identità dell'organizzazione (visure camerali, registri ufficiali).
        
    - **Livello di Fiducia:** Medio.
        
3. **Extended Validation (EV):**
    
    - **Verifica:** Controlli legali, fisici e operativi molto severi.
        
    - **Caratteristiche:** Costoso, richiede tempo.
        
    - **Visualizzazione:** Storicamente faceva apparire la "barra verde" nel browser (oggi meno evidente, ma mostra il nome dell'azienda nei dettagli).
        

### Classificazione per Dominio (Scope)

Quanti e quali domini protegge il certificato?

- **Single-Domain:** Protegge esattamente un FQDN (es. `www.example.com`).
    
- **Wildcard:** Protegge un dominio e tutti i suoi sottodomini di primo livello.
    
    - **Sintassi:** `*.example.com` (copre `mail.example.com`, `shop.example.com`).
        
    - **Rischio:** Se la chiave privata viene compromessa, tutti i sottodomini sono a rischio.
        
- **Multi-Domain (SAN):** Protegge domini diversi con un solo certificato.
    
    - **Esempio:** `example.com`, `example.org`, `mail.example.net`.
        
    - **Tecnica:** Usa l'estensione **SAN** (Subject Alternative Name).
        

---

## 3. Certificati Client e S/MIME

Questi certificati sono destinati a identificare **utenti** o **dispositivi**, non server web.

### Certificati Client

Usati per l'autenticazione forte (spesso in contesti Zero Trust o VPN).

- **Mutual TLS (mTLS):** Il server autentica il client tramite certificato (invece di user/password).
    
- **VPN Access:** Accesso sicuro alle reti aziendali.
    

### S/MIME (Secure/Multipurpose Internet Mail Extensions)

Specifici per la sicurezza delle email.

- **Firma Digitale:** Garantisce che l'email provenga davvero dal mittente e non sia stata modificata (Autenticità + Integrità).
    
- **Cifratura (Encryption):** Cifra il contenuto dell'email in modo che solo il destinatario (che possiede la chiave privata corrispondente) possa leggerla (Confidenzialità).
    

> [!tip] Exam Focus
> 
> S/MIME è lo standard dominante per la sicurezza email in ambito corporate e governativo. L'alternativa è PGP (Web of Trust), ma S/MIME si integra meglio nelle gerarchie aziendali centralizzate.

---

## 4. Code Signing e IoT

Certificati che proteggono software e hardware.

### Code Signing (Firma del Codice)

Serve a garantire che un software (es. un `.exe` o un'app mobile) provenga da uno sviluppatore legittimo e non sia stato infettato da virus dopo la compilazione.

- **Obiettivo:** Integrità del software.
    
- **Uso:** Driver Windows, App iOS/Android, Firmware.
    

> [!failure] Common Pitfall
> 
> Se un certificato di Code Signing viene rubato, un attaccante può firmare malware facendolo sembrare software legittimo di un'azienda fidata (es. Microsoft o Adobe).

### Device & IoT Certificates

Usati per l'autenticazione "Machine-to-Machine" (M2M) su larga scala.

- **Ambiti:** Smart Home, Automotive (V2X), Sistemi Industriali (SCADA).
    
- **Caratteristica:** Spesso gestiti in volumi enormi (milioni di dispositivi) e con cicli di vita automatizzati.
    

---

## 5. Certificati Specializzati e Self-Signed

### Certificati Qualificati (Qualified Certificates)

Specifici del regolamento europeo **eIDAS**.

- **Valore Legale:** La firma apposta con questi certificati ha lo stesso valore legale di una firma autografa.
    
- **Uso:** Atti pubblici, contratti finanziari, Pubblica Amministrazione.
    

### Attribute Certificates

Una particolarità: **non contengono una chiave pubblica**.

- **Scopo:** Legano un'identità a un **ruolo** o permesso (es. "Mario Rossi è un Medico").
    
- **Uso:** Sistemi di controllo accessi (Authorization), non autenticazione pura.
    

### Short-Lived Certificates

Certificati "usa e getta" validi per pochissimo tempo (ore o giorni).

- **Vantaggio:** Riducono la dipendenza dalle liste di revoca (CRL/OCSP). Se il certificato viene rubato, scade talmente in fretta che il danno è limitato.
    
- **Contesto:** Ambienti DevOps, Kubernetes, ACME.
    

### Self-Signed Certificates (Auto-firmati)

Certificati firmati con la loro stessa chiave privata (non da una CA fidata).

- **Pro:** Gratuiti, facili da creare per test/sviluppo.
    
- **Contro:** Generano errori di sicurezza nel browser ("Non sicuro").
    
- **Rischio:** Vulnerabili agli attacchi Man-in-the-Middle (MITM) perché non c'è una terza parte che garantisce l'identità.
    

> [!example] Professor's Example
> 
> Usare un certificato Self-Signed in produzione è accettabile SOLO se si ha il controllo completo di tutti i client (es. una rete interna chiusa dove si installa manualmente il certificato su ogni macchina). Sul web pubblico è un errore grave.