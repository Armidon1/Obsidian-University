---
title: Best Effort Broadcast (BEB)
tags:
  - dependable-distributed-systems
  - concetto
  - broadcast
---

# Best Effort Broadcast (BEB)

> [!summary] In breve
> The sender sends the message to everyone over perfect links: **if the sender is correct**, every correct process delivers it. Nothing is promised if the sender crashes.

- **BEB1 validity**: if $p_i$ and $p_j$ are correct, every message broadcast by $p_i$ is eventually delivered by $p_j$.
- **BEB2 no duplication**, **BEB3 no creation**.
- Implementation (Basic Broadcast): $N$ `pp2p` sends — 1 step, $N$ messages.
- Building block of [[Reliable Broadcast (RB)]] and of all the register algorithms ([[Read-One Write-All]], [[Majority Voting Regular Register]], …).

## Collegamenti

- **Concetti correlati**: [[Reliable Broadcast (RB)]] · [[Uniform Reliable Broadcast (URB)]] · [[Probabilistic Broadcast (Gossip)]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[7 - DDS - Broadcast Communications#Best Effort Broadcast (BEB)|Lezione 7 — Best Effort Broadcast (BEB)]]
> - [[13 - DDS - Registers#Communication primitives|Lezione 13 — Communication primitives]]
