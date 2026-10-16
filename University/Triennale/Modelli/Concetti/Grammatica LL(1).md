---
title: Grammatica LL(1)
tags:
  - modelli-di-calcolo
  - concetto
  - parsing
  - ll-parsing
---

# Grammatica LL(1)

> [!summary] In breve
> Una grammatica CF è LL(1) se per ogni coppia di produzioni sullo stesso non terminale $A \to \alpha$ e $A \to \beta$ vale $\mathrm{SELECT}(A \to \alpha) \cap \mathrm{SELECT}(A \to \beta) = \emptyset$: basta un token di lookahead per scegliere la produzione.

- **L**eft-to-right, **L**eftmost derivation, **1** token di lookahead.
- Tabella di parsing $|V_N| \times |V_T|$: in $(A, t)$ la produzione con $t \in \mathrm{SELECT}$; caselle vuote = errori.
- Non sono LL(1): grammatiche ambigue, con **ricorsione sinistra**, con **prefissi comuni**.
- I linguaggi LL(1) sono un sottoinsieme proprio dei CF deterministici (LR(1) è più potente).

| non LL(1) | LL(1) equivalente |
|---|---|
| $E \to E + T \mid T$ | $E \to TE'$, $E' \to +TE' \mid \varepsilon$ |
| $S \to Ac \mid Bd$, $A \to a$, $B \to a$ | $S \to aX$, $X \to c \mid d$ |

## Collegamenti

- **Concetti correlati**: [[Insiemi FIRST e FOLLOW]] · [[Eliminazione della ricorsione sinistra]] · [[Fattorizzazione sinistra]] · [[Grammatica LR(0)]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[11 - MC - Analisi sintattica top-down e automi a pila#Grammatiche LL(1)|Lezione 11 — Grammatiche LL(1)]]
> - [[11 - MC - Analisi sintattica top-down e automi a pila#Definizione di grammatica CF LL(1)|Lezione 11 — Definizione di grammatica CF LL(1)]]
> - [[11 - MC - Analisi sintattica top-down e automi a pila#LL contro LR|Lezione 11 — LL contro LR]]
