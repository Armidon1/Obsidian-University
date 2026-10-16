---
title: Iteratore
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - liste
  - java
---

# Iteratore

> [!summary] In breve
> Un iteratore scandisce una collezione un elemento alla volta con `hasNext()` e `next()`; una classe `Iterable` fornisce `iterator()` e si può usare nel ciclo for-each.

```java
for (E e : list) { ... }      // equivale a:
Iterator<E> it = list.iterator();
while (it.hasNext()) { E e = it.next(); ... }
```

- `remove()` opzionale: elimina l'ultimo elemento restituito.
- Iteratore **lazy** (legge la struttura man mano) vs **snapshot** (copia iniziale): il lazy è $O(1)$ in spazio ma si invalida se la struttura cambia (`ConcurrentModificationException`, *fail-fast*).
- Nel libro: `iterator()` sugli elementi e `positions()` sulle posizioni.

## Collegamenti

- **Concetti correlati**: [[Lista posizionale]] · [[Attraversamenti di un albero]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[07 - ASD - Liste e iteratori#Iteratori|Lezione 7 — Iteratori]]
