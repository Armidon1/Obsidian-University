---
title: Integrale di Riemann
tags:
  - analisi-1
  - concetto
  - integrali
---

# Integrale di Riemann

> [!summary] In breve
> f è integrabile su [a, b] se il sup delle somme inferiori coincide con l'inf delle somme superiori; il valore comune è ∫ₐᵇ f(x) dx, l'area con segno sotto il grafico.

$$s(f, P) = \sum m_i \Delta x_i \le \int_a^b f(x)\,dx \le S(f, P) = \sum M_i \Delta x_i$$

- Criterio: integrabile $\iff$ $\forall \varepsilon\ \exists P : S(f, P) - s(f, P) < \varepsilon$.
- Integrabili: funzioni continue, monotone, limitate con finite discontinuità. Non integrabile: Dirichlet.
- Proprietà: linearità, monotonia, $\left|\int f\right| \le \int |f|$, additività negli estremi ($\int_\alpha^\beta = -\int_\beta^\alpha$).
- Area geometrica: $\int_a^b |f|$; tra due grafici: $\int_a^b |f - g|$.

## Collegamenti

- **Concetti correlati**: [[Teorema fondamentale del calcolo integrale]] · [[Teorema della media integrale]] · [[Integrale improprio]] · [[Integrale doppio]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[06 - AN1 - Calcolo Integrale#Integrale, definizione e prime proprietà|Lezione 6 — Integrale, definizione e prime proprietà]]
> - [[06 - AN1 - Calcolo Integrale#Quali funzioni sono integrabili|Lezione 6 — Quali funzioni sono integrabili]]
> - [[06 - AN1 - Calcolo Integrale#Calcolo di Aree Piane|Lezione 6 — Calcolo di Aree Piane]]
