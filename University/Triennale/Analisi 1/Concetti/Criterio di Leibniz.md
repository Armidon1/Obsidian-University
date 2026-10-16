---
title: Criterio di Leibniz
tags:
  - analisi-1
  - concetto
  - serie
  - criteri-di-convergenza
---

# Criterio di Leibniz

> [!summary] In breve
> Se (aₖ) è decrescente e infinitesima, la serie a segni alterni Σ (−1)^k aₖ converge, e l'errore commesso troncandola è al più il primo termine trascurato.

$$a_k \searrow 0 \quad\Rightarrow\quad \sum_{k=0}^{+\infty} (-1)^k a_k = s \text{ converge}, \qquad |s - s_n| \le a_{n+1}.$$

- Le somme parziali pari e dispari si "inseguono" e intrappolano $s$.
- Esempio: $\sum \frac{(-1)^k}{k} = -\ln 2$ converge, ma $\sum \frac1k$ diverge: convergenza **non assoluta**.
- $\sum \frac{(-1)^k}{k^\alpha}$ converge per ogni $\alpha > 0$.
- Per le serie che convergono solo semplicemente l'ordine conta (riordinamenti, Riemann–Dini).

## Collegamenti

- **Concetti correlati**: [[Convergenza assoluta]] · [[Serie armonica]] · [[Serie numerica]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[02 - AN1 - Serie Numeriche#Criterio di Leibniz|Lezione 2 — Criterio di Leibniz]]
> - [[02 - AN1 - Serie Numeriche#Riordinamenti di una serie|Lezione 2 — Riordinamenti di una serie]]
