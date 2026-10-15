---
title: Software Architectures
aliases:
  - LASS — Software Architectures
tags:
  - lab-architetture-software-sicurezza
  - architettura-software
  - multi-tier
  - cloud
source: 2 - Software Architectures.pdf
---

# Software Architectures

> [!abstract]
> Dopo il *come si lavora* di [[01 - LASS - Software Development Process]], questa lezione affronta il **come si organizza un sistema software**: cos'è un'architettura, quali compromessi impone sugli attributi di qualità, cosa sono componenti, servizi e microservizi, come si dividono le funzionalità in **layer** e come i layer si distribuiscono su **tier** (1, 2, 3 o più livelli). Chiude con i **modelli di esecuzione** (stand-alone, ibrido, SaaS), il **cloud** (IaaS, PaaS, SaaS) e tre linee guida di progettazione.
>
> Il modello SaaS è ripreso e approfondito in [[04 - LASS - SaaS Essentials]]; l'architettura a 3 tier è quella delle app [[05 - LASS - Rails Parte 1|Rails]]. Collegamenti con [[Middleware]], [[Service-Oriented Architecture]] e [[Modello Client-Server]] di Sistemi di Calcolo 2.
>
> Indice dei concetti: [[MOC - Lab Architetture Software e Sicurezza]]. Materiale basato sulle slide dei proff. Massimo Mecella, John Yang e Ian Sommerville.

---

## Cos'è un'architettura software

Vedi [[Architettura Software]].

L'**architettura software** è l'**organizzazione complessiva** di un prodotto software:
- i **componenti software**;
- l'**organizzazione dei server**;
- le **tecnologie** usate.

L'architettura influenza gli **attributi di qualità non funzionali** del sistema, cioè le proprietà che non riguardano *cosa* fa il sistema ma *come* lo fa:

| Attributo | Domanda |
|---|---|
| responsiveness | quanto è rapido a rispondere? |
| reliability | si comporta come previsto? |
| availability | è disponibile quando serve? |
| security | resiste agli attacchi? |
| usability | è facile da usare? |
| maintainability | è facile da modificare? |
| resilience | continua a funzionare in caso di guasti? |

Due osservazioni importanti:
- **è impossibile ottimizzare tutti gli attributi non funzionali nello stesso sistema**: migliorarne uno spesso ne peggiora un altro;
- l'architettura influenza la **complessità** del prodotto.

![[LASS-L02-p02.png]]

La stella mostra le **influenze architetturali** (*architectural influences*), cioè i fattori che orientano le scelte di architettura: le **caratteristiche non funzionali** del prodotto, la **durata prevista** del prodotto (*product lifetime*: un software che deve durare anni va reso manutenibile), il **riuso del software** (si possono riusare componenti esistenti?), il **numero di utenti** (determina le esigenze di scalabilità) e la **compatibilità** con altro software.

### Trade-off

Esempi di compromessi:

