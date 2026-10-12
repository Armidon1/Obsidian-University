---
title: SQL
tags:
  - basi-di-dati
  - concetto
  - sql
---

# SQL

> [!summary] In breve
> Il linguaggio standard dei DBMS relazionali, che comprende DDL e DML; parzialmente dichiarativo. Le sue tabelle sono multiinsiemi.

- Da SEQUEL (IBM, 1974); standard 1986 → 1992 (SQL-92) → 1999 → 2003.
- Una tabella SQL è un **multiinsieme**: senza `primary key`/`unique` ammette righe duplicate; anche le query producono duplicati (`distinct` per toglierli).
- Una `select` è **analoga** (non equivalente) all'espressione algebrica, "a meno dei duplicati".
- DBMS di riferimento: **PostgreSQL** (database → schemi/namespace → tabelle).

## Collegamenti

- **Concetti correlati**: [[Select SQL]] · [[DDL e DML]] · [[Algebra Relazionale]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[03 - BD - SQL#Introduzione a SQL|Lezione 3 — Introduzione a SQL]]
> - [[03 - BD - SQL#SQL e modello relazionale|Lezione 3 — SQL e modello relazionale]]
> - [[03 - BD - SQL#Basi di dati, schemi e tabelle in PostgreSQL|Lezione 3 — Basi di dati, schemi e tabelle in PostgreSQL]]
