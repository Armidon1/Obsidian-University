---
title: K-Means
tags:
  - machine-learning
  - concetto
  - clustering
  - unsupervised-learning
---

# K-Means

> [!summary] In short
> Minimise $\sum_i\sum_{x\in C_i}d(x,\mu_i)^2$ by alternating: assign each point to the nearest centroid, recompute each centroid as the mean. Never increases the objective, but depends on initialisation and has no guarantees.

```
random μ₁..μ_k
repeat: C_i = {x : i = argmin_j ‖x − μ_j‖};  μ_i = mean(C_i)   until no change
```
- Variants: **k-medoids** (centre must be a data point), **k-median** (sum of distances, not squared).
- No bound on iterations, no approximation guarantee → repeat with several initialisations; choose $k$ by testing.

## Links

- **Related concepts**: [[Clustering]] · [[Linkage-Based Clustering]] · [[Principal Component Analysis]]
- **Map**: [[MOC - Machine Learning]]

> [!info] Full explanation
> - [[08 - ML - Clustering#4. k-means clustering|Lecture 8 — 4. k-means clustering]]
> - [[08 - ML - Clustering#Properties|Lecture 8 — Properties]]
