---
title: Parallel Query Processing
aliases:
  - Shared-nothing
tags:
  - data-management
  - concept
  - query-processing
  - parallel-databases
---

# Parallel Query Processing

> [!summary] In short
> In a **shared-nothing** architecture each relation is partitioned among $P$ nodes (round robin, range, hash); operators run on the partitions in parallel, dividing elapsed time by about $P$.

| Partitioning | Good for | Weakness |
|---|---|---|
| round robin | balance | always reads everything |
| range on $A$ | range predicates | skew |
| hash | equality, full scans | ranges |

- Hash partitioning on the grouping / join attributes makes grouping and joins **local**.
- Join of $R, S$ initially on one node: $(B(R)+B(S))(P+4)/P$ instead of $3(B(R)+B(S))$.

## Links

- **Related concepts**: [[Hash Join]] · [[Sharding]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[08 - DM - Evaluation of Relational Operators#Parallel algorithms|Lecture 8 — Parallel algorithms]]
> - [[08 - DM - Evaluation of Relational Operators#Horizontal data partitioning|Lecture 8 — Horizontal data partitioning]]
> - [[08 - DM - Evaluation of Relational Operators#Performance|Lecture 8 — Performance]]
