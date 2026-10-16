---
title: Criterio del rapporto e della radice
tags:
  - analisi-1
  - concetto
  - serie
  - criteri-di-convergenza
---

# Criterio del rapporto e della radice

> [!summary] In breve
> Se lim aₖ₊₁/aₖ = q oppure lim ᵏ√aₖ = q (aₖ > 0): la serie converge per q < 1, diverge per q > 1; per q = 1 non si conclude nulla.

$$q = \lim_{k\to+\infty} \frac{a_{k+1}}{a_k} \quad \text{oppure} \quad q = \lim_{k\to+\infty} \sqrt[k]{a_k}: \qquad \begin{cases} q < 1 & \text{converge} \\ q > 1 & \text{diverge} \\ q = 1 & ? \end{cases}$$

- Confrontano la serie con una [[Serie geometrica]] di ragione $q$.
- **Rapporto** quando ci sono fattoriali; **radice** quando ci sono potenze $k$-esime.
- Danno sempre $q = 1$ per $\sum \frac{1}{k^\alpha}$: lì serve il confronto.
- Con $|a_k|$ dimostrano la [[Convergenza assoluta]] (es. $\sum \frac{a^k}{k!}$ converge per ogni $a \in \mathbb{R}$).
- Se esiste $\lim \frac{a_{n+1}}{a_n} = q$, allora $\sqrt[n]{a_n} \to q$ (es. $\sqrt[n]{n} \to 1$, $\frac{\sqrt[n]{n!}}{n} \to \frac1e$).

## Collegamenti

- **Concetti correlati**: [[Serie geometrica]] · [[Criterio del confronto per le serie]] · [[Convergenza assoluta]] · [[Serie di Taylor]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[02 - AN1 - Serie Numeriche#Criteri della radice e del rapporto|Lezione 2 — Criteri della radice e del rapporto]]
> - [[01 - AN1 - Successioni Numeriche#Criterio del rapporto per le radici n-esime|Lezione 1 — Criterio del rapporto per le radici n-esime]]
> - [[02 - AN1 - Serie Numeriche#Convergenza assoluta|Lezione 2 — Convergenza assoluta]]
