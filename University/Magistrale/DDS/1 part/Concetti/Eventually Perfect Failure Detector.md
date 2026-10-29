---
title: Eventually Perfect Failure Detector
tags:
  - dependable-distributed-systems
  - concetto
  - failure-detection
---

# Eventually Perfect Failure Detector

> [!summary] In breve
> $\Diamond\mathcal{P}$: strong completeness + **eventual strong accuracy** — it may make mistakes, but after an unknown time it stops suspecting correct processes. Implementable in partially synchronous systems.

- Implementation: **Increasing Timeout** — on a false suspicion (a heartbeat arrives from a suspected process) restore it and increase the timeout.
- Once the timeout exceeds the (unknown) bound of the stable period, no more false suspicions.
- Algorithms using it must tolerate wrong suspicions: they usually also need a **majority of correct processes** (e.g. [[Paxos]], [[Majority Voting Regular Register]]).

## Collegamenti

- **Concetti correlati**: [[Failure Detector]] · [[Perfect Failure Detector]] · [[Eventual Leader Election (Omega)]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[6 - DDS - Failure Detection and Leader Election#Failure detector classification|Lezione 6 — Failure detector classification]]
> - [[6 - DDS - Failure Detection and Leader Election#Lecture 7A — Failure detection|Lezione 6 — Lecture 7A — Failure detection]]
