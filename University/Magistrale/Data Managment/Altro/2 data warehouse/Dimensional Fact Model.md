---
title: Dimensional Fact Model
aliases:
  - DFM
tags:
  - data-management
  - concept
  - data-warehousing
  - conceptual-design
---

# Dimensional Fact Model

> [!summary] In short
> Graphical conceptual model for data marts: a **fact** box with its measures, dimensions as root attributes, and **hierarchies** drawn as trees of dimensional attributes.

| Construct | Meaning |
|---|---|
| Fact (box) | Event of interest, with its measures |
| Dimension | Root of a hierarchy, connected to the fact |
| Dimensional attribute | Node of a hierarchy; arcs = functional dependencies |
| Descriptive attribute | Extra information, not used for grouping |
| Cross-dimensional attribute | Depends on attributes of several dimensions |
| Optional arc / dimension | Value may be missing |
| Convergence | Two paths reach the same attribute |
| Shared hierarchy | Same hierarchy reused with different roles |
| Multiple arc | Many-to-many relationship (bridge table in ROLAP) |

- Starts from the ER schema of the sources: the fact usually corresponds to an entity or n-ary relationship.

## Links

- **Related concepts**: [[Multidimensional Data Model]] · [[Additivity of Measures]] · [[Star Schema]]
- **Base triennale (Basi di Dati)**: [[Modello Entità-Relazione]] · [[Vincoli di Cardinalità]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[02 - DM - Data Warehouses#The Dimensional Fact Model (DMF)|Lecture 2 — The Dimensional Fact Model (DMF)]]
> - [[02 - DM - Data Warehouses#Basic Constructs|Lecture 2 — Basic Constructs]]
> - [[02 - DM - Data Warehouses#Relationship with ER Diagrams|Lecture 2 — Relationship with ER Diagrams]]
