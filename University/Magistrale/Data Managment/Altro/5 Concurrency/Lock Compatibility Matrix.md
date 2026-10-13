---
title: Lock Compatibility Matrix
aliases:
  - Shared and exclusive locks
tags:
  - data-management
  - concept
  - locking
---

# Lock Compatibility Matrix

> [!summary] In short
> Rule deciding whether a lock request is granted: shared (S) locks are compatible with each other, exclusive (X) locks with nothing.

| held \ requested | S | X |
|---|:---:|:---:|
| **S** | yes | no |
| **X** | no | no |

- $sl_i(A)$ to read, $xl_i(A)$ to write; S → X without unlock = **lock upgrade**.
- Waiting requests are usually served first-come-first-served to avoid starvation.

## Links

- **Related concepts**: [[Two-Phase Locking]] · [[Deadlock Management in DBMS]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[05 - DM - Concurrency Control#Adding shared locks|Lecture 5 — Adding shared locks]]
> - [[05 - DM - Concurrency Control#Compatibility matrix|Lecture 5 — Compatibility matrix]]
