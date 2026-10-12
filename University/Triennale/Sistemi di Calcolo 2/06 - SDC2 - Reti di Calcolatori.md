---
title: Reti di Calcolatori
aliases:
  - SDC2 — Reti di calcolatori
  - Sistemi di Calcolo 2 — Lezione 6
tags:
  - sistemi-di-calcolo-2
  - reti
  - tcp-ip
  - osi
  - indirizzamento
source: Appunti Filippo/6-reti_di_calcolatori.pdf
---

# Reti di calcolatori

> [!abstract] Scopo della lezione
> Finora i processi comunicavano sulla stessa macchina. Per farli comunicare tra macchine diverse serve una **rete**. La lezione introduce i modelli **client-server** e **peer-to-peer**, la classificazione delle reti per estensione (PAN, LAN, MAN, WAN, Internet), l'architettura di Internet (ISP, backbone, colli di bottiglia, CDN), il principio dell'**architettura a livelli** e dei **protocolli**, il modello **OSI** e lo stack **TCP/IP**, con **IP** (indirizzi e classi, header), **ARP**, **TCP**, **UDP** e **DNS**. È la base per i **socket** della [[07 - SDC2 - Socket|lezione 7]].
> Mappa dei concetti: [[MOC - Sistemi di Calcolo 2]]

## Modelli di comunicazione

![[SDC2-L06-001-000.png]]

Più **client** (i computer degli utenti) sono collegati attraverso una **rete** a un **server** (la macchina che offre il servizio).

Vedi [[Modello Client-Server]].

Il **modello client-server** si basa su **richieste e risposte**:

![[SDC2-L06-001-001.png]]

Il processo client, sulla macchina client, invia una **richiesta** attraverso la rete al processo server, sulla macchina server, che risponde con una **risposta** (*reply*). Il server è sempre attivo e in attesa; il client inizia la comunicazione.

In un sistema **peer-to-peer** invece **non ci sono client e server fissi**: ogni nodo può fare da entrambi.

![[SDC2-L06-001-002.png]]

Ogni computer comunica direttamente con altri (es. BitTorrent, la condivisione di file tra pari).

## Classificazione per dimensione

![[SDC2-L06-001-003.png]]

| Distanza tra processori | Processori nello stesso… | Tipo di rete |
| --- | --- | --- |
| 1 m | metro quadro | **Personal Area Network** (PAN) |
| 10 m – 1 km | stanza, edificio, campus | **Local Area Network** (LAN) |
| 10 km | città | **Metropolitan Area Network** (MAN) |
| 100 – 1000 km | nazione, continente | **Wide Area Network** (WAN) |
| 10 000 km | pianeta | **Internet** |

**Personal Area Network**:

![[SDC2-L06-002-004.png]]

Un computer collegato senza fili (es. Bluetooth) a mouse, tastiera, stampante, cuffie e smartwatch.

**Local Area Network (LAN)**: può essere **wireless** (802.11, il Wi-Fi) o **cablata** (Switched Ethernet).

![[SDC2-L06-002-005.png]]

A sinistra i portatili si collegano via radio a un **access point**, connesso alla rete cablata. A destra i computer sono collegati con i cavi alle **porte** di uno **switch Ethernet**, collegato al resto della rete.

Reti wireless:

![[SDC2-L06-002-006.png]]

*Multipath fading*: il segnale del trasmettitore arriva al ricevitore per **più percorsi** (uno diretto, altri riflessi da ostacoli) con ritardi diversi, e le copie possono sommarsi o annullarsi.

![[SDC2-L06-002-007.png]]

Il **raggio d'azione** di una singola radio può non coprire l'intero sistema: A e C sono entrambi nel raggio di B, ma non si "sentono" tra loro (è il problema del *terminale nascosto*). Il limite principale del wireless è proprio la portata.

**Metropolitan Area Network**:

![[SDC2-L06-002-008.png]]

Una MAN basata sulla TV via cavo: un **head end** riceve i segnali (antenna e Internet) e li distribuisce lungo i cavi, tramite delle *junction box*, alle case della città.

**Wide Area Network (WAN)**:

![[SDC2-L06-003-009.png]]

