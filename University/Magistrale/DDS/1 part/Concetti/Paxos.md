---
title: Paxos
tags:
  - dependable-distributed-systems
  - concetto
  - consensus
  - paxos
---

# Paxos

> [!summary] In breve
> Consensus in partial synchrony with a majority of correct processes: **always safe**, live when a single leader is stable. Two phases (prepare/promise, accept/accepted) with numbered proposals.

- Roles: proposers, acceptors, learners.
- **Phase 1**: the proposer sends `prepare(n)`; acceptors promise not to accept lower numbers and return the highest accepted proposal.
- **Phase 2**: the proposer sends `accept(n, v)` with $v$ = value of the highest-numbered proposal reported (or its own); chosen when a **majority** accepts.
- Invariant **P2c** + intersecting majorities ⇒ once a value is chosen, every higher proposal has the same value.
- Liveness needs [[Eventual Leader Election (Omega)|Ω]] (dueling proposers otherwise).

## Collegamenti

- **Concetti correlati**: [[Consensus Abstraction]] · [[Majority Quorum]] · [[Eventual Leader Election (Omega)]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[9 - DDS - Paxos#Paxos|Lezione 9 — Paxos]]
> - [[9 - DDS - Paxos#The Paxos protocol|Lezione 9 — The Paxos protocol]]
> - [[9 - DDS - Paxos#P2c: the invariant|Lezione 9 — P2c: the invariant]]
> - [[9 - DDS - Paxos#Liveness|Lezione 9 — Liveness]]
