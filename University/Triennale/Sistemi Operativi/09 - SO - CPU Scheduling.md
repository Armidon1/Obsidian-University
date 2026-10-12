---
title: CPU Scheduling
aliases:
  - SO — Scheduling della CPU
  - Sistemi Operativi — Lezione 9
tags:
  - sistemi-operativi
  - scheduling
  - fcfs
  - sjf
  - round-robin
  - real-time
source: lezione9_cpu_scheduling.docx
---

# CPU Scheduling

> [!abstract] Scopo della lezione
> Nelle lezioni precedenti abbiamo costruito il **meccanismo** del cambio di processo (context switch, code di PCB). Qui si studia la **politica**: *quale* processo pronto deve ricevere la CPU, e per quanto tempo. Si definiscono i criteri per giudicare uno scheduler (utilizzo, throughput, turnaround, waiting, risposta), si analizzano gli algoritmi classici **non preemptive** (FCFS, SJF, priorità) e **preemptive** (Round Robin), le **code multilivello**, lo scheduling **multiprocessore** e **real-time**, e infine i metodi per **valutare** un algoritmo (modelli deterministici, teoria delle code, simulazione).
> Mappa dei concetti: [[MOC - Sistemi Operativi]]

## CPU scheduler

Vedi [[CPU Scheduler e Dispatcher]].

Il **CPU scheduler** sceglie a quale processo, tra quelli nella **coda ready**, assegnare la CPU. Viene invocato quando un processo:

1. passa da **running a waiting** (es. richiesta di I/O, `wait`);
2. **termina**;
3. passa da **running a ready** (es. interrupt del timer);
4. passa da **waiting a ready** (es. fine di un I/O).

Nei sistemi **preemptive** si usano tutte e quattro le occasioni; nei sistemi **non preemptive** solo la 1 e la 2 (vedi gli [[Stati di un Processo]]).

In un sistema **multiprogrammato** lo scheduler viene invocato ogni volta che un programma fa una richiesta di I/O: durante l'I/O la CPU sarebbe inutile per il processo che l'ha richiesto, quindi conviene assegnarla a un altro processo pronto.

- **Scheduler non preemptive**: un processo in esecuzione non viene mai tolto dalla CPU, a meno che non richieda un I/O o termini.
- **Scheduler preemptive**: un processo in esecuzione può essere rimesso nella coda ready anche senza aver richiesto un I/O, se ha consumato l'**unità di tempo** che gli era stata assegnata.

### Dispatcher

Il **dispatcher** è il modulo che **assegna effettivamente la CPU** al processo scelto dallo scheduler (*short-term scheduler*). Il dispatcher:

- passa in **kernel mode** e salva lo stato del processo corrente (**preambolo**);
- passa in **user mode** e ripristina lo stato del nuovo processo (**postambolo**).

È esattamente il preambolo/postambolo visto nel [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Context switch nel kernel|context switch nel kernel]]. Questi switch **costano tempo**: bisogna salvare e ripristinare lo stato della CPU, e dopo uno switch la **cache** non è più valida per il nuovo processo (cache "fredda").

## CPU burst e I/O burst

Vedi [[CPU Burst e IO Burst]].

I programmi utente sono caratterizzati da un'**alternanza** di:

- **CPU burst**: intervallo in cui si usa la CPU (la CPU è il collo di bottiglia, l'I/O riposa);
- **I/O burst**: intervallo in cui si usa l'I/O (l'I/O è il collo di bottiglia, la CPU riposa).

![[SO-L09-01.png]]

È di primaria importanza la **distribuzione della durata dei CPU burst**, che caratterizza il comportamento di un programma rispetto alla CPU. La si può misurare con un **istogramma** durante l'esecuzione.

![[SO-L09-02.png]]

Sull'asse x c'è la durata del burst, sull'asse y quante volte si è osservato un burst di quella durata. La curva tipica ha moltissimi burst **brevi** e pochi burst **lunghi**: la maggior parte dei processi usa la CPU per poco e poi fa I/O.

## Criteri di scheduling

Vedi [[Criteri di Scheduling]].

La scelta del prossimo processo influenza il comportamento di tutto il sistema, che si può misurare con questi indicatori:

