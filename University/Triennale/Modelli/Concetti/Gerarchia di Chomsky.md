---
title: Gerarchia di Chomsky
tags:
  - modelli-di-calcolo
  - concetto
  - linguaggi-formali
  - grammatiche
---

# Gerarchia di Chomsky

> [!summary] In breve
> Classifica le grammatiche in quattro tipi annidati in base alla forma delle produzioni; a ogni tipo corrisponde un modello di calcolo che riconosce i suoi linguaggi.

| tipo | produzioni | linguaggi | modello |
|---|---|---|---|
| 0 | $\alpha \to \beta$ qualunque | semidecidibili | macchina di Turing |
| 1 | $\lvert\alpha\rvert \le \lvert\beta\rvert$ (context sensitive) | contestuali, decidibili | MT lineare |
| 2 | $A \to \beta$ (context free) | liberi dal contesto | automa a pila non deterministico |
| 3 | $A \to aB \mid a$ | regolari | automa a stati finiti |

- Il tipo di un **linguaggio** è il più alto fra quelli delle grammatiche che lo generano.
- Gerarchia **rilassata**: $\varepsilon$-produzioni ammesse nei tipi 2 e 3, non nel tipo 1.
- Esempi: $a^n b^n$ tipo 2 (non 3); $a^n b^n c^n$ tipo 1 (non 2).

## Collegamenti

- **Concetti correlati**: [[Grammatica generativa]] · [[Automa a stati finiti]] · [[Automa a pila]] · [[Macchina di Turing]] · [[Linguaggio semidecidibile]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[09 - MC - Grammatiche e gerarchia di Chomsky#Gerarchia di Chomsky|Lezione 9 — Gerarchia di Chomsky]]
> - [[09 - MC - Grammatiche e gerarchia di Chomsky#Che cosa vuol dire context sensitive|Lezione 9 — Che cosa vuol dire context sensitive]]
> - [[08 - MC - Macchine di Turing e calcolabilità#Linguaggi di tipo 0 e MT|Lezione 8 — Linguaggi di tipo 0 e MT]]
