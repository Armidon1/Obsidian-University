In termini pratici, nel contesto della **microsegmentazione** e delle architetture moderne (come Cloud o Zero Trust), quando le slide parlano di **workload** (carico di lavoro), non si riferiscono più al semplice "computer fisico" o "server", ma all'**unità di software che sta eseguendo un compito specifico**.

Ecco cosa si intende concretamente, basandosi sui livelli di granularità descritti nelle slide e:

### 1. L'Applicazione o Servizio (Il livello Macro)

All'atto pratico, un workload è l'**applicazione stessa** che supporta una funzione di business.

- **Esempio:** Invece di proteggere la "Sottorete 192.168.1.x", proteggi il **"Workload Web Server"** o il **"Workload Database"**.
- Le policy di sicurezza sono basate sugli identificatori dell'applicazione ("Application-level identifiers") e sulla logica di business, indipendentemente dall'indirizzo IP che l'applicazione ha in quel momento.

### 2. I Singoli Processi (Il livello Micro)

Scendendo ancora più nel dettaglio, le slide definiscono la _Process-Based Microsegmentation_, suggerendo che un workload può essere identificato finanche dai **singoli processi in esecuzione** all'interno di una macchina.

- **Esempio:** Un server potrebbe ospitare sia un servizio web che un servizio di posta. Se consideriamo il workload a livello di processo, la microsegmentazione può dire: _"Il processo `apache` può parlare con internet, ma il processo `postfix` sullo stesso server no"_.

### 3. Perché usiamo la parola "Workload"?

Si usa questo termine generico perché, come evidenziato nelle slide, la microsegmentazione è progettata per ambienti **Ibridi e Cloud**, dove l'infrastruttura fisica è astratta. Un "workload" in pratica può essere:

- Una **Macchina Virtuale (VM)** intera.
- Un **Container** (es. Docker o un Pod di Kubernetes).
- Una **Funzione Serverless**.

**In sintesi:** Nell'atto pratico, proteggere un workload significa mettere una bolla di sicurezza attorno al **software che lavora** (che sia un database, un'app o un container), disinteressandosi dell'hardware o del cavo di rete a cui è collegato.