# Transport Layer Security (TLS): Architettura e Protocollo 1.3

**Tags:** #ingegneria #reti #sicurezza #tls #crittografia #protocolli

## 1. Introduzione e Obiettivi di Sicurezza

Il **TLS (Transport Layer Security)**, successore di SSL (Secure Sockets Layer), è il protocollo crittografico standard che opera sopra il livello di trasporto (TCP) per proteggere le comunicazioni di rete.

Il suo scopo è garantire tre proprietà fondamentali tra le applicazioni comunicanti:

- **Confidenzialità:** Nessuno può leggere i dati in transito (Cifratura).
    
- **Integrità:** Nessuno può modificare i dati senza essere scoperto.
    
- **Autenticazione:** Verifica dell'identità delle parti (solitamente il server, opzionalmente il client).
    

### Minacce Mitigate

Il protocollo è progettato per contrastare specifici attacchi:

- **Eavesdropping (Intercettazione):** Ascolto passivo del traffico.
    
- **Tampering (Manomissione):** Modifica attiva dei pacchetti.
    
- **Spoofing (Impersonificazione):** Falsificazione dell'identità (es. sito fake).
    
- **Replay Attacks:** Riutilizzo di messaggi vecchi per ingannare il destinatario.
    

---

## 2. Contesto Web e Fasi del Protocollo

Nel web moderno (HTTPS), l'autenticazione è tipicamente **unilaterale**: solo il server presenta un certificato X.509 per provare la sua identità. Il client rimane anonimo a livello TLS.

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

![[SCREEN_SLIDE_HANDSHAKE_FLOW]]

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

1. **Client:** Invia `ClientHello` + `KeyShare` (la sua parte di chiave ECDHE).
    
2. **Server:** Risponde con `ServerHello` + `KeyShare` + `EncryptedExtensions`.
    
3. **Server:** Invia `Certificate` (Identità) + `CertificateVerify` (Firma).
    
4. **Server:** Invia `Finished` (MAC per integrità).
    
5. **Client:** Risponde con `Finished`.
    

Da questo momento, entrambe le parti condividono le stesse chiavi di sessione e il canale è sicuro.

---

## 4. Struttura dei Messaggi: ClientHello e ServerHello

Questi sono i messaggi critici per la negoziazione iniziale.

### ClientHello

È il messaggio di "presentazione" del client. Contiene:

- **Protocol Version:** TLS 1.3.
    
- **Random:** 32 byte casuali (usati poi per derivare le chiavi).
    
- **Cipher Suites:** Lista degli algoritmi supportati (solo AEAD in TLS 1.3).
    
- **Extensions:** Il cuore della flessibilità di TLS.
    

**Estensioni Fondamentali:**

- `supported_versions`: Elenca le versioni TLS (es. 1.3, 1.2).
    
- `key_share`: Contiene i parametri pubblici per lo scambio chiavi (es. la chiave pubblica ECDHE su curva x25519).
    
- `server_name` (SNI): Indica quale hostname il client vuole contattare (essenziale per virtual hosting).
    
- `signature_algorithms`: Quali algoritmi di firma il client accetta.
    

### ServerHello

È la risposta del server. Contiene:

- **Selected Version:** La versione scelta (TLS 1.3).
    
- **Random:** 32 byte casuali del server.
    
- **Cipher Suite:** L'algoritmo scelto dalla lista del client.
    
- **Key Share:** La controparte della chiave pubblica del server per completare lo scambio Diffie-Hellman.
    

> [!failure] Common Pitfall
> 
> HelloRetryRequest (HRR): Se il server non supporta il gruppo crittografico proposto dal client nel key_share iniziale, risponde con un HRR. Il client deve ricominciare l'handshake inviando un nuovo ClientHello con i parametri corretti. Questo costa 1 RTT aggiuntivo.

---

## 5. Derivazione delle Chiavi (HKDF)

TLS 1.3 usa **HKDF (HMAC-based Key Derivation Function)** per generare tutto il materiale crittografico in modo robusto.

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

**The expansion step (per generating specific keys):**

$$\text{OKM}_i = \text{HKDF-Expand}(\text{PRK}, \text{info}_i, L_i)$$

