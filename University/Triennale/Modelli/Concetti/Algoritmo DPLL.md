---
title: Algoritmo DPLL
tags:
  - modelli-di-calcolo
  - concetto
  - logica
  - sat
---

# Algoritmo DPLL

> [!summary] In breve
> Algoritmo di backtracking per la soddisfacibilità di un insieme di clausole, con due semplificazioni: **unit propagation** (una clausola unitaria fissa il valore del suo letterale) e **pure literal elimination** (un letterale che compare con un solo segno si rende vero).

```text
function DPLL(F)
   if F is empty then return true;
   if F contains an empty clause then return false;
   for every unit clause l in F: F = unit-propagate(l, F);
   for every literal l pure in F: F = pure-literal-assign(l, F);
   l := choose-literal(F);
   return DPLL(F ∪ {l}) OR DPLL(F ∪ {¬l});
```

- unit-propagate($l$): cancella le clausole con $l$, toglie $\neg l$ dalle altre.
- Caso peggiore $O(2^n)$: SAT è NP-completo.

## Collegamenti

- **Concetti correlati**: [[Problema SAT]] · [[Forma normale congiuntiva]] · [[NP-completezza]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[13 - MC - Forme normali e algoritmo DPLL#Algoritmo DPLL|Lezione 13 — Algoritmo DPLL]]
> - [[13 - MC - Forme normali e algoritmo DPLL#Esempio (dalla prova di luglio 2021)|Lezione 13 — Esempio (dalla prova di luglio 2021)]]
