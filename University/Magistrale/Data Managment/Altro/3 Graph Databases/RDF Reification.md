---
title: RDF Reification
tags:
  - data-management
  - concept
  - rdf
---

# RDF Reification

> [!summary] In short
> Represents a whole triple as a resource (`rdf:Statement` with `rdf:subject`, `rdf:predicate`, `rdf:object`) so that statements about statements become possible.

```turtle
_:s rdf:type rdf:Statement ;
    rdf:subject :ABC ; rdf:predicate dc:creator ; rdf:object "Joe" .
_:s dc:creator "The New York Times" .      # who claims it
```

- Used for beliefs, provenance, trust, metadata about metadata.
- The four triples **do not assert** the original triple.
- If the relation itself has attributes (a date), first turn it into a resource, then reify.

## Links

- **Related concepts**: [[RDF]] · [[Blank Node]]
- **Base triennale (Basi di Dati)**: [[Reificazione]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Reification e affermazioni di ordine superiore|Lecture 3 — Reification e affermazioni di ordine superiore]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Esercizio: credenza e data|Lecture 3 — Esercizio: credenza e data]]
