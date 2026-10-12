---
title: Compare and Swap
tags:
  - sistemi-di-calcolo-2
  - concetto
  - concorrenza
  - hardware
---

# Compare and Swap

> [!summary] In breve
> Istruzione atomica: se `*reg == oldval` scrive `newval`, e restituisce sempre il vecchio valore. Con una variabile `bolt` realizza la mutua esclusione (in busy waiting).

```c
while (compare_and_swap(&bolt, 0, 1) == 1) ;   // spin finché bolt è 1
/* sezione critica */
bolt = 0;
```

- **Exchange** scambia atomicamente registro e memoria: `do exchange(&keyi, &bolt) while (keyi != 0);`.
- Pro: qualsiasi numero di processi, anche su multiprocessore; semplice; una variabile per ogni sezione critica.
- Contro: **busy waiting**, starvation e deadlock (priority inversion) possibili, dipende dall'architettura.
- Disabilitare gli interrupt funziona solo su un uniprocessore.

## Collegamenti

- **Concetti correlati**: [[Sezione Critica e Mutua Esclusione]] · [[Semafori]] · [[Polling vs Interrupt]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[02 - SDC2 - Concorrenza#Compare&Swap|Lezione 2 — Compare&Swap]]
> - [[02 - SDC2 - Concorrenza#Exchange|Lezione 2 — Exchange]]
> - [[02 - SDC2 - Concorrenza#Vantaggi e svantaggi delle istruzioni hardware|Lezione 2 — Vantaggi e svantaggi delle istruzioni hardware]]
