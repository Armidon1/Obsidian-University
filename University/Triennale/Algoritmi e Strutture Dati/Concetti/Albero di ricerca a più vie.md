---
title: Albero di ricerca a più vie
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - alberi-di-ricerca
---

# Albero di ricerca a più vie

> [!summary] In breve
> Albero ordinato in cui un $d$-nodo ha $d \ge 2$ figli e $d-1$ chiavi ordinate che separano gli intervalli dei sottoalberi; un BST è il caso $d = 2$.

- Con chiavi $k_1 < \dots < k_{d-1}$ e $k_0 = -\infty$, $k_d = +\infty$, il sottoalbero $c_i$ contiene chiavi tra $k_{i-1}$ e $k_i$.
- Un albero con $n$ voci ha $n + 1$ nodi esterni.
- Ricerca: in ogni nodo si trova l'intervallo giusto (ricerca binaria nella mappa secondaria, $O(\log d)$) → $O(h \log d_{max})$.
- Casi particolari: [[Albero (2,4)|alberi (2,4)]], [[Albero (a,b)|alberi (a,b)]], [[B-albero|B-alberi]].

## Collegamenti

- **Concetti correlati**: [[Albero (2,4)]] · [[Albero (a,b)]] · [[B-albero]] · [[Albero di ricerca binario]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[11 - ASD - Alberi di ricerca#Alberi di ricerca a più vie|Lezione 11 — Alberi di ricerca a più vie]]
