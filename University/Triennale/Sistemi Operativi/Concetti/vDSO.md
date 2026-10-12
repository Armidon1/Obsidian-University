---
title: vDSO
tags:
  - sistemi-operativi
  - concetto
  - syscall
  - kernel
---

# vDSO

> [!summary] In breve
> Virtual Dynamic Shared Object: libreria che il kernel mappa in ogni processo, con funzioni del kernel innocue (es. `gettimeofday`) eseguibili in user mode senza il costo di una syscall.

- Entrare e uscire dal kernel costa (preambolo, postambolo, cambio di modalità, cache).
- Per funzioni frequenti e non pericolose il kernel espone i dati in pagine di sola lettura e il codice nella vDSO.
- Non corrisponde a nessun file su disco: con `ldd` appare come `linux-vdso.so.1`.

## Collegamenti

- **Concetti correlati**: [[System Call]] · [[Dual Mode]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[06 - SO - Interrupt, Syscall, Dual Mode e Processi#vDSO|Lezione 6 — vDSO]]
