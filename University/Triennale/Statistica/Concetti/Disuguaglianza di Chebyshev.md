---
title: Disuguaglianza di Chebyshev
tags:
  - probabilita-e-statistica
  - concetto
  - disuguaglianze
---

# Disuguaglianza di Chebyshev

> [!summary] In breve
> Per ogni $r>0$: $P(|X-\mu|\ge r)\le\sigma^2/r^2$; con $r=k\sigma$, al più $1/k^2$ di probabilità oltre $k$ deviazioni standard.

- Dimostrazione: Markov applicata a $(X-\mu)^2$ con $a=r^2$.
- Forma "almeno": $P(\mu-r<X<\mu+r)\ge1-\frac{\sigma^2}{r^2}$.
- $P(|X-\mu|>k\sigma)\le\frac1{k^2}$: entro $2\sigma$ almeno il 75%, entro $3\sigma$ almeno l'88,9% (per **qualunque** distribuzione).
- Esempio: $\mu=24$, $\sigma=2$, voti tra 21 e 27 → $k=1{,}5$, almeno il 56%.

## Collegamenti

- **Concetti correlati**: [[Disuguaglianza di Markov]] · [[Legge Debole dei Grandi Numeri]] · [[Variance]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[05 - PS - Disuguaglianze e Legge dei Grandi Numeri#Disuguaglianza di Chebyshev|Lezione 5 — Disuguaglianza di Chebyshev]]
> - [[05 - PS - Disuguaglianze e Legge dei Grandi Numeri#Forma con k deviazioni standard|Lezione 5 — Forma con k deviazioni standard]]
