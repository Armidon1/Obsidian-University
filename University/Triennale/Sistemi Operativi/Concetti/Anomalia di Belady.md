---
title: Anomalia di Belady
tags:
  - sistemi-operativi
  - concetto
  - memoria-virtuale
---

# Anomalia di Belady

> [!summary] In breve
> Con FIFO, aumentare il numero di frame può aumentare i page fault.

Con la reference string `1 2 3 4 1 2 5 1 2 3 4 5`: 3 frame → **9** page fault, 4 frame → **10**.

LRU e l'algoritmo ottimo ne sono immuni: sono **algoritmi a stack**, in cui le pagine in memoria con n frame sono sempre un sottoinsieme di quelle con n+1.

## Collegamenti

- **Concetti correlati**: [[Page Replacement]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[11 - SO - Memoria Virtuale#Anomalia di Belady|Lezione 11 — Anomalia di Belady]]
