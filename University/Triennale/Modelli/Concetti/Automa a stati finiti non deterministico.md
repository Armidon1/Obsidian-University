---
title: Automa a stati finiti non deterministico
tags:
  - modelli-di-calcolo
  - concetto
  - linguaggi-formali
  - automi
  - linguaggi-regolari
---

# Automa a stati finiti non deterministico

> [!summary] In breve
> ASF con $\delta_N: Q \times \Sigma \to 2^Q$: da uno stato, con un simbolo, si può andare in più stati (o in nessuno). Accetta se almeno uno degli stati raggiunti è finale. È equivalente all'ASF deterministico.

- **Costruzione per sottoinsiemi**: stati dell'ASFD = insiemi di stati dell'ASFND; iniziale $\{q_0\}$; da $T$ con $a$ si va in $\bigcup_{q \in T}\delta_N(q, a)$; finali gli insiemi che contengono un finale.
- Nel caso peggiore $2^k$ stati ($k$ = stati dell'ASFND): più compatto, non più potente.
- Grado di non determinismo: massimo numero di archi uscenti con lo stesso simbolo.

> [!example] Termina con 1
> ASFND $S \circlearrowleft_{0,1}$, $S \xrightarrow{1} T$ ($T$ finale) diventa l'ASFD $[S] \xrightarrow{1} [ST]$, $[ST] \xrightarrow{0} [S]$, con cappi $[S] \circlearrowleft_0$ e $[ST] \circlearrowleft_1$.

## Collegamenti

- **Concetti correlati**: [[Automa a stati finiti]] · [[Macchina di Turing non deterministica]]
- **Mappa**: [[MOC - Modelli di Calcolo]]

> [!info] Approfondimento
> - [[10 - MC - Automi a stati finiti ed espressioni regolari#Non determinismo|Lezione 10 — Non determinismo]]
> - [[10 - MC - Automi a stati finiti ed espressioni regolari#Equivalenza fra ASFND e ASFD|Lezione 10 — Equivalenza fra ASFND e ASFD]]
