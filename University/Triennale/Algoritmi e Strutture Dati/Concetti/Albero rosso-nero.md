---
title: Albero rosso-nero
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - alberi-di-ricerca
  - bilanciamento
---

# Albero rosso-nero

> [!summary] In breve
> BST con nodi rossi o neri (radice e foglie nere, figli di un rosso neri, stessa profondità nera per tutte le foglie): altezza $\le 2\log(n+1)$ e $O(1)$ ristrutturazioni per aggiornamento.

- Corrisponde a un [[Albero (2,4)|albero (2,4)]]: ogni nero con i suoi figli rossi è un nodo (2,4).
- **Inserimento** (nuovo nodo rosso) → **doppio rosso**:
  - zio nero → `restructure` (al più una) e ricolorazione;
  - zio rosso → ricolorazione (= split), che può propagarsi verso l'alto.
- **Rimozione** di un nero → **doppio nero**:
  - fratello nero con figlio rosso → ristrutturazione (= trasferimento);
  - fratello nero con figli neri → ricolorazione (= fusione), può propagarsi;
  - fratello rosso → rotazione (riorienta un 3-nodo), poi uno dei casi precedenti.
- Inserimento: ≤ 1 ristrutturazione; rimozione: ≤ 2; ricolorazioni $O(\log n)$. Usato da `java.util.TreeMap`.

## Collegamenti

- **Concetti correlati**: [[Albero (2,4)]] · [[Albero AVL]] · [[Rotazione e ristrutturazione di una terna]] · [[Mappa ordinata]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[11 - ASD - Alberi di ricerca#Alberi rosso-nero|Lezione 11 — Alberi rosso-nero]]
