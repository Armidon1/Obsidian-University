---
title: Multidimensional Data Model
aliases:
  - Data cube
tags:
  - data-management
  - concept
  - data-warehousing
  - olap
---

# Multidimensional Data Model

> [!summary] In short
> Represents events of interest (**facts**) as cells of a cube whose axes are **dimensions**; each cell holds numeric **measures**, and dimensions are organized in **hierarchies**.

- **Fact**: an event (a sale, an admission); the **grain** says exactly what one fact represents.
- **Measure**: numeric property of the fact (quantity, receipts), to be aggregated.
- **Dimension**: analysis coordinate (product, store, date).
- **Hierarchy**: a tree of attributes linked by functional dependencies, e.g. $store \to city \to state \to country$.
- **Primary event** = a cell at the finest grain; **secondary event** = aggregation of primary events along hierarchies.

Relational equivalent of a cube cell: `SALES(product, store, date, quantity, receipts)` with key `(product, store, date)`.

## Links

- **Related concepts**: [[OLAP]] · [[Functional Dependency]] · [[Dimensional Fact Model]] · [[Additivity of Measures]] · [[Star Schema]]
- **Base triennale (Basi di Dati)**: [[Superchiave e Chiave]] · [[Eventi e Storicizzazione]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[02 - DM - Data Warehouses#The Multidimensional Data Model|Lecture 2 — The Multidimensional Data Model]]
> - [[02 - DM - Data Warehouses#A Three-Dimensional Sales Cube|Lecture 2 — A Three-Dimensional Sales Cube]]
> - [[02 - DM - Data Warehouses#Hierarchies and Functional Dependencies|Lecture 2 — Hierarchies and Functional Dependencies]]
