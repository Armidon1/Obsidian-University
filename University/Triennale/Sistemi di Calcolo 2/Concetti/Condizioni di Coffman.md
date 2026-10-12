---
title: Condizioni di Coffman
tags:
  - sistemi-di-calcolo-2
  - concetto
  - deadlock
---

# Condizioni di Coffman

> [!summary] In breve
> Mutual exclusion, hold and wait, no preemption (necessarie ma non sufficienti) + circular wait: tutte e quattro insieme provocano il deadlock.

| Condizione | Come prevenirla |
| --- | --- |
| Mutual exclusion | di solito impossibile (al più si rilassa) |
| Hold and wait | chiedere tutte le risorse insieme (inefficiente) |
| No preemption | rilasciare le risorse se una richiesta viene negata (solo per risorse con stato salvabile) |
| Circular wait | **ordinamento lineare** dei tipi di risorsa |

## Collegamenti

- **Concetti correlati**: [[Deadlock]] · [[Gestione del Deadlock]]
- **Mappa**: [[MOC - Sistemi di Calcolo 2]]

> [!info] Approfondimento
> - [[03 - SDC2 - Deadlock#Le quattro condizioni|Lezione 3 — Le quattro condizioni]]
> - [[03 - SDC2 - Deadlock#Prevention|Lezione 3 — Prevention]]
