---
title: Mutual Exclusion Abstraction
tags:
  - dependable-distributed-systems
  - concetto
  - mutual-exclusion
---

# Mutual Exclusion Abstraction

> [!summary] In breve
> Processes compete for a **critical section** (CS) through `request`/`release`; the abstraction must guarantee **mutual exclusion** (safety) and **no deadlock / no starvation** (liveness).

- **ME1 (safety)**: at most one process in the CS at any time.
- **ME2 (liveness)**: every request is eventually granted (no deadlock, no starvation).
- Optional: **fairness** (requests served in happened-before order).

| Approach | Algorithm |
|---|---|
| Permission from a coordinator | [[Coordinator-based Mutual Exclusion]] |
| Token | [[Token Ring Mutual Exclusion]] |
| Permission from everybody (logical clocks) | [[Lamport's Mutual Exclusion Algorithm]], [[Ricart-Agrawala Algorithm]] |
| Permission from a quorum | [[Maekawa's Voting Algorithm]] |

## Collegamenti

- **Concetti correlati**: [[Lamport's Mutual Exclusion Algorithm]] · [[Ricart-Agrawala Algorithm]] · [[Coordinator-based Mutual Exclusion]] · [[Token Ring Mutual Exclusion]] · [[Maekawa's Voting Algorithm]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[4 - DDS - Logical Clocks#The mutual exclusion abstraction|Lezione 4 — The mutual exclusion abstraction]]
> - [[5 - DDS - Distributed Mutual Exclusion#The abstraction|Lezione 5 — The abstraction]]
> - [[5 - DDS - Distributed Mutual Exclusion#Comparison|Lezione 5 — Comparison]]
