---
title: Instance-Based Completion
aliases:
  - IBC
tags:
  - data-management
  - concept
  - knowledge-graphs
  - reasoning
---

# Instance-Based Completion

> [!summary] In short
> Fixpoint procedure that adds to a KG every instance triple implied by `subClassOf`, `subPropertyOf`, `domain` and `range`; for instance triples $K\models T \iff T\in IBC(K)$.

```text
K1 := K ∪ immediately deducible triples
repeat  K0 := K1
  (X type C), (C subClassOf D)    ⇒ add (X type D)
  (X P Y),    (P subPropertyOf Q) ⇒ add (X Q Y)
  (X P Y),    (P domain C)        ⇒ add (X type C)
  (X P Y),    (P range C)         ⇒ add (Y type C)
until K1 = K0
```

- Terminates: only finitely many triples over the symbols of $K$.
- The interpretation built from $IBC(K)$ is a model of $K$.
- Schema-level implications are tested by adding fresh individuals.

## Links

- **Related concepts**: [[RDFS Knowledge Graph]] · [[Certain Answers]]
- **Base triennale (Basi di Dati)**: [[04 - BD - Accesso ai Dati da Software#Esempio, chiusura transitiva di un grafo|Chiusura transitiva (punto fisso)]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Instance-Based Completion|Lecture 3 — Instance-Based Completion]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Proprietà fondamentali di IBC|Lecture 3 — Proprietà fondamentali di IBC]]
