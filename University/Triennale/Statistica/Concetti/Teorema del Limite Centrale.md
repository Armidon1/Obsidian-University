---
title: Teorema del Limite Centrale
tags:
  - probabilita-e-statistica
  - concetto
  - normale
  - teorema-del-limite-centrale
---

# Teorema del Limite Centrale

> [!summary] In breve
> La somma di $n$ v.a. i.i.d. con media $\mu$ e varianza $\sigma^2$ è, per $n$ grande, approssimativamente $N(n\mu,n\sigma^2)$.

$$\frac{X_1+\dots+X_n-n\mu}{\sigma\sqrt n}\;\dot\sim\;N(0,1)\qquad P\Big(\frac{S_n-n\mu}{\sigma\sqrt n}<x\Big)\approx\Phi(x)$$

- Vale qualunque sia la distribuzione delle $X_i$ (con varianza finita).
- Media e varianza della somma sono esatte; il TLC aggiunge la **forma**.
- Ricetta: somma → $n\mu$, $\sigma\sqrt n$ → standardizzo → tavola.

## Collegamenti

- **Concetti correlati**: [[Normale Standard]] · [[Approssimazione Normale]] · [[Legge Debole dei Grandi Numeri]] · [[Media Campionaria]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[09 - PS - Distribuzione Normale e Teorema del Limite Centrale#Teorema del limite centrale|Lezione 9 — Teorema del limite centrale]]
