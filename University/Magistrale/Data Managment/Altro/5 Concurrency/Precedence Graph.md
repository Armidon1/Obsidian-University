---
title: Precedence Graph
aliases:
  - Conflict graph
  - Serialization graph
tags:
  - data-management
  - concept
  - serializability
---

# Precedence Graph

> [!summary] In short
> Graph with one node per transaction and an edge $T_i\to T_j$ when an action of $T_i$ conflicts with and precedes an action of $T_j$; the schedule is conflict-serializable **iff** the graph is acyclic.

- Any **topological order** gives an equivalent serial schedule.
- Polynomial check.
- **SGT scheduler**: maintains the graph online and aborts the transaction closing a cycle ($Gen(SGT)=CSR$); too costly for commercial DBMSs.
- Example: $w_1(x)\,r_2(x)\,w_1(z)\,r_2(z)\,r_3(x)\,r_4(z)\,w_4(z)\,w_2(x)$ → edges $1\to2, 1\to3, 3\to2, 1\to4, 2\to4$: acyclic, order $T_1T_3T_2T_4$.

## Links

- **Related concepts**: [[Conflict-Serializability]] · [[Deadlock Management in DBMS]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[05 - DM - Concurrency Control#Conflict-serializability and the precedence graph|Lecture 5 — Conflict-serializability and the precedence graph]]
> - [[05 - DM - Concurrency Control#Example of precedence graph|Lecture 5 — Example of precedence graph]]
> - [[05 - DM - Concurrency Control#Serialization graph testing (SGT)|Lecture 5 — Serialization graph testing (SGT)]]
