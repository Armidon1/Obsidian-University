---
title: Force and No-Force
aliases:
  - Force policy
  - No-force policy
  - Steal
tags:
  - data-management
  - concept
  - buffer-management
  - recovery
---

# Force and No-Force

> [!summary] In short
> **Force**: at commit all pages modified by the transaction are written to disk; **no-force**: they are written later, asynchronously (`flush`). No-force is the usual choice.

- No-force avoids many random writes at commit and writes hot pages once.
- Durability then relies on the **log** (write-ahead logging + redo after a crash).
- Steal/no-steal (writing uncommitted pages) decides whether recovery also needs undo; most systems use steal + no-force.

## Links

- **Related concepts**: [[Buffer Pool]] · [[ACID]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[06 - DM - Buffer Management#Force or no-force strategy|Lecture 6 — Force or no-force strategy]]
> - [[06 - DM - Buffer Management#The other operations|Lecture 6 — The other operations]]
