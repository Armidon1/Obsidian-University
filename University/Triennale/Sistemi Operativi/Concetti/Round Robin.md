---
title: Round Robin
tags:
  - sistemi-operativi
  - concetto
  - scheduling
---

# Round Robin

> [!summary] In breve
> FCFS con preemption a quanto fisso q: allo scadere del quanto il processo torna in fondo alla coda ready. Nessuno aspetta più di (N−1)·q.

- Esempio con q = 4 su 24, 3, 3: waiting medio ≈ 5.66; turnaround peggiore di SJF ma risposta migliore.
- **q troppo piccolo**: troppi context switch. **q troppo grande**: degenera in FCFS. Tipicamente q = 10–100 ms, context switch < 10 µs.
- Implementato nel multitasking AVR (lista FIFO di TCB) e in `internal_schedule` di disastrOS.

## Collegamenti

- **Concetti correlati**: [[First Come First Served]] · [[Context Switch]] · [[Preemptive Multitasking su AVR]] · [[disastrOS]] · [[Code Multilivello]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[09 - SO - CPU Scheduling#Round Robin (RR)|Lezione 9 — Round Robin (RR)]]
> - [[09 - SO - CPU Scheduling#Scelta del quanto|Lezione 9 — Scelta del quanto]]
> - [[05 - SO - Stack e Context Switch#Lo scheduler|Lezione 5 — Lo scheduler]]
> - [[08 - SO - disastrOS#preempt e scheduler|Lezione 8 — preempt e scheduler]]
> - [[06 - SDC - Esecuzione dei programmi#Stati, scheduling, preemption, time-sharing|Sistemi di Calcolo, cap. 6 — Stati, scheduling, preemption, time-sharing]]
