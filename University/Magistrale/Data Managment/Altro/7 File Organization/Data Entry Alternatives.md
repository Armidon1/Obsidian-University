---
title: Data Entry Alternatives
aliases:
  - Alternative 1 2 3
tags:
  - data-management
  - concept
  - indexing
---

# Data Entry Alternatives

> [!summary] In short
> A data entry $k^*$ can be (1) the **data record** itself, (2) a pair $(k, rid)$, or (3) a pair $(k, rid\text{-}list)$.

| Alternative | Content | Notes |
|---|---|---|
| 1 | the record | index = file organization; at most one per file; dense and clustered |
| 2 | $(k, rid)$ | index independent from data file; duplicates repeat $k$ |
| 3 | $(k, [rid_1, \ldots])$ | compact for duplicates; variable-length entries |

## Links

- **Related concepts**: [[Database Index]] · [[Clustering Index]] · [[Inverted List]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[07 - DM - File Organization and Indexing#Structure of data entries|Lecture 7 — Structure of data entries]]
