---
title: Algoritmi di sostituzione delle pagine
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - memoria
  - cache
---

# Algoritmi di sostituzione delle pagine

> [!summary] In breve
> Quando la cache è piena bisogna espellere un blocco: FIFO (il più vecchio inserito), LRU (il meno recentemente usato) o casuale; in pratica LRU > FIFO > casuale, ma FIFO e LRU hanno un caso peggiore pessimo.

| Strategia | Struttura | Località temporale |
|---|---|---|
| random | generatore pseudocasuale | ignorata |
| FIFO | coda | poca |
| LRU | coda prioritaria flessibile / lista con spostamento in fondo | sfruttata al meglio, costanti alte |

- Caso peggiore: un ciclo su $m + 1$ pagine con cache di $m$ → FIFO e LRU sbagliano **ogni** richiesta.
- Si basano su caching (località temporale) e blocking (località spaziale).
- Vedi [[Page Replacement]] (SO) e [[Clock Replacement Policy]] (DBMS).

## Collegamenti

- **Concetti correlati**: [[Page Replacement]] · [[Località dei Riferimenti]] · [[Euristica move-to-front]] · [[Memoria Cache]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[15 - ASD - Gestione della memoria e B-alberi#Algoritmi di sostituzione delle pagine|Lezione 15 — Algoritmi di sostituzione delle pagine]]
