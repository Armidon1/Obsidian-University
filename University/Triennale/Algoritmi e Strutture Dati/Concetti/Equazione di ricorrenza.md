---
title: Equazione di ricorrenza
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - analisi
  - ricorsione
---

# Equazione di ricorrenza

> [!summary] In breve
> Un'equazione di ricorrenza definisce il tempo di un algoritmo ricorsivo in funzione di sé stesso su input più piccoli; la si risolve ad esempio per sostituzioni ripetute fino al caso base.

Esempio (merge-sort): $t(n) = 2t(n/2) + cn$, $t(1) = b$.
$$t(n) = 2^i t(n/2^i) + icn \;\xrightarrow{\;i = \log n\;}\; t(n) = bn + cn\log n = O(n\log n)$$

Altri esempi:

| Ricorrenza | Soluzione | Algoritmo |
|---|---|---|
| $T(n) = T(n/2) + c$ | $O(\log n)$ | ricerca binaria |
| $T(n) = T(3n/4) + bn$ | $O(n)$ | quick-select (atteso) |
| $t(n) = d\,t(n/d) + cn/B$ | $O(\frac{n}{B}\log_d\frac{n}{B})$ | merge-sort a più vie |

## Collegamenti

- **Concetti correlati**: [[Merge-sort]] · [[Dividi-e-conquista]] · [[Notazione asintotica]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[12 - ASD - Ordinamento e selezione#Merge-sort ed equazioni di ricorrenza|Lezione 12 — Merge-sort ed equazioni di ricorrenza]]
