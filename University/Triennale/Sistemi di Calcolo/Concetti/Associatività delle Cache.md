---
title: Associatività delle Cache
tags:
  - sistemi-di-calcolo
  - concetto
  - memoria
  - cache
---

# Associatività delle Cache

> [!summary] In breve
> Quante linee può occupare un blocco: mapping diretto (una sola linea), associativa a k vie (k linee), completamente associativa (qualsiasi linea).

| Tipo | Linee possibili per blocco | Note |
| --- | --- | --- |
| Mapping diretto | 1 (`blocco mod N`) | semplice, molti miss di conflitto |
| A k vie | k (tipicamente 2–64) | il compromesso usato in pratica |
| Fully associative | tutte | nessun conflitto, hardware costoso |

## Collegamenti

- **Concetti correlati**: [[Memoria Cache]] · [[Località dei Riferimenti]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[07 - SDC - Gestione dei dati in memoria centrale#Associatività|Lezione 7 — Associatività]]
