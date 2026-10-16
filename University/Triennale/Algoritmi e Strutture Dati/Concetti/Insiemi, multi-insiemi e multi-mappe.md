---
title: Insiemi, multi-insiemi e multi-mappe
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - mappe
  - adt
---

# Insiemi, multi-insiemi e multi-mappe

> [!summary] In breve
> Un insieme è una collezione senza duplicati (chiavi senza valori); un multi-insieme (bag) ammette ripetizioni contando le occorrenze; una multi-mappa associa più valori alla stessa chiave.

| ADT | Implementazione tipica |
|---|---|
| insieme (`Set`) | mappa con chiavi = elementi (hash o ordinata) |
| multi-insieme | mappa elemento → numero di occorrenze |
| multi-mappa | mappa chiave → lista di valori |

Operazioni insiemistiche: unione (`addAll`), intersezione (`retainAll`), differenza (`removeAll`). Con insiemi ordinati, la fusione di due liste ordinate le calcola in tempo lineare.

## Collegamenti

- **Concetti correlati**: [[Mappa (ADT)]] · [[Tabella hash]] · [[Indice inverso]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[10 - ASD - Mappe, tabelle hash e skip list#Insiemi, multi-insiemi e multi-mappe|Lezione 10 — Insiemi, multi-insiemi e multi-mappe]]
