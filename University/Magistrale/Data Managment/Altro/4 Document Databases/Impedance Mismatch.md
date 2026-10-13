---
title: Impedance Mismatch
tags:
  - data-management
  - concept
  - nosql
  - data-models
---

# Impedance Mismatch

> [!summary] In short
> The friction that arises when two cooperating systems use different data models: objects with nested structure in programs vs flat tables and records in the relational database.

- Reconstructing an object requires joins across several tables, and identifiers often differ (e.g. `Code` in storage vs `SSN` in the program).
- Solutions: object-oriented DBs, **ORM** frameworks, different data models (aggregates/documents).

## Links

- **Related concepts**: [[Aggregate Data Model]] · [[Document Database]]
- **Base triennale (Basi di Dati)**: [[JDBC]] · [[ResultSet]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[04 - DM - Document Databases#Impedance mismatch|Lecture 4 — Impedance mismatch]]
