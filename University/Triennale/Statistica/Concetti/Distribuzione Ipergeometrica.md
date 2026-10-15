---
title: Distribuzione Ipergeometrica
tags:
  - probabilita-e-statistica
  - concetto
  - distribuzioni
  - ipergeometrica
---

# Distribuzione Ipergeometrica

> [!summary] In breve
> Numero di palline bianche in $n$ estrazioni senza reinserimento da un'urna con $m$ bianche su $N$: $P(X=i)=\binom mi\binom{N-m}{n-i}/\binom Nn$.

Con $p=\frac mN$:
$$E[X]=np\qquad\mathrm{Var}(X)=np(1-p)\Big[1-\frac{n-1}{N-1}\Big]$$

- Somma di Bernoulli **dipendenti**: $E$ per linearità, $\mathrm{Var}$ con covarianze negative $\mathrm{Cov}(X_i,X_j)<0$.
- Per $N\to\infty$ (con $p$ fisso) tende alla binomiale.
- Se $X\sim B(n,p)$, $Y\sim B(m,p)$ indipendenti: $X\mid X+Y=k\sim H(n+m,n,k)$.

## Collegamenti

- **Concetti correlati**: [[Distribuzione Binomiale]] · [[Varianza della Somma]] · [[Combinazioni]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[06 - PS - Bernoulli, Binomiale, Ipergeometrica e Uniforme#Variabili aleatorie ipergeometriche|Lezione 6 — Variabili aleatorie ipergeometriche]]
> - [[06 - PS - Bernoulli, Binomiale, Ipergeometrica e Uniforme#Calcolo del valore atteso|Lezione 6 — Calcolo del valore atteso]]
> - [[06 - PS - Bernoulli, Binomiale, Ipergeometrica e Uniforme#Calcolo della varianza|Lezione 6 — Calcolo della varianza]]
> - [[06 - PS - Bernoulli, Binomiale, Ipergeometrica e Uniforme#Relazione tra binomiale e ipergeometrica|Lezione 6 — Relazione tra binomiale e ipergeometrica]]
