---
title: Token Ring Mutual Exclusion
tags:
  - dependable-distributed-systems
  - concetto
  - mutual-exclusion
---

# Token Ring Mutual Exclusion

> [!summary] In breve
> Processes are arranged in a **logical ring** and a unique **token** circulates; only the holder may enter the CS.

- Steps: build the ring, create the token, request/use/pass the token.
- Safety: there is one token. Liveness: the token keeps circulating.
- Costs messages even when nobody wants the CS; a lost token or a crashed process requires regeneration/ring repair.

## Collegamenti

- **Concetti correlati**: [[Mutual Exclusion Abstraction]] · [[Coordinator-based Mutual Exclusion]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[5 - DDS - Distributed Mutual Exclusion#Token-based algorithm on a logical ring|Lezione 5 — Token-based algorithm on a logical ring]]
