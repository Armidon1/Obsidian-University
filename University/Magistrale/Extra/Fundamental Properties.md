Ecco una **sintesi completa e precisa** delle **proprietà fondamentali** per la **Cybersecurity** e i **sistemi distribuiti affidabili (Dependable Distributed Systems)**, con definizioni chiare e distinzioni concettuali.

## **Dependability (Affidabilità complessiva)**
[[Dependability]]

> Proprietà globale che rappresenta quanto un sistema sia **affidabile, sicuro e funzionante correttamente** nel tempo.  
> **Componenti principali:**

-  [[Fundamental Properties#**Availability (Disponibilità)**|Availability]]
    
-  [[Fundamental Properties#**Reliability (Affidabilità)**|Reliability]]
    
- [[Fundamental Properties#**Safety (Sicurezza funzionale)**|Safety]]
    
- [[Fundamental Properties#**Integrity (Integrità)**|Integrity]]
    
- [[Fundamental Properties#**Maintainability (Manutenibilità)**|Maintainability]]
    

---

## **Security (Sicurezza Informatica)**
[[Security]]

> Capacità di un sistema di **proteggere le risorse, dati e servizi da accessi non autorizzati, modifiche o interruzioni intenzionali**.  
> **Esempio:** firewall, crittografia dei dati in transito e a riposo, sistemi di autenticazione e autorizzazione robusti.
**Componenti principali (derivati dalla CIA triad):**
- [[Fundamental Properties#**Confidentiality (Riservatezza)**|Confidentiality]]
- [[Fundamental Properties#**Integrity (Integrità)**|Integrity]]
- [[Fundamental Properties#**Availability (Disponibilità)**|Availability]]

>Altri attributi strettamente correlati:
>
>- [[Fundamental Properties#**Authenticity (Autenticità)**|Authenticity]]: verificare che gli utenti o i messaggi siano genuini.  
>- [[Fundamental Properties#**Non-Repudiation (Non ripudio)**|Non-Repudiation]]: impedire che una parte neghi di aver compiuto un’azione.  
>- [[Fundamental Properties#**Accountability (Responsabilità / Tracciabilità)**|Accountability]]: rendere tracciabili le azioni degli utenti o processi.
    

**Minacce tipiche:** malware, phishing, attacchi DDoS, insider threat, man-in-the-middle, data breaches.  
**Contromisure comuni:** crittografia, autenticazione forte, patching regolare, monitoraggio, auditing, segmentazione della rete.

---

### **Confidentiality (Riservatezza)**
[[Confidentiality]]

> Garantisce che le informazioni siano accessibili solo a chi è autorizzato.  
> **Esempio:** la cifratura dei dati in transito impedisce che un attaccante legga un messaggio intercettato.  
> **Minaccia tipica:** eavesdropping, data leakage.

---

### **Integrity (Integrità)**
[[Integrity]]

> Assicura che i dati e i sistemi non siano alterati o distrutti in modo non autorizzato.  
> **Esempio:** un hash crittografico o una firma digitale protegge un file da modifiche.  
> **Minaccia tipica:** man-in-the-middle, data tampering.

---

### **Availability (Disponibilità)**
[[Availability]]

> I sistemi e i dati devono essere sempre accessibili agli utenti autorizzati quando servono.  
> **Esempio:** ridondanza, backup, load balancing.  
> **Minaccia tipica:** attacchi DoS/DDoS, guasti hardware.

---

### **Authenticity (Autenticità)**
[[Authenticity]]

> Garanzia che un’entità (utente, servizio o messaggio) sia genuina e non falsificata.  
> **Esempio:** autenticazione tramite certificato digitale o token.  
> **Minaccia tipica:** spoofing, phishing.

---

### **Non-Repudiation (Non ripudio)**
[[Non-Repudiation]]

> Impedisce a una parte di negare successivamente le proprie azioni o transazioni.  
> **Esempio:** una firma digitale dimostra che un messaggio è stato effettivamente inviato da un mittente specifico.  
> **Strumenti:** firme digitali, log immutabili, timestamping.

---

### **Reliability (Affidabilità)**
[[Reliability]]

> Capacità del sistema di fornire servizi corretti senza errori per un certo periodo di tempo.  
> **Esempio:** un server che funziona per mesi senza crash o malfunzionamenti.

---

### **Safety (Sicurezza funzionale)**
[[Safety]]

> Assicura che eventuali malfunzionamenti non causino danni alle persone, all’ambiente o ai beni.  
> **Esempio:** un sistema di controllo industriale che evita l’esplosione di una valvola anche in caso di errore software.  
> ⚠️ **Nota:** Safety ≠ Security — la prima riguarda i danni accidentali, la seconda quelli intenzionali.

---

### **Secrecy (Segretezza)**
[[Secrecy]]

> Aspetto specifico della riservatezza: impedisce che il **contenuto stesso** delle informazioni venga rivelato.  
> **Esempio:** cifrare un messaggio per nasconderne il significato anche se viene intercettato.  
> 🔹 Tutta la segretezza implica confidenzialità, ma non tutta la confidenzialità implica segretezza (es. anonimizzazione).

---

### **Maintainability (Manutenibilità)**
[[Maintainability]]

> Facilità con cui un sistema può essere corretto, aggiornato o modificato senza introdurre nuovi errori.  
> **Esempio:** patch di sicurezza regolari, modularità del codice.

---

### **Robustness (Robustezza)**
[[Robustness]]

> Capacità di un sistema di continuare a funzionare correttamente anche in presenza di input anomali o condizioni impreviste.  
> **Esempio:** un web server che non crasha se riceve richieste malformate.

---

### **Accountability (Responsabilità / Tracciabilità)**
[[Accountability]]

> Capacità di attribuire univocamente le azioni a chi le ha compiute.  
> **Esempio:** log firmati, auditing, tracciabilità utente → “chi ha fatto cosa, quando e come”.  
> **Relazione:** supporta il non-repudiation.

---

### **Fault Tolerance (Tolleranza ai guasti)**
[[Fault Tolerance]]

> Capacità di un sistema di continuare a funzionare correttamente anche se una o più componenti falliscono.  
> **Esempio:** sistemi replicati che continuano a fornire servizio se un nodo cade.  
> **Meccanismi comuni:** failover, checkpointing, replica, watchdog timers.

---

### **Resilience (Resilienza)**
[[Resilience]]

> Capacità del sistema di **resistere, assorbire e recuperare** rapidamente da eventi imprevisti, errori o attacchi.  
> **Esempio:** un servizio cloud che si ripristina automaticamente dopo un attacco DDoS.  
> 🔹 Più ampia della fault tolerance: include adattamento e recupero.

---

### **Scalability (Scalabilità)**
[[Scalability]]

> Capacità del sistema di crescere o ridursi **efficientemente** in risposta al carico o alle risorse disponibili.  
> **Esempio:** un database distribuito che può aggiungere nodi senza degradare le prestazioni.  
> **Tipi:**

- _Vertical scaling_: più potenza a un singolo nodo.
    
- _Horizontal scaling_: aggiunta di più nodi.
    

---

### **Trustworthiness (Affidabilità percepita)**
[[Trustworthiness]]

> Livello di fiducia che gli utenti possono avere che il sistema opererà correttamente, sicuro e senza comportamenti malevoli.  
> **Esempio:** software open-source con auditing trasparente e aggiornamenti regolari.  
> Combina sicurezza, integrità, affidabilità e correttezza dei dati.

---

### **Consistency (Coerenza)**
[[Consistency]]

> Tutti i nodi o repliche del sistema distribuito devono avere una **visione coerente e aggiornata** dei dati.  
> **Esempio:** in un database distribuito, una scrittura è visibile a tutti i client immediatamente o entro limiti definiti.  
> **Modelli comuni:** Strong consistency, Eventual consistency.

---

### **Auditability (Auditabilità / Tracciabilità verificabile)**
[[Auditability]]

> Possibilità di esaminare e verificare retrospettivamente le azioni, decisioni o eventi del sistema.  
> **Esempio:** log digitali immutabili e firmati che permettono di ricostruire una sequenza di operazioni.  
> **Benefici:** compliance, investigazioni post-incidente.

---

### **Resilience to Byzantine Faults (Resilienza ai guasti bizantini)**
[[Resilience]]

> Capacità di un sistema distribuito di funzionare correttamente anche se alcuni nodi agiscono **in modo arbitrario o malevolo**.  
> **Esempio:** algoritmi di consenso bizantino (BFT) come PBFT usati in blockchain.  
> 🔹 Critico in ambienti trustless o altamente ostili.

---

### **Adaptability (Adattabilità)**
[[Auditability]]

> Capacità del sistema di **modificare il proprio comportamento** in risposta a cambiamenti dell’ambiente, del carico o delle minacce.  
> **Esempio:** un firewall che aggiorna dinamicamente le regole quando rileva nuovi tipi di attacco.  
> **Benefici:** resilienza, riduzione dei downtime, migliore gestione del rischio.  
> **Minacce mitigate:** cambiamenti imprevisti, attacchi zero-day.

---

### **Observability (Osservabilità)**
[[Observability]]

> Capacità di **monitorare e misurare lo stato interno** e le metriche operative del sistema in modo che sia possibile capire cosa succede internamente.  
> **Esempio:** metriche, logging strutturato, tracing distribuito in microservizi.  
> **Benefici:** diagnostica rapida, troubleshooting, auditing.  
> **Minacce mitigate:** guasti nascosti, malfunzionamenti silenti, anomalie di sicurezza.

---

### **Self-healing (Auto-riparazione)**
[[Self-healing]]

> Capacità del sistema di **rilevare e correggere automaticamente errori o anomalie** senza intervento umano.  
> **Esempio:** un cluster Kubernetes che riavvia automaticamente un pod fallito.  
> **Benefici:** alta disponibilità, riduzione dei tempi di inattività, miglioramento della resilienza.  
> **Minacce mitigate:** guasti hardware/software, crash di servizi, configurazioni errate temporanee.

---

### **Redundancy (Ridondanza)**
[[Redundancy]]

> Presenza di **componenti o risorse duplicati** che consentono al sistema di continuare a funzionare anche se una parte fallisce.  
> **Esempio:** server duplicati in un load balancer, alimentatori doppi, mirror di database.  
> **Benefici:** fault tolerance, alta disponibilità, continuità del servizio.  
> **Minacce mitigate:** guasti hardware, errori software, interruzioni di rete.

---

### **Transparency (Trasparenza)**
[[Transparency]]

> Capacità del sistema di **presentarsi come coerente e uniforme** agli utenti o ad altri sistemi, **nascondendo la complessità interna** o la distribuzione.  
> **Esempio:** un sistema distribuito che appare come un singolo database logico anche se fisicamente replicato su più nodi.  
> **Benefici:** facilità d’uso, riduzione degli errori umani, miglior esperienza utente.  
> **Minacce mitigate:** confusione operativa, errori di sincronizzazione, percezioni errate di affidabilità.

---

