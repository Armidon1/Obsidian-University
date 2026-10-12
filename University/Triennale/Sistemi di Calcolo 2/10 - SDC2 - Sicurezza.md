---
title: Sicurezza dei Sistemi e delle Reti
aliases:
  - SDC2 — System and network security
  - Sistemi di Calcolo 2 — Lezione 10
tags:
  - sistemi-di-calcolo-2
  - sicurezza
  - malware
  - buffer-overflow
  - crittografia
  - firewall
source: Appunti Filippo/10-security.pdf
---

# Sicurezza dei sistemi e delle reti

> [!abstract] Scopo della lezione
> L'ultima lezione è una panoramica della **sicurezza**: principi generali, la triade **CIA**, gli **attacchi** (passivi e attivi, tipi di attaccanti, **malware**), il **buffer overflow** e le contromisure (canary, DEP, ASLR, return-into-libc), **botnet** e **DoS/DDoS** (SYN flood). Poi le difese: **crittografia** (simmetrica, a chiave pubblica, MAC, hash, certificati, buste digitali), **autenticazione** (password con salt, token, biometria), **controllo degli accessi** (DAC, MAC, RBAC), **antivirus**, **firewall** e **intrusion detection** con gli honeypot. Molti temi sono ripresi in dettaglio in [[1 - MA - Introduction|Malware Analysis]].
> Mappa dei concetti: [[MOC - Sistemi di Calcolo 2]]

## Principi

- La sicurezza **non è un "prodotto"** (ad esempio un firewall), ma un **processo** da gestire correttamente.
- **Nulla è sicuro al 100%** ("le tre regole d'oro della sicurezza informatica: non possedere un computer, non accenderlo, non usarlo").
- La sicurezza di un sistema è quella del suo **componente meno sicuro** (*regola dell'anello più debole*).
- **Security by obscurity non funziona mai**: tenere segreto come funziona un sistema non lo rende sicuro (basta il reverse engineering).
- La **crittografia** è uno strumento potente, ma **non basta**.
- L'anello più debole è l'**utente**: *do not rely on users!*

Quando una rete o un sistema è sicuro? Il testo di riferimento (Stallings, *Operating Systems: Internals and Design Principles*) cita **L'arte della guerra**: "non contare sulla probabilità che il nemico non venga, ma sulla nostra prontezza a riceverlo; non sulla possibilità che non attacchi, ma sul fatto di aver reso inattaccabile la nostra posizione".

![[SDC2-L10-001-000.png]]

Un sondaggio del 2020 in 14 paesi sulle minacce globali: gli **attacchi informatici da altri paesi** sono considerati una minaccia grave dal 65% degli intervistati, quasi quanto cambiamento climatico (70%), malattie infettive (69%) e terrorismo (66%).

![[SDC2-L10-002-001.png]]

I costi del crimine informatico: nel 2015, nelle aziende USA, da 28.3 milioni di dollari (servizi finanziari) a 8.2 milioni (ospitalità). Nel 2019 quasi metà delle aziende aveva oltre 1000 file sensibili non protetti, gli attacchi alla sanità erano previsti in crescita del 400%, e il costo del cybercrime era stimato oltre i **6 trilioni di dollari** l'anno entro il 2021. Il costo maggiore di un attacco è la **perdita di produttività**.

## Obiettivi della sicurezza

Vedi [[Triade CIA]].

Il NIST Computer Security Handbook definisce la **computer security** come: la protezione offerta a un sistema informativo automatizzato per raggiungere gli obiettivi di **integrità**, **disponibilità** e **confidenzialità** delle sue risorse (hardware, software, firmware, informazioni e dati, telecomunicazioni).

La **triade CIA**:

- **Confidentiality**: una perdita di confidenzialità è la **divulgazione non autorizzata** di informazioni;
- **Integrity**: una perdita di integrità è la **modifica o distruzione non autorizzata** di informazioni;
- **Availability**: una perdita di disponibilità è l'**interruzione dell'accesso** alle informazioni o al sistema.

![[SDC2-L10-002-002.png]]

Più in dettaglio:

- **Confidenzialità**:
  - **confidenzialità dei dati**: le informazioni private o riservate non vengono rese disponibili a chi non è autorizzato;
  - **privacy**: le persone controllano quali informazioni su di loro vengono raccolte e memorizzate, da chi e a chi vengono rivelate;
- **Integrità**:
  - **integrità dei dati**: informazioni e programmi cambiano solo in modo specificato e autorizzato (es. solo il professore può cambiare il voto di un esame);
  - **integrità del sistema**: il sistema svolge la sua funzione senza essere compromesso da manipolazioni non autorizzate, volontarie o accidentali;
- **Disponibilità**: i sistemi funzionano prontamente e il servizio non viene negato agli utenti autorizzati.

Concetti aggiuntivi:

- **Autenticità**: essere genuini, verificabili e affidabili; fiducia nella validità di una trasmissione, di un messaggio o del suo mittente. Significa verificare che gli utenti siano **chi dicono di essere** e che ogni input venga da una fonte fidata.
- **Accountability** (responsabilità): le azioni di un'entità devono poter essere **ricondotte univocamente** a quell'entità. Una violazione deve poter essere attribuita a un responsabile: i sistemi devono **registrare** le attività per permettere l'analisi forense o la risoluzione di controversie.

### Lo scopo della sicurezza di sistema

![[SDC2-L10-003-003.png]]

Due sistemi in cui i processi degli utenti accedono ai dati:

1. l'accesso ai dati deve essere controllato (**protezione**);
2. l'accesso al sistema deve essere controllato (**autenticazione degli utenti**, il "guardiano" all'ingresso);
3. i dati trasmessi in rete devono essere protetti (**sicurezza di rete**);
4. i file sensibili devono essere protetti (**sicurezza dei file**).

### Esempi di minacce

![[SDC2-L10-004-004.png]]

| | Disponibilità | Confidenzialità | Integrità |
| --- | --- | --- | --- |
| **Hardware** | apparecchiature rubate o disabilitate | | |
| **Software** | programmi cancellati | copia non autorizzata del software | un programma viene modificato per farlo fallire o fargli fare altro |
| **Dati** | file cancellati | lettura non autorizzata; un'analisi statistica rivela i dati sottostanti | file modificati o falsificati |
| **Linee di comunicazione** | messaggi distrutti o cancellati; linee o reti rese indisponibili | messaggi letti; si osserva lo schema del traffico | messaggi modificati, ritardati, riordinati o duplicati; messaggi falsi |

## Attacchi informatici

Vedi [[Attacchi Passivi e Attivi]].

**Attacchi passivi**: l'attaccante può solo **leggere** (es. *Tempest*, l'intercettazione delle emissioni elettromagnetiche; *packet sniffing*). Cerca di ottenere informazioni senza toccare le risorse del sistema: è un'**intercettazione** (*eavesdropping*) o un monitoraggio delle trasmissioni.

- Sono **difficili da rilevare**, perché non alterano i dati;
- si possono **prevenire** con la crittografia;
- l'enfasi è sulla **prevenzione** più che sulla rilevazione.

**Attacchi attivi**: l'attaccante può **leggere, modificare, generare, distruggere** qualsiasi informazione, alterando il flusso di dati o creandone uno falso. Quattro categorie:

- **replay**: si cattura un messaggio e lo si **ritrasmette** più tardi per ottenere un effetto non autorizzato;
- **masquerade**: un'entità **finge di essere** un'altra;
- **modifica dei messaggi**: una parte del messaggio viene alterata, oppure i messaggi vengono ritardati o riordinati;
- **denial of service**: si impedisce l'uso normale dei servizi di comunicazione, disabilitando la rete o sovraccaricandola di messaggi.

### Tipi di attaccanti

**Hacker**:

