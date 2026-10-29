---
title: Regular to Atomic Register Transformation
tags:
  - dependable-distributed-systems
  - concetto
  - registers
---

# Regular to Atomic Register Transformation

> [!summary] In breve
> Two-phase construction: **(1,N) regular → (1,1) atomic** (the reader keeps the highest timestamp seen), then **(1,1) atomic → (1,N) atomic** with $N^2$ (1,1) registers, where each reader writes back what it read.

- Phase 1: timestamps reject old values for a single reader.
- Phase 2: reader $i$ reads all registers $(\cdot, i)$, picks the highest timestamp and **writes it** to registers $(i, \cdot)$ before returning — so later readers cannot see older values.
- Simple but expensive: motivates [[Read-Impose Write-All]] and [[Read-Impose Write-Majority]].

## Collegamenti

- **Concetti correlati**: [[Atomic Register]] · [[Regular Register]] · [[Read-Impose Write-All]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[13 - DDS - Registers#Atomic register implementation|Lezione 13 — Atomic register implementation]]
> - [[13 - DDS - Registers#From $(1,N)$ regular to $(1,N)$ atomic register|Lezione 13 — From $(1,N)$ regular to $(1,N)$ atomic register]]
