---
title: TDS - Principio di separazione
tags:
  - teoria-dei-sistemi
  - concetto
  - osservatore
  - retroazione-dallo-stato
---

# TDS - Principio di separazione

> [!summary] In breve
> Retroazionando la stima dell\'osservatore ($u=v+Fz$), gli autovalori del sistema complessivo sono quelli di $A+BF$ uniti a quelli di $A-KC$: $F$ e $K$ si progettano separatamente.

- Coordinate $(x,e)$ con $e=z-x$: matrice $\begin{psmallmatrix}A+BF&BF\\0&A-KC\end{psmallmatrix}$.
- $W(s)=C(sI-A-BF)^{-1}B$: l'osservatore non si vede nel legame ingresso-uscita (è non raggiungibile).
- Stabilizzazione dall'uscita possibile ⟺ sistema stabilizzabile e rilevabile.

## Collegamenti

- **Concetti correlati**: [[TDS - Osservatore asintotico]] · [[TDS - Retroazione dallo stato]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[40 - TDS - Principio di separazione#Principio di separazione|Lezione 40 — Principio di separazione]]
> - [[40 - TDS - Principio di separazione#Osservatore nel legame ingresso-uscita|Lezione 40 — Osservatore nel legame ingresso-uscita]]
