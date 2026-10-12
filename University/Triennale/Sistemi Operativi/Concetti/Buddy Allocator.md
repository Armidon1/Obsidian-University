---
title: Buddy Allocator
tags:
  - sistemi-operativi
  - concetto
  - memoria
  - allocatori
---

# Buddy Allocator

> [!summary] In breve
> Divide ricorsivamente la memoria in metà (albero binario); assegna il più piccolo blocco potenza di 2 che contiene la richiesta e, al rilascio, fonde un blocco con il suo buddy se anche questo è libero. Costo O(livelli).

- Indici dei nodi: `level = floor(log2(idx))`, `buddy = idx ^ 1` (pari +1, dispari −1), `parent = idx/2`, figli `2·idx` e `2·idx+1`, `firstIdx(l) = 1<<l`.
- **Una free list per livello**; i `BuddyListItem` sono allocati con uno SLAB.
- **malloc(size)**: livello = `floor(log2(mem_size/(size+8)))`; `getBuddy(level)`, che se la lista è vuota chiede ricorsivamente al livello superiore e divide il blocco ottenuto. Nei primi 8 byte salva il puntatore al `BuddyListItem` e restituisce `start + 8`.
- **free(p)**: legge l'item da `p - 8`, `releaseBuddy`: lo rimette in lista; se il buddy è libero li distrugge entrambi e rilascia ricorsivamente il genitore.
- Esempio: 90 KB su 1 MB danno un blocco da 128 KB (38 KB di frammentazione interna).
- Nella pratica: l'albero sta in una **bitmap**, nessuna ricorsione, ricerca bit a bit su 64 bit alla volta.

## Collegamenti

- **Concetti correlati**: [[SLAB Allocator]] · [[Frammentazione]] · [[Paging]]
- **Mappa**: [[MOC - Sistemi Operativi]] · [[MOC - Sistemi di Calcolo]]

> [!info] Approfondimento
> - [[07 - SO - Allocatori di Memoria#Buddy allocator|Lezione 7 — Buddy allocator]]
> - [[07 - SO - Allocatori di Memoria#L'albero binario|Lezione 7 — L'albero binario]]
> - [[07 - SO - Allocatori di Memoria#getBuddy|Lezione 7 — getBuddy]]
> - [[07 - SO - Allocatori di Memoria#Rilascio|Lezione 7 — Rilascio]]
> - [[07 - SDC - Gestione dei dati in memoria centrale#malloc e free|Sistemi di Calcolo, cap. 7 — malloc e free]]
