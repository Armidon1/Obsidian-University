---
title: Algoritmo ottimo
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - lower-bound
---

# Algoritmo ottimo

> [!summary] In breve
> Un algoritmo è ottimo (ottimale) se il suo costo coincide asintoticamente con il lower bound del problema che risolve.

| problema | lower bound | algoritmo ottimo |
|---|---|---|
| ordinamento per confronti | $\Omega(n \log n)$ | merge sort, heap sort |
| ricerca in tabella ordinata | $\Omega(\log n)$ | ricerca binaria |
| massimo di un vettore | $\Omega(n)$ (banale) | scansione lineare |

Ottimo **rispetto a un modello**: il bucket sort ordina in $O(n)$ perché non usa solo confronti.

## Collegamenti

- **Concetti correlati**: [[Delimitazioni superiori e inferiori]] · [[Albero di decisione]] · [[Notazione Theta]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[05 - MC - Delimitazioni superiori e inferiori#Complessità intrinseca e algoritmi ottimi|Lezione 5 — Complessità intrinseca e algoritmi ottimi]]
> - [[05 - MC - Delimitazioni superiori e inferiori#Complessità inferiore dell'ordinamento|Lezione 5 — Complessità inferiore dell'ordinamento]]
