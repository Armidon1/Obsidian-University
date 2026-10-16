---
title: Notazione Theta
tags:
  - modelli-di-calcolo
  - concetto
  - complessita
  - notazione-asintotica
---

# Notazione Theta

> [!summary] In breve
> $f \in \Theta(g)$ se $f \in O(g)$ e $f \in \Omega(g)$: esistono $c_1, c_2 > 0$ con $c_1 g(n) \le f(n) \le c_2 g(n)$ da un certo $n_0$ in poi. "$f$ e $g$ crescono nello stesso modo" (analisi **tight**).

$$\Theta(g(n)) = \{\, f \mid (\exists c_1, c_2 > 0)(\exists n_0)(\forall n \ge n_0)\ c_1 g(n) \le f(n) \le c_2 g(n) \,\}$$

- $\Theta$ è **simmetrica**: $f \in \Theta(g) \iff g \in \Theta(f)$.
- $\Theta(1) = O(1) \cap \Omega(1)$: tutti i costi costanti sono uguali.

> [!example] Esempio
> $2n^2 - 3n + 2 \in \Theta(n^2)$: per $n \ge 2$ vale $n^2 \le 2n^2 - 3n + 2 \le 3n^2$.

## Collegamenti

- **Concetti correlati**: [[Notazione O grande]] · [[Notazione Omega]] · [[Algoritmo ottimo]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[02 - MC - Notazione asintotica#Le notazioni O, Ω, Θ|Lezione 2 — Le notazioni O, Ω, Θ]]
> - [[02 - MC - Notazione asintotica#Esercizi svolti sulla notazione asintotica|Lezione 2 — Esercizi svolti sulla notazione asintotica]]
