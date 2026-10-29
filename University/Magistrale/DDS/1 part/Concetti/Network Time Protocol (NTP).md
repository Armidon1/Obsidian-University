---
title: Network Time Protocol (NTP)
tags:
  - dependable-distributed-systems
  - concetto
  - clock-synchronization
---

# Network Time Protocol (NTP)

> [!summary] In breve
> Hierarchical, Internet-scale **external** synchronisation: servers organised in **strata** (stratum 1 = attached to a UTC source) exchange timestamped messages to estimate offset and delay.

- Hierarchy of servers (strata) → scalability and redundancy; the subnet reconfigures when a server fails.
- Reconfigurable under faults: a primary that loses UTC becomes secondary; a secondary that loses its primary connects to another one.
- Remote reading **like [[Cristian's Algorithm]]**, plus clustering, filtering and data-quality evaluation to reduce the error.
- Synchronization modes: multicast (LAN, low accuracy), procedure call, symmetric (between servers, highest accuracy).
- Accuracy decreases going down the strata.

## Collegamenti

- **Concetti correlati**: [[Cristian's Algorithm]] · [[Berkeley Algorithm]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[3 - DDS - Time in Distributed Systems#Network Time Protocol (NTP)|Lezione 3 — Network Time Protocol (NTP)]]
