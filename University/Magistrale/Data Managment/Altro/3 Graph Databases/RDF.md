---
title: RDF
aliases:
  - Resource Description Framework
tags:
  - data-management
  - concept
  - rdf
  - semantic-web
---

# RDF

> [!summary] In short
> W3C data model where all information is a set of **triples (subject, predicate, object)**, i.e. an edge-labeled directed graph.

| Term | Subject | Predicate | Object |
|---|:---:|:---:|:---:|
| URI/IRI | ✓ | ✓ | ✓ |
| Literal | | | ✓ |
| Blank node | ✓ | | ✓ |

- Vocabularies: `rdf:`, `rdfs:`, `dc:`, `foaf:`.
- Same URI can be node and edge label → statements about properties.
- Serializations: Turtle, N-Triples, N3, RDF/XML (the model is one, syntaxes many).
- Storage perspectives: relational (triple table, property tables, vertical partitioning), entity, graph.

## Links

- **Related concepts**: [[Blank Node]] · [[RDF Reification]] · [[SPARQL]] · [[RDFS Knowledge Graph]] · [[Property Graph]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Modello RDF|Lecture 3 — Modello RDF]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#URI, literal e blank node|Lecture 3 — URI, literal e blank node]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Sintassi RDF|Lecture 3 — Sintassi RDF]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Memorizzazione di RDF|Lecture 3 — Memorizzazione di RDF]]
