---
title: One-Pass Algorithms
tags:
  - data-management
  - concept
  - query-processing
---

# One-Pass Algorithms

> [!summary] In short
> Algorithms that read each operand once (cost $B$ or $B(R)+B(S)$) but require the (smaller) operand, or its distinct tuples / groups, to fit in the $M$ buffer frames.

| Operator | Frames | Cost |
|---|---|---|
| selection, projection | 2 | $B$ |
| duplicate elimination | distinct tuples ≤ $M-1$ | $B$ |
| grouping | groups ≤ $M-1$ | $B$ |
| binary ops, join | $\min(B(R),B(S))\le M-2$ | $B(R)+B(S)$ |

- Build an in-memory hash table / balanced tree on the smaller relation, stream the other.

## Links

- **Related concepts**: [[Nested-Loop Join]] · [[Hash Join]] · [[Iterator Model]]
- **Base triennale (Basi di Dati)**: [[Algebra Relazionale]] · [[Operatori Aggregati]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[08 - DM - Evaluation of Relational Operators#One-pass algorithms|Lecture 8 — One-pass algorithms]]
> - [[08 - DM - Evaluation of Relational Operators#Unary operators|Lecture 8 — Unary operators]]
> - [[08 - DM - Evaluation of Relational Operators#Binary operators|Lecture 8 — Binary operators]]
