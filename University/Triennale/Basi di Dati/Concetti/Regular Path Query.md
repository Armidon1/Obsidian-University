---
title: Regular Path Query
tags:
  - basi-di-dati
  - concetto
  - nosql
  - grafi
---

# Regular Path Query

> [!summary] In breve
> Query su un grafo etichettato definita da un'espressione regolare L: restituisce le coppie di nodi collegate da un cammino la cui etichetta appartiene a L.

- $G = (V, E)$ con $E \subseteq V \times \Sigma \times V$; etichetta di un cammino $\lambda(\pi) = a_1 \dots a_m$.
- $L ::= s \mid L \cdot L \mid L|L \mid L^* \mid L^+ \mid L? \mid (L)$.
- "Antenati" = `isChildOf+`; con $L = ab^*$ su $x \xrightarrow{a} y \xrightarrow{b} t$: $(x, y), (x, t) \in L(G)$.

## Collegamenti

- **Concetti correlati**: [[Graph Database]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[07 - BD - NoSQL#Interrogare un graph database|Lezione 7 — Interrogare un graph database]]
