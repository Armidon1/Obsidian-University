# Load Balancing (Bilanciamento del Carico)

**Tag:** #networking #server #scalability #performance #availability #high-availability #definizioni

---

## 📝 Definizione
Il **Load Balancing** (Bilanciamento del Carico) è una tecnica utilizzata per distribuire il traffico di rete o il carico di lavoro su più server (chiamati "Server Farm" o "Cluster") invece che su uno solo.

L'obiettivo è ottimizzare l'uso delle risorse, massimizzare la velocità di risposta (Throughput) e garantire che nessun server venga sopraffatto, evitando colli di bottiglia.

> [!abstract] Concetto Chiave: Le Casse del Supermercato
> Immagina un supermercato con 100 clienti e una sola cassa aperta. Si crea una coda infinita e se la cassiera si sente male, il supermercato si ferma.
> Il **Load Balancer** è il manager che apre 5 casse e smista i clienti: "Tu vai alla cassa 1, tu alla 2, tu alla 3...".
> * Risultato: Code più veloci e se la cassa 2 si rompe, il manager manda tutti alle altre 4. Il servizio non si ferma mai.

---

## ⚙️ Come Funziona
Il Load Balancer (che può essere hardware o software come **Nginx** o **HAProxy**) si posiziona davanti ai server, agendo spesso come un [[Proxy]] (specificamente un **Reverse Proxy**).

Il processo ciclico è:
1.  Il Client invia una richiesta al Load Balancer (che possiede l'IP Pubblico VIP - Virtual IP).
2.  Il Load Balancer sceglie un server interno (Backend) basandosi su un algoritmo.
3.  Inoltra la richiesta a quel server specifico.
4.  Riceve la risposta e la rimanda al Client.

---

## 🧮 Algoritmi di Bilanciamento
Come decide a chi dare il pacchetto? Esistono diverse strategie:

### 1. Round Robin (Il Girotondo)
È il più semplice. Distribuisce le richieste in ordine sequenziale.
* *Sequenza:* Richiesta A -> Server 1, Richiesta B -> Server 2, Richiesta C -> Server 1...
* *Difetto:* Non considera se il Server 1 è sovraccarico o sta elaborando una richiesta pesante.

### 2. Least Connections (Meno Connessioni)
Più intelligente. Invia la nuova richiesta al server che ha il minor numero di connessioni attive in quel momento.
* *Ideale per:* Situazioni in cui le sessioni hanno durate molto variabili.

### 3. IP Hash (Session Persistence / Sticky Session)
Calcola un hash dell'IP del client per assicurarsi che lo **stesso utente** finisca sempre sullo **stesso server**.
* *Perché serve?* Se hai fatto Login sul Server 1 e la tua sessione è salvata lì, se il Load Balancer ti manda sul Server 2, risulterai disconnesso. Questo metodo "incolla" (sticky) l'utente al server.

---

## 🗂️ Tipologie: L4 vs L7

| Caratteristica | Layer 4 Load Balancing | Layer 7 Load Balancing |
| :--- | :--- | :--- |
| **Livello OSI** | Trasporto (TCP/UDP) | Applicazione (HTTP/HTTPS) |
| **Visibilità** | Vede solo IP e Porte | Vede URL, Cookie, Header |
| **Decisione** | "Manda tutto il traffico TCP porta 80 al server X" | "Manda chi chiede `/immagini` al server X e chi chiede `/video` al server Y" |
| **Velocità** | ⭐⭐⭐ (Velocissimo) | ⭐⭐ (Richiede decodifica) |
| **Utilizzo** | Protocolli semplici, alto traffico grezzo | Routing intelligente dei contenuti |

---

## ❤️ Health Checks (Controllo Salute)
Questa è la funzione critica per l'affidabilità (**High Availability**).
Il Load Balancer "interroga" regolarmente i server di backend per vedere se sono vivi.
* *Esempio:* Invia una richiesta HTTP ogni 5 secondi.
* *Scenario:* Se il Server 3 risponde con errore (500) o non risponde (Timeout), il Load Balancer lo marca come **Dead** (Morto) e smette immediatamente di inviargli traffico.
* *Risultato:* L'utente finale non vede mai la pagina di errore.

---

## 🛡️ Ruolo nella Sicurezza
Il Load Balancer è un componente chiave nella difesa perimetrale:

1.  **Mitigazione DDoS:** Distribuendo un attacco massiccio su 50 server, l'impatto è molto minore rispetto a colpirne uno solo.
2.  **Nascondere la Topologia:** L'attaccante vede solo l'IP del Load Balancer, non conosce gli IP reali dei server interni.
3.  **SSL Offloading:** Il Load Balancer si occupa di decifrare il traffico HTTPS (pesante per la CPU), lasciando i server web liberi di generare solo le pagine.