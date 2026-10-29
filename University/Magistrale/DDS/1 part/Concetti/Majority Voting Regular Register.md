---
title: Majority Voting Regular Register
tags:
  - dependable-distributed-systems
  - concetto
  - registers
  - fail-silent
  - quorum
---

# Majority Voting Regular Register

> [!summary] In breve
> Fail-silent regular register: values carry a **timestamp**; a write completes when a **majority** acks, a read queries everyone and returns the value with the highest timestamp among a majority of replies.

- Needs a majority of correct processes ($f < N/2$), no failure detector.
- Any read quorum intersects the last write quorum → see [[Majority Quorum]].
- Write and read: 2 steps, $2N$ messages each.

## Collegamenti

- **Concetti correlati**: [[Regular Register]] · [[Majority Quorum]] · [[Read-One Write-All]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[13 - DDS - Registers#Fail-silent algorithm — Majority Voting|Lezione 13 — Fail-silent algorithm — Majority Voting]]
> - [[13 - DDS - Registers#Idea|Lezione 13 — Idea]]
