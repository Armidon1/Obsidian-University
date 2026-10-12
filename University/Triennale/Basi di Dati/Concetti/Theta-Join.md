---
title: Theta-Join
tags:
  - basi-di-dati
  - concetto
  - algebra-relazionale
---

# Theta-Join

> [!summary] In breve
> Selezione applicata al prodotto cartesiano di due relazioni senza attributi comuni; se usa solo l'uguaglianza si chiama equi-join.

$$R_1 \text{ JOIN}_{cond}\, R_2 = \text{SEL}_{cond}(R_1 \text{ JOIN } R_2)$$

- Condizione: congiunzione di confronti $A_1 \,\vartheta\, A_2$ con $\vartheta \in \{=, <, >, \dots\}$.
- Join naturale ↔ equi-join: servono ridenominazioni (e una proiezione).
- Necessario per il **self-join**: si ridenominano tutti gli attributi di una copia.

## Collegamenti

- **Concetti correlati**: [[Join]] · [[Algebra Relazionale]]
- **Mappa**: [[MOC - Basi di Dati]]

> [!info] Approfondimento
> - [[02 - BD - Modello Relazionale#Theta-join ed equi-join|Lezione 2 — Theta-join ed equi-join]]
> - [[02 - BD - Modello Relazionale#Self-join|Lezione 2 — Self-join]]
> - [[03 - BD - SQL#Il self-join in SQL|Lezione 3 — Il self-join in SQL]]
