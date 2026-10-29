---
title: Liveness
tags:
  - dependable-distributed-systems
  - concetto
  - properties
---

# Liveness

> [!summary] In breve
> A **liveness** property says that *something good eventually happens*; together with safety ("nothing bad happens") it is one of the two kinds of properties every distributed abstraction is specified with.

| | Safety | Liveness |
|---|---|---|
| Intuition | nothing bad happens | something good eventually happens |
| Violation | has a **finite bad prefix**, cannot be undone | never visible in a finite prefix: there is always a continuation that satisfies it |
| Typical keywords | "no", "at most", "only if" | "eventually" |
| Examples | no duplication, no creation, mutual exclusion, agreement | reliable delivery, termination, every request is eventually granted |

- A specification with only safety is trivially satisfied by doing nothing; one with only liveness by doing anything. Useful abstractions need **both**.
- Liveness usually depends on timing and failure assumptions: e.g. [[Paxos]] is always safe but live only when an eventual leader is stable.

> [!warning]
> In this vault `[[Safety]]` resolves to the dependability attribute (`Extra/Fundamental Properties/Safety.md`), which is a different notion from the safety *property* of a specification.

## Collegamenti

- **Concetti correlati**: [[Perfect Failure Detector]] · [[Consensus Abstraction]] · [[Paxos]]
- **Mappa**: [[MOC - Dependable Distributed Systems]]

> [!info] Approfondimento
> - [[2 - DDS - Modelling Distributed Systems and Abstracting Communications#Safety and liveness|Lezione 2 — Safety and liveness]]
> - [[10 - DDS - Ordered Communications#Liveness|Lezione 10 — Liveness]]
> - [[9 - DDS - Paxos#Liveness|Lezione 9 — Liveness]]
