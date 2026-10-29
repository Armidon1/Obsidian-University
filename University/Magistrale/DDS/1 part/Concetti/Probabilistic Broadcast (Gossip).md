---
title: Probabilistic Broadcast (Gossip)
tags:
  - dependable-distributed-systems
  - concetto
  - broadcast
  - gossip
---

# Probabilistic Broadcast (Gossip)

> [!summary] In breve
> Scalable broadcast with **probabilistic** guarantees: each process forwards the message to $k$ random processes (fan-out) for a bounded number of rounds; delivery happens to all with high probability.

- Motivation: ack implosion of deterministic broadcasts with large $N$.
- **Eager Probabilistic Broadcast**: gossip to $k$ targets for $r$ rounds.
- Validity becomes "*with probability* $1-\varepsilon$"; no duplication and no creation stay deterministic.

## Collegamenti

- **Concetti correlati**: [[Best Effort Broadcast (BEB)]] · [[Reliable Broadcast (RB)]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[7 - DDS - Broadcast Communications#Probabilistic broadcast|Lezione 7 — Probabilistic broadcast]]
> - [[7 - DDS - Broadcast Communications#Gossip dissemination|Lezione 7 — Gossip dissemination]]
> - [[7 - DDS - Broadcast Communications#Eager Probabilistic Broadcast|Lezione 7 — Eager Probabilistic Broadcast]]
