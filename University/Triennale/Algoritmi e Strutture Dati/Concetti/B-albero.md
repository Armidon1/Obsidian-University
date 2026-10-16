---
title: B-albero
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - alberi-di-ricerca
  - memoria-esterna
---

# B-albero

> [!summary] In breve
> Un B-albero di ordine $d$ è un albero (a,b) con $a = \lceil d/2 \rceil$, $b = d$, con $d$ scelto perché un nodo stia in un blocco del disco: ogni operazione costa $O(\log_B n)$ trasferimenti e i blocchi sono pieni almeno a metà.

- Overflow ($d + 1$ figli) → split in $\lfloor (d+1)/2 \rfloor$ e $\lceil (d+1)/2 \rceil$ figli.
- Underflow ($\lceil d/2 \rceil - 1$ figli) → trasferimento da un fratello con $\ge \lceil d/2 \rceil + 1$ figli, o fusione.
- Spazio $O(n/B)$ blocchi.

Confronto dei trasferimenti per una ricerca:

| Struttura | Trasferimenti |
|---|---|
| lista concatenata | $n$ |
| alberi binari bilanciati | $O(\log_2 n)$ |
| B-albero | $O(\log_B n)$ |

Nei DBMS si usa la variante [[B+-Tree]].

## Collegamenti

- **Concetti correlati**: [[Albero (a,b)]] · [[Albero (2,4)]] · [[B+-Tree]] · [[Merge-sort a più vie]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[15 - ASD - Gestione della memoria e B-alberi#B-alberi|Lezione 15 — B-alberi]]
