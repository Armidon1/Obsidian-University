---
title: Gestione della Memoria
aliases:
  - SO — Memoria principale
  - Sistemi Operativi — Lezione 10
tags:
  - sistemi-operativi
  - memoria
  - mmu
  - paging
  - segmentazione
  - tlb
  - swapping
source: lezione10_memory.docx
---

# Gestione della Memoria

> [!abstract] Scopo della lezione
> Più processi devono convivere nella stessa RAM senza potersi leggere o sporcare la memoria a vicenda, e senza sapere in anticipo **dove** verranno caricati. La lezione segue il percorso di un programma da file su disco a immagine in memoria (**loader**, **ELF**, **address binding**, **linking statico e dinamico**), introduce la distinzione tra **indirizzo logico e fisico** e la **MMU**, e poi presenta le tecniche hardware per tradurre e proteggere gli indirizzi: registri **base/limit**, **allocazione contigua**, **segmentazione** e infine **paging** con **TLB** e page table **gerarchiche**, con gli esempi reali di **IA-32** e **ARM**. Chiude lo **swapping**.
> Mappa dei concetti: [[MOC - Sistemi Operativi]]

## Memoria principale e CPU

- La **memoria principale** e i **registri** sono le uniche memorie a cui la CPU può accedere **direttamente**.
- Un'unità di memoria vede solo un **flusso di indirizzi** accompagnati da una richiesta di lettura, o di scrittura con il dato da scrivere. Non sa *chi* chiede né *perché*.
- L'accesso a un **registro** richiede un ciclo di clock (o meno).
- L'accesso alla **memoria** è più lento, può richiedere più cicli e causa uno **stallo** (*stall*) della CPU.
- La **cache** sta tra la memoria principale e i registri e riduce gli stalli.
- Negli OS moderni è fondamentale la **protezione** della memoria principale (realizzata con la memoria virtuale), per garantire il corretto funzionamento.

Ricordiamo l'immagine di memoria di un processo ([[Immagine di Memoria di un Processo]], vista in [[05 - SO - Stack e Context Switch#Processo e contesto|lezione 5]]):

![[SO-L10-01.jpeg]]

## Dal program file al processo

