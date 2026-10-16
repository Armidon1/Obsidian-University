---
title: Conflitti shift-reduce e reduce-reduce
tags:
  - modelli-di-calcolo
  - concetto
  - parsing
  - lr-parsing
---

# Conflitti shift-reduce e reduce-reduce

> [!summary] In breve
> In un parser bottom-up c'è un conflitto **reduce-reduce** se si può ridurre con due produzioni diverse, **shift-reduce** se si può sia impilare sia ridurre. Le due scelte producono alberi diversi.

- **Shift-reduce**, esempio del *dangling else*: con `if E then if E then S` in pila e `else` in input, reduce attacca l'`else` al primo `if`, shift al secondo. Si risolve con una regola esterna alla grammatica (si preferisce lo shift).
- **Reduce-reduce**: rari, di solito sintomo di grammatica ambigua (esempio: stato con $S \to bc\cdot$ e $T \to bc\cdot$).
- Nel goto-graph LR(0): uno stato con due item completi (reduce-reduce) o con un item completo e uno incompleto (shift-reduce).
- Un **lookahead** (SLR(1), LR(1)) risolve molti conflitti shift-reduce; nessun lookahead risolve l'ambiguità.

## Collegamenti

- **Concetti correlati**: [[Parsing shift-reduce]] · [[Grammatica LR(0)]] · [[Grammatica ambigua]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[12 - MC - Parsing bottom-up#Conflitti|Lezione 12 — Conflitti]]
> - [[12 - MC - Parsing bottom-up#Parsing ambiguo di abcc|Lezione 12 — Parsing ambiguo di abcc]]
> - [[12 - MC - Parsing bottom-up#Set di item e goto-graph per le E.R.|Lezione 12 — Set di item e goto-graph per le E.R.]]
