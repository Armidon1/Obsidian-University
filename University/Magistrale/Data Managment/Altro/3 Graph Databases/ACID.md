---
tags: [database, transazioni, basi-di-dati]
aliases: [Proprietà ACID]
---

# ACID

Proprietà che garantiscono l'affidabilità delle **transazioni** in un DBMS.

| Lettera | Proprietà | In breve |
|---|---|---|
| **A** | Atomicity | Tutto o niente → rollback se fallisce |
| **C** | Consistency | Da uno stato valido a un altro stato valido |
| **I** | Isolation | Transazioni concorrenti non interferiscono |
| **D** | Durability | Dopo il commit, le modifiche sono permanenti |

## Atomicity
La transazione è indivisibile: o tutte le operazioni vanno a buon fine, o nessuna.
Implementata tramite **undo log** / rollback.

## Consistency
Ogni transazione rispetta i vincoli di integrità (chiavi, foreign key, check, trigger).

## Isolation
Il risultato di esecuzioni concorrenti è equivalente a un'esecuzione seriale.

> [!info] Livelli di isolamento (SQL standard)
> - **Read Uncommitted** → possibili dirty read
> - **Read Committed** → evita dirty read
> - **Repeatable Read** → evita anche non-repeatable read
> - **Serializable** → evita anche phantom read

Tecniche: locking (2PL), MVCC.

## Durability
Le modifiche committate sopravvivono a crash.
Implementata con **Write-Ahead Logging (WAL)** e checkpoint.

> [!tip] Contrappunto: BASE
> Nei sistemi distribuiti/NoSQL: *Basically Available, Soft state, Eventual consistency*.
> Rilassa le garanzie ACID per scalabilità e disponibilità → vedi [[Teorema CAP]].

## Collegamenti
- [[Transazioni]]
- [[Teorema CAP]]
- [[MVCC]]
