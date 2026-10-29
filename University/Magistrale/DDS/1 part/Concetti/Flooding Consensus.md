---
title: Flooding Consensus
tags:
  - dependable-distributed-systems
  - concetto
  - consensus
---

# Flooding Consensus

> [!summary] In breve
> Synchronous, fail-stop consensus: in each round every process broadcasts the set of proposals it knows; a process decides (e.g. the minimum) when a round passes **without new crashes**.

- Uses [[Best Effort Broadcast (BEB)]] and [[Perfect Failure Detector|P]].
- At most $N$ rounds (at most $N-1$ crashes can change the views).
- A process that decides early and crashes may have decided a value others do not → not **uniform**; see [[Flooding Uniform Consensus]].

## Collegamenti

- **Concetti correlati**: [[Consensus Abstraction]] · [[Flooding Uniform Consensus]] · [[Perfect Failure Detector]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[8 - DDS - Consensus#Flooding Consensus (synchronous systems)|Lezione 8 — Flooding Consensus (synchronous systems)]]
> - [[8 - DDS - Consensus#When the early decider crashes|Lezione 8 — When the early decider crashes]]
