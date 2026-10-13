---
title: Buffer Pool
aliases:
  - Database buffer
  - Buffer manager
tags:
  - data-management
  - concept
  - buffer-management
  - dbms-architecture
---

# Buffer Pool

> [!summary] In short
> Main-memory area, shared by all transactions, where the **buffer manager** caches database pages in **frames** to minimize secondary-storage accesses.

- Page = block = unit of transfer (2–64 KB); memory ops ~ns vs disk ~ms.
- **Page table**: frame → page id (PID). Per frame: **pin-count** (users) and **dirty** bit.
- Primitives: `fix` (get page, load if needed), `unfix` (release), `use` (modify, set dirty), `force` (synchronous write), `flush` (asynchronous write).
- `fix(P)`: if $P$ in a frame, pin-count++; else choose a victim with pin-count 0, write it back if dirty, read $P$.

## Links

- **Related concepts**: [[Clock Replacement Policy]] · [[Force and No-Force]] · [[Cost Model for File Organizations]]
- **Base triennale (Basi di Dati)**: [[DBMS]] · [[Page Replacement]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[06 - DM - Buffer Management#The buffer|Lecture 6 — The buffer]]
> - [[06 - DM - Buffer Management#The buffer manager|Lecture 6 — The buffer manager]]
> - [[06 - DM - Buffer Management#The Fix operation|Lecture 6 — The Fix operation]]
