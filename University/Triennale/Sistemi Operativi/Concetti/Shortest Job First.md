---
title: Shortest Job First
tags:
  - sistemi-operativi
  - concetto
  - scheduling
---

# Shortest Job First

> [!summary] In breve
> Si sceglie il processo con il prossimo CPU burst più corto: è ottimo per il waiting time medio, ma richiede di prevedere i burst.

- Esempio: 6, 8, 7, 3 → ordine P4, P1, P3, P2, waiting medio **7**.
- Versione preemptive: **Shortest Remaining Time First**.
- È un priority scheduling con priorità = 1/burst, quindi rischia la **starvation**.
- La previsione si fa con una media esponenziale.

## Collegamenti

- **Concetti correlati**: [[CPU Burst e IO Burst]] · [[Priority Scheduling]] · [[First Come First Served]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[09 - SO - CPU Scheduling#Shortest Job First (SJF)|Lezione 9 — Shortest Job First (SJF)]]
> - [[09 - SO - CPU Scheduling#Predire il prossimo burst|Lezione 9 — Predire il prossimo burst]]
