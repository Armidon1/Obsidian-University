---
title: Coda doppia (deque)
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - code
  - adt
---

# Coda doppia (deque)

> [!summary] In breve
> Una deque ("deck") permette inserimenti e rimozioni a entrambe le estremità in $O(1)$; generalizza pila e coda.

| Metodo | Effetto |
|---|---|
| `addFirst(e)`, `addLast(e)` | inserimento in testa / in coda |
| `removeFirst()`, `removeLast()` | rimozione in testa / in coda |
| `first()`, `last()` | lettura |

Implementazioni: array circolare (indice di testa con `(f - 1 + N) % N`) o [[Lista doppiamente concatenata|lista doppiamente concatenata]] (una semplice non basta per `removeLast`). In Java: `java.util.ArrayDeque`, `LinkedList`.

## Collegamenti

- **Concetti correlati**: [[Pila (ADT)]] · [[Coda (ADT)]] · [[Lista doppiamente concatenata]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[06 - ASD - Pile, code e code doppie#Code doppie|Lezione 6 — Code doppie]]
