---
title: Regular Register
tags:
  - dependable-distributed-systems
  - concetto
  - registers
---

# Regular Register

> [!summary] In breve
> $(1,N)$ register where a read returns the **last written value** if it is not concurrent with a write, or the last value **or one of the concurrently written values** otherwise.

- **ONRR1 termination**: if a correct process invokes an operation, it eventually completes.
- **ONRR2 validity**: a read not concurrent with a write returns the last value written; a read concurrent with writes returns the last value or a value being written.
- Allows **new-old inversion**: a read returns the new value, a later read the old one.
- Algorithms: [[Read-One Write-All]] (fail-stop), [[Majority Voting Regular Register]] (fail-silent).

## Collegamenti

- **Concetti correlati**: [[Atomic Register]] · [[Read-One Write-All]] · [[Majority Voting Regular Register]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[13 - DDS - Registers#Register specifications: regular and atomic|Lezione 13 — Register specifications: regular and atomic]]
> - [[13 - DDS - Registers#Regular register — a surprising scenario|Lezione 13 — Regular register — a surprising scenario]]
