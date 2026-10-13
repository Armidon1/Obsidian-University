---
title: Nested-Loop Join
aliases:
  - Block nested-loop join
tags:
  - data-management
  - concept
  - query-processing
  - join-algorithms
---

# Nested-Loop Join

> [!summary] In short
> For each block of $M$ pages of the smaller relation $S$, scan the whole of $R$: cost $B(S)+B(R)\lceil B(S)/M\rceil$; always applicable, expensive for large relations.

| Variant | Cost | Example ($B(R)=1000$, $B(S)=500$) |
|---|---|---|
| tuple-based | $B(S)+p_SB(S)B(R)$ | ≈ 5,000,000 |
| page-based | $B(S)+B(S)B(R)$ | 500,500 |
| block ($M=100$) | $B(S)+B(R)\lceil B(S)/M\rceil$ | 5,500 |
| $S$ fits in memory | $B(R)+B(S)$ | 1,500 |

## Links

- **Related concepts**: [[Sort-Merge Join]] · [[Hash Join]] · [[One-Pass Algorithms]]
- **Base triennale (Basi di Dati)**: [[Join]] · [[Theta-Join]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[08 - DM - Evaluation of Relational Operators#Nested-loop join|Lecture 8 — Nested-loop join]]
> - [[08 - DM - Evaluation of Relational Operators#Block nested-loop|Lecture 8 — Block nested-loop]]
