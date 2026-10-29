---
title: FIFO Reliable Broadcast
tags:
  - dependable-distributed-systems
  - concetto
  - broadcast
  - ordering
---

# FIFO Reliable Broadcast

> [!summary] In breve
> Reliable broadcast + **FIFO delivery**: messages broadcast by the **same sender** are delivered in the order they were sent. Nothing is said about messages from different senders.

- FIFO delivery: if $p$ broadcasts $m_1$ before $m_2$, no process delivers $m_2$ unless it has already delivered $m_1$.
- Implementation: **Broadcast with Sequence Number** — each sender numbers its messages; receivers keep, per sender, the next expected number and buffer out-of-order messages.
- Built on top of [[Reliable Broadcast (RB)]].

## Collegamenti

- **Concetti correlati**: [[Reliable Broadcast (RB)]] · [[Causal Order Broadcast]] · [[Total Order Broadcast]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[10 - DDS - Ordered Communications#FIFO Broadcast|Lezione 10 — FIFO Broadcast]]
> - [[10 - DDS - Ordered Communications#Implementation: Broadcast with Sequence Number|Lezione 10 — Implementation: Broadcast with Sequence Number]]
