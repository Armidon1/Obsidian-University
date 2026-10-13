---
title: Cost Model for File Organizations
aliases:
  - Page I/O cost model
tags:
  - data-management
  - concept
  - file-organization
  - cost-model
---

# Cost Model for File Organizations

> [!summary] In short
> Since a page I/O ($D\approx15$ ms) costs ~$10^5$ times processing a record ($C\approx100$ ns), operations are measured by the **number of page accesses** in the worst case.

| | Scan | Equality | Range | Insert | Delete |
|---|---|---|---|---|---|
| Heap | $B$ | $B$ | $B$ | $O(1)$ | $B$ |
| Sorted | $B$ | $\log_2B$ | $\log_2B+$ matches | $B$ | $B$ |
| Hashed | $1.25B$ | $O(1)$ | $B$ | $O(1)$ | $O(1)$ |
| Clustered B+-tree | $1.5B$ | $\log_F1.5B$ | $\log_F1.5B+$ matches | $\log_F1.5B$ | $\log_F1.5B$ |

$B$ pages, $R$ records per page, $F$ fan-out. No organization is best for everything.

## Links

- **Related concepts**: [[Heap File]] · [[Hashed File]] · [[B+-Tree]] · [[Buffer Pool]] · [[One-Pass Algorithms]]
- **Base triennale (Basi di Dati)**: [[Modello di Costo]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[07 - DM - File Organization and Indexing#Cost model|Lecture 7 — Cost model]]
> - [[07 - DM - File Organization and Indexing#Sorted file costs|Lecture 7 — Sorted file costs]]
> - [[07 - DM - File Organization and Indexing#Comparison|Lecture 7 — Comparison]]
> - [[07 - DM - File Organization and Indexing#Discussion|Lecture 7 — Discussion]]