> [!abstract] Math Analysis
> 
> - **info:** Una stringa di contesto che cambia per ogni chiave (es. "tls13 client handshake traffic secret").
>     
> - **Garantisce la separazione:** Anche se derivano dalla stessa PRK, le chiavi per scopi diversi sono crittograficamente indipendenti.
>     

---

## 6. Transcript Hash e Integrità

TLS mantiene un "registro" hash di tutti i messaggi scambiati.

- **Funzionamento:** Ogni messaggio inviato o ricevuto viene aggiunto a un hash incrementale (Rolling Hash).
    
- **Scopo:**
    
    1. **Input per HKDF:** Le chiavi dipendono da _tutto_ ciò che è stato detto.
        
    2. **Anti-Downgrade:** Un attaccante non può modificare la lista delle Cipher Suites (es. rimuovendo quelle forti) senza alterare l'hash finale.
        
    3. **Messaggio Finished:** È un MAC calcolato sul Transcript Hash. Se la verifica fallisce, significa che qualcuno ha manomesso l'handshake.
        

---

## 7. 0-RTT (Zero Round Trip Time) e Session Resumption

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

---

## 8. Riepilogo Novità TLS 1.3 vs 1.2

|**Caratteristica**|**TLS 1.2**|**TLS 1.3**|
|---|---|---|
|**Handshake**|2-RTT (spesso)|1-RTT (Sempre)|
|**Algoritmi**|Misti (CBC, RC4, etc.)|Solo AEAD (Sicuri e Veloci)|
|**Key Exchange**|RSA statico (no Forward Secrecy)|Effimero obbligatorio (Forward Secrecy sempre)|
|**Privacy**|Certificati in chiaro|Certificati cifrati|
|**Resumption**|Session ID|PSK / Session Ticket (con 0-RTT)|

---

# IPsec: Architettura e Protocolli di Sicurezza di Rete

**Tags:** #ingegneria #reti #sicurezza #ipsec #vpn #tunneling #network_security

## 1. Introduzione e Obiettivi

IPsec è una suite di protocolli progettata per proteggere i pacchetti IP durante il transito su reti non fidate (come Internet).

L'obiettivo è fornire sicurezza "End-to-End" o "Site-to-Site" agendo direttamente al Livello di Rete (Layer 3).

### Perché IPsec?

A differenza di TLS (che protegge le applicazioni) o WPA (che protegge il link Wi-Fi), IPsec protegge tutto il traffico IP tra due host o gateway, rendendo la sicurezza **trasparente** alle applicazioni.

**Approcci alla sicurezza IP:**

- **Hop-by-hop (Fallimentare):** Decifrare e ricifrare su ogni router. Troppo costoso e insicuro (i router vedono i dati in chiaro).
    
- **End-to-end / Tunneling (IPsec):** I router intermedi inoltrano solo il testo cifrato. La sicurezza è gestita solo agli estremi.
    

---

## 2. Architettura e Protocolli Fondamentali

IPsec non è un singolo protocollo, ma un framework che utilizza due header specifici per incapsulare e proteggere il payload IP.

### Authentication Header (AH)

- **Funzione:** Fornisce autenticazione dell'origine e integrità dei dati.
    
- **Limitazione:** **NON** fornisce confidenzialità (niente crittografia, i dati viaggiano in chiaro).
    
- **Copertura:** Protegge il payload e parte dell'header IP originale (quelli immutabili).
    

### Encapsulating Security Payload (ESP)

- **Funzione:** Fornisce confidenzialità (crittografia), autenticazione, integrità e protezione anti-replay.
    
- **Funzionamento:** Incapsula l'intero pacchetto (o il payload) e lo cifra.
    
- **Nota:** È il protocollo più usato oggi.
    

![[SCREEN_SLIDE_31_ARCHITECTURE]]

> [!abstract] Visual Analysis
> 
> What to look at: La differenza tra la modalità "Host-to-Host" (Transport Mode) e "Gateway-to-Gateway" (Tunnel Mode).
> 
> Meaning:
> 
> - Nel **Tunnel Mode** (Gateway), l'intero pacchetto IP originale viene messo dentro un _nuovo_ pacchetto IPsec.
>     
> - Nel **Transport Mode** (Host), viene aggiunto solo l'header IPsec tra l'header IP originale e il payload.
>     

---

## 3. Servizi di Sicurezza: Confronto AH vs ESP

