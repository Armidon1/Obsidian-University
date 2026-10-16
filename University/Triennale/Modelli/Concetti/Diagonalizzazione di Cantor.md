---
title: Diagonalizzazione di Cantor
tags:
  - modelli-di-calcolo
  - concetto
  - calcolabilita
  - insiemi
  - diagonalizzazione
---

# Diagonalizzazione di Cantor

> [!summary] In breve
> Data una lista $\sigma_0, \sigma_1, \dots$ di sequenze infinite, si costruisce una sequenza diagonale diversa dall'$i$-esima nella posizione $i$: non è nella lista. Dimostra la non numerabilità e l'indecidibilità.

| | 0 | 1 | 2 | ⋯ |
|---|---|---|---|---|
| $\sigma_0$ | **$a_{00}$** | $a_{01}$ | $a_{02}$ | |
| $\sigma_1$ | $a_{10}$ | **$a_{11}$** | $a_{12}$ | |
| $\sigma_2$ | $a_{20}$ | $a_{21}$ | **$a_{22}$** | |

Si pone $\bar\sigma_i \ne a_{ii}$ (per esempio $1 - a_{ii}$, o la cifra $+1 \bmod 10$).

Applicazioni:
- $\mathbb{R}$ e $\mathcal{P}(\mathbb{N})$ non sono numerabili;
- le funzioni caratteristiche $\hat f(i) = 1 - f_i(i)$ non sono numerabili;
- **Halting Problem**: `diag` fa l'opposto di ciò che `itHalts` predice sul suo stesso codice.

## Collegamenti

- **Concetti correlati**: [[Insieme numerabile]] · [[Problema della fermata]] · [[Equinumerosità]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[06 - MC - Cardinalità e diagonalizzazione#Insiemi non numerabili: la diagonalizzazione|Lezione 6 — Insiemi non numerabili: la diagonalizzazione]]
> - [[06 - MC - Cardinalità e diagonalizzazione#L'insieme delle parti dei naturali non è numerabile|Lezione 6 — L'insieme delle parti dei naturali non è numerabile]]
> - [[07 - MC - Halting Problem#Perché si chiama diagonalizzazione|Lezione 7 — Perché si chiama diagonalizzazione]]
