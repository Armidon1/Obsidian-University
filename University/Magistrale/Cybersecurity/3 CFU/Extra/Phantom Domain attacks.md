# DNS Phantom Domain Attacks

**Tags:** #CyberSecurity #DNS #DDoS #Availability #AttackVector 
**Fonte:** [[6 - CS Application Level - DNS Security]]

---

## 📌 Concetto Chiave

Il **Phantom Domain Attack** è classificato come una minaccia specifica alla **Disponibilità (Availability)** dell'infrastruttura DNS.

Nelle slide, viene elencato insieme al **DDoS Amplification** e ai **NXDOMAIN floods** come una delle vulnerabilità principali che mirano a degradare o interrompere il servizio DNS, rendendo i risolutori incapaci di rispondere alle richieste legittime.

## ⚙️ Il Problema di Sicurezza

Come evidenziato dalle slide, il protocollo DNS standard **non include meccanismi di protezione nativa** per garantire la disponibilità (Availability status: "Non-existent in standard DNS").

Questo tipo di attacco mira a esaurire le risorse del server bersaglio. Anche se le slide non dettagliano il meccanismo specifico dei _Phantom Domain_ (a differenza del Cache Poisoning), il contesto indica che, similmente ai flood NXDOMAIN, l'obiettivo è stressare l'infrastruttura di risoluzione.

## ⚠️ Relazione con DNSSEC

È cruciale notare che l'implementazione di **DNSSEC** non mitiga questa minaccia.

- DNSSEC è progettato per garantire **Integrità** e **Autenticazione**, ma **non fornisce protezione contro i DoS (Denial of Service)**.
- Anzi, le slide specificano che DNSSEC **aumenta il rischio DDoS** (e quindi l'efficacia di attacchi alla disponibilità come i Phantom Domain) a causa dell'aumento delle dimensioni dei pacchetti e del carico computazionale necessario per la verifica crittografica.

---

## 🔗 Collegamenti

- [[DNS NXDOMAIN Floods]] (Altro attacco alla disponibilità citato insieme ai Phantom Domain)
- [[DDoS Amplification]]
- [[DNSSEC]] (Non protegge da questo attacco)
- [[DNS Security Goals]] (Confidenzialità, Integrità, Disponibilità)