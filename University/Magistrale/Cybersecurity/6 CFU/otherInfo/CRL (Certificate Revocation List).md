# Public Key Infrastructure (PKI) e Certificati X.509

**Tags:** #ingegneria #security #pki #x509 #crittografia #trust_model

## 1. Il Concetto Fondamentale: Perché serve la PKI?

La crittografia asimmetrica (come RSA o ECC) risolve il problema della confidenzialità senza scambiare segreti, ma introduce un nuovo problema critico: **la distribuzione sicura delle chiavi pubbliche**.

Se ricevo una chiave pubblica, come so che appartiene davvero a chi dice di essere?

- **Il Rischio:** Un attaccante (Man-in-the-Middle) può intercettare la comunicazione e sostituire la chiave pubblica legittima con la propria.
    
- **La Soluzione PKI:** Un'infrastruttura composta da hardware, software, policy e procedure che lega indissolubilmente un'identità a una chiave pubblica tramite una terza parte fidata (CA).
    

### Componenti dell'Architettura

![[SCREEN_SLIDE_COMPONENTS_ARCH]]

> [!abstract] Visual Analysis
> 
> What to look at: La relazione triangolare tra CA, RA e Repository.
> 
> Meaning:
> 
> 1. **CA (Certification Authority):** L'autorità suprema che emette, firma e gestisce il ciclo di vita dei certificati.
>     
> 2. **RA (Registration Authority):** Il "front-office" che verifica l'identità del richiedente (documenti, DNS) prima di autorizzare l'emissione.
>     
> 3. **Repository:** L'elenco pubblico dove vengono pubblicati i certificati e le informazioni di revoca (CRL).
>     

---

## 2. Il Certificato X.509: Struttura e Encoding

Il certificato digitale è il documento che attesta l'identità. Segue lo standard internazionale **X.509**.

### Encoding: La Sintassi dei Certificati

Per garantire che un certificato sia leggibile ovunque (da un server Linux a un iPhone), si usano standard precisi:

1. **ASN.1 (Abstract Syntax):** Descrive la struttura dati in modo astratto (es. "qui c'è una data", "qui un intero").
    
2. **DER (Distinguished Encoding Rules):** La traduzione in formato **binario** univoco. È il formato "puro" usato per calcolare la firma digitale.
    
3. **PEM (Privacy Enhanced Mail):** È il formato DER codificato in **Base64** (testo ASCII), racchiuso tra `-----BEGIN CERTIFICATE-----`. È il formato più usato da amministratori di sistema e web server.
    

### Struttura Interna (TBSCertificate)

Il cuore del certificato (la parte che viene firmata) contiene tre macro-sezioni.

**The logical structure is defined as:**

$$\text{Certificato} = \text{Identità} + \text{Chiave Pubblica} + \text{Validità} + \text{Firma CA}$$

I campi critici ("Core Fields") sono:

- **Serial Number:** Intero univoco assegnato dalla CA. Fondamentale per identificare il certificato nelle liste di revoca.
    
- **Issuer:** Il Distinguished Name (DN) della CA che ha emesso il certificato.
    
- **Subject:** Il DN dell'entità a cui appartiene il certificato (es. il sito web).
    
- **Validity:** Finestra temporale (`NotBefore`, `NotAfter`). Fuori da questo range, il certificato è carta straccia.
    
- **Subject Public Key Info:** Contiene l'algoritmo (es. RSA, ECDSA) e la chiave pubblica vera e propria.
    

---

## 3. Le Estensioni X.509 v3

I campi base non bastano per la complessità moderna. La versione 3 introduce le **Estensioni**, che possono essere marcate come **Critiche** (se il sistema non la capisce, deve rifiutare il certificato) o **Non Critiche**.

### Estensioni Fondamentali

- **Basic Constraints:** Distingue se il certificato è di una **CA** (può firmare altri certificati, `CA=TRUE`) o di un **End-Entity** (foglia, `CA=FALSE`).
    
- **Key Usage (KU) / Extended Key Usage (EKU):** Definisce lo scopo legale e tecnico della chiave (es. "Solo per cifrare email", "Solo per autenticazione Server HTTPS").
    
- **Subject Alternative Name (SAN):** Permette di proteggere più domini (`www.example.com`, `mail.example.org`) o indirizzi IP con un solo certificato. Oggi è il campo primario controllato dai browser (il _Common Name_ è deprecato).
    
- **SKI & AKI (Subject/Authority Key Identifier):** Hash delle chiavi pubbliche che servono al software per costruire rapidamente la catena di fiducia senza ambiguità.
    

