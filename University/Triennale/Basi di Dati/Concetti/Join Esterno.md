---
title: Join Esterno
tags:
  - basi-di-dati
  - concetto
  - algebra-relazionale
  - sql
---

# Join Esterno

> [!summary] In breve
> Join che conserva le tuple che non si combinano, estendendole con NULL: sinistro, destro o completo.

| Versione | Mantiene |
|---|---|
| sinistro (`left join`) | tutte le tuple del primo operando |
| destro (`right join`) | tutte le tuple del secondo operando |
| completo (`full join`) | le tuple di entrambi |

Esempio: padre di ogni persona e, se nota, la madre → `paternita left join maternita`.

## Collegamenti

- **Concetti correlati**: [[Join]] · [[Valore Nullo]]
- **Mappa**: [[MOC - Basi di Dati]]
- **Data Management (magistrale)**: [[MongoDB Aggregation Pipeline]] · [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#OPTIONAL|SPARQL OPTIONAL]]

> [!info] Approfondimento
> - [[02 - BD - Modello Relazionale#Join esterno|Lezione 2 — Join esterno]]
> - [[03 - BD - SQL#Join esterno|Lezione 3 — Join esterno]]
