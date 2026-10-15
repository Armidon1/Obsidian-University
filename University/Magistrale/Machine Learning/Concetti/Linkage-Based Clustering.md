---
title: Linkage-Based Clustering
tags:
  - machine-learning
  - concetto
  - clustering
---

# Linkage-Based Clustering

> [!summary] In short
> Agglomerative clustering: start with one cluster per point and repeatedly merge the two closest clusters, according to single (min), average or max linkage, until a termination condition; the history is a dendrogram.

| Linkage | $D(A,B)$ |
|---|---|
| single | $\min_{x\in A,y\in B}d(x,y)$ |
| average | $\frac1{\lvert A\rvert\lvert B\rvert}\sum d(x,y)$ |
| max | $\max d(x,y)$ |

- Termination: number of clusters $k$, or all distances above a threshold $r$.
- Expensive: at least $O(m^2)$.

## Links

- **Related concepts**: [[Clustering]] · [[K-Means]] · [[Kleinberg Impossibility Theorem]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[08 - ML - Clustering#3. Linkage-based clustering|Lecture 8 — 3. Linkage-based clustering]]
> - [[08 - ML - Clustering#Termination conditions|Lecture 8 — Termination conditions]]
