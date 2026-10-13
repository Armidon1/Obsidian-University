---
title: Clustering Index
aliases:
  - Clustered index
  - Strongly clustering index
  - Weakly clustering index
tags:
  - data-management
  - concept
  - indexing
---

# Clustering Index

> [!summary] In short
> An index is (strongly) **clustering** if the data records are stored in the same order as its data entries; then records with nearby keys are on the same pages and range queries are cheap. At most one per file.

- **Weakly clustering**: all records with a given value are on as few pages as possible, even if the file is not globally sorted.
- Unclustered index: one page access **per matching record** in the worst case; with many matches, scanning or sorting the file is cheaper (sort rids by page first).
- Example ($B=1000$, $T=20{,}000$, $V(A)=100$): clustered ≈ 2 + 10 pages, unclustered ≈ 2 + 200.

## Links

- **Related concepts**: [[Database Index]] · [[Dense and Sparse Index]] · [[B+-Tree]] · [[Index Conformance]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[07 - DM - File Organization and Indexing#Clustering and non-clustering|Lecture 7 — Clustering and non-clustering]]
> - [[07 - DM - File Organization and Indexing#Cost of an unclustered B+-tree index|Lecture 7 — Cost of an unclustered B+-tree index]]
