---
title: Tavole Action e Goto
tags:
  - modelli-di-calcolo
  - concetto
  - parsing
  - lr-parsing
---

# Tavole Action e Goto

> [!summary] In breve
> Le due tabelle che pilotano un parser LR: **Action[s, a]** dice cosa fare con lo stato $s$ in cima e il token $a$ (shift, reduce, accept, error); **Goto[s, X]** dice quale stato impilare dopo aver ridotto al non terminale $X$.

Driver LR (uguale per ogni grammatica):
- shift($s_u$): push($s_u$), leggi il prossimo token;
- reduce($A \to B_1 \dots B_k$): $k$ pop, poi push(Goto[$s_v$, $A$]) con $s_v$ lo stato affiorato; il token non cambia; si emette la produzione;
- accept / error.

Costruzione dal goto-graph: transizioni su terminali → shift; su non terminali → goto; item completi → reduce (in LR(0) su tutte le colonne).

## Collegamenti

- **Concetti correlati**: [[Item LR(0)]] · [[Parsing shift-reduce]] · [[Grammatica LR(0)]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[12 - MC - Parsing bottom-up#Tavole Action e Goto|Lezione 12 — Tavole Action e Goto]]
> - [[12 - MC - Parsing bottom-up#Operazioni di un LR parser|Lezione 12 — Operazioni di un LR parser]]
> - [[12 - MC - Parsing bottom-up#LR parsing in azione|Lezione 12 — LR parsing in azione]]
