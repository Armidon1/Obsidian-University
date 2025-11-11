# Virtualizzazione

## Virtualizzazione di Sistema e Macchine Virtuali

Fino a circa 20 anni fa, la struttura del software era tipicamente monolitica e strettamente legata all'hardware sottostante. Lo stack era semplice:

1. **Macchina "reale"** (Hardware fisico)
    
2. **Sistema Operativo** (che girava su quell'hardware)
    
3. **Applicazioni** (che giravano su quel sistema operativo)
    

Il problema principale di questo approccio era la **portabilità**. Non c'era alcuna garanzia che un software sviluppato per un'architettura (es. hardware x86 + Windows) potesse funzionare su un'altra (es. hardware PowerPC + macOS, o x86 + Linux).

Questa dipendenza era dovuta a due fattori principali:

- Il software è compilato in un linguaggio di basso livello (codice macchina) che è dipendente dalla specifica piattaforma hardware (la sua **Instruction Set Architecture** o ISA).
    
- Il software deve utilizzare i servizi specifici forniti dal sistema operativo, come le **system call** per l'I/O, la gestione della grafica, ecc.
    

---

## Macchina Virtuale e Virtualizzazione

Per risolvere il problema della portabilità, è stato introdotto il concetto di **virtualizzazione**.

In termini generali, la virtualizzazione è un processo che utilizza un livello software di **astrazione** per creare una versione _virtuale_ di una risorsa computazionale (come CPU, memoria, storage) a partire da una risorsa _reale_. Questo ci permette di "scomporre" o "aggregare" le risorse fisiche in modi più flessibili.

Esempi comuni includono:

- **Virtual Private Network (VPN):** Crea una rete privata _virtuale_ sopra una rete fisica (come Internet).
    
- **File System:** Crea un'astrazione _virtuale_ di file e cartelle sopra i blocchi grezzi di un disco fisico.
    

### System Virtualization (Virtualizzazione di Sistema)

La virtualizzazione di sistema utilizza un software per creare un livello di astrazione sopra l'hardware di un intero sistema fisico.

Questo permette di suddividere gli elementi hardware di un singolo computer (processori, memoria, storage) in più **macchine virtuali (VM)**, ognuna delle quali si comporta come un computer completo e isolato.

Questa è una tecnologia fondamentale, specialmente per i sistemi distribuiti e il cloud computing, perché:

- È la tecnologia abilitante per la **gestione flessibile** degli ambienti di esecuzione.
    
- È la tecnologia abilitante fondamentale del **cloud computing** (in particolare per il modello IaaS).
    
- Permette di implementare facilmente qualità software come l'**alta disponibilità** e la **scalabilità**.
    

---

## Le Macchine Virtuali (VM)

Una **macchina virtuale** è un livello software che emula una macchina "reale", dando al sistema operativo e alle applicazioni installate al suo interno l'illusione di girare su hardware fisico dedicato.

Una VM fornisce un set completo di risorse hardware virtuali (processori, memoria, storage, dispositivi di rete). Su questa macchina "finta", è possibile installare un sistema operativo completo (chiamato **Guest OS**) e un intero stack di applicazioni.

### Stack Virtualizzato vs. Non Virtualizzato

La differenza chiave è l'introduzione di un nuovo livello software: l'hypervisor.

**Computer Non Virtualizzato:**

- Applicazioni
    
- Sistema Operativo (Host OS)
    
- Hardware (Macchina Fisica)
    

**Computer Virtualizzato:**

- **Guest Application**
    
- **Guest Operating System**
    
- **Virtual Machine (VM)**
    
- **Software di Virtualizzazione (Hypervisor o VMM)**
    
- **Host Operating System** (presente solo nel Tipo 2)
    
- Hardware (Macchina Fisica)
    

### VM vs. Istanza VM

- **Virtual Machine (VM):** È l'entità virtuale che emula l'hardware di un computer reale. È il "progetto" o la "definizione" statica.
    
- **Istanza di VM (VM Instance):** È una macchina virtuale _in esecuzione_, che include il suo sistema operativo, le sue applicazioni e il suo **stato** corrente (contenuto della memoria, registri della CPU, ecc.).
    

---

## L'Hypervisor (Virtual Machine Monitor)

Le macchine virtuali sono coordinate dall'**hypervisor**, che è il livello software di virtualizzazione (noto anche come Virtual Machine Monitor o VMM).

Questo software agisce come interfaccia tra la VM e l'hardware fisico sottostante, assicurando che ogni VM abbia accesso alle risorse fisiche di cui ha bisogno e che le VM non interferiscano tra loro (garantendo l'**isolamento**).

### Tipi di Hypervisor

Esistono due tipi principali di hypervisor:

1. **Tipo 1 (Nativo o Bare-Metal):**
    
    - Questo hypervisor viene installato **direttamente sull'hardware fisico** ("bare-metal"), _al posto_ di un sistema operativo tradizionale.
        
    - È il tipo più performante ed efficiente, utilizzato nei data center e nel cloud.
        
    - Esempi: **VMware vSphere (ESXi)**, **Xen**, **KVM**, Microsoft Hyper-V.
        
    - Spesso include un **control plane** (piano di controllo) distribuito, un software di gestione che permette di virtualizzare un intero cluster di host fisici, facendoli apparire come un'unica enorme macchina.
        
2. **Tipo 2 (Ospitato o Hosted):**
    
    - Questo hypervisor è un'**applicazione software** che si installa e si esegue _sopra_ un sistema operativo esistente (Host OS).
        
    - È meno efficiente perché c'è un doppio strato di sistemi operativi (Host OS + Guest OS) che competono per le risorse.
        
    - È molto comodo per lo sviluppo, il testing e l'uso desktop.
        
    - Esempi: **VMware Workstation**, **Oracle VM VirtualBox**.
        

### Caratteristiche dell'Hypervisor

Un hypervisor efficace deve garantire tre proprietà:

1. **Fedeltà (Fidelity):** Il comportamento di un programma su una VM deve essere identico a quello sulla macchina fisica.
    
2. **Sicurezza (Safety):** L'hypervisor deve avere il controllo completo delle risorse e garantire che le VM siano isolate e non possano danneggiarsi a vicenda o danneggiare l'host.
    
3. **Efficienza (Efficiency):** La stragrande maggioranza del codice della VM deve essere eseguita direttamente sulla CPU host, senza l'intervento (e l'overhead) dell'hypervisor.
    

### Altri Tipi di Virtualizzazione

