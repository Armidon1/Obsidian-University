---
title: disastrOS
tags:
  - sistemi-operativi
  - concetto
  - disastros
  - kernel
---

# disastrOS

> [!summary] In breve
> OS didattico in user space: PCB in liste, syscall vector, `disastrOS_syscall` → trap → `internal_*`; scheduler preemptive con `SIGALRM` e contesti `ucontext`; `sleep` con una lista di timer.

- **Globali**: `init_pcb`, `running`, `ready_list`, `waiting_list`, `zombie_list`, `timer_list`, `syscall_vector[]`, `syscall_numarg[]`.
- **Syscall**: gli argomenti finiscono in `running->syscall_args`, poi `swapcontext` verso `trap_context`; `disastrOS_trap` chiama `syscall_vector[num]()` e fa `setcontext(&running->cpu_state)`.
- **Timer**: `setitimer` + `SIGALRM` → `timerHandler` salva il contesto e salta a `interrupt_context` → `timerInterrupt` incrementa `disastrOS_time`, chiama `internal_schedule` (round robin + risveglio dei timer scaduti) e fa `setcontext(running)`.
- Il trap context **maschera** `SIGALRM` (niente scheduling durante una syscall).
- Syscall: `fork`/`spawn`, `wait`, `exit`, `preempt`, `sleep`.

## Collegamenti

- **Concetti correlati**: [[System Call]] · [[Process Control Block]] · [[ucontext]] · [[Segnali]] · [[Round Robin]] · [[SLAB Allocator]] · [[wait e Processi Zombie]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[08 - SO - disastrOS|Lezione 8]]
