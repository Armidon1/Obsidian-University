---
title: Index-Free Adjacency
tags:
  - data-management
  - concept
  - graph-databases
---

# Index-Free Adjacency

> [!summary] In short
> Each node stores direct references to its adjacent nodes, so moving to a neighbour costs $O(1)$ and does not need an index lookup.

| | Index-free adjacency | Relational (index on FK) |
|---|---|---|
| One hop | $O(1)$ per edge | $O(\log n)$ index lookup |
| $k$ hops from one node | proportional to the visited subgraph | $k$ joins, grows with table size |

- Query cost depends on the **portion of graph traversed**, not on the total size.
- Global indexes are still useful to find the **start** nodes (e.g. "person named Alice").

## Links

- **Related concepts**: [[Graph Database Management System]] · [[Property Graph]]
- **Base triennale (Basi di Dati)**: [[Graph Database]] · [[Join]] · [[03 - BD - SQL#Indici|Indici]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Index-free adjacency|Lecture 3 — Index-free adjacency]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Costo intuitivo di una query property graph|Lecture 3 — Costo intuitivo di una query property graph]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Join contro traversal|Lecture 3 — Join contro traversal]]
