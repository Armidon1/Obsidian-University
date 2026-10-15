---
title: Kleinberg Impossibility Theorem
tags:
  - machine-learning
  - concetto
  - clustering
  - theory
---

# Kleinberg Impossibility Theorem

> [!summary] In short
> No clustering function can satisfy scale invariance, richness and consistency at the same time (Kleinberg 2003).

| Property | Meaning |
|---|---|
| scale invariance | $F(X,\alpha d)=F(X,d)$ |
| richness | every partition is the output for some $d$ |
| consistency | shrinking within-cluster and enlarging between-cluster distances keeps the output |

Fixing the number of clusters $k$ circumvents it (k-means satisfies relaxed versions).

## Links

- **Related concepts**: [[Clustering]] · [[K-Means]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[08 - ML - Clustering#5. Kleinberg's impossibility theorem|Lecture 8 — 5. Kleinberg's impossibility theorem]]
