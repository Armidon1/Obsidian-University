---
title: Lamport's Mutual Exclusion Algorithm
tags:
  - dependable-distributed-systems
  - concetto
  - mutual-exclusion
  - logical-time
---

# Lamport's Mutual Exclusion Algorithm

> [!summary] In breve
> Every process keeps a queue of requests ordered by $(timestamp, id)$; a process enters the CS when its request is at the **head of its queue** and it has received a later message from everyone. Cost: $3(N-1)$ messages.

- Request: timestamped REQUEST to all, insert in own queue.
- On REQUEST: insert in queue, reply with a timestamped ACK.
- Enter when (1) own request is first in the queue and (2) a message with larger timestamp has arrived from every other process.
- Exit: RELEASE to all, everybody removes the request.
- Safety relies on FIFO links and the **total order** on $(t, id)$ given by the [[Scalar Logical Clock]].

## Collegamenti

- **Concetti correlati**: [[Scalar Logical Clock]] · [[Ricart-Agrawala Algorithm]] · [[Mutual Exclusion Abstraction]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[4 - DDS - Logical Clocks#Lamport's distributed mutual exclusion|Lezione 4 — Lamport's distributed mutual exclusion]]
> - [[4 - DDS - Logical Clocks#Safety proof|Lezione 4 — Safety proof]]
