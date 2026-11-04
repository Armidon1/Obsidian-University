---
title: Byzantine Reliable Broadcast
tags:
  - dependable-distributed-systems
  - concetto
  - byzantine-faults
  - broadcast
---

# Byzantine Reliable Broadcast

> [!summary] In breve
> [[Byzantine Consistent Broadcast]] + **totality**: if any correct process delivers, every correct process eventually delivers. Together with consistency this gives agreement: all or none.

- **BRB1–BRB4** = BCB1–BCB4. **BRB5 Totality**: if some message is delivered by any correct process, every correct process eventually delivers a message.
- Fail-arbitrary equivalent of [[Reliable Broadcast (RB)]], restricted to **one message**.
- With a faulty sender, it is still allowed that **nobody** delivers.
- Implementation: [[Authenticated Double-Echo Broadcast]].

## Collegamenti

- **Concetti correlati**: [[Byzantine Consistent Broadcast]] · [[Authenticated Double-Echo Broadcast]] · [[Reliable Broadcast (RB)]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[14 - DDS - Byzantine Broadcast#Byzantine Reliable Broadcast|Lezione 14 — Byzantine Reliable Broadcast]]
