---
title: Basic Graph Pattern
aliases:
  - BGP
tags:
  - data-management
  - concept
  - rdf
  - query-languages
---

# Basic Graph Pattern

> [!summary] In short
> A set of triple patterns with variables; its answers are the images of the **homomorphisms** from the pattern to the RDF graph.

A homomorphism $h: B \to G$ maps constants to themselves, variables to resources, and every triple $(\alpha\,\beta\,\gamma)\in B$ to a triple $(h(\alpha)\,h(\beta)\,h(\gamma))\in G$.

$$
ans(Q,G)=\{\langle h(?x_1),\ldots,h(?x_m)\rangle \mid h \text{ homomorphism from } B \text{ to } G\}
$$

- Equivalent to a conjunctive query (select-project-join) over the triple table.

## Links

- **Related concepts**: [[SPARQL]] · [[Certain Answers]]
- **Base triennale (Basi di Dati)**: [[Algebra Relazionale]] · [[Theta-Join]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Basic Graph Pattern|Lecture 3 — Basic Graph Pattern]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Semantica tramite omomorfismi|Lecture 3 — Semantica tramite omomorfismi]]
