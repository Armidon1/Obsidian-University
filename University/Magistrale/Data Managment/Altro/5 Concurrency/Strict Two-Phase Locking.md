---
title: Strict Two-Phase Locking
aliases:
  - Strict 2PL
  - SS2PL
  - Strong strict 2PL
tags:
  - data-management
  - concept
  - locking
  - recovery
---

# Strict Two-Phase Locking

> [!summary] In short
> **Strict 2PL** keeps exclusive locks until commit/rollback (→ strict schedules); **strong strict 2PL** keeps all locks until then (→ rigorous schedules, serialization order = commit order).

- Both are 2PL, hence conflict-serializable.
- SS2PL is what lock-based DBMSs implement for SERIALIZABLE (plus range locks against phantoms).

## Links

- **Related concepts**: [[Two-Phase Locking]] · [[Recoverable Schedule]] · [[SQL Isolation Levels]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[05 - DM - Concurrency Control#Strict 2PL|Lecture 5 — Strict 2PL]]
> - [[05 - DM - Concurrency Control#Strong strict 2PL (SS2PL)|Lecture 5 — Strong strict 2PL (SS2PL)]]
