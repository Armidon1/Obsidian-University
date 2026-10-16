---
title: Criterio del confronto per le serie
tags:
  - analisi-1
  - concetto
  - serie
  - criteri-di-convergenza
---

# Criterio del confronto per le serie

> [!summary] In breve
> Per serie a termini positivi: un maggiorante convergente fa convergere, un minorante divergente fa divergere; con il confronto asintotico basta aₖ/bₖ → l ≠ 0.

Se $0 \le a_k \le b_k$ definitivamente:
$$\sum b_k \text{ converge} \Rightarrow \sum a_k \text{ converge}, \qquad \sum a_k \text{ diverge} \Rightarrow \sum b_k \text{ diverge}.$$

**Confronto asintotico**: se $\frac{a_k}{b_k} \to l \in (0, +\infty)$, le due serie hanno lo stesso carattere (in particolare se $a_k \sim b_k$).

Esempi:
- $\frac{1}{\sqrt k} \ge \frac1k$ $\Rightarrow$ $\sum \frac1{\sqrt k}$ diverge;
- $\frac{1}{k^2} \sim \frac{1}{k(k+1)}$ (Mengoli) $\Rightarrow$ $\sum \frac1{k^2}$ converge;
- $\frac{1}{k!} \le 2\left(\frac12\right)^k$ $\Rightarrow$ la serie esponenziale converge.

Lo stesso criterio vale per gli [[Integrale improprio|integrali impropri]].

## Collegamenti

- **Concetti correlati**: [[Serie numerica]] · [[Successioni asintotiche]] · [[Criterio del rapporto e della radice]] · [[Integrale improprio]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[02 - AN1 - Serie Numeriche#Criterio del confronto|Lezione 2 — Criterio del confronto]]
> - [[02 - AN1 - Serie Numeriche#Serie esponenziale|Lezione 2 — Serie esponenziale]]
