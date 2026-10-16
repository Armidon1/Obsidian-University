---
title: Pila (ADT)
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - pile
  - adt
---

# Pila (ADT)

> [!summary] In breve
> Una pila (stack) è una collezione LIFO: si inserisce (`push`) e si estrae (`pop`) solo dalla cima; tutte le operazioni costano $O(1)$ con array o lista concatenata.

| Metodo | Effetto |
|---|---|
| `push(e)` | inserisce in cima |
| `pop()` | rimuove e restituisce la cima (`null` se vuota) |
| `top()` | restituisce la cima senza rimuoverla |
| `size()`, `isEmpty()` | |

- `ArrayStack`: array a capacità fissa, indice `t` della cima.
- `LinkedStack`: [[Schema adattatore|adattatore]] di una [[Lista semplicemente concatenata|lista semplicemente concatenata]] (cima = testa).
- Applicazioni: undo, cronologia del browser, inversione, [[Verifica di delimitatori con una pila|parentesi bilanciate]], [[Pila dei metodi di Java|pila delle invocazioni]], DFS iterativo.

## Collegamenti

- **Concetti correlati**: [[Coda (ADT)]] · [[Schema adattatore]] · [[Verifica di delimitatori con una pila]] · [[Pila dei metodi di Java]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[06 - ASD - Pile, code e code doppie#Pile (stack)|Lezione 6 — Pile (stack)]]
