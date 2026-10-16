---
title: Serie numerica
tags:
  - analisi-1
  - concetto
  - serie
---

# Serie numerica

> [!summary] In breve
> Una somma infinita Σ aₖ, definita come limite della successione delle somme parziali sₙ = a₀ + … + aₙ; può convergere, divergere o essere irregolare.

$$\sum_{k=0}^{+\infty} a_k := \lim_{n\to+\infty} s_n, \qquad s_n = \sum_{k=0}^n a_k$$

- **Condizione necessaria**: se la serie converge allora $a_k \to 0$ (non sufficiente: la [[Serie armonica]] diverge).
- Serie a **termini positivi**: $s_n$ crescente $\Rightarrow$ converge $\iff$ $s_n$ limitata (mai irregolare).
- Serie modello:

| Serie | Carattere |
|---|---|
| $\sum q^k$ | converge a $\frac{1}{1-q}$ per $\lvert q\rvert < 1$ |
| $\sum \frac1{k^\alpha}$ | converge $\iff$ $\alpha > 1$ |
| $\sum \frac{1}{k(k+1)}$ (Mengoli) | $= 1$ (telescopica) |
| $\sum \frac{a^k}{k!}$ | $= e^a$ |

## Collegamenti

- **Concetti correlati**: [[Serie geometrica]] · [[Serie armonica]] · [[Criterio del confronto per le serie]] · [[Convergenza assoluta]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[02 - AN1 - Serie Numeriche#Il problema delle somme infinite|Lezione 2 — Il problema delle somme infinite]]
> - [[02 - AN1 - Serie Numeriche#Condizione necessaria|Lezione 2 — Condizione necessaria]]
> - [[02 - AN1 - Serie Numeriche#Serie a Termini Positivi|Lezione 2 — Serie a Termini Positivi]]
