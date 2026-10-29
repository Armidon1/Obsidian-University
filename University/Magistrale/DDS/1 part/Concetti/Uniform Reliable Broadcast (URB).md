---
title: Uniform Reliable Broadcast (URB)
tags:
  - dependable-distributed-systems
  - concetto
  - broadcast
---

# Uniform Reliable Broadcast (URB)

> [!summary] In breve
> **Uniform agreement**: if *any* process (correct or not) delivers $m$, every correct process delivers $m$. Deliver only when the message is "safe" at enough processes.

- Why: a process may deliver, act on the outside world, then crash — RB lets the others ignore that message.
- **All-Ack URB** (fail-stop): deliver when all non-crashed processes have relayed $m$.
- **Majority-Ack URB** (fail-silent): deliver when a **majority** has relayed $m$; needs $f < N/2$.
- Used by consensus-based [[Total Order Broadcast]] to obtain uniform agreement.

## Collegamenti

- **Concetti correlati**: [[Reliable Broadcast (RB)]] · [[Perfect Failure Detector]] · [[Majority Quorum]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[7 - DDS - Broadcast Communications#Uniform Reliable Broadcast (URB)|Lezione 7 — Uniform Reliable Broadcast (URB)]]
> - [[7 - DDS - Broadcast Communications#Why RB is not enough|Lezione 7 — Why RB is not enough]]
> - [[7 - DDS - Broadcast Communications#BEB vs RB vs URB|Lezione 7 — BEB vs RB vs URB]]
