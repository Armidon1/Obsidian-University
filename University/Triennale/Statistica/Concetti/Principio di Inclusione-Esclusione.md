---
title: Principio di Inclusione-Esclusione
tags:
  - probabilita-e-statistica
  - concetto
  - calcolo-combinatorio
---

# Principio di Inclusione-Esclusione

> [!summary] In breve
> La cardinalità (o probabilità) di un'unione si ottiene sommando gli insiemi singoli, togliendo le intersezioni a due a due, aggiungendo quelle a tre a tre, e così via a segni alterni.

$$|A\cup B|=|A|+|B|-|A\cap B|$$
$$|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|$$
$$P\Big(\bigcup_{i=1}^nE_i\Big)=\sum_iP(E_i)-\sum_{i<j}P(E_i\cap E_j)+\dots+(-1)^{n+1}P(E_1\cap\dots\cap E_n)$$

- Segno "+" per intersezioni di un numero dispari di insiemi, "−" per un numero pari.
- Se gli eventi sono incompatibili resta solo $\sum_iP(E_i)$.

## Collegamenti

- **Concetti correlati**: [[Assiomi della Probabilità]] · [[Leggi di De Morgan]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[01 - PS - Spazi di Probabilità e Calcolo Combinatorio#Principio di inclusione-esclusione|Lezione 1 — Principio di inclusione-esclusione]]
> - [[02 - PS - Probabilità Condizionata e Indipendenza#Probabilità dell'unione|Lezione 2 — Probabilità dell'unione]]
