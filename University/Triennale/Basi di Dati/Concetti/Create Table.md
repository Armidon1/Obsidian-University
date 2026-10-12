---
title: Create Table
tags:
  - basi-di-dati
  - concetto
  - sql
  - vincoli
---

# Create Table

> [!summary] In breve
> Istruzione DDL che definisce uno schema di relazione con attributi, domini e vincoli, e crea un'istanza vuota.

```sql
create table Impiegato (
  Matricola character(6) constraint pk1 primary key,
  Nome      character(20) not null,
  Dipart    character(15) references Dipartimento(NomeDip),
  Stipendio numeric(9) default 0,
  constraint un1 unique (Cognome, Nome))
```
- `unique (A, B)` ≠ `A unique, B unique`.
- Foreign key incrociate: si crea una tabella senza vincolo e lo si aggiunge con `alter table`.
- `create domain Voto as smallint check (value >= 18 and value <= 30)`.
- `check` con sottoquery e `create assertion` non sono supportati dai DBMS reali.

## Collegamenti

- **Concetti correlati**: [[DDL e DML]] · [[Chiave Primaria]] · [[Foreign Key]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[03 - BD - SQL#create table|Lezione 3 — create table]]
> - [[03 - BD - SQL#Domini|Lezione 3 — Domini]]
> - [[03 - BD - SQL#Vincoli in SQL|Lezione 3 — Vincoli in SQL]]
> - [[03 - BD - SQL#Modifiche degli schemi, alter table|Lezione 3 — Modifiche degli schemi, alter table]]
