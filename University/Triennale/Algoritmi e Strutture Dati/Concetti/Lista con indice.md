---
title: Lista con indice
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - liste
  - adt
---

# Lista con indice

> [!summary] In breve
> L'ADT lista con indice accede agli elementi per posizione intera $0..n-1$ (`get(i)`, `set(i,e)`, `add(i,e)`, `remove(i)`); su array l'accesso è $O(1)$ ma inserire o togliere in mezzo costa $O(n)$.

| Metodo | Array (`ArrayList`) |
|---|---|
| `size`, `isEmpty`, `get`, `set` | $O(1)$ |
| `add(i, e)`, `remove(i)` | $O(n - i + 1)$ (spostamento degli elementi successivi) |
| `add(e)` in fondo | $O(1)$ ammortizzato con [[Array dinamico|array dinamico]] |

Indici fuori dall'intervallo → `IndexOutOfBoundsException`.

## Collegamenti

- **Concetti correlati**: [[Array dinamico]] · [[Lista posizionale]] · [[Iteratore]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[07 - ASD - Liste e iteratori#Liste con indice|Lezione 7 — Liste con indice]]
