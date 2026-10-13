---
title: Document Database
aliases:
  - Document store
  - Document-based data model
tags:
  - data-management
  - concept
  - nosql
  - document-databases
---

# Document Database

> [!summary] In short
> Aggregate store whose aggregates are **documents**: sets of key-value pairs with arbitrarily nested values, typically JSON; the DB can query and index fields inside documents.

- Partial retrieval and secondary indexes, unlike key-value stores.
- Schemaless → the schema is implicit in the application; optional validation (MongoDB `$jsonSchema`).
- Modelling: **embed** related data (fast reads) or **reference** it (easier updates, resolved by queries or `$lookup`).
- Tools: MongoDB, CouchDB, Couchbase, RavenDB, OrientDB.

## Links

- **Related concepts**: [[Aggregate Data Model]] · [[JSON Tree]] · [[BSON]] · [[MongoDB Aggregation Pipeline]] · [[Key-Value Store]]
- **Base triennale (Basi di Dati)**: [[Database Documentale MongoDB]] · [[JSON]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[04 - DM - Document Databases#Document-based data model|Lecture 4 — Document-based data model]]
> - [[04 - DM - Document Databases#Implications of schemaless models|Lecture 4 — Implications of schemaless models]]
> - [[04 - DM - Document Databases#Data modelling with aggregates|Lecture 4 — Data modelling with aggregates]]
