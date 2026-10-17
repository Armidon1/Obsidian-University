---
title: TDS - Trasformata di Laplace
tags:
  - teoria-dei-sistemi
  - concetto
  - trasformata-di-laplace
---

# TDS - Trasformata di Laplace

> [!summary] In breve
> $F(s)=\int_0^\infty f(t)e^{-st}dt$: trasforma le equazioni differenziali in algebriche e la convoluzione in prodotto.

| $f(t)$ | $F(s)$ |
|---|---|
| $\delta(t)$ | $1$ |
| $\delta_{-1}(t)$ | $1/s$ |
| $t^k/k!$ | $1/s^{k+1}$ |
| $e^{at}$ | $1/(s-a)$ |
| $\sin\omega t$ | $\omega/(s^2+\omega^2)$ |
| $\cos\omega t$ | $s/(s^2+\omega^2)$ |

- Derivata: $\mathcal L[\dot x]=sX-x(0)$. Traslazione complessa: $\mathcal L[e^{at}f]=F(s-a)$. Ritardo: $\mathcal L[f(t-T)\delta_{-1}(t-T)]=e^{-sT}F(s)$.
- Sistema: $X=(sI-A)^{-1}x_0+(sI-A)^{-1}BU$.

## Collegamenti

- **Concetti correlati**: [[TDS - Antitrasformata e residui]] · [[TDS - Funzione di trasferimento]] · [[TDS - Trasformata Zeta]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[15 - TDS - Trasformata di Laplace#Ingressi non impulsivi e trasformata di Laplace|Lezione 15 — Ingressi non impulsivi e trasformata di Laplace]]
> - [[15 - TDS - Trasformata di Laplace#Trasformate di alcune funzioni|Lezione 15 — Trasformate di alcune funzioni]]
> - [[15 - TDS - Trasformata di Laplace#Traslazione nel dominio complesso|Lezione 15 — Traslazione nel dominio complesso]]
