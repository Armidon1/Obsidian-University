---
title: Database Index
aliases:
  - Index (DBMS)
  - Search key
tags:
  - data-management
  - concept
  - indexing
---

# Database Index

> [!summary] In short
> Auxiliary structure that, given a value of the **search key** (any set of fields, not necessarily a key), finds the matching records quickly via **data entries** $k^*$.

Properties of an index:

1. organization: sorted, tree (ISAM, B+-tree), hash;
2. data entry structure ([[Data Entry Alternatives]]);
3. clustering / non-clustering ([[Clustering Index]]);
4. primary (search key ⊇ primary key) / secondary (unique if it contains a key);
5. dense / sparse ([[Dense and Sparse Index]]);
6. simple / composite key (prefix queries are range queries; index-only evaluation);
7. single / multi level (higher levels sparse).

## Links

- **Related concepts**: [[Data Entry Alternatives]] · [[Clustering Index]] · [[Dense and Sparse Index]] · [[B+-Tree]] · [[ISAM]] · [[Index Conformance]]
- **Base triennale (Basi di Dati)**: [[Superchiave e Chiave]] · [[Chiave Primaria]] · [[03 - BD - SQL#Indici|Indici in SQL]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[07 - DM - File Organization and Indexing#The notion of index|Lecture 7 — The notion of index]]
> - [[07 - DM - File Organization and Indexing#Properties of an index|Lecture 7 — Properties of an index]]
> - [[07 - DM - File Organization and Indexing#Sorted index organization|Lecture 7 — Sorted index organization]]
