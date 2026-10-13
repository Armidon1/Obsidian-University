---
title: Negazione in Algebra Relazionale
tags:
  - basi-di-dati
  - concetto
  - algebra-relazionale
---

# Negazione in Algebra Relazionale

> [!summary] In breve
> L'unico modo di esprimere una negazione (e il 'per ogni') in algebra è la differenza: si tolgono dall'insieme gli elementi che soddisfano la proprietà.

$$\{x \mid x \in A \land \lnot B(x)\} = A - \{x \mid B(x)\}$$
$$\{x \in S \mid \forall y\, (R(x,y) \to A(y))\} = S - \{x \mid \exists y\, R(x,y) \land \lnot A(y)\}$$

- Esempio: capi i cui impiegati guadagnano **tutti** più di 40 = capi − capi con almeno un impiegato ≤ 40.
- Gli elementi senza alcun $y$ restano (verità a vuoto).
- In SQL: `not in`, `not exists`, `except`.

## Collegamenti

- **Concetti correlati**: [[Algebra Relazionale]] · [[Assunzione di Mondo Chiuso]] · [[Interrogazioni Annidate]]
- **Mappa**: [[MOC - Basi di Dati]]
- **Data Management (magistrale)**: [[Queries Expressing Absence]] · [[Difference in Relational Algebra]]

> [!info] Approfondimento
> - [[02 - BD - Modello Relazionale#Il problema della negazione|Lezione 2 — Il problema della negazione]]
> - [[02 - BD - Modello Relazionale#Esercizio 5|Lezione 2 — Esercizio 5]]
