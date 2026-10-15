---
title: Formula di Fattorizzazione
tags:
  - probabilita-e-statistica
  - concetto
  - probabilita-condizionata
---

# Formula di Fattorizzazione

> [!summary] In breve
> Se $F_1,\dots,F_n$ sono una partizione di $S$, $P(E)=\sum_iP(E\mid F_i)P(F_i)$: la probabilità di $E$ è la media pesata delle sue probabilità condizionate.

$$P(E)=P(E\mid F)P(F)+P(E\mid F^c)\,[1-P(F)]$$
$$P(E)=\sum_{i=1}^nP(E\cap F_i)=\sum_{i=1}^nP(E\mid F_i)P(F_i)$$

- Detta anche **teorema della probabilità totale** o formula di disintegrazione.
- È il denominatore della formula di Bayes.
- Versione per i valori attesi: [[Teorema del Valore Atteso Iterato]].

## Collegamenti

- **Concetti correlati**: [[Teorema di Bayes]] · [[Conditional Probability]] · [[Teorema del Valore Atteso Iterato]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[02 - PS - Probabilità Condizionata e Indipendenza#Fattorizzazione di un evento|Lezione 2 — Fattorizzazione di un evento]]
> - [[02 - PS - Probabilità Condizionata e Indipendenza#Generalizzazione: formula di fattorizzazione|Lezione 2 — Generalizzazione: formula di fattorizzazione]]
