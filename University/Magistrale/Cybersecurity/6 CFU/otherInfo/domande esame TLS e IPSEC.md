guardare sempre prima [[CS 6cfu - Domande esame]]

Certamente! Ecco la spiegazione dettagliata per **TLS** e **IPsec**, strutturata con il metodo dell'**Opzione B** (Analisi approfondita basata sulle domande d'esame 2012-2025).

---

### **Transport Layer Security (TLS)**

TLS è il protocollo di sicurezza de facto per il web (HTTPS). Gli esami si concentrano su cosa fa, come lo fa e come differisce da IPsec.

#### 1. TLS vs IPsec: Differenze e Scenari (Domanda Classica)

La Domanda d'Esame:

"Descrivi i principali obiettivi di sicurezza di TLS e IPsec. In quale scenario TLS è più utile di IPsec? In quale scenario IPsec è più utile di TLS?"

**La Spiegazione (Il "Perché"):**

- **TLS (Transport Layer):** Funziona sopra TCP. Protegge l'applicazione (process-to-process).
    
    - _Scenario:_ Voglio comprare su Amazon. Il mio browser parla col server di Amazon. Non mi serve configurare nulla sul router o sul sistema operativo. TLS è trasparente per la rete ma richiede che l'applicazione (browser) lo supporti.
        
- **IPsec (Network Layer):** Funziona al livello IP. Protegge il pacchetto (host-to-host o network-to-network).
    
    - _Scenario:_ Due filiali di un'azienda (Roma e Milano) devono collegare le loro reti LAN come se fossero una sola. Uso IPsec (VPN Tunnel). Tutte le applicazioni (mail, file sharing, VoIP) passano nel tunnel senza saperlo.
        

**Cosa scrivere all'esame:**

- **TLS:** Sicurezza End-to-End a livello di trasporto/applicazione.
    
    - _Meglio quando:_ Serve granularità (proteggere solo una specifica transazione web), portabilità (funziona ovunque senza permessi di root) e facilità d'uso per l'utente finale (HTTPS).
        
- **IPsec:** Sicurezza a livello di rete (pacchetti IP).
    
    - _Meglio quando:_ Serve proteggere _tutto_ il traffico tra due sedi (Site-to-Site VPN) o proteggere protocolli che non supportano nativamente la crittografia (legacy apps). Trasparente alle applicazioni.
        

---

#### 2. Handshake e Attacchi (MITM & Downgrade)

La Domanda d'Esame:

"Fornisci una descrizione black-box di TLS. Assumendo un'implementazione perfetta, quali attacchi sono ancora possibili?"

La Spiegazione (Il "Perché"):

TLS protegge il canale.

- **Black-box:** Input $\to$ Canale TLS $\to$ Output. Garantisce confidenzialità, integrità e autenticità del server.
    
- **Attacchi Residui:**
    
    1. **Trust Store Compromesso:** Se un attaccante compromette una Root CA nel tuo browser, può generare un certificato falso per `google.com` e farti un MITM perfetto. TLS si fida della CA, quindi è "bucato" alla radice.
        
    2. **Traffic Analysis:** Anche se cifrato, l'attaccante vede _chi_ stai chiamando (IP destinazione) e _quanto_ dati scambi (lunghezza).
        
    3. **Downgrade Attack:** Un attaccante si mette in mezzo durante l'handshake iniziale (che è in chiaro) e modifica la lista delle Cipher Suite, dicendo al server: "Il client supporta solo cifrari deboli (export grade)". Se il server accetta, la connessione usa una chiave debole che l'attaccante può rompere. (TLS 1.3 mitiga questo firmando l'intero transcript).
        

**Cosa scrivere all'esame:**

- **Descrizione:** Protocollo che fornisce un canale sicuro sopra TCP, garantendo Autenticazione (tramite certificati X.509), Confidenzialità (cifratura simmetrica) e Integrità (MAC).
    
- **Attacchi:** Compromissione delle CA (PKI failure), Attacchi al client (malware), Traffic Analysis (metadati visibili), Downgrade Attacks (su versioni vecchie).
    

---

### **IPsec (Internet Protocol Security)**

IPsec è complesso e modulare. Le domande vertono sulla struttura dei pacchetti (AH vs ESP) e sulle modalità operative (Transport vs Tunnel).

#### 1. AH vs ESP (Il dilemma del NAT)

La Domanda d'Esame:

"Qual è la differenza tra AH e ESP? Perché AH ha problemi con il NAT?"

**La Spiegazione (Il "Perché"):**

- **AH (Authentication Header):** Firma digitalmente tutto il pacchetto, incluso l'header IP (indirizzo sorgente/destinazione).
    
    - _Il problema NAT:_ Il NAT (Network Address Translation) cambia l'indirizzo IP nell'header per far uscire il pacchetto su Internet. Se cambi l'IP, la firma di AH non corrisponde più. Il pacchetto viene scartato. AH è incompatibile col NAT.
        
- **ESP (Encapsulating Security Payload):** Cifra e firma solo il payload (i dati dentro).
    
    - _NAT-Traversal:_ ESP non firma l'header IP esterno. Quindi il NAT può cambiare l'IP senza rompere l'integrità del pacchetto ESP.
        

**Cosa scrivere all'esame:**

- **AH:** Fornisce Integrità e Autenticazione, ma **NO Confidenzialità** (niente cifratura). Autentica anche l'header IP, rendendolo incompatibile con il NAT (che modifica l'header).
    
