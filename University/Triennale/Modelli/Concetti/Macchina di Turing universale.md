---
title: Macchina di Turing universale
tags:
  - modelli-di-calcolo
  - concetto
  - calcolabilita
  - macchina-di-turing
---

# Macchina di Turing universale

> [!summary] In breve
> Una MT $U$ che, ricevuta la descrizione $D_M$ di una macchina $M$ e un input $x$, simula $M$ su $x$: termina in uno stato finale se e solo se lo fa $M$. È un interprete, il modello teorico del calcolatore programmabile.

- $D_M$: per esempio la lista delle quintuple $q_i \# \sigma_j \# q_h \# \sigma_k \# t_l$.
- $q_{0U}\, D_M \# x \vdash^* \alpha\, q_{fU}\, \beta \iff q_0 x \vdash^* \alpha\, q_f\, \beta$.
- Interpretazioni: un **calcolatore** (programma + dati) o un **interprete**.
- Dimostra che la terminazione è **semi-decidibile**; può simulare anche se stessa.

## Collegamenti

- **Concetti correlati**: [[Macchina di Turing]] · [[Problema della fermata]] · [[Linguaggio semidecidibile]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[08 - MC - Macchine di Turing e calcolabilità#Macchina di Turing universale|Lezione 8 — Macchina di Turing universale]]
