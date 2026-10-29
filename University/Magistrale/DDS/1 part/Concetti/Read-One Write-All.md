---
title: Read-One Write-All
tags:
  - dependable-distributed-systems
  - concetto
  - registers
  - fail-stop
---

# Read-One Write-All

> [!summary] In breve
> Fail-stop regular register: a **write** is sent to all and completes when all non-crashed processes ack; a **read** returns the **local** copy.

- Uses [[Best Effort Broadcast (BEB)]], perfect links and [[Perfect Failure Detector|P]].
- Write: 2 steps, $2N$ messages; read: 0 messages.
- Validity fails with a single false suspicion → the detector **must be perfect**.

## Collegamenti

- **Concetti correlati**: [[Regular Register]] · [[Perfect Failure Detector]] · [[Majority Voting Regular Register]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[13 - DDS - Registers#Fail-stop algorithm — Read-One Write-All|Lezione 13 — Fail-stop algorithm — Read-One Write-All]]
> - [[13 - DDS - Registers#Problem: the failure detector must be perfect|Lezione 13 — Problem: the failure detector must be perfect]]
