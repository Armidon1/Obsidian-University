---
title: View-Serializability
aliases:
  - VSR
tags:
  - data-management
  - concept
  - serializability
---

# View-Serializability

> [!summary] In short
> A schedule is view-serializable if it has the same **READS-FROM** relation and the same **FINAL-WRITE** set as some serial schedule.

- Most general notion in the read/write model.
- Checking equivalence: polynomial; checking view-serializability: **NP-complete**.
- **Not monotone** (a projection of a VSR schedule may not be VSR) → not used in practice.
- Example VSR not CSR: $r_1(x)\,w_2(x)\,w_1(x)\,w_3(x)$ (blind write of $T_3$).

## Links

- **Related concepts**: [[Conflict-Serializability]] · [[Schedule (Concurrency)]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[05 - DM - Concurrency Control#View-equivalence|Lecture 5 — View-equivalence]]
> - [[05 - DM - Concurrency Control#Complexity of view-serializability|Lecture 5 — Complexity of view-serializability]]
> - [[05 - DM - Concurrency Control#Monotone classes of schedules|Lecture 5 — Monotone classes of schedules]]
