---
title: Authenticated Double-Echo Broadcast
tags:
  - dependable-distributed-systems
  - concetto
  - byzantine-faults
  - broadcast
---

# Authenticated Double-Echo Broadcast

> [!summary] In breve
> Implements [[Byzantine Reliable Broadcast]]: SEND, ECHO, then **READY**. READY after an echo quorum or more than $f$ READY messages (**amplification**); deliver after more than $2f$ READY messages.

| Threshold | Action | Why |
|---|---|---|
| $> (N+f)/2$ ECHO | send READY | correct processes get READY for one value only |
| $> f$ READY | send READY | at least one comes from a correct process |
| $> 2f$ READY | deliver | at least $f+1$ correct READY messages reach everyone |

- **Totality**: a delivery implies $f+1$ correct READY messages, so every correct process amplifies, and $N-f \geq 2f+1$ READY messages reach everyone.
- Cost: 3 steps (two all-to-all), $O(N^2)$ messages, MACs only. Needs $N > 3f$.

## Collegamenti

- **Concetti correlati**: [[Byzantine Reliable Broadcast]] · [[Authenticated Echo Broadcast]] · [[Byzantine Quorum]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[14 - DDS - Byzantine Broadcast#Implementation: Authenticated Double-Echo Broadcast|Lezione 14 — Implementation: Authenticated Double-Echo Broadcast]]
> - [[14 - DDS - Byzantine Broadcast#Faulty sender: only one correct process becomes READY|Lezione 14 — Faulty sender: only one correct process becomes READY]]
