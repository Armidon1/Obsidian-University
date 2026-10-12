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

## Dal PCB a `task_struct` in Linux

Il **PCB è il modello generale** della struttura con cui un kernel descrive e gestisce un processo. In Linux questo ruolo è svolto da **`struct task_struct` e dalle strutture collegate**, descritte in [[Processo Linux - task_struct]]. Le informazioni possono essere contenute direttamente nella struttura oppure raggiunte tramite puntatori: per esempio, `mm` rimanda alla gestione della memoria e `files` alla tabella dei file descriptor.

> [!important] Una struttura per ogni thread
> Linux mantiene una **`task_struct` per ogni task, cioè per ogni thread**, non una sola per l'intero processo multithread. Ogni thread ha il proprio stato e contesto di esecuzione; i thread dello stesso processo condividono normalmente risorse come memoria e file aperti. Il campo `pid` identifica la singola task, mentre `tgid` identifica il gruppo di thread del processo.

Il PCB studiato in Sistemi Operativi spiega **quali informazioni servono e perché**; `task_struct` mostra **come Linux le organizza concretamente**.

## Collegamenti

- **Concetti correlati**: [[Contesto di un Processo]] · [[Stati di un Processo]] · [[Context Switch]] · [[disastrOS]] · [[SLAB Allocator]] · [[File Descriptor]] · [[Processo Linux - task_struct]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#Process Control Block|Lezione 6 — Process Control Block]]
> - [[08 - SO - disastrOS#Il PCB|Lezione 8 — Il PCB]]
> - [[05 - SO - Stack e Context Switch#Task Control Block|Lezione 5 — Task Control Block]]
> - [[06 - SDC - Esecuzione dei programmi#Processi|Sistemi di Calcolo, cap. 6 — Processi]]
