---
title: Distribuzione Congiunta e Marginali
tags:
  - probabilita-e-statistica
  - concetto
  - variabili-aleatorie
  - distribuzione-congiunta
---

# Distribuzione Congiunta e Marginali

> [!summary] In breve
> La PMF congiunta $p(x,y)=P(X=x,Y=y)$ descrive due v.a. insieme; le marginali si ottengono sommando sull'altra variabile, ma non viceversa.

$$p_X(x)=\sum_yp(x,y)\qquad p_Y(y)=\sum_xp(x,y)$$

- In tabella: le marginali sono le somme di riga e di colonna.
- Dalle marginali **non** si ricava la congiunta, salvo indipendenza ($p(x,y)=p_X(x)p_Y(y)$).
- $E[g(X,Y)]=\sum_x\sum_yg(x,y)p(x,y)$.

## Collegamenti

- **Concetti correlati**: [[Variabili Aleatorie Indipendenti]] · [[Distribuzione Condizionale]] · [[Funzione di Massa di Probabilità]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[03 - PS - Variabili Aleatorie Discrete#Variabili aleatorie bidimensionali|Lezione 3 — Variabili aleatorie bidimensionali]]
> - [[03 - PS - Variabili Aleatorie Discrete#Distribuzione congiunta per v.a. discrete|Lezione 3 — Distribuzione congiunta per v.a. discrete]]
