---
title: Happened-Before Relation
tags:
  - dependable-distributed-systems
  - concetto
  - logical-time
  - causality
---

# Happened-Before Relation

> [!summary] In breve
> Lamport's relation $\to$ on events: $e \to e'$ if they are on the same process in that order, or $e$ is a send and $e'$ the matching receive, or by transitivity. Events not related either way are **concurrent** ($e \parallel e'$).

1. $e, e'$ on the same process and $e$ before $e'$ ⇒ $e \to e'$
2. $e = send(m)$, $e' = receive(m)$ ⇒ $e \to e'$
3. $e \to e'$ and $e' \to e''$ ⇒ $e \to e''$

- It is a **strict partial order**: it captures *potential causality*, not real time.
- Basis of [[Scalar Logical Clock]], [[Vector Clock]] and of [[Causal Order Broadcast]].

## Collegamenti

- **Concetti correlati**: [[Scalar Logical Clock]] · [[Vector Clock]] · [[Causal Order Broadcast]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[4 - DDS - Logical Clocks#The happened-before relation|Lezione 4 — The happened-before relation]]
