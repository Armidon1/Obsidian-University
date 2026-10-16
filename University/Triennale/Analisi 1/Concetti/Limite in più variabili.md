---
title: Limite in più variabili
tags:
  - analisi-1
  - concetto
  - più-variabili
  - limiti
---

# Limite in più variabili

> [!summary] In breve
> lim_{x→c} f(x) = l in ℝᴺ si definisce con le successioni (o con ε–δ e la norma); poiché ci si avvicina a c in infiniti modi, restrizioni a curve diverse servono a dimostrare la non esistenza, le coordinate polari l'esistenza.

- **Non esistenza**: due curve per il punto con limiti diversi.
  - $\frac{xy}{x^2+y^2}$: lungo $y = mx$ vale $\frac{m}{1+m^2}$ (dipende da $m$).
  - $\frac{x^2y}{x^4+y^2}$: $0$ lungo le rette, $\frac12$ lungo $y = x^2$.
- **Esistenza** (in $(0,0)$): $|f(\rho\cos\vartheta, \rho\sin\vartheta) - l| \le g(\rho) \to 0$, con $g$ **indipendente da $\vartheta$**.
  - $\frac{2x^2y}{x^2+y^2} = 2\rho\cos^2\vartheta\sin\vartheta$, $|\cdot| \le 2\rho \to 0$.
- I limiti si definiscono solo al finito ($c \in \mathbb{R}^N$).

## Collegamenti

- **Concetti correlati**: [[Coordinate polari]] · [[Norma euclidea]] · [[Limite di funzione]] · [[Funzione continua]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[07 - AN1 - Funzioni di più Variabili - Limiti e Continuità#Limiti di Funzioni Reali di più Variabili Reali|Lezione 7 — Limiti di Funzioni Reali di più Variabili Reali]]
> - [[07 - AN1 - Funzioni di più Variabili - Limiti e Continuità#Una condizione per la non esistenza del limite|Lezione 7 — Una condizione per la non esistenza del limite]]
> - [[07 - AN1 - Funzioni di più Variabili - Limiti e Continuità#Coordinate polari e esistenza del limite|Lezione 7 — Coordinate polari e esistenza del limite]]
