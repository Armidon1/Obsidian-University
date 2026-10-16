---
title: Mappa ordinata
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - mappe
  - adt
---

# Mappa ordinata

> [!summary] In breve
> Una mappa ordinata mantiene le chiavi in ordine e aggiunge ricerche approssimate (`floorEntry`, `ceilingEntry`, `lowerEntry`, `higherEntry`), `firstEntry`, `lastEntry` e intervalli `subMap(k1, k2)`.

Implementazioni:

| | Ricerca | Inserimento / rimozione |
|---|---|---|
| tabella ordinata (array + ricerca binaria) | $O(\log n)$ | $O(n)$ |
| [[Skip list]] | $O(\log n)$ atteso | $O(\log n)$ atteso |
| [[Albero di ricerca binario|BST]] | $O(h)$ | $O(h)$ |
| AVL, splay, (2,4), rosso-nero | $O(\log n)$ | $O(\log n)$ |

Applicazioni: database di voli (volo più vicino all'orario richiesto), insiemi di massimi (*maxima set*: coppie costo/prestazione non dominate).

## Collegamenti

- **Concetti correlati**: [[Mappa (ADT)]] · [[Skip list]] · [[Albero di ricerca binario]] · [[Ricerca binaria]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[10 - ASD - Mappe, tabelle hash e skip list#Mappe ordinate|Lezione 10 — Mappe ordinate]]
