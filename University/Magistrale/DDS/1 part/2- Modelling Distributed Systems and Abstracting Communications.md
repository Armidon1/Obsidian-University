## Lecture 2: Modelling Distributed Systems

---

## Recap

Un **sistema distribuito** è un insieme di entità/macchine che comunicano, si coordinano e condividono risorse per raggiungere un obiettivo comune, apparendo come un unico sistema di calcolo.

Come lo fa?  
→ Eseguendo **algoritmi distribuiti**, cioè software che gestiscono questi problemi.

---

## System Deployment

La realizzazione pratica di un sistema distribuito richiede di **istanziare e posizionare i componenti software su macchine reali**.

- Molte scelte possibili (layout, architettura, distribuzione).
    
- La configurazione finale è detta **architettura di sistema**.
    

Esempi:

- **Centralized**
    
- **Fully distributed**
    

---

## Architectural Style

Uno **stile architetturale** è definito da:

- **Componenti**: unità modulari con interfacce ben definite.
    
- **Connessioni**: modalità di collegamento tra componenti.
    
- **Dati** scambiati tra componenti.
    
- **Configurazione** complessiva del sistema.
    

I componenti si descrivono tramite **specifiche** e **interfacce**.

> In DDS ci si concentra su astrazioni distribuite e sui loro aspetti algoritmici.

---

## Perché le astrazioni sono importanti

1. Catturano proprietà comuni a molti sistemi.
    
2. Separano il fondamentale dal secondario.
    
3. Prevengono la reinvenzione continua delle stesse soluzioni.
    

---

## La strada per costruire un’astrazione distribuita

1. **Definire il modello di sistema**
    
    - Descrivere gli elementi rilevanti in modo astratto.
        
    - Identificarne le proprietà e interazioni.
        
2. **Costruire l’astrazione distribuita**
    
    - Progettare un protocollo che catturi pattern ricorrenti di interazione.
        
3. **Implementare e distribuire l’algoritmo distribuito**
    
    - Scelta del linguaggio, pattern architetturale, ecc.
        

---

## Composition Model

Gli algoritmi distribuiti sono presentati in **pseudo-codice reattivo**, dove:

- I componenti comunicano tramite **eventi**.
    
- Ogni componente implementa **gestori di eventi**.
    
- Un handler reagisce a un evento e può generare nuovi eventi.
    

---

## Programming Interface

|Tipo di Evento|Descrizione|
|---|---|
|**Request**|Usato da un componente per richiedere un servizio a un altro.|
|**Confirmation**|Indica il completamento di una richiesta.|
|**Indication**|Trasporta informazioni (es. notifica di consegna messaggio).|

---

## Esempio: Job Handler

**JH**

```
Submit(job)
Confirm(job)
```

### Versione Sincrona

Richiesta e conferma avvengono nello stesso flusso.

### Versione Asincrona

Richiesta inviata, conferma ricevuta successivamente (decoupled).

---

## Layering Example

**Job Handler (JH)** utilizza un **Transport Handler (TH)**:

```
JH: Submit(job) → TH
TH: Submit(job) → network
```

Ogni layer fornisce un’astrazione diversa (error handling, conferma, retry...).

---

# Modelling Distributed Computations

Argomenti principali:

- Modellazione di processi e interazioni
    
- Proprietà di **Safety** e **Liveness**
    
- Modellazione dei guasti
    
- Assunzioni temporali
    

---

## Processes

- L’insieme dei processi è denotato da **Π (Pi)**.
    
- È **statico** (salvo diversa indicazione) e tutti conoscono le identità degli altri.
    
- Ogni processo ha un identificatore unico `rank: Π → {1, …, N}`.
    
- Il nome **self** indica il processo corrente.
    

---

## Process Interactions and Messages

- I processi comunicano scambiando **messaggi univoci** (es. con ID o timestamp).
    
- Ogni messaggio è unico.
    
- I messaggi sono trasmessi tramite **collegamenti di comunicazione** (links).
    

---

## Distributed Algorithms

- Un algoritmo distribuito è una **collezione distribuita di automi**, uno per processo.
    
- Ogni automa gestisce:
    
    - Come reagire ai messaggi.
        
    - Le transizioni di stato interne.
        
- Tutti i processi eseguono lo stesso automa.
    
- L’esecuzione globale è una **sequenza di passi locali**.
    

---

## Safety and Liveness

|Tipo|Significato|
|---|---|
|**Safety**|“Niente di male accade.” Una volta violata, non può più essere ripristinata.|
|**Liveness**|“Qualcosa di buono accade.” Prima o poi la proprietà sarà soddisfatta.|

---

# Failure Models

|Tipo di Fault|Descrizione|
|---|---|
|**Crash**|Il processo si ferma definitivamente.|
|**Omission**|Il processo non invia o non riceve un messaggio previsto.|
|**Crash & Recovery**|Il processo può fermarsi e poi riprendersi.|
|**Eavesdropping**|Informazioni trapelano a entità esterne.|
|**Arbitrary (Byzantine)**|Il processo si comporta in modo imprevedibile o malevolo.|

---

## Crash Fault

- Modello **crash-stop**: un processo si ferma a tempo _t_ e non riprende più.
    
- Un processo è:
    
    - **Faulty** se crasha durante l’esecuzione.
        
    - **Correct** se non crasha mai e compie infiniti passi.
        

---

## Dependability and Crash Faults

- La **fault tolerance** è essenziale per la **dependability**.
    
