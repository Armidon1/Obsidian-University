---
title: Join
tags:
  - basi-di-dati
  - concetto
  - algebra-relazionale
  - sql
---

# Join

> [!summary] In breve
> Operatore che correla dati di relazioni diverse: il join naturale combina le tuple che coincidono sugli attributi comuni.

$$R_1 \text{ JOIN } R_2 = \{ t \text{ su } X_1X_2 \mid t[X_1] \in R_1, t[X_2] \in R_2 \}$$

- $0 \le |R_1 \text{ JOIN } R_2| \le |R_1| \times |R_2|$.
- Senza attributi comuni → **prodotto cartesiano**.
- **Join completo**: ogni tupla contribuisce.
- **Self-join**: la stessa relazione due volte, con ridenominazione/alias.
- SQL: tabelle nella `from` + condizione, oppure `join ... on`, `natural join`, `cross join`.

## Collegamenti

- **Concetti correlati**: [[Theta-Join]] · [[Join Esterno]] · [[Algebra Relazionale]] · [[Select SQL]]
- **Mappa**: [[MOC - Basi di Dati]]
- **Data Management (magistrale)**: [[Natural Join]] · [[Nested-Loop Join]] · [[Sort-Merge Join]] · [[Hash Join]]

> [!info] Approfondimento
> - [[02 - BD - Modello Relazionale#Join naturale|Lezione 2 — Join naturale]]
> - [[02 - BD - Modello Relazionale#Join completi, non completi, vuoti|Lezione 2 — Join completi, non completi, vuoti]]
> - [[02 - BD - Modello Relazionale#Self-join|Lezione 2 — Self-join]]
> - [[03 - BD - SQL#Join esplicito|Lezione 3 — Join esplicito]]
