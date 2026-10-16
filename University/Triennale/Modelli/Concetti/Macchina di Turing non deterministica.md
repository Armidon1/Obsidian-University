---
title: Macchina di Turing non deterministica
tags:
  - modelli-di-calcolo
  - concetto
  - calcolabilita
  - macchina-di-turing
  - complessita
---

# Macchina di Turing non deterministica

> [!summary] In breve
> MT con $\delta_N: K \times \Sigma_\flat \to \mathcal{P}(K \times \Sigma_\flat \times \{d, s, i\})$: più transizioni possibili. La computazione è un albero; accetta se **almeno un** ramo accetta.

- **Grado di non determinismo** $d$ = massimo numero di figli di un nodo.
- Stesso potere delle MT: la simulazione deterministica visita l'albero **in ampiezza** (in profondità potrebbe perdersi in un ramo infinito), $k$ passi in $O(k\,d^k)$.
- Asimmetria: accettare = esiste un ramo accettante; rifiutare = tutti i rami rifiutano.
- **NP** = linguaggi accettati da una MTND in tempo polinomiale. Simularla in tempo polinomiale è il problema **P vs NP**.

## Collegamenti

- **Concetti correlati**: [[Macchina di Turing]] · [[Classe NP]] · [[Automa a stati finiti non deterministico]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[08 - MC - Macchine di Turing e calcolabilità#MT non deterministiche (MTND)|Lezione 8 — MT non deterministiche (MTND)]]
> - [[14 - MC - Classi P e NP e NP-completezza#Macchine di Turing non deterministiche|Lezione 14 — Macchine di Turing non deterministiche]]
