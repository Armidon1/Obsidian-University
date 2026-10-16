---
title: Grammatica generativa
tags:
  - modelli-di-calcolo
  - concetto
  - linguaggi-formali
  - grammatiche
---

# Grammatica generativa

> [!summary] In breve
> Una grammatica $G = \langle V_T, V_N, P, S \rangle$ genera un linguaggio riscrivendo, a partire dall'assioma $S$, parti delle forme di frase con le produzioni $\alpha \to \beta$: $L(G) = \{x \in V_T^* \mid S \Rightarrow^* x\}$.

- **Derivazione diretta**: $\alpha_1 \alpha_2 \alpha_3 \Rightarrow \alpha_1 \gamma \alpha_3$ se $\alpha_2 \to \gamma \in P$; $\Rightarrow^*$ è la chiusura riflessiva e transitiva.
- **Forma di frase**: derivabile da $S$, con terminali e non terminali; **frase**: solo terminali.
- **Equivalenti**: $L(G_1) = L(G_2)$. **Infeconde**: produzioni che non portano a frasi.
- Derivazione **leftmost** / **rightmost**: si riscrive sempre il non terminale più a sinistra / più a destra.

> [!example] Esempio
> $S \to aSb \mid ab$ genera $\{a^n b^n \mid n \ge 1\}$: $S \Rightarrow aSb \Rightarrow aaSbb \Rightarrow aaabbb$.

## Collegamenti

- **Concetti correlati**: [[Gerarchia di Chomsky]] · [[Albero di derivazione]] · [[Espressione regolare]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[09 - MC - Grammatiche e gerarchia di Chomsky#Descrizione generativa: le grammatiche|Lezione 9 — Descrizione generativa: le grammatiche]]
> - [[09 - MC - Grammatiche e gerarchia di Chomsky#Derivazione|Lezione 9 — Derivazione]]
> - [[09 - MC - Grammatiche e gerarchia di Chomsky#Derivazioni sinistre e destre|Lezione 9 — Derivazioni sinistre e destre]]
