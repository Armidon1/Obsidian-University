---
title: Gerarchia di Memoria
tags:
  - sistemi-di-calcolo
  - concetto
  - memoria
  - cache
  - prestazioni
---

# Gerarchia di Memoria

> [!summary] In breve
> Registri → L1 → L2 → L3 → RAM → disco: scendendo, il costo per byte diminuisce e la capacità aumenta, ma la velocità crolla, fino a 6 ordini di grandezza.

| Livello | Tempo | Capacità |
| --- | --- | --- |
| Registri | < 1 ns | centinaia di byte |
| L1 | ~1 ns | ~64 KB |
| L2 | ~4 ns | ~256 KB |
| L3 | ~16 ns | ~6 MB |
| RAM (DRAM) | ~100 ns | ~16 GB |
| SSD / disco magnetico | ~16 µs / ~3 ms | TB |

- Ogni livello fa da cache a quello sotto. Nei multi-core L1 e L2 sono per core, L3 è condivisa.
- "Se un ciclo di clock durasse 1 s": RAM 4 minuti, disco meccanico mesi.
- Per questo la **località** del programma conta più del numero di istruzioni.

## Collegamenti

- **Concetti correlati**: [[Memoria Cache]] · [[Località dei Riferimenti]] · [[Memoria Virtuale]] · [[Macchina di Von Neumann]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[01 - SDC - Cosa è un sistema di calcolo#Sistema di memoria|Lezione 1 — Sistema di memoria]]
> - [[07 - SDC - Gestione dei dati in memoria centrale#Gerarchie di memoria|Lezione 7 — Gerarchie di memoria]]
> - [[05 - SDC - Ottimizzazione dei programmi#Scala degli eventi|Lezione 5 — Scala degli eventi]]
