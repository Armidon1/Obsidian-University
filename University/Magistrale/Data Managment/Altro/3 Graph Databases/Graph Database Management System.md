---
title: Graph Database Management System
aliases:
  - GDBMS
tags:
  - data-management
  - concept
  - graph-databases
  - nosql
---

# Graph Database Management System

> [!summary] In short
> A DBMS exposing a graph data model with CRUD operations; it may use **native** graph storage/processing (index-free adjacency) or store the graph in a relational or other back end.

- Types by model: **property graph** (Neo4j), **hypergraph**, **RDF triple store**.
- Native storage: data laid out as nodes and relationships; native processing: traversals follow physical pointers.
- Non-native: graph on top of relational/document stores → traversals become joins or index lookups.
- Graph physical representations: adjacency list, incidence list, adjacency matrix, incidence matrix, compressed adjacency matrix.

## Links

- **Related concepts**: [[Index-Free Adjacency]] · [[Property Graph]] · [[RDF]] · [[ACID]]
- **Base triennale (Basi di Dati)**: [[Graph Database]] · [[NoSQL]] · [[DBMS]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Graph Database Management Systems|Lecture 3 — Graph Database Management Systems]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Storage e processing nativi|Lecture 3 — Storage e processing nativi]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Rappresentazione fisica dei grafi|Lecture 3 — Rappresentazione fisica dei grafi]]
