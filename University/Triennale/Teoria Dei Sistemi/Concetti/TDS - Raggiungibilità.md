---
title: TDS - Raggiungibilità
tags:
  - teoria-dei-sistemi
  - concetto
  - raggiungibilita
---

# TDS - Raggiungibilità

> [!summary] In breve
> Gli stati raggiungibili da zero con un opportuno ingresso formano $\mathcal R=\mathrm{Im}(B\ AB\ \cdots\ A^{n-1}B)$; il sistema è tutto raggiungibile se il rango è $n$.

- Discreto: dopo $k$ passi si raggiunge $\mathrm{Im}(B\ \cdots\ A^{k-1}B)$.
- Continuo: in un tempo $T$ arbitrario, con $u(t)=B'e^{-A't}G^{-1}e^{-AT}x_R$ e $G$ il gramiano.
- $\mathcal R$ è $A$-invariante e contiene $\mathrm{Im}\,B$.
- Base (base di $\mathcal R$ | completamento): $\tilde A$ triangolare a blocchi, $\tilde B=(B_1;0)$.
- È la condizione per assegnare gli autovalori con retroazione dallo stato.

## Collegamenti

- **Concetti correlati**: [[TDS - Osservabilità]] · [[TDS - Scomposizione di Kalman]] · [[TDS - Retroazione dallo stato]] · [[TDS - Eccitabilità e osservabilità dei modi]]
- **Mappa**: [[MOC - Teoria dei Sistemi]]

> [!info] Approfondimento
> - [[27 - TDS - Scomposizione rispetto all'osservabilità e raggiungibilità#Raggiungibilità di uno stato nel tempo discreto|Lezione 27 — Raggiungibilità di uno stato nel tempo discreto]]
> - [[27 - TDS - Scomposizione rispetto all'osservabilità e raggiungibilità#Partizione del sistema secondo la raggiungibilità|Lezione 27 — Partizione del sistema secondo la raggiungibilità]]
> - [[28 - TDS - Raggiungibilità nel tempo continuo e scomposizione di Kalman#Raggiungibilità nel caso continuo|Lezione 28 — Raggiungibilità nel caso continuo]]
