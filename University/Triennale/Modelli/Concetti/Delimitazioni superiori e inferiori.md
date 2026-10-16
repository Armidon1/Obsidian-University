---
title: Delimitazioni superiori e inferiori
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - lower-bound
---

# Delimitazioni superiori e inferiori

> [!summary] In breve
> Un problema ha **upper bound** $O(f)$ se *esiste* un algoritmo con quel costo; ha **lower bound** $\Omega(g)$ se *ogni* algoritmo che lo risolve costa almeno $\Omega(g)$.

| | upper bound | lower bound |
|---|---|---|
| quantificatore | $\exists$ algoritmo | $\forall$ algoritmi |
| come si prova | esibendo un algoritmo | lower bound banale, alberi di decisione, riduzioni |
| esempio (ordinamento) | merge sort: $O(n \log n)$ | $\Omega(n \log n)$ per confronti |

- Se coincidono si ha la **complessità intrinseca** e gli algoritmi che la raggiungono sono [[Algoritmo ottimo|ottimi]].
- Il lower bound di un singolo algoritmo non dà il lower bound del problema.
- **Lower bound banale**: bisogna leggere tutto l'input, $\Omega(n)$ (non vale per la ricerca binaria).

## Collegamenti

- **Concetti correlati**: [[Algoritmo ottimo]] · [[Albero di decisione]] · [[Notazione Omega]] · [[Riduzione polinomiale]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[05 - MC - Delimitazioni superiori e inferiori#Delimitazione superiore e inferiore alla complessità di problemi|Lezione 5 — Delimitazione superiore e inferiore alla complessità di problemi]]
> - [[05 - MC - Delimitazioni superiori e inferiori#Tecniche per calcolare il lower bound|Lezione 5 — Tecniche per calcolare il lower bound]]
> - [[01 - MC - Costo degli algoritmi e modello CEM#Upper bound e lower bound: l'idea|Lezione 1 — Upper bound e lower bound: l'idea]]
