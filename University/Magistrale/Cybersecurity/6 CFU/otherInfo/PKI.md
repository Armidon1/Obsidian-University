Questa è una versione sintetica di [[14 CS Lowel Level - PKI]], per saperne di più, si rimanda alla nota in questione.
# Public Key Infrastructure (PKI) e Certificati X.509

**Tags:** #ingegneria #security #pki #x509 #crittografia #trust_model

## 1. Il Concetto Fondamentale: Perché serve la PKI?

La crittografia asimmetrica risolve il problema della confidenzialità, ma introduce un nuovo problema critico: **la distribuzione sicura delle chiavi pubbliche**.

Se ricevo una chiave pubblica, come so che appartiene davvero a chi dice di essere?

- **Il Rischio:** Un attaccante (Man-in-the-Middle) può sostituire la chiave pubblica legittima con la propria.
    
- **La Soluzione PKI:** Un'infrastruttura che lega indissolubilmente un'identità a una chiave pubblica tramite una terza parte fidata.
    

### Componenti dell'Architettura

![[Pasted image 20260103130031.png]]

> [!abstract] Visual Analysis
> 
> What to look at: La relazione triangolare tra CA, RA e Repository.
> 
> Meaning:
> 
> 1. **CA (Certification Authority):** L'autorità suprema che emette e firma i certificati.
>     
> 2. **RA (Registration Authority):** Il "front-office" che verifica l'identità del richiedente prima dell'emissione.
>     
> 3. **Repository:** L'elenco pubblico dei certificati e delle revoche (CRL).
>     

---

## 2. Il Certificato X.509: Struttura e Encoding

Il certificato digitale è il passaporto elettronico. Segue lo standard **X.509**.

### Encoding: La Lingua dei Certificati

Per garantire che un certificato sia leggibile da qualsiasi computer, si usano standard precisi:

1. **ASN.1 (Sintassi):** Descrive in astratto la struttura dati (es. "qui c'è una data", "qui un intero").
    
2. **DER (Formato Binario):** La traduzione in byte univoci e immutabili (usato per la firma).
    
3. **PEM (Formato Testo):** Il formato DER codificato in Base64 (quello che inizia con `-----BEGIN CERTIFICATE-----`).
    

### Struttura Interna (TBSCertificate)

Il cuore del certificato contiene tre macro-sezioni:

**The logical structure is defined as:**

$$\text{Certificate} = \text{Identità} + \text{Chiave Pubblica} + \text{Validità} + \text{Firma CA}$$

I campi critici sono:

- **Serial Number:** Intero univoco per CA (fondamentale per la revoca).
    
- **Issuer:** Chi ha emesso il certificato (la CA).
    
- **Subject:** A chi appartiene il certificato (es. il sito web).
    
- **Validity:** Finestra temporale (`NotBefore`, `NotAfter`).
    
- **Subject Public Key Info:** La chiave pubblica e l'algoritmo (es. RSA, ECC).
    

---

## 3. Le Estensioni X.509 v3

I campi base non bastano più. La versione 3 introduce le **Estensioni**, che possono essere **Critiche** (se non capite, il certificato va rifiutato) o **Non Critiche**.

### Estensioni Fondamentali

- **Basic Constraints:** Distingue se il certificato è di una **CA** (può firmare altri certificati) o di un **End-Entity** (foglia).
    
- **Key Usage (KU) / Extended Key Usage (EKU):** Definisce lo scopo della chiave (es. "Solo per cifrare email", "Solo per autenticazione Server").
    
- **Subject Alternative Name (SAN):** Permette di proteggere più domini (`www.example.com`, `mail.example.org`) con un solo certificato. Oggi sostituisce il _Common Name_.
    
- **SKI & AKI:** Identificatori univoci delle chiavi (Subject e Authority) per facilitare la costruzione della catena di fiducia.
    

---

## 4. La Gerarchia di Fiducia (Trust Hierarchy)

La PKI è organizzata ad albero per motivi di sicurezza e scalabilità.

