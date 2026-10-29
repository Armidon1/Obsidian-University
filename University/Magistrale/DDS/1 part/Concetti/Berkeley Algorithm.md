---
title: Berkeley Algorithm
tags:
  - dependable-distributed-systems
  - concetto
  - clock-synchronization
---

# Berkeley Algorithm

> [!summary] In breve
> **Internal** clock synchronisation: a master polls the slaves, estimates their clocks (à la Cristian), computes a **fault-tolerant average** and sends each one the *adjustment*, not the time.

- No UTC source: the goal is that the clocks agree with each other.
- The master ignores clocks that are too far from the others (fault-tolerant average), so a faulty clock does not drag the group.
- It sends **offsets** ($+\delta$, $-\delta$) because sending an absolute time would suffer the message delay.
- A clock is never moved backwards: it is **slowed down** until it catches up, to keep monotonicity.
- If the master crashes, a new one is elected ([[Leader Election]]).

## Collegamenti

- **Concetti correlati**: [[Cristian's Algorithm]] · [[Network Time Protocol (NTP)]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[3 - DDS - Time in Distributed Systems#Berkeley's algorithm|Lezione 3 — Berkeley's algorithm]]
