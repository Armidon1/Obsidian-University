---
title: Data Warehouse
tags:
  - data-management
  - concept
  - data-warehousing
---

# Data Warehouse

> [!summary] In short
> A collection of data that supports decision making: **subject-oriented, integrated, time-variant and non-volatile**, physically separated from the operational (OLTP) databases.

| Property | Meaning |
|---|---|
| Subject-oriented | Organized around business subjects (customer, product), not applications |
| Integrated | Data from many sources reconciled: names, codes, units, identifiers |
| Time-variant | Stores history; time is part of fact identification |
| Non-volatile | Loaded periodically and then read, almost never updated in place |

- Fed by [[ETL]]; analysed with [[OLAP]]; modelled with the [[Multidimensional Data Model]].
- Architectures: single-layer (virtual, unused), **two-layer** (sources → warehouse + data marts), **three-layer** (adds a reconciled layer).
- A **data mart** is a subset of the warehouse for one department or subject.

## Links

- **Related concepts**: [[OLAP]] · [[OLTP]] · [[DSS]] · [[ETL]] · [[Multidimensional Data Model]]
- **Base triennale (Basi di Dati)**: [[Base di Dati]] · [[Sistema Informativo]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[02 - DM - Data Warehouses#Definition and Fundamental Properties of a Data Warehouse|Lecture 2 — Definition and Fundamental Properties of a Data Warehouse]]
> - [[02 - DM - Data Warehouses#Data Warehouse Architectures|Lecture 2 — Data Warehouse Architectures]]
> - [[02 - DM - Data Warehouses#Data Marts|Lecture 2 — Data Marts]]
