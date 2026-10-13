---
title: Recoverable Schedule
aliases:
  - ACR
  - Strict schedule
  - Rigorous schedule
  - Cascading rollback
tags:
  - data-management
  - concept
  - transactions
  - recovery
---

# Recoverable Schedule

> [!summary] In short
> With rollbacks, schedules must also be **recoverable** (no commit before the transactions one read from); stronger classes avoid cascading rollbacks (ACR), simplify undo (strict) or fix the serialization order to the commit order (rigorous).

| Class | Condition |
|---|---|
| Recoverable | $T_i$ commits after every $T_j$ it read from |
| ACR | read only committed values |
| Strict | read and overwrite only committed values |
| Rigorous | between conflicting $a_i$ and $b_j$ there is $c_i$ |

serial ⊂ rigorous ⊂ strict ⊂ ACR ⊂ recoverable; orthogonal to serializability (but rigorous ⇒ COCSR).

## Links

- **Related concepts**: [[Strict Two-Phase Locking]] · [[Concurrency Anomalies]] · [[Conflict-Serializability]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[05 - DM - Concurrency Control#Recoverable schedules|Lecture 5 — Recoverable schedules]]
> - [[05 - DM - Concurrency Control#Avoiding cascading rollback (ACR)|Lecture 5 — Avoiding cascading rollback (ACR)]]
> - [[05 - DM - Concurrency Control#Strict schedules|Lecture 5 — Strict schedules]]
> - [[05 - DM - Concurrency Control#Rigorous schedules|Lecture 5 — Rigorous schedules]]