Una WAN che collega uffici a Perth, Melbourne e Brisbane: i computer di ogni sede sono collegati a un **router**, e i router sono collegati da **linee di trasmissione** che formano la **sottorete** (*subnet*).

![[SDC2-L06-003-010.png]]

![[SDC2-L06-003-011.png]]

A sinistra, una WAN che usa la rete di un **ISP**: le linee di trasmissione sono dell'ISP, non dell'azienda. A destra, una WAN che usa una **VPN** (*Virtual Private Network*): le sedi sono collegate da collegamenti virtuali **attraverso Internet**.

## L'architettura di Internet

Gli **Internet Service Provider (ISP)** forniscono l'accesso a Internet (TIM, Fastweb, …).

![[SDC2-L06-003-012.png]]

La rete IP dell'ISP è fatta di **POP** (*Point of Presence*, i punti di accesso con i router), collegati alla "grande Internet". Gli utenti si collegano ai POP tramite l'accesso in **xDSL** (doppino telefonico) o in **fibra**.

![[SDC2-L06-003-013.png]]

Una rete geografica per la trasmissione dati vista a cerchi concentrici: al centro la **backbone** (nodi del sottosistema di comunicazione), intorno l'**area di accesso** (unità di accesso) e all'esterno l'**area di utente** (terminali, reti locali).

![[SDC2-L06-004-014.png]]

La mappa della backbone globale di un operatore (PCCW): le dorsali che collegano i principali nodi del mondo e portano Internet nelle città.

![[SDC2-L06-004-015.png]]

La backbone italiana della rete della ricerca **GARR**, con i suoi PoP e le fibre ottiche, collegata a GÉANT (la rete della ricerca europea).

Anche **Google** ha costruito una propria backbone, anzi due grandi reti: una che collega gli utenti ai servizi Google (Search, Gmail, YouTube…) e una interna che collega i data center tra loro. Google controlla lo scheduling del traffico interno (che è *bursty*, a raffiche), ma deve affrontare problemi di **traffic engineering**: spesso deve spostare **petabyte** di dati (gli indici del web, milioni di copie di backup delle caselle Gmail) da un posto all'altro.

![[SDC2-L06-005-016.png]]

L'architettura di Internet: gli utenti accedono ai **POP** del proprio ISP con fibra (FTTH), dialup, DSL (tramite **DSLAM**), cavo (tramite **CMTS**) o rete mobile 3G. Gli ISP locali sono collegati agli ISP più grandi; al vertice ci sono gli **ISP di Tier 1**, che formano la **backbone**. Gli ISP si scambiano traffico nei punti di **peering** (gli **IXP**, *Internet eXchange Point*). I data center sono collegati direttamente alla backbone. Il percorso evidenziato è il *data path* di un pacchetto.

### Reti mobili

![[SDC2-L06-005-018.png]]

Il **design cellulare** delle reti di telefonia mobile: il territorio è diviso in **celle** esagonali, ognuna servita da una **base station**. Celle non adiacenti possono riusare le stesse frequenze.

![[SDC2-L06-005-019.png]]

L'architettura della rete **UMTS 3G**: i telefoni si collegano via radio (*air interface*) alle antenne (**Node B**), controllate dagli **RNC** (Radio Network Controller): è la **Radio Access Network**. La **Core Network** ha una parte a **circuito** per la voce (MSC/MGW verso la rete telefonica PSTN) e una a **pacchetto** per i dati (SGSN/GGSN verso Internet), con il database degli abbonati **HSS**.

![[SDC2-L06-006-020.png]]

**Handover**: un utente in movimento passa dalla cella di una base station a quella vicina senza interrompere la comunicazione.

### Reti di RFID e sensori

![[SDC2-L06-006-021.png]]

L'**RFID** permette di mettere in rete oggetti di tutti i giorni: un lettore RFID legge i tag applicati a un animale, a un documento, a un libro.

![[SDC2-L06-006-022.png]]

Una **rete di sensori** con topologia **multihop**: i nodi sensore inoltrano i dati di nodo in nodo (*wireless hop*) fino a un punto di raccolta. Sono la base dell'**Internet of Things** ([[09 - SDC2 - Internet of Things|lezione 9]]).

### Architettura a 3 livelli e colli di bottiglia

