---
title: Waiting Causal Broadcast
tags:
  - dependable-distributed-systems
  - concetto
  - broadcast
  - ordering
---

# Waiting Causal Broadcast

> [!summary] In breve
> Causal broadcast with **vector clocks**: each message carries the sender's vector; a receiver **buffers** it until it has delivered every message that causally precedes it.

- $V[j]$ = number of messages from $p_j$ delivered so far.
- Deliver $m$ with vector $W$ when $W \le V$ component-wise (all its causal past is delivered).
- Messages stay small ($N$ integers) but delivery may be delayed.

## Collegamenti

- **Concetti correlati**: [[Causal Order Broadcast]] · [[No-Waiting Causal Broadcast]] · [[Vector Clock]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[10 - DDS - Ordered Communications#Implementation 1: Waiting Causal Broadcast|Lezione 10 — Implementation 1: Waiting Causal Broadcast]]
