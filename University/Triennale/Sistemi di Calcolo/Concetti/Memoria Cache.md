---
title: Memoria Cache
tags:
  - sistemi-di-calcolo
  - concetto
  - memoria
  - cache
  - hardware
---

# Memoria Cache

> [!summary] In breve
> Memoria SRAM piccola e veloce tra CPU e DRAM, organizzata in linee (es. 64 byte) che contengono copie di blocchi di memoria: hit = dato in cache, miss = va caricato il blocco (rimpiazzando una linea vittima, di solito LRU).

- Blocco di un indirizzo x = **x / L** (L = dimensione della linea).
- In caso di miss si trasferisce **l'intera linea**; se la vittima era stata modificata va riscritta in memoria.
- Rimpiazzo: ottimo = la linea usata più tardi nel futuro (non implementabile) → **LRU**.
- Miss **cold** (prima volta), **capacity** (cache piena), **conflict** (vincoli di associatività).

## Collegamenti

- **Concetti correlati**: [[Località dei Riferimenti]] · [[Associatività delle Cache]] · [[Gerarchia di Memoria]] · [[TLB]] · [[Page Replacement]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[07 - SDC - Gestione dei dati in memoria centrale#Memorie cache|Lezione 7 — Memorie cache]]
> - [[07 - SDC - Gestione dei dati in memoria centrale#Politiche di rimpiazzo|Lezione 7 — Politiche di rimpiazzo]]
> - [[07 - SDC - Gestione dei dati in memoria centrale#Tipi di cache miss|Lezione 7 — Tipi di cache miss]]
