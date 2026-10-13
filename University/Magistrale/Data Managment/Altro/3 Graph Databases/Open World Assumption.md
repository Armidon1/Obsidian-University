---
title: Open World Assumption
aliases:
  - OWA
tags:
  - data-management
  - concept
  - knowledge-graphs
  - logic
---

# Open World Assumption

> [!summary] In short
> What is not stated is **unknown**, not false. Opposite of the Closed World Assumption of databases, where what is not stored is false.

| | CWA (database) | OWA (knowledge graph) |
|---|---|---|
| Missing fact | false | unknown |
| Models | exactly one | many |
| Query answer | evaluation on the data | **certain answers** (true in every model) |
| Negation | as failure (`NOT EXISTS`) | not derivable from absence |

## Links

- **Related concepts**: [[RDFS Knowledge Graph]] · [[Certain Answers]]
- **Base triennale (Basi di Dati)**: [[Assunzione di Mondo Chiuso]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Closed World e Open World|Lecture 3 — Closed World e Open World]]
