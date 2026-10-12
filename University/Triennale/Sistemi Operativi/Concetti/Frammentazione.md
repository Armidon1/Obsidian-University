---
title: Frammentazione
tags:
  - sistemi-operativi
  - concetto
  - memoria
---

# Frammentazione

> [!summary] In breve
> Memoria sprecata: **esterna** quando c'è abbastanza memoria libera in totale ma non contigua; **interna** quando un blocco assegnato è più grande del richiesto.

| Tecnica | Esterna | Interna |
| --- | --- | --- |
| Partizioni contigue / segmentazione | sì (si riduce con la compattazione) | — |
| SLAB | no | no (se item_size è quello giusto) |
| Buddy | limitata (merge dei buddy) | sì (arrotondamento a potenze di 2) |
| Paging | **no** | sì, nell'ultima pagina |

- La **compattazione** richiede rilocazione dinamica (a tempo di esecuzione).

## Collegamenti

- **Concetti correlati**: [[SLAB Allocator]] · [[Buddy Allocator]] · [[Allocazione Contigua]] · [[Paging]] · [[Segmentazione]]
- **Mappa**: [[MOC - Sistemi Operativi]]

> [!info] Approfondimento
> - [[07 - SO - Allocatori di Memoria#Il problema|Lezione 7 — Il problema]]
> - [[10 - SO - Gestione della Memoria#Allocazione contigua: partizioni multiple|Lezione 10 — Allocazione contigua: partizioni multiple]]
> - [[10 - SO - Gestione della Memoria#Paging|Lezione 10 — Paging]]
