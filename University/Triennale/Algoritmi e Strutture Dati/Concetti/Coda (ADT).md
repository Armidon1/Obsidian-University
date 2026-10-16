---
title: Coda (ADT)
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - code
  - adt
---

# Coda (ADT)

> [!summary] In breve
> Una coda (queue) è una collezione FIFO: si inserisce in fondo (`enqueue`) e si estrae dall'inizio (`dequeue`), entrambe in $O(1)$ con array circolare o lista concatenata.

| Metodo | Effetto |
|---|---|
| `enqueue(e)` | aggiunge in fondo |
| `dequeue()` | rimuove e restituisce il primo (`null` se vuota) |
| `first()` | restituisce il primo senza rimuoverlo |

- `ArrayQueue`: [[Array circolare|array circolare]] con indice `f` e dimensione `sz`.
- `LinkedQueue`: adattatore di una lista semplicemente concatenata (`addLast` / `removeFirst`).
- Applicazioni: buffer, [[Produttore-Consumatore]], BFS, scheduling [[Round Robin]].

## Collegamenti

- **Concetti correlati**: [[Pila (ADT)]] · [[Array circolare]] · [[Coda doppia (deque)]] · [[Attraversamento in ampiezza (BFS)]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[06 - ASD - Pile, code e code doppie#Code (queue)|Lezione 6 — Code (queue)]]
