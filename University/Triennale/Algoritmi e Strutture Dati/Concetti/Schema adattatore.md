---
title: Schema adattatore
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - design-pattern
---

# Schema adattatore

> [!summary] In breve
> L'adattatore (adapter) realizza un'interfaccia usando internamente un'altra classe, traducendo ogni metodo in una chiamata dell'oggetto adattato.

| Metodo della pila | Metodo della lista adattata |
|---|---|
| `push(e)` | `addFirst(e)` |
| `pop()` | `removeFirst()` |
| `top()` | `first()` |
| `size()` | `size()` |

Così `LinkedStack` e `LinkedQueue` riusano `SinglyLinkedList` con pochissimo codice.

## Collegamenti

- **Concetti correlati**: [[Pila (ADT)]] · [[Coda (ADT)]] · [[Tipo di dato astratto]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[06 - ASD - Pile, code e code doppie#Lo schema progettuale adattatore (adapter)|Lezione 6 — Lo schema progettuale adattatore (adapter)]]
