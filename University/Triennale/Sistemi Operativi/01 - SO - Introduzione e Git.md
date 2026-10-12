---
title: Introduzione ai Sistemi Operativi e Git
aliases:
  - SO — Introduzione
  - Sistemi Operativi — Lezione 1
tags:
  - sistemi-operativi
  - kernel
  - architettura
  - git
source: lezione1_history_git.docx
---

# Introduzione ai Sistemi Operativi e Git

> [!abstract] Scopo della lezione
> La lezione definisce cos'è un **sistema operativo (OS)**, quali risorse gestisce e quali servizi offre, come si organizza un sistema di calcolo **a strati** e come sono strutturati i kernel moderni (**monolitico** vs **microkernel**). In coda ci sono i riferimenti per **Git**, lo strumento di versionamento usato durante il corso.
> Mappa dei concetti: [[MOC - Sistemi Operativi]]

## Che cos'è un sistema operativo

Un [[Sistema Operativo]] è il software che **controlla l'esecuzione degli altri programmi** e fornisce loro un'**astrazione dell'hardware sottostante**. Invece di dover sapere come si pilota un particolare disco, una particolare scheda di rete o un particolare controller di memoria, un programma chiede all'OS di "leggere un file" o "allocare memoria", e l'OS traduce queste richieste in operazioni concrete sull'hardware.

Due compiti sono centrali:

- **Gestire le risorse**: più programmi vogliono usare CPU, memoria e dispositivi nello stesso momento. L'OS fa da arbitro e **previene i conflitti** (due programmi che scrivono contemporaneamente sullo stesso dispositivo, un programma che sovrascrive la memoria di un altro…).
- **Gestire gli errori** dei programmi o dell'hardware: un programma che accede a memoria non sua non deve far crollare l'intero sistema; l'OS lo intercetta e reagisce (ad esempio terminando solo quel programma).

Dal **punto di vista dell'utente** un buon sistema operativo:

- gestisce **efficientemente** le risorse (non spreca CPU, memoria, energia);
- rende **facile** accedere alle risorse (astrazioni comode come file, processi, socket);
- esegue **correttamente** i programmi (isolamento, protezione, gestione degli errori).

## Organizzazione a strati

Un sistema computazionale è generalmente organizzato **a strati** ([[Architettura a Strati]]). Ogni livello offre un'**astrazione** al livello superiore attraverso un'**API** (Application Programming Interface) e usa solo i servizi del livello inferiore. Questo permette di cambiare l'implementazione di uno strato senza toccare quelli sopra, purché l'interfaccia resti la stessa.

Gli strati sono:

![[SO-L01-01.png]]

Dal basso verso l'alto:

| Strato | Ruolo |
| --- | --- |
| **Hardware** | Gli apparati fisici su cui gira il software (CPU, memoria, dispositivi). |
| **Kernel** | Il software che parla direttamente con l'hardware: gestisce CPU, memoria e driver dei dispositivi. Interagisce con l'hardware tramite **interrupt** e **DMA**, con il software tramite **trap** (vedi [[Interrupt]], [[DMA]], [[System Call]]). Impone l'astrazione dell'hardware (Linux su x86, ARM, ecc.). |
| **System standard** (POSIX, Win32) | Garantisce la compatibilità tra kernel diversi: un programma scritto per POSIX funziona su qualunque kernel che implementi POSIX. |
| **libc** (language standard) | Garantisce che un programma scritto usando solo la libreria standard del linguaggio funzioni su più sistemi. |
| **User programs** | Le applicazioni. |

- **POSIX** è lo standard di sistema per i sistemi **Unix** (Linux, macOS, BSD…).
- **Win32** è lo standard di sistema per i sistemi **Windows**.

Conseguenza pratica: un programma sviluppato su un kernel può girare su un kernel diverso **se entrambi rispettano lo stesso system standard**. Ad esempio un programma scritto per una vecchia versione di Windows gira su un Windows più recente perché entrambi implementano Win32, anche se il kernel sottostante è cambiato molto. Il tema viene ripreso nel dettaglio in [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Standard di linguaggio e standard di sistema|lezione 6]].

## Organizzazione di un computer

![[SO-L01-02.png]]

A sinistra c'è l'architettura "classica" di una scheda madre PC: la **CPU** è collegata tramite il *front-side bus* al **Northbridge** (memory controller hub), che gestisce i componenti veloci: **memoria** e scheda grafica (AGP/PCI Express). Il Northbridge è collegato al **Southbridge** (I/O controller hub), che gestisce le periferiche più lente: dischi (IDE/SATA), USB, Ethernet, audio, slot PCI, e tramite il bus LPC il chip **Super I/O** (seriale, parallela, tastiera, mouse) e la **Flash ROM** con il BIOS.

A destra la stessa cosa in forma astratta: CPU, controller dei dischi, controller USB e adattatore grafico condividono un **bus** comune verso la **memoria**. Ogni dispositivo ha un **controller** che la CPU programma; il kernel, tramite i driver, parla con questi controller. Il funzionamento elettrico dei bus è approfondito in [[04 - SO - Hardware e AVR|lezione 4]] ([[Bus di Sistema]]).

## Servizi offerti da un OS

