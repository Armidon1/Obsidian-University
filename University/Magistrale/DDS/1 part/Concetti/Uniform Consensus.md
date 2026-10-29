---
title: Uniform Consensus
tags:
  - dependable-distributed-systems
  - concetto
  - consensus
---

# Uniform Consensus

> [!summary] In breve
> Consensus with **uniform agreement**: no two processes — correct **or faulty** — decide differently.

- Needed when a decision is externally visible before a possible crash (e.g. a database commit).
- [[Flooding Consensus]] is not uniform; [[Flooding Uniform Consensus]] and [[Paxos]] are.
- Used in [[Total Order Broadcast]]: uniform consensus + URB give the strongest TO specification.

## Collegamenti

- **Concetti correlati**: [[Consensus Abstraction]] · [[Flooding Uniform Consensus]] · [[Uniform Reliable Broadcast (URB)]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[8 - DDS - Consensus#Uniform consensus|Lezione 8 — Uniform consensus]]
> - [[8 - DDS - Consensus#Does Flooding Consensus satisfy uniform consensus?|Lezione 8 — Does Flooding Consensus satisfy uniform consensus?]]
