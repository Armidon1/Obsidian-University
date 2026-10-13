---
title: Aggregate Data Model
aliases:
  - Aggregate
  - Aggregate orientation
tags:
  - data-management
  - concept
  - nosql
  - data-models
---

# Aggregate Data Model

> [!summary] In short
> An **aggregate** is a complex record (with lists and nested records) treated as a unit for retrieval, atomic update and distribution. Key-value, column-family and document stores are aggregate-oriented.

- Not a logical property of data: it reflects **access patterns** (helps some queries, hinders others, e.g. product sales history over order aggregates).
- Natural unit of **distribution** on a cluster ([[Sharding]]).
- **Transactions**: atomic updates within one aggregate; multi-aggregate atomicity is the application's job. Graph and relational DBs are aggregate-agnostic and support ACID.

| Model | Aggregate is | Access |
|---|---|---|
| [[Key-Value Store]] | opaque blob | by key only |
| [[Column-Family Store]] | row key → column families | by row key and column family |
| [[Document Database]] | transparent JSON document | queries on fields, indexes |

## Links

- **Related concepts**: [[Key-Value Store]] · [[Column-Family Store]] · [[Document Database]] · [[Sharding]] · [[Impedance Mismatch]]
- **Base triennale (Basi di Dati)**: [[NoSQL]] · [[Normalizzazione e Denormalizzazione]] · [[Transazione]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[04 - DM - Document Databases#From tuples to aggregates|Lecture 4 — From tuples to aggregates]]
> - [[04 - DM - Document Databases#Consequences of aggregate orientation|Lecture 4 — Consequences of aggregate orientation]]
> - [[04 - DM - Document Databases#Aggregate DBs: wrapping up|Lecture 4 — Aggregate DBs: wrapping up]]
