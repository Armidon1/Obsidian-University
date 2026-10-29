---
title: Cristian's Algorithm
tags:
  - dependable-distributed-systems
  - concetto
  - clock-synchronization
---

# Cristian's Algorithm

> [!summary] In breve
> External clock synchronisation: a process asks a **time server** for the time and corrects the answer by **half the round-trip time**.

- $p$ sends a request at $T_0$, the server replies with its time $t$, $p$ receives at $T_1$.
- Estimate: $C_p := t + \dfrac{T_1 - T_0}{2}$ (assumes symmetric delays).
- **Accuracy**: $\pm\left(\dfrac{T_1 - T_0}{2} - min\right)$, where $min$ is the minimum one-way delay.
- Single point of failure (the server); works well only when the RTT is small compared to the required accuracy.

## Collegamenti

- **Concetti correlati**: [[Berkeley Algorithm]] · [[Network Time Protocol (NTP)]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[3 - DDS - Time in Distributed Systems#Cristian's algorithm|Lezione 3 — Cristian's algorithm]]
> - [[3 - DDS - Time in Distributed Systems#Synchronization algorithms|Lezione 3 — Synchronization algorithms]]
