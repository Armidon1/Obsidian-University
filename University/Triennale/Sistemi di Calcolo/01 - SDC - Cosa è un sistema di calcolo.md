---
title: Cosa è un sistema di calcolo
aliases:
  - SDC — Cosa è un sistema di calcolo
  - Sistemi di Calcolo — Capitolo 1
tags:
  - sistemi-di-calcolo
  - hardware
  - porte-logiche
  - sistema-operativo
source: Dispensa Sistemi di Calcolo.pdf (cap. 1, pp. 9–27)
---

# Cosa è un sistema di calcolo

> [!abstract] Scopo del capitolo
> Il capitolo fissa il vocabolario di tutto il corso. Che cos'è un **sistema di calcolo**; com'è organizzato l'**hardware** (modello di **Von Neumann**, bus, I/O bridge, gerarchia di memoria); come si costruisce una CPU a partire dalle **porte logiche**, passando per i circuiti **combinatori** (addizionatori) e **sequenziali** (flip-flop); e che ruolo ha il **sistema operativo**, con una mappa dell'intero sistema Linux/x86 che il resto della dispensa approfondisce pezzo per pezzo.
> Mappa dei concetti: [[MOC - Sistemi di Calcolo]]

## Sistemi di calcolo

Un **sistema di calcolo** è un insieme di **software** e **hardware** che lavorano insieme per eseguire programmi. Gli esempi sono molto più numerosi di quanto si pensi: smartphone, tablet, PC fissi e portatili, i data center di Facebook, Twitter e Google, i supercomputer del CERN, ma anche smart TV, lettori multimediali, modem/router, fotocamere digitali, computer di bordo delle auto e console per videogiochi.

![[SDC-p009-1.png]]

La figura mostra la varietà di dispositivi che sono a tutti gli effetti sistemi di calcolo: smartwatch, router, laptop, perfino un frigorifero "smart", console, tablet pieghevoli e fotocamere. Ciò che li accomuna non è la forma ma la **programmabilità**.

In generale, un sistema di calcolo è un **sistema programmabile**: può eseguire compiti diversi in base alle istruzioni di un **programma**. Può essere:

- **a singolo nodo**: un insieme di componenti hardware strettamente connessi e fisicamente vicini (PC, smartphone, tablet);
- **multi-nodo**: più nodi collegati da una **rete di comunicazione**. Esempi sono i data center e i supercomputer, i cui nodi sono collegati da reti ad alta velocità come Infiniband. Un sistema di questo tipo si chiama **cluster**.

_(dispensa, p. 9)_

## Hardware

Vedi [[Macchina di Von Neumann]].

Nel corso si considerano sistemi in cui l'hardware dei singoli nodi segue il **modello di Von Neumann**:

![[SDC-p010-1.png]]

- la **memoria centrale** contiene sia i **dati** da elaborare sia i **programmi** (nella stessa memoria: è il punto chiave del modello);
- i **dispositivi di input/output** scambiano dati con il mondo esterno;
- la **CPU** (*Central Processing Unit*) esegue le **istruzioni** del programma.

Più in dettaglio, l'organizzazione tipica di un calcolatore moderno è:

![[SDC-p010-2.png]]

La CPU è collegata tramite il **bus di sistema** all'**I/O bridge**, che a sua volta è collegato alla **memoria centrale (RAM)** tramite il **bus della memoria**. Dall'I/O bridge parte il **bus di I/O**, su cui si affacciano i **controller** e gli **adattatori** dei dispositivi: controller USB (mouse, tastiera), adattatore grafico (schermo), controller del disco. È lo stesso schema, semplificato, dell'architettura Northbridge/Southbridge vista in [[01 - SO - Introduzione e Git#Organizzazione di un computer|Sistemi Operativi]].

_(dispensa, p. 10)_

### Panoramica degli elementi hardware

#### CPU