- Si progetta l’algoritmo per funzionare nonostante guasti fino a un certo limite _f_.
    
- La relazione _f/N_ (faulty/total processes) è detta **resilience**.
    

---

## Crash-stop vs Crash-recovery

- Nei sistemi reali, i processi possono **riprendersi** dopo un crash.
    
- Il modello crash-stop non vieta il recupero, ma l’algoritmo **non deve dipendere** da esso.
    

---

## Crash-recovery Fault

Un processo è **faulty** se:

- Crasha e non si riprende mai, oppure
    
- Crasha e si riprende **infinite volte**.
    

Un processo è **correct** se crasha un numero finito di volte.

### Problema: Amnesia

- Dopo un crash, un processo può **perdere il suo stato interno**.
    
- Soluzione: usare **stable storage** (log) con `store()` e `retrieve()`.
    

---

# Timing Assumptions

Tre modelli principali:

- **Synchronous**
    
- **Asynchronous**
    
- **Partially synchronous**
    

---

## Synchronous Systems

Caratterizzati da:

1. **Synchronous processing** – tempo di esecuzione massimo noto.
    
2. **Synchronous communication** – tempo di trasmissione massimo noto.
    
3. **Synchronous clocks** – deriva temporale limitata.
    

### Servizi tipici

- Failure detection temporizzata
    
- Coordinazione basata sul tempo
    
- Sincronizzazione degli orologi
    
- Analisi del caso peggiore (worst-case latency)
    

> Problema: difficile garantire la copertura completa delle assunzioni di sincronismo.

---

## Asynchronous Systems

- Nessuna assunzione sui tempi di processi o link.
    
- Nessun orologio fisico affidabile.
    

Definizione del tempo basata su:

- Trasmissione e ricezione di messaggi.
    

→ Nasce il concetto di **logical time** e **logical clock**.

---

## Partial (Eventual) Synchrony

- Il sistema è **sincrono per lunghi periodi**, ma occasionalmente asincrono.
    
- Dopo un tempo ignoto _t_, il sistema diventa sincrono.
    

⚠️ Non significa che:

- Dopo _t_ tutto resta sincrono per sempre.
    
- Il sistema parte asincrono e poi si stabilizza permanentemente.
    

### Aspettativa:

Esiste un periodo di sincronismo **sufficiente per completare** l’algoritmo distribuito.

---

## Summary of Timing Assumptions

|Assunzione|Upper Bound Computation|Upper Bound Communication|Clock Drift Bound|
|---|---|---|---|
|**Synchrony**|✅|✅|✅|
|**Partial Synchrony**|dopo tempo _t_|dopo tempo _t_|dopo tempo _t_|
|**Asynchrony**|❌|❌|❌|

---

## References

- C. Cachin, R. Guerraoui, L. Rodrigues – _Introduction to Reliable and Secure Distributed Programming_, Springer 2011
    
    - Chapter 2, Sections 1, 2, 5
        

---

# Lecture 2B: Abstracting Communications

---

## Link Abstraction

L’astrazione di **link** rappresenta la componente di rete del sistema distribuito.  
Ogni coppia di processi è connessa da un **link bidirezionale**.

- Possibili topologie complesse → servono algoritmi di **routing**.
    
- I messaggi devono avere identificatori univoci (timestamp, ID, ecc.).
    
- Alcuni messaggi possono perdersi, ma la probabilità di consegna è > 0.
    
- La comunicazione può essere protetta da metodi **criptografici**.
    

---

## Link Types (under Crash-Failure Model)

1. **Fair-loss links** – i messaggi possono perdersi, ma alcuni arrivano.
    
2. **Stubborn links** – continuano a ritrasmettere fino alla consegna.
    
3. **Perfect links** – ogni messaggio è consegnato una sola volta e mai perso.
    

---

## System Model

- Due processi: **sender** e **receiver**.
    
- I messaggi:
    
    - Possono perdersi.
        
    - Possono subire ritardi imprevedibili.
        
- I processi:
    
    - Possono crashare.
        
    - Hanno tempo di esecuzione finito (anche se sconosciuto).
        

---

## Generic Link Interface

```
Send(msg)
Deliver(msg)
```

> “Deliver” ≠ “Receive”:  
> Ricevere significa che il messaggio arriva al buffer; consegnare significa che rispetta le proprietà dell’astrazione richiesta.

---

## Fair-Loss Link

### Specifica

- Alcuni messaggi possono perdersi.
    
- Se un messaggio è inviato infinite volte, sarà consegnato infinite volte.
    

### Problemi

- Il mittente deve gestire le **ritrasmissioni**.
    
- Non garantisce **unicità** (messaggi duplicati possibili).
    

---

## Stubborn Link

- Simile al fair-loss, ma continua a ritrasmettere fino alla consegna.
    
- Ogni messaggio può essere ricevuto più volte.
    
- Implementabile sopra un fair-loss link.
    

---

## Perfect Link

### Specifica

- Nessun messaggio perso o duplicato.
    
- Garantisce **integrità**, **affidabilità** e **unicità**.
    

### Implementazione

- Usa stubborn link come base.
    
- Aggiunge meccanismi di controllo duplicati e conferme.
    

---

## References

- C. Cachin, R. Guerraoui, L. Rodrigues – _Introduction to Reliable and Secure Distributed Programming_, Springer 2011
    
    - Chapter 2, Sections 4–2.4.4
        

---

Vuoi che ti esporti anche questo contenuto in un **file `.md`** (Markdown scaricabile e formattato)?