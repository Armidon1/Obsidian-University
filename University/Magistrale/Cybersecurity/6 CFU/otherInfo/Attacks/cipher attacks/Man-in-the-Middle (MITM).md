# Man-in-the-Middle (MITM) — spiegazione rapida e completa

### Cos’è

Un **Man-in-the-Middle (MITM)** (anche definito come **"Meddler-In-The-Middle"**) è un attacco in cui un avversario si **inserisce tra due entità** (es. client ⇄ server) per **intercettare, leggere, modificare o reindirizzare** le comunicazioni senza che le parti se ne accorgano.

---

### Tipi principali

- **Passive MITM:** l’attaccante ascolta/ registra il traffico (e.g. sniffing).
    
- **Active MITM:** l’attaccante altera o inietta messaggi (e.g. modifica pagine web, cambia risposte DNS).
    
- **MitM legittimo (corporate proxies):** proxy aziendali che terminano TLS per ispezione — tecnicamente MITM ma autorizzato.
    

---

### Tecniche comuni usate dagli attaccanti

- **ARP spoofing / ARP poisoning:** in LAN per farsi passare per gateway.
    
- **DNS spoofing / DNS cache poisoning:** rispondere con IP falsi a query DNS.
    
- **Rogue Wi-Fi / Evil Twin:** creare hotspot con nome simile per far connettere le vittime.
    
- **SSL/TLS stripping:** degradare una connessione HTTPS a HTTP (es. via proxy non verificante).
    
- **Proxy/forwarding malevolo:** catturare traffico su routing compromesso.
    
- **Compromissione del router/modem:** cambiare DNS o reindirizzamenti.
    
- **Certificate spoofing / CA compromessa:** presentare certificati fasulli o usare CA malevole.
    
- **Strumenti:** mitmproxy, Ettercap, Burp Suite, Responder, Wireshark (per l’attaccante e per il difensore).
    

---

### Cosa può fare l’attaccante

- Leggere dati sensibili (password, cookie, token).
    
- Modificare contenuti (iniettare malware, cambiare transazioni).
    
- Eseguire session hijacking o replay.
    
- Rubare credenziali o exfiltrare dati.
    

---

### Segnali che potresti essere vittima di un MITM

- Avvisi del browser su certificati non validi / errore HTTPS.
    
- Certificati cambiati improvvisamente per servizi noti.
    
- Connessioni lente, molte disconnessioni o redirect strani.
    
- Login che richiedono re-autenticazione ripetuta.
    
- Inserimento di contenuti/annunci non previsti su siti “familiari”.
    

---

### Contromisure efficaci (utente / amministratore / sviluppatore)

**A livello utente / device**

- Usa **HTTPS** (non ignorare gli avvisi di certificato).
    
- Usa **VPN** affidabile su reti pubbliche.
    
- Evita reti Wi-Fi aperte; preferisci WPA3/WPA2 con password forte.
    
- Aggiorna OS, browser e firmware del router.
    
- Abilita 2-FA / MFA su account critici.
    
- Controlla certificati (fingerprint) se accedi a servizi sensibili da reti sospette.
    

**A livello applicazione / protocollo**

- Usa **TLS corretto** (versioni aggiornate). Configura cipher suite sicure e **AEAD**.
    
- Implementa **HSTS** per prevenire downgrade a HTTP.
    
- Verifica correttamente i certificati (non disabilitare la verifica).
    
- Usa **Certificate Pinning** con cautela (mobile apps) o meccanismi moderni tipo Expect-CT/HPKP è deprecato.
    
- Usa **mutual TLS (mTLS)** dove opportuno per autenticare client/server.
    
- Autentica e valida token lato server; non fare affidamento su dati di rete non verificati.
    

**A livello infrastrutturale / rete**

- Proteggi router e DNS: **DNSSEC** per validare risposte DNS.
    
- Segmentazione di rete e DHCP/ARP protection (dynamic ARP inspection).
    
- Monitoraggio e IDS/IPS per rilevare ARP poisoning, rogue AP, anomalie DNS.
    
- Usare **TLS termination** solo quando necessario e con controlli (HSM, logging, policy).
    
- Disabilitare management remoto su WAN o proteggerlo con accesso sicuro.
    

---

### Best practice rapide

- Non ignorare avvisi di sicurezza del browser.
    
- Non immettere credenziali su reti pubbliche non sicure senza VPN.
    
- Rotazione delle chiavi, revoca certificati compromessi, e logging centralizzato per forensics.
    
- Testa le implementazioni con strumenti (scansione TLS, pen-test, controllo HSTS/HSTS preload, simulazione MitM).
    

---

### In breve

> MITM = attaccante si mette **in mezzo** alla comunicazione per leggere o manipolare il traffico.  
> **Prevenzione**: TLS correttamente configurato, verifica dei certificati, uso di AEAD/mTLS, DNSSEC, VPN su reti insicure, aggiornamenti e monitoraggio di rete.