- tradizionalmente lo fanno per il **brivido** o per lo **status**;
- cercano bersagli di opportunità e condividono le informazioni;
- anche gli intrusi "benigni" consumano risorse e possono rallentare il sistema;
- contro di loro si usano IDS e IPS (*Intrusion Detection/Prevention System*);
- i **CERT** (*Computer Emergency Response Team*) raccolgono informazioni sulle vulnerabilità e le diffondono agli amministratori.

![[SDC2-L10-005-005.png]]

Le fasi tipiche di un hacker: (1) scegliere il bersaglio con strumenti di lookup IP (NSLookup, Dig…); (2) mappare la rete in cerca di servizi accessibili (NMAP); (3) individuare i servizi vulnerabili; (4) indovinare le password con forza bruta; (5) installare uno strumento di amministrazione remota; (6) aspettare che l'amministratore faccia login e catturare la sua password; (7) usarla per accedere al resto della rete.

**Insider**:

- tra i più **difficili da rilevare e prevenire**;
- motivati da vendetta o da un senso di "diritto";
- i dipendenti **conoscono già** la struttura e il contenuto dei database aziendali.

![[SDC2-L10-005-007.png]]

Comportamenti tipici di una minaccia interna: creare account per sé e per gli amici; accedere ad account e applicazioni non necessari per il proprio lavoro; scrivere a ex e futuri datori di lavoro; chat nascoste; visitare siti per dipendenti scontenti; grandi download e copie di file; accedere alla rete fuori orario.

**Organizzazioni criminali**:

- gruppi organizzati che si incontrano in forum underground per scambiarsi informazioni e dati e coordinare gli attacchi;
- hanno bersagli specifici (es. il file delle carte di credito di un e-commerce);
- attacchi **mordi e fuggi**.

![[SDC2-L10-005-009.png]]

Agiscono in fretta e con precisione; sfruttano le porte vulnerabili del perimetro; lasciano **trojan** come backdoor per rientrare; usano **sniffer** per catturare le password; non restano finché non vengono notati; commettono pochi o nessun errore.

**Advanced Persistent Threat** (APT):

- gruppi organizzati, spesso **sponsorizzati da stati**;
- composti da persone esperte (non solo hacker);
- prendono di mira **infrastrutture critiche**, per sabotarle o esfiltrare informazioni sensibili;
- attacchi **complessi e continui** fino al raggiungimento dell'obiettivo;
- restano **nascosti** a lungo nell'organizzazione bersaglio.

![[SDC2-L10-006-010.png]]

Le fasi di un APT (la *kill chain*): ricognizione, preparazione dell'arma (*weaponization*), consegna, sfruttamento, installazione, contatto con il server di **Command and Control** (C&C, C2), azioni sugli obiettivi, occultamento delle attività.

### Malware

Vedi [[Malware]].

**Malware** è il termine generico per qualsiasi software **malevolo**: progettato per danneggiare un computer o consumarne le risorse, spesso nascosto dentro (o travestito da) software legittimo. A volte si diffonde ad altri computer via email o supporti infetti.

![[SDC2-L10-006-012.png]]

| Nome | Descrizione |
| --- | --- |
| **Virus** | quando viene eseguito, cerca di **replicarsi** in altro codice eseguibile (che diventa "infetto"); quando il codice infetto viene eseguito, esegue anche il virus |
| **Worm** | programma che gira **autonomamente** e propaga una copia completa di sé ad altri host in rete |
| **Logic bomb** | codice inserito da un intruso, dormiente finché non si verifica una condizione; poi compie un'azione non autorizzata |
| **Trojan horse** | programma apparentemente utile che ha una funzione nascosta malevola |
| **Backdoor** (trapdoor) | meccanismo che **aggira** un normale controllo di sicurezza |
| **Platform independent code** | codice (script, macro…) che gira identico su piattaforme eterogenee |
| **Exploit** | codice specifico per una vulnerabilità o un insieme di vulnerabilità |
| **Downloader** | installa altro software su una macchina attaccata (spesso inviato per email) |
| **Auto-rooter** | strumento per entrare in nuove macchine da remoto |
| **Kit** (virus generator) | strumenti per generare automaticamente nuovi virus |
| **Spammer** | invia grandi volumi di email indesiderate |
| **Flooder** | genera grandi volumi di traffico per un attacco DoS |
| **Keylogger** | cattura i tasti premuti |
| **Rootkit** | strumenti usati **dopo** essere entrati e aver ottenuto l'accesso root |
| **Zombie, bot** | programma su una macchina infetta, attivato per lanciare attacchi su altre macchine |
| **Spyware** | raccoglie informazioni da un computer e le trasmette altrove |
| **Adware** | pubblicità integrata nel software (pop-up, redirect) |

**Backdoor (trapdoor)**: un **punto di ingresso segreto** in un programma, che permette di accedere senza le normali procedure di sicurezza. Una **maintenance hook** è una backdoor che i programmatori usano per il debug e il test. Le backdoor diventano minacce quando programmatori senza scrupoli le usano per accessi non autorizzati. È difficile per il sistema operativo controllarle.

**Trojan horse**: un programma utile, o apparentemente utile, che contiene codice nascosto che, quando invocato, fa qualcosa di indesiderato o dannoso. Tre modelli:

- continua a svolgere la funzione del programma originale e **in più** un'attività malevola separata;
- continua a svolgere la funzione originale ma la **modifica** per fare qualcosa di malevolo o per nascondere altre attività;
- svolge una funzione malevola che **sostituisce completamente** quella originale.

**Platform independent code**: programmi che possono essere inviati senza modifiche a piattaforme eterogenee ed eseguiti con la stessa semantica. Vengono trasmessi da un sistema remoto ed eseguiti localmente **senza un'istruzione esplicita dell'utente**. Spesso servono a veicolare virus, worm o trojan, sfruttando le vulnerabilità.

**Virus**: software che "infetta" altri programmi **modificandoli**: contiene il codice per **duplicarsi** e si inserisce in un programma. Quando il computer infetto entra in contatto con software non infetto, una nuova copia del virus vi entra. Si diffonde scambiando dischi o via rete. Ha tre parti:

