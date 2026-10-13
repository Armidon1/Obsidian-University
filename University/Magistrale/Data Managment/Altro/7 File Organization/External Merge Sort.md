---
title: External Merge Sort
aliases:
  - Multipass merge sort
  - External sorting
tags:
  - data-management
  - concept
  - sorting
  - file-organization
---

# External Merge Sort

> [!summary] In short
> Sorts a file larger than memory with $F$ buffer frames: pass 0 creates sorted runs of $F$ pages, each later pass merges $F-1$ runs; cost $2B(\lceil\log_{F-1}\lceil B/F\rceil\rceil+1)$ page I/Os.

- 2-way version: 3 frames, $2B(\lceil\log_2B\rceil+1)$.
- **Two passes** suffice if $B\le F(F-1)\approx F^2$; $N$ passes if $B\le F(F-1)^{N-1}$.
- Example: 12,500 pages, 10 frames → 1,250 runs → 139 → 16 → 2 → 1: 5 passes, 125,000 I/Os.
- Used for ORDER BY, DISTINCT, bulk-loading B+-trees, sort-merge join.

## Links

- **Related concepts**: [[Sort-Merge Join]] · [[B+-Tree]] · [[Cost Model for File Organizations]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[07 - DM - File Organization and Indexing#External sorting|Lecture 7 — External sorting]]
> - [[07 - DM - File Organization and Indexing#2-way external merge sort|Lecture 7 — 2-way external merge sort]]
> - [[07 - DM - File Organization and Indexing#Multipass (k-way) merge sort|Lecture 7 — Multipass (k-way) merge sort]]
