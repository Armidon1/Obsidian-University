---
title: Blank Node
aliases:
  - bnode
tags:
  - data-management
  - concept
  - rdf
---

# Blank Node

> [!summary] In short
> An RDF node without a URI (`_:x`): an anonymous resource whose existence is asserted but which is not globally identified.

```turtle
:Marco foaf:knows _:x .
_:x foaf:birthDate "01-06" .
```

- Allowed as subject or object, never as predicate.
- Used for n-ary relations (an intermediate "friendship" node with a `since` date) and for [[RDF Reification]].
- Not a query variable: `?x` in SPARQL can match many resources; `_:x` denotes one resource local to the graph.

## Links

- **Related concepts**: [[RDF]] · [[RDF Reification]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Blank node|Lecture 3 — Blank node]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Relazioni n-arie in RDF|Lecture 3 — Relazioni n-arie in RDF]]
