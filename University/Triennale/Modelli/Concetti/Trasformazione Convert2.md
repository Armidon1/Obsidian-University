---
title: Trasformazione Convert2
tags:
  - modelli-di-calcolo
  - concetto
  - logica
  - sat
  - cnf
---

# Trasformazione Convert2

> [!summary] In breve
> Trasforma una formula in CNF introducendo una lettera nuova $A_\gamma$ per ogni sottoformula $\gamma$: il risultato non è equivalente ma **equisoddisfacibile**, e ha dimensione **lineare**. È (una variante della) trasformazione di Tseitin.

| sottoformula | clausole aggiunte |
|---|---|
| $\gamma = \alpha \wedge \beta$ | $\neg A_\gamma \vee A_\alpha$, $\neg A_\gamma \vee A_\beta$ |
| $\gamma = \alpha \vee \beta$ | $\neg A_\gamma \vee A_\alpha \vee A_\beta$ |
| la formula $F$ | $A_F$ |

- $\neg A_\gamma \vee A_\alpha$ si legge "$A_\gamma \to A_\alpha$".
- $\alpha$ soddisfacibile $\iff$ $\mathit{Convert2}(\alpha)$ soddisfacibile: basta per le riduzioni a SAT.

## Collegamenti

- **Concetti correlati**: [[Forma normale congiuntiva]] · [[Problema SAT]] · [[Riduzione polinomiale]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[13 - MC - Forme normali e algoritmo DPLL#Trasformazione in clausole: Convert2|Lezione 13 — Trasformazione in clausole: Convert2]]
> - [[13 - MC - Forme normali e algoritmo DPLL#Proprietà delle due trasformazioni|Lezione 13 — Proprietà delle due trasformazioni]]
