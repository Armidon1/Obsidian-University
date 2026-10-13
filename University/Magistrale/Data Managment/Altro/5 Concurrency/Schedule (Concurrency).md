---
title: Schedule (Concurrency)
aliases:
  - Schedule
  - Serializability
tags:
  - data-management
  - concept
  - transactions
  - serializability
---

# Schedule (Concurrency)

> [!summary] In short
> A sequence of the actions of a set of transactions respecting the order inside each transaction; **serial** if transactions do not interleave, **serializable** if equivalent to some serial schedule.

- Partial schedule = prefix of a schedule.
- Equivalence (general): same outcome from every initial state → undecidable in general, hence view- and conflict-equivalence.
- Hierarchy: serial ⊂ COCSR ⊂ OCSR ⊂ CSR ⊂ VSR ⊂ serializable.

## Links

- **Related concepts**: [[Transaction]] · [[View-Serializability]] · [[Conflict-Serializability]] · [[Concurrency Anomalies]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[05 - DM - Concurrency Control#Schedules and serial schedules|Lecture 5 — Schedules and serial schedules]]
> - [[05 - DM - Concurrency Control#Serializability|Lecture 5 — Serializability]]
> - [[05 - DM - Concurrency Control#Simplifying the notion of schedule|Lecture 5 — Simplifying the notion of schedule]]
