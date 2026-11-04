---
title: Byzantine Consistent Broadcast
tags:
  - dependable-distributed-systems
  - concetto
  - byzantine-faults
  - broadcast
---

# Byzantine Consistent Broadcast

> [!summary] In breve
> Single-instance broadcast with a designated sender: correct processes that deliver, deliver the **same** message, but with a faulty sender some may deliver **nothing**.

- **BCB1 Validity**: a correct sender's message is delivered by every correct process.
- **BCB2 No duplication**: every correct process delivers at most **one** message.
- **BCB3 Integrity**: if the sender is correct, a delivered message really was broadcast by it.
- **BCB4 Consistency**: two correct processes never deliver different messages.
- No uniform variant exists in the Byzantine model.
- Implementation: [[Authenticated Echo Broadcast]]. Without **totality** → [[Byzantine Reliable Broadcast]].

## Collegamenti

- **Concetti correlati**: [[Authenticated Echo Broadcast]] · [[Byzantine Reliable Broadcast]] · [[Reliable Broadcast (RB)]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[14 - DDS - Byzantine Broadcast#Byzantine consistent broadcast|Lezione 14 — Byzantine consistent broadcast]]
> - [[14 - DDS - Byzantine Broadcast#Correct and faulty state|Lezione 14 — Correct and faulty state]]
