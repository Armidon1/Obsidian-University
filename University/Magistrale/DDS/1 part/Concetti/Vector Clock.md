---
title: Vector Clock
tags:
  - dependable-distributed-systems
  - concetto
  - logical-time
  - causality
---

# Vector Clock

> [!summary] In breve
> A vector of $N$ counters per process; characterises causality **exactly**: $e \to e' \iff V(e) < V(e')$, and incomparable vectors mean concurrent events.

- $V_i[i]$ counts the events of $p_i$; messages carry the vector; on receive $V_i := \max(V_i, V_m)$ component-wise, then increment $V_i[i]$.
- $V \le V' \iff \forall k: V[k] \le V'[k]$; $V < V' \iff V \le V' \wedge V \ne V'$.
- Cost: $O(N)$ integers per message.
- Used by [[Waiting Causal Broadcast]] to decide whether a message can be delivered.

## Collegamenti

- **Concetti correlati**: [[Scalar Logical Clock]] · [[Happened-Before Relation]] · [[Causal Order Broadcast]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[4 - DDS - Logical Clocks#Vector clock|Lezione 4 — Vector clock]]
> - [[4 - DDS - Logical Clocks#Properties|Lezione 4 — Properties]]
