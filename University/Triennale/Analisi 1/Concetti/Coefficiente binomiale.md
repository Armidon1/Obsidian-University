---
title: Coefficiente binomiale
tags:
  - analisi-1
  - concetto
  - combinatoria
---

# Coefficiente binomiale

> [!summary] In breve
> n su k = n!/(k!(n−k)!) è il numero di sottoinsiemi di k elementi di un insieme di n elementi; si calcola con il triangolo di Tartaglia.

$$\binom nk = \frac{n!}{k!(n-k)!} = \frac{n(n-1)\cdots(n-k+1)}{k!}$$

- $\binom n0 = \binom nn = 1$, $\binom nk = \binom n{n-k}$.
- **Regola di Tartaglia**: $\binom nk = \binom{n-1}{k-1} + \binom{n-1}{k}$.
- Esempio: $\binom{90}{6} = 622.614.630$ (sestine del SuperEnalotto).
- **Generalizzato** ($\alpha \in \mathbb{R}$): $\binom\alpha k = \frac{\alpha(\alpha-1)\cdots(\alpha-k+1)}{k!}$, usato nello sviluppo di $(1+x)^\alpha$.

## Collegamenti

- **Concetti correlati**: [[Binomio di Newton]] · [[Formula di Taylor]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[00 - AN1 - Concetti Fondamentali#Fattoriale e Coefficienti Binomiali|Lezione 0 — Fattoriale e Coefficienti Binomiali]]
> - [[00 - AN1 - Concetti Fondamentali#Proprietà e triangolo di Tartaglia|Lezione 0 — Proprietà e triangolo di Tartaglia]]
> - [[05 - AN1 - Calcolo Differenziale#Sviluppi di Taylor notevoli|Lezione 5 — Sviluppi di Taylor notevoli]]
