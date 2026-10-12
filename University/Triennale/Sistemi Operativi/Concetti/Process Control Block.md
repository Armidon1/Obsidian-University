---
title: Process Control Block
tags:
  - sistemi-operativi
  - concetto
  - processi
  - kernel
---

# Process Control Block

> [!summary] In breve
> Struttura del kernel che descrive un processo: PID, UID, stato, registri salvati (o almeno lo SP), informazioni di scheduling, di memoria (page table) e di I/O (descrittori). I PCB stanno in code (ready, waiting…).

- Vive nella **memoria del kernel**, accessibile solo in modalità privilegiata.
- Il contenuto dipende dall'implementazione (sull'AVR il TCB conteneva solo lo SP).
- È organizzato in **liste/code** (ready, waiting, zombie) e in un **albero** padre/figli.
- In disastrOS: `ListItem list` (primo campo), `pid`, `status`, `return_value`, `signals`, `parent`, `children`, `cpu_state` (`ucontext_t`), `stack`, `syscall_num`/`syscall_args`/`syscall_retvalue` (registri finti), `timer`. Allocato con uno **SLAB**.
- Il file descriptor è un indice nella tabella dei file aperti raggiungibile dal PCB.

## Collegamenti

- **Concetti correlati**: [[Contesto di un Processo]] · [[Stati di un Processo]] · [[Context Switch]] · [[disastrOS]] · [[SLAB Allocator]] · [[File Descriptor]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Process Control Block|Lezione 6 — Process Control Block]]
> - [[08 - SO - disastrOS#Il PCB|Lezione 8 — Il PCB]]
> - [[05 - SO - Stack e Context Switch#Task Control Block|Lezione 5 — Task Control Block]]
