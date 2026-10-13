---
title: Scaling Up vs Scaling Out
aliases:
  - Vertical scaling
  - Horizontal scaling
tags:
  - data-management
  - concept
  - nosql
  - distributed-systems
---

# Scaling Up vs Scaling Out

> [!summary] In short
> **Scaling up** = a more powerful single machine; **scaling out** = more, cheaper machines in a cluster. NoSQL aggregate stores are designed to scale out.

| | Scaling up | Scaling out |
|---|---|---|
| How | more CPU/RAM/disk on one node | more nodes in a cluster |
| Cost | expensive at the high end | commodity hardware |
| Limit | physical limits | coordination, consistency |
| Failures | single point of failure | resilient to node failures |

- Scaling out requires partitioning data ([[Sharding]]) and raises the consistency trade-off of the [[CAP Theorem]].

## Links

- **Related concepts**: [[Sharding]] · [[Aggregate Data Model]] · [[CAP Theorem]]
- **Base triennale (Basi di Dati)**: [[NoSQL]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[04 - DM - Document Databases#Scaling up vs scaling out|Lecture 4 — Scaling up vs scaling out]]
