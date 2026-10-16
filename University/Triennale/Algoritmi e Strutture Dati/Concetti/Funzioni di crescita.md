---
title: Funzioni di crescita
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - analisi
  - matematica
---

# Funzioni di crescita

> [!summary] In breve
> Sette funzioni descrivono quasi tutti i tempi d'esecuzione: costante, logaritmo, lineare, $n\log n$, quadratica, cubica, esponenziale.

| Funzione | Nome | Esempio |
|---|---|---|
| $1$ | costante | accesso a un array |
| $\log n$ | logaritmica | ricerca binaria |
| $n$ | lineare | massimo di un array |
| $n\log n$ | $n$-log-$n$ | merge-sort |
| $n^2$ | quadratica | insertion-sort (caso peggiore) |
| $n^3$ | cubica | moltiplicazione di matrici |
| $2^n$ | esponenziale | tutti i sottoinsiemi |

Utili: $\log_b a = \log_c a / \log_c b$; $\sum_{i=1}^n i = n(n+1)/2$; $\sum_{i=0}^n a^i = (a^{n+1} - 1)/(a - 1)$ (serie geometrica).

## Collegamenti

- **Concetti correlati**: [[Notazione asintotica]] · [[Analisi del caso peggiore]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[04 - ASD - Analisi di algoritmi#Le sette funzioni usate in questo libro|Lezione 4 — Le sette funzioni usate in questo libro]]