![[SDC2-L06-006-023.png]]

![[SDC2-L06-006-025.png]]

Internet vista in tre zone: la **first mile** (dove si collegano i fornitori di contenuti, a sinistra), la **backbone** (la rete degli ISP o NSP, *Network Service Provider*, collegati tramite punti di accesso neutrali) e la **last mile** (dove si collegano gli utenti, a destra). Tutte e tre sono **potenziali colli di bottiglia**.

Come eliminarli:

- **first e last mile** (soluzione hardware): aumentare la **banda** del collegamento al provider;
- **backbone**: dipende dal miglioramento delle infrastrutture dei singoli ISP, che gli utenti finali non controllano. La soluzione è **software**:
  - **Content Delivery Network (CDN)**: si mettono **copie dei contenuti** (caching delle pagine) **vicino agli utenti**, in modo trasparente (es. **Akamai**). L'utente accede alla copia vicina con banda larga, senza attraversare la backbone.

È la stessa idea della **gerarchia di cache** dei processori (vedi [[Gerarchia di Memoria]]).

![[SDC2-L06-007-026.png]]

La piattaforma di Akamai: oltre 100 000 server in 72 paesi, 1 500 località e 1 000 reti; trasporta il **15–30% del traffico web mondiale**, oltre un trilione di richieste e 30 petabyte al giorno. I servizi sono distribuiti su moltissimi server, e le richieste dei client vanno verso il server più vicino.

## Architettura a livelli e protocolli

Vedi [[Architettura a Livelli dei Protocolli]].

Far comunicare due computer pone molti problemi (codifica dei bit, errori, instradamento, affidabilità, formato dei dati…). Si usa quindi un'**architettura gerarchica a livelli**: ogni livello risolve un problema e offre un servizio a quello superiore.

**Esempio: filosofo, traduttore, segretaria.**

![[SDC2-L06-007-027.png]]

Due filosofi in luoghi diversi vogliono comunicare ma parlano lingue diverse. Il filosofo A (livello 3) scrive "I like rabbits" e lo passa al suo **traduttore** (livello 2), che lo traduce in una lingua concordata con l'altro traduttore (olandese: "Ik vind konijnen leuk") e aggiunge l'informazione "L: Dutch". La **segretaria** (livello 1) aggiunge l'informazione per l'altra segretaria (un numero di fax) e lo trasmette. Dall'altra parte il messaggio risale: la segretaria lo passa al traduttore, che lo traduce in francese per il filosofo B ("J'aime bien les lapins").

Ogni livello comunica "logicamente" con il livello **corrispondente** dall'altra parte (i traduttori si accordano sulla lingua, le segretarie sul mezzo), ma fisicamente passa il messaggio al livello **sotto**. Ogni livello può cambiare (es. la segretaria usa l'email invece del fax) senza che gli altri se ne accorgano.

### Gerarchie di protocolli

![[SDC2-L06-008-028.png]]

Due host con 5 livelli. Il livello n di un host parla con il livello n dell'altro secondo il **protocollo di livello n** (frecce tratteggiate: comunicazione virtuale). Tra livelli adiacenti dello stesso host c'è un'**interfaccia**. Solo il livello 1 comunica davvero, attraverso il **mezzo fisico**.

- **Protocollo**: l'insieme di regole (formato e ordine dei messaggi, azioni da compiere) con cui comunicano due entità **pari** (dello stesso livello) su macchine diverse.
- **Interfaccia**: le operazioni e i servizi che un livello offre a quello superiore sulla stessa macchina.

![[SDC2-L06-008-029.png]]

**Incapsulamento**: il messaggio M nasce al livello 5. Il livello 4 aggiunge un header H4. Il livello 3 lo divide in due pezzi (M1 e M2) se è troppo grande, e a ognuno aggiunge H3. Il livello 2 aggiunge un header H2 e un trailer T2 (es. un checksum). Sulla macchina di destinazione ogni livello toglie il proprio header e passa il resto in su, fino a ricostruire M.

### Il modello OSI

Vedi [[Modello OSI e TCP-IP]].

Il modello **OSI** (*Open Systems Interconnection*, ISO) è un'architettura a **7 livelli**. Principi:

