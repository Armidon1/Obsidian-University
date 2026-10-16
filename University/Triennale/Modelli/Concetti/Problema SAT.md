---
title: Problema SAT
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - np-completezza
  - sat
---

# Problema SAT

> [!summary] In breve
> Data una formula proposizionale (di solito in CNF), decidere se esiste un'assegnazione che la rende vera. È il primo problema dimostrato NP-completo.

- Forza bruta: $2^n$ assegnazioni × verifica polinomiale = esponenziale.
- In NP: il certificato è l'assegnazione.
- NP-completo (Cook-Levin); anche **3SAT** lo è (clausole di 3 letterali), mentre **2SAT** è in P.
- Riduzione SAT → 3SAT: clausole di 1 o 2 letterali completate con variabili nuove; clausole lunghe spezzate con una catena $\{l_0, l_1, y_0\}, \{\neg y_0, l_2, y_1\}, \dots$
- In pratica: [[Algoritmo DPLL|DPLL]] e i SAT solver.

## Collegamenti

- **Concetti correlati**: [[Teorema di Cook-Levin]] · [[Algoritmo DPLL]] · [[Forma normale congiuntiva]] · [[NP-completezza]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[14 - MC - Classi P e NP e NP-completezza#SAT|Lezione 14 — SAT]]
> - [[14 - MC - Classi P e NP e NP-completezza#Riduzione polinomiale da SAT a 3SAT|Lezione 14 — Riduzione polinomiale da SAT a 3SAT]]
> - [[13 - MC - Forme normali e algoritmo DPLL#Algoritmo DPLL|Lezione 13 — Algoritmo DPLL]]
