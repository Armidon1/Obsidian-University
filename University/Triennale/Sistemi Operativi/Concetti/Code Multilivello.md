---
title: Code Multilivello
tags:
  - sistemi-operativi
  - concetto
  - scheduling
---

# Code Multilivello

> [!summary] In breve
> La coda ready è divisa in più code (es. foreground con RR, background con FCFS) con scheduling tra le code; nella variante con feedback i processi possono cambiare coda.

- Tra le code: **priorità fissa** (rischio di starvation) o **time slice** (es. 80% / 20%).
- **Multilevel feedback queue**: è definita dal numero di code, dall'algoritmo di ogni coda, dalle regole di promozione/degradazione e dalla coda iniziale.
  - Chi consuma tutto il quanto (CPU bound) viene **degradato**.
  - Chi usa meno del quanto (I/O bound, interattivo) viene **promosso**.
  - È un modo per implementare l'aging.

## Collegamenti

- **Concetti correlati**: [[Round Robin]] · [[Priority Scheduling]] · [[First Come First Served]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[09 - SO - CPU Scheduling#Code multilivello|Lezione 9 — Code multilivello]]
> - [[09 - SO - CPU Scheduling#Code multilivello con feedback|Lezione 9 — Code multilivello con feedback]]