- **Virtualizzazione di Processo (Process Virtualization):**
    
    - Non emula un intero hardware, ma un ambiente di esecuzione astratto per un singolo processo.
        
    - L'esempio più famoso è la **Java Virtual Machine (JVM)**, che dà l'illusione che un processo Java sia una risorsa di calcolo a sé stante, permettendo al bytecode Java (indipendente dall'hardware) di girare su qualsiasi OS che abbia una JVM.
        
    - **Virtualizzazione Basata su Container (Container-based):**
        
    - Nota anche come **virtualizzazione a livello di OS**.
        
    - È più potente della virtualizzazione di processo ma molto più leggera della virtualizzazione di sistema (VM).
        
    - I **container** non emulano l'hardware. Invece, **condividono tutti il kernel del sistema operativo host**.
        
    - L'isolamento avviene a livello di processo, rendendoli estremamente leggeri e veloci.
        

---

## Tecniche di Virtualizzazione di Sistema

L'hypervisor deve virtualizzare ogni componente dell'hardware.

### 1. Virtualizzazione del Processore

Un processore è definito dalla sua **ISA (Instruction Set Architecture)**.

- **Emulazione del Processore:**
    
    - Necessaria quando la CPU virtuale e quella reale sono _diverse_ (es. emulare una CPU ARM su un processore x86).
        
    - Virtualizza l'ISA tramite **traduzione binaria** delle istruzioni. È molto più lenta.
        
- **Virtualizzazione del Processore (Stesso Tipo):**
    
    - Se la CPU reale e quella virtuale sono dello stesso tipo (es. x86 su x86), la maggior parte delle istruzioni della VM può essere **eseguita direttamente** dalla CPU host.
        
    - Tuttavia, alcune istruzioni _privilegiate_ (quelle del kernel Guest) non possono essere eseguite direttamente, perché interferirebbero con l'Host o le altre VM (es. gestione della memoria MMU, abilitare/disabilitare interrupt).
        

#### Hardware-Assisted Virtualization (Trap-and-Emulate)

Questa è la tecnica principale usata oggi.

- Le istruzioni della VM (sia user-mode che kernel-mode) girano direttamente sulla CPU reale.
    
- Quando la VM tenta di eseguire un'istruzione "problematica" (privilegiata), la CPU fisica **"intrappola" (trap)** l'istruzione e passa il controllo all'hypervisor.
    
- L'hypervisor **"emula" (emulate)** in sicurezza il comportamento dell'istruzione e poi restituisce il controllo alla VM.
    
- Questo è reso possibile da estensioni hardware specifiche (es. **Intel VT-x** e **AMD-V**).
    

#### Full Virtualization vs. Paravirtualization

- **Full Virtualization (Virtualizzazione Completa):** La VM non sa di essere virtualizzata. Il Guest OS è _completamente non modificato_. L'hypervisor fa tutto il lavoro di "inganno" (tramite trap-and-emulate o traduzione binaria) per isolare il Guest OS.
    
- **Paravirtualization (Paravirtualizzazione):** Il Guest OS è _modificato_ e "sa" di essere virtualizzato. Invece di eseguire istruzioni privilegiate che verrebbero intrappolate, fa delle chiamate dirette all'hypervisor (chiamate **hypercall**). Questo è molto più efficiente, specialmente per l'I/O.
    
- Oggi, la maggior parte dei sistemi (come VMware e Xen) usa un **approccio ibrido**: virtualizzazione hardware per la CPU e la memoria, e driver paravirtualizzati (PV) per l'I/O per ottenere le massime prestazioni.
    

#### Virtualizzazione Multi-Processore

L'hypervisor virtualizza i core fisici del processore host in **CPU virtuali (vCPU)** e le assegna alle VM. Una singola VM può essere configurata con una o più vCPU, permettendo il multitasking simmetrico (SMP) al suo interno.

### 2. Virtualizzazione della Memoria

La virtualizzazione della memoria è complessa perché c'è un doppio livello di virtualizzazione: la memoria virtuale _all'interno_ della VM (gestita dal Guest OS) deve essere mappata sulla memoria fisica _dell'host_ (gestita dall'hypervisor).

I processori moderni (Intel EPT, AMD RVI) forniscono assistenza hardware per gestire questa doppia traduzione di indirizzi. Gli hypervisor usano anche tecniche intelligenti per ottimizzare l'uso della RAM:

- **Page Deduplication:** Se più VM hanno la stessa pagina di memoria (es. la stessa DLL di sistema), l'hypervisor la salva in memoria fisica una sola volta.
    
- **Ballooning:** Un driver speciale ("balloon driver") all'interno della VM può "gonfiarsi" (richiedere memoria al Guest OS) quando l'host ha bisogno di RAM, costringendo il Guest OS a liberare le pagine meno usate.
    

### 3. Virtualizzazione I/O

L'hypervisor gestisce l'allocazione delle risorse I/O (Input/Output). Invece di assegnare un dispositivo hardware fisico (es. una scheda di rete) direttamente a una VM, l'hypervisor assegna un **dispositivo virtuale** a ciascuna VM.

- Il Guest OS vede questo dispositivo virtuale (es. una vNIC - Virtual Network Card) e carica un driver standard per esso.
    
- Quando il Guest OS cerca di usare la vNIC, l'hypervisor intercetta l'operazione e la "traduce" in un'azione sull'hardware fisico.
    
- L'hypervisor può anche creare dispositivi puramente virtuali che non hanno una controparte fisica, come un **virtual switch (vSwitch)**.
    

### 4. Virtualizzazione dello Storage

Questo astrae lo storage fisico (dischi) dalle VM.

- **DAS (Direct Attached Storage):** Virtualizzazione di dischi connessi direttamente all'host.
    
- **Storage di Rete:**
    
    - **SAN (Storage Area Network):** Fornisce accesso a livello di _blocco_ su dischi remoti. La VM vede un disco grezzo.
        
    - **NAS (Network Attached Storage):** Fornisce accesso a livello di _file_ su condivisioni di rete.
        

Opzioni comuni di virtualizzazione dello storage:

1. **Disco Fisico Diretto:** Un disco virtuale corrisponde direttamente a un disco fisico o partizione. Offre le migliori prestazioni ma zero flessibilità.
    
2. **Immagine Disco (File):** Un disco virtuale è implementato come un singolo file (o un set di file) sul filesystem dell'host (es. `my-vm.vdi` o `my-vm.vmdk`). Offre la massima flessibilità.
    
3. **Shared Folders:** Con gli hypervisor di Tipo 2, una cartella fisica dell'host viene mappata come una cartella virtuale nel Guest OS per una facile condivisione dei file.
    

### 5. Virtualizzazione di Rete

La virtualizzazione di rete crea un'infrastruttura di rete virtuale per le VM.

- **Componenti Fisici:** Host, Schede di Rete Fisiche (pNIC), Switch Fisici (pSwitch).
    
- **Componenti Virtuali:** VM, Schede di Rete Virtuali (vNIC), Switch Virtuali (vSwitch).
    

Un **vSwitch** è un componente software dell'hypervisor che connette le vNIC tra loro e con le pNIC del mondo esterno.

#### Modalità di Rete delle vNIC

Le vNIC possono operare in diverse modalità per connettersi al mondo esterno:

- **NAT (Network Address Translation):** La VM "si nasconde" dietro l'indirizzo IP dell'host. L'host agisce come un router. Questo è ottimo per dare alla VM l'accesso a Internet senza esporla direttamente.
    
- **Bridged Networking (Rete con Bridge):** La vNIC è "collegata" (bridged) direttamente alla pNIC. La VM appare sulla rete fisica come un qualsiasi altro computer, con il proprio indirizzo IP.
    
- **Internal Networking (Rete Interna):** Le vNIC sono connesse solo a un vSwitch interno. Le VM possono parlarsi tra loro, ma non possono accedere né all'host né alla rete esterna. Utile per creare "sandbox" isolate.
    
- **Host-only Networking (Rete Solo Host):** Definisce una rete privata che contiene solo l'host e le VM. Le VM possono parlare con l'host, ma non con la rete esterna.
    

#### Port Forwarding

Una tecnica usata con la modalità NAT per rendere un servizio in esecuzione sulla VM accessibile dall'esterno. L'host inoltra il traffico da una delle sue porte a una porta della VM.

- Esempio: Mappare `host:8080` -> `guest:80`. Le richieste che arrivano all'host sulla porta 8080 vengono reindirizzate alla porta 80 della VM.
    

---

## Ciclo di Vita della VM

### Istanze, Immagini e Cloning

- **Istanza di VM (VM Instance):** Un'entità dinamica e in esecuzione con un proprio stato (memoria, registri vCPU, disco) che cambia nel tempo.
    
- **Immagine di VM (VM Image):** Un'entità statica, un "modello" o "template". Non può essere eseguita, ma viene usata per _creare_ nuove istanze. È composta da metadati (configurazione hardware virtuale) e dal contenuto dei dischi virtuali.
    
- **Relazione:** Si crea un'istanza _da_ un'immagine. Si può salvare lo stato di un'istanza _come_ una nuova immagine.
    
    - Esempio: Su Amazon EC2, si sceglie un "Tipo di Istanza" (l'hardware, es. `a1.large`) e una "Immagine" (l'AMI, es. `Ubuntu 18.04`) per creare una nuova istanza.
        
- **Cloning di VM:** Consiste nel creare una o più nuove istanze da un'immagine. Non è una semplice copia, ma una duplicazione completa della configurazione, creando VM identiche ma separate e indipendenti.
    
- **Virtual Appliance:** Un'immagine di VM pre-configurata e pronta all'uso, spesso fornita da terze parti per eseguire un software specifico (es. un firewall o un database già installato).
    

### Snapshot (Checkpoint)

Una VM può essere avviata, fermata, messa in pausa o riavviata.

- Uno **snapshot** (o checkpoint) salva lo stato _esatto_ di una VM in un determinato momento (disco, memoria e registri della vCPU).
    
- Questo permette di "riavvolgere" la VM a uno stato precedente, cosa estremamente utile per testare aggiornamenti software rischiosi o per l'analisi malware.
    
