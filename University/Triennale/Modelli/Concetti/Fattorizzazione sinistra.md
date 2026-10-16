---
title: Fattorizzazione sinistra
tags:
  - modelli-di-calcolo
  - concetto
  - parsing
  - ll-parsing
---

# Fattorizzazione sinistra

> [!summary] In breve
> Due produzioni con un prefisso comune $A \to \alpha\beta \mid \alpha\gamma$ si riscrivono $A \to \alpha A'$, $A' \to \beta \mid \gamma$: la scelta si rimanda a dopo aver letto il prefisso.

> [!example] Istruzione if
> `ifStmt ::= if ( expr ) stmt | if ( expr ) stmt else stmt`
> diventa
> `ifStmt ::= if ( expr ) stmt ifTail`, `ifTail ::= else stmt | ε`

La grammatica fattorizzata resta **ambigua** (*dangling else*): $\mathrm{else} \in \mathrm{SELECT}(ifTail \to else\ stmt) \cap \mathrm{FOLLOW}(ifTail)$. Si risolve nel codice associando l'`else` all'ultimo `if` aperto.

## Collegamenti

- **Concetti correlati**: [[Eliminazione della ricorsione sinistra]] · [[Grammatica LL(1)]] · [[Grammatica ambigua]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[11 - MC - Analisi sintattica top-down e automi a pila#Prefissi comuni e fattorizzazione|Lezione 11 — Prefissi comuni e fattorizzazione]]
> - [[11 - MC - Analisi sintattica top-down e automi a pila#Possibili problemi|Lezione 11 — Possibili problemi]]
