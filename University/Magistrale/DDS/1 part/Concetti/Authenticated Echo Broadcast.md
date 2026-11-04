---
title: Authenticated Echo Broadcast
tags:
  - dependable-distributed-systems
  - concetto
  - byzantine-faults
  - broadcast
---

# Authenticated Echo Broadcast

> [!summary] In breve
> Implements [[Byzantine Consistent Broadcast]]: the sender sends to all, everyone **echoes** once to all, and a process delivers on more than $(N+f)/2$ equal echoes. Needs $N > 3f$.

- Rounds: **SEND**, then **ECHO** (every process witnesses one value only, thanks to `sentecho`).
- Only the first echo per process is recorded, so a Byzantine process cannot vote twice.
- Cost: 2 steps, $O(N^2)$ messages. Uses only [[Authenticated Perfect Links]].
- Faulty sender with $N=4$, $f=1$: votes can split 2–2 at one process, which then never delivers.

## Collegamenti

- **Concetti correlati**: [[Byzantine Consistent Broadcast]] · [[Byzantine Quorum]] · [[Authenticated Double-Echo Broadcast]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[14 - DDS - Byzantine Broadcast#Implementation: Authenticated Echo Broadcast|Lezione 14 — Implementation: Authenticated Echo Broadcast]]
> - [[14 - DDS - Byzantine Broadcast#Faulty sender|Lezione 14 — Faulty sender]]