- È anche possibile avviare una VM da uno snapshot per ridurre i tempi di avvio (bypassando il boot del sistema operativo).
    

### Migrazione di VM

La migrazione sposta un'istanza di VM _in esecuzione_ da un host fisico a un altro.

- **Modo Semplice (con downtime):** Spegnere la VM sull'host A, riavviarla sull'host B.
    
- **Modo Veloce (con breve pausa):** Pausa VM, snapshot, copia snapshot su host B, riavvia VM da snapshot.
    
- **Live Migration (Migrazione a Caldo):** Se lo storage della VM (i file del disco virtuale) si trova su uno storage condiviso (SAN/NAS) accessibile da entrambi gli host, la migrazione può essere quasi istantanea. L'hypervisor deve solo copiare lo stato della memoria (RAM) attraverso la rete, per poi "switchare" l'esecuzione sull'host B con un downtime nullo o quasi nullo. Questa è una funzione chiave per l'alta disponibilità e la manutenzione del data center.
    

### Gestione delle VM

Le operazioni sulle VM (creazione, configurazione, avvio) possono essere gestite in diversi modi:

- **Manualmente:** Tramite un'interfaccia grafica (GUI) come VirtualBox, o una console web (come quella di AWS o vSphere).
    
- **Via API:** Tramite una Command-Line Interface (CLI) o una REST API. Questo è ciò che abilita l'**automazione** e l'approccio **"Infrastructure as Code" (IaC)**.
    

---

## Conseguenze e Applicazioni della Virtualizzazione

La virtualizzazione permette di eseguire applicazioni in modo fedele con un overhead prestazionale che può essere mantenuto basso.

**Benefici chiave:**

- **Flessibilità:** Rilascio flessibile di sistemi software.
    
- **Sicurezza:** Le VM sono isolate l'una dall'altra e dall'host.
    
- **Disponibilità:** Creazione e avvio rapido di nuove VM per il ripristino.
    

**Applicazioni Principali:**

- **Server Consolidation (Consolidamento dei Server):** Invece di avere 10 server fisici sottoutilizzati, si ha 1 solo server fisico che esegue 10 VM, aumentando l'utilizzo delle risorse, risparmiando energia e semplificando la gestione.
    
- **Application Consolidation:** Eseguire applicazioni "legacy" (vecchie) su hardware moderno, incapsulandole nel loro ambiente OS originale.
    
- **Sviluppo e Testing (QA):** Creare rapidamente ambienti di test multipli e isolati.
    
- **Sandboxing:** Eseguire applicazioni non sicure o sospette in una VM isolata per vedere cosa fanno senza rischiare il sistema host.
    
