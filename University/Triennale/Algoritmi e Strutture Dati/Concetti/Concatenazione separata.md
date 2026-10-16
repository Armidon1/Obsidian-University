---
title: Concatenazione separata
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - hashing
---

# Concatenazione separata

> [!summary] In breve
> Ogni bucket della tabella hash contiene una piccola mappa (lista) con tutte le voci che vi collidono; il costo atteso delle operazioni è $O(1 + \lambda)$.

- Semplice, tollera fattori di carico vicini a 1 (si consiglia $\lambda < 0.9$).
- Spazio extra per le strutture secondarie.
- In Java: `ChainHashMap` del libro; `java.util.HashMap` usa una variante (con alberi per i bucket molto lunghi).

## Collegamenti

- **Concetti correlati**: [[Tabella hash]] · [[Indirizzamento aperto]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[10 - ASD - Mappe, tabelle hash e skip list#Concatenazione separata|Lezione 10 — Concatenazione separata]]
