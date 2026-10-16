---
title: Heap sort
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - ordinamento
  - code-prioritarie
---

# Heap sort

> [!summary] In breve
> Heap-sort costruisce uno heap e ne estrae ripetutamente il massimo (o minimo): $O(n\log n)$ nel caso peggiore, sul posto, non stabile.

Versione sul posto su un array:
1. si costruisce un **max-heap** nell'array (bottom-up, $O(n)$);
2. per $i = n-1, \dots, 1$: si scambia la radice (massimo) con l'elemento in posizione $i$ e si fa down-heap sulla parte $0..i-1$.

Alla fine l'array è ordinato in modo crescente. Ottimo asintoticamente tra gli ordinamenti per confronti, ma in pratica spesso più lento di quick-sort e merge-sort su grandi input.

## Collegamenti

- **Concetti correlati**: [[Heap binario]] · [[Costruzione bottom-up di uno heap]] · [[Quick-sort]] · [[Merge-sort]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[09 - ASD - Code prioritarie#Heap Sort|Lezione 9 — Heap Sort]]
