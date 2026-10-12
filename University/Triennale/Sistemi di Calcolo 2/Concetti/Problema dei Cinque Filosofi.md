---
title: Problema dei Cinque Filosofi
tags:
  - sistemi-di-calcolo-2
  - concetto
  - deadlock
  - problemi-classici
---

# Problema dei Cinque Filosofi

> [!summary] In breve
> Cinque filosofi e cinque forchette: prendere prima la sinistra e poi la destra porta a deadlock; limitando a 4 i filosofi seduti (semaforo `room = 4`) uno riesce sempre a mangiare.

```c
wait(room);                 // room = 4
wait(fork[i]); wait(fork[(i+1) % 5]);
eat();
signal(fork[(i+1) % 5]); signal(fork[i]);
signal(room);
```

- Alternative: un filosofo mancino (ordinamento delle risorse), un monitor che dà due forchette insieme.

## Collegamenti

- **Concetti correlati**: [[Deadlock]] · [[Semafori]] · [[Condizioni di Coffman]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[03 - SDC2 - Deadlock#Il problema dei cinque filosofi|Lezione 3 — Il problema dei cinque filosofi]]
