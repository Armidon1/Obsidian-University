---
title: Macchina di Turing
tags:
  - modelli-di-calcolo
  - concetto
  - calcolabilita
  - macchina-di-turing
---

# Macchina di Turing

> [!summary] In breve
> Automa a stati finiti con un nastro illimitato di lettura/scrittura: $M = \langle \Sigma, \flat, K, q_0, F, \delta \rangle$ con $\delta: K \times \Sigma_\flat \to K \times \Sigma_\flat \times \{d, s, i\}$. È il modello di riferimento per la nozione di algoritmo.

- **Configurazione**: contenuto del nastro, posizione della testina, stato (stringa $\alpha q \beta$).
- **Trasduttrice**: calcola $f$ se $q_0 x \vdash^* x \flat q f(x)$ con $q \in F$.
- **Riconosce (decide)** $L$: si ferma sempre, in uno stato finale sse $x \in L$.
- **Accetta** $L$: si ferma in uno stato finale per tutte e sole le $x \in L$ (altrimenti può non fermarsi).

Varianti equivalenti: multinastro, non deterministica, nastro semi-infinito, alfabeto binario. Simula ed è simulata da una RAM a costi logaritmici in tempo polinomiale.

## Collegamenti

- **Concetti correlati**: [[Macchina di Turing multinastro]] · [[Macchina di Turing non deterministica]] · [[Macchina di Turing universale]] · [[Tesi di Church-Turing]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[08 - MC - Macchine di Turing e calcolabilità#Funzioni calcolabili secondo Turing|Lezione 8 — Funzioni calcolabili secondo Turing]]
> - [[08 - MC - Macchine di Turing e calcolabilità#Configurazioni e computazioni|Lezione 8 — Configurazioni e computazioni]]
> - [[08 - MC - Macchine di Turing e calcolabilità#Insiemi e linguaggi decidibili e semidecidibili|Lezione 8 — Insiemi e linguaggi decidibili e semidecidibili]]
