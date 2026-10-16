---
title: Coda prioritaria flessibile
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - code-prioritarie
  - adt
---

# Coda prioritaria flessibile

> [!summary] In breve
> Una coda prioritaria flessibile (adaptable) permette anche di rimuovere una voce qualsiasi e di cambiarne chiave o valore, grazie a voci "location-aware" che ricordano la propria posizione nello heap.

| Metodo | Heap con voci location-aware |
|---|---|
| `remove(e)` | $O(\log n)$ |
| `replaceKey(e, k)` | $O(\log n)$ (up-heap o down-heap) |
| `replaceValue(e, v)` | $O(1)$ |

Ogni voce memorizza il proprio indice nell'array e lo aggiorna a ogni scambio. Indispensabile per [[Algoritmo di Dijkstra|Dijkstra]] e [[Algoritmo di Prim-Jarník|Prim-Jarník]] (aggiornamento delle etichette $D[v]$).

## Collegamenti

- **Concetti correlati**: [[Coda prioritaria (ADT)]] · [[Heap binario]] · [[Algoritmo di Dijkstra]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[09 - ASD - Code prioritarie#Code prioritarie flessibili|Lezione 9 — Code prioritarie flessibili]]
