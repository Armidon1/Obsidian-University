## Segmentazione della Rete e Zero Trust

### Il Modello Tradizionale: "Castello e Fossato"

- Il design di rete tipico si basa sul concetto di **"fiducia interna" (internal trust)**.
    
- Il mondo è diviso in due zone: "esterno" (non fidato) e "interno" (fidato). So the border between the trusted network and the outside needs to be setup. We can fully protect the assets inside our domain: this means that a machine inside my domain cannot be compromised even by someone inside my network. Most Attacks ignores the border but uses an already compromised PC inside the network (which is trusted). It may happen because the adversary is using my employees (who are dumb) and with a [[Phishing]] email gives the opportunity to the adversary to compromise a trusted PC in my network. 
    
- Il trasferimento di dati è possibile solo attraverso checkpoint controllati (il **firewall**, o "fossato").
    
- **Debolezza:** Questo modello ha un guscio duro ma un centro morbido. Se un attaccante viola la barriera (es. tramite un'email di phishing), **nulla gli impedisce di muoversi liberamente all'interno della rete** (questo è chiamato **movimento laterale**).
    

---

## Architettura Zero Trust
[[Zero Trust Architecture]] 
**Principio:** Un modello di sicurezza moderno che opera sul principio **"Mai fidarsi, sempre verificare" (Never trust, always verify).**  

Assume che nessun utente o dispositivo debba essere considerato fidato per impostazione predefinita, anche se si trova "all'interno" del perimetro di rete.

note that: imagine if we cannot define a phisical limit of the border:
-  imagine if there are a smart working employees
- or maybe some of things are in a cloud service
- in those cases Zero Trust helps, because we don't care about the borders, we simply say "fuck you" to every one who are not idoneo.

### Principi Fondamentali

- **Verifica Esplicita:** Convalida continuamente l'accesso per ogni richiesta usando tutti i punti dati disponibili (identità, posizione, salute del dispositivo, servizio).
    
- **Usa il Minimo Privilegio di Accesso (Least Privilege):** Limita i permessi degli utenti al _minimo_ necessario per il loro lavoro, riducendo il potenziale raggio d'azione (blast radius) se le credenziali vengono compromesse.
	- for example, my employees cannot modify particular parts of my documents.
    
- **Presupponi la Violazione (Assume Breach):** Progetta la rete per _contenere_ potenziali violazioni e minimizzarne l'impatto. Non cercare solo di tenere fuori gli attaccanti; presupponi che siano già dentro.
	- means that, even if you created a good security system, always assume that an attack may be successful: in those cases, i have to minimise the damages.  
    

### Componenti Chiave di un'Architettura Zero Trust

- **Identity and Access Management (IAM):** Gestisce le identità degli utenti e impone autenticazione e autorizzazione forti.
	- of course, i want to know who is acting in my devices
    
- **Sicurezza dei Dispositivi (Device Security):** Monitora la "salute" dei dispositivi (es. "questo dispositivo ha le patch ed ha l'antivirus attivo?").
	- i need to patch my software/hardware vulnerabilities
    
- **Segmentazione della Rete:** (Vedi sotto) Suddivide la rete in piccole zone per limitare il movimento laterale.
	- the idea is that: let's start by a border defence, if someone breaches my trusted network, then i'm fucked. So i decide to creating borders between my internal PC's. Of course i have to control each borders, so i have to control more stuff. The more borders i include in my systems, the more overhead i'll get.
    
- **Protezione dei Dati (Data Protection):** Protegge i dati stessi (es. tramite crittografia) e impone la privacy dei dati.
	- of course, it doesn't mean that my data can be shared everywhere. Reducing the risk means that we are reducing a lot the possibility to be breached.
    
- **Monitoraggio Continuo e Analisi:** Traccia il comportamento di utenti e dispositivi per rilevare anomalie.
    

### Benefici

- **Sicurezza Migliorata:** Limita l'accesso e minimizza l'impatto di una violazione.
    
- **Superficie d'Attacco Ridotta:** Non esiste un'unica rete interna "fidata" da attaccare.
    
- **Supporto per Lavoro Remoto e Cloud:** Progettato per ambienti di lavoro moderni e distribuiti.
    
- **Compliance e Privacy dei Dati:** Aiuta a soddisfare i requisiti normativi con controlli d'accesso granulari.
    

---

## Strategie di Segmentazione della Rete (Implementare la Zero Trust)
è il cuore pulsante della sicurezza di una rete: è assolutamente necessario essere esperti in questo campo. 
### Cos'è la Segmentazione della Rete?

Una strategia di sicurezza che divide una rete in domini di protezione più piccoli e isolati (segmenti). Richiede l'implementazione di controlli (come i firewall) sui confini che collegano questi segmenti.
- esempio: a humanity resources office, to communicate with the logistic ones has to respect many rules. Inside each office, is not controlled
- può succedere anche che a volte questi bound sono validi solo per un certo periodo di tempo: se un team specifico deve lavorare solo per 2 anni, allora dopo 2 anni questi bound devono sparire

**Vantaggi:**

- **Ostacola il movimento laterale** per un attaccante.
    
- **Riduce la superficie d'attacco** e limita i potenziali danni.
	- la superficie d'attacco: immagina un adversary che è fuori dalla compagnia, fa un check da fuori delle possibili vulnerabilità della compagnia ([[Probing-Scanning]]): magari studiandone i servizi prodotti da possibili macchine internet. Dopo aver studiato queste opportunità, l'adversary ha davanti la "Superficie d'attacco". Che succede se l'adversary attacca anche i laptop personali degli employees? Potrebbe scoprire che magari qualche coglione nella mia compagnia è vulnerabile ad attacchi [[Phishing]], allora lo frega con un email [[Phishing]] e scopre nuove vulnerabilità della mia compagnia: in questo modo la superficie d'attacco cresce.   
    
- **Permette un monitoraggio e una gestione più granulari** del traffico.
    
- **Aiuta a soddisfare i requisiti normativi** isolando i dati sensibili (es. un segmento PCI per le carte di credito).
	- Immagina il GDPR (dal 2018): se hai a che fare con dati sensibili, tu sei costretto a gestire correttamente questi dati. Può succedere che un controllore arrivi nella tua struttura e controlla che hai implementato tutti i best practices
    

---

### Segmentazione Fisica

- Funziona a **livello hardware**, dividendo la rete in blocchi fisicamente separati (es. switch diversi, stanze diverse).
    
- L'esempio estremo è una rete **"air-gapped"** (fisicamente isolata) senza alcuna connessione ad altre reti.
    
- **Pro:** Massima sicurezza e isolamento.
    
- **Contro:** Estremamente inflessibile, costosa e difficile da gestire.
	- che succede se devo spostare un tizio da un ufficio ad un altro? devo staccare il suo PC fisicamente dal cavo Ethernet e portare fisicamente il PC da una parte all'altra.
![[Pasted image 20251105143511.png]]
this device is a device which impone la direzione della trasmissione dati in un unica direzione.

è possibile anche lavorare con trasmissioni wireless, ma sono molto più insicure e difficili da gestire, perciò lo si ignora. Ancora di più se si parla di connessioni wireless tra più reti wireless.

Una volta che hai creato la tua architettura della rete a partire dal livello hardware, allora sai già perfettamente quale PC fa cosa e come è connesso, perciò implementare la sicurezza a livello software sarà più semplice.

### Segmentazione Logica
funziona semplicemente andando a modificare a livello software gli accessi. 

- Funziona a livello software, creando confini definiti via software su hardware condiviso.
    
- **Pro:** Molto più **flessibile** della segmentazione fisica; permette un **controllo dinamico** e **centralizzato** (es. Software-Defined Networking - SDN). questo però può essere un problema però: proprio perché è più semplice e flessibile, spesso per mancanza di attenzione si fanno errori. 
    
- **Contro:** Può essere vulnerabile a bug software che rompono le garanzie di sicurezza.
    

### Micro-segmentazione

- Un approccio molto granulare che applica la segmentazione a livello della **singola applicazione o workload**.
    
- **Esempio:** Invece di un segmento "Web Server", _ogni singolo web server_ è nel proprio segmento ed è autorizzato a parlare solo con il _suo specifico database_ sulla _sua specifica porta_, e nient'altro.
    
- **Pro:** L'opzione migliore per implementare la Zero Trust; massima flessibilità; supporta ambienti ibridi e cloud.
	- Bisogna lavorare anche con i Firewall
    
- **Contro:** Può portare a una gestione complessa delle policy; potenziale overhead.
    

#### Approcci alla Micro-segmentazione

- **Basata sulla Rete (Network-Based):** Usa indirizzi IP o sottoreti.
    
- **Basata sull'Applicazione (Application-Based):** Le policy si basano su identificatori a livello di applicazione.
    
- **Basata sull'Utente (User-Based):** Controlla l'accesso a livello di utente (es. "Alice" può accedere all'app finanziaria).
    
- **Basata sul Processo (Process-Based):** Le policy si basano su _processi specifici_ all'interno di un workload (es. `apache.exe` può parlare sulla porta 80, ma `powershell.exe` no).
    

---
