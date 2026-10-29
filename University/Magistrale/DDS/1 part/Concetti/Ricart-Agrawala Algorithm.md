---
title: Ricart-Agrawala Algorithm
tags:
  - dependable-distributed-systems
  - concetto
  - mutual-exclusion
  - logical-time
---

# Ricart-Agrawala Algorithm

> [!summary] In breve
> Optimises Lamport by merging ACK and RELEASE: a process **defers its reply** while it is in the CS or has a request with higher priority. Cost: $2(N-1)$ messages.

- On REQUEST$(t, j)$: if `State = CS` or (`State = Requesting` and $(Last\_Req, i) < (t, j)$) → defer in $Q$; else reply.
- Enter the CS after $N-1$ replies; on exit, reply to all deferred requests.
- Priorities compared **lexicographically** on (timestamp, id).

## Collegamenti

- **Concetti correlati**: [[Lamport's Mutual Exclusion Algorithm]] · [[Mutual Exclusion Abstraction]] · [[Scalar Logical Clock]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[4 - DDS - Logical Clocks#Ricart-Agrawala's algorithm|Lezione 4 — Ricart-Agrawala's algorithm]]
