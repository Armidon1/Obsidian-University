---
title: Consensus Abstraction
tags:
  - dependable-distributed-systems
  - concetto
  - consensus
---

# Consensus Abstraction

> [!summary] In breve
> Every process **proposes** a value and all correct processes **decide** the same value, which must be one of the proposals. Impossible deterministically in asynchronous systems with even one crash (**FLP**).

- **Termination**: every correct process eventually decides.
- **Validity**: a decided value was proposed by some process.
- **Integrity**: a process decides at most once.
- **Agreement**: no two **correct** processes decide differently ([[Uniform Consensus]]: no two processes at all).
- FLP: no deterministic algorithm in an asynchronous system with one crash → use synchrony ([[Flooding Consensus]]) or partial synchrony + majority ([[Paxos]]).

## Collegamenti

- **Concetti correlati**: [[Flooding Consensus]] · [[Uniform Consensus]] · [[Paxos]] · [[Total Order Broadcast]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[8 - DDS - Consensus#The consensus problem|Lezione 8 — The consensus problem]]
> - [[8 - DDS - Consensus#The FLP impossibility result|Lezione 8 — The FLP impossibility result]]
