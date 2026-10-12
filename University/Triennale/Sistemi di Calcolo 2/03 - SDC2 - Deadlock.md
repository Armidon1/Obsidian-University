---
title: Deadlock
aliases:
  - SDC2 — Deadlock and starvation, more on mutual exclusion
  - Sistemi di Calcolo 2 — Lezione 3
tags:
  - sistemi-di-calcolo-2
  - deadlock
  - concorrenza
  - mutua-esclusione
source: Appunti Filippo/3-deadlock.pdf
---

# Deadlock e starvation, ancora sulla mutua esclusione

> [!abstract] Scopo della lezione
> Il **deadlock** è il blocco permanente di un gruppo di processi che si aspettano a vicenda. La lezione ne dà la definizione, distingue le risorse **riutilizzabili** e **consumabili**, enuncia le **quattro condizioni** di Coffman e il **grafo di allocazione delle risorse**, e poi presenta le tre strategie: **prevention**, **avoidance** (stato safe e **algoritmo del banchiere**) e **detection** con recovery. Applica tutto al problema dei **cinque filosofi** e chiude con la mutua esclusione **solo software**: i quattro tentativi che portano all'**algoritmo di Dekker** e la sua generalizzazione a N processi, l'**algoritmo di Dijkstra**.
> Mappa dei concetti: [[MOC - Sistemi di Calcolo 2]]

> [!important] Per l'esame
> All'esame c'è una domanda sull'**algoritmo di Dijkstra** o sull'**algoritmo del panettiere** (Lamport): viene mostrato l'algoritmo **con un errore** da trovare.

## Deadlock

Vedi [[Deadlock]].

Il **deadlock** è il **blocco permanente** di un insieme di processi che competono per le risorse del sistema o che comunicano tra loro. Un insieme di processi è in deadlock quando **ogni processo dell'insieme è bloccato in attesa di un evento che può essere generato solo da un altro processo dell'insieme**, anch'esso bloccato.

Il deadlock è **permanente** (nessuno dei processi coinvolti può sbloccarsi da solo) e **non esiste una soluzione efficiente** in generale.

**Esempio reale: un incrocio.**

![[SDC2-L03-001-000.png]]

*Deadlock potenziale*: quattro auto arrivano contemporaneamente a un incrocio diviso in quattro quadranti a, b, c, d. Ognuna, per attraversare, ha bisogno di due quadranti: l'auto 1 di a e b, la 2 di b e c, la 3 di c e d, la 4 di d e a.

![[SDC2-L03-001-001.png]]

*Deadlock verificato*: ogni auto ha occupato il primo quadrante e aspetta il secondo, che è occupato dall'auto successiva. L'auto 1 aspetta B, la 2 aspetta C, la 3 aspetta D, la 4 aspetta A: nessuno può procedere.

Deadlock e busy waiting sono **due cose indipendenti**: in un deadlock i processi possono essere bloccati (senza consumare CPU) oppure in busy waiting.

### Risorse riutilizzabili e consumabili

Vedi [[Risorse Riutilizzabili e Consumabili]].

- **Risorsa riutilizzabile** (*reusable*): può essere usata in sicurezza da **un processo alla volta** e **non si esaurisce** con l'uso: viene rilasciata e riusata. Esempi: processori, canali di I/O, memoria principale e secondaria, dispositivi, file, database, semafori.
- **Risorsa consumabile** (*consumable*): viene **creata** (prodotta) e **distrutta** (consumata). Esempi: interrupt, segnali, messaggi, informazioni nei buffer di I/O.

**Esempio con risorse riutilizzabili**: due processi in competizione.

![[SDC2-L03-002-002.png]]

| Passo | Processo P | Passo | Processo Q |
| --- | --- | --- | --- |
| p0 | Request(D) | q0 | Request(T) |
| p1 | Lock(D) | q1 | Lock(T) |
| p2 | Request(T) | q2 | Request(D) |
| p3 | Lock(T) | q3 | Lock(D) |
| p4 | Perform function | q4 | Perform function |
| p5 | Unlock(D) | q5 | Unlock(T) |
| p6 | Unlock(T) | q6 | Unlock(D) |

Con l'esecuzione intercalata p0, p1, q0, q1, p2, q2: P ha D e aspetta T, che è bloccato da Q; Q ha T e aspetta D, che è bloccato da P.

