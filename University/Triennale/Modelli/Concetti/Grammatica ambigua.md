---
title: Grammatica ambigua
tags:
  - modelli-di-calcolo
  - concetto
  - linguaggi-formali
  - parsing
---

# Grammatica ambigua

> [!summary] In breve
> Una grammatica è ambigua se una stessa stringa del linguaggio ha due alberi di derivazione diversi (equivalentemente, due derivazioni sinistre diverse).

- Non adatta ai linguaggi di programmazione: semantica non chiara, analisi più complessa.
- Nessun parser deterministico (LL o LR) può gestirla: il conflitto riflette due alberi entrambi corretti.
- Spesso si disambigua con **livelli di precedenza**:

| ambigua | non ambigua |
|---|---|
| $E \to E + E \mid E * E \mid \mathrm{id} \mid (E)$ | $E \to E + T \mid T$, $T \to T * F \mid F$, $F \to \mathrm{id} \mid (E)$ |

- *Dangling else*: $S \to \texttt{if } E \texttt{ then } S \mid \texttt{if } E \texttt{ then } S \texttt{ else } S$, risolto con la regola "else all'ultimo if aperto".
- Decidere se una CF è ambigua è **indecidibile**.

## Collegamenti

- **Concetti correlati**: [[Albero di derivazione]] · [[Conflitti shift-reduce e reduce-reduce]] · [[Grammatica LL(1)]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[11 - MC - Analisi sintattica top-down e automi a pila#Grammatiche ambigue|Lezione 11 — Grammatiche ambigue]]
> - [[11 - MC - Analisi sintattica top-down e automi a pila#Grammatiche non ambigue per espressioni aritmetiche|Lezione 11 — Grammatiche non ambigue per espressioni aritmetiche]]
> - [[12 - MC - Parsing bottom-up#Parsing ambiguo di abcc|Lezione 12 — Parsing ambiguo di abcc]]
