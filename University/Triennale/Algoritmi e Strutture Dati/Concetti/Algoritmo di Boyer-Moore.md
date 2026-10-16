---
title: Algoritmo di Boyer-Moore
tags:
  - algoritmi-e-strutture-dati
  - concetto
  - stringhe
  - pattern-matching
---

# Algoritmo di Boyer-Moore

> [!summary] In breve
> Confronta il pattern con il testo **da destra a sinistra** e, a ogni discordanza su un carattere $c$, salta allineando l'ultima occorrenza di $c$ nel pattern (o oltre $c$ se non c'è): spesso esamina solo una frazione del testo.

- Euristica **looking-glass**: confronti da destra a sinistra.
- Euristica **character-jump** con $\text{last}(c)$ = indice dell'ultima occorrenza di $c$ nel pattern (−1 se assente):
  $$i \mathrel{+}= m - \min(k,\ 1 + \text{last}(c)), \qquad k = m - 1$$
- `last` in una tabella hash: spazio $O(\min(m, |\Sigma|))$.
- Caso peggiore $O(nm)$ (testo `aaa…a`, pattern `baa…a`), ma su testo inglese circa 0,24 confronti per carattere; la versione completa è $O(n + m + |\Sigma|)$.

## Collegamenti

- **Concetti correlati**: [[Pattern matching su stringhe]] · [[Algoritmo di Knuth-Morris-Pratt]]
- **Mappa**: [[MOC - Algoritmi e Strutture Dati]]

> [!info] Approfondimento
> - [[13 - ASD - Elaborazione di testi#L'algoritmo di Boyer-Moore|Lezione 13 — L'algoritmo di Boyer-Moore]]
