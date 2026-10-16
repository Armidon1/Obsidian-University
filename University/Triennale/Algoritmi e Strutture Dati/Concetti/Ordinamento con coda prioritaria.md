---
title: Ordinamento con coda prioritaria
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - ordinamento
  - code-prioritarie
---

# Ordinamento con coda prioritaria

> [!summary] In breve
> Si inseriscono tutti gli elementi in una coda prioritaria e li si estrae con `removeMin`: il tempo dipende dall'implementazione della coda (selection-sort, insertion-sort o heap-sort).

| Coda prioritaria | Fase 1 ($n$ insert) | Fase 2 ($n$ removeMin) | Algoritmo |
|---|---|---|---|
| lista non ordinata | $O(n)$ | $O(n^2)$ | **selection-sort** |
| lista ordinata | $O(n^2)$ | $O(n)$ | **insertion-sort** |
| heap | $O(n\log n)$ | $O(n\log n)$ | **heap-sort** |

## Collegamenti

- **Concetti correlati**: [[Heap sort]] · [[Ordinamento per inserimento]] · [[Coda prioritaria (ADT)]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[09 - ASD - Code prioritarie#Ordinare con una coda prioritaria|Lezione 9 — Ordinare con una coda prioritaria]]
