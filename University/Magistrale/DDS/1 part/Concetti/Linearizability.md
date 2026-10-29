---
title: Linearizability
tags:
  - dependable-distributed-systems
  - concetto
  - replication
  - consistency
---

# Linearizability

> [!summary] In breve
> Consistency criterion: every operation appears to take effect **atomically at a point** between its invocation and its response, and the resulting sequential history respects real-time order and the object's sequential specification.

- A replicated object is linearizable if it behaves like a single, non-replicated copy.
- **Sufficient condition** (for replication): all replicas apply the same updates in the **same order** (atomicity + order).
- For registers, linearizability = [[Atomic Register]].

## Collegamenti

- **Concetti correlati**: [[Primary-Backup Replication]] · [[Active Replication]] · [[Atomic Register]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[12 - DDS - Software Replication#Linearizability|Lezione 12 — Linearizability]]
> - [[12 - DDS - Software Replication#A sufficient condition for linearizability|Lezione 12 — A sufficient condition for linearizability]]
