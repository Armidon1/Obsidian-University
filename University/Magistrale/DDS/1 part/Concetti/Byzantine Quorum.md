---
title: Byzantine Quorum
tags:
  - dependable-distributed-systems
  - concetto
  - byzantine-faults
  - quorum
---

# Byzantine Quorum

> [!summary] In breve
> A set of **more than $(N+f)/2$ processes**. Two such sets always share a **correct** process, and one exists among the correct processes only if $N > 3f$.

- **Intersection**: $2\cdot\frac{N+f}{2} - N = f$, so two quorums overlap in more than $f$ processes, at least one of them correct.
- **Availability**: $N - f > \frac{N+f}{2} \iff N > 3f$.
- A plain [[Majority Quorum]] is not enough: its overlap may be a single Byzantine process.

| $N$ | $f$ | Quorum size | Majority |
|---|---|---|---|
| 4 | 1 | 3 | 3 |
| 7 | 2 | 5 | 4 |
| 10 | 3 | 7 | 6 |

## Collegamenti

- **Concetti correlati**: [[Majority Quorum]] · [[Authenticated Echo Broadcast]] · [[Authenticated Double-Echo Broadcast]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[14 - DDS - Byzantine Broadcast#Why the threshold is (N+f)/2, and why N > 3f|Lezione 14 — Why the threshold is (N+f)/2, and why N > 3f]]