La **CPU** (o **microprocessore**) è il cuore del sistema. Esegue programmi scritti in **linguaggio macchina** (codice **nativo**), cioè sequenze di byte che codificano istruzioni. Il **set di istruzioni** (l'insieme delle istruzioni che la CPU riconosce) è specifico di una **famiglia** di CPU e può essere molto diverso tra produttori. Esempi di famiglie: **x86** (Intel, AMD), **PowerPC** (Apple-Motorola-IBM), **SPARC** (Sun), **ARM** (ARM Holdings).

Le istruzioni vengono eseguite **nell'ordine in cui compaiono in memoria** e tipicamente:

1. **trasferiscono dati** all'interno della CPU, all'interno della memoria, tra memoria e CPU, o tra dispositivi esterni e CPU;
2. calcolano operatori **aritmetico/logici** (somme, prodotti), **booleani** (congiunzione, disgiunzione, negazione) e **relazionali** (uguale, maggiore, minore). Se ne occupa un modulo della CPU, l'**ALU** (*Arithmetic Logic Unit*);
3. effettuano **salti**: l'esecuzione continua non dall'istruzione successiva ma da un altro punto del programma. Servono a realizzare **cicli** (`for`, `while`) e **selezioni** (`if … else`).

Queste tre categorie (movimento dati, aritmetica/logica, salti) torneranno pari pari nell'assembly IA32: [[03 - SDC - Traduzione dei programmi C in linguaggio macchina|capitolo 3]].

#### Bus

Vedi [[Bus di Sistema]].

I **bus** sono le strutture di interconnessione che collegano i componenti e permettono lo scambio di dati. Trasferiscono i dati a blocchi di dimensione fissa chiamati **word**: tipicamente 4 byte (32 bit) o 8 byte (64 bit), a seconda dell'architettura. La dispensa assume word da **8 byte** (architettura a 64 bit) e che su un bus si trasferisca **una word alla volta**.

#### I/O bridge

Coordina lo scambio dei dati tra la CPU e il resto del sistema (memoria e dispositivi di I/O, non solo questi ultimi).

#### Controller e adattatori

Interfacciano il sistema con il mondo esterno (movimenti del mouse, tasti premuti, …). La differenza:

- i **controller** sono **saldati sulla scheda madre** (il circuito stampato che ospita CPU, memoria e bus) o integrati nel dispositivo esterno;
- gli **adattatori** sono **schede esterne** collegate alla scheda madre (es. scheda video o di rete).

#### Sistema di memoria

Vedi [[Gerarchia di Memoria]].

La CPU non comunica direttamente con la RAM: in mezzo ci sono più livelli di memorie intermedie, le **cache**, che conservano i dati usati più spesso o vicini a quelli usati. Le cache sono molto più veloci della RAM.

![[SDC-p012-1.png]]

La gerarchia, dall'alto verso il basso (costo per byte decrescente, capacità crescente, velocità decrescente):

| Livello | Tempo di accesso | Capacità tipica |
| --- | --- | --- |
| Registri della CPU | < 1 ns | decine/centinaia di byte |
| Cache L1 | ~1 ns | ~64 KB |
| Cache L2 | ~4 ns | ~256 KB |
| Cache L3 | ~16 ns | ~6 MB |
| Memoria centrale | ~100 ns | ~16 GB |
| Disco (memoria virtuale) | ~16 µs (SSD), ~3 ms (magnetico) | terabyte |

Il punto da ricordare è il **rapporto tra i tempi**: un accesso a disco magnetico costa circa **30 milioni** di volte un accesso a registro. Per questo le prestazioni di un programma dipendono molto da *dove* si trovano i dati (cache e località: [[07 - SDC - Gestione dei dati in memoria centrale|capitolo 7]]).

_(dispensa, pp. 11–12)_

## Elementi di base di un microprocessore

### Porte logiche

Vedi [[Porte Logiche]].

Le **porte logiche** realizzano le funzionalità elementari di una CPU: calcolano **funzioni booleane** che associano a uno o più bit di input un bit di output. Le tre principali sono **AND**, **OR** e **NOT**:

![[SDC-p012-2.png]]

Si realizzano con componenti elettronici a **semiconduttore**, i **transistor**. Un transistor ha tre terminali, **collettore**, **base** ed **emettitore**, e funziona come un **interruttore pilotato dall'elettricità**: se la base riceve corrente, si crea un collegamento elettrico tra collettore ed emettitore. Convenzione: **5 V = 1 (true)**, **0 V = 0 (false)**.

#### Porta AND

Vale 1 **se e solo se entrambi** gli input sono 1.

| X | Y | X AND Y |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

*(Figura 1.1.2.2: tabella di verità dell'operatore AND)*

Realizzazione con transistor NPN:

![[SDC-p013-2.png]]

I due transistor sono **in serie**: il LED O si accende solo se **entrambi** gli interruttori I₁ e I₂ sono chiusi, cioè se le basi di entrambi i transistor ricevono corrente. Solo così la corrente può passare dalla resistenza da 220 Ω e dal LED fino a massa. Le resistenze da 10 kΩ limitano la corrente sulle basi.

Demo su breadboard con Arduino come alimentazione:

![[SDC-p014-1.png]]

_(dispensa, pp. 12–14)_

#### Porta OR

Vale 1 **se almeno uno** degli input è 1.

| X | Y | X OR Y |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

*(Figura 1.1.2.5)*

![[SDC-p015-1.png]]

Qui i due transistor sono **in parallelo**: basta che **almeno una** base riceva corrente perché si apra un percorso verso massa e il LED si accenda.

![[SDC-p015-2.png]]

#### Porta NOT

Operatore **unario**: vale 1 se e solo se l'input è 0 (inverte il valore di verità).

| X | NOT X |
| --- | --- |
| 0 | 1 |
| 1 | 0 |

> [!warning] Correzione
> Nella dispensa la didascalia di questa tabella (Figura 1.1.2.8) dice "tabella di verità dell'operatore OR": è la tabella del **NOT**.

![[SDC-p016-2.png]]

Funzionamento: chiudendo l'interruttore la base riceve corrente, quindi il transistor **cortocircuita a massa** la corrente che arriva dalla resistenza da 220 Ω, che non passa più dal LED (spento). Con l'interruttore aperto, la corrente attraversa il LED (acceso). Input 1 → LED spento; input 0 → LED acceso.

![[SDC-p017-1.png]]

_(dispensa, pp. 14–17)_

### Miniaturizzazione e VLSI

I circuiti visti finora usano transistor discreti. Le CPU reali sono costruite con la **VLSI** (*Very Large Scale Integration*), che produce circuiti visibili solo al microscopio.

![[SDC-p017-2.png]]

In alto, due dettagli di chip al microscopio; in basso, un **wafer** di silicio: un disco di semiconduttore che contiene centinaia di chip, che poi vengono ritagliati e diventano circuiti integrati (CPU, memorie). Oggi si arriva a circa **17 milioni di transistor per mm²**, cioè circa **3 miliardi** di transistor in una CPU recente come un Intel Core i7.

_(dispensa, pp. 16–17)_

### Circuiti combinatori

Vedi [[Circuiti Combinatori e Addizionatori]].

Combinando le porte logiche si ottengono **circuiti combinatori**, che realizzano funzioni booleane arbitrarie. Il loro output dipende **solo dal valore attuale degli input**.

Precedenza degli operatori, dalla maggiore alla minore: **NOT, AND, OR**. Quindi `NOT X OR X AND Y` = `(NOT X) OR (X AND Y)`.

#### Esempio: addizionatore parziale (half adder)

Somma due bit e produce **somma** e **riporto**:

| X | Y | somma(X,Y) | riporto(X,Y) |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

*(Figura 1.1.2.12)*

Prendendo le righe in cui l'output vale 1 (forma *somma di prodotti*):

- $somma(X,Y) = \overline{X}\,Y + X\,\overline{Y} = X \oplus Y$ (XOR);
- $riporto(X,Y) = X \cdot Y$ (AND).

![[SDC-p018-2.png]]

Lo **XOR** (OR esclusivo) vale 1 se gli input sono **diversi**:

| X | Y | X XOR Y |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

*(Figura 1.1.2.14)*

Si costruisce con porte di base:

![[SDC-p019-2.png]]

Ogni ramo calcola uno dei due termini, `NOT X AND Y` e `X AND NOT Y`, e una OR li combina; a destra il simbolo compatto della XOR.

> [!warning] Correzione
> Il testo dice che la XOR "può essere realizzata con due porte AND e due NOT": dalla figura servono anche **una porta OR** (2 NOT + 2 AND + 1 OR).

#### Esempio: addizionatore completo (full adder)

Per sommare numeri di più bit serve un addizionatore che prenda in input **anche il riporto R** prodotto dalla cifra precedente:

![[SDC-p019-3.png]]

Il circuito usa due XOR in cascata per la somma ($S = X \oplus Y \oplus R$) e due AND più una OR per il riporto in uscita ($R' = XY + R(X \oplus Y)$). A destra il suo "packaging" come **scatola nera**, con ingressi X, Y, R e uscite S, R'.

| X | Y | R | S | R' |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

*(Figura 1.1.2.17)*

#### Esempio: addizionatore a n bit

Mettendo **in cascata** n addizionatori completi (il riporto in uscita di uno è il riporto in ingresso del successivo) si ottiene un addizionatore a n bit (*ripple-carry adder*):

![[SDC-p020-2.png]]

Per n = 4 calcola $X_3X_2X_1X_0 + Y_3Y_2Y_1Y_0 = S_3S_2S_1S_0$; il primo riporto in ingresso è 0. Il riporto deve propagarsi attraverso tutti gli stadi: è uno dei motivi per cui la velocità di un circuito ha dei limiti fisici.

_(dispensa, pp. 18–20)_

### Logica sequenziale e flip-flop

Vedi [[Flip-Flop SR]].

I **circuiti sequenziali**, a differenza di quelli combinatori, hanno uno **stato**: una memoria degli eventi passati, per cui l'output dipende anche dalla storia degli input. Nei calcolatori la realizzazione tipica è **sincrona**: un **clock** invia impulsi in cui il segnale oscilla tra acceso e spento a una certa frequenza.

Il segnale elettrico si propaga a velocità variabile (dipende anche dalla temperatura; come riferimento servono circa **10 ns per 15 cm** di conduttore metallico), e componenti diversi hanno tempi di propagazione diversi. Per questo, e per la **dissipazione di calore**, la frequenza di clock **non può superare una certa soglia** senza rendere il sistema instabile. (La dispensa assume una frequenza costante; nei processori moderni varia dinamicamente per controllare calore e consumi.)

Il **flip-flop** è un componente fatto di porte logiche che fa da mattoncino per le memorie veloci come i **registri** della CPU. Il più comune è il **flip-flop SR**:

- due ingressi, **S** (*set*) e **R** (*reset*), e due uscite, **Q** e **Q'** (= NOT Q);
- un segnale su S imposta Q = 1, un segnale su R imposta Q = 0;
- se non arriva nessun segnale, il flip-flop **mantiene l'ultimo stato** (è una memoria da 1 bit);
- S e R contemporaneamente → stato **indefinito**;
- di per sé è asincrono, ma pilotato da un oscillatore cambia stato solo durante una pulsazione (sincrono).

Si costruisce con porte **NOR** (una OR con l'uscita negata):

![[SDC-p021-1.png]]

| X | Y | X NOR Y |
| --- | --- | --- |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

Tabella di transizione del flip-flop SR:

| S | R | Q | Q' |
| --- | --- | --- | --- |
| 0 | 0 | stato immutato | |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | indefinito | |

![[SDC-p022-2.png]]

> [!warning] Correzione
> Nella dispensa tre figure diverse (definizione della NOR, tabella della NOR e tabella di transizione del flip-flop) sono tutte numerate **1.1.2.19**.

La stabilità viene dal **feedback**: l'uscita di ogni NOR è un ingresso dell'altra. Esempio: con S = 1 e R = 0, la NOR in basso (ingressi S e Q) dà Q' = 0, perché una NOR dà 1 solo se entrambi gli ingressi sono 0. Allora la NOR in alto ha ingressi R = 0 e Q' = 0, quindi Q = 1. Anche quando S torna a 0, Q' resta 0 (perché Q = 1) e Q resta 1: il bit è **memorizzato**. In letteratura questo dispositivo si chiama **latch**: mantiene lo stato finché non riceve un nuovo set/reset.

_(dispensa, pp. 20–22)_

## Sistema operativo

Vedi [[Sistema Operativo]].

I sistemi più complessi si basano su un **sistema operativo**: il software che permette di eseguire le applicazioni sull'hardware disponibile. La dispensa considera un sistema operativo **Linux su hardware x86**.

### Compiti

- **gestione dei processi**, cioè dei programmi in esecuzione (creazione, eliminazione, assegnazione del tempo di CPU);
- **allocazione delle risorse** ai processi: RAM, dischi, connessioni di rete;
- **misurazione e gestione del tempo** (orologio, timer);
- **gestione delle utenze**: più utenti, con privilegi di accesso alle risorse;
- **comunicazione tra processi**, sulla stessa macchina o in rete;
- **gestione degli errori** dei processi e del sistema;
- **protezione e sicurezza**: isolare i processi perché non interferiscano tra loro, con il sistema operativo o con l'hardware (per malizia o per bug).

### Obiettivi di progettazione

- **multitasking**: più applicazioni in esecuzione contemporaneamente;
- **preemption**: poter togliere la CPU a un processo per darla a un altro;
- **progresso e assenza di starvation**: ogni processo riceve periodicamente la CPU e quindi avanza;
- **alto throughput**: massimizzare le istruzioni eseguite nell'unità di tempo;
- **bassa latenza**: minimizzare il tempo delle singole operazioni del sistema, cruciale nei sistemi **real-time** (es. il software che decide l'apertura di un airbag).

Questi obiettivi sono in tensione tra loro (throughput vs latenza): il loro bilanciamento è il tema dello scheduling, studiato in [[09 - SO - CPU Scheduling|Sistemi Operativi]].

_(dispensa, pp. 22–23)_

### Panoramica del funzionamento

![[SDC-p024-1.png]]

La figura è la "mappa" dell'intera dispensa, dall'alto (applicazioni) verso il basso (hardware). Ogni blocco verrà ripreso in un capitolo:

1. **Processi**: in alto c'è il programma C in esecuzione. Può usare le **librerie** (es. la libc: `printf`, `malloc`, `strlen`) oppure chiedere servizi al sistema operativo tramite **funzioni wrapper** delle **system call** POSIX (`open`, `fork`, `read`, …), che passano il controllo al kernel. Alcune funzioni di libreria usano a loro volta system call (`printf`), altre no (`strlen`). Lo standard **POSIX** (edizione 2017, oltre 400 funzioni) comprende le system call e la libreria standard C (ISO C). → [[04 - SDC - Librerie standard del C|capitolo 4]]
2. **ABI** (*Application Binary Interface*): l'insieme di convenzioni che programmi e librerie rispettano, ad esempio come si passano i parametri a una funzione e come si restituisce un valore. → [[03 - SDC - Traduzione dei programmi C in linguaggio macchina#Funzioni|capitolo 3]]
3. **ISA** (*Instruction Set Architecture*): definisce lo stato della CPU, le sue istruzioni e il loro effetto sullo stato. Vedi [[ABI e ISA]].
4. **Modalità utente e supervisore**: i programmi girano in **modalità utente**, con privilegi ridotti; quando eseguono codice del sistema operativo tramite una system call passano in **modalità supervisore** (o kernel), con il pieno controllo della macchina. Vedi [[Dual Mode]].
5. **Interrupt**: il passaggio del controllo al **kernel** (nucleo) avviene con il meccanismo degli **interrupt**, eventi che interrompono il flusso del programma, passano il controllo al sistema operativo e alzano i privilegi. Possono essere generati dalla CPU stessa (istruzione `INT` su x86, oppure una condizione di errore) o da eventi esterni (un tasto premuto). Vedi [[Interrupt]] e [[System Call]].
6. **Moduli del kernel**, attivati tramite interrupt:
   - **esecuzione dei processi**: caricamento dei programmi (*loading*), scheduling, gestione degli interrupt, **Process Control Block** ([[Process Control Block]]), **segnali** (notifiche di eventi tra processi e tra kernel e processi). → [[06 - SDC - Esecuzione dei programmi|capitolo 6]]
   - **gestione della memoria**: **virtualizzazione** della memoria, per cui ogni processo vede uno spazio suo e non può accedere a quello di un altro senza permesso. Si basa sulla separazione tra **memoria fisica** e **memoria logica**. Comprende anche l'allocazione dello spazio logico (`malloc`/`free`). → [[07 - SDC - Gestione dei dati in memoria centrale|capitolo 7]]
   - **file e I/O**: soddisfa le richieste di uso di dischi e dispositivi. Fondamentali i **driver**, che offrono al kernel un'interfaccia standard astraendo i dettagli dei dispositivi e possono essere installati e aggiornati separatamente. → [[08 - SDC - Gestione dei file|capitolo 8]]
   - **tempo**: misura del tempo reale e del tempo di CPU di ogni processo. → [[05 - SDC - Ottimizzazione dei programmi#Profilazione delle prestazioni|capitolo 5]]
7. **Uso dell'hardware**: un programma in modalità utente usa la **CPU direttamente**, senza passare dal sistema operativo; **ogni altra interazione** con l'hardware è mediata dal sistema operativo.

_(dispensa, pp. 23–25)_

## Domande riepilogative

La dispensa propone domande vero/falso. Ecco le risposte con una breve motivazione.

> [!question]- Risposte (clicca per espandere)
> 1. **Vero**: un router è programmabile.
> 2. **Falso**: in Von Neumann programmi e dati condividono la stessa memoria.
> 3. **Vero**.
> 4. **Falso**: l'ALU è **dentro** la CPU.
> 5. **Falso**: coordina gli scambi tra la CPU e tutto il resto del sistema, memoria compresa.
> 6. **Falso**: gli adattatori sono schede esterne; quelli saldati sono i controller.
> 7. **Vero**.
> 8. **Falso**: è il contrario, le porte logiche sono costruite con i transistor.
> 9. **Vero**.
> 10. **Vero** (vedi Figura 1.1.2.15).
> 11. **Vero**: tutte corrette.
> 12. **Falso**: nei circuiti digitali sono usati come interruttori.
> 13. **Vero**: anzi, miliardi.
> 14. **Vero**.
> 15. **Vero**.
> 16. **Falso**: la differenza è che hanno uno **stato**.
> 17. **Falso**: è sequenziale.
> 18. **Vero** (addizionatore parziale).
> 19. **Vero**.
> 20. **Falso**: limiti di propagazione e calore.
> 21. **Falso**: due ingressi (S, R) e due uscite (Q, Q').
> 22. **Vero** negli stati validi (Q' = NOT Q); con S = R = 1 lo stato è indefinito.
> 23. **Vero**.
> 24. **Falso**: un processo è un programma **in esecuzione**.
> 25. **Falso**.
> 26. **Falso**: è mediata dal sistema operativo.
> 27. **Vero**.
> 28. **Vero**.
> 29. **Falso**: il progresso riguarda l'avanzamento della computazione, non l'I/O.
> 30. **Vero**: direttamente (con l'istruzione apposita) o tramite una funzione di libreria.
> 31. **Falso**: quella è la definizione di **ISA**.
> 32. **Vero**.
> 33. **Falso**: anche la CPU può generarli (`INT`, eccezioni).
> 34. **Vero**.

_(dispensa, pp. 26–27)_
