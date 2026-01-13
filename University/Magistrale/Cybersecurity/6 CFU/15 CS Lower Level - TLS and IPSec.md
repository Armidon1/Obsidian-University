last lesson [[14 CS Lowel Level - PKI]]
# Transport Layer Security (TLS): Architettura e Protocollo 1.3

**Tags:** #ingegneria #reti #sicurezza #tls #crittografia #protocolli

## 1. Introduzione e Obiettivi di Sicurezza

Il **TLS (Transport Layer Security)**, successore di SSL (Secure Sockets Layer), è il protocollo crittografico standard che opera sopra il livello di trasporto (TCP) per proteggere le comunicazioni di rete.

Il suo scopo è garantire tre proprietà fondamentali tra le applicazioni comunicanti:

- **[[Confidentiality]]:** Nessuno può leggere i dati in transito (Cifratura).
    
- **[[Integrity]]:** Nessuno può modificare i dati senza essere scoperto.
    
- **[[Authentication]]:** Verifica dell'identità delle parti (solitamente il server, opzionalmente il client).
    

### Minacce Mitigate

Il protocollo è progettato per contrastare specifici attacchi:

- **[[Eavesdropping]] (Intercettazione):** Ascolto passivo del traffico.
    
- **[[Tampering]] (Manomissione):** Modifica attiva dei pacchetti.
    
- **[[Spoofing]] (Impersonificazione):** Falsificazione dell'identità (es. sito fake).
    
- **[[Replay attack]]:** Riutilizzo di messaggi vecchi per ingannare il destinatario.
    

---

## 2. Contesto Web e Fasi del Protocollo

Nel web moderno ([[HTTPS]]), l'autenticazione è tipicamente **unilaterale**: solo il server presenta un certificato X.509 per provare la sua identità. Il client rimane anonimo a livello TLS.

> [!tip] Exam Focus
> 
> Esiste anche la Mutual Authentication (mTLS), dove sia client che server presentano certificati. È rara sul web pubblico ma molto comune in ambienti Enterprise e architetture Zero Trust.

### Le Tre Fasi Principali

Ogni connessione TLS attraversa una sequenza logica:

1. **Negoziazione:** Le parti si accordano su algoritmi e parametri (Cipher Suites).
    
2. **Autenticazione & Scambio Chiavi:** Il server si autentica e viene stabilito un segreto condiviso.
    
3. **Comunicazione Sicura:** Trasferimento dati cifrato con chiavi simmetriche.
    

---

## 3. Architettura dell'Handshake TLS 1.3

TLS 1.3 ha rivoluzionato il processo di handshake rendendolo più veloce (1-RTT) e sicuro rispetto a TLS 1.2.

![[Pasted image 20260106111050.png]]

> [!abstract] Visual Analysis
> 
> What to look at: Il diagramma mostra lo scambio di messaggi tra Client e Server.
> 
> Meaning:
> 
> - **1-RTT (Round Trip Time):** Il client invia dati e chiavi _subito_. Il server risponde e la connessione cifrata è pronta in un solo "giro".
>     
> - **Encrypted Extensions:** Nota che gran parte dell'handshake (dopo il ServerHello) è ora cifrata, proteggendo i certificati da occhi indiscreti (privacy migliorata).
>     

### Flusso Dettagliato (Server Auth Only)

**The sequence of messages is:**

1. **Client:** Invia `ClientHello` + `KeyShare` (la sua parte di chiave [[ECDHE]]).
    
2. **Server:** Risponde con `ServerHello` + `KeyShare` + `EncryptedExtensions`.
    
3. **Server:** Invia `Certificate` (Identità) + `CertificateVerify` (Firma).
    
4. **Server:** Invia `Finished` ([[MAC]] per integrità).
    
5. **Client:** Risponde con `Finished`.
    

Da questo momento, entrambe le parti condividono le stesse chiavi di sessione e il canale è sicuro.

---

## 4. Struttura dei Messaggi: ClientHello e ServerHello

Questi sono i messaggi critici per la negoziazione iniziale.

### ClientHello

È il messaggio di "presentazione" del client. Contiene:

- **Protocol Version:** [[TLS]] 1.3.
    
- **Random:** 32 byte casuali (usati poi per derivare le chiavi).
    
- **Cipher Suites:** Lista degli algoritmi supportati (solo [[AEAD]] in TLS 1.3).
    
- **Extensions:** Il cuore della flessibilità di TLS.
    

**Estensioni Fondamentali:**

- `supported_versions`: Elenca le versioni TLS (es. 1.3, 1.2).
    
- `key_share`: Contiene i parametri pubblici per lo scambio chiavi (es. la chiave pubblica [[ECDHE]] su curva x25519).
    
