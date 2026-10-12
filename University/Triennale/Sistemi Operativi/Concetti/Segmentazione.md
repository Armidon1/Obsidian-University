---
title: Segmentazione
tags:
  - sistemi-operativi
  - concetto
  - memoria
---

# Segmentazione

> [!summary] In breve
> Lo spazio logico è diviso in segmenti di dimensione variabile (codice, dati, stack…); l'indirizzo è (segmento, offset) e la segment table fornisce base, limit, permessi e bit di validità.

- `fisico = base[s] + d` se `d < limit[s]`, altrimenti trap.
- **STBR** punta alla segment table, **STLR** indica il numero di segmenti.
- Permessi per segmento (r/w/x): rispecchia la struttura logica del programma.
- 8086: `segment * 16 + offset`. IA-32: segmentazione (indirizzo logico → lineare) + paging (lineare → fisico).
- Difetto: **frammentazione esterna**.

## Collegamenti

- **Concetti correlati**: [[Paging]] · [[MMU]] · [[Frammentazione]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[10 - SO - Gestione della Memoria#Segmentazione|Lezione 10 — Segmentazione]]
> - [[10 - SO - Gestione della Memoria#IA-32|Lezione 10 — IA-32]]
