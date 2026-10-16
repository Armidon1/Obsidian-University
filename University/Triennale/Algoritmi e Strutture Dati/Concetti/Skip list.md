---
title: Skip list
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - mappe
  - randomizzazione
---

# Skip list

> [!summary] In breve
> Una skip list è una pila di liste ordinate: ogni elemento sale al livello successivo con probabilità 1/2 (lancio di moneta); ricerca, inserimento e rimozione costano $O(\log n)$ atteso.

- Livello $S_0$ con tutte le chiavi; $S_{i+1}$ contiene circa metà delle chiavi di $S_i$; sentinelle $-\infty$ e $+\infty$ in ogni lista.
- **Ricerca**: si parte in alto a sinistra; si va a destra finché la chiave successiva è $\le k$, poi si scende ("scendi e scorri").
- **Inserimento**: si inserisce in $S_0$ e si "promuove" lanciando una moneta finché esce croce.
- Altezza attesa $O(\log n)$, spazio atteso $O(n)$.
- Struttura **randomizzata**: le prestazioni non dipendono dall'ordine degli input (servono buoni numeri pseudocasuali: [[PRNG (Pseudo-Random Number Generator)]]).

## Collegamenti

- **Concetti correlati**: [[Mappa ordinata]] · [[Mappa (ADT)]] · [[Albero rosso-nero]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[10 - ASD - Mappe, tabelle hash e skip list#Skip list|Lezione 10 — Skip list]]