**Esempio con richieste di memoria**: ci sono 200 KB allocabili e due processi.

![[SDC2-L03-002-003.png]]

P1 chiede 80 KB e poi 60 KB; P2 chiede 70 KB e poi 80 KB. Dopo le prime richieste sono occupati 150 KB e ne restano 50: se entrambi arrivano alla seconda richiesta (60 e 80 > 50) si bloccano a vicenda, e c'è deadlock.

**Esempio con risorse consumabili**: ogni processo prova a ricevere un messaggio dall'altro e poi gli invia un messaggio.

![[SDC2-L03-002-004.png]]

```
P1:  ... receive(P2); ... send(P2, M1);
P2:  ... receive(P1); ... send(P1, M2);
```

Se la `receive` è **bloccante**, entrambi aspettano un messaggio che l'altro invierà solo dopo averne ricevuto uno: deadlock. È un errore di progettazione che può restare nascosto a lungo.

### Le quattro condizioni

Vedi [[Condizioni di Coffman]].

Il deadlock si verifica quando valgono **tutte** queste condizioni:

1. **Mutual exclusion**: solo un processo alla volta può usare una risorsa.
2. **Hold and wait**: un processo può trattenere le risorse già allocate mentre aspetta di ottenerne altre.
3. **No preemption**: nessuna risorsa può essere tolta forzatamente a un processo che la sta trattenendo.
4. **Circular wait**: esiste una catena chiusa di processi in cui ognuno trattiene almeno una risorsa richiesta dal processo successivo.

Le prime tre sono condizioni **necessarie ma non sufficienti**: rendono il deadlock *possibile*. La quarta è ciò che lo fa *accadere*. Tutte e quattro insieme sono **necessarie e sufficienti**.

### Grafo di allocazione delle risorse

Vedi [[Grafo di Allocazione delle Risorse]].

I processi sono cerchi, le risorse rettangoli, e ogni pallino dentro un rettangolo è un'**istanza** della risorsa.

![[SDC2-L03-003-005.png]]

- **(a)** freccia processo → risorsa: la risorsa è **richiesta**;
- **(b)** freccia risorsa → processo: la risorsa è **trattenuta** (*held by*).

![[SDC2-L03-003-006.png]]

- **(c) circular wait**: P1 chiede Ra, trattenuta da P2; P2 chiede Rb, trattenuta da P1. Con una sola istanza per risorsa il ciclo è un **deadlock**.
- **(d) no deadlock**: stesso ciclo, ma Ra e Rb hanno più istanze. Un'istanza libera può soddisfare una richiesta e rompere l'attesa. Con risorse a più istanze, un ciclo nel grafo è **necessario ma non sufficiente** per il deadlock.

Esempio: il grafo dell'incrocio.

![[SDC2-L03-003-007.png]]

![[SDC2-L03-003-008.png]]

Le quattro auto sono i processi P1…P4, i quadranti le risorse Ra…Rd. Ogni Pi trattiene Ri e chiede R(i+1): il grafo è un unico ciclo P1 → Rb → P2 → Rc → P3 → Rd → P4 → Ra → P1.

## Gestione del deadlock

Tre approcci principali:

| Approccio | Idea |
| --- | --- |
| **Prevention** | si adotta una politica che **elimina una delle condizioni** necessarie |
| **Avoidance** | si fanno scelte **dinamiche** in base allo stato corrente dell'allocazione, evitando gli stati pericolosi |
| **Detection** | si lasciano concedere le risorse, si **individua** il deadlock quando si verifica e si **recupera** |

