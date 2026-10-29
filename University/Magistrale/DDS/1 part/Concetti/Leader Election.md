---
title: Leader Election
tags:
  - dependable-distributed-systems
  - concetto
  - leader-election
---

# Leader Election

> [!summary] In breve
> LE: elect a **unique leader** that is correct — *eventual detection* (a correct leader is eventually elected) and *accuracy* (a leader is replaced only after it crashes). Built on a perfect failure detector.

- **Monarchical Leader Election**: processes are ranked; the leader is the highest-ranked process not detected as crashed by [[Perfect Failure Detector|P]].
- With an imperfect detector two processes may believe to be leaders at the same time → [[Eventual Leader Election (Omega)]].
- Used by [[Primary-Backup Replication]] to replace a crashed primary.

## Collegamenti

- **Concetti correlati**: [[Perfect Failure Detector]] · [[Eventual Leader Election (Omega)]] · [[Primary-Backup Replication]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[6 - DDS - Failure Detection and Leader Election#Leader election (LE)|Lezione 6 — Leader election (LE)]]
> - [[6 - DDS - Failure Detection and Leader Election#What if the failure detector is not perfect?|Lezione 6 — What if the failure detector is not perfect?]]
