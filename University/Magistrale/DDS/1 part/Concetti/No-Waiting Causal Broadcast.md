---
title: No-Waiting Causal Broadcast
tags:
  - dependable-distributed-systems
  - concetto
  - broadcast
  - ordering
---

# No-Waiting Causal Broadcast

> [!summary] In breve
> Causal broadcast that **piggybacks the causal past** (the list of preceding messages) on every message: the receiver delivers the missing past first, then the message — never waits.

- No buffering, but messages grow with the history → needs garbage collection of the past.
- Trade-off with [[Waiting Causal Broadcast]]: message size vs delivery latency.

## Collegamenti

- **Concetti correlati**: [[Causal Order Broadcast]] · [[Waiting Causal Broadcast]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[10 - DDS - Ordered Communications#Implementation 2: No-Waiting Causal Broadcast|Lezione 10 — Implementation 2: No-Waiting Causal Broadcast]]
