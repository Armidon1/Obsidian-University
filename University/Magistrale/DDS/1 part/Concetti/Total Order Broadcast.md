---
title: Total Order Broadcast
tags:
  - dependable-distributed-systems
  - concetto
  - broadcast
  - ordering
  - consensus
---

# Total Order Broadcast

> [!summary] In breve
> All processes deliver messages in the **same order**, whatever their sender (atomic broadcast). Orthogonal to FIFO/causal and **equivalent to consensus**.

- Specifications vary along two axes: **agreement** (uniform / non-uniform) and **order** (uniform / non-uniform), giving several TO variants.
- Implementation: messages are disseminated with [[Reliable Broadcast (RB)|RB]]/[[Uniform Reliable Broadcast (URB)|URB]]; a sequence of [[Consensus Abstraction|consensus]] instances decides the next batch, delivered in a deterministic order.
- [[Uniform Consensus]] + URB → the strongest TO specification.
- Basis of [[Active Replication]].

## Collegamenti

- **Concetti correlati**: [[Consensus Abstraction]] · [[Causal Order Broadcast]] · [[Active Replication]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[10 - DDS - Ordered Communications#Total Order Broadcast|Lezione 10 — Total Order Broadcast]]
> - [[11 - DDS - Total Order Broadcast#TO specifications|Lezione 11 — TO specifications]]
> - [[11 - DDS - Total Order Broadcast#Combining agreement and order|Lezione 11 — Combining agreement and order]]
> - [[11 - DDS - Total Order Broadcast#Total Order implementation|Lezione 11 — Total Order implementation]]
