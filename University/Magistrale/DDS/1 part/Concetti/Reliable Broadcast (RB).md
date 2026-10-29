---
title: Reliable Broadcast (RB)
tags:
  - dependable-distributed-systems
  - concetto
  - broadcast
---

# Reliable Broadcast (RB)

> [!summary] In breve
> Adds **agreement** to BEB: if a **correct** process delivers $m$, every correct process delivers $m$ — even if the sender crashes in the middle.

- Properties: validity, no duplication, no creation, **agreement** (among correct processes).
- **Lazy RB** (fail-stop, [[Perfect Failure Detector|P]]): relay the messages of a sender when it is detected crashed.
- **Eager RB** (fail-silent): every process relays every message the first time it delivers it — $O(N^2)$ messages.
- A process that delivers and then crashes is not constrained → [[Uniform Reliable Broadcast (URB)]].

## Collegamenti

- **Concetti correlati**: [[Best Effort Broadcast (BEB)]] · [[Uniform Reliable Broadcast (URB)]] · [[FIFO Reliable Broadcast]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[7 - DDS - Broadcast Communications#(Regular) Reliable Broadcast (RB)|Lezione 7 — (Regular) Reliable Broadcast (RB)]]
> - [[7 - DDS - Broadcast Communications#BEB vs RB|Lezione 7 — BEB vs RB]]
