---
title: Read-Impose Write-All
tags:
  - dependable-distributed-systems
  - concetto
  - registers
  - fail-stop
---

# Read-Impose Write-All

> [!summary] In breve
> Fail-stop atomic register: like Read-One Write-All, but a **read imposes** the value it read to all processes (a write) before returning.

- Read = "write back" the local value to all non-crashed processes, then return it → no new-old inversion.
- Uses [[Perfect Failure Detector|P]]; read and write: 2 steps, $2N$ messages.

## Collegamenti

- **Concetti correlati**: [[Read-One Write-All]] · [[Atomic Register]] · [[Read-Impose Write-Majority]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[13 - DDS - Registers#Read-Impose Write-All|Lezione 13 — Read-Impose Write-All]]
