---
title: Transaction
aliases:
  - Transazioni
  - Database transaction
tags:
  - data-management
  - concept
  - transactions
---

# Transaction

> [!summary] In short
> A sequence of reads and writes on a database forming a **single logical unit**, delimited by `begin` and ending with `commit` or `rollback`, which should satisfy the ACID properties.

- Abstract form: $r_i(A)$, $w_i(A)$, $c_i$, $a_i$ (local computations ignored).
- States: active (running/blocked), committed, aborted.
- In SQL: autocommit for single statements; `BEGIN … COMMIT|END|ROLLBACK`.
- Concurrency control makes the interleaving of transactions behave like a serial execution.

## Links

- **Related concepts**: [[ACID]] · [[Schedule (Concurrency)]] · [[SQL Isolation Levels]]
- **Base triennale (Basi di Dati)**: [[Transazione]] · [[03 - BD - SQL#Transazioni|Transazioni in SQL]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[05 - DM - Concurrency Control#Transactions|Lecture 5 — Transactions]]
> - [[05 - DM - Concurrency Control#ACID properties|Lecture 5 — ACID properties]]
> - [[05 - DM - Concurrency Control#Transactions in SQL|Lecture 5 — Transactions in SQL]]
