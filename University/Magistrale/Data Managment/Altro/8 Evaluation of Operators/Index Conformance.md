---
title: Index Conformance
aliases:
  - Index-based selection
  - Index nested-loop join
tags:
  - data-management
  - concept
  - query-processing
  - indexing
---

# Index Conformance

> [!summary] In short
> An index **conforms** to a condition when it can evaluate it: a tree index if the condition has terms on a **prefix** of its key, a hash index if it has equality terms on **all** its key attributes.

- Selection with a matching index: key `=` → 3–4 I/Os (tree) or 1–2 (hash); non-key `=` → + $B(R)/V(R,A)$ (clustering) or up to $T(R)/V(R,A)$ (non-clustering).
- Index-only scan for projections on attributes in the search key.
- **Index nested-loop join**: $B(R)+T(R)\times$(lookup + $B(S)/V(S,Y)$) with a clustering index on $S.Y$; good when $R$ is small.

## Links

- **Related concepts**: [[Database Index]] · [[B+-Tree]] · [[Clustering Index]] · [[Nested-Loop Join]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[08 - DM - Evaluation of Relational Operators#Conformance of an index to a condition|Lecture 8 — Conformance of an index to a condition]]
> - [[08 - DM - Evaluation of Relational Operators#Index-based selection|Lecture 8 — Index-based selection]]
> - [[08 - DM - Evaluation of Relational Operators#Index-based join|Lecture 8 — Index-based join]]