- **meccanismo di infezione** (come si propaga);
- **trigger** (l'evento che attiva il payload);
- **payload** (cosa fa, oltre a diffondersi).

Un virus può infettare il **boot sector**, i **file** e/o le **macro**.

**Multiple-threat malware**: infetta in più modi. Un virus *multipartite* infetta più tipi di file; un *blended attack* usa più metodi di infezione o trasmissione per massimizzare la velocità di contagio e la gravità.

**Rootkit**: un insieme di programmi installati su un sistema per **mantenere l'accesso amministrativo** (root). Con l'accesso root si ha accesso a tutte le funzioni e i servizi del sistema operativo: il rootkit altera le funzionalità standard dell'host in modo malevolo e **furtivo** (aggiungere o cambiare programmi e file, monitorare processi, inviare e ricevere traffico, avere una backdoor su richiesta). Si nasconde **sovvertendo i meccanismi** che monitorano e riportano processi, file e registri.

Si classifica in base a se sopravvive a un riavvio e alla modalità di esecuzione:

- **persistente**: si attiva a ogni avvio;
- **in memoria**: non ha codice persistente, quindi non sopravvive a un riavvio;
- **user mode**: intercetta le chiamate alle API e ne modifica i risultati;
- **kernel mode**: intercetta le chiamate alle API native del kernel. Può nascondere un processo malevolo **togliendolo dalla lista dei processi attivi** del kernel (vedi [[Process Control Block]]).

## Buffer overflow

Vedi [[Buffer Overflow]].

Il **buffer overflow** è un meccanismo di attacco molto comune. Le tecniche di prevenzione sono note, ma resta un problema serio per l'eredità di software vecchio e bacato e per le cattive abitudini di programmazione.

È causato da un **errore di programmazione** che permette di scrivere **più dati della capacità** di un buffer di dimensione fissa. Il buffer può essere sullo stack, nello heap o tra i dati globali. Si **sovrascrivono le locazioni di memoria adiacenti**, con effetti che vanno dalla corruzione dei dati al trasferimento inatteso del controllo, alle violazioni di accesso, fino all'**esecuzione di codice scelto dall'attaccante**.

Per sfruttarlo, un attaccante deve:

- individuare una vulnerabilità in un programma (ispezionando il codice, tracciandone l'esecuzione o con strumenti di *fuzzing*);
- capire come il buffer è memorizzato e cosa si può corrompere.

### Lo stack

Lo **stack** di un programma contiene gli **stack frame** (record di attivazione) di ogni funzione invocata (vedi [[Stack Frame]] e [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Stack frame e registro EBP|Sistemi di Calcolo]]). È un meccanismo così comune che ha supporto hardware: il registro **ESP** (stack pointer), il registro **EBP** (frame pointer), le istruzioni `push` e `pop`.

- I parametri possono essere passati sullo stack o nei registri, secondo la **convenzione di chiamata**.
- Le variabili locali hanno spazio sullo stack.
- Il frame pointer aiuta a trovare argomenti e variabili locali.

Esempio:

![[SDC2-L10-009-013.png]]

```c
void fun1(char arg1, int arg2) {
    int i;
    char buffer[5];
    buffer[0] = (char)i;
}
void main() {
    fun1('a', 77);
}
```

![[SDC2-L10-009-014.png]]

Il frame di `fun1` sta sotto quello del `main`: dall'alto, `arg2`, `arg1`, l'**indirizzo di ritorno**, `i` e `buffer` (puntato dallo stack pointer). Lo stack cresce verso il basso, ma il buffer si riempie verso l'**alto**: scrivendo oltre la fine di `buffer` si sovrascrivono `i` e poi l'**indirizzo di ritorno**.

![[SDC2-L10-009-015.png]]

L'attacco classico:

- il payload malevolo sovrascrive tutto lo spazio del buffer fino all'indirizzo di ritorno;
- l'indirizzo di ritorno viene cambiato per **puntare dentro lo stack**, poco prima del codice d'attacco;
- di solito il codice d'attacco **avvia una shell** (*shellcode*).

All'attaccante basta mettere un programma nel buffer (o nell'ambiente), perché è lui a controllare cosa ci finisce. Quando la funzione esegue `ret`, salta al suo codice.

**Esempio: autenticazione aggirata.**

![[SDC2-L10-010-016.png]]

```c
void interact_with_user(char* pwd) {
    int authorized = check_auth(pwd);   // 1 se la password è giusta, 0 altrimenti
    char buf[256];
    printf("Enter your data: ");
    gets(buf);
    if (authorized) store_input_data(buf);
    else printf("Denied!");
}
int main(int argc, char** argv) {
    if (argc == 2) interact_with_user(argv[1]);
    return 0;
}
```

`gets` non controlla la lunghezza dell'input. Ci sono **due vulnerabilità**:

1. scrivendo oltre i 256 byte di `buf` si sovrascrive `authorized` e lo si rende **diverso da zero** senza conoscere la password;
2. scrivendo ancora oltre si cambia l'**indirizzo di ritorno** (eseguendo codice in memoria o nel buffer).

Gli appunti stimano che con 261 byte (256 per riempire `buf` + 4 per `authorized`) si arrivi all'indirizzo di ritorno.