- un livello per ogni **astrazione** diversa;
- ogni livello svolge una **funzione ben definita**;
- le funzioni sono scelte pensando a **protocolli standard internazionali**;
- i confini tra livelli minimizzano il **flusso di informazioni** tra le interfacce;
- il numero di livelli è **ottimale**: abbastanza da separare funzioni diverse, non troppi da rendere l'architettura ingestibile.

![[SDC2-L06-009-030.png]]

Due profili di protocolli per il piano utente:

- **commutazione di pacchetto**: i nodi di rete intermedi implementano i livelli **fisico, collegamento e rete**, perché devono decidere dove instradare ogni pacchetto; i livelli superiori sono solo nei terminali (*end-to-end*);
- **commutazione di circuito**: i nodi intermedi implementano solo il livello **fisico**, perché il circuito è già stabilito.

| Livello | Funzione |
| --- | --- |
| 7. **Applicazione** | i protocolli usati dalle applicazioni (HTTP, SMTP, FTP…) |
| 6. **Presentazione** | rappresentazione dei dati (codifica, compressione, cifratura) |
| 5. **Sessione** | gestione del dialogo tra applicazioni (apertura, sincronizzazione, chiusura) |
| 4. **Trasporto** | comunicazione **tra processi** end-to-end, affidabile o no: **TCP** e **UDP** |
| 3. **Rete** | identifica la macchina di destinazione e **instrada** il messaggio attraverso i nodi intermedi, scegliendo il nodo successivo (routing) |
| 2. **Collegamento** | divide il messaggio in **frame**, li mette in sequenza e li invia sul singolo collegamento; il nodo ricevente li ricompone e li riscompone per il collegamento successivo; rileva gli errori |
| 1. **Fisico** | trasforma i bit in un **segnale fisico** reale (onda elettromagnetica, impulso ottico…) |

> [!warning] Correzione
> Gli appunti lasciano vuote le descrizioni dei livelli applicazione, presentazione, sessione e trasporto: le ho completate con le definizioni standard del modello OSI.

Problemi del modello OSI (secondo Tanenbaum):

- **bad timing**: arrivò quando TCP/IP era già diffuso, ed è stato fatto in fretta;
- **bad technology**: alcuni livelli (sessione, presentazione) sono quasi vuoti, altri (rete, collegamento) troppo pieni;
- **bad implementations**: le prime implementazioni erano lente e poco ottimizzate;
- **bad politics**: era visto come imposto da burocrazie governative.

### Architettura a 3 livelli e TCP/IP

![[SDC2-L06-009-031.png]]

Una visione più semplice in tre aree:

| Area | Livelli |
| --- | --- |
| **Area applicativa** | applicazione |
| **Interoperabilità del trasporto dell'informazione** | trasporto e rete |
| **Infrastruttura di trasporto dell'informazione** | link e fisico |

![[SDC2-L06-010-032.png]]

Le **applicazioni** e le **funzioni end-to-end** riguardano solo i due host agli estremi; le **funzioni di accesso alla rete** riguardano il collegamento tra ogni host e la rete (la "nuvola").

![[SDC2-L06-010-033.png]]

Tra l'host A e l'host B: l'**area applicativa** comunica direttamente con l'altro capo; l'area di interoperabilità fornisce l'astrazione **process-to-process** (il trasporto) e **host-to-host** (la rete, che passa per nodi intermedi); l'**infrastruttura** è eterogenea (Token Ring, ATM, Ethernet…), e i nodi intermedi traducono tra tecnologie diverse.

**Il problema dell'indirizzamento**: ogni area ha il proprio tipo di indirizzo.

![[SDC2-L06-010-034.png]]

| Area | Indirizzo | Esempio |
| --- | --- | --- |
| Applicativa | nome **DNS** | `www.uniroma1.it` |
| Interoperabilità | indirizzo **IP** | `151.100.16.1` |
| Infrastruttura | indirizzo **MAC** | `ABC123578ABB` |

Servono meccanismi per tradurre da uno all'altro: **DNS** (nome → IP) e **ARP** (IP → MAC).

![[SDC2-L06-011-035.png]]

Riepilogo: tre reti LAN/WAN collegate dai router R1 e R2. Le tre architetture a confronto: la struttura a tre livelli, **Internet** (applicazione, trasporto, internetwork IP, interfaccia di rete) e **OSI** (7 livelli).

