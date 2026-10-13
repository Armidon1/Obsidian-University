---
title: MVCC
aliases:
  - Multiversion concurrency control
  - Multiversion timestamps
tags:
  - data-management
  - concept
  - concurrency-control
  - mvcc
---

# MVCC

> [!summary] In short
> Every write creates a new **version**; reads choose the version coherent with their timestamp/snapshot, so **readers are never blocked** and never block writers.

- Multiversion timestamps: $r_i(X)$ reads the version with the largest $wts \le ts(T_i)$; $w_i(X)$ is refused if a younger transaction already read the previous version ($rts > ts(T_i)$).
- Old versions are garbage-collected; commits are delayed for recoverability.
- PostgreSQL: MVCC + locks; [[Snapshot Isolation]] at REPEATABLE READ, SSI at SERIALIZABLE.

## Links

- **Related concepts**: [[Snapshot Isolation]] · [[Timestamp-Based Concurrency Control]] · [[SQL Isolation Levels]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[05 - DM - Concurrency Control#5.7 Multiversion concurrency control|Lecture 5 — 5.7 Multiversion concurrency control]]
> - [[05 - DM - Concurrency Control#Multiversion timestamp method|Lecture 5 — Multiversion timestamp method]]