> [!warning] Correzione
> Il conto dipende dal layout scelto dal compilatore. Con il frame classico (EBP salvato tra le variabili locali e l'indirizzo di ritorno) servono 256 (`buf`) + 4 (`authorized`) + 4 (EBP salvato) = **264 byte** per arrivare all'indirizzo di ritorno, e 4 in più per sovrascriverlo; con 260 si arriva solo alla fine di `authorized`. Inoltre il compilatore può riordinare le variabili (e con lo stack protector mette i buffer sopra gli interi proprio per impedire il primo attacco).

### Memory safety

I linguaggi a basso livello manipolano la memoria **direttamente**:

- *vantaggio*: efficienza e precisione;
- *svantaggio*: è facile violare le astrazioni dei dati, con accessi arbitrari alla memoria, puntatori e aritmetica dei puntatori; un errore viola la **memory safety**.

Un linguaggio o uno strumento di analisi garantisce la **memory safety** se assicura che letture e scritture restino entro aree di memoria ben definite, appartenenti a parti diverse del programma (spesso delimitate dai **tipi**).

Per fermare gli attacchi: **programmare con più attenzione**. La difesa migliore è il **controllo dei limiti** (*bounds checking*), ma non è sempre ovvio come farlo e i programmatori se ne dimenticano. Nessuna contromisura esistente risolve del tutto il problema.

Le protezioni si dividono in:

- **difese a compile time**: rendono i **nuovi** programmi resistenti agli attacchi. Si basano sulla scelta del linguaggio, sulle tecniche di programmazione sicura, sulle estensioni del linguaggio e le librerie sicure, sui meccanismi di protezione dello stack;
- **meccanismi di protezione dello stack** a runtime: rilevano e bloccano gli attacchi nei programmi **esistenti**.

### Funzioni della libreria C

![[SDC2-L10-011-017.png]]

Molte funzioni della libreria C **non controllano la dimensione dell'input** (vedi [[04 - SDC - Librerie standard del C#Stringhe|Sistemi di Calcolo]]):

- **`gets`** è intrinsecamente insicura ed è stata **rimossa** dallo standard (C11);
- **`strcpy`** è sicura solo se si sa quello che si fa: passarle una stringa di lunghezza ignota o dati senza `'\0'` è un errore. Lo stesso vale per `strcat`.

Le varianti che controllano la dimensione:

- **`strncpy`** viene spesso suggerita al posto di `strcpy`, ma **non aggiunge `'\0'`** se la sorgente è più lunga del limite; meglio `strlcpy` e `strlcat`;
- **`snprintf`** è meglio di `sprintf`;
- **`fgets`** è sicuramente meglio di `gets` (ma si può considerare anche `getline`).

Si combinano più tecniche: **NX bit**, **canary**, **ASLR**.

### Canary

Tecnica a livello di **compilatore**: l'obiettivo è **rilevare** la sovrascrittura dell'indirizzo di ritorno. Il **prologo** delle funzioni mette sullo stack un **canary**, un valore di 32 bit tra l'indirizzo di ritorno e le variabili locali; l'**epilogo** controlla che non sia cambiato prima di eseguire `ret`. (Il nome viene dai canarini usati nelle miniere per rilevare i gas.)

![[SDC2-L10-011-018.png]]

Dall'alto: indirizzo di ritorno, frame pointer, **canary**, variabili locali. Un overflow che vuole arrivare all'indirizzo di ritorno deve per forza sovrascrivere il canary.

Tipi di canary:

- **terminator**: contiene caratteri terminatori (`'\0'`, `'\n'`, `0xFF`…) che le funzioni sulle stringhe non riescono a copiare;
- **random**: un valore casuale scelto all'avvio del programma;
- **random XOR**: un valore casuale in XOR con dati di controllo (es. l'indirizzo di ritorno).

Svantaggio: richiede di **ricompilare** il programma. (In gcc: `-fstack-protector`.)

### DEP (W⊕X) e return-into-libc

Tecnica a livello di **sistema**: separare la memoria eseguibile da quella scrivibile. Una pagina non può essere **scrivibile ed eseguibile** contemporaneamente: è la **Data Execution Prevention** (DEP), detta anche **W⊕X** o bit **NX**. Lo shellcode sullo stack non può più essere eseguito (vedi i permessi delle pagine in [[06 - SDC - Esecuzione dei programmi#/proc/[pid]/maps|Sistemi di Calcolo]]).

**Aggirare W⊕X: return into libc.** Tre ipotesi:

- si può manipolare un **puntatore a codice** (es. l'indirizzo di ritorno);
- lo stack è **scrivibile**;
- si conosce l'indirizzo di una funzione di libreria "adatta" (es. `system()`, che può avviare una shell).

![[SDC2-L10-012-019.png]]

Invece di saltare a codice iniettato, l'attaccante sovrascrive l'indirizzo di ritorno con l'**indirizzo di una funzione di libreria** (già eseguibile), seguito da un indirizzo di ritorno fittizio e dagli argomenti (es. l'indirizzo della stringa `"/bin/sh"`). Quando la funzione vulnerabile esegue `ret`, "chiama" `system("/bin/sh")`. La generalizzazione di questa idea è il **ROP** (*Return-Oriented Programming*).

**ASLR** (*Address Space Layout Randomization*): la posizione di stack, heap e librerie viene **randomizzata** a ogni esecuzione, così l'attaccante non conosce gli indirizzi a cui saltare. È proprio la randomizzazione vista in [[06 - SDC - Esecuzione dei programmi#Immagine di memoria di un processo|Sistemi di Calcolo]].

## Botnet

Vedi [[Botnet e DDoS]].

Un **bot** (*zombie*, *drone*) è un programma che prende segretamente il controllo di un computer collegato a Internet e lo usa per lanciare attacchi difficili da ricondurre al suo autore. Di solito viene installato su centinaia o migliaia di computer di terzi ignari. Un insieme di bot che agiscono in modo coordinato è una **botnet**, che ha tre caratteristiche:

- la **funzionalità del bot**;
- un sistema di **controllo remoto**;
- un **meccanismo di diffusione** per propagare i bot e costruire la botnet.

Il primo passo è infettare molte macchine con il software del bot. Ingredienti essenziali:

- software capace di compiere l'attacco;
- una **vulnerabilità** in un gran numero di sistemi;
- una strategia per trovare le macchine vulnerabili (**scanning** o *fingerprinting*).

L'attaccante cerca macchine vulnerabili e le infetta; il bot sulle macchine infette ripete lo stesso processo, finché non si forma una grande rete distribuita di macchine infette. Strategie di scanning: **casuale**, **hit list** (lista di bersagli preparata in anticipo), **topologica** (usa le informazioni trovate sulla macchina infetta, es. la rubrica), **sottorete locale**.

Usi dei bot:

- attacchi **DDoS**;
- **spam** in massa;
- **sniffing** del traffico per catturare nomi utente e password;
- **keylogging**;
- diffusione di **nuovo malware**;
- installazione di add-on pubblicitari e *browser helper object*, con siti falsi e accordi per farsi pagare i clic sulle pubblicità;
- attacchi alle reti **IRC** (la vittima viene sommersa di richieste);
- **manipolazione di sondaggi e giochi online** (ogni bot ha un IP diverso e sembra una persona reale).

## Denial of Service

Un **Denial of Service** (DoS) impedisce o degrada l'uso autorizzato di reti, sistemi o applicazioni **esaurendo le risorse**: CPU, memoria, banda, spazio su disco. Può colpire la banda di rete, le risorse di sistema o quelle delle applicazioni.

Un DoS classico è un semplice **flood di ping** da un collegamento ad alta capacità verso uno a bassa capacità, che fa perdere traffico; la sorgente è però facile da identificare.

Attacchi di **flooding**, classificati per protocollo:

- **ICMP flood**: pacchetti ICMP, es. *echo request* (di solito lasciati passare, alcuni sono necessari);
- **UDP flood**: pacchetti UDP verso una porta;
- **TCP SYN flood**: pacchetti SYN (richieste di connessione), ma come attacco di volume.

**Source address spoofing**: si usano indirizzi sorgente **falsificati** (facile con i *raw socket*, se si hanno i privilegi). Si generano grandi volumi di pacchetti verso il bersaglio con indirizzi sorgente casuali: si ottiene la stessa congestione, le risposte si disperdono per Internet e la vera sorgente è molto più difficile da identificare.

**SYN spoofing**: l'attaccante usa indirizzi sorgente casuali o di un server sovraccarico, così (quasi) nessuno risponde con un reset. Richiede **molto meno traffico**: l'attaccante può essere su un collegamento a bassa capacità.

![[SDC2-L10-013-020.png]]

Il **three-way handshake** di TCP: il client invia **SYN**, il server risponde **SYN-ACK** e riserva risorse per la connessione, il client conferma con **ACK** e la connessione è stabilita.

![[SDC2-L10-013-021.png]]

Il **SYN spoofing**: l'attaccante invia molti SYN con indirizzi falsi. Il server risponde con SYN-ACK a indirizzi che non risponderanno mai, e tiene ogni connessione mezza aperta in attesa dell'ACK ("Open port. Waiting for ACK"). Presto la tabella delle connessioni si **esaurisce**, e quando un client legittimo invia il suo SYN viene **rifiutato**.

### DDoS

Un singolo attaccante ha un volume limitato. Usando **molti sistemi** si ottengono volumi molto più alti: è il **Distributed Denial of Service** (DDoS). Spesso si usano PC compromessi (zombie con backdoor) che formano una botnet.

![[SDC2-L10-014-022.png]]

La gerarchia di controllo: l'**attaccante** comanda alcuni **handler zombie**, ognuno dei quali comanda molti **agent zombie**, che attaccano tutti insieme il **bersaglio**.

### Difese contro il DoS

- Volumi di traffico alti possono essere **legittimi**: un sito diventato improvvisamente popolare (*slashdotted*) o molto visitato (es. le Olimpiadi).
- Anche il traffico legittimo può essere creato da un attaccante.
- Tre linee di difesa: **prevenzione** e anticipo dell'attacco; **rilevazione e filtraggio**; **risalita alla sorgente** e identificazione.

**Prevenzione**:

- bloccare gli indirizzi sorgente falsificati sui router il più vicino possibile alla sorgente (ancora troppo poco fatto);
- limitare la velocità (*rate control*) di certi tipi di pacchetti (alcuni ICMP, UDP, TCP SYN);
- gestire le connessioni TCP in modo modificato: **SYN cookie** quando la tabella è piena, o scarto selettivo o casuale;
- bloccare i broadcast IP diretti;
- bloccare servizi e combinazioni sospette;
- gestire gli attacchi applicativi con dei "**puzzle**" per distinguere gli umani (es. i CAPTCHA);
- buone pratiche generali di sicurezza;
- server **replicati** quando servono prestazioni e affidabilità.

**Risposta agli attacchi**:

- avere un buon **piano di risposta agli incidenti**, con i contatti dell'ISP per filtrare il traffico a monte;
- avere filtri standard;
- idealmente, monitor di rete e IDS per rilevare e notificare il traffico anomalo;
- identificare il tipo di attacco, catturare e analizzare i pacchetti, progettare filtri per bloccare il traffico a monte, o identificare e correggere il bug;
- chiedere all'ISP di risalire alla sorgente (difficile e lungo, ma necessario per un'azione legale);
- attuare il piano di emergenza;
- aggiornare il piano di risposta.

## Tecniche di protezione: crittografia

Vedi [[Crittografia Simmetrica e Asimmetrica]].

Gli algoritmi crittografici sono un elemento importante dei servizi di sicurezza: crittografia **simmetrica**, a **chiave pubblica** (asimmetrica), **firme digitali** e gestione delle chiavi, **funzioni hash** sicure.

**Numeri casuali**: hanno molti usi (chiavi, nonce…). Requisiti:

- **casualità**: superare i test statistici di distribuzione uniforme e indipendenza;
- **imprevedibilità**: i valori successivi non devono essere deducibili dai precedenti.

Spesso si usano algoritmi che generano numeri **pseudocasuali**: superano i test statistici, ma sono potenzialmente prevedibili. I veri generatori casuali usano una sorgente **non deterministica** (radiazioni, scariche di gas, condensatori con perdite), sempre più spesso integrata nei processori.

### Crittografia simmetrica

![[SDC2-L10-015-023.png]]

Mittente e destinatario **condividono la stessa chiave segreta K**. Il testo in chiaro X viene cifrato: $Y = E(K, X)$; il destinatario decifra con l'algoritmo inverso: $X = D(K, Y)$.

Attacchi:

- **crittoanalisi**: si sfrutta la natura dell'algoritmo, più qualche conoscenza del testo in chiaro o qualche coppia testo in chiaro/cifrato, per dedurre il testo o la chiave;
- **forza bruta**: si provano **tutte le chiavi** possibili finché non si ottiene un testo sensato.

![[SDC2-L10-015-024.png]]

Ricerca esaustiva delle chiavi:

| Chiave (bit) | Numero di chiavi | A 1 decifratura/µs | A 10⁶ decifrature/µs |
| --- | --- | --- | --- |
| 32 | 2³² ≈ 4.3 × 10⁹ | 2³¹ µs ≈ 35.8 minuti | 2.15 ms |
| 56 | 2⁵⁶ ≈ 7.2 × 10¹⁶ | 2⁵⁵ µs ≈ 1142 anni | 10.01 ore |
| 128 | 2¹²⁸ ≈ 3.4 × 10³⁸ | ≈ 5.4 × 10²⁴ anni | ≈ 5.4 × 10¹⁸ anni |
| 168 | 2¹⁶⁸ ≈ 3.7 × 10⁵⁰ | ≈ 5.9 × 10³⁶ anni | ≈ 5.9 × 10³⁰ anni |
| 26 caratteri (permutazione) | 26! ≈ 4 × 10²⁶ | ≈ 6.4 × 10¹² anni | ≈ 6.4 × 10⁶ anni |

In media si trova la chiave dopo averne provata **metà** (per questo il tempo è 2ⁿ⁻¹).

![[SDC2-L10-015-025.png]]

Gli anni necessari a rompere la chiave crescono **esponenzialmente** con la sua lunghezza (asse y logaritmico): ogni bit in più raddoppia il tempo.

![[SDC2-L10-016-026.png]]

| | DES | Triple DES | AES |
| --- | --- | --- | --- |
| Blocco in chiaro (bit) | 64 | 64 | 128 |
| Blocco cifrato (bit) | 64 | 64 | 128 |
| Chiave (bit) | 56 | 112 o 168 | 128, 192 o 256 |

- **DES** (*Data Encryption Standard*): purtroppo ancora tra i più usati. Blocchi da 64 bit e chiave da **56 bit**: troppo corta (si rompe in poche ore).
- **Triple DES**: ripete DES **tre volte** con due o tre chiavi diverse. Molto più sicuro ma molto più lento.
- **AES** (*Advanced Encryption Standard*): cifrario a blocchi con blocchi da 128 bit e chiavi da 128, 192 o 256 bit. Lo standard attuale.

**Cifrari a blocchi e a flusso**:

![[SDC2-L10-016-027.png]]

(a) **Cifrario a blocchi** (modalità ECB, *electronic codebook*): il testo è diviso in blocchi P1…Pn di b bit, ognuno cifrato indipendentemente con la chiave K.

> [!note]
> In modalità ECB blocchi in chiaro uguali danno blocchi cifrati uguali, e quindi si vedono gli schemi del testo: nella pratica si usano modalità come CBC o GCM.

![[SDC2-L10-016-028.png]]

(b) **Cifrario a flusso**: un generatore pseudocasuale, inizializzato con la chiave K, produce un flusso di byte k che viene combinato in **XOR** con il testo in chiaro; il destinatario genera lo stesso flusso e fa di nuovo XOR per riottenere il testo.

### Crittografia a chiave pubblica

![[SDC2-L10-017-029.png]]

**Confidenzialità**: ogni utente ha una coppia di chiavi, una **pubblica** (nota a tutti, nel "portachiavi" pubblico) e una **privata**. Bob cifra con la **chiave pubblica di Alice** ($PU_a$): $Y = E(PU_a, X)$. Solo Alice, con la sua **chiave privata** ($PR_a$), può decifrare: $X = D(PR_a, Y)$.

Requisiti:

- è computazionalmente **facile** generare le coppie di chiavi;
- è facile per il mittente, conoscendo la chiave pubblica, cifrare;
- è facile per il destinatario, conoscendo la chiave privata, decifrare;
- è computazionalmente **impossibile** ricavare la chiave privata da quella pubblica;
- è computazionalmente impossibile ricavare in altro modo il messaggio originale;
- è utile se **entrambe** le chiavi possono essere usate per cifrare (una cifra, l'altra decifra).

Algoritmi più noti:

- **RSA** (Rivest, Shamir, Adleman): l'unico algoritmo a chiave pubblica ampiamente accettato per la cifratura; servono chiavi da **1024+ bit** (oggi almeno 2048);
- **Diffie-Hellman**: permette solo lo **scambio** di una chiave segreta;
- **DSS** (*Digital Signature Standard*): solo firma digitale (con SHA-1);
- **crittografia a curve ellittiche** (ECC): sicurezza come RSA con chiavi molto più piccole;
- **crittografia omomorfica** (HE): permette di **elaborare dati cifrati** senza decifrarli.

![[SDC2-L10-017-030.png]]

**Autenticazione**: si usano le chiavi al contrario. Bob cifra con la propria **chiave privata** ($PR_b$); chiunque può decifrare con la sua **chiave pubblica** ($PU_b$). Se la decifratura funziona, il messaggio **può venire solo da Bob**: è il principio della **firma digitale**.

### Autenticazione dei messaggi

Protegge dagli **attacchi attivi**: verifica che il messaggio ricevuto sia **autentico** (contenuto non alterato, mittente autentico, tempestivo e nella sequenza giusta). Si può usare la crittografia convenzionale (solo mittente e destinatario hanno la chiave) o meccanismi di autenticazione separati (si aggiunge un **tag di autenticazione** al messaggio in chiaro).

![[SDC2-L10-018-031.png]]

**Message Authentication Code** (MAC): il mittente calcola un MAC dal messaggio con un algoritmo e una chiave segreta K, e lo aggiunge al messaggio. Il destinatario ricalcola il MAC con la stessa chiave e lo **confronta** con quello ricevuto: se coincidono, il messaggio è integro e viene da chi conosce K.

### Funzioni hash sicure

![[SDC2-L10-018-032.png]]

Una **funzione hash** H prende un messaggio di **lunghezza qualsiasi** e produce un **valore di lunghezza fissa** h (l'impronta, o *digest*).

![[SDC2-L10-019-033.png]]

Tre modi di usare l'hash per autenticare un messaggio:

- **(a) con crittografia convenzionale**: si calcola l'hash, lo si cifra con la chiave condivisa K e lo si aggiunge al messaggio; il destinatario ricalcola l'hash, decifra quello ricevuto e li confronta;
- **(b) con crittografia a chiave pubblica**: l'hash viene cifrato con la **chiave privata** del mittente ($PR_a$) e verificato con la sua chiave pubblica: è una **firma digitale**;
- **(c) con un valore segreto**: mittente e destinatario condividono un segreto S, che viene concatenato al messaggio prima di calcolare l'hash (senza cifratura); il segreto non viene trasmesso (è l'idea dell'HMAC).

Requisiti di una funzione hash:

- si applica a dati di **qualsiasi dimensione**;
- produce un output di **lunghezza fissa**;
- H(x) è **facile da calcolare**;
- **one-way**: dato h, è computazionalmente impossibile trovare x tale che H(x) = h;
- **resistenza debole alle collisioni**: dato x, è impossibile trovare y ≠ x con H(y) = H(x);
- **resistenza forte alle collisioni**: è impossibile trovare **qualsiasi** coppia (x, y) con H(x) = H(y).

Due approcci di attacco: **crittoanalisi** (debolezze logiche dell'algoritmo) e **forza bruta** (la robustezza è proporzionale alla lunghezza dell'hash).

**SHA** è l'algoritmo di hash più usato: SHA-1 dà un hash di 160 bit (oggi considerato insicuro); i più recenti SHA-256, SHA-384, SHA-512 offrono maggiore dimensione e sicurezza.

### Certificati a chiave pubblica

![[SDC2-L10-020-034.png]]

Come si fa a sapere che una chiave pubblica appartiene davvero a chi dice di possederla? Un **certificato** contiene l'identità dell'utente e la sua chiave pubblica. Una **Certification Authority** (CA) ne calcola l'hash e lo **cifra con la propria chiave privata**, formando la **firma**, che viene aggiunta al certificato. Chi riceve il certificato firmato può verificare la firma con la **chiave pubblica della CA** (che è nota e fidata, es. preinstallata nel browser). È il meccanismo di HTTPS.

### Buste digitali

![[SDC2-L10-020-035.png]]

La crittografia a chiave pubblica è lenta, quella simmetrica veloce ma richiede di condividere la chiave. La **busta digitale** le combina:

- **(a) creazione**: si genera una **chiave simmetrica casuale**, si cifra il messaggio con quella, e si cifra la chiave simmetrica con la **chiave pubblica del destinatario**. La busta contiene il messaggio cifrato e la chiave cifrata;
- **(b) apertura**: il destinatario decifra la chiave simmetrica con la propria **chiave privata**, e poi il messaggio con la chiave simmetrica.

### Cifratura dei dati memorizzati

È comune cifrare i dati **trasmessi**, molto meno quelli **memorizzati**, che però possono essere copiati, salvati in backup e recuperati. Approcci: appliance di back-end, cifratura dei nastri nelle librerie di backup, cifratura in background dei dati di laptop e PC.

## Autenticazione

Vedi [[Autenticazione e Controllo degli Accessi]].

L'**autenticazione basata su password** è la linea di difesa più usata contro gli intrusi. La password **autentica l'ID** dell'utente che fa login. L'ID determina se l'utente è autorizzato ad accedere, quali privilegi ha e (con il controllo discrezionale) a cosa può accedere.

### Password con hash e salt

![[SDC2-L10-021-036.png]]

**(a) Memorizzare una nuova password**: si genera un **salt** casuale; password e salt passano per una **funzione hash lenta**; nel file delle password si memorizzano **ID utente, salt e hash** (mai la password in chiaro).

![[SDC2-L10-022-037.png]]

**(b) Verificare una password**: dall'ID si legge il salt memorizzato, si calcola l'hash della password inserita con quel salt e lo si **confronta** con quello memorizzato.

Il **salt** serve a tre cose:

- impedisce che **password uguali** siano visibili come tali nel file (due utenti con la stessa password hanno salt diversi, quindi hash diversi);
- rende molto più difficili gli **attacchi a dizionario offline** (non si può precalcolare un'unica tabella di hash);
- rende quasi impossibile scoprire se una persona usa **la stessa password** su più sistemi.

La funzione hash è volutamente **lenta**, per rallentare i tentativi di forza bruta.

Due minacce allo schema delle password UNIX:

- un utente può accedere a una macchina con un account **guest**;
- i **password cracker**: programmi che indovinano le password. Se l'attaccante ottiene una copia del file delle password, può far girare il cracker su un'altra macchina con calma, provando milioni di password in tempi ragionevoli.

Implementazioni UNIX:

- storicamente ogni utente sceglie una password di **massimo 8 caratteri** stampabili, convertita in un valore di 56 bit usato come chiave di una routine di cifratura;
- la routine di hash, **`crypt(3)`**, è basata su **DES**, ed è progettata per scoraggiare i tentativi (le implementazioni software di DES sono lente rispetto all'hardware);
- molti sistemi (Linux, Solaris, FreeBSD) usano un hash basato su **MD5**;
- la versione più sicura, sviluppata per OpenBSD, usa **bcrypt**, basato sul cifrario a blocchi Blowfish.

(Oggi Linux usa SHA-512 in `/etc/shadow`, e si consigliano funzioni come bcrypt, scrypt o Argon2, appositamente lente.)

### Token

I **token** sono oggetti che l'utente **possiede** per autenticarsi. Due tipi:

- **memory card**: memorizzano ma **non elaborano** dati. La più comune è la carta bancaria con **banda magnetica**, che contiene un semplice codice leggibile e riprogrammabile da un lettore economico (esistono anche memory card con memoria elettronica). Si usano da sole per l'accesso fisico o insieme a una password o un PIN.

  ![[SDC2-L10-023-038.png]]

  Possibili svantaggi: servono **lettori speciali**, il token si può **perdere**, gli utenti sono **insoddisfatti** (scomodità).

- **smart card**: contengono un **processore**. Possono avere la forma di una carta bancaria, ma anche di calcolatrici, chiavi o altri piccoli oggetti. L'interfaccia può essere **manuale** (tastierino e display) o **elettronica** (comunicazione con un lettore). Protocolli di autenticazione:
  - **statico**;
  - **generatore di password dinamiche** (es. le chiavette OTP delle banche);
  - **challenge-response** (il sistema invia una sfida e la carta risponde calcolando una funzione con la propria chiave segreta).

### Biometria

L'**autenticazione biometrica** riconosce una persona in base a sue **caratteristiche fisiche** uniche.

- **Statiche**: impronte digitali, geometria della mano, caratteristiche del viso, retina e iride.
- **Dinamiche**: voce, firma.

![[SDC2-L10-024-040.png]]

- **viso**: il modo più comune con cui gli umani si riconoscono (occhi, sopracciglia, naso, labbra, mento); in alternativa si usa una telecamera a infrarossi per un *termogramma* del viso;
- **impronte digitali**: lo schema di creste e solchi sulla punta delle dita, **unico** in tutta la popolazione;
- **geometria della mano**: forma, lunghezza e larghezza delle dita;
- **retina**: lo schema dei vasi sanguigni sotto la superficie della retina è unico; si ottiene proiettando nell'occhio un fascio di luce visibile o infrarossa a bassa intensità;
- **iride**: la sua struttura dettagliata è unica;
- **firma**: ognuno ha uno stile di scrittura unico;
- **voce**: legata alle caratteristiche fisiche e anatomiche di chi parla.

![[SDC2-L10-024-041.png]]

**Costo vs accuratezza**: voce, viso, firma e mano sono meno accurati; impronte e retina più accurati; l'**iride** è il più accurato ma anche il più costoso.

## Controllo degli accessi

Il **controllo degli accessi** stabilisce **quali tipi di accesso** sono permessi, **in quali circostanze** e **a chi**. Le politiche:

- **DAC** (*Discretionary Access Control*): in base all'**identità** di chi chiede l'accesso e a regole che dicono cosa può fare. Il proprietario di una risorsa decide chi può accedervi (es. i permessi Unix, vedi [[Permessi e Ownership]]);
- **MAC** (*Mandatory Access Control*): si confrontano **etichette di sicurezza** (quanto è sensibile la risorsa) con **autorizzazioni** (*clearance*, a cosa può accedere il soggetto), come nei sistemi militari (riservato, segreto, top secret). Il proprietario non può cambiare le regole;
- **RBAC** (*Role-Based Access Control*): in base ai **ruoli** degli utenti nel sistema e alle regole su cosa può fare ogni ruolo.

![[SDC2-L10-025-042.png]]

Le tre politiche **non sono esclusive**: un sistema può usarne più di una contemporaneamente.

> [!warning] MAC: due significati
> In questa lezione **MAC** indica sia il *Message Authentication Code* (crittografia) sia il *Mandatory Access Control* (controllo degli accessi). Dal contesto è sempre chiaro quale.

![[SDC2-L10-025-043.png]]

La **matrice di controllo degli accessi estesa**: le righe sono i **soggetti** (S1, S2, S3), le colonne gli **oggetti** (gli stessi soggetti, i file F1 e F2, i processi P1 e P2, i dischi D1 e D2). Ogni cella dice quali diritti ha il soggetto sull'oggetto: *control*, *owner*, *read*, *write*, *execute*, *wakeup*, *stop*, *seek*… L'asterisco indica il **copy flag**: il soggetto può trasferire quel diritto ad altri.

![[SDC2-L10-026-044.png]]

L'organizzazione della funzione di controllo degli accessi: ogni richiesta di un soggetto (es. S1 *read F*) passa per il meccanismo di controllo corrispondente (file system, hardware di indirizzamento della memoria, gestore dei processi, dei terminali e dispositivi, hardware di decodifica delle istruzioni), che consulta la **matrice** prima di permettere l'accesso all'oggetto. Le richieste di modificare i diritti (*grant*, *delete*) passano per l'**access matrix monitor**, l'unico che può scrivere nella matrice.

### RBAC

Il **Role-Based Access Control** si basa sui **ruoli** che gli utenti assumono nel sistema, non sulla loro identità. Un ruolo è una funzione lavorativa nell'organizzazione. I diritti di accesso vengono assegnati ai **ruoli**, e gli utenti vengono assegnati ai ruoli (in modo statico o dinamico) secondo le loro responsabilità. Il NIST ha emanato uno standard per il controllo degli accessi e l'amministrazione tramite ruoli.

![[SDC2-L10-026-045.png]]

Gli **utenti** sono assegnati ai **ruoli**, e i ruoli hanno accesso alle **risorse**. Più utenti possono avere lo **stesso ruolo**, e un utente può avere **più ruoli**.

![[SDC2-L10-027-046.png]]

![[SDC2-L10-027-047.png]]

La rappresentazione con matrici: una prima matrice **utenti × ruoli** (una X indica che l'utente ha quel ruolo) e una seconda matrice **ruoli × oggetti** con i diritti, come la matrice di controllo degli accessi ma con i ruoli al posto dei soggetti. Quando un utente cambia mansione, basta cambiargli il ruolo invece di modificare tutti i suoi diritti uno per uno.

## Antivirus

![[SDC2-L10-027-049.png]]

Gli approcci antivirus:

1. **rilevazione** (*detection*): una volta avvenuta l'infezione, accorgersene e trovare il virus;
2. **identificazione**: identificare il virus specifico che ha infettato il programma;
3. **rimozione**: eliminare ogni traccia del virus dal programma infetto e riportarlo allo stato originale, e rimuoverlo da tutti i sistemi infetti perché non si diffonda.

La soluzione ideale è la **prevenzione**: non far entrare il virus nel sistema. In generale è impossibile, ma riduce il numero di attacchi riusciti. Se la rilevazione funziona ma l'identificazione o la rimozione no, l'alternativa è **eliminare il programma infetto** e ricaricare una **copia pulita** dal backup.

### Generic Decryption

Il **Generic Decryption** (GD) permette all'antivirus di rilevare anche i **virus polimorfici** più complessi (che cambiano il proprio codice a ogni infezione, cifrandosi con chiavi diverse) mantenendo una scansione veloce. L'idea: per attivarsi, un virus polimorfico deve **decifrarsi**. I file eseguibili vengono quindi fatti girare in uno scanner GD.

![[SDC2-L10-028-050.png]]

Lo scanner GD contiene:

- un **emulatore di CPU**: un computer virtuale software. I file eseguibili vengono **interpretati** dall'emulatore, quindi il processore reale non viene toccato;
- uno **scanner di firme virali**: cerca nel codice le firme dei virus noti (dopo che il virus si è decifrato da solo nell'emulatore);
- un **modulo di controllo dell'emulazione**: controlla l'esecuzione del codice.

Il problema di progetto più difficile è decidere **per quanto tempo** far girare ogni interpretazione.

### Digital Immune System

Il **Digital Immune System** è un approccio completo alla protezione dai virus, sviluppato da IBM e perfezionato da Symantec. È nato per la crescente minaccia dei virus propagati via Internet: due tendenze hanno aumentato la velocità di propagazione, la **posta integrata** e i **programmi mobili**. L'obiettivo è una **risposta rapida**, così da eliminare i virus quasi appena compaiono.

![[SDC2-L10-028-051.png]]

1. Un programma di monitoraggio su un client rileva un possibile virus e ne invia una copia alla **macchina amministrativa** della rete privata.
2. La macchina amministrativa lo inoltra alla **macchina di analisi** centrale.
3. La macchina di analisi esegue il virus in un ambiente protetto, ne **analizza** comportamento e struttura, ne **estrae la firma** e ricava la "prescrizione" (come identificarlo e rimuoverlo).
4. La prescrizione torna alla macchina amministrativa.
5. Che la invia al client infetto.
6. E a tutti gli altri client della rete.
7. La prescrizione viene inviata anche ad altre reti e utenti, che sono così protetti prima ancora di essere infettati.

## Firewall

Vedi [[Firewall e Intrusion Detection]].

Un **firewall** protegge una rete: **analizza i pacchetti** del traffico e decide se un pacchetto può **proseguire** o no. È un mezzo efficace per proteggere le LAN: la connettività a Internet è essenziale per organizzazioni e persone, ma crea una minaccia. Si possono proteggere le singole workstation e i server, ma si usa il firewall soprattutto come **difesa perimetrale** (un unico punto di passaggio in cui imporre la sicurezza).

Capacità:

- definisce un unico **punto di strozzatura** (*choke point*);
- è un posto in cui **monitorare** gli eventi di sicurezza;
- è una piattaforma comoda per altre funzioni (NAT, monitoraggio dell'uso, VPN IPsec).

Limiti:

- non protegge dagli attacchi che lo **aggirano** (es. un modem che collega direttamente un PC interno a Internet);
- non protegge del tutto dalle **minacce interne**;
- una LAN wireless mal protetta può permettere l'accesso dall'esterno;
- laptop, PDA o dispositivi portatili **infettati fuori** e poi usati dentro la rete.

![[SDC2-L10-029-052.png]]

I tipi di firewall:

- **(a) modello generale**: il firewall separa la rete interna (protetta, es. aziendale) da quella esterna (non fidata, es. Internet);
- **(b) packet filtering**: guarda solo gli header dei livelli **rete e trasporto** di ogni pacchetto;
- **(c) stateful inspection**: come il packet filtering, ma tiene **informazioni di stato** sulle connessioni;
- **(d) application proxy**: lavora a livello **applicativo**; il client si connette al proxy, che si connette al server per lui (ci sono due connessioni di trasporto separate);
- **(e) circuit-level proxy**: lavora a livello di **trasporto**: inoltra le connessioni TCP senza guardare il contenuto applicativo.

### Packet filtering

Applica delle **regole** ai pacchetti in entrata e in uscita, in base alle informazioni nell'header: indirizzi IP e porte di sorgente e destinazione, protocollo IP, interfaccia. Di solito è una lista di regole: se un pacchetto corrisponde a una regola, la regola dice se inoltrarlo o scartarlo.

Due politiche di default:

- **discard**: si **vieta tutto** ciò che non è esplicitamente permesso. Più conservativa e controllata, più visibile agli utenti;
- **forward**: si **permette tutto** ciò che non è esplicitamente vietato. Più facile da gestire e usare, ma meno sicura.

![[SDC2-L10-030-053.png]]

Esempi di insiemi di regole ("tutto passa tranne…" o "niente passa tranne…"):

- **A**: blocca tutto il traffico da `SPIGOT` (un host non fidato); permette le connessioni in entrata alla porta 25 (SMTP) del nostro gateway di posta;
- **B**: la regola di **default**: blocca tutto;
- **C**: permette a qualsiasi host interno di inviare alla porta 25 di qualsiasi host esterno. È troppo permissiva: chiunque all'esterno può usare la propria porta 25 per raggiungere qualunque nostro host;
- **D**: permette ai nostri host di inviare pacchetti alla porta SMTP esterna, e accetta in ingresso solo i pacchetti dalla porta 25 con il flag **ACK** (risposte a connessioni già aperte da noi);
- **E**: permette le nostre connessioni in uscita, le risposte (ACK) e il traffico verso porte > 1024 (i server non privilegiati).

Debolezze del packet filter:

- non può prevenire gli attacchi ai **bug delle applicazioni**;
- logging limitato;
- non supporta l'autenticazione avanzata degli utenti;
- vulnerabile agli attacchi ai bug di TCP/IP;
- una **configurazione sbagliata** può aprire delle falle.

Attacchi: **IP address spoofing** (falsificare l'indirizzo sorgente per sembrare un host interno), **source route attack** (il mittente specifica il percorso del pacchetto per aggirare i controlli), **tiny fragment attack** (frammentare il pacchetto in modo che le informazioni dell'header TCP finiscano in un secondo frammento non controllato).

### Stateful inspection

Esamina gli header ma tiene anche traccia delle **connessioni TCP**. Di solito il server usa una porta bassa nota e il client una porta alta assegnata dinamicamente. Un semplice packet filter deve permettere **tutti** i pacchetti in ingresso verso le porte alte (per le risposte); un firewall stateful invece tiene una **tabella delle connessioni TCP** e permette il traffico in ingresso verso le porte alte solo per i pacchetti che corrispondono a una connessione nella tabella. Può controllare anche i numeri di sequenza TCP.

Altre soluzioni: **application-level gateway** (proxy), **circuit-level gateway**, socket-level gateway.

### Posizione dei firewall

![[SDC2-L10-031-054.png]]

Una configurazione tipica: dopo il **router di confine** c'è un **firewall esterno**; dietro, la **DMZ** interna con i server pubblici (web, email, DNS); poi un **firewall interno** che protegge la **rete interna** (server applicativi e di database, workstation). La DMZ è una zona intermedia: se un server pubblico viene compromesso, l'attaccante deve comunque superare il secondo firewall.

![[SDC2-L10-031-055.png]]

**Firewall distribuiti**: oltre ai firewall di rete, ogni host (server, workstation, utenti remoti) ha un proprio **firewall residente sull'host**. Questo protegge anche dalle minacce interne e dagli host mobili.

## Intrusion detection

L'obiettivo è identificare le **anomalie**. Le intrusioni ostili o indesiderate vanno da quelle benigne a quelle gravi:

- **intrusione dell'utente**: login non autorizzato, abuso di privilegi;
- **intrusione software**: virus, worm o trojan.

Classi di intrusi: hacker, **masquerader** (chi usa l'account di un altro), APT.

Principi:

- l'intrusion detection si basa sull'ipotesi che il comportamento di un intruso **differisca** da quello di un utente legittimo in modi **quantificabili**;
- se un'intrusione viene rilevata in fretta, l'intruso può essere identificato e cacciato prima che faccia danni;
- un IDS efficace è un **deterrente**, quindi aiuta anche a prevenire;
- l'intrusion detection raccoglie informazioni sulle tecniche di intrusione, utili a migliorare la prevenzione.

![[SDC2-L10-032-056.png]]

I profili di comportamento di intrusi e utenti autorizzati, come due distribuzioni di probabilità su un parametro misurabile. Le medie sono diverse, ma le due curve **si sovrappongono**: nella zona comune un IDS non può distinguere con certezza. Se si sposta la soglia per rilevare più intrusi si hanno più **falsi positivi** (utenti legittimi segnalati); se la si sposta dall'altra parte, più **falsi negativi** (intrusi non rilevati).

### IDS basati sull'host

Un **Host-Based IDS** monitora in vari modi l'attività del sistema per rilevare comportamenti sospetti: il suo scopo è rilevare le intrusioni, **registrare** gli eventi sospetti e inviare **allarmi**. Rileva sia intrusioni **esterne** sia **interne**.

**Anomaly detection**: raccoglie dati sul comportamento degli utenti legittimi nel tempo e segnala le deviazioni.

- **Threshold detection**: controlla se certi eventi si ripetono troppo spesso in un intervallo. Da sola è un rilevatore rozzo e poco efficace: bisogna scegliere sia le soglie sia gli intervalli.
- **Profile based**: caratterizza il comportamento passato di utenti e gruppi e rileva le deviazioni significative analizzando gli **audit record**. Metriche: contatori, indicatori (*gauge*), timer di intervallo, uso delle risorse. Analisi: media e deviazione standard, analisi multivariata, processi di Markov, serie temporali, modelli operativi.

**Signature detection**: definisce un insieme di **regole o schemi d'attacco** per decidere se un comportamento è quello di un intruso. Approcci:

- **rule-based anomaly detection**: si analizzano gli audit record storici per ricavare il comportamento atteso e lo si confronta con quello attuale;
- **rule-based penetration identification**: regole che identificano penetrazioni e debolezze note, spesso ricavate dagli script d'attacco trovati su Internet e integrate con le regole degli esperti;
- **intelligenza artificiale**.

![[SDC2-L10-033-057.png]]

Gli **audit record**, le registrazioni dell'attività del sistema, possono essere:

- **nativi** (quelli che il sistema già produce): *vantaggio*, non serve software aggiuntivo; *svantaggio*, possono non contenere le informazioni necessarie o non averle in una forma comoda;
- **specifici per il rilevamento**: *vantaggio*, possono essere indipendenti dal produttore e portabili; *svantaggio*, l'overhead di avere in pratica due sistemi di registrazione sulla stessa macchina.

### IDS distribuiti

![[SDC2-L10-034-058.png]]

Un **IDS host-based distribuito**: ogni host (e un monitor della LAN) esegue un **modulo agente** che raccoglie i dati e li invia, attraverso Internet, al **modulo manager** di un gestore centrale, che li correla.

Tecniche di intrusion detection in rete:

- **signature detection** ai livelli applicazione, trasporto e rete: servizi applicativi inattesi, violazioni delle politiche;
- **anomaly detection**: attacchi DoS, scansioni, worm;
- quando rileva una possibile violazione, il sensore invia un **allarme** e registra le informazioni. Queste servono al modulo di analisi per affinare i parametri e gli algoritmi, e all'amministratore per migliorare la protezione.

![[SDC2-L10-034-059.png]]

L'**intrusion detection distribuita adattiva**: gli host e i **PEP** (*policy enforcement point*, i punti in cui si applicano le politiche, come i firewall) si scambiano informazioni direttamente (*gossip*) per la **DDI** (*distributed detection and inference*). Un nodo centrale riceve eventi di riepilogo, eventi delle piattaforme e dei PEP, e invia indietro politiche (di piattaforma, di rete, collaborative) adattate in base ai feedback.

### Honeypot

Gli **honeypot** sono sistemi **esca**, pieni di informazioni fasulle e strumentati con monitor e registratori di eventi. Servono a **distrarre e trattenere** l'attaccante per raccogliere informazioni sulla sua attività, senza esporre i sistemi di produzione. All'inizio erano singoli sistemi, oggi possono essere (o emulare) **intere reti**.

![[SDC2-L10-035-060.png]]

Tre posizioni possibili: (1) **fuori** dal firewall esterno: attira gli attacchi senza aumentare il rischio per la rete interna, ma non rileva gli attaccanti interni; (2) nella **rete dei servizi** (DMZ, con web, mail, DNS): attira chi attacca i servizi pubblici; (3) nella **rete interna**: rileva gli attaccanti che hanno già superato il firewall e quelli interni, ma se viene compromesso è un punto d'accesso alla rete interna.

## Qualità del software e sicurezza

La **qualità e l'affidabilità** del software riguardano i **guasti accidentali** di un programma, causati da input imprevisti teoricamente casuali. Si migliorano con la progettazione strutturata e il **testing**. Conta non quanti bug ci sono, ma **quanto spesso si manifestano**.

La **sicurezza del software** è collegata, ma l'attaccante **sceglie la distribuzione degli input**, mirando proprio al codice bacato da sfruttare. I bug vengono attivati da input molto improbabili, che il testing normale non individua (per questo esiste il *fuzzing*).

(Gli appunti si fermano qui, rimandando alle slide dalla 151 in poi.)
