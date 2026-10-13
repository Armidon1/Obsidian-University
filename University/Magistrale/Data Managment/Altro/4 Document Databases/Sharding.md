---
title: Sharding
tags:
  - data-management
  - concept
  - nosql
  - distributed-systems
---

# Sharding

> [!summary] In short
> Partitioning the data of a database among the machines of a cluster; each portion (**shard**) is a subset of the database stored on one node.

- Divides the workload → better performance and scalability.
- Open problems: **granularity** of shards, **locating** data, **referential integrity and consistency** across nodes.
- The [[Aggregate Data Model|aggregate]] is the natural unit of sharding: all its data stays on one node.
- Relational analogue: horizontal decomposition, but across machines.

## Links

- **Related concepts**: [[Scaling Up vs Scaling Out]] · [[Aggregate Data Model]] · [[CAP Theorem]]
- **Base triennale (Basi di Dati)**: [[06 - BD - Progettazione Logica#Decomposizione orizzontale|Decomposizione orizzontale]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[04 - DM - Document Databases#Sharding|Lecture 4 — Sharding]]