- **Desktop Virtualization (VDI):** Gli utenti accedono al loro "desktop" (un'istanza VM Windows/Linux) da qualsiasi client, con i dati che rimangono centralizzati nel data center.
    
- **Cloud Computing:** La virtualizzazione è la tecnologia fondamentale che abilita il cloud computing.
    

### Rilascio di Software tramite VM

Le VM sono un'opzione per il rilascio di software. Invece di installare manualmente, si può distribuire un'intera VM (o virtual appliance) con l'applicazione e tutte le sue dipendenze già configurate.

- **Approccio Moderno:** Le immagini delle VM vengono costruite automaticamente (tramite script) e le istanze VM vengono create da queste immagini.
    

**Benefici del Rilascio tramite VM:**

- **Affidabilità:** Il rilascio è semplice, basta creare una VM dall'immagine.
    
- **Isolamento:** Ogni servizio gira nella sua VM isolata.
    
- **Portabilità:** Le VM possono girare sia "on premises" (nel data center privato) sia sul cloud.
    
- **Velocità:** L'avvio di una VM richiede poco tempo (da pochi secondi a minuti).
    

**Svantaggi del Rilascio tramite VM:**

- **Inefficienza delle Risorse:** Ogni VM richiede un intero sistema operativo (con kernel, driver, ecc.), il che è uno spreco se la VM deve eseguire un singolo servizio leggero.
    
- **Overhead di Amministrazione:** Chi crea l'immagine della VM è responsabile anche degli aggiornamenti di sicurezza del sistema operativo e di tutto il software al suo interno.
    

Questi svantaggi, in particolare l'inefficienza e i tempi di avvio (secondi/minuti), hanno portato allo sviluppo della containerization.

---

### Piattaforme di Virtualizzazione x86

#### Xen

- Un hypervisor **Tipo 1** open-source per sistemi x86.
    
- Nato come progetto di ricerca, è diventato un progetto della Linux Foundation (supportato da Amazon, Google, Intel, ecc.).
    
- Supporta più Guest OS (Linux, Unix, Windows) e sia la **paravirtualizzazione (PV)** che la **virtualizzazione hardware-assisted (HVM)**.
    
- **Architettura:** Xen si posiziona direttamente sull'hardware. La prima VM che parte, `VM0` (o **`Dom0`**), è una VM privilegiata che contiene il "Toolstack" (il software di controllo) e i driver fisici per l'I/O. Le altre VM ("DomU") sono non privilegiate e usano driver paravirtualizzati (`PV front`) per comunicare con i driver `back` in Dom0.
    

#### KVM (Kernel Virtual Machine)

- Una soluzione di virtualizzazione open-source **integrata direttamente nel kernel Linux**.
    
- Può essere considerato un hypervisor **Tipo 1**.
    
- Trasforma il kernel Linux stesso in un hypervisor.
    
- Supporta Guest OS non modificati (Unix, Windows).
    
- **Architettura:** Utilizza un modulo del kernel (`kvm.ko`) per le funzionalità core di virtualizzazione. Spesso si integra con **QEMU** (un hypervisor hosted) per l'emulazione dell'hardware.
    
- Ogni **vCPU** di una VM è gestita come un normale thread Linux dall'host, permettendo un'alta efficienza.
    
- **libvirt** è un'API comune usata per gestire KVM (e altri hypervisor) in modo sicuro e remoto.
    

#### VMware

- Un'azienda leader nella virtualizzazione, offre un ricco portafoglio di prodotti.
    
- **Prodotti Desktop (Tipo 2):** VMware Workstation (Windows/Linux) e Fusion (macOS).
    
- **Prodotti Data Center (Tipo 1):** **vSphere** (che include l'hypervisor **ESXi**) e la suite vCloud per la gestione del cloud privato.
    
- **Prodotti Desktop Virtualization (VDI):** Horizon.
    
- **VMware Workstation (Architettura Tipo 2):** Si basa su tre componenti: il **VMM** (l'hypervisor hosted), il **VMX** (l'interfaccia utente nell'Host OS) e un **VMM Driver** (un driver nell'Host OS che gestisce il VMM).
    

#### VirtualBox

- Un prodotto di virtualizzazione open-source (controllato da Oracle) per uso personale e aziendale.
    
- È un hypervisor di **Tipo 2**, disponibile per host Windows, Linux e macOS.
    
- Supporta Guest OS Windows e Linux.
    
- Può essere gestito sia tramite GUI che tramite la potente interfaccia a riga di comando `VBoxManage`.

---
# Cloud computing
## Introduzione al Cloud Computing

Il cloud computing deriva da un'idea vecchia: vedere l'informatica (le risorse computazionali) come un **servizio di utility**, simile all'elettricità o all'acqua.

Esiste un'infrastruttura centrale che funge da fornitore del servizio (utility provider). Tutti i dispositivi circostanti (laptop, desktop, telefoni, tablet) possono sfruttare le risorse di calcolo di questa infrastruttura in modo "plug-and-play".

---

## Una Definizione di Cloud Computing

Secondo la definizione del **NIST** (National Institute of Standards and Technology), il cloud computing è:

> "un modello per abilitare un accesso di rete **ubiquo, conveniente e on-demand** a un **pool condiviso e configurabile** di risorse computazionali (es. CPU, storage, reti, sistemi operativi, servizi e/o applicazioni) che possono essere **acquisite e rilasciate rapidamente** e dinamicamente con uno sforzo di gestione minimo, o comunque con minima interazione con il service provider."

Questo modello di elaborazione prevede **cinque caratteristiche essenziali**, **tre modelli di servizio** e **quattro modelli di deployment** (distribuzione).

---

## Modelli di Servizio (Il Modello SPI)

I principali modelli di servizio nel cloud computing sono:

### 1. Software as a Service (SaaS)

È un modello di distribuzione software in cui le applicazioni sono ospitate da un service provider e rese disponibili agli utenti tramite Internet.

- **Cosa gestisci tu:** Niente. Usi solo il software.
    
- **Cosa gestisce il provider:** Applicazioni, Dati, Runtime, Middleware, OS, Virtualizzazione, Server, Storage, Networking.
    
- **Esempi:** Google Workspace (Gmail, Google Docs), Microsoft Office 365, Netflix, Salesforce.com (CRM).
    

### 2. Platform as a Service (PaaS)

I servizi PaaS forniscono un ambiente completo per lo sviluppo e l'esecuzione (deployment) delle applicazioni.

- **Cosa gestisci tu:** Le tue Applicazioni e i tuoi Dati.
    
- **Cosa gestisce il provider:** Runtime, Middleware, OS, Virtualizzazione, Server, Storage, Networking.
    
- **Esempi:** Google App Engine, Amazon Elastic Beanstalk, Service App Microsoft Azure.
    

### 3. Infrastructure as a Service (IaaS)

I servizi IaaS forniscono accesso virtuale a risorse hardware fondamentali, come server (VM), reti, storage e altri componenti infrastrutturali.

- **Cosa gestisci tu:** Applicazioni, Dati, Runtime, Middleware, Sistema Operativo (OS).
    
- **Cosa gestisce il provider:** Virtualizzazione, Server, Storage, Networking.
    
- **Esempi:** Molti prodotti Amazon Web Services (AWS), come EC2.
    

Il modello SPI (SaaS, PaaS, IaaS) rappresenta un **trade-off tra flessibilità e ottimizzazione**:

- **IaaS** offre la massima **flessibilità** e controllo.
    
- **SaaS** offre la massima **ottimizzazione** (semplicità) per l'utente finale.
    

---

## Modelli di Deployment (Distribuzione)

Il cloud computing include quattro modelli di deployment:

- **Cloud Pubblico (Public Cloud):** L'infrastruttura cloud è resa disponibile al pubblico generale ed è gestita da un provider esterno.
    
- **Cloud Privato (Private Cloud):** L'infrastruttura cloud è gestita e utilizzata da una singola organizzazione.
    
- **Cloud Ibrido (Hybrid Cloud):** È una composizione di due o più cloud (pubblici o privati) che rimangono entità distinte ma sono interconnesse.
    
- **Cloud Comunitario (Community Cloud):** L'infrastruttura è condivisa da più organizzazioni con interessi o requisiti comuni.
    

---

## Architettura e Tecnologie Abilitanti del Cloud

### Architettura Cloud

Si può pensare al cloud in termini di un'architettura stratificata, che riflette il modello SPI:

1. **Software as a Service (SaaS)**
    
2. **Platform as a Service (PaaS)**
    
3. **Infrastructure as a Service (IaaS)**
    

### Tecnologie Abilitanti

1. **Hardware (Data Center):**
    
    - **Rack:** Armadi metallici che ospitano l'hardware.
        
    - **Server/Nodi/Blade:** I computer fisici che forniscono la potenza di calcolo.
        
    - **Storage Devices:** Dispositivi di archiviazione (dischi).
        
    - **Network Switches:** Apparati che connettono i server tra loro e con altri rack.
        
2. **Data Center (Co-location):**
    
    - I data center sono edifici fisici che ospitano migliaia di rack.
        
    - Questi edifici forniscono le infrastrutture critiche:
        
        - **Reti** (connettività Internet ad alta velocità).
            
        - **Energia Elettrica** (con sistemi di backup come UPS e generatori).
            
        - **Condizionamento** (sistemi di raffreddamento avanzati).
            
    - Un'infrastruttura cloud globale è composta da _molti_ data center distribuiti geograficamente.
        
3. **Virtualizzazione:**
    
    - Questa è la tecnologia software _chiave_.
        
    - Un **Virtual Machine Monitor (Hypervisor)** astrae l'hardware fisico del server.
        
    - Permette a un singolo server fisico di eseguire più **macchine virtuali (VM)** isolate, che vengono poi fornite ai clienti (es. Alice, Bob, Charlie).
        

---

## Cloud Computing e Servizi

Nel cloud, un **servizio** è un'entità computazionale ben definita, gestita da un provider.

- È **incapsulato**, ovvero espone un'interfaccia definita contrattualmente.
    
- La sua implementazione interna è **trasparente** agli utenti.
    
- È accessibile via Internet da un client (il consumatore del servizio).
    

### Esempi di Piattaforme Cloud

#### Google App Engine (GAE)

- Un servizio **PaaS** (Platform as a Service) _serverless_ e completamente gestito da Google.
    
- Supporta molti linguaggi (Java, PHP, Node.js, ecc.).
    
- L'utente deve solo "scrivere il codice"; GAE gestisce automaticamente l'esecuzione, il bilanciamento del carico e la scalabilità.
    
- Offre autenticazione, sicurezza (sandboxing) e un modello di pagamento "pay-per-use" (inizialmente gratuito).
    

#### Amazon Web Services (AWS)

AWS è il leader di mercato e offre una suite completa di servizi IaaS e PaaS.

**Servizi IaaS Chiave:**

- **Amazon EC2 (Elastic Compute Cloud):** Fornisce risorse di calcolo (macchine virtuali). Le VM vengono create da modelli chiamati **AMI (Amazon Machine Image)**. Le AMI possono essere preconfigurate con vari OS (Linux, Windows) e software.
    
- **Amazon S3 (Simple Storage Service):** Un servizio di **object storage** (archiviazione a oggetti). I dati sono memorizzati come "oggetti" (da 1 byte a 5 GB) e accessibili tramite API web (REST/SOAP). Offre varie opzioni di sicurezza (ACL, autenticazione) e affidabilità.
    
- **Amazon EBS (Elastic Block Store):** Un servizio di **block storage** (archiviazione a blocchi). Funziona come un hard disk virtuale (volume) che può essere "montato" su un'istanza EC2.
    

**Servizi PaaS e Serverless Chiave:**

- **Amazon RDS (Relational Database Service):** Un servizio gestito per database relazionali (es. MySQL, Oracle, PostgreSQL).
    
- **Amazon DynamoDB:** Un servizio gestito per database NoSQL (non relazionali).
    
- **AWS Elastic Beanstalk:** Un servizio PaaS per il deploy rapido di applicazioni web (simile a GAE). L'utente carica l'applicazione e Beanstalk gestisce automaticamente il provisioning, il bilanciamento del carico e il monitoraggio.
    
- **Amazon ECS (Elastic Container Service):** Un servizio di **orchestrazione di container** altamente scalabile e completamente gestito.
    
- **AWS Lambda:** Un servizio di elaborazione **serverless** ("senza server"). Esegue codice (Funzioni Lambda) in risposta a eventi (es. richieste HTTP, modifiche su S3), gestendo automaticamente le risorse di calcolo.
    

AWS e DevOps:

AWS fornisce un set completo di servizi per supportare le pratiche DevOps (la combinazione di Sviluppo e Operations), inclusi servizi per:

- Provisioning e gestione dell'infrastruttura.
    
- Gestione del codice sorgente (es. CodeCommit).
    
- Automazione del rilascio del software (es. CodePipeline).
    
- Monitoraggio.
    

Regioni e Zone di Disponibilità (AZ):

L'infrastruttura globale di AWS è fondamentale per l'alta disponibilità.

- **Regione (Region):** Una località geografica (es. EU/Irlanda, US East/Ohio) dove i data center sono raggruppati.
    
- **Zona di Disponibilità (Availability Zone - AZ):** Un set di uno o più data center all'interno di una regione, dotati di alimentazione, rete e connettività ridondanti e indipendenti.
    
- Distribuendo le applicazioni su più AZ, è possibile garantire la continuità del servizio anche in caso di guasto di un intero data center.
    

#### Microsoft Azure

Microsoft Azure è un'altra piattaforma cloud leader che offre una gamma completa di servizi IaaS, PaaS e SaaS.

- È una piattaforma completa e flessibile che supporta anche soluzioni "open", non necessariamente legate al mondo Microsoft, come VM Linux e servizi di orchestrazione Docker.
    
- **Servizi Chiave:** Virtual Machines (Windows o Linux), Azure App Service (PaaS), Azure SQL Database, Azure Kubernetes Service (AKS), e Azure Functions (serverless).
    

#### Altri Player

- **Salesforce.com:** Leader nel mercato **SaaS** (con le sue applicazioni CRM), ma offre anche una piattaforma **PaaS** (force.com) per lo sviluppo di applicazioni personalizzate.
    
- **Cloud Foundry:** Una piattaforma **PaaS open-source**. La sua architettura basata su container permette di eseguire applicazioni in qualsiasi linguaggio su qualsiasi cloud (pubblico o privato), garantendo la portabilità.
    
- **Netflix:** Un perfetto esempio di **SaaS** (distribuzione di contenuti video). Utilizza un'architettura a microservizi, con componenti rilasciati in container, che gira quasi interamente sull'infrastruttura cloud **IaaS** di Amazon (AWS).
    

---

## Attori Coinvolti (Player)

Un'organizzazione o una persona può assumere uno o più dei seguenti ruoli:

- **Cloud Provider:** Il fornitore dell'utility computing (IaaS o PaaS).
    
- **Cloud User (o Consumer):** L'utente (consumatore) dell'utility computing (IaaS o PaaS).
    
- **SaaS Provider:** Il fornitore di un'applicazione SaaS. Potrebbe anche essere un Cloud User (se ospita la sua app su un IaaS).
    
- **SaaS User:** L'utente (consumatore) finale di un'applicazione SaaS.
    

**Esempio:** Mario Rossi guarda Netflix, che gira su Amazon AWS.

- **Mario Rossi:** SaaS User.
    
- **Netflix Inc.:** SaaS Provider (fornisce Netflix) E Cloud User (consuma risorse AWS).
    
- **Amazon:** Cloud Provider (fornisce servizi IaaS/PaaS).
    

---

## Campi di Applicazione e Caratteristiche Economiche

### Campi di Applicazione

Il cloud computing è utilizzato in molti campi:

- Web applications.
    
- Estensione di software desktop (es. Matlab, Mathematica).
    
- Applicazioni con necessità momentanee di grandi risorse di calcolo.
    
- Prototipazione rapida.
    
- Startup (che possono evitare costi hardware iniziali).
    
- Attività di ricerca.
    

### Caratteristiche Essenziali (NIST)

Le 5 caratteristiche essenziali del cloud computing sono:

1. **Servizi On-Demand:** Un consumatore può acquisire risorse (es. VM) unilateralmente e automaticamente.
    
2. **Accesso via Rete (Broad Network Access):** Le risorse sono accessibili tramite Internet.
    
3. **Pool di Risorse (Resource Pooling):** Le risorse di un provider sono raggruppate per servire molti consumatori (modello _multi-tenant_).
    
4. **Elasticità Rapida (Rapid Elasticity):** Le risorse possono essere ottenute (e rilasciate) rapidamente e in modo flessibile per adattarsi alla domanda.
    
5. **Servizio Misurato (Measured Service):** L'uso delle risorse è controllato e misurato automaticamente (es. per fatturazione).
    

### Economia del Cloud Computing

#### Per il Consumatore (Cloud User)

Gli aspetti economici chiave per chi _usa_ il cloud sono:

- **Modello Pay-per-Use:** Il cloud permette la transizione da una spesa in conto capitale (**CAPEX** - acquisto di hardware) a una spesa operativa corrente (**OPEX** - pagamento di una "bolletta" mensile).
    
- **Elasticità:** Permette di mitigare i rischi di un dimensionamento errato dell'infrastruttura.
    
    - **Over-provisioning (Statico):** Acquistare hardware per il picco di domanda significa sprecare risorse (costi) quando la domanda è bassa.
        
    - **Under-provisioning (Statico):** Acquistare hardware per la domanda media significa perdere clienti e ricavi (Lost revenue/users) quando la domanda supera la capacità.
        
    - **Cloud (Elastico):** La capacità si adatta dinamicamente alla domanda, minimizzando gli sprechi e massimizzando i ricavi.
        
- **Economie di Scala:** I grandi provider possono costruire data center enormi, ottenendo risorse (hardware, rete, energia) a costi molto più bassi rispetto a una piccola o media azienda. Possono quindi vendere queste risorse a prezzi vantaggiosi.
    

#### Per il Fornitore (Cloud Provider)

I benefici per chi _offre_ il cloud sono:

- Sfruttare le economie di scala.
    
- Capitalizzare:
    
    - Amazon ha iniziato sfruttando la capacità di calcolo residua (inutilizzata) al di fuori dei periodi di picco (es. Natale).
        
    - Google ha sfruttato l'infrastruttura esistente, costruita per i propri servizi.
        
- Difendere un brand (es. Microsoft per vendere strumenti .NET).
    
- Rafforzare le relazioni con i clienti (es. offrendo un servizio di disaster recovery in cloud).
    

Le conseguenze economiche includono il supporto all'innovazione: le piccole startup possono avviare un business con costi iniziali minimi, senza dipendere da investitori esterni per acquistare hardware.

---

## Sistemi Software per il Cloud

Rilasciare software sul cloud richiede un'architettura diversa per sfruttarne le caratteristiche.

- **Rischi:** Rilascio in un ambiente di esecuzione condiviso; utilizzo di servizi specifici del provider (rischio di _vendor lock-in_).
    
- **Opportunità:** Rilascio su piattaforme elastiche, scalabili e disponibili.
    
- **Sfida:** Rendere effettivamente un'applicazione scalabile, disponibile e modificabile.
    

**Requisiti per i sistemi software cloud:**

- **Alta disponibilità:** Nessuna interruzione del servizio.
    
- **Scalabilità:** Accettare un numero crescente di utenti o richieste.
    
- **Modificabilità:** Cicli di sviluppo e feedback rapidi (DevOps).
    
- Supporto per client mobili, IoT e Big Data.
    

Per ottenere ciò, è necessario utilizzare tattiche e pattern specifici e automatizzare la gestione dell'infrastruttura e dei rilasci. Il cloud, infatti, offre modelli di servizio (IaaS, PaaS) e modelli di deployment (pubblico, privato) che supportano diverse opzioni per gli ambienti di esecuzione e il rilascio automatizzato (DevOps).

---
# Containerization

## Virtualizzazione basata su container

La **virtualizzazione basata su container** (o _containerization_) è un'infrastruttura che permette alle applicazioni di girare in ambienti isolati noti come **container**.

I container sono un'unità di distribuzione software che racchiude l'applicazione e **tutte le sue dipendenze** (librerie, strumenti, file di configurazione, ecc.) in un ambiente isolato.

Questi container sono noti per essere **estremamente leggeri e veloci da avviare**, poiché **condividono il kernel del sistema operativo (OS) host** anziché virtualizzare un intero sistema operativo (e l'hardware sottostante), come fanno invece le macchine virtuali (VM).

---

### Come funzionano i container
![[Pasted image 20251105164608.png]]
La virtualizzazione basata su container, specialmente nel mondo Unix/Linux, è una forma di virtualizzazione leggera, chiamata anche **virtualizzazione a livello di OS** perché è supportata direttamente dal kernel del sistema operativo host.

Il software di virtualizzazione (il **container engine**, come Docker) permette di definire un container come un insieme di processi e altre risorse. Ad esempio, un container che esegue un servizio Java consiste essenzialmente in un processo JVM in esecuzione sull'host.

#### Considerazioni chiave

- **Kernel Condiviso:** Il sistema host esegue **un solo kernel condiviso**, che gestisce le risorse sia per l'host stesso sia per tutti i container in esecuzione.
    
- **Isolamento Virtuale:** Sebbene il kernel sia condiviso, ogni container esegue il proprio _spazio utente_ (user-space) e ha le proprie risorse "virtuali" (come un proprio file system completo, uno stack di rete e un proprio indirizzo IP).
    
- **Ruolo del Container Engine:** Il software di virtualizzazione (es. Docker Engine) garantisce l'**isolamento** tra i container e tra i container e l'host.
    
- **Gestione dei Processi:** I processi all'interno di un container sono gestiti come normali processi host, ma sono isolati in modo che il container "veda" solo i propri processi.
    
- **Gestione del Filesystem:** Il file system di un container è gestito come un sotto-albero del file system host (ad esempio, in `/var/lib/docker/containers/...`), ma il container lo vede come la propria directory root (`/`).
    

---

## Il Container

Un container è un'unità software standardizzata che impacchetta una o più applicazioni, insieme alle loro configurazioni e dipendenze, in modo che queste applicazioni possano essere eseguite in modo rapido e affidabile in un ambiente di esecuzione appropriato.

- Ogni istanza di container è tipicamente utilizzata per eseguire un **singolo servizio o applicazione specifica**, realizzando un ambiente di esecuzione virtuale completo e autonomo, con tutte le dipendenze necessarie (librerie OS, runtime, middleware).
    
- Il container è anche un **ambiente di esecuzione standardizzato**. Questo significa che un'applicazione "containerizzata" può essere rilasciata ed eseguita in modo coerente su una varietà di piattaforme (dal laptop dello sviluppatore, al server di test, al cloud).
    

### Vantaggi e Svantaggi

- **Overhead Basso:** I container introducono un overhead molto più basso rispetto alle VM. Le prestazioni sono **quasi native**, poiché non c'è emulazione hardware né un hypervisor.
    
- **Flessibilità Limitata:** I container offrono meno flessibilità operativa e un isolamento inferiore rispetto alle VM. L'OS del container (il suo user-space) **deve essere compatibile con il kernel dell'host** (es. non è possibile eseguire container Windows su un host Linux, o viceversa). Per questo molto spesso la parte grafica si appoggia alle Web-App, cioè si appoggiano ai browser. Se voglio aprire un applicazione con interfaccia grafica scritto, ad esempio, in Java con le sue librerie, qui ho bisogno di una VM (questo perché ho bisogno di un Windows Manager).
    
- **Isolamento di Sicurezza:** L'isolamento tra le VM è completo (a livello hardware). L'isolamento tra i container non è completo (a livello di kernel). Una vulnerabilità nel kernel host può potenzialmente compromettere tutti i container.
    

### Container vs. VM: L'Interfaccia
![[Pasted image 20251105170529.png]]

Il confronto fondamentale tra VM e container può essere visto dal punto di vista dell'interfaccia che espongono:

- L'interfaccia esposta da una **VM** è quella dell'**hardware** di un computer.
    
- L'interfaccia esposta da un **Container** è quella del **kernel di un OS** (ovvero, l'interfaccia delle _system call_).
    

### Istanza vs. Immagine
![[Pasted image 20251105170539.png]]

Proprio come per le VM, è fondamentale distinguere tra istanze e immagini:

- **Istanza di Container (Container Instance):** È un'entità _dinamica_ ed eseguibile. Include le librerie dell'OS, gli strumenti e le applicazioni installate. È un processo (o un gruppo di processi) in esecuzione sull'host.
    
- **Immagine di Container (Container Image):** È un'entità _statica_ e immutabile. È lo "snapshot" del file system di un container e funge da **modello** per creare nuove istanze. Include tutto il software necessario per eseguire l'applicazione.
    

---

### Tipi di Container

Esiste una classificazione principale per i container:

1. **OS Container:**
    
    - Progettato per essere usato come una **VM leggera**.
        
    - Avvia un sistema operativo quasi completo (con un processo `init`, gestione dei servizi, ecc.) ed è pensato per eseguire _più applicazioni_ o servizi al suo interno.
        
    - Esempio: **LXC**.
        
2. **Application Container:**
    
    - Progettato per contenere ed eseguire **una singola applicazione o servizio** (es. un web server, un database).
        
    - Questo è il modello che ha reso popolare Docker e che sta alla base delle architetture a **microservizi**.
        

#### Vantaggi degli Application Container

Focalizzare ogni container su una singola applicazione offre enormi vantaggi:

- **Isolamento dell'Applicazione:** Isola le singole applicazioni in ambienti autonomi, migliorando [[Reliability|affidabilità]] e [[Safety|sicurezza]].
    
- **Gestione delle Dipendenze:** Ogni container include _solo_ le dipendenze necessarie per la sua specifica applicazione, eliminando i conflitti tra le dipendenze di diverse applicazioni.
    
- **Leggerezza e Velocità:** I container sono leggeri e possono essere creati e avviati in pochi secondi (o meno), migliorando drasticamente l'efficienza e la scalabilità.
    

---

### Tecnologie per la Containerization

Esistono diverse tecnologie di container, principalmente nel mondo UNIX/Linux:

- **LXC (Linux Containers)**
    
- OpenVZ (per Linux)
    
- Solaris Containers (per Solaris)
    
- FreeBSD jail
    
- **Docker**
    

### LXC (Linux Containers)

LXC è un insieme di strumenti e API per creare e gestire container su un host Linux.
![[Pasted image 20251105173536.png]]

- Sfrutta le funzionalità del kernel Linux per creare gerarchie di processi isolate, ognuna con le proprie risorse (CPU, memoria, disco).
    
- **Kernel Condiviso:** Anche se il kernel è quello dell'host, è possibile eseguire sistemi operativi (user-space) diversi all'interno dei container, purché siano distribuzioni Linux (es. un container CentOS 7 su un host Ubuntu 18.04).
    
- **Isolamento:** LXC fornisce un livello di isolamento simile alle VM ma senza la necessità di un hypervisor.
    

LXC combina due potenti funzionalità del kernel Linux per ottenere l'isolamento:

1. **Control Groups (cgroup):**
    
    - Questa funzione permette di **isolare, limitare e misurare l'uso delle risorse** (CPU, memoria, rete, I/O del disco) assegnate a un gruppo di processi.
        
2. **Namespaces (Spazi dei Nomi):**
    
    - Questa funzione controlla la **visibilità** delle risorse. Permette di disaccoppiare un gruppo di processi dalle risorse reali.
        
    - Ad esempio, un container ha il proprio _namespace PID_ (vede solo i propri processi, con il processo principale come PID 1), il proprio _namespace di rete_ (proprio indirizzo IP e porte) e il proprio _namespace utente_ (propri ID utente).
        

---

## Docker

**Docker** ([www.docker.com](https://www.docker.com)) è la piattaforma di container più popolare, progettata per **costruire, rilasciare ed eseguire applicazioni distribuite** in modo semplice, veloce, scalabile e portabile.
![[Pasted image 20251105173553.png]]

- Un container Docker è un'unità software standardizzata che impacchetta un servizio software con le sue configurazioni e dipendenze.
    
- I container Docker sono leggeri (usano poche risorse e si avviano rapidamente), standardizzati, open-source e sicuri.
    
- Sono **portatili**: possono girare su qualsiasi macchina con Docker (Linux, Windows, Mac OS) e sul cloud.
    

### Piattaforma Docker

La piattaforma Docker (nata nel 2013) è stata inizialmente costruita sopra i container LXC (2008). Oggi si basa su librerie proprie come `containerd` e `runc`, che interfacciano direttamente le funzionalità del kernel (cgroup e namespace).
![[Pasted image 20251105173952.png]]
La piattaforma Docker abilita la **separazione tra le applicazioni e l'infrastruttura** di esecuzione, semplificando il rilascio del software e garantendo la portabilità.

Le caratteristiche principali offerte dalla piattaforma Docker includono:

- Creare un container (un'istanza) da un'immagine.
    
- Avviare, monitorare, ispezionare, arrestare e distruggere i container.
    
- Creare e gestire le immagini dei container.
    
- Gestire gruppi correlati di container per eseguire applicazioni distribuite multi-container (ad esempio, con **Docker Compose**).
    

---

### Container Docker vs. Macchine Virtuali

- **Flessibilità:** I container offrono meno flessibilità delle VM. L'OS di un container deve essere compatibile con il kernel dell'host (solitamente Unix/Linux). Le VM possono eseguire OS completamente diversi (es. Windows su un host Linux).
    
- **Costo (Overhead):** La flessibilità delle VM ha un costo in termini di risorse (ogni VM ha un intero OS), overhead di esecuzione (l'hypervisor) e tempi di avvio (minuti vs. secondi).
    
- **Leggerezza:** I container sono "più leggeri" delle VM. Richiedono meno risorse, hanno prestazioni quasi native e possono essere creati e avviati molto più velocemente.
    
- **Isolamento:** L'isolamento tra le VM è completo (a livello hardware). L'isolamento tra i container non è completo (il kernel è condiviso).
    

### Container e Rilascio del Software

I container (in particolare gli "application container") sono un'opzione eccellente per il rilascio di software:

**Benefici:**

- Ogni container incapsula un singolo servizio software in modo facile e affidabile.
    
- Garantisce l'isolamento dei guasti (fault isolation) e la sicurezza tra i servizi.
    
- I container sono leggeri.
    
- I container possono essere rilasciati sia "on-premises" (su server locali) sia nel cloud, e gestiti da piattaforme di orchestrazione (es. Kubernetes).
    

**Svantaggi:**

- L'isolamento tra i container non è completo (condivisione del kernel).
    
- Overhead nell'amministrazione e aggiornamento delle immagini dei container.
    
- Overhead nell'amministrazione dell'infrastruttura di esecuzione, a meno che non si utilizzino soluzioni cloud gestite (come AWS ECS o Google GKE).
    

---

## Docker Engine

Il cuore della piattaforma Docker è il **Docker Engine**.
![[Pasted image 20251105174022.png]]

Il Docker Engine si basa su un'**architettura client-server**:

- **Server (Host):** È un host che esegue il processo daemon di Docker (`dockerd`). Questo daemon gestisce tutti gli oggetti Docker (container, immagini, reti e volumi).
    
- **Client:** È il comando `docker` che l'utente usa dalla riga di comando (CLI). Comunica con il daemon Docker sull'host tramite una REST API.
    
- **Registry (Registro):** Contiene un set di immagini. Il registry pubblico predefinito di Docker è **Docker Hub**.
    

### Image Registry

- Un **registry** è un servizio (pubblico o privato) che contiene una collezione di immagini di container.
    
- Un registry pubblico ospita generalmente immagini di base (es. `ubuntu`, `postgres`, `openjdk`).
    
- **Docker Hub** ([https://hub.docker.com](https://hub.docker.com)) è il registry pubblico ufficiale di Docker.
    
- Un **repository** è una porzione di un registry che contiene un set di immagini correlate, solitamente varianti o versioni diverse della stessa immagine (es. il repository `ubuntu` contiene i tag `20.04`, `22.04`, `latest`).
    

---

## Oggetti Docker

### Container

- Un container è un'**istanza eseguibile** di un'immagine.
    
- È un'entità **dinamica** che esiste durante l'esecuzione (runtime).
    
- Ha un proprio **stato**, che può cambiare durante l'esecuzione (es. contenuto del file system, stato della sessione in memoria).
    

### Immagine (Image)

- Un'immagine è un set di file che rappresenta lo snapshot del file system di un container. È un **modello** per creare container (es. un'immagine con Ubuntu, OpenJDK e un'applicazione Java specifica).
    
- È un concetto **statico**, che non viene eseguito direttamente.
    
- Non ha uno stato proprio; è **immutabile**.
    

### Interagire con Docker

L'interazione con un host Docker avviene tramite la **Command-Line Interface (CLI)**, `docker`.

- `docker image ...` (comandi per la gestione delle immagini)
    
- `docker container ...` (comandi per la gestione dei container)
    

#### Comandi di Base

- `docker image build` (o `docker build`): Permette di costruire un'immagine (custom).
    
    - `docker build -t image-name context`
        
- `docker container create` (o `docker create`): Permette di creare un nuovo container da un'immagine (senza avviarlo).
    
    - `docker create --name=container-name image-name`
        
- `docker container start` (o `docker start`): Permette di avviare un container già creato.
    
    - `docker start container-name`
        
- `docker container run` (o `docker run`): Crea e avvia un nuovo container (possibilmente anonimo) con un singolo comando.
    
    - `docker run [--name=container-name] image-name`
        

#### Esempi di `docker run`

- docker run hello-world
    
    Questo è un test classico. Il client contatta il daemon. Il daemon scarica (pull) l'immagine "hello-world" da Docker Hub (se non è già presente localmente), crea un nuovo container da quell'immagine, lo esegue (producendo l'output "Hello from Docker!"), e il daemon invia l'output al client.
    
- docker run docker/whalesay cowsay Hello, world!
    
    Avvia un container dall'immagine docker/whalesay, che esegue il programma cowsay passando "Hello, world!" come argomento.
    

---

## Creazione di Immagini (Imaging)

Per creare un'immagine personalizzata, Docker usa un approccio **"infrastructure-as-code"** basato su un file di testo speciale chiamato **Dockerfile**.

- Il `Dockerfile` contiene un set di comandi che Docker esegue per costruire un'immagine.
    
- Il comando `docker build -t image-name context` avvia la costruzione. Il `context` è la directory (di solito `.`) che contiene il Dockerfile e tutti i file necessari (es. il file `.jar` dell'applicazione).
    

### Istruzioni del Dockerfile

Un Dockerfile è una sequenza di istruzioni:

- FROM busybox:latest
    
    FROM specifica l'immagine di base da cui partire (es. busybox è una distribuzione Linux minima).
    
- ENTRYPOINT ["echo", "Hello, world!"]
    
    ENTRYPOINT specifica l'eseguibile o il comando che deve essere eseguito all'avvio del container.
    
- CMD ["Hello, world!"]
    
    CMD specifica gli argomenti predefiniti per l'ENTRYPOINT. La differenza chiave è che gli argomenti CMD possono essere sovrascritti dalla riga di comando quando si esegue docker run.
    
    - `docker run myhello2` -> Esegue `echo Hello, world!`
        
    - `docker run myhello2 Ciao, mondo!` -> Esegue `echo Ciao, mondo!`
        
- RUN (RUN apt-get update)
    
    Specifica un comando che deve essere eseguito durante la costruzione dell'immagine (es. per installare dipendenze, configurare l'ambiente).
    
    - **Differenza chiave:** `RUN` viene eseguito _una volta_ al momento del build. `ENTRYPOINT` e `CMD` vengono eseguiti _ogni volta_ che il container viene avviato.
        
- VOLUME (VOLUME /var/www/html)
    
    Definisce un punto di mount per i dati (volumi) dal sistema host o da un altro container. Questo è fondamentale per i dati persistenti.
    
- EXPOSE (EXPOSE 80)
    
    Specifica (documenta) le porte su cui il container è in ascolto durante l'esecuzione. Non pubblica la porta; serve a informare l'operatore.
    

---

### Esempio: Dockerfile per Apache HTTP Server

Dockerfile

```
# Dockerfile per Apache HTTP Server
FROM ubuntu:18.04

# Installa il pacchetto apache2
RUN apt-get update && \
    apt-get install -y apache2

# Altre istruzioni
ENV APACHE_LOG_DIR /var/log/apache2
VOLUME /var/www/html
EXPOSE 80

# Avvia il server apache2 in foreground
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
```

- **`FROM`**: Specifica l'immagine di base (Ubuntu 18.04).
    
- **`RUN`**: Aggiorna i repository e installa `apache2`.
    
- **`ENV`**: Imposta una variabile d'ambiente necessaria per Apache.
    
- **`VOLUME`**: Dichiara che `/var/www/html` (dove Apache salva i siti) dovrebbe essere gestito come un volume (per dati persistenti).
![[Pasted image 20251105163915.png]]    
- **`EXPOSE 80`**: Documenta che il container ascolterà sulla porta 80.
    
- **`ENTRYPOINT`**: Avvia Apache in modalità "FOREGROUND" (necessario affinché il container non si spenga immediatamente).
    

#### Utilizzo dell'immagine Apache

1. Costruzione dell'immagine:
    
    docker build -t myapache .
    
2. Creazione del container:
    
    docker create -v ~/projects/www:/var/www/html -p 8080:80 --name=myapache myapache
    
    - `-v ~/projects/www:/var/www/html`: Monta la directory locale `~/projects/www` all'interno del container in `/var/www/html`.
        
    - `-p 8080:80`: Esegue il **port forwarding**, mappando la porta 8080 dell'host sulla porta 80 (quella esposta) del container.
        
3. Esecuzione del container:
    
    docker start myapache
    
    (Ora è possibile accedere a http://localhost:8080 sull'host).
    

---

### Altri Comandi Docker Utili

#### Gestione Container

- `docker container ls` o `docker ps [-a]`: Lista i container in esecuzione (o tutti, con `-a`).
    
- `docker container port <container-name>`: Ispeziona le porte mappate.
    
- `docker container inspect <container-name>`: Restituisce informazioni dettagliate (in JSON) su un container.
    
- `docker container logs <container-name>`: Mostra i log (output standard) generati da un container.
    
- `docker container stop <container-name>`: Ferma un container in esecuzione.
    
- `docker container rm <container-name>`: Rimuove un container (deve essere fermato prima).
    

#### Gestione Immagini

- `docker image ls` o `docker images`: Lista le immagini nella cache locale.
    
- `docker image rm <image-name>` o `docker rmi`: Rimuove un'immagine dalla cache locale.
    

#### Gestione Remota

È possibile usare il client Docker per specificare comandi a un host Docker remoto:

- Usando il flag `-H`: `docker -H=tcp://docker-host:2375 ps`
    
- Impostando la variabile d'ambiente `DOCKER_HOST`: `export DOCKER_HOST=tcp://docker-host:2375`
    

---

### Formato delle Immagini (Layered File System)

Il file system di un'immagine (e di un container) è composto da una serie di **strati (layers)**.

- Questi strati sono combinati in un'unica vista coerente grazie al **Union File System (UFS)**.
    
- È un formato leggero che permette la condivisione degli strati: se più immagini condividono la stessa base (es. `ubuntu`), quella base è archiviata su disco una sola volta.
    
- Ogni strato superiore può sovrascrivere o nascondere i file degli strati sottostanti.
    
- Quando un file viene richiesto, Docker lo cerca a partire dallo strato più alto e scende finché non lo trova.
    

#### Costruzione e Strati

- Un'immagine Docker è basata su un'immagine di base (`FROM`), che costituisce il primo strato (o set di strati) _read-only_.
    
- Ogni istruzione successiva nel Dockerfile (come `RUN`, `COPY`, `ADD`) crea un **nuovo strato read-only** separato.
    
- Quando un container viene creato, Docker aggiunge un ultimo strato finale, noto come **"read-write layer" (strato scrivibile)**.
    
- Questo strato è l'unica parte modificabile del file system del container. Tutte le modifiche (creazione, modifica, cancellazione di file) avvengono in questo strato sottile tramite un meccanismo di **Copy-on-Write (CoW)**.
    

### Creazione ed Esecuzione di Container

- **Creazione:** Creare un container da un'immagine significa essenzialmente prendere gli strati read-only dell'immagine e aggiungervi sopra un nuovo strato scrivibile.
    
- **Esecuzione:**
    
    1. **Allocazione Risorse:** Il container engine alloca le risorse di runtime (es. crea i `namespaces` nel kernel host).
        
    2. **Configurazione Rete:** Configura la rete per il container (es. crea un'interfaccia di rete virtuale).
        
    3. **Avvio:** Avvia il container usando l'immagine (e il suo file system a strati).
        
    4. **Esecuzione Comando:** Esegue il comando specificato dall'`ENTRYPOINT` (con gli argomenti `CMD`).
        

---

### Volumi e Condivisione Dati

Lo strato scrivibile del container è effimero: viene eliminato quando il container viene rimosso (docker rm).

Per gestire dati persistenti, si usano i volumi.

- Un volume è una directory _al di fuori_ del Union File System del container.
    
- Un volume può essere aceduto, condiviso e riutilizzato da più container.
    
- Permette ai dati di sopravvivere al ciclo di vita dei container.
    

**Come usare i volumi:**

1. **Bind Mount (Montaggio da Host):**
    
    - L'opzione `-v host-src:container-dest` associa una directory specifica dell'host a una directory all'interno del container.
        
    - Esempio: `docker run -v ~/projects/www:/var/www/html ...`
        
    - I dati nella cartella `~/projects/www` dell'host sono ora accessibili (e modificabili) dal container.
        
2. **Volumi Condivisi (tra container):**
    
    - È possibile avere volumi condivisi tra container senza legarli a una cartella specifica dell'host.
        
    - Si crea un container "dati" e poi si usa l'opzione `--volumes-from container-name` per montare i volumi di quel container in altri container.
        

---

### Networking in Docker

Docker offre capacità avanzate di gestione della rete.

Quando installato, crea automaticamente tre reti:

- **`bridge` (Ponte):** La rete predefinita. Usa un'interfaccia virtuale `docker0` sull'host. Ai container vengono assegnati IP privati (es. 172.17.0.1/16). Possono comunicare tra loro tramite IP, ma per essere raggiunti dall'esterno necessitano di _port mapping_ (`-p`).
    
- **`host`:** Connette il container direttamente alla rete dell'host, condividendo lo stack di rete. Non c'è isolamento di rete (massime prestazioni, minima sicurezza).
    
- **`none`:** Rimuove la rete, isolando il container (utile per lavori batch senza accesso a Internet).
    

**Port Mapping (Port Forwarding):**

- Le opzioni `-p` e `-P` (in `docker run`) sono usate per gestire il port mapping.
    
- `-p 8080:80`: Mappa la porta 8080 dell'host sulla porta 80 del container.
    
- Queste opzioni sono gestite automaticamente configurando le regole NAT di `iptables` sull'host.
    

**Reti Definite dall'Utente (User-defined Networks):**

- È possibile creare reti personalizzate (es. `docker network create my-net`).
    
- **Vantaggio chiave:** I container connessi a una rete definita dall'utente possono comunicare tra loro usando il loro **nome logico** (il nome del container) come se fosse un nome DNS.
    
- Esempio: `docker run --network=my-net --name=container1 ...`
    
- Un altro container sulla stessa rete `my-net` può ora contattare il primo semplicemente pingando `container1`.
    

---

### Registry (Registro)

Un registry è un servizio per la gestione di un set di immagini di container.

- **Docker Hub:** Il registry pubblico predefinito.
    
- **Docker Registry:** Uno strumento per gestire un proprio registry privato (può essere eseguito come container).
    

**Operazioni Principali:**

- `docker pull image-name`: Scarica un'immagine dal registry alla cache locale dell'host.
    
- `docker push image-name`: Carica un'immagine dalla cache locale al registry.
    

#### Flusso di Lavoro con Docker Hub

1. **Login:** `docker login`
    
2. **Costruzione e Tagging:** `docker build -t aswroma3/myhello .`
    
    - (Oppure `docker build -t myhello .` seguito da `docker tag myhello aswroma3/myhello`)
        
    - Il "tag" `aswroma3/myhello` dice a Docker a quale utente/organizzazione (`aswroma3`) appartiene l'immagine.
        
3. **Salvataggio (Push):** `docker push aswroma3/myhello`
    
4. **Caricamento (Pull) e Esecuzione (su un altro host):** `docker run aswroma3/myhello`
    

---

### Raccomandazioni Generali

Per massimizzare efficienza, portabilità e facilità di gestione:

1. **Un solo processo per container:**
    
    - Mantenere un singolo processo (es. un web server, un database) per container ne facilita il riutilizzo e la gestione.
        
    - **Scalabilità Orizzontale:** I container "monolitici" (nel senso che fanno una sola cosa) possono essere replicati orizzontalmente per supportare aumenti di carico.
        
2. **Container "Effimeri" (Ephemeral):**
    
    - **Stateless:** I container dovrebbero essere progettati per essere "stateless" (senza stato) e temporanei.
        
    - Devono poter essere fermati, distrutti e sostituiti rapidamente con nuovi container senza perdita di dati (i dati persistenti devono stare nei _volumi_).
        
3. **Container Minimali:**
    
    - **Immagini di Base Piccole:** Scegliere l'immagine di base più leggera possibile (es. `alpine` invece di `ubuntu`) per ridurre le dimensioni e migliorare le prestazioni e la sicurezza (meno superficie d'attacco).
        
    - **Evitare Pacchetti Inutili.**
        
    - **Minimizzare il Numero di Layer:** Limitare il numero di istruzioni (soprattutto `RUN`) nel Dockerfile.
        

---

### Errore Comune

**Attenzione:** C'è un errore comune che prima o poi tutti commettono.

Dopo aver **modificato il codice sorgente** di un'applicazione (es. il file `.java`):

1. **Ricorda (sempre!)** di rieseguire il build dell'applicazione (es. `gradle build` per creare il nuovo `.jar`).
    
2. **Ricorda (sempre!)** di rieseguire il build dell'immagine Docker (`docker build ...`) per includere il nuovo file `.jar`.
    
3. Se necessario, riesegui il push (`docker push ...`) dell'immagine aggiornata sul registry.
    
4. Potrebbe anche essere necessario rimuovere la versione precedente dell'immagine dalla cache locale (`docker rmi ...`).