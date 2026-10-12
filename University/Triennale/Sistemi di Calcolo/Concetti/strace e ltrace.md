---
title: strace e ltrace
tags:
  - sistemi-di-calcolo
  - concetto
  - strumenti
  - debugging
---

# strace e ltrace

> [!summary] In breve
> `strace` mostra le system call di un programma (confine user/kernel); `ltrace` mostra le chiamate alle librerie dinamiche.

```
$ strace ./hello > /dev/null      # l'output di strace va su stderr
write(1, "hello world\n", 12) = 12
exit_group(0)                     = ?
$ ltrace ./mytest > /dev/null
sqrt(...)          = ...
printf("%f\n", 1.414214) = 9
```

- Mostrano che `printf` → `write` sul descrittore 1, e `return 0` → `exit_group(0)`.
- Prima del `main` ci sono molte system call di preparazione (caricamento delle librerie, `mmap`, `mprotect`, `brk`…).

## Collegamenti

- **Concetti correlati**: [[System Call]] · [[Funzioni della libc]] · [[Architettura a Strati]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[04 - SDC - Librerie standard del C#Tracciare le system call: strace|Lezione 4 — Tracciare le system call: strace]]
> - [[04 - SDC - Librerie standard del C#Tracciare le chiamate di libreria: ltrace|Lezione 4 — Tracciare le chiamate di libreria: ltrace]]
