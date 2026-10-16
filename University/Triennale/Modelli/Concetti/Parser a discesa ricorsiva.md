---
title: Parser a discesa ricorsiva
tags:
  - modelli-di-calcolo
  - concetto
  - parsing
  - ll-parsing
---

# Parser a discesa ricorsiva

> [!summary] In breve
> Parser top-down con una funzione per ogni non terminale, che consuma i terminali della parte destra e chiama le funzioni dei non terminali. Con backtracking è esponenziale; se la grammatica è LL(1) diventa predittivo e lineare.

```c
// expr ::= term { + term }*
void expr() {
   term();
   while (next symbol is PLUS) { getNextToken(); term(); }
}
```

- Le ricorsioni sinistre ($E \to E + T$) causano ricorsione infinita: vanno eliminate.
- **Predittivo**: sceglie la produzione guardando il prossimo token ($\mathrm{SELECT}$); la funzione di un non terminale è uno `switch` sui token.
- Il caso `if-else` si risolve nel codice: "else all'ultimo if aperto".

## Collegamenti

- **Concetti correlati**: [[Grammatica LL(1)]] · [[Insiemi FIRST e FOLLOW]] · [[Eliminazione della ricorsione sinistra]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[11 - MC - Analisi sintattica top-down e automi a pila#Parser a discesa ricorsiva|Lezione 11 — Parser a discesa ricorsiva]]
> - [[11 - MC - Analisi sintattica top-down e automi a pila#Parser predittivi|Lezione 11 — Parser predittivi]]
> - [[11 - MC - Analisi sintattica top-down e automi a pila#Codice per le espressioni|Lezione 11 — Codice per le espressioni]]
