# Containerization

## Virtualizzazione basata su [[Container]]

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

Vedi anche [[Docker]]