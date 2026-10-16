---
title: Limite di funzione
tags:
  - analisi-1
  - concetto
  - limiti
---

# Limite di funzione

> [!summary] In breve
> lim_{x→c} f(x) = l se per ogni successione xₙ → c con xₙ ≠ c si ha f(xₙ) → l; equivalentemente con ε e δ. c deve essere punto di accumulazione del dominio.

$$\lim_{x\to c} f(x) = l \iff \forall (x_n) \subset X \setminus \{c\},\ x_n \to c:\ f(x_n) \to l$$
$$\iff \forall \varepsilon > 0\ \exists \delta > 0 : |f(x) - l| < \varepsilon \ \ \forall x \in X,\ 0 < |x - c| < \delta \quad (c, l \in \mathbb{R})$$

- Il valore $f(c)$ non conta.
- Esiste $\iff$ esistono uguali i limiti destro e sinistro.
- Per dimostrare che **non** esiste: due successioni con limiti diversi (es. $\frac{|x|}{x}$ in $0$).
- Composta: $\lim g(f(x)) = l$ se $f \to y_0$, $g \to l$ e $f \neq y_0$ vicino a $c$.
- In $\mathbb{R}^N$ si sostituisce il modulo con la norma: vedi [[Limite in più variabili]].

## Collegamenti

- **Concetti correlati**: [[Limite di successione]] · [[Funzione continua]] · [[Asintoti]] · [[Limite in più variabili]]
- **Mappa**: [[MOC - Analisi 1]]

> [!info] Approfondimento
> - [[03 - AN1 - Funzioni Reali di una Variabile Reale#Definizione di limite|Lezione 3 — Definizione di limite]]
> - [[03 - AN1 - Funzioni Reali di una Variabile Reale#Limite destro e sinistro|Lezione 3 — Limite destro e sinistro]]
> - [[12 - AN1 - Appendice#Definizione alternativa dei Limiti per Funzioni|Lezione 12 — Definizione alternativa dei Limiti per Funzioni]]