- **Esegue programmi**: carica il codice in memoria e lo fa partire (vedi [[Program File e Processo]]).
- **Accesso protetto a risorse condivise** (I/O e memoria): un programma non può usare liberamente risorse altrui (vedi [[Dual Mode]]).
- **Gestisce gli errori**, come il *segmentation fault* (accesso a memoria non valida): l'hardware solleva un'eccezione e l'OS decide cosa fare (vedi [[Eccezioni]]).
- **Raccoglie statistiche sull'uso delle risorse**: servono a decidere quali **politiche** adottare (ad esempio quale algoritmo di scheduling è più adatto al carico osservato, vedi [[09 - SO - CPU Scheduling|lezione 9]]).
- Tipicamente un OS è **impacchettato con strumenti applicativi** (editor, compilatori, debugger, interpreti di comandi come la shell…). Questi **non fanno parte del kernel**, ma fanno parte dell'**ecosistema** dell'OS.

## Risorse da gestire

| Risorsa | Obiettivi | Tecniche |
| --- | --- | --- |
| **CPU** | servire il massimo numero di utenti/processi con una singola CPU | scheduling, multitasking ([[CPU Scheduler e Dispatcher]]) |
| **Memoria** | protezione, ridurre il tempo di accesso, virtualizzazione | paginazione/segmentazione ([[Paging]], [[Segmentazione]], [[Memoria Virtuale]]) |
| **I/O** | semplificare l'uso, minimizzare il tempo di accesso, massimizzare il **throughput** | buffering, I/O scheduling |

### Multicore e Symmetric Multiprocessing

Oggi la frequenza di clock delle CPU **non può più crescere** in modo significativo: non si riesce a rimpicciolire ulteriormente i componenti e il calore/consumo diventerebbe ingestibile. Per aumentare le prestazioni si mettono **più CPU (core) in un singolo chip**. I core però **condividono lo stesso bus verso la memoria**, che può diventare un **collo di bottiglia**.

![[SO-L01-03.png]]

Ogni core ha i propri **registri** e la propria **cache**, ma la **memoria** principale è comune.

**[[Symmetric Multiprocessing]] (SMP)**: ci sono più CPU **identiche**, il carico è distribuito tra di esse e ognuna può eseguire sia codice utente che codice kernel. Il kernel può essere:

- **preemptive**: un processo (anche in kernel mode) può essere interrotto per far girare un altro;
- **non preemptive**: un processo viene tolto dalla CPU solo quando la rilascia volontariamente.

La distinzione tornerà parlando di scheduling ([[09 - SO - CPU Scheduling#Scheduling multiprocessore|scheduling multiprocessore]]).

## Componenti di un OS moderno

Un OS moderno è composto da diversi **manager**:

- **Process manager**: creazione, terminazione e scheduling dei processi ([[Process Control Block]], [[CPU Scheduler e Dispatcher]]).
- **Memory manager**: allocazione e protezione della memoria ([[Paging]], [[Memoria Virtuale]]).
- **I/O manager**: driver e dispositivi ([[Driver e Block Device]]).
- **File manager**: il file system ([[File System]]).
- **Network manager**: stack di rete.
- **Login manager**: autenticazione degli utenti.
- **Command manager**: interprete dei comandi (shell).

E offre i servizi:

- esecuzione dei programmi;
- astrazioni di I/O (file, socket, dispositivi come file);
- accesso al file system;
- inter-comunicazione e sincronizzazione tra processi (IPC);
- gestione delle risorse (RAM, CPU, disco, dispositivi);
- primitive per rafforzare la **protezione**;
- gestione delle **eccezioni**;
- raccolta di statistiche sull'uso di programmi e risorse.

## Strutture moderne di kernel

![[SO-L01-04.png]]

Esistono due grandi famiglie ([[Kernel Monolitico e Microkernel]]):

- **Kernel monolitico**: il kernel è **un unico grande programma** che gestisce tutte le interazioni tra hardware e programmi. File system, comunicazione tra processi, gestione dell'I/O, memoria virtuale e gestione dei processi girano tutti in **modo kernel**, nello stesso spazio di indirizzi. *Pro*: le parti si chiamano tra loro con semplici chiamate a funzione, quindi è veloce. *Contro*: un bug in un driver può far crollare tutto il sistema. Esempio: Linux.
- **Microkernel**: il kernel è composto da un **nucleo leggero** che gestisce solo memoria e processi (più il meccanismo di comunicazione), mentre tutto il resto (I/O server, file server, process server, memoria virtuale) gira come insieme di **moduli in modo meno privilegiato** (modo utente). *Pro*: più robusto e modulare, un server che crasha può essere riavviato. *Contro*: le componenti comunicano tramite messaggi, quindi c'è più overhead. Esempi: Minix, QNX.

La distinzione tra **modo user** e **modo kernel** che appare nella figura è il meccanismo hardware di [[Dual Mode]], spiegato in dettaglio in [[06 - SO - Interrupt, Syscall, Dual Mode e Processi|lezione 6]].

## Git

Durante il corso il codice viene distribuito e versionato con [[Git]], un sistema di controllo di versione distribuito. Riferimenti utili:

- Git tutorial: <http://schacon.github.com/git/gittutorial.html>
- Pro Git book: <http://git-scm.com/book>
- Git for computer scientists: <http://eagain.net/articles/git-for-computer-scientists/>

> [!tip] Comandi essenziali
> - `git clone <url>`: copia un repository remoto in locale.
> - `git status` / `git diff`: vedere cosa è cambiato.
> - `git add <file>` e `git commit -m "msg"`: registrare una nuova versione.
> - `git pull` / `git push`: sincronizzarsi con il repository remoto.
> - `git log`: storia dei commit.
>
> L'idea di fondo (spiegata in *Git for computer scientists*) è che la storia è un **grafo aciclico di commit**: ogni commit è uno snapshot dell'intero progetto che punta al commit padre, e i branch sono semplici puntatori a commit.
