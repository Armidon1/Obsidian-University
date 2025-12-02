## Docker

**Docker** ([www.docker.com](https://www.docker.com)) è la piattaforma di [[Container]] più popolare, progettata per **costruire, rilasciare ed eseguire applicazioni distribuite** in modo semplice, veloce, scalabile e portabile.
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