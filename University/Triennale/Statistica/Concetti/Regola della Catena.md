---
title: Regola della Catena
tags:
  - probabilita-e-statistica
  - concetto
  - probabilita-condizionata
---

# Regola della Catena

> [!summary] In breve
> La probabilità dell'intersezione di più eventi è il prodotto delle probabilità condizionate di ciascuno dati i precedenti.

$$P(E\cap F)=P(E\mid F)\,P(F)\qquad\text{(formula inversa)}$$
$$P(E_1\cap\dots\cap E_n)=P(E_1)\,P(E_2\mid E_1)\,P(E_3\mid E_1\cap E_2)\cdots P(E_n\mid E_1\cap\dots\cap E_{n-1})$$

- Serve $P(E_1\cap\dots\cap E_{n-1})\ne0$.
- Esempio: 3 cuori di fila senza reinserimento $=\frac{13}{52}\cdot\frac{12}{51}\cdot\frac{11}{50}$.

## Collegamenti

- **Concetti correlati**: [[Conditional Probability]] · [[Formula di Fattorizzazione]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[02 - PS - Probabilità Condizionata e Indipendenza#Formula inversa|Lezione 2 — Formula inversa]]
> - [[02 - PS - Probabilità Condizionata e Indipendenza#Formula delle probabilità composte|Lezione 2 — Formula delle probabilità composte]]
