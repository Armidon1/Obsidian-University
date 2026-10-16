---
title: Chiusura transitiva e Floyd-Warshall
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - grafi
  - programmazione-dinamica
---

# Chiusura transitiva e Floyd-Warshall

> [!summary] In breve
> La chiusura transitiva $G^*$ ha un lato $(u,v)$ se in $G$ c'è un percorso da $u$ a $v$; Floyd-Warshall la calcola in $O(n^3)$ aggiungendo $(v_i, v_j)$ quando esistono $(v_i, v_k)$ e $(v_k, v_j)$, per $k = 1..n$.

```text
for k = 1..n:
  for ogni i ≠ k, j ≠ k, i ≠ j:
    if (vi, vk) e (vk, vj) ∈ G: aggiungi (vi, vj)
```

- Invariante: dopo la fase $k$ c'è $(v_i, v_j)$ ⇔ esiste un percorso con intermedi in $\{v_1..v_k\}$.
- Adatto alla matrice di adiacenze (anche di bit), semplice e con costanti piccole.
- Alternativa: $n$ DFS in $O(n(n + m))$, migliore sui grafi sparsi.

## Collegamenti

- **Concetti correlati**: [[Attraversamento in profondità (DFS)]] · [[Programmazione dinamica]] · [[Strutture dati per grafi]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[14 - ASD - Algoritmi per grafi#Chiusura transitiva|Lezione 14 — Chiusura transitiva]]