- **maintainability vs performance**: per essere manutenibile un sistema va diviso in **molte parti autonome**, facili da sostituire o migliorare; ma i componenti **impiegano tempo a comunicare** tra loro, e le prestazioni calano;
- **security vs usability**: **più livelli di sicurezza** significano un'interazione **più lenta e/o complicata** per l'utente (pensa all'autenticazione a due fattori);
- **availability vs time to market e costi**: l'alta disponibilità richiede **ridondanza**, che costa e aumenta la complessità.

Una volta chiariti i compromessi, l'architetto deve rispondere a tre domande:
- **come organizzare il sistema?**
- **come sono distribuiti i componenti e come comunicano?**
- **quali tecnologie si usano?**

## Esempi di architetture

![[LASS-L02-p04-1.png]]

Prima architettura: un'unica **user interface** comunica con due componenti **C1** e **C2**, che condividono un **database comune** (*shared database*). È semplice e i dati sono sempre consistenti, ma i due componenti sono accoppiati tramite il database: una modifica allo schema li tocca entrambi.

![[LASS-L02-p04-2.png]]

Seconda architettura: ogni componente ha il **proprio database** (C1 database, C2 database), e un terzo componente **C3** si occupa della **riconciliazione dei database** (*database reconciliation*), cioè di mantenerli coerenti. I componenti sono più indipendenti, ma ora serve un meccanismo esplicito di sincronizzazione.

## Componenti, servizi e microservizi

Vedi [[Componenti, Servizi e Microservizi]].

- Un **componente** è un elemento che implementa un **insieme coerente di funzionalità**: offre uno o più **servizi** che possono essere usati da altri componenti.
- Un **servizio** è un **frammento coerente di funzionalità**. Può andare da un servizio su larga scala (es. un database) a un **microservizio**, che svolge **un unico compito molto specifico**.
- I servizi possono essere acceduti **direttamente** oppure tramite l'**API del componente**.

![[LASS-L02-p05.png]]

A sinistra, il *Component 1* espone i servizi S1, S2, S3 che vengono **acceduti direttamente** da altri componenti. A destra, il *Component 2* nasconde i servizi S4, S5, S6 dietro un'**API**: chi lo usa passa sempre dall'interfaccia. Il secondo modo è più robusto: si possono cambiare i servizi interni senza toccare chi li usa, finché l'API resta la stessa.

![[LASS-L02-p06.png]]

Esempio concreto di decomposizione in componenti (dal libro di Sommerville, un sistema di gestione documentale), organizzato in fasce:
- **web browser**: interazione utente, validazione locale dell'input, stampa locale;
- **user interface management**: autenticazione e autorizzazione, gestore di form e query, generazione delle pagine web;
- **information retrieval**: ricerca, recupero documenti, gestione dei diritti, pagamenti, contabilità;
- **document index**: gestione, interrogazione e creazione degli indici;
- **basic services**: query al database, validazione delle query, logging, gestione degli account utente;
- **databases**: DB1…DB5.

Ogni riquadro è un componente con una responsabilità precisa; le fasce anticipano l'idea di *layer* della prossima sezione.

### Perché decomporre in componenti

I componenti possono essere:
- **sviluppati in parallelo** da team diversi;
- **riusati** in altri sistemi;
- **sostituiti** con implementazioni migliori;
- **distribuiti** su macchine diverse.

## Layers

Vedi [[Layer e Tier]].

I **layer** (livelli) sono **raggruppamenti logici di componenti**. Molti prodotti software hanno una struttura a livelli comune:

- **Presentation**: gestisce le **interazioni** con il sistema (interfaccia utente);
- **Application** (logica applicativa): **cosa fa** il sistema;
- **Resource management**: si occupa dell'**organizzazione dei dati** (database, file).

Un **tier** è il **modulo software che implementa un layer**, tipicamente in esecuzione su una macchina o un processo distinto. La differenza conta: il *layer* è una divisione logica, il *tier* è una divisione fisica di deployment.

![[LASS-L02-p08.png]]

Il diagramma mostra il **client** che parla con un *information system* (riquadro tratteggiato) composto dai tre layer impilati: **presentation layer**, **application logic layer**, **resource management layer**. Ogni layer comunica solo con quello adiacente.

## Architetture 1-tier, 2-tier e 3-tier

Vedi [[Architettura Multi-Tier]].

### 1-tier

![[LASS-L02-p09.png]]

Nell'architettura **1-tier** i tre layer sono **tutti nello stesso tier**, su un'unica macchina (il riquadro dell'information system li contiene tutti; il client è solo un terminale). È il modello dei vecchi mainframe.

| Svantaggi | Vantaggi |
|---|---|
| bassa portabilità | nessun costo di comunicazione tra tier |
| bassa manutenibilità | gestione delle risorse più semplice |
| più difficile da aggiornare | i layer si possono fondere → prestazioni migliori |

### 2-tier

![[LASS-L02-p10.png]]

Nell'architettura **2-tier** il **presentation layer passa sul client**, mentre logica applicativa e gestione delle risorse restano sul **server**.

- I **client sono indipendenti** tra loro: possono esistere **più presentation layer** diversi a seconda di cosa ogni client vuole fare (un'app desktop, una mobile…).
- Il **server risparmia risorse**, perché non deve generare l'interfaccia.
- Nasce il concetto di **API** (*Application Program Interface*): un'interfaccia per invocare il sistema dall'esterno, che **abilita le integrazioni** con altri sistemi.

### 3-tier

![[LASS-L02-p11.png]]

Nell'architettura **3-tier** ogni layer è in un tier separato: il presentation layer sul client, la logica applicativa (supportata da un **middleware**) su un tier, la gestione delle risorse su un altro.

- Abilita la **scalabilità**: si possono aggiungere **più server**.
- Il **middleware** fornisce astrazioni e infrastrutture che supportano il layer applicativo (vedi [[Middleware]]).
- **Pro**: più manutenibile, più facile da aggiornare, più scalabile, distribuibile su server diversi.
- **Contro**: **costi di comunicazione tra i tier**.

### Scalabilità del 3-tier

![[LASS-L02-p12.png]]

Esempio realistico di 3-tier scalabile, da sinistra a destra:
- **presentation tier**: le richieste passano da un **load balancer** che le distribuisce su più **web server**, più un *asset server* per i contenuti statici (immagini, CSS);
- **logic (application) tier**: un altro load balancer distribuisce il lavoro su più **app server**;
- **persistence tier**: un **database master** e più **slave** (repliche, usate tipicamente in lettura), con un altro load balancer davanti.

Ogni tier scala **in modo indipendente**: se il collo di bottiglia è la logica, si aggiungono app server senza toccare il resto.

## Architetture distribuite: multi-tier e service-oriented

![[LASS-L02-p13-1.png]]

**Multi-tier**: i client parlano con un **web server**, che chiama un **application server**, che usa un **database server**. È la generalizzazione del 3-tier.

![[LASS-L02-p13-2.png]]

**Service-oriented**: i client parlano con un web server, che passa per un **service gateway** che smista le richieste su molti **servizi** indipendenti (s1…s6). Vedi [[Service-Oriented Architecture]].

La scelta tra le due dipende da:
- **tipo di dati e aggiornamenti dei dati**;
- **frequenza dei cambiamenti**;
- **piattaforma di esecuzione** del sistema.

Nell'architettura a servizi, i **servizi sono componenti stateless** (senza stato): ogni richiesta contiene tutto ciò che serve, quindi è **più facile scalare** (si avviano più copie dello stesso servizio) e **aggiornare** (si sostituisce un servizio senza fermare gli altri).

## Modelli di esecuzione del software

Vedi [[Modelli di Esecuzione del Software]].

![[LASS-L02-p14.png]]

Tre modi di eseguire un software:
- **stand-alone execution**: sul computer dell'utente ci sono interfaccia, funzionalità e dati; i server del produttore forniscono solo gli **aggiornamenti** (es. un'app desktop tradizionale);
- **hybrid execution**: sul computer dell'utente c'è l'interfaccia, una **parte** delle funzionalità e i dati; il resto delle funzionalità, i backup e gli aggiornamenti stanno sui server del produttore;
- **software as a service**: sul computer dell'utente c'è solo l'**interfaccia** (browser o app); **funzionalità e dati sono sui server del produttore**.

## Vantaggi del SaaS

Vedi [[Software as a Service]].

1. **Nessuna installazione locale**: niente requisiti di compatibilità hardware.
2. I **dati restano nel servizio**: il cliente non si preoccupa di backup e perdite di dati.
3. È più facile per gruppi di utenti **collaborare sugli stessi dati**.
4. Va bene per dati **grandi e aggiornati spesso**, acceduti da remoto.
5. Gli sviluppatori mantengono **un'unica copia** del software server (invece di una per sistema operativo).
6. Gli **aggiornamenti** non interferiscono con l'esperienza utente.

La slide chiede: **svantaggi?** Alcuni possibili:
- serve una **connessione** a Internet (senza rete il servizio non funziona);
- i dati sono **in mano al fornitore** (privacy, *lock-in*, cosa succede se il fornitore chiude);
- **latenza** maggiore rispetto a un'app locale;
- il server è un **bersaglio** di attacchi che riguarda tutti gli utenti insieme (tema delle lezioni [[13 - LASS - Introduzione alla Sicurezza|13]]–[[17 - LASS - Sicurezza delle Web Application|17]]).

## Cloud

Vedi [[Cloud Computing IaaS PaaS SaaS]].

- Il **cloud** è un grande numero di **server remoti offerti in affitto**.
- I server remoti sono **virtuali**: implementati in software anziché in hardware (macchine virtuali, container).
- Caratteristiche del software in cloud: **scalabilità**, **elasticità** (si aggiungono o tolgono risorse in base al carico) e **resilienza**.

Tre livelli di servizio:
- **Infrastructure as a Service (IaaS)**;
- **Platform as a Service (PaaS)**;
- **Software as a Service (SaaS)**.

![[LASS-L02-p17-1.png]]

La pila del cloud, dal basso: il **cloud data center** fisico; sopra, l'**IaaS** (calcolo, virtualizzazione, storage, rete); sopra ancora, il **PaaS** (database, ambienti di sviluppo software, gestione e monitoraggio del cloud); in cima, il **SaaS**, cioè l'applicazione pronta per l'utente finale.

![[LASS-L02-p17-2.png]]

Il secondo schema confronta **chi gestisce cosa**:
- in **IaaS** il *cloud vendor* gestisce solo i servizi computazionali di base; il **fornitore del software** gestisce la gestione cloud, i servizi applicativi (database ecc.) e il software;
- in **PaaS** il cloud vendor gestisce anche la gestione cloud e i servizi applicativi; il fornitore del software si occupa solo del proprio software.

Più si sale, meno il cliente deve gestire. Esempi tipici: IaaS = Amazon EC2; PaaS = Heroku (molto usato per Rails); SaaS = Gmail. Il tema è approfondito in [[1 - Cloud Computing, Virtualizzazione e Containerization]] (Lab Advanced Programming).

## Linee guida per la progettazione architetturale

Vedi [[Linee Guida di Progettazione Architetturale]].

![[LASS-L02-p18.png]]

Tre linee guida, ai vertici di un triangolo:
- **Separation of concerns** (separazione delle responsabilità): organizzare l'architettura in componenti che si concentrano su **un solo aspetto** (un componente per l'autenticazione, uno per i pagamenti…);
- **Stable interfaces** (interfacce stabili): progettare interfacce dei componenti **coerenti e che cambiano lentamente**, così chi le usa non deve essere riscritto spesso;
- **Implement once** (implementa una volta sola): **evitare di duplicare funzionalità** in punti diversi dell'architettura. È il principio [[Don't Repeat Yourself|DRY]] che Rails mette al centro (vedi [[05 - LASS - Rails Parte 1#La filosofia di Rails|lezione 5]]).
