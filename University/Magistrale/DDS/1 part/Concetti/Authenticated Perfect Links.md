---
title: Authenticated Perfect Links
tags:
  - dependable-distributed-systems
  - concetto
  - byzantine-faults
  - links
---

# Authenticated Perfect Links

> [!summary] In breve
> Perfect links for the Byzantine model: **reliable delivery** and **no duplication** stay the same, while **no creation** becomes **authenticity**: if the claimed sender is correct, it really sent the message.

- **AL3 Authenticity**: if a correct $q$ delivers $m$ with sender $p$ and $p$ is correct, then $m$ was previously sent to $q$ by $p$.
- A Byzantine sender can still send anything in its own name: the link only stops it from impersonating correct processes.
- Implementation: **Authenticate and Filter**, a MAC over message, sender and recipient, on top of stubborn links.

## Collegamenti

- **Concetti correlati**: [[Byzantine Consistent Broadcast]] · [[Authenticated Echo Broadcast]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[14 - DDS - Byzantine Broadcast#Authenticated Perfect Link|Lezione 14 — Authenticated Perfect Link]]
> - [[14 - DDS - Byzantine Broadcast#Basic step to fight Byzantine processes|Lezione 14 — Basic step to fight Byzantine processes]]
