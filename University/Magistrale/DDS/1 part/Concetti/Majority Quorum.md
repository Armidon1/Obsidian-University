---
title: Majority Quorum
tags:
  - dependable-distributed-systems
  - concetto
  - quorum
---

# Majority Quorum

> [!summary] In breve
> A **quorum** is a set of processes such that any two quorums intersect; **majorities** ($> N/2$ processes) are the simplest quorums. Waiting for a majority instead of for everybody tolerates $f < N/2$ crashes without a perfect failure detector.

- $|Q_1| + |Q_2| > N \Rightarrow Q_1 \cap Q_2 \neq \emptyset$: some process carries information from one operation to the next.
- Termination needs a majority of **correct** processes, so that a quorum always answers.

| Where | What the intersection guarantees |
|---|---|
| [[Maekawa's Voting Algorithm]] | two processes cannot both get all votes |
| Majority-Ack [[Uniform Reliable Broadcast (URB)]] | a delivered message survives at some correct process |
| [[Paxos]] | a chosen value is seen by every later proposer |
| [[Majority Voting Regular Register]], [[Read-Impose Write-Majority]] | a read sees the last write (and the last imposed read) |

## Collegamenti

- **Concetti correlati**: [[Paxos]] · [[Maekawa's Voting Algorithm]] · [[Majority Voting Regular Register]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[5 - DDS - Distributed Mutual Exclusion#How big must the voting sets be?|Lezione 5 — How big must the voting sets be?]]
> - [[9 - DDS - Paxos#A possible solution: majorities|Lezione 9 — A possible solution: majorities]]
> - [[13 - DDS - Registers#Idea|Lezione 13 — Idea]]