- **ESP:** Fornisce Integrità, Autenticazione e **Confidenzialità** (Cifratura). È più flessibile e supporta il NAT-Traversal (incapsulamento in UDP).
    

#### 2. Modalità Transport vs Tunnel

La Domanda d'Esame:

"Disegna/Descrivi la differenza tra Transport Mode e Tunnel Mode in IPsec."

**La Spiegazione (Il "Perché"):**

- **Transport Mode:** "Proteggiamo la conversazione tra me e te".
    
    - L'header IP originale resta. Si aggiunge l'header IPsec _dopo_ l'IP e _prima_ dei dati (TCP).
        
    - Usato per connessioni Host-to-Host (es. Sysadmin che gestisce un Server remoto).
        
- **Tunnel Mode:** "Creiamo un tubo segreto tra due reti".
    
    - Il pacchetto originale (IP+Dati) viene preso, cifrato e messo dentro un _nuovo_ pacchetto IP.
        
    - L'IP esterno è quello dei Gateway VPN. L'IP interno è quello privato dei PC.
        
    - Usato per VPN Gateway-to-Gateway.
        

**Cosa scrivere all'esame:**

- **Transport:** Protegge solo il payload (L4). Header IP originale visibile. `[IP | ESP | TCP | Data]`. Uso: End-to-End.
    
- **Tunnel:** Protegge l'intero pacchetto IP originale. Nuovo Header IP aggiunto. `[New IP | ESP | Orig IP | TCP | Data]`. Uso: VPN (Site-to-Site).
    

#### 3. I Database: SPD e SAD

La Domanda d'Esame (Concettuale):

"Come decide IPsec quale traffico cifrare?"

La Spiegazione (Il "Perché"):

Il kernel non può cifrare tutto (sarebbe lento e inutile per traffico pubblico).

- **SPD (Security Policy Database):** È il "Manager". Contiene le regole di alto livello: "Tutto il traffico verso la subnet 10.0.0.0/24 deve essere cifrato". (Policy: BYPASS, DISCARD, PROTECT).
    
- **SAD (Security Association Database):** È l'"Ingegnere". Contiene i parametri tecnici attivi per cifrare verso 10.0.0.1: "Usa chiave 0x1234, algoritmo AES, SPI 500".
    

**Cosa scrivere all'esame:**

- **SPD:** Contiene le policy di sicurezza (Cosa proteggere). Regole basate su selettori (IP, Port, Protocol).
    
- **SAD:** Contiene le Security Associations attive (Come proteggere). Parametri crittografici (Chiavi, SPI, Algoritmi) negoziati tramite IKE.
    

#### 4. IKE (Internet Key Exchange)

La Domanda d'Esame:

"A cosa serve il protocollo IKE in IPsec?"

La Spiegazione (Il "Perché"):

Configurare manualmente le chiavi su 1000 computer è impossibile.

IKE è un protocollo (basato su UDP 500) che permette a due host di:

1. Autenticarsi a vicenda.
    
2. Negoziare gli algoritmi (es. "Usiamo AES o 3DES?").
    
3. Generare le chiavi di sessione in modo sicuro (Diffie-Hellman).
    
4. Creare le voci nel SAD.
    

Cosa scrivere all'esame:

IKE è il protocollo di controllo per IPsec. Automatizza la negoziazione delle Security Associations (SA), l'autenticazione dei peer e lo scambio sicuro delle chiavi (tramite Diffie-Hellman), garantendo anche il periodico rinnovo delle chiavi (Rekeying) per la Perfect Forward Secrecy.