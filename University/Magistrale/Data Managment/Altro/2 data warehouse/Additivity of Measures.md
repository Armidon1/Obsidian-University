---
title: Additivity of Measures
tags:
  - data-management
  - concept
  - data-warehousing
  - olap
---

# Additivity of Measures

> [!summary] In short
> A measure is **additive along a dimension** if summing it along that dimension is meaningful; otherwise other aggregate operators (AVG, MIN, MAX, last value) must be used.

| Measure type | Example | Sum over time? | Sum over other dims? |
|---|---|:---:|:---:|
| Flow | units sold per day | yes | yes |
| Level (stock) | inventory level | **no** | yes |
| Unit | unit price, percentage | no | no |

- Count of distinct customers is not additive across products (one customer buys many products).
- Rule: the valid operator depends on measure semantics, grain and the dimension being rolled up.

## Links

- **Related concepts**: [[OLAP]] · [[Multidimensional Data Model]] · [[Dimensional Fact Model]]
- **Base triennale (Basi di Dati)**: [[Operatori Aggregati]] · [[Group By e Having]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[02 - DM - Data Warehouses#Additivity|Lecture 2 — Additivity]]
> - [[02 - DM - Data Warehouses#Flow, Level, and Unit Measures|Lecture 2 — Flow, Level, and Unit Measures]]
> - [[02 - DM - Data Warehouses#Additive and Non-Additive Measures|Lecture 2 — Additive and Non-Additive Measures]]
