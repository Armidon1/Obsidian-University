---
title: Variabili Aleatorie Indipendenti
tags:
  - probabilita-e-statistica
  - concetto
  - variabili-aleatorie
  - indipendenza
---

# Variabili Aleatorie Indipendenti

> [!summary] In breve
> $X$ e $Y$ sono indipendenti se $P(X\in A,Y\in B)=P(X\in A)P(Y\in B)$ per ogni $A,B$; nel discreto, se la PMF congiunta è il prodotto delle marginali.

- Equivalenze: $F(a,b)=F_X(a)F_Y(b)$; nel discreto $p(x,y)=p_X(x)p_Y(y)$ per **ogni** $x,y$.
- Per dimostrare la dipendenza basta **una** coppia con $p(x,y)\ne p_X(x)p_Y(y)$.
- Conseguenze: $E[XY]=E[X]E[Y]$, $\mathrm{Cov}(X,Y)=0$, $\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)$.
- Se $X,Y$ indipendenti, anche $g(X)$ e $h(Y)$ lo sono.

## Collegamenti

- **Concetti correlati**: [[Eventi Indipendenti]] · [[Distribuzione Congiunta e Marginali]] · [[Coefficiente di Correlazione]]
- **Mappa**: [[MOC - Probabilità e Statistica]]

> [!info] Approfondimento
> - [[03 - PS - Variabili Aleatorie Discrete#Variabili aleatorie indipendenti|Lezione 3 — Variabili aleatorie indipendenti]]
