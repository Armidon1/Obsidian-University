---
title: Conflict-Serializability
aliases:
  - CSR
tags:
  - data-management
  - concept
  - serializability
---

# Conflict-Serializability

> [!summary] In short
> A schedule is conflict-serializable if it can be turned into a serial one by swapping adjacent **non-conflicting** actions; equivalently, its precedence graph is acyclic.

- Conflict: different transactions, same element, at least one write ($rw$, $wr$, $ww$).
- $S_1, S_2$ conflict-equivalent ⇔ same order of all conflicting pairs.
- CSR ⊂ VSR; CSR is monotone, prefix- and commit-closed: the largest monotone subclass of VSR.
- Variants: OCSR (keeps order of non-overlapping transactions), COCSR (commit order = serialization order).

## Links

- **Related concepts**: [[Precedence Graph]] · [[View-Serializability]] · [[Two-Phase Locking]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[05 - DM - Concurrency Control#Conflict-equivalence|Lecture 5 — Conflict-equivalence]]
> - [[05 - DM - Concurrency Control#Conflict-serializability and the precedence graph|Lecture 5 — Conflict-serializability and the precedence graph]]
> - [[05 - DM - Concurrency Control#Order-preserving variants|Lecture 5 — Order-preserving variants]]
