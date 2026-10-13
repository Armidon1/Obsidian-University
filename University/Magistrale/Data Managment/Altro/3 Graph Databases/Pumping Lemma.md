---
title: Pumping Lemma
aliases:
  - Pumping lemma
tags:
  - data-management
  - concept
  - formal-languages
---

# Pumping Lemma

> [!summary] In short
> Property of every regular language used to prove that a language is **not** regular: long enough strings contain a part that can be repeated ("pumped").

If $L$ is regular, there is $p$ such that every $w\in L$ with $|w|\ge p$ can be written $w=xyz$ with $|xy|\le p$, $|y|\ge1$ and $xy^iz\in L$ for all $i\ge0$.

- Classic use: $\{a^nb^n\mid n\ge0\}$ is not regular → no regular expression (and no RPQ) can check "same number of $a$ and $b$ edges".

## Links

- **Related concepts**: [[Formal Language]] · [[Finite Automaton]] · [[Regular Expressions]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[03 - DM - Graph Databases - RDF, SPARQL e Knowledge Graphs#Espressioni regolari sui cammini|Lecture 3 — Espressioni regolari sui cammini]]
