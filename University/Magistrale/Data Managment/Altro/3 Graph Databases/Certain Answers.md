---
title: Certain Answers
tags:
  - data-management
  - concept
  - knowledge-graphs
  - query-answering
---

# Certain Answers

> [!summary] In short
> A tuple is a certain answer to $Q$ over a KG $K$ if it is an answer in **every model** of $K$; for BGP queries it equals the ordinary answer over $comp(K)$.

$$
cert(Q,K)=\bigcap_{I\in Models(K)} ans(Q,G_I) = ans(Q, comp(K))
$$

- $comp(K) = IBC(K)$ ∪ implied `subClassOf`, `subPropertyOf`, `domain`, `range` triples.
- Practical recipe: materialize $comp(K)$, then evaluate the BGP as on a normal graph database.

## Links

- **Related concepts**: [[Instance-Based Completion]] · [[Basic Graph Pattern]] · [[Open World Assumption]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Certain answers|Lecture 3 — Certain answers]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Completion completa|Lecture 3 — Completion completa]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Esempio finale|Lecture 3 — Esempio finale]]
