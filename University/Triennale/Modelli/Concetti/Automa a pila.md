---
title: Automa a pila
tags:
  - modelli-di-calcolo
  - concetto
  - linguaggi-formali
  - automi
  - parsing
---

# Automa a pila

> [!summary] In breve
> Automa a stati finiti con una pila illimitata (MT a due nastri: input in sola lettura one-way + pila). Nella versione non deterministica riconosce esattamente i linguaggi di tipo 2 (liberi dal contesto).

- Transizioni $(x, y, z)$: legge $x$ dall'input, $y$ dalla cima della pila e la sostituisce con $z$.
- $a^n b^n$: si impilano le $a$ e se ne toglie una per ogni $b$.
- **Grammatica → automa**: si impila l'assioma; un non terminale in cima viene sostituito (non deterministicamente) da una parte destra; un terminale in cima si confronta con l'input. È un parser top-down.
- Il **non determinismo serve**: i palindromi $ww^R$ non sono riconoscibili da un automa a pila deterministico.

| | linguaggi |
|---|---|
| automi a pila deterministici | CF deterministici = LR(1) |
| automi a pila non deterministici | CF (tipo 2) |

## Collegamenti

- **Concetti correlati**: [[Gerarchia di Chomsky]] · [[Grammatica LL(1)]] · [[Grammatica LR(0)]] · [[Automa a stati finiti]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[11 - MC - Analisi sintattica top-down e automi a pila#Automi pushdown|Lezione 11 — Automi pushdown]]
> - [[09 - MC - Grammatiche e gerarchia di Chomsky#Forme normali|Lezione 9 — Forme normali]]
> - [[12 - MC - Parsing bottom-up#LR(0) contro LR(k)|Lezione 12 — LR(0) contro LR(k)]]
