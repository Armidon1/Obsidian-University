# 🗑️ Spam (Unsolicited Bulk Email - UBE)

### Definizione

Lo **Spam** (dall'inglese _Unsolicited Bulk Email_ o **UBE**) è l'invio di **messaggi di posta elettronica non richiesti, in grande quantità e in modo indiscriminato** a un vasto numero di destinatari. Sebbene lo spam possa includere qualsiasi contenuto indesiderato, la maggior parte è di natura commerciale, fraudolenta o maligna.

Lo Spam non è un attacco informatico nel senso stretto di _exploit_ o _compromissione_, ma è un **abuso del protocollo SMTP** e un vettore primario per la diffusione di malware, phishing e frodi.

Il termine deriva da un vecchio sketch comico dei Monty Python in cui la parola "Spam" (un marchio di carne in scatola) era onnipresente e indesiderata.

### Dettagli Tecnici e Vettori di Distribuzione

Lo spam si basa sull'efficienza dell'invio massivo e sulla capacità di sfruttare le vulnerabilità del server o del protocollo.

#### 1. Fonti di Invio (Sending Infrastructure)

- **Botnet:** La maggior parte dello spam moderno è inviato da **reti di computer compromessi (_botnet_)** gestiti da un _Command and Control (C2)_ centrale. Ogni "bot" è un computer di un utente ignaro la cui risorsa (indirizzo IP, banda, client SMTP) è sfruttata per l'invio.
    
    - _Implicazione Tecnica:_ Poiché le e-mail provengono da centinaia o migliaia di indirizzi IP diversi e legittimi (seppur compromessi), è difficile bloccarli esclusivamente per indirizzo IP.
        
- **Open Relay:** Server SMTP configurati erroneamente che consentono a _chiunque_ di inviare e-mail a destinatari esterni, abusando della fiducia del server. Sebbene la maggior parte sia chiusa oggi, i _relay_ abusati sono ancora un problema.
    

#### 2. Tecniche di Bypassing

- **Snowshoe Spamming:** Una tattica per evadere i filtri che monitorano gli indirizzi IP ad alto volume. Consiste nell'invio di un **volume molto basso** di messaggi da una **gamma molto ampia** di indirizzi IP, creando una "neve fresca" superficiale (da cui _snowshoe_) che i filtri non riescono a rilevare come traffico ad alto rischio.
    
- **Spamming Polimorfico:** Utilizzo di tecniche per **variare leggermente il contenuto** del messaggio (es. introducendo caratteri casuali o sinonimi) in ogni e-mail inviata, rendendo difficile ai filtri basati su _signature_ o _hash_ rilevare pattern identici.
    
- **Indirizzi Spoofed e Non Spoofed:** Lo spam spesso utilizza indirizzi mittenti falsificati (_spoofed_) o, in alcuni casi, indirizzi validi ma compromessi (se si usa una botnet).
    

#### 3. Raccolta degli Indirizzi (Harvesting)

Gli indirizzi e-mail delle vittime sono spesso raccolti tramite:

- **Web Crawling:** Bot che scansionano siti web pubblici, forum e social media alla ricerca di indirizzi e-mail.
    
- **Attacchi di Dizionario:** Tentativi di indovinare indirizzi validi (es. `info@dominio.it`, `admin@dominio.it`).
    
- **Violazioni di Dati (Data Breaches):** L'acquisto di liste di indirizzi e-mail validi ottenute da precedenti _data breaches_.
    

### Implicazioni di Cybersecurity per Ingegneri

Lo spam è un problema di sicurezza per diverse ragioni che vanno oltre il semplice fastidio:

1. **Vettore di Malware e Phishing:** La maggior parte delle minacce di sicurezza (ransomware, trojan, attacchi di phishing per credenziali) utilizzano lo spam come meccanismo di consegna iniziale. Bloccare lo spam significa bloccare la maggior parte degli attacchi.
    
2. **Resource Exhaustion (Consumo di Risorse):** Lo spam consuma banda di rete, spazio su disco e tempo di elaborazione del server MTA, dei client e dei sistemi di difesa (filtri, antivirus). Un'ondata di spam può agire come un attacco DoS indiretto.
    
3. **Danneggiamento della Reputazione:** Se i server della tua organizzazione (o le macchine degli utenti) vengono compromessi e usati per inviare spam, l'indirizzo IP e il dominio aziendale finiranno rapidamente in **black list internazionali** (es. Spamhaus). Questo danneggia la reputazione di invio legittimo e impedisce alle e-mail aziendali legittime di raggiungere i destinatari.
    

### Misure di Mitigazione Avanzate

Oltre all'uso di filtri antispam di base, gli ingegneri devono concentrarsi sull'implementazione di controlli a livello di protocollo e rete:

1. **Autenticazione E-mail (Livello Dominio):** Implementazione rigorosa e monitoraggio di **SPF, DKIM e DMARC**. Questi protocolli consentono ai server riceventi di verificare se l'e-mail proviene da un server autorizzato (difesa contro lo _spoofing_).
    
2. **Greylisting:** Una tecnica in cui il server ricevente rifiuta temporaneamente il primo tentativo di consegna. I server di spam (o botnet) di solito non ritentano la consegna, mentre i server di posta legittimi lo fanno.
    
3. **Honeypot e Blacklist Dinamiche:** Utilizzare indirizzi e-mail civetta (_honeypot_) pubblicati solo per i _crawler_ di spam. Qualsiasi e-mail inviata a quell'indirizzo viene utilizzata per alimentare **liste nere dinamiche** (RBL - Real-time Blackhole Lists) che bloccano l'IP mittente.
    
4. **Rate Limiting e Limiti di Connessione:** Configurare il server MTA per limitare il numero di connessioni SMTP o il volume di messaggi che un singolo indirizzo IP può inviare in un determinato intervallo di tempo, contrastando efficacemente il _bombing_ e lo _snowshoe spamming_.
    
5. **Reverse DNS Lookup:** Bloccare le connessioni da server che non hanno un record DNS inverso (PTR) valido, un indicatore comune di server di spam.