---
title: Inverted List
aliases:
  - Bucket index
  - Posting list
tags:
  - data-management
  - concept
  - indexing
  - information-retrieval
---

# Inverted List

> [!summary] In short
> For each search key value, a bucket (list) of pointers to all records with that value: realizes alternative 3 for non-clustering indexes with duplicates.

- Conjunctive queries = **intersection** of pointer sets (Toy department ∩ 2nd floor), before touching the data file.
- Information retrieval: word → documents; AND / OR / AND NOT = intersection / union / difference.

## Links

- **Related concepts**: [[Data Entry Alternatives]] · [[Database Index]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[07 - DM - File Organization and Indexing#Non-clustering sorted index on a non-key|Lecture 7 — Non-clustering sorted index on a non-key]]
