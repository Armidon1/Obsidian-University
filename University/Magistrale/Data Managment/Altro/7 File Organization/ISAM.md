---
title: ISAM
aliases:
  - Indexed Sequential Access Method
tags:
  - data-management
  - concept
  - indexing
  - tree-index
---

# ISAM

> [!summary] In short
> Static, balanced tree index: leaves (data entries) allocated sequentially, internal nodes built once and never changed; insertions go to **overflow pages**.

- Fan-out $F$, height $h$: $F^h$ leaves; $F=100$, $h=4$ → $10^8$ leaves, search in 4 I/Os (vs > 25 for binary search).
- Search cost $\log_FN$.
- Deleted keys may remain as separators in internal nodes (e.g. 51 in the example).
- Degrades with many insertions → B+-tree for dynamic data.

## Links

- **Related concepts**: [[B+-Tree]] · [[Database Index]] · [[Dense and Sparse Index]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[07 - DM - File Organization and Indexing#ISAM|Lecture 7 — ISAM]]
> - [[07 - DM - File Organization and Indexing#The problem with sorted indexes|Lecture 7 — The problem with sorted indexes]]
