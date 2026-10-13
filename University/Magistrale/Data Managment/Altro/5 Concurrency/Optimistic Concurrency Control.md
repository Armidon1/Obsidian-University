---
title: Optimistic Concurrency Control
aliases:
  - BOCC
  - FOCC
  - Validation-based concurrency control
tags:
  - data-management
  - concept
  - concurrency-control
---

# Optimistic Concurrency Control

> [!summary] In short
> Transactions run without checks on a private workspace (read phase), are **validated** at commit against read and write sets, and only then write (deferred writes); suited to low-conflict workloads.

| | BOCC | FOCC |
|---|---|---|
| Validate against | committed transactions | active transactions |
| Condition | $RS(t_j)\cap WS(t_i)=\emptyset$ | $WS(t_j)\cap RS^*(t_i)=\emptyset$ |
| On failure | abort $t_j$ | abort $t_j$ or $t_i$, or wait |

- Both produce conflict-serializable schedules; FOCC needs no validation for read-only transactions.

## Links

- **Related concepts**: [[Timestamp-Based Concurrency Control]] · [[Two-Phase Locking]] · [[Conflict-Serializability]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[05 - DM - Concurrency Control#5.8 Optimistic concurrency control|Lecture 5 — 5.8 Optimistic concurrency control]]
> - [[05 - DM - Concurrency Control#Backward-oriented OCC (BOCC)|Lecture 5 — Backward-oriented OCC (BOCC)]]
> - [[05 - DM - Concurrency Control#Forward-oriented OCC (FOCC)|Lecture 5 — Forward-oriented OCC (FOCC)]]
