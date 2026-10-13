---
title: SPARQL
tags:
  - data-management
  - concept
  - rdf
  - query-languages
---

# SPARQL

> [!summary] In short
> W3C query language for RDF: a query matches a **Basic Graph Pattern** against the graph and returns variable bindings (SELECT) or a new graph (CONSTRUCT).

```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?name (COUNT(?y) AS ?n)
WHERE { ?x foaf:name ?name . ?x foaf:knows+ ?y .
        OPTIONAL { ?x foaf:mbox ?m } FILTER (!BOUND(?m)) }
GROUP BY ?name
```

| SPARQL | Relational analogue |
|---|---|
| BGP (`.` between patterns) | joins on shared variables |
| `FILTER` | selection |
| `OPTIONAL` | left outer join |
| `UNION`, `MINUS` / `NOT EXISTS` | union, difference |
| property path `p+` | transitive closure (RPQ) |
| `GROUP BY`/`HAVING` | same |

## Links

- **Related concepts**: [[Basic Graph Pattern]] · [[RDF]] · [[Certain Answers]] · [[Regular Expressions]]
- **Base triennale (Basi di Dati)**: [[Join Esterno]] · [[Regular Path Query]] · [[Group By e Having]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#SPARQL|Lecture 3 — SPARQL]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#OPTIONAL|Lecture 3 — OPTIONAL]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Negazione come fallimento|Lecture 3 — Negazione come fallimento]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Property path|Lecture 3 — Property path]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#CONSTRUCT|Lecture 3 — CONSTRUCT]]
