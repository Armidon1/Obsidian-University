---
title: Sistemi Distribuiti
aliases:
  - SDC2 — Distributed systems
  - Sistemi di Calcolo 2 — Lezione 8
tags:
  - sistemi-di-calcolo-2
  - sistemi-distribuiti
  - client-server
  - middleware
  - rpc
  - cluster
source: Appunti Filippo/8-distributed_systems.pdf
---

# Sistemi distribuiti

> [!abstract] Scopo della lezione
> Un **sistema distribuito** è un insieme di computer indipendenti che appare agli utenti come un unico sistema. La lezione ne presenta esempi, vantaggi e svantaggi, i problemi di **coordinamento** (niente clock globale, guasti, latenze imprevedibili) e gli aspetti di progetto (eterogeneità, apertura, sicurezza, scalabilità, affidabilità, **trasparenza**…). Poi descrive il **middleware**, il **client/server computing** (le quattro classi di applicazioni, l'architettura **three-tier**, la **SOA**), il **message passing** distribuito, le **Remote Procedure Call** (binding, sincrone e asincrone, semantiche *at least once*, *at most once*, *exactly once*) e infine i **cluster**.
> Mappa dei concetti: [[MOC - Sistemi di Calcolo 2]]

## Introduzione

Vedi [[Sistema Distribuito]].

Un **sistema distribuito** è un insieme di entità **spazialmente separate**, ognuna con una certa capacità di calcolo, che **comunicano** e si **coordinano** per raggiungere un obiettivo comune, e che appaiono agli utenti come **un unico sistema coerente**. In breve: una collezione di computer indipendenti che agli utenti sembra un solo sistema.

Esempi: una rete di workstation, un sistema di produzione distribuito (es. una catena di montaggio automatizzata), la rete dei computer delle filiali di un'azienda.

I sistemi distribuiti si sono diffusi grazie alla disponibilità di **microprocessori potenti ma economici** (PC, workstation) e ai continui progressi delle **tecnologie di comunicazione**.

![[SDC2-L08-001-000.png]]

Esempi di applicazioni di rete per settore:

| Settore | Applicazioni |
| --- | --- |
| Finanza e commercio | eCommerce (Amazon, eBay, PayPal), online banking e trading |
| Società dell'informazione | web e motori di ricerca, ebook, Wikipedia, social network |
| Industrie creative e intrattenimento | giochi online, musica e film, contenuti degli utenti (YouTube, Flickr) |
| Sanità | informatica medica, cartelle cliniche online, monitoraggio dei pazienti |
| Istruzione | e-learning, ambienti virtuali, formazione a distanza |
| Trasporti e logistica | GPS, mappe (Google Maps, Google Earth) |
| Scienza | la Grid per la collaborazione tra scienziati |
| Gestione ambientale | sensori per terremoti, alluvioni, tsunami |

![[SDC2-L08-001-001.png]]

Esempi di sistemi distribuiti, creati per rispondere alle esigenze di questi domini: LAN e intranet, sistemi di gestione di database, la rete dei bancomat, Internet e il World Wide Web, sistemi pervasivi e *ubiquitous computing*, **Service Oriented Architecture**, reti virtuali, **peer-to-peer**, **cloud computing**, **big data computing**.

![[SDC2-L08-002-002.png]]

**Internet** è un sistema distribuito in cui molte macchine consultano dati sui server passando per gli ISP: intranet aziendali e utenti collegati agli ISP, uniti dalla **backbone** (anche via satellite).

- **World Wide Web**: l'applicazione più grande del mondo, la collezione di tutte le pagine che qualcuno ha creato e messo a disposizione degli altri.
- **Massively Multiplayer Online Games** (MMOG): un'esperienza immersiva in cui moltissimi utenti interagiscono via Internet con un mondo virtuale **persistente**. Comprendono arene di gioco complesse (le interazioni di un utente con il mondo e con gli altri devono essere propagate **in tempo reale** a tutti), sistemi sociali (comunicare con gli altri giocatori) e sistemi finanziari (conversione di denaro reale in denaro virtuale). Richiedono risposte rapide, propagazione in tempo reale degli eventi e una **visione consistente** dell'intero mondo.

### Vantaggi rispetto ai sistemi centralizzati

- **Economicità**: un insieme di microprocessori ha un rapporto **prezzo/prestazioni** migliore di un mainframe. Un unico server potente costa molto; con tante macchine più economiche si raggiunge la stessa potenza.
- **Velocità**: un sistema distribuito può avere **più potenza di calcolo totale** di un mainframe. Esempio: 10 000 CPU da 50 MIPS ciascuna fanno 500 000 MIPS, che un singolo processore non può raggiungere, perché richiederebbe un ciclo di istruzione di 0.002 ns. Un singolo server ha un numero limitato di core: il suo limite di velocità è fissato dalla potenza e dal numero di questi.
- **Distribuzione intrinseca**: alcune applicazioni sono **intrinsecamente distribuite** (es. una catena di supermercati, con negozi in luoghi diversi).
- **Affidabilità**: se una macchina si guasta, il sistema nel suo complesso può sopravvivere (maggiore disponibilità). Con un unico server, se si guasta bisogna ripararlo prima di poter continuare.
- **Crescita incrementale**: si può aggiungere potenza di calcolo **a piccoli incrementi** (espandibilità modulare).
- **Altra spinta**: l'esistenza di moltissimi PC e dispositivi IoT, e il bisogno delle persone di **collaborare** e condividere informazioni.

### Vantaggi rispetto a PC indipendenti

- **Condivisione dei dati**: molti utenti accedono a un database comune.
- **Condivisione delle risorse**: periferiche costose come le stampanti a colori.
- **Comunicazione**: migliora la comunicazione tra persone (email, chat).
- **Flessibilità**: il carico di lavoro si distribuisce sulle macchine disponibili.

### Svantaggi

- **Software**: è **difficile** sviluppare software per sistemi distribuiti.
- **Rete**: saturazione, perdita di pacchetti.
- **Sicurezza**: la facilità di accesso vale anche per i dati segreti.

### Coordinamento

L'obiettivo principale dei sistemi distribuiti è **condividere dati e risorse**; i problemi principali sono **sincronizzazione** e **coordinamento**. Rispetto ai sistemi centralizzati, bisogna tenere conto di condizioni nuove:

- **concorrenza temporale e spaziale**: oltre a quella temporale, c'è la concorrenza **spaziale**: un dato può essere replicato su più macchine contemporaneamente;
- **niente clock globale**: ogni macchina ha il proprio clock, e i clock possono differire;
- **guasti**: le macchine possono guastarsi. Se aspetto un dato da una macchina che si è guastata, cosa faccio? Serve qualcuno che si accorga dei guasti;
- **latenze imprevedibili**.

Queste limitazioni **restringono l'insieme dei problemi di coordinamento** che si possono risolvere in un sistema distribuito.

## Aspetti di progetto

Nel progettare un sistema distribuito bisogna gestire: **eterogeneità**, **apertura**, **sicurezza**, **scalabilità**, **affidabilità**, **concorrenza**, **flessibilità**, **prestazioni**, **trasparenza**.

**Eterogeneità**: il sistema deve funzionare su:

- **reti** diverse;
- **hardware** diverso (l'applicazione deve girare su Mac, Windows, Android…);
- **sistemi operativi** diversi;
- **linguaggi di programmazione** diversi;
- implementazioni di **sviluppatori** diversi;
- **codice mobile** (codice che si sposta da una macchina all'altra, es. JavaScript).

**Apertura** (*openness*): i servizi distribuiti devono essere utilizzabili, quindi le loro **interfacce devono essere pubbliche**. Un sistema aperto si basa su un meccanismo di comunicazione uniforme e su interfacce pubbliche per accedere alle risorse condivise. Può essere costruito con hardware e software eterogenei, ma la **conformità** di ogni componente allo standard pubblicato va verificata con cura.

**Sicurezza**: bisogna garantire

- **confidenzialità**: impedire l'accesso a chi non è autorizzato;
- **integrità**: protezione da alterazioni o corruzioni (per errore, durante la trasmissione, o da parte di non autorizzati);
- **disponibilità**: protezione dalle interferenze con i mezzi di accesso alle risorse.

(La triade CIA della [[10 - SDC2 - Sicurezza|lezione 10]].)

**Scalabilità**: i sistemi crescono nel tempo o diventano obsoleti (e la crescita non è lineare). Problemi:

- controllare il **costo** delle risorse fisiche;
- controllare la **perdita di prestazioni**: un sistema distribuito aggiunge overhead per gestire le macchine, che non deve diventare predominante;
- evitare che le **risorse software si esauriscano** (es. gli indirizzi IPv4);
- evitare i **colli di bottiglia**: componenti centralizzati (un unico server di posta), tabelle centralizzate (un'unica rubrica di URL), algoritmi centralizzati (routing basato su informazioni complete).

**Affidabilità**: un sistema distribuito dovrebbe essere **più affidabile** di un sistema singolo. Bisogna gestire i guasti: rilevarli, mascherarli, tollerarli, recuperare (*fault recovery*), usare la ridondanza.

> [!warning] Correzione
> Gli appunti scrivono "3 macchine con 95% di probabilità di essere attive → (95)^3% di probabilità di essere attive", senza dire cosa si calcola.
> - Se il sistema funziona solo quando funzionano **tutte e tre**: $0.95^3 \approx 0.857$, cioè 85.7%, **meno** di una macchina sola.
> - Se basta **almeno una** macchina (ridondanza): $1 - 0.05^3 = 0.999875$, cioè 99.99%.
>
> La ridondanza aumenta l'affidabilità solo se il sistema è progettato per sopravvivere al guasto di qualche nodo.

**Concorrenza**: temporale e spaziale.

**Flessibilità**: il sistema deve adattarsi rapidamente a qualsiasi cambiamento, cioè essere **facile da modificare**. Per questo sono preferibili i **microkernel** ai **kernel monolitici**:

![[SDC2-L08-005-003.png]]

- **kernel monolitico**: le system call vengono intercettate ed eseguite dal kernel, che serve **tutte** le system call (file, directory, gestione dei processi), come in UNIX;
- **microkernel**: offre solo servizi minimi (IPC, un po' di gestione della memoria, gestione dei processi e scheduling di basso livello, I/O di basso livello); il resto (file server, directory server, process server) gira come **servizi separati**, anche su macchine diverse collegate in rete.

Vedi [[Kernel Monolitico e Microkernel]].

**Prestazioni**:

- perdita dovuta ai **ritardi di comunicazione**: bisogna usare meno parallelismo a **grana fine** (tante piccole attività parallele richiedono molta comunicazione per riunire i risultati) e più parallelismo a **grana grossa**;
- perdita dovuta al rendere il sistema **tollerante ai guasti**.

### Trasparenza

Vedi [[Trasparenza nei Sistemi Distribuiti]].

La **trasparenza** è far sembrare che tutto sia su **un'unica macchina** (*single-system image*).

| Tipo | Significato |
| --- | --- |
| **Accesso** | risorse locali e remote si usano con **le stesse operazioni** |
| **Locazione** | l'utente non sa **dove** si trovano le risorse (CPU, stampanti, file, database) |
| **Concorrenza** | l'utente non si accorge degli **altri utenti**; più utenti accedono alla stessa risorsa (con lock e unlock per la mutua esclusione) |
| **Replicazione** | il sistema può creare **copie** di file e risorse senza che l'utente se ne accorga |
| **Guasti** | i guasti vengono **nascosti**: utenti e applicazioni completano i loro compiti nonostante i guasti di hardware o software |
| **Migrazione** | risorse e client possono **spostarsi** senza effetti sulle operazioni né cambi di nome (es. `/usr/lee` → `/central/usr/lee`) |
| **Prestazioni** | il sistema si può **riconfigurare** per migliorare le prestazioni al variare del carico |
| **Scalabilità** | il sistema e le applicazioni possono **crescere** senza cambiare struttura né algoritmi |
| **Parallelismo** | uso **automatico** del parallelismo senza programmarlo esplicitamente: il "santo graal" dei progettisti di sistemi distribuiti e paralleli |

### Modelli di interazione

![[SDC2-L08-006-004.png]]

**Client/server**: i client invocano un server, che restituisce il risultato; un server può a sua volta essere client di un altro server.

![[SDC2-L08-006-005.png]]

**Peer-to-peer**: ogni processo contiene sia l'**applicazione** sia il **codice di coordinamento**, e comunica direttamente con gli altri.

## Middleware

Vedi [[Middleware]].

![[SDC2-L08-006-006.png]]

Il layering hardware/software su un'unica macchina: rete e hardware e sistema operativo formano la **piattaforma**; sopra c'è il **middleware**; sopra ancora applicazioni e servizi.

![[SDC2-L08-006-007.png]]

In un sistema distribuito il **livello middleware si estende su più macchine**: sotto ogni macchina ha il proprio sistema operativo locale, sopra le applicazioni distribuite vedono un unico servizio. Quando si chiede l'elaborazione di un dato, questa può avvenire su una qualunque delle macchine.

Problemi nello sviluppo del middleware:

- **eterogeneità**: sistemi operativi, clock, rappresentazione dei dati, memoria, architettura hardware possono essere diversi su ogni macchina;
- **asincronia locale**: un nodo troppo carico, hardware diverso, interrupt;
- **mancanza di conoscenza globale**: la conoscenza si propaga con messaggi, il cui tempo di propagazione è molto più lungo del tempo di un evento interno;
- **asincronia di rete**: i tempi di propagazione dei messaggi sono imprevedibili;
- **guasti** di nodi o **partizioni** della rete;
- **mancanza di un ordine globale degli eventi**;
- **consistenza vs disponibilità vs partizioni di rete** (non si possono avere tutte e tre: è il teorema CAP).

Questi problemi limitano l'insieme dei problemi risolvibili con **algoritmi deterministici** in certi sistemi distribuiti.

Per ottenere i veri benefici di un sistema distribuito, gli sviluppatori hanno bisogno di strumenti che diano un modo **uniforme** di accedere alle risorse su tutte le piattaforme: applicazioni con lo stesso aspetto ovunque e lo stesso metodo per accedere ai dati, **ovunque si trovino**. Lo si ottiene con **interfacce di programmazione e protocolli standard** tra l'applicazione (sopra) e il software di comunicazione e il sistema operativo (sotto).

![[SDC2-L08-007-008.png]]

Vista logica del middleware: le applicazioni lo usano tramite **API**; il middleware (i servizi del sistema distribuito) usa le **interfacce di piattaforma** delle varie macchine (sistema operativo e hardware).

## Client/server computing

Vedi [[Modello Client-Server]].

- Le macchine **client** sono di solito PC o workstation monoutente, con un'interfaccia molto facile da usare.
- Ogni **server** offre ai client un insieme di **servizi condivisi**. Il server permette a molti client di condividere l'accesso allo stesso database e di usare un sistema ad alte prestazioni per gestirlo.

![[SDC2-L08-008-009.png]]

Un ambiente client/server generico: molte workstation (client) e alcuni server collegati da una LAN, una WAN o Internet.

Caratteristiche del client/server (rispetto ad altri tipi di elaborazione distribuita):

- forte affidamento su applicazioni **facili da usare** sul sistema dell'utente;
- enfasi sulla **centralizzazione** dei database aziendali e di molte funzioni di gestione della rete;
- impegno di utenti e produttori verso sistemi **aperti e modulari**;
- il **networking** è fondamentale per il funzionamento.

Nelle applicazioni client/server il grosso del software applicativo gira sul **server**; parte della logica applicativa e i servizi di presentazione stanno sul **client**.

La caratteristica chiave è l'**allocazione dei compiti applicativi** tra client e server. Hardware e sistema operativo di client e server possono essere **diversi**: queste differenze non contano, purché condividano gli stessi **protocolli di comunicazione** (principalmente TCP/IP) e supportino le stesse applicazioni. Le funzioni dell'applicazione si possono dividere tra client e server in modo da ottimizzare l'uso delle risorse.

Il progetto dell'**interfaccia utente** sul client è critico: si punta molto su una **GUI** facile da usare e da imparare, ma potente e flessibile.

![[SDC2-L08-008-010.png]]

L'architettura generica: sul **client**, servizi di presentazione, **logica applicativa** (parte client), software di comunicazione, sistema operativo, hardware; sul **server**, logica applicativa (parte server), software di comunicazione, sistema operativo, hardware. Le logiche applicative si scambiano richieste e risposte; i software di comunicazione interagiscono secondo un protocollo.

### Le componenti di un'applicazione

Le applicazioni aziendali (paghe, ordini, gestione clienti, magazzino…) hanno quattro componenti:

- **logica di presentazione**: l'interfaccia utente;
- **logica di I/O**: la validazione dei dati;
- **logica di business**: regole e calcoli;
- **logica di memorizzazione dei dati**: vincoli come chiavi primarie e integrità referenziale, e il recupero dei dati.

Quasi tutte le applicazioni le contengono, ma **non devono** stare nello stesso programma, sullo stesso computer, essere scritte nello stesso linguaggio né dallo stesso gruppo.

Domande da porsi nello sviluppo di una componente:

- in che **linguaggio** scriverla?
- su quale **risorsa hardware** farla girare?
- quanto spesso **cambierà** (linguaggio, piattaforma, business)?
- chi è **responsabile** della sua manutenzione?
- quanto deve **durare** l'applicazione?

### Il ruolo del middleware

![[SDC2-L08-009-011.png]]

Sul client il **middleware** sta tra la logica applicativa e il software di comunicazione; sul server sta sopra il software di comunicazione e i servizi applicativi. I middleware di client e server interagiscono tra loro. Sul server i **servizi applicativi stanno accanto al software di comunicazione**, sotto il middleware: così possono comunicare direttamente con il sistema operativo, il che è più efficiente.

### Le quattro classi di applicazioni client/server

**Host-based processing**: non è un vero client/server, è il tradizionale ambiente **mainframe**: il server fa tutto (presentazione, logica applicativa, logica del database, DBMS) e il client è un terminale vuoto.

![[SDC2-L08-009-012.png]]

**Server-based processing**: il server fa tutta l'elaborazione; il client fornisce solo l'**interfaccia grafica** (logica di presentazione).

![[SDC2-L08-010-013.png]]

**Client-based processing**: tutta l'elaborazione applicativa avviene sul **client**; la validazione dei dati e altre funzioni della logica del database stanno sul server.

![[SDC2-L08-010-014.png]]

**Cooperative processing**: l'elaborazione è divisa in modo **ottimizzato** tra client e server (entrambi hanno parte della logica applicativa). È complessa da configurare e mantenere. Si parla di **fat client** (client con molta logica) e **thin client** (client con poca logica).

![[SDC2-L08-010-015.png]]

### Architettura three-tier

L'architettura **a tre livelli** distribuisce il software applicativo su tre tipi di macchine:

- **macchina utente** (*thin client*);
- **middle-tier server** (*application server*): smista il lavoro (fa da gateway, converte i protocolli, unisce i risultati di sorgenti di dati diverse). Quando si chiede un servizio, il middle-tier sa a quale server di backend rivolgersi;
- **backend server** (*data server*).

![[SDC2-L08-010-016.png]]

### Service-Oriented Architecture (SOA)

Vedi [[Service-Oriented Architecture]].

La **SOA** è una forma di architettura client/server usata nei sistemi aziendali. Organizza le funzioni aziendali in una struttura **modulare** invece che in applicazioni monolitiche per ogni reparto: le funzioni comuni possono essere usate da reparti diversi e anche da partner esterni.

È composta da un insieme di **servizi** e da un insieme di **applicazioni client** che li usano. Si usano **interfacce standardizzate** per far comunicare i servizi tra loro e con le applicazioni client.

![[SDC2-L08-011-017.png]]

Il triangolo della SOA: il **service provider** pubblica il servizio presso il **service broker**; il **service requester** trova il servizio tramite il broker e poi si collega (*bind*) direttamente al provider.

**Esempio: un'applicazione bancaria senza SOA.**

![[SDC2-L08-011-018.png]]

Tre applicazioni separate (conto corrente via web per il cliente, conto corrente per l'impiegato, gestione dei prestiti per il funzionario) accedono **direttamente** ai database (dati del conto, dei clienti, dei prestiti) e all'analisi del rischio di credito esterna. Ogni applicazione duplica la logica di accesso.

**La stessa con SOA.**

![[SDC2-L08-011-019.png]]

Le applicazioni (sportello, bancomat, cliente web, gestione prestiti) usano **servizi** condivisi: servizio conto corrente, servizio clienti, servizio gestione prestiti, servizio richiesta prestiti, servizio di rischio di credito (proxy verso quello esterno). Solo i servizi accedono ai dati. La logica è scritta una volta sola e riusata.

## Message passing distribuito

Vedi [[Message Passing]].

Una parte del middleware è orientata allo **scambio di messaggi**.

![[SDC2-L08-012-020.png]]

Il **Message-Oriented Middleware** (MOM, con code di messaggi) sta tra l'applicazione e il trasporto, su client e server; le applicazioni si scambiano messaggi specifici dell'applicazione.

![[SDC2-L08-012-021.png]]

Le primitive di base, già viste nella [[05 - SDC2 - Comunicazione tra Processi#Message passing|lezione 5]]: il processo mittente passa il messaggio al proprio modulo di message passing, che lo trasmette (con l'ID del processo) al modulo del destinatario.

## Remote Procedure Call

Vedi [[Remote Procedure Call]].

Le **Remote Procedure Call** (RPC) permettono a programmi su macchine diverse di interagire con la semplice semantica di **chiamata e ritorno di una procedura**. Si usano per accedere a servizi remoti, e sono un metodo diffuso e accettato per incapsulare la comunicazione in un sistema distribuito.

L'RPC è una tecnologia **standard**. Vantaggi della standardizzazione:

- il **codice di comunicazione** di un'applicazione può essere **generato automaticamente**;
- i moduli client e server si possono spostare tra computer e sistemi operativi con poche modifiche.

![[SDC2-L08-012-022.png]]

Nell'architettura RPC, client e server hanno ciascuno un **RPC stub program** tra l'applicazione e il livello di trasporto; gli stub si scambiano invocazioni e ritorni di procedure.

![[SDC2-L08-013-023.png]]

Il meccanismo:

1. l'applicazione client fa una **chiamata di procedura locale** allo **stub** (come se chiamasse una funzione qualsiasi);
2. lo stub **impacchetta** i parametri (*marshalling*) e il meccanismo RPC li invia al server;
3. lo stub del server **spacchetta** i parametri e fa una chiamata locale alla procedura dell'applicazione server;
4. la risposta locale torna allo stub del server, che la invia a quello del client, che la restituisce all'applicazione.

Le altre chiamate del client vanno normalmente all'applicazione o al sistema operativo locale.

**Parametri**:

- passare un parametro **per valore** è facile (si copia il valore nel messaggio);
- passarlo **per riferimento** è difficile: un puntatore ha senso solo nello spazio di indirizzi di una macchina. Servirebbe un puntatore unico in tutto il sistema, e l'overhead potrebbe non valerne la pena;
- la **rappresentazione** dei parametri e dei messaggi può essere difficile se client e server usano linguaggi (o architetture) diversi: endianness, dimensione degli interi… Si usa un formato di rappresentazione comune.

### Binding

Un **binding** si forma quando due applicazioni hanno stabilito una connessione logica e sono pronte a scambiarsi comandi e dati.

- **Binding non persistente**: la connessione logica viene stabilita al momento della chiamata remota e **chiusa** appena arrivano i risultati. L'overhead di stabilire le connessioni lo rende inadatto a procedure chiamate spesso dallo stesso chiamante.
- **Binding persistente**: la connessione resta aperta dopo il ritorno della procedura e si può usare per chiamate future; se resta inattiva per un certo tempo viene chiusa. Per le applicazioni che fanno molte chiamate ripetute, permette di riusare la stessa connessione.

### RPC sincrone e asincrone

- **Sincrona**: si comporta come una normale chiamata di funzione (il chiamante si blocca fino alla risposta). Il comportamento è prevedibile, ma non sfrutta il parallelismo intrinseco delle applicazioni distribuite: limita le interazioni possibili e riduce le prestazioni.
- **Asincrona**: **non blocca** il chiamante; le risposte si ricevono quando servono, e il client continua a lavorare in parallelo con il server.

### Semantiche delle chiamate in caso di guasti

Il funzionamento normale di una RPC può essere interrotto: il messaggio di chiamata o di risposta si perde, il nodo chiamante si guasta e riparte, il nodo chiamato si guasta e riparte. La **semantica della chiamata** stabilisce **quante volte** la procedura remota può essere eseguita in caso di guasto.

| Semantica | Garanzia | Implementazione | Adatta a |
| --- | --- | --- | --- |
| **At least once** | la chiamata viene eseguita **una o più volte**, senza dire quale risultato viene restituito | facile, poco overhead: il client **ritrasmette** dopo un timeout finché non riceve una risposta, senza curarsi delle *orphan calls* (chiamate su server che si sono guastati). Se si perdono delle risposte, il server può eseguire la chiamata più volte | solo operazioni **idempotenti** |
| **At most once** | la chiamata viene eseguita **al massimo una volta**: o non viene eseguita, o viene eseguita esattamente una volta, a seconda che il server cada | richiede di **rilevare i pacchetti duplicati** (il server ricorda le richieste già servite) | anche operazioni **non idempotenti** |
| **Exactly once** | il sistema garantisce la semantica di una chiamata locale, assumendo che un server guasto prima o poi riparta | tiene traccia delle chiamate orfane e permette che vengano "adottate" da un nuovo server; implementazione **molto complessa** | |

> [!example] Idempotenza
> Un'operazione è **idempotente** se eseguirla più volte ha lo stesso effetto di eseguirla una volta: "leggi il saldo" o "imposta il saldo a 100" sono idempotenti; "aggiungi 10 al saldo" no. Con la semantica *at least once* un bonifico potrebbe essere eseguito due volte.

## Cluster

Vedi [[Cluster]].

I **cluster** sono un'alternativa al **Symmetric Multiprocessing** (vedi [[01 - SDC2 - Processi e Thread#Symmetric Multiprocessing (SMP)|lezione 1]]) per ottenere alte prestazioni e alta disponibilità. Un cluster è un gruppo di **computer completi** interconnessi (ognuno può funzionare anche da solo, fuori dal cluster) che lavorano insieme come un'unica risorsa di calcolo, dando l'illusione di essere una sola macchina. Ogni computer del cluster è un **nodo**.

Benefici:

- **scalabilità assoluta**: si possono creare cluster molto più potenti della più grande macchina singola;
- **scalabilità incrementale**: si possono aggiungere nuovi sistemi al cluster a piccoli incrementi;
- **alta disponibilità**: il guasto di un nodo non è critico per il sistema;
- **rapporto prezzo/prestazioni migliore**: usando componenti comuni, un cluster costa molto meno di una grande macchina singola.

### Configurazioni

![[SDC2-L08-015-024.png]]

**Server di standby senza disco condiviso**: due nodi, ognuno con i propri processori (P), memoria (M), I/O e disco, collegati da un **link ad alta velocità** per i messaggi.

![[SDC2-L08-015-025.png]]

**Disco condiviso**: oltre al link per i messaggi, i nodi condividono un **array di dischi RAID**.

### Metodi di clustering

| Metodo | Descrizione | Benefici | Limiti |
| --- | --- | --- | --- |
| **Passive standby** | un server secondario subentra se il primario si guasta | facile da implementare | costo alto: il secondario non fa altro |
| **Active secondary** | il secondario viene usato anche per elaborare | costo ridotto | più complesso |
| **Separate servers** | server separati con i propri dischi; i dati vengono copiati continuamente dal primario al secondario | alta disponibilità | overhead di rete e di server per le copie |
| **Servers connected to disks** | i server sono collegati agli stessi dischi, ma ognuno possiede i propri; se un server si guasta, l'altro prende i suoi dischi | niente copie, meno overhead | di solito serve mirroring o RAID contro i guasti dei dischi |
| **Servers share disks** | più server condividono l'accesso **simultaneo** ai dischi | poco overhead, meno rischio di fermo per i guasti dei dischi | serve un **lock manager**; di solito con mirroring o RAID |

### Gestione dei guasti

- **Cluster ad alta disponibilità** (*highly available*): alta probabilità che tutte le risorse siano in servizio. Una query persa, se ripetuta, viene servita da un altro computer del cluster. Il sistema operativo del cluster **non garantisce nulla** sullo stato delle transazioni eseguite a metà: se c'è un guasto, le query in corso sono perse.
- **Cluster fault-tolerant**: si usano dischi condivisi ridondanti e meccanismi per **annullare** le transazioni non confermate e **confermare** quelle completate. Garantisce che tutte le risorse siano **sempre** disponibili.

Due operazioni:

- **failover**: spostare applicazioni e dati da un sistema guasto a un sistema alternativo del cluster;
- **failback**: riportarli sul sistema originale quando è stato riparato.

Il failback si può automatizzare, ma conviene solo se il problema è davvero risolto e non si ripresenterà: un failback automatico può far "rimbalzare" le risorse avanti e indietro tra due computer, con problemi di prestazioni e di recovery.

> [!warning] Correzione
> Gli appunti scrivono "Fallover": il termine è **failover**.

### Bilanciamento del carico

Un cluster deve saper **bilanciare il carico** tra i computer disponibili, ed essere scalabile in modo incrementale: quando si aggiunge un computer, il bilanciamento deve includerlo automaticamente nello scheduling delle applicazioni. Il middleware deve sapere che i servizi possono comparire su membri diversi del cluster e **migrare** dall'uno all'altro.

### Parallelizzare il calcolo

- **Compilatore parallelizzante**: decide a **compile time** quali parti dell'applicazione possono girare in parallelo. Le prestazioni dipendono dalla natura del problema e da quanto è ben progettato il compilatore.
- **Applicazione parallelizzata**: il programmatore progetta l'applicazione per girare su un cluster e usa il **message passing** per spostare i dati tra i nodi. È molto faticoso per il programmatore, ma può essere l'approccio migliore per alcune applicazioni.
- **Calcolo parametrico**: quando un'applicazione deve essere eseguita **molte volte** con condizioni iniziali o parametri diversi (es. simulazioni). Servono strumenti per organizzare, eseguire e gestire i job in modo ordinato.

![[SDC2-L08-017-026.png]]

L'architettura di un cluster: ogni nodo (PC/workstation) ha il proprio software di comunicazione e la propria interfaccia di rete, ed è collegato a una **rete o switch ad alta velocità**. Sopra c'è il **middleware del cluster** (immagine di sistema unico e infrastruttura di disponibilità), su cui girano sia applicazioni **sequenziali** sia applicazioni **parallele** (tramite un ambiente di programmazione parallela).
