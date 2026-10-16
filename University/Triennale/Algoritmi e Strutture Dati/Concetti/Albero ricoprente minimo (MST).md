---
title: Albero ricoprente minimo (MST)
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - grafi
  - mst
---

# Albero ricoprente minimo (MST)

> [!summary] In breve
> Un MST di un grafo connesso, non orientato e pesato è un albero ricoprente di peso totale minimo; si basa sulla proprietà del taglio: il lato più leggero tra due parti di una partizione sta in un MST.

- **Proprietà del taglio**: per ogni partizione $(V_1, V_2)$ dei vertici, un lato di peso minimo tra $V_1$ e $V_2$ appartiene a qualche MST (scambio con un lato del ciclo creato).
- Pesi tutti distinti ⇒ MST unico. Vale anche con pesi negativi.

| Algoritmo | Strategia | Tempo |
|---|---|---|
| [[Algoritmo di Prim-Jarník|Prim-Jarník]] | un albero che cresce da una radice | $O(m\log n)$ |
| [[Algoritmo di Kruskal|Kruskal]] | lati in ordine crescente, cluster con union-find | $O(m\log n)$ |

## Collegamenti

- **Concetti correlati**: [[Algoritmo di Prim-Jarník]] · [[Algoritmo di Kruskal]] · [[Metodo greedy]] · [[Partizione union-find]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[14 - ASD - Algoritmi per grafi#Alberi ricoprenti minimi|Lezione 14 — Alberi ricoprenti minimi]]