![[SDC2-L06-011-036.png]]

Lo stack TCP/IP attraverso tre reti: i due host hanno tutti i livelli (applicazione, TCP/UDP, IP, interfaccia di rete); i router intermedi solo **IP** e l'interfaccia di rete. IP collega reti diverse (l'*internetwork*).

![[SDC2-L06-011-037.png]]

Le dipendenze tra protocolli: HTTP (web) e SMTP (posta) usano **TCP**; RPC (Remote Procedure Call) usa **UDP**; sia TCP sia UDP usano **IP**, che usa **Ethernet**.

## TCP/IP

Vedi [[Modello OSI e TCP-IP]].

![[SDC2-L06-012-038.png]]

La forma a **clessidra** di TCP/IP: sopra, molte applicazioni (Web, Telnet, Email, FTP) e servizi di interoperabilità (RPC, CORBA, SNMP); sotto, molte tecnologie di rete (le LAN 802.3 Ethernet, 802.5 Token Ring, FDDI, 802.11 wireless; le backbone X.25, Frame Relay, ATM). Al centro, il "collo" stretto: un solo protocollo, **TCP/IP**, che fornisce l'astrazione process-to-process e host-to-host. È questo collo stretto a permettere a qualsiasi applicazione di funzionare su qualsiasi rete.

## IP

Vedi [[Protocollo IP]].

Il **protocollo IP** è una grande "coperta" che nasconde ai protocolli superiori tutte le **disomogeneità** dell'infrastruttura di trasporto. Per farlo ha due funzioni di base:

- **indirizzamento di rete**: indirizzi **omogenei**, indipendenti dalla rete fisica sottostante;
- **instradamento** (*routing*) dei pacchetti: inviare pacchetti da un host a un altro usando questi indirizzi.

Proprietà di IP:

- **senza connessione** (*datagram based*): ogni pacchetto viaggia da solo;
- **consegna best effort**: i pacchetti possono **perdersi**, arrivare **fuori ordine**, essere **duplicati** o subire **ritardi arbitrari**. IP ci prova, ma non garantisce nulla.

Servizi di compatibilità con l'hardware sottostante:

- **frammentazione e riassemblaggio** (quando un pacchetto è più grande del massimo consentito dalla rete fisica, la MTU);
- **corrispondenza con gli indirizzi** dei livelli sottostanti (**ARP**).

### Incapsulamento in TCP/IP

![[SDC2-L06-012-039.png]]

I **dati** dell'applicazione ricevono l'header applicativo (**app**); TCP aggiunge il suo header e forma il **segmento TCP**; IP aggiunge il suo header e forma il **datagram IP**; Ethernet aggiunge header e trailer e forma il **frame Ethernet**.

![[SDC2-L06-013-040.png]]

**In trasmissione** IP riceve il segmento dal livello di trasporto, aggiunge l'header e crea il datagram, applica l'algoritmo di routing e invia i dati all'interfaccia di rete opportuna. **In ricezione** IP riceve i dati dall'interfaccia, verifica la validità del datagram e dell'indirizzo; se i dati sono locali individua il protocollo di trasporto, elimina l'header e consegna il segmento.

### Indirizzi IP (IPv4)

![[SDC2-L06-013-041.png]]

Un indirizzo IPv4 è di **32 bit**, scritto come 4 numeri decimali da 0 a 255 (*dotted decimal*). È diviso in:

- **Net-id**: identifica la **rete**;
- **Host-id**: identifica l'**host** dentro quella rete.

![[SDC2-L06-013-042.png]]

Nell'indirizzamento **a classi** (storico), i primi bit dicono dove finisce il net-id:

| Classe | Bit iniziali | Net-id / Host-id | Intervallo |
| --- | --- | --- | --- |
| **A** | `0` | 7 / 24 bit | 0.0.0.0 – 127.255.255.255 (127.x riservato al loopback) |
| **B** | `10` | 14 / 16 bit | 128.0.0.0 – 191.255.255.255 |
| **C** | `110` | 21 / 8 bit | 192.0.0.0 – 223.255.255.255 |
| **D** | `1110` | multicast group ID (28 bit) | 224.0.0.0 – 239.255.255.255 |
| **E** | `11110` | riservato (27 bit) | 240.0.0.0 – 255.255.255.254 |