---

## 4. La Gerarchia di Fiducia (Trust Hierarchy)

La PKI è organizzata ad albero per motivi di sicurezza e scalabilità.

### Root CA (Trust Anchor)

- **Ruolo:** È la radice della fiducia. Non ha nessuno sopra di sé.
    
- **Caratteristica:** Il suo certificato è **Self-Signed** (firmato da se stesso).
    
- **Sicurezza:** La chiave privata è tenuta **Offline** (in cassaforte fisica/HSM, air-gapped) e usata raramente (solo per firmare le Intermediate).
    
- **Distribuzione:** È pre-installata nei Trust Store dei Sistemi Operativi e Browser.
    

### Intermediate CA

- **Ruolo:** Delegata dalla Root per l'operatività quotidiana.
    
- **Vantaggio:** Se viene compromessa, la Root può revocarla senza dover aggiornare milioni di dispositivi. La Root resta al sicuro.
    
- **Policy:** Spesso le Intermediate sono divise per scopo (es. "Intermediate per SSL", "Intermediate per Firma Codice").
    

### End-Entity (Leaf)

- **Ruolo:** Il certificato finale usato dall'utente o dal server.
    
- **Limite:** Non può firmare altri certificati. È la "foglia" dell'albero.
    

---

## 5. La Catena di Fiducia (Chain of Trust)

Quando un browser si collega a un sito sicuro, non si fida del certificato del sito a priori. Deve validare l'intero percorso (path) fino a una Root fidata.

**Validation Logic Algorithm:**

1. Il browser riceve il certificato Foglia.
    
2. Cerca il genitore (Issuer) usando l'estensione **AIA** o i certificati inviati dal server.
    
3. Verifica il collegamento crittografico: `AKI del Figlio == SKI del Genitore`.
    
4. Verifica la firma digitale del genitore sul figlio.
    
5. Controlla validità temporale e revoca.
    
6. Ripete il processo salendo fino a trovare una **Root CA** presente nel suo Trust Store locale.
    

**Mathematical verification step at each link:**

$$\text{Verify}(Pk_{Parent}, \text{Sig}_{Parent}, \text{Data}_{Child}) \rightarrow \text{Valid}$$

> [!failure] Common Pitfall
> 
> Missing Intermediate: Spesso i server inviano solo il certificato foglia. Se mancano i certificati intermedi, il browser non riesce a "collegare i puntini" fino alla Root e mostra un errore di sicurezza. Il server deve essere configurato per inviare la "catena completa" (Chain file).

---

## 6. La Revoca: Quando la fiducia finisce

Un certificato può essere invalidato prima della scadenza naturale (es. furto della chiave privata, errore di emissione).

### Metodi di Revoca

1. **CRL (Certificate Revocation List):**
    
    - Una lista periodica ("Blacklist") firmata dalla CA contenente tutti i seriali revocati.
        
    - **Contro:** Lenta da scaricare (può pesare MB), rischio di latenza (dati vecchi tra un aggiornamento e l'altro).
        
2. **OCSP (Online Certificate Status Protocol):**
    
    - Verifica in tempo reale. Il client chiede alla CA: "Il seriale X è valido?".
        
    - **Contro:** Problemi di privacy (la CA sa quali siti visiti) e performance (una connessione in più).
        
3. **OCSP Stapling:**
    
    - Il server web scarica periodicamente la prova OCSP firmata dalla CA e la "spilla" (staples) al certificato durante l'handshake TLS.
        
    - **Pro:** Veloce, privacy preservata (il client non parla con la CA), robusto.
        

---

## 7. Tipologie di Certificati

Esistono diverse categorie basate sul livello di verifica e sull'utilizzo.

### Per Livello di Validazione (SSL/TLS)

- **DV (Domain Validated):** Verifica solo il controllo tecnico del dominio (email/DNS). Veloce, economico, ma bassa garanzia sull'identità reale.
    
- **OV (Organization Validated):** Verifica l'esistenza legale dell'azienda.
    
- **EV (Extended Validation):** Controlli legali e fisici severissimi. Offre la massima garanzia di identità.
    

### Per Ambito d'Uso

- **Wildcard:** Protegge `*.dominio.com` (tutti i sottodomini di primo livello).
    
- **Client Certificate:** Usato per autenticare utenti o dispositivi (es. Smart Card, VPN aziendali, mTLS).
    
- **Code Signing:** Garantisce l'integrità del software e l'identità dello sviluppatore, prevenendo manomissioni (malware).
    
- **S/MIME:** Cifra e firma le email per garantire confidenzialità e autenticità.