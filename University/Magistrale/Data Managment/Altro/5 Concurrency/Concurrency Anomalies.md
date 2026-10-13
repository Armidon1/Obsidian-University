---
title: Concurrency Anomalies
aliases:
  - Lost update
  - Dirty read
  - Phantom read
tags:
  - data-management
  - concept
  - transactions
  - isolation
---

# Concurrency Anomalies

> [!summary] In short
> Typical incorrect patterns of interleaved transactions: reading temporary data / dirty read, lost update, unrepeatable read, ghost update, phantom read.

| Anomaly | Pattern |
|---|---|
| Dirty read (temporary data) | $w_1(A)\,r_2(A)\,a_1$ |
| Lost update | $r_1(A)\,r_2(A)\,w_2(A)\,w_1(A)$ |
| Unrepeatable read | $r_1(A)\,w_2(A)\,c_2\,r_1(A)$ |
| Ghost update | $w_1(A)\,w_2(B)\,w_1(B)\,w_2(A)$ with constraint $A=B$ |
| Phantom | range query repeated after insert/delete by another transaction |

## Links

- **Related concepts**: [[SQL Isolation Levels]] · [[Schedule (Concurrency)]] · [[Recoverable Schedule]]
- **Map**: [[00 - Data Management MOC]]

> [!info] In depth
> - [[05 - DM - Concurrency Control#Anomalies|Lecture 5 — Anomalies]]
> - [[05 - DM - Concurrency Control#Dirty read (WR anomaly)|Lecture 5 — Dirty read (WR anomaly)]]
> - [[05 - DM - Concurrency Control#Anomalies considered by SQL|Lecture 5 — Anomalies considered by SQL]]
