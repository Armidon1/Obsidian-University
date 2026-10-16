---
title: Mappa (ADT)
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - mappe
  - adt
---

# Mappa (ADT)

> [!summary] In breve
> Una mappa associa chiavi **uniche** a valori: `get(k)`, `put(k, v)` (sostituisce se la chiave esiste), `remove(k)`, più `keySet`, `values`, `entrySet`.

- Detta anche *array associativo* o *dizionario*; in Java `java.util.Map`.
- `get` e `remove` restituiscono `null` se la chiave manca (ambiguo se i valori possono essere `null`).

| Implementazione | `get`/`put`/`remove` |
|---|---|
| lista non ordinata | $O(n)$ |
| [[Tabella hash]] | $O(1)$ atteso |
| tabella ordinata (ricerca binaria) | $O(\log n)$ / $O(n)$ / $O(n)$ |
| [[Skip list]] | $O(\log n)$ atteso |
| alberi bilanciati (AVL, rosso-nero) | $O(\log n)$ |

## Collegamenti

- **Concetti correlati**: [[Tabella hash]] · [[Mappa ordinata]] · [[Insiemi, multi-insiemi e multi-mappe]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[10 - ASD - Mappe, tabelle hash e skip list#Mappe|Lezione 10 — Mappe]]
