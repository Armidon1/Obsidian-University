---
title: Proprietà degli alberi binari
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - alberi
  - matematica
---

# Proprietà degli alberi binari

> [!summary] In breve
> Un albero binario di altezza $h$ ha tra $h+1$ e $2^{h+1}-1$ nodi, e quindi $\log(n+1) - 1 \le h \le n - 1$; in un albero binario proprio le foglie sono una in più dei nodi interni.

Al livello $d$ ci sono al più $2^d$ nodi. Con $n$ nodi, $n_E$ foglie, $n_I$ interni e altezza $h$:

| Grandezza | Limiti |
|---|---|
| $n$ | $h + 1 \le n \le 2^{h+1} - 1$ |
| $n_E$ | $1 \le n_E \le 2^h$ |
| $n_I$ | $h \le n_I \le 2^h - 1$ |
| $h$ | $\log(n+1) - 1 \le h \le n - 1$ |

**Albero proprio**: $n_E = n_I + 1$ (si dimostra togliendo coppie foglia-genitore), e $h \le (n-1)/2$.

Queste relazioni danno l'altezza logaritmica di heap e alberi bilanciati e il limite $\log(n!)$ degli alberi di decisione.

## Collegamenti

- **Concetti correlati**: [[Albero binario]] · [[Profondità e altezza di un albero]] · [[Limite inferiore per l'ordinamento basato su confronti]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[08 - ASD - Alberi#Proprietà degli alberi binari|Lezione 8 — Proprietà degli alberi binari]]
