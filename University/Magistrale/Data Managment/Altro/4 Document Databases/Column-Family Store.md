---
title: Column-Family Store
aliases:
  - Column-family data model
  - Wide-column store
tags:
  - data-management
  - concept
  - nosql
---

# Column-Family Store

> [!summary] In short
> Two-level aggregate model (from Google BigTable): a **row key** selects the aggregate, whose columns are grouped in **column families**; rows may have different columns.

- Row-oriented view: a row is an aggregate (≈ document); column-oriented view: a column family is like a table with variable columns.
- **Supercolumn**: a column containing a map of columns; slow, since all sub-columns must be deserialized.
- Tools: Cassandra, HBase, Hypertable, SimpleDB.
- ≠ **column store** (MonetDB, Vertica): relational DBMS storing data physically by columns.

## Links

- **Related concepts**: [[Aggregate Data Model]] · [[Key-Value Store]] · [[Document Database]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[04 - DM - Document Databases#Column-family data model|Lecture 4 — Column-family data model]]
> - [[04 - DM - Document Databases#Supercolumn family|Lecture 4 — Supercolumn family]]
> - [[04 - DM - Document Databases#Tools|Lecture 4 — Tools]]
