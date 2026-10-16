---
title: Albero (a,b)
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - alberi-di-ricerca
  - memoria-esterna
---

# Albero (a,b)

> [!summary] In breve
> Albero di ricerca a più vie con $2 \le a \le (b+1)/2$: ogni nodo interno (tranne la radice) ha tra $a$ e $b$ figli e le foglie sono alla stessa profondità; altezza $\Theta(\log n / \log a)$.

- Generalizza gli [[Albero (2,4)|alberi (2,4)]]: stessi algoritmi (split per overflow, trasferimento o fusione per underflow).
- $a \le (b+1)/2$ garantisce che lo split di un $(b+1)$-nodo e la fusione di un $(a-1)$-nodo con un $a$-nodo diano nodi validi.
- Altezza: $\frac{\log(n+1)}{\log b} \le h \le \frac{\log((n+1)/2)}{\log a} + 1$.
- Scegliendo $a$, $b$ in base alla dimensione dei blocchi del disco si ottengono i [[B-albero|B-alberi]].

## Collegamenti

- **Concetti correlati**: [[B-albero]] · [[Albero (2,4)]] · [[Albero di ricerca a più vie]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[15 - ASD - Gestione della memoria e B-alberi#Alberi (a,b)|Lezione 15 — Alberi (a,b)]]
