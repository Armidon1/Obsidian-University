---
title: TDS - Trasformata Zeta
tags:
  - teoria-dei-sistemi
  - concetto
  - trasformata-zeta
  - tempo-discreto
---

# TDS - Trasformata Zeta

> [!summary] In breve
> $F(z)=\sum_{t\ge0}f(t)z^{-t}$: l\'analogo discreto di Laplace; $z$ anticipa e $z^{-1}$ ritarda di un passo.

| $f(t)$ | $F(z)$ |
|---|---|
| $\delta(t)$ | $1$ |
| $\delta_{-1}(t)$ | $z/(z-1)$ |
| $a^t$ | $z/(z-a)$ |
| $\sin\theta t$ | $z\sin\theta/(z^2-2z\cos\theta+1)$ |

- $\mathcal Z[f(t+1)]=zF(z)-zf(0)$, $\mathcal Z[f(t-1)]=z^{-1}F(z)$, $\mathcal Z[a^tf(t)]=F(z/a)$.
- $\Phi(z)=z(zI-A)^{-1}$, $H(z)=(zI-A)^{-1}B$, $W(z)=C(zI-A)^{-1}B+D$.

## Collegamenti

- **Concetti correlati**: [[TDS - Trasformata di Laplace]] · [[TDS - Antitrasformata e residui]] · [[TDS - Sistemi a tempo discreto]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[18 - TDS - Trasformata Zeta#Trasformata nel tempo discreto|Lezione 18 — Trasformata nel tempo discreto]]
> - [[19 - TDS - Antitrasformata Zeta#Trasformate Z di funzioni comuni|Lezione 19 — Trasformate Z di funzioni comuni]]
> - [[20 - TDS - Risposta forzata nel tempo discreto#Intuizione e funzioni|Lezione 20 — Intuizione e funzioni]]
