---
title: Thrashing e Working Set
tags:
  - sistemi-operativi
  - concetto
  - memoria-virtuale
---

# Thrashing e Working Set

> [!summary] In breve
> Thrashing: il sistema passa più tempo a paginare che a eseguire, perché i processi non hanno abbastanza frame per il loro working set. Avviene quando D(t) = Σ|wss(p,t)| supera i frame disponibili.

- Circolo vizioso: CPU poco usata → l'OS aumenta la multiprogrammazione → ancora più page fault.
- **Località**: un processo usa un insieme di pagine che cambia lentamente.
- **Working set** `wss(p, t)`: le pagine usate da p nella finestra t.
- Rimedio: se $D(t) > max\_frames$, sospendere qualche processo.
- Il page fault rate ha picchi a ogni cambio di località.

## Collegamenti

- **Concetti correlati**: [[Page Replacement]] · [[Demand Paging]] · [[Memoria Virtuale]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[11 - SO - Memoria Virtuale#Thrashing|Lezione 11 — Thrashing]]
> - [[11 - SO - Memoria Virtuale#Località e working set|Lezione 11 — Località e working set]]