> [!tip] Exam Focus
> 
> Ricorda che solo ESP offre la confidenzialità. AH è usato raramente oggi a causa di problemi con il NAT.

|**Servizio**|**AH**|**ESP (solo cifratura)**|**ESP (cifratura + auth)**|
|---|---|---|---|
|**Confidenzialità**|❌ No|✅ Sì|✅ Sì|
|**Integrità Dati**|✅ Sì|❌ No|✅ Sì|
|**Autenticazione Origine**|✅ Sì|❌ No|✅ Sì|
|**Anti-Replay**|✅ Sì|✅ Sì|✅ Sì|

---

## 4. Il Concetto di Security Association (SA)

La **Security Association (SA)** è il concetto chiave di IPsec. È un "contratto" logico unidirezionale tra mittente e destinatario che definisce _come_ proteggere il traffico.

**The logical definition of an SA is:**

$$\text{SA} = \text{Unidirectional Relationship} \ (\text{Sender} \to \text{Receiver})$$

> [!abstract] Math Analysis
> 
> Poiché è unidirezionale, per una comunicazione bidirezionale (A $\leftrightarrow$ B) servono due SA distinte: una per A $\to$ B e una per B $\to$ A.

### Identificazione Univoca della SA

Ogni SA è identificata univocamente da una tripla di valori:

1. **SPI (Security Parameters Index):** Un'etichetta numerica a 32 bit presente nell'header IPsec.
    
2. **IP Destination Address:** L'indirizzo dell'endpoint della SA.
    
3. **Security Protocol ID:** AH o ESP.
    

### Parametri della SA

La SA contiene tutti i segreti e le configurazioni:

- **Chiavi crittografiche:** Per cifratura e autenticazione.
    
- **Algoritmi:** Es. AES-GCM per cifratura, SHA-256 per integrità.
    
- **Sequence Number Counter:** Un contatore a 32 bit per prevenire attacchi di Replay.
    
- **Lifetime:** Quanto dura la chiave (tempo o volume dati).
    

---

## 5. Database di Gestione: SAD e SPD

Il funzionamento di IPsec si basa su due database presenti nel kernel del sistema operativo o nel router.

### A. Security Policy Database (SPD)

È il "Cervello". Decide cosa fare con il traffico.

Contiene le regole di alto livello (Policy) che classificano i pacchetti in tre azioni:

1. **Protect:** Applica IPsec (crea o usa una SA).
    
2. **Bypass:** Lascia passare in chiaro (es. traffico DNS locale).
    
3. **Discard:** Scarta il pacchetto (Firewalling).
    

Logic for Traffic Selector (TS):

Il traffico viene selezionato basandosi su campi come:

- IP Sorgente / Destinazione (o subnet).
    
- Porta TCP/UDP Sorgente / Destinazione.
    
- Protocollo (TCP, UDP, ICMP).
    

### B. Security Association Database (SAD)

È il "Braccio". Contiene le SA attive.

Quando un pacchetto deve essere protetto, il sistema consulta il SAD per trovare le chiavi e gli algoritmi da usare.

**Packet Processing Flow (Outbound):**

$$\text{Packet} \xrightarrow{\text{Check SPD}} \text{Action: Protect} \xrightarrow{\text{Find SA in SAD}} \xrightarrow{\text{Encrypt/Encap}} \to \text{Network}$$

---

## 6. Pro e Contro di IPsec

### Vantaggi

- **Trasparenza:** Le applicazioni non sanno che IPsec esiste; non devono essere modificate.
    
- **Sicurezza Perimetrale:** Eccellente per creare VPN Site-to-Site, garantendo che tutto il traffico tra due filiali sia cifrato.
    
- **Robustezza:** Algoritmi forti e resistenza agli attacchi di replay.
    

### Svantaggi

- **Complessità:** Configurare IPsec (specialmente IKE, il protocollo di scambio chiavi) è difficile.
    
- **Problemi con NAT:** IPsec (specialmente AH, ma anche ESP) rompe il principio del NAT (Network Address Translation). Richiede meccanismi extra come "NAT-Traversal" (incapsulamento in UDP).
    
- **Overhead:** L'aggiunta di header aumenta la dimensione del pacchetto, causando frammentazione (MTU issues).
    
- **Nessuna Autenticazione Utente:** IPsec autentica la macchina (IP), non l'utente umano (a differenza di TLS o SSH).
    

