---
title: Star Schema
tags:
  - data-management
  - concept
  - data-warehousing
  - rolap
---

# Star Schema

> [!summary] In short
> ROLAP logical schema: one central **fact table** (foreign keys + measures) referencing one **denormalized dimension table** per dimension.

```text
DATE(keyD, fullDate, month, quarter, year)
STORE(keyS, store, storeCity, state, country)
PRODUCT(keyP, product, type, category)
SALES(keyD, keyS, keyP, quantity, receipts)      -- fact table
```

- Fact key = combination of the dimension foreign keys.
- Dimension tables contain whole hierarchies → redundancy (not in [[Third Normal Form 3NF]]), accepted because the warehouse is read-mostly and joins are fewer.
- OLAP query = joins + `WHERE` (slice/dice) + `GROUP BY` (aggregation level) + `SUM`.

## Links

- **Related concepts**: [[Snowflake Schema]] · [[Surrogate Key]] · [[OLAP]] · [[Functional Dependency]]
- **Base triennale (Basi di Dati)**: [[Normalizzazione e Denormalizzazione]] · [[Foreign Key]] · [[Join]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[02 - DM - Data Warehouses#ROLAP: The Star Schema|Lecture 2 — ROLAP: The Star Schema]]
> - [[02 - DM - Data Warehouses#Why Dimension Tables Are Denormalized|Lecture 2 — Why Dimension Tables Are Denormalized]]
> - [[02 - DM - Data Warehouses#OLAP Queries over a Star Schema|Lecture 2 — OLAP Queries over a Star Schema]]