> [!note] Classi e CIDR
> Oggi le classi non si usano più: con il **CIDR** il confine tra net-id e host-id è arbitrario e si indica con un prefisso, es. `192.168.10.0/24` (24 bit di rete). Nella notazione con le classi, una classe A ha 2²⁴ − 2 host per rete, una C solo 254.

> [!warning] Correzione
> La figura indica per la classe E un campo di 27 bit dopo 5 bit iniziali (`11111`). Nella definizione standard la classe E inizia con `1111` (4 bit) e copre 240.0.0.0–255.255.255.255.

### Il pacchetto IP

![[SDC2-L06-013-043.png]]

L'header IPv4 (righe da 32 bit):

| Campo | Significato |
| --- | --- |
| **Versione** | 4 per IPv4 |
| **IHL** | lunghezza dell'header (in parole da 32 bit) |
| **Tipo di servizio** | priorità / qualità del servizio |
| **Lunghezza totale** | dimensione del datagram |
| **Identificativo, Flags, Offset frammento** | per la frammentazione e il riassemblaggio |
| **Tempo di vita** (TTL) | decrementato a ogni router; a 0 il pacchetto viene scartato (evita cicli infiniti) |
| **Protocollo** | protocollo del livello superiore (6 = TCP, 17 = UDP) |
| **Checksum intestazione** | controllo degli errori sull'header |
| **Indirizzo IP sorgente e destinatario** | |
| **Opzioni, Padding** | campi facoltativi |

L'header senza opzioni è di **20 byte**.

## ARP

Vedi [[ARP]].

L'**ARP** (*Address Resolution Protocol*) serve a passare da un **indirizzo IP** al corrispondente **indirizzo MAC**: così due host sulla stessa rete fisica possono identificarsi e scambiarsi frame.

![[SDC2-L06-014-044.png]]

Gli host A (148.27.34.1) e B (148.27.2.5) hanno ognuno lo stack TELNET / TCP / IP / driver Ethernet con il modulo ARP e la propria scheda con indirizzo MAC. A invia un'**ARP request** sulla rete e B risponde con un'**ARP response** che contiene il proprio MAC.

![[SDC2-L06-014-045.png]]

A invia la richiesta in **broadcast** a tutti gli host della rete ("chi ha questo indirizzo IP?"); C, D, E la ignorano; solo l'host con quell'IP (B) **risponde** con il proprio MAC. A memorizza la risposta in una cache (la tabella ARP).

![[SDC2-L06-014-046.png]]

Nella stessa subnet `192.168.10.0/24`, l'host `.10` invia un frame all'host `.35`: MAC destinazione `000060AD8744`, MAC sorgente `00082C785852`, IP destinazione `192.168.10.35`, IP sorgente `192.168.10.10`.

**Esempio con un router**:

![[SDC2-L06-014-047.png]]

L'host `192.168.10.10` deve raggiungere il server `192.168.11.90`, che è in un'**altra rete**. Lo manda quindi al suo **default gateway** (il router, `192.168.10.1`):

1. primo tratto: **MAC destinazione = quello del router** (`00000C87654A`), MAC sorgente = l'host; **IP destinazione = il server**, IP sorgente = l'host;
2. il router ha un MAC per ogni rete. Riceve il pacchetto e lo inoltra sulla seconda rete, sostituendo il **MAC sorgente con il proprio** (`00000CAB22A7`) e il **MAC destinazione con quello del server** (`009A8744B8C2`). Gli **indirizzi IP non cambiano**.

> [!important] IP vs MAC
> L'indirizzo **IP** identifica la destinazione **finale** e resta uguale per tutto il viaggio. L'indirizzo **MAC** identifica il **prossimo salto** e cambia a ogni router.

## Livello di trasporto: TCP e UDP

Al livello di trasporto ci sono due protocolli: **TCP** e **UDP**.

![[SDC2-L06-015-048.png]]

Il segmento TCP/UDP (header + dati) è il campo dati del datagram IP. Header IP e header TCP sono di 20 byte ciascuno (senza opzioni).

