---
title: Costruzione bottom-up di uno heap
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - code-prioritarie
  - analisi
---

# Costruzione bottom-up di uno heap

> [!summary] In breve
> Dati $n$ elementi, si costruisce uno heap in $O(n)$ (invece di $O(n\log n)$) applicando down-heap ai nodi interni dal basso verso l'alto.

```java
int startIndex = parent(size() - 1);
for (int j = startIndex; j >= 0; j--)
  downheap(j);
```

Perché $O(n)$: il down-heap di un nodo costa quanto la sua altezza, e la somma delle altezze di tutti i nodi di un albero completo è $O(n)$ (pochi nodi in alto, dove il costo è alto). Usata da heap-sort e da Kruskal per inizializzare la coda dei lati.

## Collegamenti

- **Concetti correlati**: [[Heap binario]] · [[Heap sort]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[09 - ASD - Code prioritarie#Costruzione di uno heap dal basso verso l'alto (bottom-up)|Lezione 9 — Costruzione di uno heap dal basso verso l'alto (bottom-up)]]
