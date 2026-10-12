---
title: SLAB Allocator
tags:
  - sistemi-operativi
  - concetto
  - memoria
  - allocatori
---

# SLAB Allocator

> [!summary] In breve
> Pool allocator per oggetti di dimensione fissa: il buffer è diviso in blocchi uguali e una free list (array list di indici) dà allocazione e rilascio in O(1), senza frammentazione esterna.

- `ptr = buffer + i * item_size`; `i = (ptr - buffer) / item_size`.
- Free list come **array list**: `free_list[i]` = indice del prossimo libero; `first_idx` = testa.
- **getBlock**: stacca la testa (`first_idx = free_list[first_idx]`) e marca il blocco come `Detached`.
- **releaseBlock**: controlli (`UnalignedFree`, `OutOfRange`, `DoubleFree`), poi lo reinserisce in testa.
- Memoria necessaria: `N * (item_size + sizeof(int))`.
- Usato dal kernel per PCB, nodi di lista, `BuddyListItem`: nessuna `malloc` nel kernel.

## Collegamenti

- **Concetti correlati**: [[Array List]] · [[Buddy Allocator]] · [[Frammentazione]] · [[Process Control Block]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[07 - SO - Allocatori di Memoria#SLAB allocator|Lezione 7 — SLAB allocator]]
> - [[07 - SO - Allocatori di Memoria#Implementazione del PoolAllocator|Lezione 7 — Implementazione del PoolAllocator]]
> - [[07 - SDC - Gestione dei dati in memoria centrale#Allocazione dinamica|Sistemi di Calcolo, cap. 7 — Allocazione dinamica]]