> [!warning] Correzione
> Nella figura è indicato "20 byte" anche per l'header UDP: l'header UDP è di **8 byte**, quello TCP di 20.

![[SDC2-L06-015-049.png]]

Una connessione è individuata dagli estremi: **(IP client, porta client)** e **(IP server, porta server)**. La coppia **indirizzo IP + porta** identifica un **processo** su una macchina: IP individua l'host, la porta il processo. È esattamente ciò che si specifica in un socket.

### TCP

Vedi [[TCP e UDP]].

![[SDC2-L06-015-050.png]]

L'header TCP (20 byte senza opzioni): **porta sorgente** e **porta destinazione**; **sequence number** (posizione del primo byte nel flusso); **acknowledgement number** (prossimo byte atteso dall'altro lato); lunghezza dell'header, flag (SYN, ACK, FIN, RST…), **window** (quanti byte il ricevente può accettare: controllo di flusso); checksum; urgent pointer; opzioni.

Caratteristiche di TCP:

- **orientato alla connessione**: prima di scambiare dati si apre una connessione (il *three-way handshake* SYN, SYN-ACK, ACK);
- **byte stream**: l'applicazione scrive byte, TCP li invia in segmenti, l'applicazione dall'altra parte legge byte (i confini dei messaggi **non** sono preservati);
- **full duplex**: dati in entrambe le direzioni;
- **affidabile**: riscontri, ritrasmissioni, ordinamento, eliminazione dei duplicati;
- **controllo di flusso**: impedisce al mittente di sommergere il **ricevente**;
- **controllo di congestione**: impedisce al mittente di sommergere la **rete**.

![[SDC2-L06-016-051.png]]

Il processo applicativo scrive byte nel **buffer di invio** di TCP, che li trasmette in **segmenti**; il TCP ricevente li mette nel **buffer di ricezione**, da cui l'applicazione legge byte.

![[SDC2-L06-016-052.png]]

Il datagram IP contiene l'header IP (20 byte), l'header TCP (20 byte) e i dati TCP.

### UDP

**UDP** è un protocollo con il **minimo dei meccanismi**:

![[SDC2-L06-016-053.png]]

L'header UDP (8 byte): porta sorgente, porta destinazione, lunghezza del segmento, checksum.

Caratteristiche di UDP:

- **senza connessione**;
- **nessuna garanzia** di consegna, ordine o assenza di duplicati;
- utile per applicazioni **orientate alle transazioni** (una domanda, una risposta: es. DNS) e per i dati in tempo reale (voce, video, giochi), dove un pacchetto in ritardo è inutile;
- supporta il **multicast**.

| | TCP | UDP |
| --- | --- | --- |
| Connessione | sì | no |
| Affidabilità | consegna, ordine, niente duplicati | nessuna garanzia |
| Unità | flusso di byte | datagram (messaggi separati) |
| Controllo di flusso/congestione | sì | no |
| Header | 20 byte | 8 byte |
| Usi | web, email, file transfer | DNS, streaming, VoIP, giochi |

## DNS

Vedi [[DNS]].

Il **DNS** (*Domain Name System*) traduce i **nomi** (es. `www.uniroma1.it`) negli **indirizzi IP**. I server DNS sono messi a disposizione dagli ISP, a cui ci si collega automaticamente.

![[SDC2-L06-017-054.png]]

1. Il client vuole accedere a `thehappylearning.com` e chiede l'indirizzo al **DNS Server 1** (quello del suo ISP).
2. Il DNS Server 1 non ha un record per quel nome e chiede al server successivo.
3. Il **DNS Server 2** trova il record e risponde con l'indirizzo IP (`103.21.59.199`).
4. Il DNS Server 1 **memorizza in cache** il record per le richieste future.
5. Il client riceve l'indirizzo e si collega al sito.

Si può voler cambiare il server DNS. Ad esempio, se in Italia un sito viene dichiarato illegale ma il suo server è all'estero e non viene spento, si ordina ai DNS degli ISP italiani di **non rispondere** per quel nome. Per raggiungere comunque il sito basta usare un altro server DNS (es. uno pubblico), perché il blocco è solo sulla traduzione del nome, non sull'indirizzo IP.
