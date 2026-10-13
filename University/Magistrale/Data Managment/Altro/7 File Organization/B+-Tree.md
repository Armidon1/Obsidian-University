---
title: B+-Tree
aliases:
  - B+ tree
  - B-plus tree
tags:
  - data-management
  - concept
  - indexing
  - tree-index
---

# B+-Tree

> [!summary] In short
> Dynamic balanced tree index: every node is a page at least half full, data entries are in the leaves, linked in key order for range scans; insertions split nodes, deletions redistribute or merge.

- Rank $d$: non-root nodes hold between ~$d/2$ and $d$ keys; average fan-out $F\approx\frac34d$; leaves ~67% full.
- Search: root → leaf, $\log_F N$ pages ($F=100$, $10^6$ leaves → 4, or 3 with root in memory).
- **Insert**: split full leaf, **copy** the first key of the new leaf up; split full internal node, **push** the middle key up; tree grows only at the root.
- **Delete**: underflow → borrow from a sibling (redistribution, update the parent key) or **coalesce** (remove a key from the parent, possibly recursively; height may decrease).
- Clustered (alt. 1): equality $\log_F(1.5B)$; unclustered: + one I/O per match.

## Links

- **Related concepts**: [[ISAM]] · [[Database Index]] · [[Clustering Index]] · [[External Merge Sort]] · [[Index Conformance]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[07 - DM - File Organization and Indexing#B+-tree|Lecture 7 — B+-tree]]
> - [[07 - DM - File Organization and Indexing#Search|Lecture 7 — Search]]
> - [[07 - DM - File Organization and Indexing#Insertion|Lecture 7 — Insertion]]
> - [[07 - DM - File Organization and Indexing#Deletion|Lecture 7 — Deletion]]
> - [[07 - DM - File Organization and Indexing#Cost of a clustered B+-tree index|Lecture 7 — Cost of a clustered B+-tree index]]
