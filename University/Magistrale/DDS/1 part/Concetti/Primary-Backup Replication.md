---
title: Primary-Backup Replication
tags:
  - dependable-distributed-systems
  - concetto
  - replication
---

# Primary-Backup Replication

> [!summary] In breve
> **Passive replication**: only the **primary** executes requests and pushes the resulting state updates to the backups, then answers the client. When the primary crashes, a backup is elected.

- Order decided by the primary → non-deterministic operations are fine.
- Crashes: needs a [[Perfect Failure Detector]] and [[Leader Election]]; the update must reach the backups before the reply (the client may re-send after a timeout).
- Failure scenarios: crash after the answer, before the updates, during the update.

## Collegamenti

- **Concetti correlati**: [[Active Replication]] · [[Linearizability]] · [[Leader Election]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[12 - DDS - Software Replication#Passive replication: primary-backup|Lezione 12 — Passive replication: primary-backup]]
> - [[12 - DDS - Software Replication#Presence of crashes|Lezione 12 — Presence of crashes]]
