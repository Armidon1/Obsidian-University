---
title: Teorema del Valore Atteso Iterato
tags:
  - probabilita-e-statistica
  - concetto
  - valore-atteso
---

# Teorema del Valore Atteso Iterato

> [!summary] In breve
> $E[E[Y\mid X]]=E[Y]$: la media delle medie condizionate è la media globale.

$$E[X]=\sum_yE[X\mid Y=y]\,P(Y=y)$$

- Versione "per valori attesi" della [[Formula di Fattorizzazione]].
- Somma di un numero aleatorio $N$ di v.a. i.i.d. indipendenti da $N$: $E\big[\sum_{i=1}^NX_i\big]=E[N]\,E[X]$.
- Esempio del labirinto: $E[X]=\frac13(5+3+E[X]+8+E[X])\Rightarrow E[X]=16$.

## Collegamenti

- **Concetti correlati**: [[Valore Atteso Condizionato]] · [[Formula di Fattorizzazione]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[04 - PS - Valore Atteso, Varianza e Covarianza#Teorema sul valore atteso del valore atteso condizionato|Lezione 4 — Teorema sul valore atteso del valore atteso condizionato]]
