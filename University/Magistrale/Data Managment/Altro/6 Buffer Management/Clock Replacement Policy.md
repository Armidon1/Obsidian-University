---
title: Clock Replacement Policy
aliases:
  - Second chance
  - Clock algorithm
tags:
  - data-management
  - concept
  - buffer-management
  - replacement-policy
---

# Clock Replacement Policy

> [!summary] In short
> Approximation of LRU: a hand cycles over the frames; an unpinned frame with `referenced`=true gets a second chance (bit cleared), the first unpinned frame with `referenced`=false is the victim.

```text
loop:
  F := frames[current]
  if pin-count(F) > 0:            skip
  elif referenced(F):             referenced(F) := false; skip
  else:                           return F   // victim
  current := (current + 1) mod N
```

- `referenced` is set when pin-count drops to 0.
- Cheaper than LRU (no queue updates); LRU suffers from sequential flooding.
- Exercise: 10 frames, odd pinned, even referenced, current = 5 → victim frame 6 after clearing 6, 8, 10, 2, 4.

## Links

- **Related concepts**: [[Buffer Pool]] · [[Force and No-Force]]
- **Base triennale (Basi di Dati)**: [[Page Replacement]] · [[Anomalia di Belady]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[06 - DM - Buffer Management#Replacement policy|Lecture 6 — Replacement policy]]
> - [[06 - DM - Buffer Management#Clock replacement|Lecture 6 — Clock replacement]]
> - [[06 - DM - Buffer Management#Exercise: clock replacement|Lecture 6 — Exercise: clock replacement]]