> [!failure] Common Pitfall
> 
> NAT vs IPsec: Il NAT modifica l'header IP (cambia l'indirizzo sorgente) e i checksum TCP/UDP.
> 
> - **AH:** Autentica l'header IP. Se il NAT lo cambia, la verifica di integrità **fallisce sempre**. AH è incompatibile con il NAT.
>     
> - **ESP:** Cifra i dati. Se il NAT cambia le porte (PAT) che sono cifrate, il NAT non può funzionare. Serve incapsulare ESP dentro UDP port 4500.


---

## 1. Le Modalità Operative: Transport vs Tunnel

IPsec può proteggere i pacchetti in due modi distinti, a seconda di dove viene applicato (sugli host finali o sui gateway).

### A. Transport Mode (End-to-End)

- **Utilizzo:** Comunicazione diretta tra due host (es. Server-to-Server).
    
- **Funzionamento:** L'header IP originale viene mantenuto. L'header IPsec (AH o ESP) viene inserito **tra** l'header IP originale e il payload (TCP/UDP).
    
- **Limitazione:** L'indirizzo IP sorgente/destinazione è visibile in chiaro. Non nasconde la topologia della rete.
    

### B. Tunnel Mode (Site-to-Site)

- **Utilizzo:** VPN tra due Gateway (Router/Firewall) o tra Host e Gateway.
    
- **Funzionamento:** L'intero pacchetto IP originale (header + dati) viene cifrato/autenticato e incapsulato dentro un **nuovo pacchetto IP**.
    
- **Vantaggio:** Nasconde gli indirizzi IP interni (quelli originali). Chi intercetta vede solo gli IP dei due Gateway esterni.
    

![[SCREEN_SLIDE_45_MODES]]

> [!abstract] Visual Analysis
> 
> What to look at: La posizione degli header.
> 
> Meaning:
> 
> - **Transport:** `[IP Orig] [IPsec] [Payload]`
>     
> - Tunnel: [IP Nuovo] [IPsec] [IP Orig] [Payload]
>     
>     Nel modo Tunnel, il pacchetto originale diventa il payload del nuovo pacchetto.
>     

---

## 2. Authentication Header (AH)

Il protocollo **AH** fornisce integrità e autenticazione, ma **NON** confidenzialità (i dati sono leggibili).

### Struttura dell'Header

L'header AH è posizionato dopo l'header IP e prima del protocollo di livello superiore (o ESP).

**Struttura dei Campi:**

- **Next Header:** Indica il protocollo successivo (TCP, UDP, etc.).
    
- **Payload Length:** Lunghezza dell'header AH.
    
- **SPI (Security Parameters Index):** Identifica la Security Association (SA).
    
- **Sequence Number:** Contatore anti-replay.
    
- **Authentication Data (ICV):** Il valore HMAC calcolato sul pacchetto.
    

### Il Problema dei "Mutable Fields"

AH autentica l'intero pacchetto, incluso l'header IP. Tuttavia, alcuni campi dell'header IP cambiano durante il transito (es. **TTL** - Time To Live, **Checksum**).

- **Logica:** Se AH autenticasse il TTL, ogni router che lo decrementa invaliderebbe la firma.
    
- **Soluzione:** AH considera questi campi come "mutabili" e li pone a zero durante il calcolo dell'HMAC.
    

> [!failure] Common Pitfall
> 
> AH e NAT: Il NAT (Network Address Translation) modifica l'indirizzo IP e il checksum. Poiché AH autentica questi campi (che sono considerati immutabili), il NAT rompe inevitabilmente AH. Se c'è un NAT, AH non funzionerà mai.

---

## 3. Encapsulating Security Payload (ESP)

**ESP** è il protocollo principale oggi, poiché offre **confidenzialità** (cifratura) oltre all'autenticazione.

### Struttura e Incapsulamento

ESP avvolge il payload come un guscio. Ha un header (prima dei dati) e un trailer (dopo i dati).

**Struttura Logica:**

1. **ESP Header:**
    
    - `SPI`: Identifica la SA.
        
    - `Sequence Number`: Anti-replay.
        
2. **Payload (Cifrato):** I dati veri e propri (TCP/UDP/IP originale).
    
