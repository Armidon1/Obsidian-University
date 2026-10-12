---
title: Preemptive Multitasking su AVR
tags:
  - sistemi-operativi
  - concetto
  - avr
  - context-switch
  - scheduling
---

# Preemptive Multitasking su AVR

> [!summary] In breve
> Un timer genera interrupt periodici; la ISR chiama `schedule()`, che rimette il TCB corrente in coda, prende il prossimo e fa `archContextSwitch` in assembly.

- **TCB**: `sp_save_ptr` (primo campo), `thread_fn`, `thread_arg`, `prev`/`next`, `status`.
- `TCB_create` costruisce lo stack del nuovo thread: indirizzo di `_trampoline` (3 byte) più i registri a 0.
- `_trampoline`: `sei()`, chiama `thread_fn(thread_arg)`, poi imposta lo stato `Terminated`.
- `archContextSwitch(old, new)`: push dei registri, SP → `old->sp_save_ptr`, SP ← `new->sp_save_ptr`, pop dei registri, `ret`.
- `archFirstThreadRestore(tcb)`: la seconda metà del context switch, usata per avviare il primo thread.
- `startSchedule`: estrae il primo TCB, `timerStart()` (timer 1 in CTC), primo restore.
- `ISR(TIMER1_COMPA_vect) { schedule(); }`. Coda FIFO, quindi **round robin**.
- Le `printf` vanno protette con `cli()`/`sei()`: la seriale è una risorsa condivisa (**sezione critica**).

## Collegamenti

- **Concetti correlati**: [[Context Switch]] · [[Timer AVR]] · [[Round Robin]] · [[Contesto di un Processo]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[05 - SO - Stack e Context Switch#Preemptive multitasking su AVR|Lezione 5 — Preemptive multitasking su AVR]]
> - [[05 - SO - Stack e Context Switch#Lo scheduler|Lezione 5 — Lo scheduler]]
