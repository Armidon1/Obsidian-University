---
title: Hash Join
aliases:
  - Partitioned hash join
  - Two-pass hash-based algorithms
tags:
  - data-management
  - concept
  - query-processing
  - join-algorithms
  - hashing
---

# Hash Join

> [!summary] In short
> Partition $R$ and $S$ with the same hash function on $Y$ into $M-1$ buckets, then join each pair of buckets in memory: $3(B(R)+B(S))$ I/Os, needs only $\sqrt{\min(B(R),B(S))}$ frames.

- Same idea for duplicate elimination (hash on all attributes) and grouping (hash on grouping attributes): $3B$.
- Memory depends on the **smaller** relation (vs the sum for sort-based).
- Sensitive to skew (unequal buckets).
- Multipass: recursive partitioning with a new hash function at each level: $(2K-1)(B(R)+B(S))$.

## Links

- **Related concepts**: [[Sort-Merge Join]] · [[Hashed File]] · [[Parallel Query Processing]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[08 - DM - Evaluation of Relational Operators#Hash-based|Lecture 8 — Hash-based]]
> - [[08 - DM - Evaluation of Relational Operators#Hash join|Lecture 8 — Hash join]]
> - [[08 - DM - Evaluation of Relational Operators#Sort-based vs hash-based|Lecture 8 — Sort-based vs hash-based]]
