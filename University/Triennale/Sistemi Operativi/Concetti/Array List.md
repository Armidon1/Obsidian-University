---
title: Array List
tags:
  - sistemi-operativi
  - concetto
  - strutture-dati
  - allocatori
---

# Array List

> [!summary] In breve
> Linked list su memoria fissa: un array di interi in cui la cella i contiene l'indice dell'elemento successivo (−1 = fine), più l'indice della testa.

Esempio: la lista 1 → 7 → 2 → 3 → 0 diventa `start = 1`, `a[1]=7`, `a[7]=2`, `a[2]=3`, `a[3]=0`, `a[0]=-1`; le altre celle valgono −1.

- Non richiede allocazione dinamica: serve proprio per implementare un allocatore.

## Collegamenti

- **Concetti correlati**: [[SLAB Allocator]] · [[Lista Generica in C]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[07 - SO - Allocatori di Memoria#La free list senza malloc: array list|Lezione 7 — La free list senza malloc: array list]]
