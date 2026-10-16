---
title: Principio di induzione
tags:
  - analisi-1
  - concetto
  - dimostrazioni
---

# Principio di induzione

> [!summary] In breve
> Per dimostrare A(n) per ogni n ≥ n₀ basta la base A(n₀) e il passo induttivo A(n) ⇒ A(n+1): è l'effetto domino.

1. **Base**: $A(n_0)$ è vera.
2. **Passo induttivo**: per ogni $n \ge n_0$, $A(n) \Rightarrow A(n+1)$.

Esempi classici del corso:
- $1 + 2 + \ldots + n = \frac{n(n+1)}{2}$;
- [[Disuguaglianza di Bernoulli]];
- somma geometrica $\sum_{k=0}^n q^k = \frac{1 - q^{n+1}}{1 - q}$.

> [!warning] Attenzione
> Il passo induttivo deve valere per **ogni** $n \ge n_0$: nel paradosso "tutti i cavalli sono bianchi" fallisce da $n = 1$ a $n = 2$.

## Collegamenti

- **Concetti correlati**: [[Disuguaglianza di Bernoulli]] · [[Serie geometrica]] · [[Dimostrazione per induzione]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[00 - AN1 - Concetti Fondamentali#Principio di Induzione|Lezione 0 — Principio di Induzione]]
> - [[00 - AN1 - Concetti Fondamentali#Dov'è l'errore? Tutti i cavalli sono bianchi|Lezione 0 — Dov'è l'errore? Tutti i cavalli sono bianchi]]
