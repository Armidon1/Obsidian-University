---
title: Eventual Leader Election (Omega)
tags:
  - dependable-distributed-systems
  - concetto
  - leader-election
---

# Eventual Leader Election (Omega)

> [!summary] In breve
> $\Omega$: *eventual accuracy* — there is a time after which every correct process trusts the **same correct** leader. Before that, different processes may trust different leaders.

- Weakest failure detector to solve consensus in partial synchrony.
- Crash-stop implementation: Monarchical Eventual Leader Detection on top of [[Eventually Perfect Failure Detector|◇P]].
- Crash-recovery implementation: Elect Lower Epoch (epochs count recoveries).
- [[Paxos]] uses $\Omega$ for **liveness** only: safety never depends on it.

## Collegamenti

- **Concetti correlati**: [[Leader Election]] · [[Eventually Perfect Failure Detector]] · [[Paxos]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[6 - DDS - Failure Detection and Leader Election#Lecture 7B — Leader election|Lezione 6 — Lecture 7B — Leader election]]
> - [[9 - DDS - Paxos#Liveness|Lezione 9 — Liveness]]
