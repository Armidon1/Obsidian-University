---
title: Dimostrazione per induzione
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - analisi
  - dimostrazioni
---

# Dimostrazione per induzione

> [!summary] In breve
> Per dimostrare $P(n)$ per ogni $n \ge n_0$ si prova il caso base e si mostra che, se vale per i valori più piccoli, vale anche per $n$.

1. **Base**: $P(n_0)$ (eventualmente più casi base).
2. **Passo induttivo**: assumendo $P(k)$ vero per ogni $k < n$, si dimostra $P(n)$.

Esempio: $\sum_{i=1}^n i = n(n+1)/2$. Base $n = 1$. Passo: $\sum_{i=1}^{n} i = \frac{(n-1)n}{2} + n = \frac{n(n+1)}{2}$.

Altre tecniche: **controesempio** (per smentire), **contrapposizione** e **assurdo**.

## Collegamenti

- **Concetti correlati**: [[Invariante di ciclo]] · [[Ricorsione]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[04 - ASD - Analisi di algoritmi#Dimostrare per induzione o mediante invariante di ciclo|Lezione 4 — Dimostrare per induzione o mediante invariante di ciclo]]
