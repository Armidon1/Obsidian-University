---
title: Two-Phase Locking
aliases:
  - 2PL
tags:
  - data-management
  - concept
  - locking
  - concurrency-control
---

# Two-Phase Locking

> [!summary] In short
> Locking protocol where each transaction acquires all its locks before releasing any (growing phase, then shrinking phase); it guarantees conflict-serializability.

- Requires well-formed transactions and legal schedules; locks alone (without 2PL) allow the ghost update.
- Equivalent serial order: transactions sorted by their **first unlock** (lock point).
- Not all CSR schedules are 2PL: $w_1(x)\,r_2(x)\,r_3(y)\,w_1(y)$.
- Deadlocks remain possible.
- Lock anticipation: an active scheduler acquires future locks early to release others sooner.

## Links

- **Related concepts**: [[Lock Compatibility Matrix]] · [[Strict Two-Phase Locking]] · [[Deadlock Management in DBMS]] · [[Conflict-Serializability]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[05 - DM - Concurrency Control#Two-Phase Locking (2PL)|Lecture 5 — Two-Phase Locking (2PL)]]
> - [[05 - DM - Concurrency Control#2PL and conflict-serializability|Lecture 5 — 2PL and conflict-serializability]]
> - [[05 - DM - Concurrency Control#Adding shared locks|Lecture 5 — Adding shared locks]]