| Indicatore | Definizione | Obiettivo |
| --- | --- | --- |
| **Utilizzo della CPU** | frazione di tempo in cui la CPU è occupata | massimizzare |
| **Throughput** | numero di processi completati per unità di tempo | massimizzare |
| **Turnaround time** | tempo per completare un processo (dall'arrivo alla terminazione) | minimizzare |
| **Waiting time** | tempo totale passato dal processo nella **coda ready** | minimizzare |
| **Response time** | tempo tra l'arrivo di una richiesta e l'inizio della risposta | minimizzare |

Per lo scheduler un processo si riassume in:

- il suo **tempo di arrivo**;
- una **lista di azioni**: ognuna è un CPU burst di durata data o un I/O burst su un certo dispositivo, di durata data.

![[SO-L09-03.png]]

![[SO-L09-04.png]]

P1 arriva a T=100 ed è **I/O bound** (burst di CPU cortissimi, I/O lunghissimi); P2 arriva a T=10 ed è **CPU bound** (burst di CPU lunghi, I/O brevi).

Per processi non interattivi l'**I/O asincrono** non viene considerato (in una comunicazione asincrona il mittente invia il messaggio e continua a lavorare senza attendere risposta).

### Diagrammi di Gantt

Il comportamento di uno scheduler su un insieme di processi si illustra con un diagramma: sull'asse x il **tempo**, una riga per ogni risorsa di I/O e una per ogni core (per semplicità: una risorsa I/O e un solo core). Le righe sono colorate con l'id del processo che usa quella risorsa in quell'intervallo. Le latenze di dispatch di solito si trascurano. Per costruire questi diagrammi è comodo usare anche una riga per ogni processo.

Formule utili per un processo con un solo CPU burst:

$$turnaround = t_{fine} - t_{arrivo} \qquad waiting = turnaround - burst$$

## Scheduler non preemptive

### First Come First Served (FCFS)

Vedi [[First Come First Served]].

Si prende il **primo processo della coda ready**. Quando un I/O termina, il processo torna ready e va **in fondo** alla coda. È una semplice coda FIFO.

Esempio:

![[SO-L09-05.png]]

P1 (24), P2 (3), P3 (3) arrivano in quest'ordine. Waiting time: P1 = 0, P2 = 23, P3 = 25 (ognuno aspetta la fine dei precedenti meno il proprio istante di arrivo). Media = (0 + 23 + 25) / 3 = **16**.

Se invece arrivano nell'ordine

![[SO-L09-06.png]]

allora:

![[SO-L09-07.png]]

waiting time: P1 = 6, P2 = 0, P3 = 3; media = **3**. Molto meglio.

**Convoy effect**: con FCFS i processi corti restano bloccati dietro un processo lungo, come le auto dietro un camion. Il waiting time medio dipende fortemente dall'ordine di arrivo.

### Shortest Job First (SJF)

Vedi [[Shortest Job First]].

Si sceglie il processo il cui **prossimo CPU burst è il più corto** (si mantiene la coda ready ordinata per lunghezza del prossimo burst).

- **Vantaggi**: è **ottimale** per il **waiting time medio** (dimostrabile con un argomento di scambio: anticipare un job corto riduce l'attesa di tutti quelli dopo più di quanto aumenti quella del job lungo) e massimizza il throughput.
- **Svantaggi**: richiede di conoscere **in anticipo** la durata dei burst, spesso impossibile nella pratica.

Esempio, tutti i processi arrivano al tempo 0:

![[SO-L09-08.png]]

![[SO-L09-09.png]]

![[SO-L09-10.png]]

Ordine P4 (3), P1 (6), P3 (7), P2 (8). Waiting: P1 = 3, P2 = 16, P3 = 9, P4 = 0. Media = **7** (con FCFS sarebbe (0 + 6 + 14 + 21) / 4 = 10.25).

#### Predire il prossimo burst

SJF si può usare se si ha un modo di **prevedere** il prossimo CPU burst. Un processo tipicamente ha un **comportamento ciclico**: CPU burst di lunghezza simile seguiti da I/O burst di lunghezza simile. Il comportamento può cambiare durante l'esecuzione, ma resta più o meno costante per periodi relativamente lunghi. Esempi:

- un **editor** ha CPU burst brevi e I/O burst lunghi (aspetta la tastiera);
- un **compilatore** ha CPU burst lunghi e I/O burst di media durata (legge dal disco).

**Regola empirica**: il prossimo burst sarà circa lungo quanto quello corrente.

**Problema**: picchi improvvisi nella durata di un burst degradano la qualità della previsione.

**Soluzione**: un **filtro passa basso** (media esponenziale) che smorza i picchi:

![[SO-L09-11.png]]

$$\hat{b}_{t+1} = \alpha\, b_t + (1-\alpha)\, \hat{b}_t$$

- $b_t$: durata **misurata** dell'ultimo burst;
- $\hat{b}_t$: la previsione precedente (che riassume la storia);
- $\alpha \in [0,1]$: **decay coefficient**. Con α = 0 si ignora la misura recente; con α = 1 conta solo l'ultimo burst; tipicamente α = 1/2.

Espandendo la formula, i burst passati pesano $\alpha(1-\alpha)^k$: il peso decade esponenzialmente con l'età.

### Priority scheduling

Vedi [[Priority Scheduling]].

A ogni processo si assegna una **priorità** (un intero `p`; per convenzione un **intero più piccolo = priorità più alta**). Si esegue prima il processo pronto con priorità più alta. SJF è un priority scheduler in cui la priorità è l'inverso della durata del prossimo burst.

- **Problema: starvation**: processi a bassa priorità potrebbero non essere **mai** eseguiti se continuano ad arrivare processi a priorità alta.
- **Soluzione: aging**: la priorità di un processo **aumenta** con il tempo che passa nella coda ready.

Esempio:

![[SO-L09-12.png]]

![[SO-L09-13.png]]

![[SO-L09-14.png]]

P1 parte a 0; a t = 1 arriva P2 con priorità 1 (più alta) e **toglie la CPU** a P1: il diagramma è quello della versione **preemptive**. P2 finisce a 6, P1 riprende fino a 16, poi P3 (16–18) e P4 (18–19).

> [!warning] Verifica dei conti
> Dal diagramma: waiting P1 = 16 − 11 − 0 = 5, P2 = 0, P3 = 18 − 2 − 2 = 14, P4 = 19 − 1 − 3 = 15, quindi la media è 34 / 4 = **8.5**. La slide riporta 8.2; il diagramma di Gantt dà 8.5.

## Scheduler preemptive

Tutti gli schemi precedenti (FCFS, SJF, priorità) si possono rendere **preemptive**. Alla base c'è una routine (attivata dal **timer**) che può riportare un processo da running a ready anche se non ha chiesto un I/O. SJF preemptive si chiama anche **Shortest Remaining Time First**: se arriva un processo con burst più corto del tempo rimanente di quello in esecuzione, lo sostituisce.

A ogni processo si assegna un piccolo intervallo di CPU, il **quanto** *q* (tipicamente 10–100 ms): se allo scadere del quanto il processo sta ancora usando la CPU, viene rimesso nella coda ready.

### Round Robin (RR)

Vedi [[Round Robin]].

Il processo tolto dalla CPU va in **ultima posizione** della coda ready: è un FCFS con preemption a quanto fisso. È quello che abbiamo implementato in [[05 - SO - Stack e Context Switch|lezione 5]] e in [[08 - SO - disastrOS|disastrOS]].

Lo scheduler viene invocato alle richieste di I/O e agli interrupt del timer. Con *N* processi nella coda ready e quanto *q*, **nessun processo aspetta più di (N − 1)·q** prima di ricevere la CPU: c'è una garanzia sul tempo di risposta.

Esempio con q = 4:

![[SO-L09-15.png]]

![[SO-L09-16.png]]

P1 0–4, P2 4–7, P3 7–10, poi P1 fino a 30. Waiting: P1 = 6, P2 = 4, P3 = 7; media ≈ 5.66 (con SJF sarebbe 3, con FCFS 17).

Tipicamente RR ha un **turnaround medio maggiore** di SJF, ma un **tempo di risposta migliore**.

#### Scelta del quanto

Il quanto deve essere **grande rispetto al tempo di context switch** (q tra 10 e 100 ms, context switch < 10 µs). Più piccolo è il quanto, **più context switch** si fanno:

![[SO-L09-17.png]]

Un processo che dura 10 unità: con q = 12 nessun context switch, con q = 6 uno, con q = 1 nove.

- Quanto **troppo piccolo**: si spreca CPU in context switch.
- Quanto **troppo grande**: RR degenera in FCFS.

Di solito si sceglie *q* in modo che circa l'**80% dei CPU burst sia più corto di q**.

La scelta dei parametri da ottimizzare dipende dall'applicazione: i processi **interattivi** (es. editor) vogliono un tempo di risposta molto basso; i processi **batch** (lavori raccolti in gruppo ed eseguiti senza interazione, es. compilare un'applicazione) vogliono massimizzare il throughput. Lo scheduler cerca di ottimizzare i parametri giusti per ogni tipo di applicazione, trattandole in modo diverso.

## Code multilivello

Vedi [[Code Multilivello]].

La coda ready viene **partizionata** in più code, ad esempio **foreground** (processi interattivi) e **background** (processi batch).

- I processi restano **permanentemente** nella propria coda.
- Ogni coda ha il **proprio algoritmo** (es. foreground con RR, background con FCFS).
- Serve anche uno scheduling **tra le code**:
  - **fixed priority**: si servono prima tutti i processi foreground e poi quelli background. Possibile **starvation**.

    ![[SO-L09-18.png]]

    Cinque code in ordine di priorità decrescente: processi di sistema, interattivi, editing interattivo, batch, processi "studente".
  - **time slice**: a ogni coda si assegna una quota del tempo di CPU, che viene poi distribuita tra i suoi processi (es. 80% al foreground con RR, 20% al background con FCFS).

### Code multilivello con feedback

Un processo può **spostarsi da una coda all'altra**: così si implementa l'**aging** e si adatta la priorità al comportamento osservato.

Uno scheduler *multilevel feedback queue* è definito da:

- il numero di code;
- l'algoritmo di scheduling di ogni coda;
- il metodo per decidere quando **promuovere** un processo a una coda più prioritaria;
- il metodo per decidere quando **degradarlo** a una coda meno prioritaria;
- il metodo per decidere in quale coda entra un processo quando ha bisogno di servizio.

![[SO-L09-19.png]]

Un processo che consuma **sempre tutto il suo quanto** (CPU bound) viene **degradato** alla coda a priorità più bassa; un processo che usa **sempre meno** del suo quanto (I/O bound, interattivo) viene **promosso** alla coda a priorità più alta.

> [!warning] Correzione
> Nell'immagine la nota in basso dice "is demoted": l'intenzione (freccia blu verso l'alto) è che il processo venga **promosso** a una coda a priorità più alta.

## Scheduling multiprocessore

Vedi [[Scheduling Multiprocessore]].

Ci sono più CPU disponibili.

- **Processori omogenei**: i processori sono tutti uguali.
- **Multiprocessing asimmetrico**: un **solo processore** accede alle strutture dati del sistema (e fa lo scheduling), gli altri eseguono solo codice utente. Si evita il problema della condivisione dei dati.
- **Multiprocessing simmetrico (SMP)**: ogni processore fa **self-scheduling**; i processori possono avere una coda ready **comune** oppure **ognuno la propria**. È il più usato oggi (vedi [[Symmetric Multiprocessing]]).

**Affinità del processore**: un processo ha "affinità" con il processore su cui sta girando, perché la sua cache contiene i dati del processo; spostarlo su un altro core costa. Può esserci **soft affinity** (l'OS cerca di tenerlo sullo stesso core, ma non lo garantisce) o **hard affinity** (il processo può girare solo su un insieme di core specificato).

## Scheduling real-time

Vedi [[Scheduling Real-Time]].

- **Soft real-time**: nessuna garanzia su **quando** verrà eseguito il processo real-time, solo una preferenza.
- **Hard real-time**: un task **deve** essere servito entro la sua **deadline**; mancarla è un errore.

Due tipi di latenza influenzano le prestazioni:

- **Interrupt latency**: tempo dall'arrivo dell'interrupt all'inizio della routine che lo gestisce (bisogna completare l'istruzione corrente, determinare il tipo di interrupt, salvare il contesto).

  ![[SO-L09-20.png]]

- **Dispatch latency**: tempo che impiega lo scheduler per togliere il processo corrente dalla CPU e far partire un altro.

  ![[SO-L09-21.png]]

  L'intervallo di risposta a un evento è: elaborazione dell'interrupt + dispatch latency (che comprende la fase dei **conflitti**, cioè la preemption dei processi in kernel e il rilascio delle risorse da parte dei processi a bassa priorità, e il **dispatch** vero e proprio) + esecuzione del processo real-time.

### Priority scheduling real-time

- Per il **soft real-time** lo scheduler deve supportare uno scheduling **preemptive basato su priorità**.
- Per l'**hard real-time** deve anche saper **rispettare le deadline**.

Alcuni processi sono **periodici**: richiedono la CPU a intervalli regolari. Un processo periodico è caratterizzato da un tempo di elaborazione *t*, una deadline *d* e un periodo *p*, con

![[SO-L09-22.png]]

$$0 \le t \le d \le p$$

La frequenza del task periodico è $1/p$.

![[SO-L09-23.png]]

In ogni periodo *p* il task deve ricevere *t* unità di CPU entro la deadline *d*.

## Valutazione degli algoritmi

Vedi [[Valutazione degli Algoritmi di Scheduling]].

Come si sceglie un algoritmo di scheduling per un OS? Bisogna prima definire i criteri (es. "massimizzare l'utilizzo con tempo di risposta massimo di 1 s") e poi valutare gli algoritmi.

### Deterministic modeling

Valutazione **analitica**: si prende un **carico di lavoro predeterminato** e si calcolano le prestazioni di ogni algoritmo su quel carico.

Esempio: processi che arrivano tutti all'istante 0:

![[SO-L09-24.png]]

Per ogni algoritmo si calcola il waiting time medio:

![[SO-L09-25.png]]

| Algoritmo | Ordine | Waiting medio |
| --- | --- | --- |
| FCFS | P1, P2, P3, P4, P5 | (0 + 10 + 39 + 42 + 49) / 5 = **28 ms** |
| SJF non preemptive | P3, P4, P1, P5, P2 | (10 + 32 + 0 + 3 + 20) / 5 = **13 ms** |
| RR (q = 10) | P1, P2, P3, P4, P5, P2, P5, P2 | (0 + 32 + 20 + 23 + 40) / 5 = **23 ms** |

Semplice e preciso, ma vale **solo per quel carico**.

### Queuing models

Descrivono gli **arrivi** dei processi nelle code e le **distribuzioni di probabilità** delle durate dei CPU e I/O burst. Il sistema è una **rete di server**, ognuno con la propria coda d'attesa. Si studiano frequenze di arrivo e di servizio, utilizzo, lunghezza media delle code, waiting time medio, …

Si cercano condizioni di **equilibrio**, in cui la frequenza di ingresso nelle code è uguale a quella di uscita.

**Legge di Little**: all'equilibrio il numero di processi che lasciano una coda è uguale a quello che vi arrivano, quindi

![[SO-L09-26.png]]

![[SO-L09-27.png]]

$$n = \lambda \cdot W$$

con *n* = lunghezza media della coda, *W* = tempo medio di attesa in coda, λ = frequenza media di arrivo.

Esempio: se arrivano in media 7 processi al secondo e in coda ce ne sono 14, il waiting time medio è W = n / λ = 14 / 7 = **2 s**.

I queuing models sono **limitati**: le distribuzioni devono essere matematicamente trattabili e spesso non rappresentano bene i carichi reali.

### Simulazioni

Sono più **accurate**: si programma un **modello** del sistema, il clock è una variabile, si raccolgono statistiche sulle prestazioni degli algoritmi. I dati che guidano la simulazione possono essere generati casualmente oppure presi da **tracce** di esecuzioni reali.

![[SO-L09-28.png]]

L'esecuzione reale dei processi produce un **trace tape** (sequenza di CPU e I/O burst), che viene dato in input a simulazioni di FCFS, SJF e RR (q = 14), ottenendo statistiche confrontabili sullo **stesso carico reale**.