- `server_name` (SNI): Indica quale hostname il client vuole contattare (essenziale per virtual hosting).
    
- `signature_algorithms`: Quali algoritmi di firma il client accetta.

![[Pasted image 20260106114759.png]]
![[Pasted image 20260106113007.png]]
### ServerHello

È la risposta del server. Contiene:

- **Selected Version:** La versione scelta (TLS 1.3).
    
- **Random:** 32 byte casuali del server.
    
- **Cipher Suite:** L'algoritmo scelto dalla lista del client.
    
- **Key Share:** La controparte della chiave pubblica del server per completare lo scambio Diffie-Hellman.

![[Pasted image 20260106114817.png]]
![[Pasted image 20260106113021.png]]

> [!failure] Common Pitfall
> 
> HelloRetryRequest (HRR): Se il server non supporta il gruppo crittografico proposto dal client nel key_share iniziale, risponde con un HRR. Il client deve ricominciare l'handshake inviando un nuovo ClientHello con i parametri corretti. Questo costa 1 RTT aggiuntivo.

## Core Properties of TLS 1.3

- Forward secrecy. Mandatory (via ephemeral Diffie-Hellman)
    
- 1-RTT handshake. Faster connection setup
    
- Simplified ciphersuites: AEAD-only (AES-GCM, ChaCha20-Poly1305), legacy modes removed
    
- HKDF-based key derivation (standardized, robust KDF)
    
- Replay protection: handshake protected; 0-RTT data limited/vulnerable

![[Pasted image 20260106113036.png]]
---

## 5. Derivazione delle Chiavi (HKDF)

TLS 1.3 usa **[[HKDF (HMAC-based Key Derivation Function)]]** per generare tutto il materiale crittografico in modo robusto.

### Logica Matematica

Il processo si divide in due fasi: **Extract** (estrazione entropia) ed **Expand** (espansione chiavi).

**The extraction step:**

$$\text{PRK} = \text{HMAC}(\text{salt}, \text{IKM})$$

> [!abstract] Math Analysis
> 
> - **IKM (Input Keying Material):** Il segreto condiviso ottenuto da ECDHE.
>     
> - **PRK (Pseudorandom Key):** Una chiave maestra uniforme ad alta entropia.
>     