La memoria serve a caricarci un **program file**. Quando si avvia un programma dal disco con `exec` ([[exec e Variabili d'Ambiente]]) avvengono diverse azioni:

1. l'**header** del program file viene decodificato, e se ne estraggono le informazioni sui **segmenti** (`.text`, `.data`, `.bss`) e sulle **librerie dinamiche** richieste;
2. il **dynamic linker** carica le librerie dinamiche dai rispettivi file, le decodifica e le mappa nello spazio del programma;
3. si risolvono i **riferimenti pendenti** (simboli usati nel programma ma definiti nelle librerie); la procedura può essere ricorsiva, perché anche le librerie dipendono da altre librerie;
4. gli indirizzi usati dal programma potrebbero dover essere adattati al **layout di memoria reale**.

Vedi [[Loader ed ELF]].

Il **loader** è il modulo del kernel che carica dal file eseguibile, nella regione `.text` dell'immagine del processo, il codice macchina del programma. Si occupa anche di caricare dinamicamente le librerie.

I programmi eseguibili sono memorizzati su disco come file binari in formato **ELF** (*Executable and Linkable Format*), che contengono tutte le informazioni per caricare un'immagine di programma in memoria.

![[SO-L10-02.png]]

Un file ELF è composto da:

- l'**ELF header** (tipo di file, architettura, entry point, dove si trovano le tabelle);
- la **program header table**, che descrive i **segmenti** da caricare in memoria (usata dal **loader** a runtime);
- le **sezioni**: `.text`, `.rodata`, …, `.data`;
- la **section header table**, che descrive le **sezioni** (usata dal **linker** e dai debugger).

Un programma su disco, portato in memoria per essere eseguito, forma una **coda di input**. Senza supporto hardware verrebbe caricato all'indirizzo `0000`, ma è scomodo che il primo processo utente stia proprio all'indirizzo fisico 0.

## Address binding

Vedi [[Address Binding]].

L'**address binding** associa un'istruzione o un dato del programma a una **locazione di memoria**. Gli indirizzi cambiano rappresentazione nelle varie fasi di vita del programma:

- nel **codice sorgente** gli indirizzi sono **simbolici** (nomi di variabili e funzioni);
- nel **codice compilato** (object file) sono legati a indirizzi **rilocabili** (etichette, es. "14 byte dall'inizio di questo modulo");
- il **linker o il loader** lega gli indirizzi rilocabili a indirizzi **assoluti**;
- ogni binding mappa uno spazio di indirizzi su un altro.

Fasi:

| Fase | Indirizzi |
| --- | --- |
| **source** | simbolici |
| **object file** | etichette |
| **load time** | le etichette vengono riempite con indirizzi reali |
| **execution time** | le etichette vengono riempite con indirizzi forniti dai moduli caricati |

![[SO-L10-03.png]]

(La stessa figura della [[02 - SO - Programmi, Makefile e pkg-config#Program file e processo|lezione 2]]: compile time, load time, execution time.)

Il binding di istruzioni e dati a indirizzi **fisici** può avvenire in 3 momenti:

- **a tempo di compilazione**: se la posizione in memoria è nota a priori si genera **codice assoluto**. Se la posizione iniziale cambia, bisogna **ricompilare**.
- **a tempo di caricamento (load)**: se la posizione non è nota a compile time, bisogna generare **codice rilocabile**; il binding avviene quando il programma viene caricato.
- **a tempo di esecuzione**: il binding viene rimandato al **run time** se il processo può essere **spostato** da un segmento di memoria a un altro durante l'esecuzione. Serve **supporto hardware** (la MMU).

## Linking statico e dinamico

Vedi [[Linking Statico e Dinamico]].

Il **linker** prende vari object file e li collega in un unico eseguibile.

- **Static linking**: le librerie di sistema e il codice del programma vengono combinati nell'immagine binaria del programma. Ogni eseguibile ha una propria copia delle librerie.
- **Dynamic linking**: il collegamento viene rimandato al **tempo di esecuzione**.
  - Nel codice si inserisce uno **stub**: un piccolo pezzo di codice che sa come **trovare la routine di libreria** residente in memoria.
  - Lo stub **sostituisce sé stesso** con l'indirizzo della routine e la esegue (le chiamate successive vanno direttamente alla routine).
  - L'OS controlla che la routine sia nello spazio di indirizzi del processo; se non c'è, la aggiunge.
  - È particolarmente utile per le librerie, dette **shared libraries** (`.so`): una sola copia in memoria condivisa da tutti i processi, e aggiornarla non richiede di ricompilare i programmi.

## Problemi dell'allocazione della memoria

Con l'**allocazione** si partiziona la memoria per dare a ogni processo ciò di cui ha bisogno. Problemi:

- il fabbisogno di memoria **varia** durante la vita del processo (si caricano/scaricano moduli, lo heap cresce);
- **frammentazione** ([[Frammentazione]]);
- **protezione**: un processo utente non deve poter leggere/scrivere memoria che non gli appartiene, né eseguire codice in aree non eseguibili.

Vediamo diverse tecniche **hardware** per risolvere questi problemi. Oggi si usa soprattutto il **paging**; il resto è in gran parte obsoleto, ma serve a capire perché il paging è fatto così.

### Registri base e limit

Come garantire che un programma non legga/scriva lo spazio di indirizzi di un altro, né la memoria del kernel?

Si delimita la regione del programma con un **inizio** (**base**) e una **dimensione** (**limit**). Ogni volta che la CPU genera un indirizzo, l'hardware verifica che appartenga alla regione; se non vi appartiene genera un'**eccezione**.

![[SO-L10-04.png]]

Il processo occupa gli indirizzi da 300040 (base) a 300040 + 120900 = 420940 (limit).

## Indirizzi logici e fisici, MMU

Vedi [[MMU]].

- **Indirizzo logico (virtuale)**: indirizzo generato dalla **CPU**.
- **Indirizzo fisico**: indirizzo visto dalla **RAM**.

Indirizzi logici e fisici **coincidono** con il binding a compile time e a load time, ma **differiscono** con il binding a execution time.

- **Spazio degli indirizzi logici**: l'insieme degli indirizzi logici generati da un programma.
- **Spazio degli indirizzi fisici**: l'insieme degli indirizzi fisici corrispondenti.

La **Memory Management Unit (MMU)** è il dispositivo hardware che **mappa gli indirizzi logici su quelli fisici a tempo di esecuzione**.

![[SO-L10-05.png]]

La CPU emette indirizzi logici; la MMU li traduce in indirizzi fisici e, se l'indirizzo non è valido, solleva un'**eccezione** verso la CPU.

- La CPU **non conosce gli indirizzi fisici**: può solo **configurare** la MMU (e solo in modalità privilegiata, vedi [[Dual Mode]]). Questo risolve il problema della **protezione**.
- Configurazioni diverse della MMU producono indirizzi fisici diversi dallo stesso indirizzo logico: per questo tutti i processi possono avere la stessa immagine di memoria.

### MMU con registri relocation e limit

I due registri **relocation** e **limit** definiscono lo spazio logico e servono a calcolare l'indirizzo fisico: l'hardware controlla che l'indirizzo logico sia **minore di limit**, poi gli **somma relocation** ottenendo l'indirizzo fisico.

![[SO-L10-06.png]]

Il registro di rilocazione (base) contiene il **più piccolo indirizzo fisico** del processo. Se l'indirizzo è ≥ limit, si ha una trap (*addressing error*).

La MMU mappa gli indirizzi **dinamicamente**, a tempo di esecuzione: questo permette al codice del kernel di essere effimero (caricare/scaricare moduli) e al kernel di cambiare dimensione, e permette di spostare un processo cambiando solo il registro di rilocazione.

## Allocazione contigua: partizioni multiple

Vedi [[Allocazione Contigua]].

**Multiple partition allocation**: la memoria è divisa in **partizioni**, ognuna delle quali contiene un processo. A ogni processo si dà un **intervallo contiguo** di indirizzi; quando il programma termina la sua partizione viene liberata. Il numero di programmi caricabili è limitato dalla dimensione della memoria, e la memoria di cui ha bisogno ogni programma può cambiare.

Problemi:

- **frammentazione interna**: memoria non usata **dentro** una partizione assegnata (la partizione è più grande del necessario);
- **frammentazione esterna**: in totale c'è abbastanza memoria libera, ma **non contigua**, per ospitare un nuovo processo.

In quale "buco" libero mettere un processo?

- **First-fit**: il **primo** buco abbastanza grande;
- **Best-fit**: il buco **più piccolo** tra quelli abbastanza grandi (lascia il residuo più piccolo);
- **Worst-fit**: il buco **più grande** (lascia il residuo più grande, sperando che sia ancora utile).

First-fit e best-fit sono migliori di worst-fit sia in **velocità** che in **utilizzo dello spazio**; first-fit è di solito il più veloce.

![[SO-L10-07.png]]

La frammentazione esterna si riduce con la **compattazione**: si spostano le partizioni per riunire tutta la memoria libera in un unico grande blocco.

![[SO-L10-08.png]]

La compattazione è possibile solo se la rilocazione è **dinamica** e avviene a **tempo di esecuzione** (basta aggiornare i registri di rilocazione dei processi spostati). È comunque costosa, perché bisogna copiare la memoria.

## Segmentazione

Vedi [[Segmentazione]].

I primi processori avevano **spazi di indirizzi più grandi dei loro registri** (es. 8086: registri a 16 bit, indirizzi fisici a 20 bit). Come si accede a più RAM di quanta un registro possa indirizzare?

Con la **segmentazione** lo spazio logico del programma viene diviso in **segmenti** (codice, dati, stack, …), ognuno con una propria dimensione. L'indirizzo di un oggetto dipende dal **numero del segmento** che lo contiene e dall'**offset** (distanza dall'inizio del segmento):

$$\text{indirizzo logico} = (\text{NumSegmento}, \text{Offset})$$

Per ottenere l'indirizzo fisico si prende l'indirizzo d'inizio del segmento fisico e gli si somma l'offset.

All'inizio si usava un **registro di segmento** esterno, che conteneva i bit alti dell'indirizzo d'inizio del segmento. L'8086 calcolava l'indirizzo fisico come `segment * 16 + offset` (cioè registro di segmento shiftato di 4 bit più l'offset).

Lo schema è stato poi migliorato spostando le informazioni sui segmenti in RAM, nella **segment table**: una tabella che contiene, per ogni processo, le informazioni sui suoi segmenti logici e serve a tradurre gli indirizzi logici in fisici.

Con una memoria virtuale segmentata si caricano in memoria solo i segmenti che servono, il che permette di avere più segmenti. Ogni entry della segment table contiene:

- **validation bit**: dice se il segmento è caricato in memoria (0 = non valido);
- **base**: indirizzo fisico di inizio del segmento;
- **limit**: dimensione del segmento;
- **privilegi** di read/write/execute (bit di protezione).

Segmenti diversi possono avere **permessi diversi**: la memoria si organizza in modo più vicino al layout logico del programma (codice eseguibile e non scrivibile, dati scrivibili e non eseguibili…). Durante la vita di un programma i segmenti cambiano raramente.

![[SO-L10-09.png]]

La CPU genera un indirizzo logico (*s*, *d*). *s* indicizza la segment table, da cui si leggono limit e base. Se *d* < limit, l'indirizzo fisico è **base + d**; altrimenti si ha una trap (*addressing error*).

- **Segment-table base register (STBR)**: punta alla segment table in memoria.
- **Segment-table length register (STLR)**: indica il numero di segmenti usati dal programma (un numero di segmento *s* è valido se *s* < STLR).

Il difetto della segmentazione: i segmenti hanno dimensione variabile, quindi resta il problema della **frammentazione esterna**.

## Paging

Vedi [[Paging]].

Con la **paginazione** la memoria **logica** viene divisa in blocchi della stessa dimensione, le **pagine**, e la memoria **fisica** in blocchi della stessa dimensione, i **frame**. Qualunque pagina può andare in qualunque frame: lo spazio fisico di un processo **non deve essere contiguo**.

La **page table** traduce gli indirizzi logici in fisici: per ogni indice di pagina dice qual è l'indice del frame che ne contiene i dati. **Ogni processo ha la propria page table.**

Un indirizzo logico è diviso in due parti:

- **page number (p)**: indice della pagina che contiene l'indirizzo (bit alti);
- **page offset (d)**: distanza in byte dall'inizio della pagina (bit bassi).

L'indirizzo fisico è diviso in:

- **f**: indice del frame;
- **d**: lo stesso offset.

![[SO-L10-10.png]]

Si usa *p* come indice nella page table, si legge *f*, e l'indirizzo fisico è *f* concatenato a *d*. Con pagine di 2ⁿ byte e indirizzi logici di *m* bit: *d* sono gli *n* bit bassi, *p* gli *m − n* bit alti.

> [!example] Esempio
> Pagine da 4 KB (2¹²), indirizzi a 32 bit: offset = 12 bit, page number = 20 bit, quindi 2²⁰ pagine. L'indirizzo logico `0x00003ABC` ha p = `0x3`, d = `0xABC`. Se la page table dice che la pagina 3 sta nel frame 7, l'indirizzo fisico è `0x00007ABC`.

La page table sta in **memoria centrale**.

- **Page-table base register (PTBR)**: punta alla page table. A ogni context switch basta cambiare il PTBR per cambiare spazio di indirizzi.
- **Page-table length register (PTLR)**: indica la dimensione della page table.

Con questo schema **ogni accesso ai dati richiede due accessi in memoria**: uno alla page table e uno al dato. Il problema si risolve con una cache hardware speciale ad accesso veloce: la **memoria associativa** o **TLB**.

- **Vantaggi**: **nessuna frammentazione esterna** (qualunque frame libero va bene).
- **Svantaggi**: **frammentazione interna** nell'ultima pagina di ogni processo (minore con pagine più piccole); accessi a memoria più lenti (doppio accesso, mitigato dalla TLB); spazio aggiuntivo per la page table (maggiore con pagine più piccole). La dimensione delle pagine è quindi un compromesso.

> [!warning] Correzione
> Negli appunti tra gli svantaggi compare "frammentazione esterna": è la frammentazione **interna** (lo spazio non usato nell'ultima pagina).

## TLB

Vedi [[TLB]].

Il **Translation Lookaside Buffer (TLB)** è una **memoria associativa**: una memoria capace di cercare una chiave **in parallelo** su tutti gli elementi, ad alta velocità.

- Fa da **cache** per le entry della page table (coppie pagina → frame).
- È **più veloce della RAM**, ma contiene un numero **limitato** di elementi (decine o poche centinaia).
- Rende **molto probabile** che la traduzione di una pagina sia rapidissima, grazie al principio di località.

Quando la CPU accede a un indirizzo logico:

1. cerca la pagina nella TLB;
2. **TLB hit**: ricava il frame dalla TLB, senza accedere alla page table;
3. **TLB miss**: consulta la page table in memoria e inserisce la traduzione nella TLB, sostituendo un elemento vecchio.

![[SO-L10-11.png]]

A ogni context switch la TLB va **svuotata** (o le sue entry vanno etichettate con un identificatore del processo, *ASID*), altrimenti il nuovo processo userebbe le traduzioni del vecchio.

## Protezione con il paging

- A ogni frame è associato un **bit di protezione** che indica i permessi (read-only o read-write); si possono aggiungere altri bit (es. execute-only).
- A ogni entry della page table è associato un **bit di validità** (*valid-invalid bit*): *valid* se la pagina appartiene allo spazio logico del processo, *invalid* altrimenti. Un accesso a una pagina invalida genera una trap.
- In alternativa si può usare il PTLR per sapere quante entry sono valide.

![[SO-L10-12.png]]

Le pagine 0–5 sono valide (mappate sui frame 2, 3, 4, 7, 8, 9); le pagine 6 e 7 sono invalide: non fanno parte dello spazio del processo.

## Pagine condivise

**Shared code**: una copia **read-only** di codice condiviso viene condivisa tra più processi. Il codice deve essere **rientrante** (*reentrant*): progettato in modo che una sola copia in memoria possa essere eseguita contemporaneamente da più utenti/processi (non modifica sé stesso e tiene i dati di ogni esecuzione separati).

![[SO-L10-13.png]]

Tre processi eseguono lo stesso editor (pagine `ed 1`, `ed 2`, `ed 3`): le loro page table mappano quelle pagine sugli **stessi frame** (3, 4, 6), mentre ognuno ha la propria pagina di dati (`data 1` → frame 1, `data 2` → frame 7, `data 3` → frame 2). In memoria c'è una sola copia dell'editor.

- È concettualmente simile a più thread che condividono lo stesso spazio di indirizzi.
- Se si permette la condivisione di pagine **read-write**, la condivisione serve anche per la **comunicazione tra processi** (memoria condivisa).

**Private code and data**: ogni processo ha una copia separata del proprio codice e dei propri dati. Le pagine private possono stare in qualunque punto dello spazio logico.

## Effective Access Time

Vedi [[Effective Access Time]].

L'**Effective Access Time (EAT)** è il tempo **atteso** di un'operazione di memoria, tenendo conto della TLB.

![[SO-L10-14.png]]

$$EAT = \alpha\,(T_{ram} + T_{tlb}) + (1-\alpha)\cdot 2\,(T_{ram} + T_{tlb})$$

con

![[SO-L10-15.png]]

α = **hit ratio**: la percentuale di volte in cui la pagina viene trovata nella TLB (negli *associative registers*). L'hit ratio dipende dal numero di entry della TLB.

> [!note] Formula più precisa
> In caso di hit si fa un accesso alla TLB e uno alla RAM; in caso di miss si fa un accesso alla TLB, uno alla page table e uno al dato:
> $$EAT = \alpha\,(T_{tlb} + T_{ram}) + (1-\alpha)\,(T_{tlb} + 2\,T_{ram})$$
> Esempio: $T_{ram}$ = 100 ns, $T_{tlb}$ = 20 ns, α = 0.8: EAT = 0.8·120 + 0.2·220 = **140 ns** (40% in più rispetto a un accesso diretto). Con α = 0.99: EAT = 121 ns.

## Page table gerarchica

Vedi [[Page Table Gerarchica]].

Con indirizzi a 32 bit e pagine da 4 KB la page table ha 2²⁰ entry (4 MB per processo!), e la maggior parte sarebbe inutilizzata. Soluzione: **paginare la page table stessa**. La versione più semplice è a **due livelli**.

![[SO-L10-16.png]]

L'indirizzo logico si divide in *p₁* (indice nella **outer page table**), *p₂* (indice nella pagina della page table selezionata) e *d* (offset). La outer page table punta alle pagine della page table, che puntano ai frame. Le pagine della page table relative a zone non usate dello spazio logico **non vengono allocate**.

- **Vantaggi**: la page table può essere molto più grande senza occupare memoria contigua, e si allocano solo le parti necessarie.
- **Svantaggi**: aumenta l'EAT: in caso di TLB miss servono **più accessi** in memoria (uno per livello).

## IA-32

In **IA-32** (architettura Intel a 32 bit) si usa una **combinazione di segmentazione e paging**. La CPU genera un **indirizzo logico**, che passa alla **segmentation unit**, che produce un **indirizzo lineare**; questo passa alla **paging unit** a due livelli (l'equivalente della MMU), che genera l'**indirizzo fisico**.

![[SO-L10-17.png]]

Le pagine possono essere da **4 KB** o da **4 MB**.

![[SO-L10-18.png]]

- **Segmentazione**: l'indirizzo logico è (*selector*, *offset*). Il selector indica il segmento e seleziona un **segment descriptor** nella *descriptor table* (la segment table), che contiene la **base** del segmento. Indirizzo lineare = base + offset.
- **Paging**: l'indirizzo lineare a 32 bit è diviso in *p₁* (10 bit, indice nella **page directory**, la outer page table, puntata dal registro **CR3**), *p₂* (10 bit, indice nella **page table**) e *d* (12 bit, offset in una pagina da 4 KB).
- Per le pagine da **4 MB** la page directory punta direttamente alla pagina e l'offset è di 22 bit.

## ARM

Nell'architettura **ARM** a 32 bit le pagine sono da **4 KB** e **16 KB**, e ci sono pagine da **1 MB** e **16 MB** chiamate **sezioni**. Si usa paging a **un livello** per le sezioni e a **due livelli** per le pagine più piccole.

![[SO-L10-19.png]]

L'indirizzo è diviso in *outer page*, *inner page* e *offset*: per le pagine piccole si attraversano i due livelli, per le sezioni basta la outer page table.

Ci sono **due livelli di TLB**: il livello più esterno ha **due micro TLB** (uno per i dati e uno per le istruzioni), quello interno è una TLB **principale** unica. Si controlla prima la micro TLB, poi quella principale; se entrambe mancano si consulta la page table.

## Swapping

Vedi [[Swapping]].

Lo **swapping** sposta temporaneamente un processo **fuori dalla memoria**, su un **backing store**, e lo riporta in memoria più tardi per continuare l'esecuzione. Così lo spazio fisico totale dei processi **può superare** la RAM disponibile.

Il **backing store** è un disco veloce, abbastanza grande da contenere copie delle immagini di memoria di tutti i processi di tutti gli utenti.

![[SO-L10-20.png]]

- **Roll out, roll in**: variante dello swapping per algoritmi di scheduling a priorità: si spostano fuori per primi i processi a **priorità più bassa**, per far posto a quelli più importanti.
- Gran parte del tempo di swapping è tempo di **trasferimento**, proporzionale alla quantità di memoria spostata.
- Il sistema tiene una **coda ready** di processi le cui immagini di memoria sono sul disco.
- Un processo portato fuori deve tornare **allo stesso indirizzo fisico**? Dipende dal metodo di address binding (con binding a execution time no). Bisogna anche considerare gli **I/O pendenti** verso o dalla memoria del processo.
- Nei sistemi operativi moderni lo swapping è normalmente **disattivato**: si attiva quando la memoria allocata supera una **soglia** (*threshold*) e si disattiva quando torna sotto.

Se al context switch il processo da eseguire **non è in memoria**, bisogna fare swap-in, ed eventualmente swap-out di un altro processo: il tempo di context switch può diventare **molto alto**. Si riduce un po' se si sa quanta memoria il processo usa davvero (si sposta solo quella).

Altri limiti:

- non si può portare fuori un processo **in attesa di I/O**, altrimenti l'I/O verrebbe consegnato nella memoria sbagliata. Soluzione: consegnare sempre gli I/O in buffer del **kernel** e poi copiarli al processo (**double buffering**), che però aggiunge overhead.

Lo swapping **standard** (di processi interi) non si usa negli OS moderni, ma sono comuni versioni **modificate**: si swappano **singole pagine** invece di interi processi. È la base della **memoria virtuale** con demand paging: [[11 - SO - Memoria Virtuale|lezione 11]].
