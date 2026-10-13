---
title: Snapshot Isolation
tags:
  - data-management
  - concept
  - concurrency-control
  - mvcc
  - postgresql
---

# Snapshot Isolation

> [!summary] In short
> Each transaction works on a snapshot of the database taken at its start and commits only if no concurrent transaction committed a write to the same items (first-committer/updater wins).

- Prevents dirty reads, unrepeatable reads, lost updates, phantoms.
- **Not serializable**: allows **write skew** (two transactions read overlapping data and write disjoint data), e.g. the `mytab` example of the PostgreSQL notes.
- PostgreSQL REPEATABLE READ = SI; SERIALIZABLE = SI + detection of read-write dependency cycles (SSI, error 40001).

## Links

- **Related concepts**: [[MVCC]] · [[SQL Isolation Levels]] · [[Concurrency Anomalies]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[05 - DM - Concurrency Control#Snapshot isolation|Lecture 5 — Snapshot isolation]]
> - [[05 - DM - Concurrency Control#REPEATABLE READ|Lecture 5 — REPEATABLE READ]]
> - [[05 - DM - Concurrency Control#SERIALIZABLE|Lecture 5 — SERIALIZABLE]]
