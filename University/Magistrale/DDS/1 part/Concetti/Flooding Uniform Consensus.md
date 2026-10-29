---
title: Flooding Uniform Consensus
tags:
  - dependable-distributed-systems
  - concetto
  - consensus
---

# Flooding Uniform Consensus

> [!summary] In breve
> Uniform variant of flooding: processes **always run all $N$ rounds** and decide only at the end, so everybody decides on the same set of proposals.

- No early decision → a crashed process cannot have decided anything different.
- Cost: always $N$ rounds, even without failures.

## Collegamenti

- **Concetti correlati**: [[Flooding Consensus]] · [[Uniform Consensus]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[8 - DDS - Consensus#Flooding Uniform Consensus (synchronous systems)|Lezione 8 — Flooding Uniform Consensus (synchronous systems)]]
