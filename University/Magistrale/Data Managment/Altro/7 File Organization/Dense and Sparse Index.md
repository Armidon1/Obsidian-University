---
title: Dense and Sparse Index
aliases:
  - Dense index
  - Sparse index
tags:
  - data-management
  - concept
  - indexing
---

# Dense and Sparse Index

> [!summary] In short
> **Dense**: every search key value in the file has a data entry; **sparse**: only some (typically one per page, the first key). A sparse index must be clustering.

| Dense | Sparse |
|---|---|
| existence check without the file | must access the data page |
| more space | ~ one entry per page: fits in memory |
| any number per file | at most one (needs sorted file) |

- **Strongly dense**: one entry per record (rids). Sparse entries point to pages.
- Example: $10^6$ records, 10 per page, 100 entries per index page → dense 10,000 pages, sparse 1,000, second level 10.

## Links

- **Related concepts**: [[Database Index]] · [[Clustering Index]] · [[ISAM]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[07 - DM - File Organization and Indexing#Dense and sparse|Lecture 7 — Dense and sparse]]
> - [[07 - DM - File Organization and Indexing#Clustering sorted index on a key (unique)|Lecture 7 — Clustering sorted index on a key (unique)]]
> - [[07 - DM - File Organization and Indexing#Multi-level clustering sorted index|Lecture 7 — Multi-level clustering sorted index]]
