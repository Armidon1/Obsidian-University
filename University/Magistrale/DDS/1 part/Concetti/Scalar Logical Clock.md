---
title: Scalar Logical Clock
tags:
  - dependable-distributed-systems
  - concetto
  - logical-time
---

# Scalar Logical Clock

> [!summary] In breve
> Lamport clock: an integer per process, incremented at each event and set to $\max(local, received) + 1$ on receive. Guarantees $e \to e' \Rightarrow L(e) < L(e')$, **not** the converse.

- Rules: before each event $L_i := L_i + 1$; messages carry $L_i$; on receive $L_i := \max(L_i, t_m) + 1$.
- Total order: break ties with the process id, $(L(e), i)$ — used by [[Lamport's Mutual Exclusion Algorithm]].
- Limit: from $L(e) < L(e')$ we **cannot** conclude $e \to e'$ (they may be concurrent) → [[Vector Clock]].

## Collegamenti

- **Concetti correlati**: [[Happened-Before Relation]] · [[Vector Clock]] · [[Lamport's Mutual Exclusion Algorithm]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[4 - DDS - Logical Clocks#Scalar logical clock|Lezione 4 — Scalar logical clock]]
> - [[4 - DDS - Logical Clocks#Limits of the scalar logical clock|Lezione 4 — Limits of the scalar logical clock]]
