---
title: Legge Debole dei Grandi Numeri
tags:
  - probabilita-e-statistica
  - concetto
  - legge-dei-grandi-numeri
---

# Legge Debole dei Grandi Numeri

> [!summary] In breve
> La media aritmetica di $n$ v.a. i.i.d. di media $\mu$ converge in probabilità a $\mu$: $P(|\bar X_n-\mu|>\varepsilon)\to0$.

$$P\Big(\Big|\frac{X_1+\dots+X_n}n-\mu\Big|>\varepsilon\Big)\le\frac{\sigma^2}{n\varepsilon^2}\xrightarrow[n\to\infty]{}0$$

- Dimostrazione: $E[\bar X_n]=\mu$, $\mathrm{Var}(\bar X_n)=\sigma^2/n$, poi Chebyshev.
- Con $X_i$ indicatrici di $E$: la frequenza relativa di $E$ tende a $P(E)$ (interpretazione frequentista).

## Collegamenti

- **Concetti correlati**: [[Media Campionaria]] · [[Disuguaglianza di Chebyshev]] · [[Teorema del Limite Centrale]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[05 - PS - Disuguaglianze e Legge dei Grandi Numeri#Legge debole dei grandi numeri|Lezione 5 — Legge debole dei grandi numeri]]
> - [[05 - PS - Disuguaglianze e Legge dei Grandi Numeri#Interpretazione frequentista della probabilità|Lezione 5 — Interpretazione frequentista della probabilità]]
