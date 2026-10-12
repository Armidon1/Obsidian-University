---
title: CPU Scheduler e Dispatcher
tags:
  - sistemi-operativi
  - concetto
  - scheduling
---

# CPU Scheduler e Dispatcher

> [!summary] In breve
> Lo scheduler sceglie quale processo ready riceve la CPU; il dispatcher esegue il cambio (preambolo in kernel mode, postambolo in user mode).

Lo scheduler viene invocato quando un processo:

1. va da running a waiting;
2. termina;
3. va da running a ready;
4. va da waiting a ready.

- **Non preemptive**: solo nei casi 1 e 2. **Preemptive**: in tutti.
- Il dispatch costa: salvataggio e ripristino dello stato, cache non più valida.

## Collegamenti

- **Concetti correlati**: [[Criteri di Scheduling]] · [[Context Switch]] · [[Round Robin]] · [[Stati di un Processo]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[09 - SO - CPU Scheduling#CPU scheduler|Lezione 9 — CPU scheduler]]
> - [[09 - SO - CPU Scheduling#Dispatcher|Lezione 9 — Dispatcher]]
