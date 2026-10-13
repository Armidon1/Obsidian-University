---
title: Sort-Merge Join
aliases:
  - Sort join
  - Two-pass sort-based algorithms
tags:
  - data-management
  - concept
  - query-processing
  - join-algorithms
  - sorting
---

# Sort-Merge Join

> [!summary] In short
> Create sorted sublists of $R$ and $S$ on $Y$, then merge them, joining tuples with equal $Y$: $3(B(R)+B(S))$ I/Os with about $\sqrt{B(R)+B(S)}$ frames.

- Same scheme for duplicate elimination / grouping ($3B$, $\sqrt B$ frames) and set/bag operations.
- Simple sort join (full sort first): $5(B(R)+B(S))$, $\sqrt{\max}$ frames.
- Problem: many tuples with the same $Y$ (fine if $Y$ is a key of one relation).
- Output sorted on $Y$; zig-zag join with tree indexes on both relations.

## Links

- **Related concepts**: [[External Merge Sort]] · [[Hash Join]] · [[Nested-Loop Join]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[08 - DM - Evaluation of Relational Operators#Sort-based|Lecture 8 — Sort-based]]
> - [[08 - DM - Evaluation of Relational Operators#Sort-merge join|Lecture 8 — Sort-merge join]]
> - [[08 - DM - Evaluation of Relational Operators#Simple sort-based join|Lecture 8 — Simple sort-based join]]
