---
title: Parsing shift-reduce
tags:
  - modelli-di-calcolo
  - concetto
  - parsing
  - lr-parsing
---

# Parsing shift-reduce

> [!summary] In breve
> Parsing bottom-up con una pila: a ogni passo si fa **shift** (si impila il prossimo token) o **reduce** (si sostituisce l'handle $\alpha$ in cima con $X$, se $X \to \alpha$). Ripercorre al contrario una derivazione destra.

| pila | input | azione |
|---|---|---|
| | `abbbcccc$` | shift (×5) |
| `abbbc` | `ccc$` | reduce $T \to bc$ |
| `abbT` | `ccc$` | shift |
| `abbTc` | `cc$` | reduce $T \to bTc$ |
| … | | |
| `aTc` | `$` | reduce $S \to aTc$ |
| `S` | `$` | successo |

(grammatica $S \to aSc \mid aTc$, $T \to bTc \mid bc$)

- Successo: input finito e in pila solo l'assioma.
- Il problema è **riconoscere l'handle**: nascono i [[Conflitti shift-reduce e reduce-reduce|conflitti]], risolti dai parser LR.

## Collegamenti

- **Concetti correlati**: [[Conflitti shift-reduce e reduce-reduce]] · [[Tavole Action e Goto]] · [[Item LR(0)]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[12 - MC - Parsing bottom-up#Parsing shift-reduce|Lezione 12 — Parsing shift-reduce]]
> - [[12 - MC - Parsing bottom-up#Un semplice esempio|Lezione 12 — Un semplice esempio]]
> - [[12 - MC - Parsing bottom-up#Approcci al parsing|Lezione 12 — Approcci al parsing]]
