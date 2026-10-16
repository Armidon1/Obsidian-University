---
title: Eliminazione della ricorsione sinistra
tags:
  - modelli-di-calcolo
  - concetto
  - parsing
  - ll-parsing
---

# Eliminazione della ricorsione sinistra

> [!summary] In breve
> Le produzioni $A \to A\alpha \mid \beta$ (che generano $\beta\alpha^*$) si sostituiscono con $A \to \beta A'$, $A' \to \alpha A' \mid \varepsilon$: stesso linguaggio, niente ricorsione sinistra, adatte al parsing top-down.

Caso generale:
$$A \to A\alpha_1 \mid \dots \mid A\alpha_r \mid \beta_1 \mid \dots \mid \beta_s$$
diventa
$$A \to \beta_1 A' \mid \dots \mid \beta_s A' \qquad A' \to \alpha_1 A' \mid \dots \mid \alpha_r A' \mid \varepsilon$$

- Perché serve: `expr() { expr(); ... }` richiama se stesso senza consumare input (ricorsione infinita).
- Sostituire con una ricorsione **destra** ($E \to T + E \mid T$) non basta: crea un prefisso comune.
- In EBNF: $E \to T\{+T\}^*$, tradotto con un ciclo `while` (che mantiene l'associatività a sinistra).

## Collegamenti

- **Concetti correlati**: [[Grammatica LL(1)]] · [[Fattorizzazione sinistra]] · [[Parser a discesa ricorsiva]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[11 - MC - Analisi sintattica top-down e automi a pila#Ricorsione sinistra|Lezione 11 — Ricorsione sinistra]]
> - [[11 - MC - Analisi sintattica top-down e automi a pila#Codice per le espressioni|Lezione 11 — Codice per le espressioni]]
