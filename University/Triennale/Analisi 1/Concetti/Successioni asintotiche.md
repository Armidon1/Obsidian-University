---
title: Successioni asintotiche
tags:
  - analisi-1
  - concetto
  - limiti
---

# Successioni asintotiche

> [!summary] In breve
> aₙ ∼ bₙ se aₙ/bₙ → 1; nei prodotti e nei rapporti si può sostituire una quantità con una asintotica (principio di sostituzione), ma non nelle somme.

$$a_n \sim b_n \iff \frac{a_n}{b_n} \to 1 \qquad (\text{per funzioni: } f \sim g \iff \tfrac fg \to 1)$$

- $\sim$ è una relazione di equivalenza; quantità asintotiche hanno lo stesso comportamento.
- **Principio di sostituzione**: $\frac{a_n b_n}{c_n} \sim \frac{a_n' b_n'}{c_n'}$.
- Un polinomio è asintotico al termine di grado massimo: $2n^3 - 5n^2 + 11 \sim 2n^3$.
- $f \sim g \iff f = g + o(g)$.

> [!warning] Non vale per somme, differenze e potenze
> $n + 1 \sim n$ e $-n \sim -n$, ma $(n + 1) - n = 1 \not\sim 0$; $\left(1 + \frac1n\right)^n \to e$ ma $1^n = 1$.

## Collegamenti

- **Concetti correlati**: [[Simbolo o-piccolo]] · [[Limite di successione]] · [[Criterio del confronto per le serie]] · [[Formula di Taylor]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[01 - AN1 - Successioni Numeriche#Confronto tra Successioni|Lezione 1 — Confronto tra Successioni]]
> - [[05 - AN1 - Calcolo Differenziale#Calcolo dei limiti con Taylor|Lezione 5 — Calcolo dei limiti con Taylor]]
