---
title: Perfect Failure Detector
tags:
  - dependable-distributed-systems
  - concetto
  - failure-detection
---

# Perfect Failure Detector

> [!summary] In breve
> $\mathcal{P}$: **strong completeness** (every crashed process is eventually detected by every correct process) + **strong accuracy** (no process is detected before it crashes). Needs a synchronous system.

- Implementation: **Exclude on Timeout** — heartbeat every period; a process that does not answer within the (known) bound is detected as crashed, forever.
- Used by fail-stop algorithms: [[Reliable Broadcast (RB)|Lazy RB]], All-Ack [[Uniform Reliable Broadcast (URB)|URB]], [[Flooding Consensus]], [[Leader Election|Monarchical LE]], [[Primary-Backup Replication]], [[Read-One Write-All]], [[Read-Impose Write-All]].
- A single **false suspicion** can break safety (e.g. validity of [[Read-One Write-All]]).

## Collegamenti

- **Concetti correlati**: [[Failure Detector]] · [[Eventually Perfect Failure Detector]] · [[Read-One Write-All]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[6 - DDS - Failure Detection and Leader Election#Failure detector classification|Lezione 6 — Failure detector classification]]
> - [[6 - DDS - Failure Detection and Leader Election#Lecture 7A — Failure detection|Lezione 6 — Lecture 7A — Failure detection]]
> - [[13 - DDS - Registers#Problem: the failure detector must be perfect|Lezione 13 — Problem: the failure detector must be perfect]]
