---
title: Page Replacement
tags:
  - sistemi-operativi
  - concetto
  - memoria-virtuale
---

# Page Replacement

> [!summary] In breve
> Quando non ci sono frame liberi si sceglie una pagina vittima da rimuovere (riscrivendola su disco solo se è dirty). Obiettivo: minimizzare il page fault rate.

Sulla reference string `7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1` con 3 frame:

| Algoritmo | Vittima | Page fault |
| --- | --- | --- |
| FIFO | la pagina caricata per prima | 15 (soffre di Belady) |
| Ottimo | quella usata più tardi nel futuro (non implementabile) | 9 |
| LRU | quella non usata da più tempo | 12 |

- LRU esatto (contatore o stack) è troppo costoso → **reference bit**.
- **Second chance (clock)**: bit a 1 → lo si azzera e si passa oltre; bit a 0 → vittima.
- **Second chance migliorato** con (ref, dirty): (0,0) è la vittima migliore, (1,1) la peggiore.

## Collegamenti

- **Concetti correlati**: [[Anomalia di Belady]] · [[Demand Paging]] · [[Thrashing e Working Set]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[11 - SO - Memoria Virtuale#Page replacement|Lezione 11 — Page replacement]]
> - [[11 - SO - Memoria Virtuale#FIFO|Lezione 11 — FIFO]]
> - [[11 - SO - Memoria Virtuale#Optimal page replacement|Lezione 11 — Optimal page replacement]]
> - [[11 - SO - Memoria Virtuale#LRU (Least Recently Used)|Lezione 11 — LRU (Least Recently Used)]]
> - [[11 - SO - Memoria Virtuale#LRU approssimato|Lezione 11 — LRU approssimato]]
> - [[07 - SDC - Gestione dei dati in memoria centrale#Politiche di rimpiazzo|Sistemi di Calcolo, cap. 7 — Politiche di rimpiazzo]]
