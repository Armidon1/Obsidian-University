# Distributed Ledger Technology (Registri Distribuiti)

>[!Abstract] Definizione
>La Distributed Ledger Technology (DLT), o tecnologia a registro distribuito, è un sistema digitale che permette a gruppi di partecipanti di condividere, replicare e sincronizzare dati su una rete distribuita. A differenza dei database tradizionali centralizzati, non esiste un'autorità centrale che detiene e gestisce il registro (come una banca o un ente governativo); ogni nodo della rete possiede una copia identica e aggiornata.

## **Caratteristiche Principali**

- **Decentralizzazione:** Il controllo è distribuito tra i partecipanti ([[Peer-To-Peer (P2P)]]), eliminando il "single point of failure" (un punto singolo di vulnerabilità che, se colpito, blocca tutto il sistema).
    
- **Immutabilità e Sicurezza:** L'uso della crittografia avanzata garantisce che, una volta validati e registrati, i dati non possano essere facilmente alterati o cancellati ([[Integrity]]).
    
- **Trasparenza:** Tutti i partecipanti autorizzati hanno accesso alla stessa versione della verità in tempo reale.
    
- **[[Consensus]]:** L'aggiunta di nuovi dati richiede l'accordo dei nodi della rete tramite meccanismi di consenso (ad esempio [[Proof of Work (PoW)]] o [[Proof of Stake (PoS)]]).
    

## Differenza tra DLT e Blockchain

Spesso i termini vengono usati come sinonimi, ma c'è una distinzione tecnica:

- **DLT** è la categoria generale (il "contenitore").
    
- **Blockchain** è un _tipo specifico_ di DLT che organizza i dati in blocchi sequenziali legati crittograficamente in una catena.
    
- Esistono DLT che _non_ usano la struttura a catena di blocchi (ad esempio il Tangle di IOTA o R3 Corda).
    

## **Vantaggi**

- **Efficienza:** Riduzione degli intermediari e dei costi di gestione.
    
- **Velocità:** Esecuzione e riconciliazione delle transazioni più rapida (spesso immediata).
    
- **Resilienza:** Maggiore resistenza agli attacchi informatici grazie alla distribuzione dei dati su molti nodi.
    
- **Auditability:** Tracciabilità migliorata di ogni modifica o transazione.
    

## **Applicazioni Comuni**

- **Finanza:** Criptovalute, pagamenti transfrontalieri, clearing e settlement.
    
- **Supply Chain:** Tracciamento della filiera produttiva, garanzia di autenticità e anticontraffazione.
    
- **Identità Digitale:** Gestione sicura e autonoma delle credenziali personali (Self-Sovereign Identity).
    
- **Voto Elettronico:** Sistemi di voto sicuri, trasparenti e verificabili.


# CRUD vs CRAB: Database vs Blockchain

**Contesto:** Il passaggio da un'architettura centralizzata a una decentralizzata (Blockchain/DLT) richiede un cambio di mentalità nella gestione dei dati. Mentre i database tradizionali sono progettati per essere mutevoli ed efficienti, le blockchain sono progettate per essere immutabili e verificabili. Questo cambiamento è riassunto nell'evoluzione dall'acronimo CRUD all'acronimo CRAB.

## 1. CRUD (Database Tradizionali)

Utilizzato nei database relazionali (SQL) e molti NoSQL. L'obiettivo è la gestione efficiente dello stato corrente.

- **C - Create:** Creazione di un nuovo record.
    
- **R - Read:** Lettura dei dati esistenti.
    
- **U - Update:** Modifica di un record esistente. _Il dato originale viene sovrascritto e perso (a meno di backup specifici)._
    
- **D - Delete:** Cancellazione di un record. _Il dato viene rimosso fisicamente o logicamente dal sistema._
    

> **Caratteristica chiave:** **Mutabilità**. La storia può essere riscritta o cancellata.

---

## 2. CRAB (Blockchain & DLT)

Utilizzato nei registri distribuiti dove la storia non può essere alterata.

- **C - Create:** Creazione di una nuova transazione o smart contract.
    
- **R - Retrieve (o Read):** Recupero dei dati dal registro.
    
- **A - Append (Aggiungere):** Invece di modificare ("Update"), si **aggiunge** un nuovo record che rappresenta il nuovo stato. La storia delle modifiche rimane intatta.
    
- **B - Burn (Bruciare):** Invece di cancellare ("Delete"), si rende un asset o un dato inutilizzabile (es. inviando token a un indirizzo senza chiave privata), ma la registrazione di questa azione rimane per sempre visibile.
    

> **Caratteristica chiave:** **Immutabilità**. La storia è additiva (append-only) e permanente.

## Tabella di Confronto

|**Operazione**|**CRUD (Database SQL)**|**CRAB (Blockchain)**|**Implicazione**|
|---|---|---|---|
|**Inserimento**|Create|Create|Simile in entrambi i casi.|
|**Lettura**|Read|Retrieve|Simile, ma in Blockchain leggi spesso l'intera storia per calcolare lo stato.|
|**Modifica**|**Update** (Sovrascrittura)|**Append** (Aggiunta)|In Blockchain, il valore precedente (v1) esiste ancora accanto al nuovo (v2).|
|**Rimozione**|**Delete** (Cancellazione)|**Burn** (Disattivazione)|In Blockchain, nulla sparisce mai veramente; viene solo marcato come "speso" o "distrutto".|

## Perché questo cambiamento è importante?

### 1. Audit Trail (Tracciabilità)

- **CRUD:** Se un amministratore cambia un saldo bancario da 100€ a 1000€ usando "Update", il valore 100€ sparisce. Serve un log separato per sapere che è successo.
    
- **CRAB:** Esiste una transazione di input (100€) e una nuova transazione (stato 1000€). Entrambe restano nel ledger. È impossibile cambiare il saldo senza lasciare la traccia del "perché" e del "quando".
    

### 2. Trust (Fiducia)

- **CRUD:** Richiede fiducia nell'amministratore del database, che ha il potere di fare `DELETE` o `UPDATE` senza lasciare traccia.
    
- **CRAB:** È un sistema _trustless_. Nessuno può fare `DELETE` sul passato. Se vedi un dato, sai che nessuno lo ha manipolato silenziosamente.
    

### 3. Gestione dello Spazio

- **CRUD:** È efficiente nello spazio perché i dati vecchi vengono sovrascritti o cancellati.
    
- **CRAB:** I registri tendono a crescere all'infinito (Blockchain Bloat) perché mantengono ogni singola versione di ogni dato ("Append-only").
    

---

Poiché hai menzionato il concetto di "Burn" e "Append", potrebbe interessarti una nota sugli **[[Smart Contracts]]** (che eseguono queste logiche) o sul **Blockchain Trilemma** (che spiega le sfide di scalabilità dovute proprio a questo modello CRAB).