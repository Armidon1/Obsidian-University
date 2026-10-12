---
title: First Come First Served
tags:
  - sistemi-operativi
  - concetto
  - scheduling
---

# First Come First Served

> [!summary] In breve
> Non preemptive, coda FIFO: si serve il primo arrivato. Semplice, ma soffre del convoy effect.

- P1 = 24, P2 = 3, P3 = 3 in quest'ordine: waiting medio (0 + 23 + 25) / 3 = **16**. In ordine P2, P3, P1: **3**.
- **Convoy effect**: i processi corti restano bloccati dietro uno lungo.

## Collegamenti

- **Concetti correlati**: [[Shortest Job First]] · [[Round Robin]] · [[Criteri di Scheduling]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[09 - SO - CPU Scheduling#First Come First Served (FCFS)|Lezione 9 — First Come First Served (FCFS)]]
