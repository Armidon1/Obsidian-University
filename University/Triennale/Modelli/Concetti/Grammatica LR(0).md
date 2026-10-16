---
title: Grammatica LR(0)
tags:
  - modelli-di-calcolo
  - concetto
  - parsing
  - lr-parsing
---

# Grammatica LR(0)

> [!summary] In breve
> Una grammatica è LR(0) se nessuno stato del goto-graph contiene due item completi (reduce-reduce) o un item completo insieme a uno incompleto (shift-reduce): il parser decide senza guardare l'input.

- LR(0) si applica a poche grammatiche; con $k \ge 1$ token di lookahead (LR(k)) a molte di più.
- Una grammatica ambigua non è LR(k) per nessun $k$.
- Teoremi (senza prova): $L$ ha una grammatica LR(k) **sse** è CF **deterministico**; LR(1) = LR(k) per $k \ge 1$.
- LR(1) è più potente di LL(1): include tutte le grammatiche dei linguaggi di programmazione; tool: bison.

> [!example] Domanda tipica
> *$S \to aS \mid ab \mid aSb$ è LR(0)?* Si costruisce il goto-graph e si cercano stati con conflitti.

## Collegamenti

- **Concetti correlati**: [[Item LR(0)]] · [[Conflitti shift-reduce e reduce-reduce]] · [[Grammatica LL(1)]] · [[Automa a pila]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[12 - MC - Parsing bottom-up#Grammatica LR(0)|Lezione 12 — Grammatica LR(0)]]
> - [[12 - MC - Parsing bottom-up#LR(0) contro LR(k)|Lezione 12 — LR(0) contro LR(k)]]
