---
title: Macchina di Turing multinastro
tags:
  - modelli-di-calcolo
  - concetto
  - calcolabilita
  - macchina-di-turing
---

# Macchina di Turing multinastro

> [!summary] In breve
> MT con $k$ nastri e $k$ testine indipendenti: $\delta^{(k)}: K \times \Sigma_\flat^k \to K \times \Sigma_\flat^k \times \{d, s, i\}^k$. Una MT a un nastro la simula con rallentamento quadratico: $t$ passi in $O(t^2)$.

- Simulazione: un nastro con $2k$ **tracce** (le pari = i nastri, le dispari = marcatori delle testine); ogni passo costa la distanza fra i marcatori più lontani, $O(t)$.
- Alfabeto della macchina simulante: $O((2|\Sigma|)^k)$.
- Esempio: $xcx^R$ si riconosce in $O(n)$ con due nastri (il secondo usato come pila), in $O(n^2)$ con uno.
- ASF = MT a un nastro di sola lettura unidirezionale; automa a pila = MT a due nastri (input one-way + pila).

## Collegamenti

- **Concetti correlati**: [[Macchina di Turing]] · [[Automa a pila]] · [[Automa a stati finiti]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[08 - MC - Macchine di Turing e calcolabilità#MT multinastro (MTM)|Lezione 8 — MT multinastro (MTM)]]
