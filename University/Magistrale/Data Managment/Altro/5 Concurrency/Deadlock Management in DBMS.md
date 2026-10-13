---
title: Deadlock Management in DBMS
aliases:
  - Wait-die
  - Wait-for graph
tags:
  - data-management
  - concept
  - locking
  - deadlock
---

# Deadlock Management in DBMS

> [!summary] In short
> Transactions waiting for each other’s locks: handled by **timeout**, **detection** on the wait-for graph (kill a transaction in a cycle) or **prevention** with priorities (wait-die).

| Technique | Idea | Issue |
|---|---|---|
| Timeout | kill after waiting $t$ | choosing $t$; repeated victims |
| Wait-for graph | cycle ⇒ deadlock, kill one | maintaining the graph |
| Wait-die | $T_i$ may wait for $T_j$ only if $pr(T_i)>pr(T_j)$, else killed | unnecessary aborts |

- Probability grows linearly with the number of transactions and quadratically with locks per transaction.
- PostgreSQL uses detection (`deadlock detected`, SQLSTATE 40P01).

## Links

- **Related concepts**: [[Two-Phase Locking]] · [[Precedence Graph]] · [[Deadlock]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[05 - DM - Concurrency Control#Deadlock management|Lecture 5 — Deadlock management]]
> - [[05 - DM - Concurrency Control#Deadlock recognition|Lecture 5 — Deadlock recognition]]
> - [[05 - DM - Concurrency Control#Deadlock prevention: wait-die|Lecture 5 — Deadlock prevention: wait-die]]