(Un quarto approccio, molto diffuso nella pratica, è ignorare il problema: l'"algoritmo dello struzzo".)

### Prevention

Vedi [[Gestione del Deadlock]].

Si progetta il sistema in modo da **escludere** la possibilità di deadlock. Due metodi:

- **indiretto**: si impedisce una delle tre condizioni necessarie (mutual exclusion, hold and wait, no preemption);
- **diretto**: si impedisce la circular wait.

Prevenzione delle singole condizioni:

- **Mutual exclusion**: se l'accesso a una risorsa richiede mutua esclusione, l'OS deve supportarla. Di solito **non si può eliminare** (una stampante non può essere usata da due processi insieme); al massimo si può rilassare in alcuni casi (es. file in sola lettura).
- **Hold and wait**: si richiede che un processo chieda **tutte le risorse insieme**, e lo si blocca finché non possono essere concesse tutte contemporaneamente. È **inefficiente**: un processo può aspettare a lungo che siano libere tutte insieme, può trattenere risorse per molto tempo senza usarle, e spesso **non sa in anticipo** di quali risorse avrà bisogno.
- **No preemption**: se a un processo che trattiene delle risorse viene negata un'ulteriore richiesta, deve **rilasciare** le risorse che ha e richiederle di nuovo in seguito. In alternativa l'OS può chiedere a un altro processo di rilasciare le sue risorse (serve che il primo abbia priorità maggiore). È pratico solo per risorse il cui **stato si può salvare e ripristinare** (es. la CPU, i registri).
- **Circular wait**: si definisce un **ordinamento lineare** dei tipi di risorsa. Se a un processo è stata assegnata una risorsa di tipo R, può poi richiedere solo risorse di tipo **successivo** a R nell'ordinamento. Così non si può formare un ciclo. Ha problemi simili a quelli di hold and wait (le risorse si chiedono in un ordine imposto, non quando servono).

### Avoidance

Si decide **dinamicamente** se la richiesta corrente di allocazione, se soddisfatta, **potrebbe** portare a un deadlock. Richiede di **conoscere in anticipo le richieste future** dei processi. Permette **più concorrenza** della prevention.

Due approcci:

- **Process initiation denial**: non si avvia un processo se le sue richieste potrebbero portare a un deadlock. L'OS avvia un nuovo processo solo se le richieste massime di tutti i processi in esecuzione più quelle del nuovo **non superano** le risorse disponibili:

  $$R_j \ge C_{(n+1)j} + \sum_{i=1}^{n} C_{ij} \quad \text{per ogni risorsa } j$$

- **Resource allocation denial**: non si concede una richiesta incrementale di risorse se l'allocazione potrebbe portare a un deadlock. È l'**algoritmo del banchiere**.

> [!warning] Correzione
> Gli appunti scrivono la condizione con "<" stretto; la formulazione di Stallings usa **≤** (si può avviare il processo anche se la somma delle richieste massime è esattamente uguale alle risorse).

Esempio di process initiation denial:

![[SDC2-L03-004-009.png]]

Risorse totali R = (9, 3, 6). Le richieste massime (*claim matrix* C) sono P1 = (3, 2, 2), P2 = (6, 1, 3), P3 = (3, 1, 4), P4 = (4, 2, 2). P1 + P2 = (9, 3, 5) ≤ (9, 3, 6), quindi possono girare insieme; aggiungendo P3 si arriva a (12, 4, 9), troppo. Se P1 e P2 sono in esecuzione, **P3 e P4 non possono essere avviati**. È una strategia molto pessimista: assume che tutti chiedano il massimo contemporaneamente.

#### Stato safe

Vedi [[Algoritmo del Banchiere]].

Uno **stato è safe** se esiste **almeno una sequenza** di esecuzione dei processi che li porta tutti a termine senza deadlock. Altrimenti è **unsafe** (che non significa necessariamente deadlock, ma che il sistema non può più garantirne l'assenza).

Strutture dati, con n processi e m risorse:

| Nome | Contenuto |
| --- | --- |
| **Resource vector R** | quantità totale di ogni risorsa |
| **Available vector V** | quantità di ogni risorsa ancora disponibile |
| **Claim matrix C** | C[i][j] = massima richiesta del processo i per la risorsa j |
| **Allocation matrix A** | A[i][j] = quantità della risorsa j già assegnata al processo i |
| **C − A** | ciò che manca a ogni processo per poter terminare |

**Esempio: determinazione di uno stato safe.**

![[SDC2-L03-005-010.png]]

![[SDC2-L03-005-012.png]]

Stato iniziale con 4 processi e 3 risorse. R = (9, 3, 6) sono le risorse esistenti; V = (0, 1, 1) quelle ancora disponibili dopo l'allocazione.

| | C | A | C − A |
| --- | --- | --- | --- |
| P1 | 3 2 2 | 1 0 0 | 2 2 2 |
| P2 | 6 1 3 | 6 1 2 | 0 0 1 |
| P3 | 3 1 4 | 2 1 1 | 1 0 3 |
| P4 | 4 2 2 | 0 0 2 | 4 2 0 |

![[SDC2-L03-005-013.png]]

**(b)** A P2 manca solo una unità di R3, e V = (0, 1, 1) la contiene: P2 può terminare e rilascia tutto ciò che aveva (6, 1, 2). V = (0, 1, 1) + (6, 1, 2) = (6, 2, 3).

![[SDC2-L03-005-014.png]]

**(c)** A P1 servono (2, 2, 2) ≤ (6, 2, 3): P1 termina e rilascia (3, 2, 2) (le 1 + 0 + 0 che aveva più le 2 + 2 + 2 appena prese). V = (6, 2, 3) + (1, 0, 0) = (7, 2, 3).

![[SDC2-L03-006-015.png]]

**(d)** A P3 servono (1, 0, 3) ≤ (7, 2, 3): P3 termina. V = (7, 2, 3) + (2, 1, 1) = (9, 3, 4). Ora tutto è disponibile per P4, che può terminare.

La sequenza P2, P1, P3, P4 porta tutti a termine: **lo stato iniziale è safe**.

> [!note] Come si aggiorna V
> Quando un processo termina, V aumenta esattamente di ciò che quel processo aveva **già allocato** (riga di A), perché le risorse prese temporaneamente per finire vengono restituite subito dopo.

**Esempio: determinazione di uno stato unsafe.**

![[SDC2-L03-006-016.png]]

![[SDC2-L03-006-018.png]]

Stato iniziale: A ha P2 = (5, 1, 1) e V = (1, 1, 2).

| | C | A | C − A |
| --- | --- | --- | --- |
| P1 | 3 2 2 | 1 0 0 | 2 2 2 |
| P2 | 6 1 3 | 5 1 1 | 1 0 2 |
| P3 | 3 1 4 | 2 1 1 | 1 0 3 |
| P4 | 4 2 2 | 0 0 2 | 4 2 0 |

![[SDC2-L03-006-020.png]]

P1 chiede una unità di R1 e una di R3. Se la si concede, V = (0, 1, 1) e C − A diventa P1 = (1, 2, 1), P2 = (1, 0, 2), P3 = (1, 0, 3), P4 = (4, 2, 0).

**È safe?** No: **a tutti i processi manca almeno una unità di R1**, e V ha R1 = 0. Nessun processo può terminare, quindi lo stato è **unsafe** e la richiesta di P1 va **negata** (P1 viene sospeso). Non c'è ancora un deadlock (se P1 rilasciasse le risorse si potrebbe uscirne), ma il sistema non può più garantire che non si verifichi.

#### L'algoritmo

![[SDC2-L03-007-021.png]]

```c
struct state {
    int resource[m];
    int available[m];
    int claim[n][m];
    int alloc[n][m];
};

// il processo i chiede request[*]
if (alloc[i,*] + request[*] > claim[i,*])
    <error>;                              // chiede più del massimo dichiarato
else if (request[*] > available[*])
    <suspend process>;                    // le risorse non ci sono
else {                                    // simula l'allocazione
    <define newstate by:
     alloc[i,*] = alloc[i,*] + request[*];
     available[*] = available[*] - request[*]>;
}
if (safe(newstate))
    <carry out allocation>;
else {
    <restore original state>;
    <suspend process>;
}
```

Il test di sicurezza è l'**algoritmo del banchiere** (Dijkstra):

![[SDC2-L03-007-022.png]]

```c
boolean safe(state S) {
    int currentavail[m];
    process rest[<number of processes>];
    currentavail = available;
    rest = {all processes};
    possible = true;
    while (possible) {
        <find a process Pk in rest such that
         claim[k,*] - alloc[k,*] <= currentavail;>
        if (found) {                               // simula l'esecuzione di Pk
            currentavail = currentavail + alloc[k,*];
            rest = rest - {Pk};
        }
        else possible = false;
    }
    return (rest == null);                         // safe se tutti possono terminare
}
```

Cerca ripetutamente un processo a cui basta ciò che è disponibile per terminare; lo "fa terminare" restituendone le risorse e ricomincia. Lo stato è safe se alla fine sono stati tolti **tutti** i processi. Costo O(m · n²).

#### Vantaggi e svantaggi dell'avoidance

La process initiation denial non è ottimale; la resource allocation denial invece:

- **non** richiede di fare preemption e rollback dei processi, come la detection;
- è **meno restrittiva** della prevention.

Svantaggi:

- la **richiesta massima** di ogni processo va dichiarata a priori;
- i processi considerati devono essere **indipendenti**, senza vincoli di sincronizzazione tra loro;
- il numero di risorse da allocare deve essere **fisso**;
- nessun processo può terminare mentre trattiene delle risorse.

Le strategie di prevention sono molto **conservative** (limitano l'accesso alle risorse con vincoli sui processi); quelle di detection fanno l'opposto (le richieste vengono concesse ogni volta che è possibile).

### Detection

Si cerca di **individuare** la presenza di un deadlock e di **risolverlo**.

Il controllo si può fare a **ogni richiesta** di risorsa, oppure meno spesso, a seconda di quanto è probabile un deadlock.

- Controllare a ogni richiesta porta a una **rilevazione precoce** e l'algoritmo è semplice (ogni volta cambia poco);
- ma i controlli frequenti **consumano tempo di CPU**.

Algoritmo (con Q = matrice delle richieste, A = allocazioni, W = copia dell'available vector):

1. **marca** ogni processo che ha una riga di A tutta a zero (un processo senza risorse non può partecipare a un deadlock);
2. W = available;
3. cerca un processo **non marcato** i tale che la riga i di Q sia ≤ W, cioè le sue richieste possono essere soddisfatte;
4. se non c'è, **termina**;
5. se c'è, **marca** i e somma a W la sua riga di A (simula che termini e liberi le risorse); torna al punto 3.

**Alla fine, i processi non marcati sono in deadlock.**

![[SDC2-L03-008-023.png]]

| | Q (R1 … R5) | A (R1 … R5) |
| --- | --- | --- |
| P1 | 0 1 0 0 1 | 1 0 1 1 0 |
| P2 | 0 0 1 0 1 | 1 1 0 0 0 |
| P3 | 0 0 0 0 1 | 0 0 0 1 0 |
| P4 | 1 0 1 0 1 | 0 0 0 0 0 |

Resource vector (2, 1, 1, 2, 1), allocation (available) vector W = (0, 0, 0, 0, 1).

1. P4 non ha risorse allocate: viene marcato.
2. Le richieste di P3, (0, 0, 0, 0, 1), sono ≤ W: P3 viene marcato e W = W + (0, 0, 0, 1, 0) = (0, 0, 0, 1, 1).
3. P1 chiede una unità di R2 e P2 una di R3, ma W ha R2 = R3 = 0: nessuno dei due può proseguire.

**P1 e P2 sono in deadlock.**

#### Recovery

Approcci in ordine crescente di sofisticazione:

1. **terminare tutti** i processi coinvolti nel deadlock (il più comune);
2. riportare ogni processo in deadlock a un **checkpoint** salvato in precedenza e farlo ripartire (il deadlock potrebbe ripresentarsi, ma il non determinismo di solito lo evita);
3. terminare i processi in deadlock **uno alla volta** finché il deadlock non scompare (scegliendo con criteri come tempo di CPU già usato, output prodotto, priorità…);
4. fare **preemption delle risorse** una alla volta finché il deadlock non scompare (serve un meccanismo di rollback al momento precedente l'acquisizione della risorsa).

> [!warning] Correzione
> Negli appunti si legge "deadline detection-recovery": si intende **deadlock** detection-recovery.

### Tabella riassuntiva

![[SDC2-L03-009-025.png]]

| Approccio | Politica di allocazione | Schemi | Vantaggi | Svantaggi |
| --- | --- | --- | --- | --- |
| **Prevention** | conservativa: sottoutilizza le risorse | richiedere **tutte le risorse insieme** (contro hold and wait) | va bene per processi con un solo burst di attività; non serve preemption | inefficiente; ritarda l'avvio dei processi; i processi devono conoscere in anticipo le richieste future |
| | | **preemption** (contro no preemption) | comoda per risorse il cui stato si salva e ripristina facilmente | fa preemption più spesso del necessario |
| | | **ordinamento delle risorse** (contro circular wait) | verificabile con controlli a compile time; nessun calcolo a runtime, il problema si risolve in fase di progetto | non permette richieste incrementali di risorse |
| **Avoidance** | a metà tra detection e prevention | si manipola l'allocazione per avere almeno un percorso safe | non serve preemption | l'OS deve conoscere le richieste future; i processi possono restare bloccati a lungo |
| **Detection** | molto liberale: le risorse si concedono quando possibile | si invoca periodicamente il test di deadlock | non ritarda mai l'avvio dei processi; facilita la gestione online | perdite dovute alla preemption |

## Il problema dei cinque filosofi

Vedi [[Problema dei Cinque Filosofi]].

![[SDC2-L03-010-026.png]]

Cinque filosofi sono seduti a un tavolo rotondo e alternano **pensare** e **mangiare**. Tra ogni coppia di filosofi c'è **una forchetta** (5 in tutto), e per mangiare un filosofo ha bisogno **di entrambe** le forchette accanto a sé.

- Due filosofi non possono usare la stessa forchetta contemporaneamente (**mutua esclusione**).
- Nessun filosofo deve morire di fame (niente **deadlock** né **starvation**).

È il caso di test standard per valutare i meccanismi di sincronizzazione, perché mostra entrambi i problemi.

**Soluzione con 5 semafori (sbagliata):**

![[SDC2-L03-010-028.png]]

```c
semaphore fork[5] = {1};
void philosopher(int i) {
    while (true) {
        think();
        wait(fork[i]);              // forchetta di sinistra
        wait(fork[(i+1) mod 5]);    // forchetta di destra
        eat();
        signal(fork[(i+1) mod 5]);
        signal(fork[i]);
    }
}
```

Ogni filosofo prende prima la forchetta di sinistra (i) e poi quella di destra (i+1). Se tutti e cinque prendono la sinistra nello stesso momento, ognuno aspetta la destra, che è la sinistra del vicino: **deadlock** (circular wait).

> [!warning] Correzione
> `semaphore fork[5] = {1};` in C inizializzerebbe solo il primo elemento a 1 e gli altri a 0. L'intenzione (di Stallings) è che **tutti** i semafori valgano 1.

**Soluzione corretta:** si toglie una sedia. Nella stanza possono stare al massimo **4 filosofi** alla volta: con 4 filosofi e 5 forchette, **almeno uno** riesce sempre a prendere due forchette e a mangiare (piccionaia). Quando finisce, entra il filosofo rimasto fuori.

![[SDC2-L03-011-029.png]]

```c
semaphore fork[5] = {1};
semaphore room = {4};
void philosopher(int i) {
    while (true) {
        think();
        wait(room);                 // prova a prendere una sedia
        wait(fork[i]);
        wait(fork[(i+1) mod 5]);
        eat();
        signal(fork[(i+1) mod 5]);
        signal(fork[i]);
        signal(room);               // lascia forchette e sedia
    }
}
```

Il semaforo `room` impedisce la circular wait. Altre soluzioni: un filosofo "mancino" che prende prima la destra (ordinamento delle risorse), o un monitor che dà le forchette solo se sono libere entrambe.

## Mutua esclusione in software

La mutua esclusione si può implementare anche **solo in software**. Ipotesi:

- i processi comunicano tramite la memoria centrale, su una macchina uni- o multiprocessore;
- c'è mutua esclusione **a livello di accesso alla memoria**: letture e scritture sulla stessa locazione non avvengono mai contemporaneamente, ma vengono serializzate da una sorta di *memory arbiter* in un **ordine sconosciuto**;
- **nessun supporto** dall'OS, dall'hardware (niente compare&swap) o dal linguaggio.

> [!note] Validità oggi
> Su CPU moderne il compilatore e il processore possono **riordinare** letture e scritture: questi algoritmi funzionano solo con barriere di memoria o variabili `volatile`/atomiche. Restano fondamentali per capire il problema.

### Algoritmo di Dekker

Vedi [[Algoritmo di Dekker]].

È un algoritmo di mutua esclusione per **due processi**, ideato da Dekker e pubblicato da Dijkstra. Ci si arriva per tentativi.

**Primo tentativo: turni stretti.**

![[SDC2-L03-011-030.png]]

```c
int turn = 0;                       // globale
// per P0 (invertire per P1)
int me = 0, other = 1;
while (true) {
    /* NCS */
    while (turn != me)
        /* busy wait */ ;           // aspetta il proprio turno
    /* CS */
    turn = other;                   // passa il turno all'altro
}
```

Garantisce la mutua esclusione, ma impone una **stretta alternanza**: se io devo entrare una volta al secondo e l'altro ogni mezz'ora, anch'io entrerò solo ogni mezz'ora. E se l'altro processo termina, io resto bloccato per sempre (viola il requisito "se la sezione critica è libera si deve poter entrare").

**Secondo tentativo: flag di interesse, controllati prima.**

![[SDC2-L03-012-031.png]]

```c
boolean flag[2] = {false, false};
while (true) {
    /* NCS */
    while (flag[other])
        /* busy wait */ ;           // aspetto finché l'altro è interessato
    flag[me] = true;                // sono interessato
    /* CS */
    flag[me] = false;               // non lo sono più
}
```

Ogni processo usa un flag per dire se è interessato a entrare. **Non garantisce la mutua esclusione**: due processi in parallelo possono vedere entrambi l'altro "non interessato", mettere entrambi il proprio flag a `true` ed entrare **entrambi** nella sezione critica.

**Terzo tentativo: flag impostato prima del controllo.**

![[SDC2-L03-012-032.png]]

```c
while (true) {
    /* NCS */
    flag[me] = true;                // dichiaro subito l'interesse
    while (flag[other])
        /* busy wait */ ;
    /* CS */
    flag[me] = false;
}
```

Ora la mutua esclusione c'è, ma può verificarsi un **deadlock**: se entrambi mettono il flag a `true` prima di controllare, ognuno aspetta per sempre che l'altro non sia più interessato.

**Quarto tentativo: cortesia.**

![[SDC2-L03-013-033.png]]

```c
while (true) {
    /* NCS */
    flag[me] = true;
    while (flag[other]) {
        flag[me] = false;           // cedo il passo
        /* delay */
        flag[me] = true;            // e riprovo
    }
    /* CS */
    flag[me] = false;
}
```

Se l'altro è interessato, si ritira per un po' e riprova. Niente deadlock, ma è possibile un **livelock**: se i due processi procedono in perfetta sincronia, si ritirano e riprovano all'infinito senza mai entrare.

**Soluzione corretta: algoritmo di Dekker.**

![[SDC2-L03-013-034.png]]

![[SDC2-L03-013-035.png]]

```c
int turn = 0;                           // globale
boolean flag[2] = {false, false};
// P0 (invertire per P1)
int me = 0, other = 1;
while (true) {
    /* NCS */
    flag[me] = true;                    // sono interessato
    while (flag[other]) {               // finché l'altro è interessato
        if (turn == other) {            // se è il turno dell'altro
            flag[me] = false;           // mi ritiro
            while (turn == other)
                /* busy wait */ ;       // aspetto che sia il mio turno
            flag[me] = true;            // e torno interessato
        }
    }
    /* CS */
    turn = other;                       // il turno passa all'altro
    flag[me] = false;                   // non sono più interessato
}
```

Combina i flag (per entrare subito se l'altro non è interessato) con la variabile `turn` (per decidere chi ha la precedenza in caso di conflitto): solo chi **non** ha il turno si ritira. Garantisce mutua esclusione, assenza di deadlock e di starvation.

La soluzione di Dekker funziona per **due** processi; per estenderla serve modificarla.

> [!tip] Algoritmo di Peterson
> Una versione più semplice per due processi (1981): `flag[me] = true; turn = other; while (flag[other] && turn == other);` — chi arriva per secondo cede il turno all'altro.

### Algoritmo di Dijkstra

Vedi [[Algoritmo di Dijkstra per la Mutua Esclusione]].

Dijkstra ha **generalizzato** l'algoritmo di Dekker a **N processi** e ha formalizzato le proprietà di **mutua esclusione (ME)**, **assenza di deadlock (ND)** e **assenza di starvation (NS)**. NS implica ND (se nessuno muore di fame, il sistema progredisce).

![[SDC2-L03-014-036.png]]

```c
/* memoria globale */
boolean interested[N] = {false, ..., false};
boolean passed[N]     = {false, ..., false};
int k = <any>;                  // k ∈ {0, 1, ..., N-1}
/* informazione locale */
int i = <entity ID>;            // i ∈ {0, 1, ..., N-1}
```

Si assume che le modifiche a `k` siano **atomiche**, perché tutti possono scriverci.

![[SDC2-L03-014-037.png]]

```
while (true) {
    /* NCS */
 1. interested[i] = true                // sono interessato
 2. while (k != i) {                    // finché il turno è di qualcun altro
 3.     passed[i] = false               //   non sono "passato"
 4.     if (!interested[k]) then k = i  //   se il processo k non è interessato,
    }                                   //   mi prendo il turno
 5. passed[i] = true                    // sono passato al secondo stadio
 6. for j in 1 ... N except i do
 7.     if (passed[j]) then goto 2      // se un altro è passato, ricomincio
 8. <critical section>
 9. passed[i] = false; interested[i] = false
}
```

Due stadi:

- **primo stadio (righe 2–4)**: si cerca di prendere il turno `k`. Si può prendere solo se il proprietario attuale non è interessato. Più processi possono superarlo, perché leggono `interested[k]` quasi insieme;
- **secondo stadio (righe 5–7)**: chi l'ha superato dichiara `passed[i] = true` e controlla che **nessun altro** sia passato. Se qualcuno lo è, torna alla riga 2 (e azzera `passed[i]`). Tra i processi in conflitto, quello che ha scritto `k` **per ultimo** trova `k == i` al ritorno e salta direttamente alla riga 5, mentre gli altri restano nel ciclo: solo uno arriva alla sezione critica.

Un processo può dover tornare indietro più volte, ma **uno solo** arriva alla sezione critica.

#### Esempio con N ≥ 4 (inizialmente k = 4)

![[SDC2-L03-014-038.png]]

P1, P2 e P3 dichiarano l'interesse (`intr[i] = true`), entrano nel ciclo (`k != i`) e mettono `pass[i] = false`. Tutti vedono che P4 **non è interessato** (`!intr[4]`) e quindi tutti si prendono il turno: k = 1, poi k = 2, poi k = 3. L'ultima scrittura è k = 3.

P1, P2 e P3 sono ora pronti a eseguire le righe 5–7, ma solo uno di loro entrerà nella sezione critica. `k` serve solo a **risolvere i conflitti**: non significa che P3 passerà per primo, lo scheduler potrebbe far avanzare anche P1 o P2. Si crea un conflitto quando due processi mettono entrambi `passed[i] = true` prima che l'altro sia entrato e uscito dalla sezione critica.

Una possibile prosecuzione **senza conflitti**: lo scheduler fa eseguire P3 mentre P1 e P2 sono ancora fermi alla riga 5.

![[SDC2-L03-015-039.png]]

P3 mette `pass[3] = true`, controlla gli altri (nessuno è passato), entra nella sezione critica, poi rimette `pass[3] = false` e `intr[3] = false`.

**C'è conflitto tra P1 e P2?**

![[SDC2-L03-015-040.png]]

Entrambi tornano nel ciclo e vedono che P3 (il proprietario di k) non è più interessato: P1 mette k = 1, esce dal ciclo e mette `pass[1] = true`; P2 mette k = 2, esce dal ciclo e mette `pass[2] = true`. Ora P1 vede `pass[2]` e torna alla riga 2; P2 vede `pass[1]` e torna alla riga 2: **conflitto**.

Quando c'è un conflitto, l'algoritmo torna alla riga 2 e azzera `passed[i]`, **tranne che per il processo che ha scritto `k` per ultimo** (qui P2, con k = 2): P2 trova `k == 2`, salta il ciclo, rimette `pass[2] = true`, e questa volta P1 (che è nel ciclo con `pass[1] = false`) non gli dà fastidio. P2 entra.

> [!note]
> L'algoritmo di Dijkstra garantisce ME e ND, ma **non** la starvation-freedom (un processo può essere superato indefinitamente). Algoritmi successivi (Knuth, Lamport con il **panettiere**) aggiungono questa garanzia: il panettiere assegna a ogni processo un "numero" crescente come il biglietto di una coda, ed entra chi ha il numero più basso.
