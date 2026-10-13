---
title: RDFS Knowledge Graph
aliases:
  - RDFS
  - Knowledge Graph
tags:
  - data-management
  - concept
  - rdfs
  - knowledge-graphs
---

# RDFS Knowledge Graph

> [!summary] In short
> A set of RDF triples using the RDFS vocabulary (`rdf:type`, `rdfs:subClassOf`, `rdfs:subPropertyOf`, `rdfs:domain`, `rdfs:range`) with a logical semantics, so that implicit facts can be inferred.

| Triple | First-order meaning |
|---|---|
| `a rdf:type C` | $C(a)$ |
| `C rdfs:subClassOf D` | $\forall x\,(C(x)\to D(x))$ |
| `P rdfs:subPropertyOf Q` | $\forall x,y\,(P(x,y)\to Q(x,y))$ |
| `P rdfs:domain C` | $\forall x,y\,(P(x,y)\to C(x))$ |
| `P rdfs:range C` | $\forall x,y\,(P(x,y)\to C(y))$ |

- **Legal** KG: pure individuals, classes and properties are disjoint and used only in their positions.
- An interpretation is a **model** if it satisfies every triple; a KG has **many** models (open world).

## Links

- **Related concepts**: [[Open World Assumption]] · [[Instance-Based Completion]] · [[Certain Answers]] · [[RDF]]
- **Base triennale (Basi di Dati)**: [[ISA e Generalizzazione]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Knowledge Graph e RDFS|Lecture 3 — Knowledge Graph e RDFS]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Forme ammesse delle triple|Lecture 3 — Forme ammesse delle triple]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Semantica: interpretazioni e modelli|Lecture 3 — Semantica: interpretazioni e modelli]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Collegamento con la logica del primo ordine|Lecture 3 — Collegamento con la logica del primo ordine]]
