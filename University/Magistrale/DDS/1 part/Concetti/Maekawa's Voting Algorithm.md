---
title: Maekawa's Voting Algorithm
tags:
  - dependable-distributed-systems
  - concetto
  - mutual-exclusion
  - quorum
---

# Maekawa's Voting Algorithm

> [!summary] In breve
> Each process asks permission only to its **voting set** $V_i$; any two voting sets intersect, and each process votes for one requester at a time, so two processes cannot be in the CS together. Sets of size $\sim\sqrt N$.

- $V_i \cap V_j \neq \emptyset$ for all $i, j$ — the [[Majority Quorum]] idea generalised.
- Optimal size $K \sim \sqrt N$ (each process in $M = K$ sets); the grid construction gives $|V_i| = 2\sqrt N - 1$.
- Cost: $3K$ messages per CS (REQ, ACK, REL to $V_i$).
- **Not deadlock-free** in its basic form (cyclic waits between votes); fixed with timestamps/inquire messages.

## Collegamenti

- **Concetti correlati**: [[Majority Quorum]] · [[Mutual Exclusion Abstraction]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[5 - DDS - Distributed Mutual Exclusion#Quorum-based algorithm — Maekawa's voting algorithm|Lezione 5 — Quorum-based algorithm — Maekawa's voting algorithm]]
> - [[5 - DDS - Distributed Mutual Exclusion#Maekawa's algorithm is not deadlock-free|Lezione 5 — Maekawa's algorithm is not deadlock-free]]
