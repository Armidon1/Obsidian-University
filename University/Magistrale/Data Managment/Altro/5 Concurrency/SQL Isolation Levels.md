---
title: SQL Isolation Levels
aliases:
  - Isolation level
  - READ COMMITTED
  - REPEATABLE READ
tags:
  - data-management
  - concept
  - sql
  - isolation
  - postgresql
---

# SQL Isolation Levels

> [!summary] In short
> SQL defines four isolation levels by the anomalies they forbid; each transaction chooses one with `SET TRANSACTION ISOLATION LEVEL`.

| Level | Dirty read | Nonrepeatable read | Phantom |
|---|---|---|---|
| Read uncommitted | possible | possible | possible |
| Read committed | — | possible | possible |
| Repeatable read | — | — | possible (PostgreSQL: no) |
| Serializable | — | — | — |

- Lock implementation: RC releases S locks after each `SELECT`; RR keeps all locks; SERIALIZABLE = SS2PL + range locks.
- PostgreSQL: default and minimum READ COMMITTED (lost update possible); REPEATABLE READ aborts on concurrent update (40001); SERIALIZABLE uses SSI.

## Links

- **Related concepts**: [[Concurrency Anomalies]] · [[Snapshot Isolation]] · [[Strict Two-Phase Locking]] · [[Transaction]]
- **Base triennale (Basi di Dati)**: [[03 - BD - SQL#Transazioni|Transazioni in SQL]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[05 - DM - Concurrency Control#Isolation levels (SQL standard)|Lecture 5 — Isolation levels (SQL standard)]]
> - [[05 - DM - Concurrency Control#PostgreSQL|Lecture 5 — PostgreSQL]]
> - [[05 - DM - Concurrency Control#READ COMMITTED|Lecture 5 — READ COMMITTED]]
> - [[05 - DM - Concurrency Control#REPEATABLE READ|Lecture 5 — REPEATABLE READ]]
