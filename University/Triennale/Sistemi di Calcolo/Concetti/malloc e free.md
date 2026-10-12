---
title: malloc e free
tags:
  - sistemi-di-calcolo
  - concetto
  - memoria
  - allocatori
  - linguaggio-c
---

# malloc e free

> [!summary] In breve
> Allocatore in spazio utente che gestisce l'heap (ingrandito con `sbrk`): blocchi con un header (size, più `next` se liberi), lista dei blocchi liberi, scelta first-fit o best-fit.

- `malloc(n)`: cerca un blocco libero ≥ n nella `free_list`; se non c'è, `sbrk(n+4)`. Restituisce l'indirizzo del payload.
- `free(p)`: rimette in testa alla `free_list` il blocco che inizia a `p-4`.
- Payload minimo 8 byte (spazio per `next`); indirizzi allineati a 8 o 16.
- Miglioramenti: fusione e partizione dei blocchi liberi, più liste per dimensione.
- Non si può **compattare** (l'applicazione ha in mano i puntatori) → frammentazione esterna.
- Dimenticare `free` = **memory leak** (si trova con Valgrind).
- Allocatori in cascata: OS (memoria fisica) → malloc (heap) → allocatori custom.

## Collegamenti

- **Concetti correlati**: [[Frammentazione]] · [[SLAB Allocator]] · [[Buddy Allocator]] · [[Valgrind]] · [[Immagine di Memoria di un Processo]]
- **Mappa**: [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[07 - SDC - Gestione dei dati in memoria centrale#malloc e free|Lezione 7 — malloc e free]]
> - [[07 - SDC - Gestione dei dati in memoria centrale#Allocazione dinamica|Lezione 7 — Allocazione dinamica]]
