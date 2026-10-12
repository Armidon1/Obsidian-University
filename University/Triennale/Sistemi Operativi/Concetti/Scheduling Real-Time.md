---
title: Scheduling Real-Time
tags:
  - sistemi-operativi
  - concetto
  - scheduling
  - real-time
---

# Scheduling Real-Time

> [!summary] In breve
> Soft real-time: priorità ai task critici senza garanzie. Hard real-time: ogni task deve finire entro la propria deadline. Contano la interrupt latency e la dispatch latency.

- **Interrupt latency**: dall'arrivo dell'interrupt all'inizio della ISR.
- **Dispatch latency**: tempo per fermare un processo e avviarne un altro (conflitti + dispatch).
- Task periodici: tempo di elaborazione t, deadline d, periodo p, con $0 \le t \le d \le p$; frequenza 1/p.

## Collegamenti

- **Concetti correlati**: [[Priority Scheduling]] · [[Interrupt]] · [[CPU Scheduler e Dispatcher]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[09 - SO - CPU Scheduling#Scheduling real-time|Lezione 9 — Scheduling real-time]]
> - [[09 - SO - CPU Scheduling#Priority scheduling real-time|Lezione 9 — Priority scheduling real-time]]