**The expansion step (generata per ogni chiave i-esima:**

$$\text{OKM}_i = \text{HKDF-Expand}(\text{PRK}, \text{info}_i, L_i)$$

> [!abstract] Math Analysis
> 
> - **info:** Una stringa di contesto che cambia per ogni chiave (es. "tls13 client handshake traffic secret").
> - **$L_i$**:  lunghezza dell'$OKM_i$
>     
> - **Garantisce la separazione:** Anche se derivano dalla stessa PRK, le chiavi per scopi diversi sono crittograficamente indipendenti.
>     

---

## 6. Il Cuore dell'Integrità: Transcript Hash

Il **Transcript Hash** è molto più di un semplice log. È il meccanismo crittografico che "incolla" insieme ogni singolo bit scambiato durante la negoziazione, garantendo che nessuno abbia modificato i messaggi in transito.

### Come Funziona (The Rolling Hash)

Tutti i messaggi dell'handshake vengono inseriti sequenzialmente in un hash incrementale.

- **Binding:** Ogni nuovo messaggio viene "assorbito" nello stato corrente dell'hash.
    
- **Risultato:** L'hash finale rappresenta l'impronta digitale unica di _quella specifica_ conversazione.
    

> [!abstract] Visual Analysis
> 
> Meaning: Il Transcript Hash lega crittograficamente i parametri negoziati (Cipher Suite, Versione) e i valori casuali (Randoms). Se un attaccante modifica anche solo un bit (es. cercando di forzare una cifratura debole), l'hash finale cambierà completamente.

### I Quattro Usi del Transcript Hash

Le slide identificano quattro funzioni critiche per la sicurezza:

1. **Key Derivation (Derivazione Chiavi):**
    
    - L'hash del transcript è un input diretto per le fasi finali di **HKDF-Expand**.
        
    - _Conseguenza:_ Le chiavi di sessione dipendono matematicamente dall'intera storia dell'handshake. Se la storia cambia, le chiavi cambiano.
        
2. **Messaggio Finished:**
    
    - Sia il client che il server calcolano un **MAC** (Message Authentication Code) sopra il Transcript Hash.
        
    - È la prova finale: "Ecco la firma di tutto ciò che ho visto finora".
        
3. **Downgrade Protection (Anti-Downgrade):**
    
    - Poiché il transcript include la versione del protocollo e la Cipher Suite negoziata, un attaccante non può modificare la scelta (es. forzando TLS 1.2) senza alterare l'hash e far fallire la verifica del MAC.
        
4. **Replay Protection:**
    
    - Legando i "Random" del client e del server, ogni handshake diventa unico.
        

### Quando avviene la Verifica?

La verifica è implicita nello scambio dei messaggi `Finished`.

> [!abstract] Visual Analysis
> 
> Flow:
> 
> 1. **Server Finished:** Il server calcola il MAC sul Transcript Hash _corrente_.
>     
> 2. **Client Check:** Il client ricalcola il MAC localmente. Se i valori coincidono, il client sa che il server ha visto esattamente gli stessi messaggi.
>     
> 3. **Client Finished:** Il client aggiorna l'hash con il messaggio del server e invia il suo MAC.
>     
> 4. Server Check: Il server verifica. Se c'è un match, l'integrità è garantita al 100%.
>     
>     Regola: Al primo mismatch, l'handshake viene abortito immediatamente.
>     

---

## 7. Flusso Dettagliato: Server Authentication Only

Questo è lo scenario standard per la navigazione Web (HTTPS), dove solo il server prova la sua identità.

> [!abstract] Visual Analysis
> ![[Pasted image 20260106125131.png]]
> 
> What to look at: La sequenza esatta dei messaggi e il momento in cui la crittografia si attiva.
> 
> Key Steps:
> 
> 1. **ClientHello:** Propone versioni, suite e chiavi (`KeyShare`).
>     
> 2. **ServerHello:** Sceglie i parametri e completa lo scambio chiavi (`KeyShare`). _Da qui in poi tutto è cifrato._
>     
> 3. **EncryptedExtensions:** Estensioni sensibili (come ALPN).
>     
> 4. **Certificate:** Il certificato X.509 del server.
>     
> 5. **CertificateVerify:** Il server firma digitalmente il Transcript Hash con la sua chiave privata (prova di possesso).
>     
> 6. **Finished (Server):** MAC sul transcript.
>     
> 7. **Finished (Client):** Il client conferma che tutto è integro.
>     

---

## 8. 0-RTT (Zero Round Trip Time) e Session Resumption

TLS 1.3 introduce una modalità ultra-veloce per i client che ritornano su un sito già visitato.

### Come funziona

1. Nella connessione precedente, il server invia un **Session Ticket** (NewSessionTicket).
    
2. Il client usa questo ticket come **PSK (Pre-Shared Key)**.
    
3. Nella nuova connessione, il client invia dati cifrati (Early Data) _insieme_ al primo `ClientHello`, senza aspettare la risposta del server.
    

### Rischi di Sicurezza (Replay)

I dati 0-RTT sono meno sicuri.

- **Mancanza di Forward Secrecy:** Se la chiave del ticket viene compromessa, i dati passati possono essere decifrati.
    
- **Vulnerabilità al Replay:** Un attaccante può registrare il pacchetto 0-RTT e inviarlo di nuovo al server (es. inviare due volte un ordine di pagamento).
    

> [!tip] Exam Focus
> 
> Mitigazione: I server dovrebbero accettare dati 0-RTT solo per richieste idempotenti (es. HTTP GET), che non cambiano lo stato del server se ripetute. Molte implementazioni disabilitano 0-RTT di default per sicurezza.

### Struttura della NewSessionTicket

- **ticket_lifetime** (4 bytes)
	- Validity of the ticket in seconds
    
- **ticket_age_add** (4 bytes, random)
	- Random offset used by client to calculate ticket age
	- Mitigates timing-based replay
    
- **ticket_nonce** (variable length)
	- Unique nonce for deriving the PSK
    
- **ticket** (opaque blob)
	- Token opque to client, identifies or encodes PSK
	- Can be stateful (ID) or stateless (encrypted PSK)
    
- **extensions** (optional)
	- e.g., _early_data_ with max_early_data_size
---

## 9. Riepilogo Novità TLS 1.3 vs 1.2

|**Caratteristica**|**TLS 1.2**|**TLS 1.3**|
|---|---|---|
|**Handshake**|2-RTT (spesso)|1-RTT (Sempre)|
|**Algoritmi**|Misti (CBC, RC4, etc.)|Solo AEAD (Sicuri e Veloci)|
|**Key Exchange**|RSA statico (no Forward Secrecy)|Effimero obbligatorio (Forward Secrecy sempre)|
|**Privacy**|Certificati in chiaro|Certificati cifrati|
|**Resumption**|Session ID|PSK / Session Ticket (con 0-RTT)|

---


# IPsec: Architettura, Security Associations e Database (SAD/SPD)

**Tags:** #ingegneria #reti #sicurezza #ipsec #sa #sad #spd #architettura

## 1. Il Problema della Sicurezza IP

Il protocollo IP originale non è stato progettato con la sicurezza in mente. Per proteggere i pacchetti (datagrammi) durante il transito su reti non sicure, esistono due approcci teorici.

### Approccio 1: Hop-by-Hop (Scartato)

Ogni router lungo il percorso decifra il pacchetto, lo controlla e lo ricifra per il router successivo.

- **Pro:** Protezione totale, inclusi gli header di instradamento.
    
- **Contro:** Carico di lavoro insostenibile per i router; gestione chiavi impossibile su scala globale; i dati sono in chiaro dentro ogni router (rischio sicurezza).
    

### Approccio 2: End-to-End / IPsec (Adottato)

La sicurezza è applicata solo agli estremi della comunicazione (Host o Gateway). I router intermedi vedono solo pacchetti cifrati e li inoltrano senza dover elaborare la crittografia.

- **Standardizzazione:** Inizialmente obbligatorio in IPv6, oggi opzionale (RFC 6434).
    

![[Pasted image 20260106140707.png]]

> [!abstract] Visual Analysis
> 
> What to look at: Lo schema mostra due scenari. In alto "Host-to-Host", in basso "Gateway-to-Gateway" (Tunnel).
> 
> Meaning: IPsec è flessibile: può proteggere la comunicazione tra due singoli PC o creare un tunnel sicuro tra due intere reti aziendali attraverso Internet.

---

## 2. Pro e Contro di IPsec

Analisi ingegneristica dell'adozione di IPsec rispetto ad altre soluzioni (come TLS).

### Vantaggi (Benefits)

- **Trasparenza:** Agendo al Livello 3 (Network), è invisibile alle applicazioni. Non serve modificare il software (browser, email, database) per usarlo.
    
- **Sicurezza Perimetrale:** Un firewall/gateway IPsec protegge tutto il traffico che entra/esce dall'azienda, anche se l'utente interno è negligente.
    
- **Anti-Bypass:** Essendo nel layer di rete, è difficile per un utente o un malware aggirare i controlli se la policy impone la cifratura.
    

### Svantaggi (Drawbacks)

- **Complessità:** La configurazione è notoriamente difficile e prona a errori.
    
- **Problemi con NAT:** Il NAT modifica gli header IP e le porte; questo rompe i controlli di integrità di IPsec (richiede "NAT-Traversal" over UDP).
    
- **Overhead:** L'aggiunta di header crittografici aumenta la dimensione del pacchetto, causando spesso frammentazione (problemi di [[MTU]]).
    

---

## 3. Il Concetto di Security Association (SA)

La **Security Association (SA)** è il mattone fondamentale di IPsec. È una relazione logica "contrattuale" tra mittente e destinatario.

> [!failure] Common Pitfall
> 
> Direzionalità: Una SA è rigorosamente unidirezionale.
> 
> Per una chat bidirezionale tra Alice e Bob servono due SA: una per $Alice \rightarrow Bob$ e una per $Bob \rightarrow Alice$.

### Identificazione Univoca

Come fa il router a sapere quale chiave usare per un pacchetto in arrivo? Usa una tripla univoca:
$$\text{SA ID} = \langle \text{SPI}, \ \text{IP}_{dst}, \ \text{ProtocolID} \rangle$$

> [!abstract] Math Analysis
> 
> - **SPI (Security Parameters Index):** Un'etichetta numerica a 32 bit inserita nell'header del pacchetto per "taggare" la connessione.
>     
> - **IP Destination:** L'indirizzo di chi riceve.
>     
> - **Protocol ID:** Indica se stiamo usando AH o ESP.
>     
![[Pasted image 20260107162252.png]]
### Parametri della SA

La SA non è solo una chiave, è un container di stato che include:

- **Sequence Number Counter:** Contatore a 32 bit per ordinare i pacchetti.
    
- **Anti-Replay Window:** Finestra scorrevole per scartare pacchetti duplicati o vecchi (protezione contro attacchi di replay).
    
- **Algoritmi e Chiavi:** Quale algoritmo usare (es. AES-GCM) e la relativa chiave segreta.
    
- **Lifetime:** Tempo di vita della SA (in secondi o Kbyte trasferiti), dopo il quale la SA muore o deve essere rinnovata.
    

---

## 4. I Database di Gestione: SPD e SAD

IPsec non cifra "tutto a caso". Decide cosa proteggere basandosi su regole precise gestite dal kernel del sistema operativo. Queste regole risiedono in due database fondamentali.

### A. Security Policy Database (SPD)

L'SPD è il "Legislatore". Definisce le regole di alto livello per classificare il traffico IP in tre categorie di azione:

1. **Protect:** Il traffico deve essere protetto con IPsec (creando o usando una SA).
    
2. **Bypass:** Il traffico passa in chiaro (es. traffico locale fidato).
    
3. **Discard:** Il traffico viene bloccato (funzione firewall).
    

I Selettori (Selectors):

Per decidere quale regola applicare, l'SPD guarda specifici campi del pacchetto, chiamati selettori:

- **Indirizzi IP:** Sorgente e Destinazione (singoli, range, wildcard).
    
- **Porte:** TCP/UDP (per distinguere servizi, es. proteggi Telnet ma non Web).
    
- **Protocollo:** TCP, UDP, ICMP, etc.
    
- **User ID:** Identificativo dell'utente (se disponibile nel sistema host).
    
- **Data Sensitivity:** Livello di classificazione (es. Top Secret vs Unclassified).
    

### B. Security Association Database (SAD)

Il SAD è l'"Esecutore". Contiene i parametri tecnici delle connessioni sicure (Security Associations - SA) attualmente attive.

- Include: Chiavi crittografiche, Algoritmi scelti, Sequence Numbers, Lifetime della connessione.
    

### Logica di Elaborazione (Outbound Processing)

Quando un pacchetto deve essere inviato, il sistema segue questo algoritmo:

**Here is the exact processing logic described:**

Plaintext

```
1. COMPARE packet fields against SPD selectors
2. IF Match Found THEN
      CASE Action OF
         Discard: DROP packet
         Bypass:  SEND packet (Plaintext)
         Protect:
            LOOKUP in SAD for active SA
            IF SA exists THEN
               GET SPI (Security Parameters Index)
               APPLY IPsec (AH or ESP)
            ELSE
               TRIGGER IKE (Key Exchange) to create new SA
            ENDIF
      ENDCASE
3. SEND processed packet
```

> [!abstract] Code Analysis
> 
> L'SPD viene sempre consultato prima del SAD. L'SPD dice "Cosa fare", il SAD dice "Come farlo" (con quali chiavi).

---

## 5. Modalità Operative: Transport vs Tunnel

IPsec può incapsulare i pacchetti in due modi, a seconda dell'architettura di rete (Host-to-Host o Gateway-to-Gateway).

### Transport Mode (Host-to-Host)

Protegge solo il **payload** del pacchetto IP originale (es. il segmento TCP/UDP). L'header IP originale rimane intatto e visibile per il routing.

- **Uso:** Comunicazione End-to-End tra due server.
    
- **Struttura:** `[IP Header Orig] [IPsec Header] [Payload]`
    

### Tunnel Mode (Gateway-to-Gateway)

Protegge l'**intero pacchetto IP originale** (Header + Payload). Il pacchetto originale viene cifrato/autenticato e inserito dentro un _nuovo_ pacchetto IP esterno.

- **Uso:** VPN tra firewall o router (Site-to-Site).
    
- **Struttura:** `[New IP Header] [IPsec Header] [Old IP Header] [Payload]`
    

![[Pasted image 20260107163219.png]]

> [!abstract] Visual Analysis
> 
> What to look at: La posizione degli header rossi (IPsec).
> 
> Meaning:
> 
> - **Transport:** L'header IPsec si inserisce _dentro_ il pacchetto originale.
>     
> - **Tunnel:** L'intero pacchetto originale diventa il _contenuto_ di un nuovo pacchetto.
>     

---

## 6. Authentication Header (AH)

Il protocollo **AH** (RFC 4302) fornisce integrità e autenticazione dell'origine, ma **NON** confidenzialità (niente cifratura).

### Caratteristiche Chiave

- **Integrità:** Garantisce che il pacchetto non sia stato modificato.
    
- **Autenticazione:** Garantisce l'identità del mittente.
    
- **Anti-Replay:** Protegge contro la reiniezione di pacchetti vecchi tramite numeri di sequenza.
    
- **No Encryption:** Chiunque intercetti il traffico può leggere i dati.
    

### Struttura dell'Header AH

L'header AH è identificato dal protocol number 51.
 
![[Pasted image 20260107164801.png]]

> [!abstract] Visual Analysis
> 
> What to look at: I campi interni dell'header.
> 
> Meaning:
> 
> - **Next Header:** Indica cosa c'è dopo (TCP, UDP, etc.).
>     
> - **SPI (Security Parameters Index):** Un numero a 32 bit che identifica univocamente la SA (insieme all'IP destinazione e al protocollo).
>     
> - **Sequence Number:** Contatore incrementale per prevenire attacchi Replay.
>     
> - **Authentication Data (ICV):** Il valore [[HMAC]] (Hash-based Message Authentication Code) che firma il pacchetto.
>     

### Copertura dell'Autenticazione (Il problema dei campi mutabili)

AH cerca di autenticare "tutto il pacchetto", incluso l'header IP. Tuttavia, alcuni campi dell'[[IP protocol (IPv4)|IP header]] (come TTL e Checksum) cambiano ad ogni salto (hop) del router.

Se AH li firmasse, la firma si romperebbe al primo router.

Soluzione Tecnica:

AH considera questi campi come Mutabili. Prima di calcolare l'HMAC:

1. I campi mutabili (es. TTL, TOS) vengono azzerati.
    
2. Si calcola l'hash.
    
3. I campi vengono ripristinati per la trasmissione.
    

> [!failure] Common Pitfall
> 
> AH e NAT: Il [[NAT (Network Address Translation)]] cambia l'indirizzo IP sorgente/destinazione nell'header. Poiché AH autentica gli indirizzi IP (considerandoli immutabili), il NAT rompe irreversibilmente AH. Se c'è NAT, AH fallisce sempre.

## 7. Modalità Operative AH: Transport vs Tunnel

AH cambia comportamento in base alla topologia.

### A. Transport Mode (Host-to-Host)

Usato per comunicazioni end-to-end tra due server. Protegge solo il payload del livello trasporto.

**Struttura del pacchetto:**
![[Pasted image 20260107171957.png]]

> [!failure] Common Pitfall
> 
> In Transport Mode, l'header IP originale è autenticato eccetto i cambi mutabili.

### B. Tunnel Mode (Gateway-to-Gateway)

Usato nelle VPN:
![[Pasted image 20260107172143.png]]
> [!failure] Common Pitfall
> 
> In Tunnel Mode, è tutto autenticato eccetto per i campi mutabili del NUOVO IP Header .

---

## 7. Tabella Comparativa: AH vs ESP

|**Funzionalità**|**AH (Transport/Tunnel)**|**ESP (Transport/Tunnel)**|
|---|---|---|
|**Confidenzialità (Cifratura)**|❌ NO|✅ SI|
|**Integrità Dati**|✅ SI (tutto il pacchetto*)|✅ SI (solo payload + header ESP)|
|**Autenticazione Origine**|✅ SI|✅ SI|
|**Anti-Replay**|✅ SI|✅ SI|
|**Compatibilità NAT**|❌ Bassa (rompe l'hash)|⚠️ Media (richiede NAT-T)|

> [!tip] Exam Focus
> 
> Nota che AH autentica anche parti dell'header IP esterno, mentre ESP autentica solo ciò che viene incapsulato dopo l'header ESP. Questo rende AH teoricamente più sicuro per l'integrità dell'indirizzamento, ma praticamente inutilizzabile su Internet moderno a causa del NAT.


## 8. Encapsulating Security Payload (ESP)

Mentre AH fornisce solo integrità ed autenticazione dell'origine, **ESP** (Protocollo 50) è il protocollo IPsec più completo perché offre **Confidenzialità** (Cifratura) oltre all'autenticazione e all'integrità.

### Struttura del Pacchetto ESP

ESP incapsula i dati avvolgendoli con un Header (prima dei dati) e un Trailer (dopo i dati).

**Struttura Logica dei Campi:**

1. **ESP Header (In chiaro):**
    
    - `SPI`: Identifica la Security Association.
        
    - `Sequence Number`: Contatore anti-replay.
        
2. **Payload (Cifrato):** I dati trasportati (es. segmento TCP).
    
3. **ESP Trailer (Cifrato):**
    
    - `Padding`: Bit di riempimento per allineare la cifratura a blocchi (es. AES-CBC richiede blocchi di 128 bit).
        
    - `Pad Length`: Lunghezza del padding.
        
    - `Next Header`: Identifica il protocollo contenuto nel payload.
        
4. **ESP Auth Data (In chiaro):** L'ICV (Integrity Check Value) calcolato sul pacchetto.
    

![[Pasted image 20260107170305.png]]

> [!abstract] Visual Analysis
> 
> What to look at: Le due frecce laterali "Confidentiality Coverage" e "Authentication Coverage".
> 
> Meaning:
> 
> - **Cifratura:** Copre dal _Payload_ fino al _Next Header_. L'Header ESP iniziale rimane leggibile.
>     
> - **Autenticazione:** Copre dall'_Header ESP_ fino al _Next Header_.
>     
> - **Nota:** L'Auth Data stesso non è né cifrato né autenticato (è il risultato dell'operazione).
>     

---

## 9. Modalità Operative ESP: Transport vs Tunnel

Come per AH, anche ESP cambia comportamento in base alla topologia.

### A. Transport Mode (Host-to-Host)

Usato per comunicazioni end-to-end tra due server. Protegge solo il payload del livello trasporto.

**Struttura del pacchetto:**
![[Pasted image 20260107171709.png]]

```
[Orig IP Hdr] [ESP Hdr] [Encrypt: TCP/UDP + Data + ESP Trlr] [ESP Auth]
```

> [!failure] Common Pitfall
> 
> In Transport Mode, l'header IP originale non è cifrato. Un attaccante può vedere chi sta parlando con chi (Traffic Analysis), ma non il contenuto.

### B. Tunnel Mode (Gateway-to-Gateway)

Usato per le VPN. Cifra l'intero pacchetto IP originale.

**Struttura del pacchetto:**
![[Pasted image 20260107171717.png]]

```
[New IP Hdr] [ESP Hdr] [Encrypt: Orig IP Hdr + TCP/UDP + Data + ESP Trlr] [ESP Auth]
```

> [!abstract] Visual Analysis
> 
> Il pacchetto originale diventa il payload del nuovo pacchetto. L'indirizzo IP esterno (New IP Hdr) mostra solo i gateway della VPN, nascondendo la topologia interna.

---

## 10. Internet Key Exchange (IKE)

Gestire manualmente le chiavi (Manual Keying) è impossibile su larga scala. **IKE** è il protocollo che automatizza la negoziazione delle Security Association (SA).

### Funzioni Chiave di IKE

- **Autenticazione Mutua:** Verifica l'identità dei peer (tramite Pre-Shared Key o Certificati).
    
- **Negoziazione:** Concorda algoritmi di cifratura/hash (es. "Usiamo [[AES]]-256 e [[SHA-256]]?").
    
- **Generazione Chiavi:** Usa [[Diffie-Hellman Key Exchange]] per creare chiavi segrete condivise su un canale insicuro.
    
- **Rekeying:** Ruota periodicamente le chiavi per garantire la sicurezza ([[Perfect Forward Secrecy (PFS)]]).
    

---

## 11. Architettura e Fasi di IKEv2

IKEv2 semplifica il processo rispetto alla versione 1, riducendo lo scambio a 4 messaggi principali per stabilire la connessione.
    
- **IKE_SA_INIT**: negotiation of algorithms, Diffie–Hellman exchange, provisional IKE SA
    
- **IKE_AUTH**: peer authentication, consolidation of the IKE SA, creation of the first Child SA
    
- **CREATE_CHILD_SA**: additional Child SAs or rekeying of existing ones
    
- **INFORMATIONAL**: error reporting, SA deletion, keep-alive messages
    
Each exchange usually involves 2 messages (request/response), except EAP-based authentication which may require more

### IKE SA vs Child SA

- **IKE SA (Control Plane):** Un canale sicuro bidirezionale usato _solo_ per scambiare messaggi di controllo IKE.
    
- **Child SA (Data Plane):** Le vere SA IPsec (ESP/AH) usate per proteggere il traffico utente.
    

### Fase 1: IKE_SA_INIT (Negoziazione Iniziale)

1. **Initiator → Responder**
	    
	- HDR: IKE header with Initiator SPI, Responder SPI = 0, exchange type, flags
	    
	- SAi1: Initiator’s proposals (encryption, integrity, PRF, DH group)
	    
	- KEi: Diffie–Hellman value from the Initiator
	    
	- Ni: Initiator nonce (random value)
	    
2. **Responder → Initiator**
	    
	- HDR: IKE header with both SPIs set
	    
	- SAr1: Responder’s chosen algorithms from the proposals
	    
	- KEr: Diffie–Hellman value from the Responder
	    
	- Nr: Responder nonce (random value)
	    
	- [CERTREQ] (optional): certificate request
    
- **Purpose**
	    
	- Negotiate cryptographic algorithms
	    
	- Exchange DH values and nonces
	    
	- Derive the shared secret and create a provisional IKE SA

> [!abstract] Math Analysis
> 
> - **SA:** Proposte di algoritmi (Cipher Suite).
>     
> - **KE (Key Exchange):** I valori pubblici Diffie-Hellman ($g^a \mod p$).
>     
> - **N (Nonce):** Numeri casuali per prevenire attacchi di replay e aggiungere entropia.
>     
> - **Risultato:** Dopo questo scambio, i peer calcolano una chiave segreta condivisa $K = g^{ab}$. Tutto il traffico successivo è cifrato.
>     

### Fase 2: IKE_AUTH (Autenticazione)

1.  Initiator → Responder
	    
	- HDR: IKE header with both SPIs set
	    
	- IDi: Initiator Identity (IP address, FQDN, or other identifier)
	    
	- AUTH: Authentication payload (PSK, certificate-based signature, or EAP method)
	    
	- [CERT, CERTREQ] (optional): certificates and certificate requests
	    
	- SAi2: Proposal for the first Child SA (ESP or AH parameters)
	    
	- TSi: Traffic Selectors (initiator’s view of protected traffic)
	    
	- TSr: Traffic Selectors (responder’s view of protected traffic)
    
2. Responder → Initiator
	    
	- HDR: IKE header with both SPIs
	    
	- IDr: Responder Identity
	    
	- AUTH: Authentication payload of the responder
	    
	- [CERT] (optional): responder’s certificate(s)
	    
	- SAr2: Accepted Child SA proposal
	    
	- TSi/TSr: Final traffic selectors agreed for the Child SA
	    
- Purpose
	    
	- Authenticate both peers (initiator and responder)
	    
	- Consolidate the IKE SA (it becomes fully established)
	    
	- Negotiate and create the first Child SA for IPsec traffic

> [!abstract] Technical Logic
> 
> - **ID:** L'identità (es. IP o FQDN).
>     
> - **AUTH:** La prova dell'identità (Firma digitale sul messaggio precedente).
>     
> - **TS (Traffic Selectors):** Definiscono quale traffico deve entrare nel tunnel (es. "Tutta la subnet 192.168.1.0/24").
>     

### Fase 3: CREATE_CHILD_SA (Gestione)

1. Initiator → Responder
	    
	- HDR: IKE header with existing IKE SA SPIs
	    
	- SA: Proposal for the new Child SA (algorithms, mode, lifetimes)
	    
	- Ni: Nonce generated by the initiator
	    
	- [KEi] (optional): Diffie–Hellman value, if a new DH exchange is required (for Perfect Forward Secrecy)
	    
	- TSi: Traffic Selectors proposed by initiator
	    
	- TSr: Traffic Selectors proposed for responder
	    
2. Responder → Initiator
	    
	- HDR: IKE header with same SPIs
	    
	- SA: Accepted proposal for the Child SA
	    
	- Nr: Nonce generated by the responder
	    
	- [KEr] (optional): Responder’s Diffie–Hellman value
	    
	- TSi/TSr: Final traffic selectors chosen by responder
    
- Purpose
	    
	- Create additional Child SAs under the same IKE SA
	    
	- Perform rekeying of an existing Child SA or the IKE SA itself
	    
	- Allow traffic with new parameters, selectors, or lifetimes without renegotiating the IKE SA

---
## 12. SA attraverso IKE
- IKE SA (Control Plane)
	    
	- Secures IKE signaling and negotiation
    
- Child SA(s) (Data Plane)
	    
	- Protect data traffic using ESP or AH
	    
	- All Child SAs are created, updated, and deleted by a single IKE SA
    
- SAD (Security Association Database)
	    
	- Stores IKE SA and all Child SAs
	    
	- Contains
		    
		- keys
		    
		- algorithms
		    
		- lifetimes
		    
		- sequence numbers

## 13. IPsec con IKE

1. Complementary roles
	    
	- IPsec (AH/ESP) provides packet security
	    
	- IKE manages negotiation and keys
	    
2. Transparency
	    
	- Works below transport and application layers
    
3. Deployment flexibility
	    
	- Host-to-host, gateway-to-gateway, host-to-gateway

## 14. Riepilogo: Ruoli e Differenze

|**Caratteristica**|**IKE (Control Plane)**|**IPsec ESP/AH (Data Plane)**|
|---|---|---|
|**Protocollo**|UDP Porta 500|Protocollo IP 50 (ESP) o 51 (AH)|
|**Funzione**|"L'Avvocato": Negozia il contratto|"Il Corriere Blindato": Trasporta i dati|
|**Sicurezza**|Protegge se stesso (IKE SA)|Protegge il traffico utente (Child SA)|
|**Durata**|Lunga (Sessione di gestione)|Breve (Rinnovata spesso per sicurezza)|

> [!tip] Exam Focus
> 
> Traffic Selectors (TS): Sono cruciali in IKEv2. Se l'Initiator propone un TS (es. "voglio parlare con tutti") e il Responder ha una policy diversa (es. "puoi parlare solo col server web"), la negoziazione del TS permette di restringere il tunnel alla sola intersezione permessa (Narrowing).

![[Pasted image 20260107174725.png]]

---
next lesson [[16 CS Lower Level - Firewall]]
domadne esame [[domande esame TLS e IPSEC|qui]]