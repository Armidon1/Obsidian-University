---
title: Snowflake Schema
tags:
  - data-management
  - concept
  - data-warehousing
  - rolap
---

# Snowflake Schema

> [!summary] In short
> A star schema in which some dimension tables are **normalized**: transitive dependencies are moved to secondary dimension tables.

```text
STORE(keyS, store, keyC, salesManager)    -- primary dimension table
CITY(keyC, storeCity, state, country)     -- secondary dimension table
```

| | Star | Snowflake |
|---|---|---|
| Redundancy | high | lower |
| Joins per query | few | more |
| Storage | larger dimensions | smaller |
| Typical choice | default | very large or shared hierarchy portions |

- A correct decomposition splits along a functional dependency (e.g. $storeCity \to state$).

## Links

- **Related concepts**: [[Star Schema]] · [[Functional Dependency]] · [[Third Normal Form 3NF]]
- **Base triennale (Basi di Dati)**: [[Normalizzazione e Denormalizzazione]] · [[06 - BD - Progettazione Logica#Decomposizione verticale|Decomposizione verticale]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[02 - DM - Data Warehouses#The Snowflake Schema|Lecture 2 — The Snowflake Schema]]
> - [[02 - DM - Data Warehouses#Correct Snowflake Decomposition|Lecture 2 — Correct Snowflake Decomposition]]
> - [[02 - DM - Data Warehouses#Star versus Snowflake|Lecture 2 — Star versus Snowflake]]
