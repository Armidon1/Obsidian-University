---
title: Limite di successione
tags:
  - analisi-1
  - concetto
  - successioni
  - limiti
---

# Limite di successione

> [!summary] In breve
> aₙ → l se per ogni ε > 0 da un certo indice in poi |aₙ − l| < ε; aₙ → +∞ se supera definitivamente ogni soglia M. Una successione è convergente, divergente o irregolare.

$$\lim_{n\to+\infty} a_n = l \iff \forall \varepsilon > 0\ \exists n_0 : |a_n - l| < \varepsilon\ \ \forall n \ge n_0$$
$$\lim_{n\to+\infty} a_n = +\infty \iff \forall M > 0\ \exists n_0 : a_n > M\ \ \forall n \ge n_0$$

| Tipo | Esempio |
|---|---|
| convergente (infinitesima se $l = 0$) | $\frac1n \to 0$ |
| divergente | $n \to +\infty$ |
| irregolare | $(-1)^n$ |

- Il limite è **unico**; una successione convergente è **limitata** (non viceversa).
- **Permanenza del segno**: $a_n \ge 0$ definitivamente $\Rightarrow$ $l \ge 0$ (le disuguaglianze strette diventano larghe).

## Collegamenti

- **Concetti correlati**: [[Successione]] · [[Forme indeterminate]] · [[Teorema dei carabinieri]] · [[Limite di funzione]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[01 - AN1 - Successioni Numeriche#Successioni convergenti|Lezione 1 — Successioni convergenti]]
> - [[01 - AN1 - Successioni Numeriche#Successioni divergenti|Lezione 1 — Successioni divergenti]]
> - [[01 - AN1 - Successioni Numeriche#Definitivamente e permanenza del segno|Lezione 1 — Definitivamente e permanenza del segno]]
