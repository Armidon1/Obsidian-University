---
title: Failure Detector
tags:
  - dependable-distributed-systems
  - concetto
  - failure-detection
---

# Failure Detector

> [!summary] In breve
> An oracle, local to each process, that outputs the set of processes it **suspects** to have crashed. It encapsulates timing assumptions and is classified by **completeness** and **accuracy**.

- **Completeness** (liveness): crashed processes are eventually suspected.
- **Accuracy** (safety): correct processes are not suspected (always = strong, eventually = eventual).
- Implemented with heartbeats and timeouts: what the timeout can guarantee depends on the timing model.

| Detector | Completeness | Accuracy | Timing model |
|---|---|---|---|
| [[Perfect Failure Detector]] $\mathcal{P}$ | strong | strong | synchronous |
| [[Eventually Perfect Failure Detector]] $\Diamond\mathcal{P}$ | strong | eventual strong | partially synchronous |

## Collegamenti

- **Concetti correlati**: [[Perfect Failure Detector]] · [[Eventually Perfect Failure Detector]] · [[Leader Election]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[6 - DDS - Failure Detection and Leader Election#Failure detector abstraction|Lezione 6 — Failure detector abstraction]]
> - [[6 - DDS - Failure Detection and Leader Election#Failure detector classification|Lezione 6 — Failure detector classification]]
