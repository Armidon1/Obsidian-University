# 🎭 Spoofing

### Definizione

Lo **Spoofing** (dall'inglese _to spoof_, ingannare o parodiare) è un tipo di attacco informatico in cui un aggressore **falsifica i dati di identificazione** (come indirizzi IP, indirizzi MAC, identità del mittente e-mail, o numeri di telefono) per mascherarsi da entità attendibile o legittima.

L'obiettivo principale dello Spoofing è **ottenere accesso** a sistemi protetti, **bypassare i controlli di sicurezza** come i firewall o le policy di autenticazione, o **raccogliere informazioni sensibili** ingannando la vittima o il sistema di destinazione.

In sintesi, si tratta di un attacco basato sulla **falsificazione dell'identità** alla base dello stack di rete o a livello applicativo.

---

### Dettagli Tecnici e Tipi Comuni

Lo Spoofing si manifesta a diversi livelli del modello OSI:

#### 1. IP Spoofing (Livello 3 - Rete)

- **Tecnica:** L'aggressore modifica l'**indirizzo IP di origine** nei pacchetti dati per far sembrare che provengano da un host diverso.
    
- **Implicazioni:**
    
    - **Attacchi DoS/DDoS:** Utilizzato per nascondere la vera fonte dell'attacco (specialmente nei _reflected_ o _amplified_ DoS), rendendo estremamente difficile il _tracing_ e il _blocking_.
        
    - **Bypass di Filtri:** Se un firewall o un router si fida dell'IP di un host interno specifico, l'IP Spoofing può essere usato per eludere i controlli di accesso basati su indirizzo.
        
- **Contromisure:** Implementazione di **filtri _Ingress_ e _Egress_** da parte degli ISP e sui router di confine per garantire che l'indirizzo IP sorgente di un pacchetto provenga da una rete che è effettivamente dietro quel router.
    

#### 2. ARP Spoofing (Livello 2 - Data Link)

- **Tecnica:** L'aggressore invia messaggi **ARP (Address Resolution Protocol)** falsificati sulla rete locale (LAN). Questo lega l'indirizzo MAC dell'aggressore all'indirizzo IP di un gateway o di un altro host.
    
- **Implicazioni:**
    
    - **Man-in-the-Middle (MITM):** Permette all'aggressore di intercettare tutto il traffico destinato al gateway (es. il router) o all'host preso di mira, prima di inoltrarlo alla destinazione reale.
        
    - **Session Hijacking:** Utilizzato per dirottare le sessioni di comunicazione.
        
- **Contromisure:** Utilizzo di **ARP statico** per le voci critiche, implementazione di protocolli di sicurezza come **Dynamic ARP Inspection (DAI)** sugli switch.
    

#### 3. DNS Spoofing / Cache Poisoning (Livello 7 - Applicazione)

- **Tecnica:** L'aggressore inietta dati DNS falsificati nel resolver di un server DNS (Cache Poisoning) o direttamente nell'host vittima.
    
- **Implicazioni:**
    
    - **Phishing/Malware:** Quando la vittima cerca un sito legittimo (es. `banca.it`), il resolver avvelenato la indirizza a un sito malevolo controllato dall'aggressore, permettendo il furto di credenziali.
        
- **Contromisure:** Implementazione di **DNSSEC (Domain Name System Security Extensions)** per autenticare l'origine dei dati DNS, hardening dei server DNS.
    

#### 4. Email Spoofing (Livello 7 - Applicazione)

- **Tecnica:** L'aggressore falsifica l'indirizzo del mittente (il campo `From:` nell'header del messaggio) per far sembrare che l'e-mail provenga da una fonte fidata (es. un collega, un dirigente, una banca).
    
- **Implicazioni:**
    
    - **Phishing e BEC (Business Email Compromise):** È la base per la maggior parte degli attacchi di phishing e di truffe finanziarie mirate. Sfrutta la **mancanza di autenticazione intrinseca** dell'SMTP di base.
        
- **Contromisure:** Implementazione rigorosa dei protocolli di autenticazione a livello di dominio: **SPF** (Sender Policy Framework), **DKIM** (DomainKeys Identified Mail) e **DMARC** (Domain-based Message Authentication, Reporting, and Conformance).
    

---

### Misure di Prevenzione per Ingegneri

Per gli ingegneri informatici, la difesa contro lo Spoofing richiede un approccio a più livelli:

1. **Validazione degli Indirizzi:** Implementare **filtri _Ingress/Egress_ robusti** sui router e sui firewall per impedire che pacchetti con indirizzi sorgente falsificati entrino o escano dalla rete.
    
2. **Autenticazione E-mail:** **Configurare e monitorare i record DNS SPF, DKIM e DMARC** per i domini aziendali. Questo è lo strumento più efficace contro l'Email Spoofing e il phishing.
    
3. **Sicurezza della Rete Locale:** Utilizzare l'**HTTPS** in modo che il traffico sia cifrato a prescindere da attacchi MITM a livello ARP. Abilitare la **Dynamic ARP Inspection (DAI)** sugli switch per prevenire l'ARP Spoofing.
    
4. **Sicurezza DNS:** Implementare o richiedere l'uso di **DNSSEC** e utilizzare resolver DNS affidabili che prevengano il Cache Poisoning.
    
5. **Autenticazione Forte:** Adottare sistemi che utilizzano meccanismi di autenticazione crittografica (come le firme digitali o le connessioni TLS/SSL) a livello applicativo, rendendo irrilevante la falsificazione degli indirizzi sottostanti.