---
title: CAP Theorem
aliases:
  - Teorema CAP
  - Brewer theorem
tags:
  - data-management
  - concept
  - distributed-systems
  - nosql
  - consistency
---

# CAP Theorem

> [!summary] In short
> A distributed data store cannot guarantee at the same time **Consistency**, **Availability** and **Partition tolerance**: when the network partitions, it must give up consistency or availability.

| Letter | Meaning |
|---|---|
| C | every read sees the latest write (one up-to-date copy) |
| A | every request to a live node gets an answer |
| P | the system keeps working despite lost messages between nodes |

- Partitions happen in clusters, so the real choice is **CP** (refuse requests to stay consistent) vs **AP** (answer, possibly with stale data).
- **BASE** (*Basically Available, Soft state, Eventual consistency*) is the AP approach of many NoSQL stores, opposed to [[ACID]].
- Not covered explicitly by the slides: it explains why "running on clusters" and ACID transactions are in tension.

## Links

- **Related concepts**: [[ACID]] · [[Sharding]] · [[Scaling Up vs Scaling Out]] · [[Aggregate Data Model]]
- **Base triennale (Basi di Dati)**: [[NoSQL]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[04 - DM - Document Databases#Main NoSQL characteristics|Lecture 4 — Main NoSQL characteristics]]
> - [[04 - DM - Document Databases#Consequences of aggregate orientation|Lecture 4 — Consequences of aggregate orientation]]
