---
title: Grafo orientato aciclico e ordinamento topologico
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - grafi
  - dag
---

# Grafo orientato aciclico e ordinamento topologico

> [!summary] In breve
> Un DAG è un grafo orientato senza cicli; ammette un ordinamento topologico (ogni lato va da un vertice precedente a uno successivo) se e solo se è aciclico, e lo si calcola in $O(n + m)$.

- Esempi: prerequisiti tra esami, ereditarietà tra classi, vincoli di scheduling.
- Algoritmo: si contano i gradi entranti (`inCount`); si mettono in una pila i vertici con conteggio 0; si estrae, si aggiunge all'ordine e si decrementano i vicini uscenti.
- Se alla fine restano vertici non ordinati, il grafo contiene un **ciclo orientato**.
- L'ordinamento può non essere unico.

## Collegamenti

- **Concetti correlati**: [[Attraversamento in profondità (DFS)]] · [[Grafo (ADT)]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[14 - ASD - Algoritmi per grafi#Grafi orientati aciclici|Lezione 14 — Grafi orientati aciclici]]
