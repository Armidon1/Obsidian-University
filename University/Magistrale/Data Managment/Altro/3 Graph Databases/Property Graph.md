---
title: Property Graph
tags:
  - data-management
  - concept
  - graph-databases
---

# Property Graph

> [!summary] In short
> Labeled directed multigraph where **nodes and edges carry key-value properties**; the model used by Neo4j and queried with Cypher.

- $G=(V,E)$ over alphabet $\Sigma$, with properties $\lambda: (V\cup E)\times K \to Values$.
- Edges are first-class: they have a type, a direction and their own properties (e.g. `FRIEND {since: 2019}`).
- Differs from [[RDF]]: in RDF a property on an edge needs extra triples (reification or intermediate node).
- **Hypergraph**: an edge may connect any number of nodes.

## Links

- **Related concepts**: [[Graph Database Management System]] · [[Index-Free Adjacency]] · [[RDF]]
- **Base triennale (Basi di Dati)**: [[Graph Database]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Property graph|Lecture 3 — Property graph]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Hypergraph|Lecture 3 — Hypergraph]]