### Root CA (Trust Anchor)

- **Ruolo:** È la radice della fiducia.
    
- **Caratteristica:** Il suo certificato è **Self-Signed** (firmato da se stesso).
    
- **Sicurezza:** La chiave privata è tenuta **Offline** (in cassaforte fisica/HSM) e usata raramente.
    
- **Distribuzione:** Pre-installata nei Trust Store di Browser e Sistemi Operativi.
    

### Intermediate CA

- **Ruolo:** Delegata dalla Root per operare quotidianamente.
    
- **Vantaggio:** Se compromessa, si revoca solo l'intermedia senza dover aggiornare milioni di dispositivi (la Root resta salva).
    
- **Policy:** Spesso dedicate a scopi specifici (es. "Intermediate per SSL", "Intermediate per Firma Codice").
    

### End-Entity (Leaf)

- **Ruolo:** Il certificato finale usato dall'utente o dal server.
    
- **Limite:** Non può firmare altri certificati (`BasicConstraints: CA=FALSE`).
    

---

## 5. La Catena di Fiducia (Chain of Trust)

Quando visiti un sito sicuro, il browser deve validare l'intero percorso dal certificato del sito fino a una Root fidata.

**Validation Logic Algorithm:**

1. Prendi il certificato foglia.
    
2. Trova il genitore (Issuer) confrontando `Issuer Name` e `AKI`.
    
3. Verifica la firma digitale del genitore sul figlio.
    
4. Controlla la validità temporale e lo stato di revoca.
    
5. Ripeti salendo fino alla Root.
    

**Mathematical verification step at each link:**

$$\text{Verify}(Pk_{Parent}, \text{Sig}_{Parent}, \text{Data}_{Child}) \rightarrow \text{Valid}$$

> [!failure] Common Pitfall
> 
> Missing Intermediate: Spesso i server inviano solo il certificato foglia. Se mancano i certificati intermedi, il browser non riesce a ricostruire la catena fino alla Root e dà errore. Il server deve inviare la "catena completa" (eccetto la Root).

---

## 6. La Revoca: Quando la fiducia finisce

Un certificato può essere invalidato prima della scadenza (es. furto della chiave privata).

### Metodi di Revoca

1. **CRL (Certificate Revocation List):**
    
    - Una lista periodica firmata dalla CA con tutti i seriali revocati.
        
    - **Contro:** Lenta da scaricare, può diventare enorme, rischio di latenza (dati vecchi).
        
2. **OCSP (Online Certificate Status Protocol):**
    
    - Verifica in tempo reale chiedendo alla CA: "Il seriale X è valido?".
        
    - **Contro:** Problemi di privacy (la CA sa chi visiti) e performance.
        
3. **OCSP Stapling:**
    
    - Il server web scarica periodicamente la prova OCSP dalla CA e la "spilla" (staples) al certificato durante la connessione.
        
    - **Pro:** Veloce, privacy preservata, robusto.
        

---

## 7. Tipologie di Certificati

Esistono diversi tipi basati sulla validazione e sull'uso.

### Per Livello di Validazione (SSL/TLS)

- **DV (Domain Validated):** Verifica solo il controllo del dominio. Veloce, economico.
    
- **OV (Organization Validated):** Verifica anche l'esistenza dell'azienda.
    
- **EV (Extended Validation):** Controlli legali severissimi. Massima fiducia.
    

### Per Ambito d'Uso

- **Wildcard:** Protegge `*.dominio.com` (tutti i sottodomini).
    
- **Client Certificate:** Per autenticare un utente (es. smart card, VPN).
    
- **Code Signing:** Garantisce l'integrità del software e l'identità dello sviluppatore.
    
- **S/MIME:** Cifra e firma le email aziendali.
    

> [!tip] Exam Focus
> 
> Ricorda la differenza tra Trust Store (dove sono le Root fidate) e Chain of Trust (il percorso dinamico costruito per validare un certificato). Senza una Root nel Trust Store, la catena non può chiudersi.