---
title: Context Switch
tags:
  - sistemi-operativi
  - concetto
  - context-switch
  - scheduling
---

# Context Switch

> [!summary] In breve
> Il passaggio della CPU da un processo a un altro: si salvano i registri del processo corrente (sul suo stack, SP nel PCB), si sceglie il prossimo, si ricaricano i suoi registri e si ritorna dall'interrupt.

Avviene **solo** a seguito di un interrupt o di un'eccezione (inclusa una syscall).

1. La CPU salva PC e FLAGS sullo stack di P1 (interrupt).
2. **Preambolo**: `pushAll()`, `running->sp = SP`, `SP = kernel_sp`.
3. Codice del kernel; lo scheduler sceglie `running = P2`.
4. **Postambolo**: `SP = running->sp`, `popAll()`, `iret`.

- Un processo **mai eseguito** ha uno stack preparato a mano, con l'aspetto di un processo interrotto (IP = trampolino, registri = 0).
- **Costo**: salvataggio/ripristino dello stato, cache e TLB "fredde". Per questo il quanto deve essere molto più lungo del context switch (ms contro µs).

## Collegamenti

- **Concetti correlati**: [[Contesto di un Processo]] · [[Preemptive Multitasking su AVR]] · [[Process Control Block]] · [[Interrupt]] · [[CPU Scheduler e Dispatcher]] · [[Round Robin]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[05 - SO - Stack e Context Switch#Il context switch passo per passo|Lezione 5 — Il context switch passo per passo]]
> - [[05 - SO - Stack e Context Switch#Il context switch in assembly|Lezione 5 — Il context switch in assembly]]
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Context switch nel kernel|Lezione 6 — Context switch nel kernel]]
