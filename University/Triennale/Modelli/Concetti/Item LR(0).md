---
title: Item LR(0)
tags:
  - modelli-di-calcolo
  - concetto
  - parsing
  - lr-parsing
---

# Item LR(0)

> [!summary] In breve
> Un item LR(0) è una produzione con un punto nella parte destra, $A \to \alpha \cdot \beta$: $\alpha$ è già stato letto (in pila), $\beta$ resta da leggere. Gli stati di un parser LR sono insiemi **chiusi** di item.

- Da $E \to E + T$: $E \to \cdot E+T$, $E \to E\cdot+T$, $E \to E+\cdot T$, $E \to E+T\cdot$.
- **Grammatica aumentata**: nuovo assioma $S' \to S$, per la reduce finale.
- **Chiusura**: se c'è $A \to \alpha \cdot B\beta$, si aggiungono tutti i $B \to \cdot\gamma$, finché possibile.
- **Transizioni**: da uno stato, per ogni simbolo $X$ dopo il punto, si va nella chiusura di $\{A \to \alpha X \cdot \beta\}$ (il simbolo "scavalcato").
- Stati e transizioni formano il **goto-graph**, che è un ASF.

## Collegamenti

- **Concetti correlati**: [[Tavole Action e Goto]] · [[Grammatica LR(0)]] · [[Automa a stati finiti]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[12 - MC - Parsing bottom-up#Notazione punto e item LR(0)|Lezione 12 — Notazione punto e item LR(0)]]
> - [[12 - MC - Parsing bottom-up#Chiusura di un set di item|Lezione 12 — Chiusura di un set di item]]
> - [[12 - MC - Parsing bottom-up#Ripresa dell'esempio: set di item e goto-graph|Lezione 12 — Ripresa dell'esempio: set di item e goto-graph]]
