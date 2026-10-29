---
title: Atomic Register
tags:
  - dependable-distributed-systems
  - concetto
  - registers
---

# Atomic Register

> [!summary] In breve
> Regular register + **ordering** (ONAR3): once a read returns a value, no later read returns an older one — no new-old inversion. Equivalent to linearizability.

- ONAR3: if a read returns $v_2$ and a later read (succeeding it) returns $v_1$, then $v_1$ is not older than $v_2$.
- Every atomic register is regular, not vice versa.
- Built from regular registers via [[Regular to Atomic Register Transformation]], or directly with [[Read-Impose Write-All]] / [[Read-Impose Write-Majority]].

## Collegamenti

- **Concetti correlati**: [[Regular Register]] · [[Linearizability]] · [[Read-Impose Write-Majority]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[13 - DDS - Registers#Register specifications: regular and atomic|Lezione 13 — Register specifications: regular and atomic]]
> - [[13 - DDS - Registers#Atomic register scenarios|Lezione 13 — Atomic register scenarios]]
