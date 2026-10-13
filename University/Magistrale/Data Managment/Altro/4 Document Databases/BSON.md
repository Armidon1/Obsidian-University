---
title: BSON
aliases:
  - Binary JSON
tags:
  - data-management
  - concept
  - mongodb
  - json
---

# BSON

> [!summary] In short
> Binary JSON used by MongoDB: same key-value structure, plus types such as `Date`, `Timestamp`, `ObjectId`, `Double`, `Long`, `Decimal128`, regex.

- mongosh numbers default to 64-bit doubles; `NumberInt`, `NumberLong("…")`, `NumberDecimal` for exact types.
- `Date`: 64-bit milliseconds since 1970 (±≈ 292 million years each way).
- `ObjectId`: 12 bytes = 4 timestamp + 5 random + 3 counter; default `_id`.
- Max document size 16 MB (GridFS for larger files).

## Links

- **Related concepts**: [[Document Database]] · [[JSON Tree]]
- **Base triennale (Basi di Dati)**: [[Database Documentale MongoDB]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[04 - DM - Document Databases#JSON vs BSON|Lecture 4 — JSON vs BSON]]
> - [[04 - DM - Document Databases#Data types|Lecture 4 — Data types]]
> - [[04 - DM - Document Databases#Documents|Lecture 4 — Documents]]
