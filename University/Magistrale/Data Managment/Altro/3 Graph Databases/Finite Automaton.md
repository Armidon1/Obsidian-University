---
title: Finite Automaton
aliases:
  - Automi a stati finiti
  - DFA
  - NFA
tags:
  - data-management
  - concept
  - formal-languages
---

# Finite Automaton

> [!summary] In short
> Abstract machine with a finite set of states that reads a string symbol by symbol and accepts it if it ends in a final state; recognizes exactly the **regular languages**.

- $A=(Q,\Sigma,\delta,q_0,F)$; DFA: $\delta: Q\times\Sigma\to Q$; NFA: $\delta: Q\times\Sigma\to 2^Q$ (equivalent power, subset construction).
- Every regular expression can be turned into an NFA (Thompson) and vice versa (Kleene).
- In graph databases an RPQ is evaluated on the **product** of the graph with the automaton of the expression: a pair $(x,y)$ is an answer iff $(y,q_f)$ is reachable from $(x,q_0)$.

## Links

- **Related concepts**: [[Regular Expressions]] · [[Formal Language]] · [[Pumping Lemma]]
- **Base triennale (Basi di Dati)**: [[Regular Path Query]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Espressioni regolari sui cammini|Lecture 3 — Espressioni regolari sui cammini]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Regular Path Query|Lecture 3 — Regular Path Query]]
