---
title: Lista concatenata circolare
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - liste
  - strutture-dati
---

# Lista concatenata circolare

> [!summary] In breve
> Lista semplicemente concatenata in cui l'ultimo nodo punta al primo: basta il riferimento `tail` (la testa è `tail.next`) e `rotate()` sposta il primo elemento in fondo in $O(1)$.

- `first()` = `tail.getNext()`; `rotate()`: `tail = tail.getNext()`.
- Utile per il **round-robin** (scheduling circolare dei processi, [[Round Robin]]) e per il [[Problema di Josephus]].

## Collegamenti

- **Concetti correlati**: [[Lista semplicemente concatenata]] · [[Coda (ADT)]] · [[Array circolare]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[03 - ASD - Strutture dati fondamentali#Liste concatenate circolari|Lezione 3 — Liste concatenate circolari]]
