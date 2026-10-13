---
title: ROLAP and MOLAP
aliases:
  - ROLAP
  - MOLAP
  - HOLAP
tags:
  - data-management
  - concept
  - data-warehousing
  - olap
---

# ROLAP and MOLAP

> [!summary] In short
> Two ways to implement the multidimensional model: **ROLAP** on relational tables and SQL, **MOLAP** on native multidimensional arrays; **HOLAP** mixes them.

| | ROLAP | MOLAP |
|---|---|---|
| Storage | relational tables (star/snowflake) | arrays / cubes |
| Query | generated SQL (joins + GROUP BY) | direct cell access |
| Scalability | high | limited by sparsity |
| Speed | slower aggregations | very fast, pre-aggregated cubes |
| Problem | join cost | **sparsity**: most cells empty |

- MOLAP may **materialize** secondary cubes in advance; storage cost grows quickly.

## Links

- **Related concepts**: [[OLAP]] · [[Star Schema]] · [[Multidimensional Data Model]]
- **Base triennale (Basi di Dati)**: [[Modello Relazionale]] · [[Vista]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[02 - DM - Data Warehouses#ROLAP|Lecture 2 — ROLAP]]
> - [[02 - DM - Data Warehouses#MOLAP|Lecture 2 — MOLAP]]
> - [[02 - DM - Data Warehouses#The Sparsity Problem|Lecture 2 — The Sparsity Problem]]
> - [[02 - DM - Data Warehouses#Hybrid OLAP|Lecture 2 — Hybrid OLAP]]
