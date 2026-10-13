---
title: Iterator Model
aliases:
  - Pipelining
  - Volcano model
tags:
  - data-management
  - concept
  - query-processing
---

# Iterator Model

> [!summary] In short
> Each physical operator is an iterator with `Open`, `GetNext`, `Close`; a parent pulls one tuple at a time from its children, so a plan runs in **pipeline** without materializing intermediate results.

- Materialization: compute and store the whole intermediate result.
- Pipeline: tuple-by-tuple on demand; blocking operators (grouping, sorting) do their work in `Open`.
- Physical plan = logical plan + choice of algorithm per operator.

## Links

- **Related concepts**: [[One-Pass Algorithms]] · [[Nested-Loop Join]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[08 - DM - Evaluation of Relational Operators#Materialization or pipeline|Lecture 8 — Materialization or pipeline]]
> - [[08 - DM - Evaluation of Relational Operators#Iterators|Lecture 8 — Iterators]]
> - [[08 - DM - Evaluation of Relational Operators#Logical and physical query plans|Lecture 8 — Logical and physical query plans]]
