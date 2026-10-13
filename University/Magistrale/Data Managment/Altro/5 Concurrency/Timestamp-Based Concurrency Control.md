---
title: Timestamp-Based Concurrency Control
aliases:
  - Timestamp ordering
  - Thomas write rule
tags:
  - data-management
  - concept
  - concurrency-control
  - timestamps
---

# Timestamp-Based Concurrency Control

> [!summary] In short
> Each transaction gets a timestamp; an operation is accepted only if compatible with the timestamp order, otherwise the transaction restarts. Data items keep $rts$, $wts$ and a commit bit.

| Case | Condition | Action |
|---|---|---|
| read ok | $ts \ge wts$ | read (wait if $cb$ false) |
| read too late | $ts < wts$ | restart |
| write ok | $ts \ge rts, wts$ | write (wait if $cb$ false) |
| Thomas rule | $rts \le ts < wts$ | ignore the write |
| write too late | $ts < rts$ | restart |

- No locks, but waits on commit bits can still deadlock.
- Better than 2PL with few conflicts / read-mostly workloads.

## Links

- **Related concepts**: [[MVCC]] · [[Two-Phase Locking]] · [[Optimistic Concurrency Control]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[05 - DM - Concurrency Control#Basic idea|Lecture 5 — Basic idea]]
> - [[05 - DM - Concurrency Control#The scheduler|Lecture 5 — The scheduler]]
> - [[05 - DM - Concurrency Control#Case 2b: Thomas write rule|Lecture 5 — Case 2b: Thomas write rule]]
> - [[05 - DM - Concurrency Control#Comparison between timestamps and 2PL|Lecture 5 — Comparison between timestamps and 2PL]]
