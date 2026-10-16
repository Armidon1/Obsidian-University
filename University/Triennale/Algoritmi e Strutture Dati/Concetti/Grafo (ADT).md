---
title: Grafo (ADT)
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - grafi
  - adt
---

# Grafo (ADT)

> [!summary] In breve
> Un grafo $G = (V, E)$ è un insieme di vertici e una collezione di lati (coppie di vertici), orientati o no; l'ADT offre vertici, lati, adiacenze, gradi, inserimenti e rimozioni.

- Termini: adiacenti, incidente, grado $\deg(v)$, $\text{indeg}$/$\text{outdeg}$, percorso, ciclo, semplice, connesso, fortemente connesso, sotto-grafo ricoprente, foresta, albero, albero ricoprente.
- **Proprietà**: $\sum_v \deg(v) = 2m$; nei orientati $\sum \text{indeg} = \sum \text{outdeg} = m$; grafo semplice: $m \le n(n-1)/2$ (non orientato), $m \le n(n-1)$ (orientato).
- Grafo non orientato: connesso ⇒ $m \ge n - 1$; albero ⇒ $m = n - 1$; foresta ⇒ $m \le n - 1$.
- Metodi: `vertices`, `edges`, `getEdge(u,v)`, `endVertices(e)`, `opposite(v,e)`, `outDegree`, `inDegree`, `outgoingEdges`, `incomingEdges`, `insertVertex`, `insertEdge`, `removeVertex`, `removeEdge`.

## Collegamenti

- **Concetti correlati**: [[Strutture dati per grafi]] · [[Attraversamento in profondità (DFS)]] · [[Attraversamento in ampiezza (BFS)]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[14 - ASD - Algoritmi per grafi#Grafi|Lezione 14 — Grafi]]
