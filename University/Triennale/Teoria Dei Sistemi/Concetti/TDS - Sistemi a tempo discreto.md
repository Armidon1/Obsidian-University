---
title: TDS - Sistemi a tempo discreto
tags:
  - teoria-dei-sistemi
  - concetto
  - tempo-discreto
---

# TDS - Sistemi a tempo discreto

> [!summary] In breve
> $x(t+1)=Ax(t)+Bu(t)$: forma esplicita con somme, $\Phi(t)=A^t$, modi $\lambda^t$; stabilità con il modulo degli autovalori.

- $x(t)=A^tx_0+\sum_{\tau=0}^{t-1}A^{t-1-\tau}Bu(\tau)$, $H(t)=A^{t-1}B$.
- $\lambda>1$ diverge, $0<\lambda<1$ converge, $-1<\lambda<0$ converge alternando, $\lambda<-1$ diverge alternando.
- Coppie complesse in forma polare $\rho e^{\pm j\theta}$; frequenza massima (aliasing).
- Eccitabilità/osservabilità: stesse condizioni $v_i'B$, $Cu_i$.

## Collegamenti

- **Concetti correlati**: [[TDS - Campionamento]] · [[TDS - Trasformata Zeta]] · [[TDS - Criterio di Jury]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[09 - TDS - Esempio massa-molla e sistemi a tempo discreto#Sistemi a tempo discreto|Lezione 9 — Sistemi a tempo discreto]]
> - [[09 - TDS - Esempio massa-molla e sistemi a tempo discreto#Calcolo di $A^t$ e modi naturali|Lezione 9 — Calcolo di $A^t$ e modi naturali]]
> - [[13 - TDS - Criterio di Lyapunov e stabilità nel tempo discreto#Stabilità dei sistemi lineari a tempo discreto|Lezione 13 — Stabilità dei sistemi lineari a tempo discreto]]
