# DNS DDoS Amplification

**Tags:** #CyberSecurity #DNS #DDoS #NetworkSecurity #AttackVector 
**Fonte:** [[6 - CS Application Level - DNS Security]]

---

## 📌 Concetto Chiave

Il **DNS Amplification Attack** è una tipologia di attacco DDoS (Distributed Denial of Service) che sfrutta il protocollo DNS per amplificare il traffico diretto verso una vittima. L'attacco fa leva sulla **larghezza di banda asimmetrica** tra la richiesta DNS (piccola) e la risposta DNS (molto più grande).

## ⚙️ Meccanismo di Attacco

L'attacco segue un flusso preciso che coinvolge tre attori principali: l'attaccante (spesso tramite una botnet), dei risolutori DNS aperti (Open Resolvers) e la vittima.

1. **IP Spoofing:** L'attaccante invia richieste DNS falsificando l'indirizzo IP sorgente, sostituendolo con l'indirizzo IP della vittima.
2. **Open Resolvers:** Le richieste vengono inviate a server DNS configurati come "Open Resolvers" (ricorsivi aperti accessibili da Internet), che rispondono a chiunque.
3. **Query Voluminose:** L'attaccante utilizza query specifiche progettate per generare le risposte più grandi possibili (es. query `ANY` utilizzando l'estensione `EDNS0`).
4. **Riflessione e Amplificazione:** I server DNS inviano le risposte (molto grandi) all'IP della vittima (che non le ha mai richieste), saturando la sua banda.

## 📊 Metriche di Amplificazione

La pericolosità dell'attacco risiede nel rapporto tra la dimensione della richiesta e quella della risposta:

- **Dimensione Richiesta (Input):** ~60 bytes (via UDP).
- **Dimensione Risposta (Output):** 3000+ bytes.
- **Fattore di Amplificazione:** Circa **50x - 70x**.

> _In pratica, con poca larghezza di banda, l'attaccante può generare un traffico enorme verso il target._

## ⚠️ Il Ruolo di DNSSEC

Sebbene **DNSSEC** nasca per garantire integrità e autenticazione dei dati DNS, in questo contesto presenta uno svantaggio collaterale:

- Aggiungendo firme crittografiche (RRSIG, DNSKEY) ai pacchetti, DNSSEC aumenta notevolmente la dimensione delle risposte DNS.
- Di conseguenza, **DNSSEC incrementa il rischio e l'efficacia degli attacchi DDoS**, fornendo un fattore di amplificazione ancora maggiore.

---

## 🔗 Collegamenti

- [[DNS Cache Poisoning]]
- [[DNSSEC]]
- [[Network Protocols]]