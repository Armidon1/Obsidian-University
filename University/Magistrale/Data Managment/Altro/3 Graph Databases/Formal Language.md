---
title: Formal Language
aliases:
  - Linguaggi formali
tags:
  - data-management
  - concept
  - formal-languages
---

# Formal Language

> [!summary] In short
> A set of strings over a finite alphabet $\Sigma$, i.e. a subset of $\Sigma^*$; classified by the Chomsky hierarchy.

| Class | Generated / recognized by |
|---|---|
| Regular | regular expressions, [[Finite Automaton|finite automata]] |
| Context-free | context-free grammars, pushdown automata |
| Context-sensitive | linear bounded automata |
| Recursively enumerable | Turing machines |

- Operations: union, concatenation $L_1L_2$, Kleene star $L^*$.
- In graph databases the labels of a path form a string, and an RPQ asks whether it belongs to a language.

## Links

- **Related concepts**: [[Regular Expressions]] · [[Finite Automaton]] · [[Pumping Lemma]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Cammini ed etichette|Lecture 3 — Cammini ed etichette]]
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Espressioni regolari sui cammini|Lecture 3 — Espressioni regolari sui cammini]]
