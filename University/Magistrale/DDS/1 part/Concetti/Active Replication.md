---
title: Active Replication
tags:
  - dependable-distributed-systems
  - concetto
  - replication
---

# Active Replication

> [!summary] In breve
> **State machine replication**: the client sends the request to **all replicas**, which execute it in the same order (via total order broadcast); no failover needed.

- Requires **deterministic** operations and [[Total Order Broadcast]].
- A crash of a replica is transparent: the others keep answering.
- Compared to [[Primary-Backup Replication]]: more computation, no recovery delay.

## Collegamenti

- **Concetti correlati**: [[Primary-Backup Replication]] · [[Total Order Broadcast]] · [[Linearizability]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[12 - DDS - Software Replication#Active replication|Lezione 12 — Active replication]]
> - [[12 - DDS - Software Replication#How to guarantee linearizability|Lezione 12 — How to guarantee linearizability]]
