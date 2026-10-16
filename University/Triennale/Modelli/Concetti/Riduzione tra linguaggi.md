---
title: Riduzione tra linguaggi
tags:
  - modelli-di-calcolo
  - concetto
  - calcolabilita
  - riduzioni
---

# Riduzione tra linguaggi

> [!summary] In breve
> $L_1$ si riduce a $L_2$ se esiste una funzione totale calcolabile $f$ con $x \in L_1 \iff f(x) \in L_2$. Così $L_1$ "non è più difficile" di $L_2$.

- Trasferisce ad $A$ l'**upper bound** di $B$ e a $B$ il **lower bound** di $A$ (se $A \le B$).
- **Indecidibilità**: $A$ indecidibile e $A \le B$ ⇒ $B$ indecidibile.
- Esempio di lower bound: ordinamento $\le$ convex hull (punti sulla parabola $y = x^2$) ⇒ convex hull $\Omega(n \log n)$.
- Se $f$ è calcolabile in tempo polinomiale si parla di [[Riduzione polinomiale]].

## Collegamenti

- **Concetti correlati**: [[Riduzione polinomiale]] · [[Problema della fermata]] · [[Delimitazioni superiori e inferiori]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[05 - MC - Delimitazioni superiori e inferiori#Riduzioni|Lezione 5 — Riduzioni]]
> - [[07 - MC - Halting Problem#Riduzioni|Lezione 7 — Riduzioni]]
> - [[14 - MC - Classi P e NP e NP-completezza#Riduzione fra linguaggi|Lezione 14 — Riduzione fra linguaggi]]
