---
title: Ricorsione lineare, binaria e multipla
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - ricorsione
---

# Ricorsione lineare, binaria e multipla

> [!summary] In breve
> Una ricorsione è lineare se ogni chiamata ne fa al più una, binaria se ne fa due, multipla se ne fa più di due.

| Tipo | Chiamate per invocazione | Esempi |
|---|---|---|
| lineare | ≤ 1 | fattoriale, somma di un array, ricerca binaria, inversione di un array |
| binaria | 2 | somma con divisione a metà, Fibonacci ingenuo, merge-sort |
| multipla | > 2 | enumerazione di permutazioni/sottoinsiemi, puzzle |

La somma binaria di $n$ elementi fa $2n - 1$ chiamate ma la profondità è solo $1 + \log n$ (spazio $O(\log n)$).

## Collegamenti

- **Concetti correlati**: [[Ricorsione]] · [[Fibonacci ricorsivo]] · [[Ricorsione in coda]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[05 - ASD - Ricorsione#Ulteriori esempi di ricorsione|Lezione 5 — Ulteriori esempi di ricorsione]]