3. **ESP Trailer (Cifrato):**
    
    - `Padding`: Riempitivo per allineare i dati alla lunghezza del blocco (es. per AES-CBC).
        
    - `Pad Length`: Quanto padding è stato aggiunto.
        
    - `Next Header`: Tipo di protocollo contenuto.
        
4. **ESP Auth (In chiaro):** L'HMAC che autentica tutto il pacchetto ESP (tranne l'IP esterno).
    

![[SCREEN_SLIDE_52_ESP_STRUCTURE]]

> [!abstract] Visual Analysis
> 
> What to look at: Le frecce che indicano "Confidentiality Coverage" vs "Authentication Coverage".
> 
> Meaning:
> 
> - La cifratura copre dal Payload fino al Next Header.
>     
> - L'autenticazione copre dall'Header ESP fino al Next Header.
>     
> - L'Auth Data stesso non è cifrato né autenticato (è il risultato dell'autenticazione).
>     

---

## 4. IKEv2: Internet Key Exchange

Configurare manualmente le chiavi IPsec (Manual Keying) non scala. **IKE** è il protocollo che automatizza la negoziazione delle Security Association (SA) e la generazione delle chiavi.

### Architettura IKE

IKE funziona separando il piano di controllo dal piano dati.

1. **IKE SA (Control Plane):** Un canale sicuro per gestire il protocollo IKE stesso.
    
2. **Child SA (Data Plane):** Le SA IPsec (ESP/AH) usate per proteggere il traffico utente.
    

### Le Fasi di IKEv2

IKEv2 semplifica il processo rispetto a v1, riducendo lo scambio a 4 messaggi principali per stabilire la connessione.

#### Fase 1: IKE_SA_INIT

Negoziazione dei parametri crittografici di base.

Message Exchange:

$$\text{Initiator} \xrightarrow{\text{HDR, SA, KE, Nonce}} \text{Responder}$$

$$\text{Responder} \xrightarrow{\text{HDR, SA, KE, Nonce, [CertReq]}} \text{Initiator}$$

> [!abstract] Technical Logic
> 
> - **SA:** Proposte di algoritmi (es. "Uso AES-256 e SHA-256").
>     
> - **KE (Key Exchange):** Scambio delle chiavi pubbliche Diffie-Hellman per generare il segreto condiviso.
>     
> - **Nonce:** Numeri casuali per garantire freschezza e unicità.
>     

#### Fase 2: IKE_AUTH

Autenticazione delle identità e creazione della prima Child SA (tunnel IPsec).

Message Exchange (Encrypted):

$$\text{Initiator} \xrightarrow{\text{HDR, Encrypted \{ IDi, Auth, SA2, TSi, TSr \}}} \text{Responder}$$

> [!abstract] Technical Logic
> 
> - **IDi:** Identità dell'iniziatore (es. IP o FQDN).
>     
> - **Auth:** Prova dell'identità (Firma digitale o Pre-Shared Key).
>     
> - **TS (Traffic Selectors):** Regole per il traffico da proteggere (es. "Tutto il traffico dalla subnet 10.0.1.0/24").
>     

#### Fase 3: CREATE_CHILD_SA (Opzionale/Successiva)

Usata per:

- Creare ulteriori tunnel IPsec con parametri diversi.
    
- **Rekeying:** Ruotare le chiavi crittografiche per mantenere la sicurezza nel tempo (PFS - Perfect Forward Secrecy).
    

---

## 5. Riepilogo IKE vs IPsec

È fondamentale distinguere i ruoli:

|**Caratteristica**|**IKE (Porta UDP 500)**|**IPsec (Protocollo IP 50/51)**|
|---|---|---|
|**Ruolo**|Negoziatore ("Avvocato")|Trasportatore ("Corriere Blindato")|
|**Scopo**|Autenticare i peer e generare chiavi|Cifrare e autenticare i pacchetti dati|
|**Sicurezza**|Protegge se stesso (IKE SA)|Protegge il traffico utente (Child SA)|
|**Durata**|Lunga (Gestione sessione)|Breve/Media (Rinnovata spesso)|

> [!tip] Exam Focus
> 
> Traffic Selectors (TS): In IKEv2, i TS negoziano quali pacchetti devono finire nel tunnel. Se il TS dell'Initiator non combacia con quello del Responder (es. uno vuole proteggere solo HTTP, l'altro tutto il traffico), la negoziazione fallisce.