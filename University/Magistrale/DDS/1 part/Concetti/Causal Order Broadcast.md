---
title: Causal Order Broadcast
tags:
  - dependable-distributed-systems
  - concetto
  - broadcast
  - ordering
---

# Causal Order Broadcast

> [!summary] In breve
> Delivery respects the **causal (happened-before) order** between broadcasts: if $m_1 \to m_2$, every process delivers $m_1$ before $m_2$. Causal = FIFO + local order.

- $m_1 \to m_2$ if the same process broadcast $m_1$ before $m_2$, or a process delivered $m_1$ before broadcasting $m_2$, or by transitivity (see [[Happened-Before Relation]]).
- Concurrent messages can be delivered in different orders at different processes.
- Implementations: [[Waiting Causal Broadcast]] (vector clocks) and [[No-Waiting Causal Broadcast]] (piggyback the past).

## Collegamenti

- **Concetti correlati**: [[FIFO Reliable Broadcast]] · [[Waiting Causal Broadcast]] · [[No-Waiting Causal Broadcast]] · [[Happened-Before Relation]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[10 - DDS - Ordered Communications#Causal Order Broadcast|Lezione 10 — Causal Order Broadcast]]
> - [[10 - DDS - Ordered Communications#Causal = FIFO + Local order|Lezione 10 — Causal = FIFO + Local order]]
