---
title: Coda prioritaria (ADT)
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - code-prioritarie
  - adt
---

# Coda prioritaria (ADT)

> [!summary] In breve
> Una coda prioritaria memorizza voci (chiave, valore) e permette di estrarre in ogni momento quella con chiave **minima**.

| Metodo | Lista non ordinata | Lista ordinata | Heap |
|---|---|---|---|
| `insert(k, v)` | $O(1)$ | $O(n)$ | $O(\log n)$ |
| `min()` | $O(n)$ | $O(1)$ | $O(1)$ |
| `removeMin()` | $O(n)$ | $O(1)$ | $O(\log n)$ |

- Le chiavi devono avere un **ordine totale** (riflessivo, antisimmetrico, transitivo, totale); si confrontano con un [[Comparatore|comparatore]].
- Chiavi uguali ammesse.
- Usi: scheduling, [[Algoritmo di Dijkstra|Dijkstra]], [[Algoritmo di Prim-Jarník|Prim]], [[Algoritmo di Kruskal|Kruskal]], [[Codifica di Huffman|Huffman]], simulazioni a eventi.

## Collegamenti

- **Concetti correlati**: [[Heap binario]] · [[Comparatore]] · [[Coda prioritaria flessibile]] · [[Ordinamento con coda prioritaria]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[09 - ASD - Code prioritarie#La coda prioritaria come ADT|Lezione 9 — La coda prioritaria come ADT]]
