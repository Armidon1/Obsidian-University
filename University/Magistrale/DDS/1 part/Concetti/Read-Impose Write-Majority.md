---
title: Read-Impose Write-Majority
tags:
  - dependable-distributed-systems
  - concetto
  - registers
  - fail-silent
  - quorum
---

# Read-Impose Write-Majority

> [!summary] In breve
> Fail-silent atomic register: [[Majority Voting Regular Register|majority voting]] + the reader **imposes** the value with the highest timestamp on a majority before returning.

- Read: query a majority, pick the highest timestamp, write it back to a majority, return it.
- Needs $f < N/2$; read: 4 steps, $4N$ messages; write: 2 steps, $2N$ messages.

| Register | Fail-stop ([[Perfect Failure Detector\|P]]) | Fail-silent (majority) |
|---|---|---|
| Regular | [[Read-One Write-All]] | [[Majority Voting Regular Register]] |
| Atomic | [[Read-Impose Write-All]] | Read-Impose Write-Majority |

## Collegamenti

- **Concetti correlati**: [[Majority Voting Regular Register]] · [[Atomic Register]] · [[Majority Quorum]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[13 - DDS - Registers#Read-Impose Write-Majority|Lezione 13 — Read-Impose Write-Majority]]
> - [[13 - DDS - Registers#Summary of the algorithms|Lezione 13 — Summary of the algorithms]]
