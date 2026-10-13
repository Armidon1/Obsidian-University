---
title: Hashed File
aliases:
  - Static hashing
tags:
  - data-management
  - concept
  - file-organization
  - hashing
---

# Hashed File

> [!summary] In short
> Pages grouped in $N$ **buckets** (primary page + overflow chain); a record with search key $k$ is in bucket $h(k) \bmod N$. Equality in $O(1)$, ranges need a full scan.

- Pages kept ~80% full → $1.25B$ pages.
- Equality: 1 access + overflow pages; insertion $2D+RC$; scan and range $1.25B$.
- Fixed $N$: long overflow chains as the file grows; dynamic variants are **extendible** and **linear hashing**.

## Links

- **Related concepts**: [[Heap File]] · [[Cost Model for File Organizations]] · [[Hash Join]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[07 - DM - File Organization and Indexing#Hashed file|Lecture 7 — Hashed file]]
> - [[07 - DM - File Organization and Indexing#Hashed file costs (rough)|Lecture 7 — Hashed file costs (rough)]]
