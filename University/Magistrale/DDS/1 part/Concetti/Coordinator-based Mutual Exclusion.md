---
title: Coordinator-based Mutual Exclusion
tags:
  - dependable-distributed-systems
  - concetto
  - mutual-exclusion
---

# Coordinator-based Mutual Exclusion

> [!summary] In breve
> A central **coordinator** grants the CS: request → grant → release, 3 messages per CS, but the coordinator is a single point of failure and a bottleneck.

- The coordinator keeps a FIFO queue of pending requests and grants one at a time.
- Safety and liveness are trivial if the coordinator is correct.
- If it crashes a new one must be elected ([[Leader Election]]) and the state rebuilt.

## Collegamenti

- **Concetti correlati**: [[Mutual Exclusion Abstraction]] · [[Token Ring Mutual Exclusion]] · [[Leader Election]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[5 - DDS - Distributed Mutual Exclusion#Coordinator-based mutual exclusion|Lezione 5 — Coordinator-based mutual exclusion]]
