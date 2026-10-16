---
title: Quick-select probabilistico
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - selezione
  - randomizzazione
---

# Quick-select probabilistico

> [!summary] In breve
> Per trovare il $k$-esimo elemento più piccolo si partiziona con un pivot casuale in $L$, $E$, $G$ e si ricorre **solo** sulla parte che contiene il rango cercato: $O(n)$ atteso.

```text
quickSelect(S, k):
  se |S| = 1: return S[0]
  pivot x casuale; L = {< x}, E = {= x}, G = {> x}
  se k ≤ |L|:            return quickSelect(L, k)
  se k ≤ |L| + |E|:      return x
  altrimenti:            return quickSelect(G, k - |L| - |E|)
```

- Schema **prune-and-search** (come la ricerca binaria).
- Analisi: un pivot è "buono" ($|L|, |G| \le 3n/4$) con probabilità $\ge 1/2$ → $T(n) \le T(3n/4) + 2bn$ → serie geometrica → $O(n)$.
- Caso peggiore $O(n^2)$; esiste una versione deterministica $O(n)$ (mediana delle mediane) con costanti alte.

## Collegamenti

- **Concetti correlati**: [[Quick-sort]] · [[Ricerca binaria]] · [[Dividi-e-conquista]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[12 - ASD - Ordinamento e selezione#Selezione|Lezione 12 — Selezione]]
